1.在系统环境变量中增加 WORKON_HOME键，其值设置为venv
2.添加.env文件，设置FLASK_ENV,SECRET_KEY,DATABASE_URI
3.pipenv install --dev 创建虚拟环境和下载依赖包
4.vscode的"设置"中查找 "python.pythonPath" 修改为虚拟环境中的python地址
5.pipenv shell  激活虚拟环境
# 调试代码
6.ctrl+F5调试
# 运行代码
6.flask run 运行
