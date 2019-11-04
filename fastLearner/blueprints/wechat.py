from flask import Blueprint,request
import hashlib
from lxml import etree

we_bp=Blueprint('wechat',__name__)
WE_TOKEN='1T3ET5IwzEA0Y4yrwvXukZin9cB_7mkXgVjWGKqsLJXDmiFUC'

@we_bp.route('/wx',methods=['GET'])
def getWechat():
    #接收到微信服务器的请求后，取出参数signature,timestamp,echostr,nonce
    signature = request.args.get('signature','')
    timestamp = request.args.get('timestamp','')
    echostr = request.args.get('echostr','success')
    nonce = request.args.get('nonce','')
    # 把token、timestamp、nonce进行字典排序，CONFIG.token换为你自己的token就好
    arr = [WE_TOKEN, timestamp, nonce]
    arr.sort()
    print(arr)
    # sha1加密
    arr.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, arr)
    result = sha1.hexdigest()
    print(result)
    #此处校验方式不正确，待确认
    # 与signature对比后返回结果
    # if(result == signature):
    #     print('success')
    #     return echostr
    # else:
    #     return 'error'
    return echostr

@we_bp.route('/wx',methods=['POST'])
def postWechat():
    str_xml = request.get_data()
    print(str_xml)
    xml = etree.fromstring(str_xml)
    #xml = urllib.unquote(xml)
    mstype=xml.find("MsgType").text 
    fromUser=xml.find("FromUserName").text
    toUser=xml.find("ToUserName").text
    fromTime=xml.find('CreateTime').text
    XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
    if(mstype=='text'):
        data=xml.find('Content').text  
        content='我记下了，你得内容是:{0}'.format(data)
        dict={'ToUserName':fromUser,'FromUserName':toUser,'CreateTime':fromTime,'Content':content}
        return XmlForm.format(**dict)
    elif(mstype=='event'):
        eventName=xml.find('Event').text
        print(eventName)
        content='欢迎进入公众号，相见恨晚啊'
        dict={'ToUserName':fromUser,'FromUserName':toUser,'CreateTime':fromTime,'Content':content}
        return XmlForm.format(**dict)
    else:
        dict={'ToUserName':fromUser,'FromUserName':toUser,'CreateTime':fromTime,'Content':'别闹'}
        return XmlForm.format({**dict})