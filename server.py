#-*-coding:utf-8-*-
#从wsgiref 模块导入
from wsgiref.simple_server import make_server
#导入我们自己编写的application 函数
from hello import application
#创建一个服务器，ip为空，端口为8000，处理函数为application
httpd=make_server('',8000,application)
print "Serving HTTP on port 8000...."
#开始监听HTTP 请求
httpd.serve_forever()