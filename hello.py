#-*-coding:utf-8-*-
#hello.py

def application(environ,start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return '<h1>hello,%s!</h1>'% (environ ['PATH_INFO'][1:] or 'web')

