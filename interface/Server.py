# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import socket
import threading
import random
import httplib
from util.Logger import Logger
from Interface import Interface
from BaseHTTPServer import BaseHTTPRequestHandler
from cgi import parse_header, parse_multipart
__author__ = 'shadowmydx'


class HttpConnection:

    version_dict = {11: 'HTTP/1.1'}

    def __init__(self):
        self.proxy = ('127.0.0.1', 8087)

    def connect(self, method, url, request_header):
        conn = httplib.HTTPConnection(self.proxy[0], self.proxy[1])
        if request_header:
            conn.request(method, url, headers=request_header)
        else:
            conn.request(method, url)
        response = conn.getresponse()
        print self.version_dict[response.version], response.status, response.reason
        print str(response.msg)
        print len(response.read())

class HttpHandler(BaseHTTPRequestHandler):

    # def do_METHOD(self):
    #     print '\r\n'.join([str(self.command) + ' ' + str(self.path) + ' ' + str(self.request_version), str(self.headers)])
    #     self.send_response(200)
    #     self.end_headers()
    #     self.wfile.write('hello world')

    def parse_body(self):
        try:
            ctype, pdict = parse_header(self.headers['content-type'])
            if ctype == 'multipart/form-data':
                postvars = parse_multipart(self.rfile, pdict)
            elif ctype == 'application/x-www-form-urlencoded':
                length = int(self.headers['content-length'])
                postvars = parse_qs(
                        self.rfile.read(length), 
                        keep_blank_values=1)
            else:
                postvars = {}
            return postvars
        except:
            return None    

    def do_GET(self):
        print '\r\n'.join([str(self.command) + ' ' + str(self.path) + ' ' + str(self.request_version), str(self.headers)])
        self.body = self.parse_body()
        self.send_response(200)
        self.end_headers()
        self.wfile.write('hello world')

    def do_POST(self):
        print '\r\n'.join([str(self.command) + ' ' + str(self.path) + ' ' + str(self.request_version), str(self.headers)])
        self.send_response(200)
        self.end_headers()
        self.wfile.write('hello world')

    def do_CONNECT(self):
        print '\r\n'.join([str(self.command) + ' ' + str(self.path) + ' ' + str(self.request_version), str(self.headers)])
        self.send_response(200)
        self.end_headers()
        self.wfile.write('hello world')

    def do_PUT(self):
        print '\r\n'.join([str(self.command) + ' ' + str(self.path) + ' ' + str(self.request_version), str(self.headers)])
        self.send_response(200)
        self.end_headers()
        self.wfile.write('hello world')

    def do_HEAD(self):
        print '\r\n'.join([str(self.command) + ' ' + str(self.path) + ' ' + str(self.request_version), str(self.headers)])
        self.send_response(200)
        self.end_headers()
        self.wfile.write('hello world')

    def do_OPTIONS(self):
        print '\r\n'.join([str(self.command) + ' ' + str(self.path) + ' ' + str(self.request_version), str(self.headers)])
        self.send_response(200)
        self.end_headers()
        self.wfile.write('hello world')

    def do_DELETE(self):
        print '\r\n'.join([str(self.command) + ' ' + str(self.path) + ' ' + str(self.request_version), str(self.headers)])
        self.send_response(200)
        self.end_headers()
        self.wfile.write('hello world')

    def do_TRACE(self):
        print '\r\n'.join([str(self.command) + ' ' + str(self.path) + ' ' + str(self.request_version), str(self.headers)])
        self.send_response(200)
        self.end_headers()
        self.wfile.write('hello world')

class Handler(threading.Thread):
    
    def __init__(self, clientsocket, proxy_ip):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        Logger.log(clientsocket)
        self.proxy_ip = proxy_ip
    
    def run(self):
        data_chunck = u''
        rec_data = 0
        s = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        s.connect(self.proxy_ip)
        while True:
            tmp_chunck = self.clientsocket.recv(1024)
            s.sendall(tmp_chunck)
            data_chunck += str(tmp_chunck)
            if data_chunck.find('\r\n\r\n') != -1:
                Logger.log(data_chunck)
                break
        Logger.log('end')
        data_chunck = u''
        while True:
            tmp_chunck = s.recv(1024)
            self.clientsocket.sendall(tmp_chunck)
            data_chunck += str(tmp_chunck)
            border = data_chunck.find('\r\n\r\n')
            if border != -1:
                Logger.log(data_chunck)
                break
        Logger.log('end2')

class ProxyServer(Interface):
    
    def __init__(self):
        Interface.__init__(self)
        self.port = 7890
        self.ip_addresses = [('127.0.0.1', 8087)]
        
    def run(self): 
        serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('127.0.0.1', self.port))
        serversocket.listen(5)
        while True:
            (clientsocket, address) = serversocket.accept()
            Logger.log(address)
            ct = Handler(clientsocket, random.choice(self.ip_addresses))
            ct.start()
        
if __name__ == '__main__':
    # server = ProxyServer()
    # server.setDaemon(True)
    # server.start()
    # while True:
    #     pass

    # from BaseHTTPServer import HTTPServer
    # server = HTTPServer(('localhost', 7890), HttpHandler)
    # Logger.log('Starting server at 7890')
    # server.serve_forever()

    h = HttpConnection()
    h.connect('GET', 'http://www.zhihu.com', None)