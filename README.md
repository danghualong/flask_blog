1.新建.venv文件夹
2.pipenv install --dev 创建虚拟环境和下载依赖包
#运行方法1
3.打开app.py，新建.vscode和settings.json
4.创建launch.json,增加pythonPath节点
5.ctrl+F5调试
#运行方法2
3.添加.env文件，设置FLASK_APP和FLASK_ENV
4.pipenv shell  激活虚拟环境
5.flask run 运行
