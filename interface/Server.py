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
from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer
__author__ = 'shadowmydx'


class HttpConnection:

    def __init__(self):
        pass

    class Connection(Interface):

        version_dict = {11: 'HTTP/1.1'}
        TIME_OUT = 10

        def __init__(self):
            Interface.__init__(self)
            self.proxy = ('127.0.0.1', 8087)

        def connect(self, method, url, request_header, request_body):
            conn = httplib.HTTPConnection(self.proxy[0], self.proxy[1])
            if request_header:
                if request_body:
                    conn.request(method, url, headers=request_header, body=request_body)
                else:
                    conn.request(method, url, headers=request_header)
            else:
                if request_body:
                    conn.request(method, url, body=request_body)
                else:
                    conn.request(method, url)
            response = conn.getresponse()
            if method == 'CONNECT':
                return self.version_dict[response.version], response.status, response.reason, response.msg, None
            return self.version_dict[response.version], response.status, response.reason, response.msg, response.read()

    connection_instance = Connection()

    @staticmethod
    def get_single_instance():
        return HttpConnection.connection_instance


class HttpHandler(BaseHTTPRequestHandler):

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
           
        try:
            body = self.parse_body()
            conn = HttpConnection.get_single_instance()
            headers = dict()
            for key in self.headers:
                headers[key] = self.headers[key]
            response_tuple = conn.connect(str(self.command), str(self.path), headers, body)
            self.send_response(response_tuple[1])
            try:
                for key in response_tuple[3]:
                    self.send_header(key, response_tuple[3][key])
            except:
                import traceback
                traceback.print_exc()
            self.end_headers()
            self.wfile.write(response_tuple[4])
        except:
            self.send_error(500)

    def do_POST(self):
        try:
            body = self.parse_body()
            conn = HttpConnection.get_single_instance()
            headers = dict()
            for key in self.headers:
                headers[key] = self.headers[key]
            response_tuple = conn.connect(str(self.command), str(self.path), headers, body)
            self.send_response(response_tuple[1])
            try:
                for key in response_tuple[3]:
                    self.send_header(key, response_tuple[3][key])
            except:
                import traceback
                traceback.print_exc()
            self.end_headers()
            self.wfile.write(response_tuple[4])
        except:
            self.send_error(500)

    def do_CONNECT(self):
        try:
            body = self.parse_body()
            conn = HttpConnection.get_single_instance()
            headers = dict()
            for key in self.headers:
                headers[key] = self.headers[key]
            response_tuple = conn.connect(str(self.command), str(self.path), headers, body)
            self.send_response(response_tuple[1])
            try:
                for key in response_tuple[3]:
                    self.send_header(key, response_tuple[3][key])
            except:
                import traceback
                traceback.print_exc()
            self.end_headers()
        except:
            import traceback
            traceback.print_exc()
            self.send_error(500)

    def do_PUT(self):
        try:
            body = self.parse_body()
            conn = HttpConnection.get_single_instance()
            headers = dict()
            for key in self.headers:
                headers[key] = self.headers[key]
            response_tuple = conn.connect(str(self.command), str(self.path), headers, body)
            self.send_response(response_tuple[1])
            try:
                for key in response_tuple[3]:
                    self.send_header(key, response_tuple[3][key])
            except:
                import traceback
                traceback.print_exc()
            self.end_headers()
            self.wfile.write(response_tuple[4])
        except:
            self.send_error(500)

    def do_HEAD(self):
        try:
            body = self.parse_body()
            conn = HttpConnection.get_single_instance()
            headers = dict()
            for key in self.headers:
                headers[key] = self.headers[key]
            response_tuple = conn.connect(str(self.command), str(self.path), headers, body)
            self.send_response(response_tuple[1])
            try:
                for key in response_tuple[3]:
                    self.send_header(key, response_tuple[3][key])
            except:
                import traceback
                traceback.print_exc()
            self.end_headers()
            self.wfile.write(response_tuple[4])
        except:
            self.send_error(500)

    def do_OPTIONS(self):
        try:
            body = self.parse_body()
            conn = HttpConnection.get_single_instance()
            headers = dict()
            for key in self.headers:
                headers[key] = self.headers[key]
            response_tuple = conn.connect(str(self.command), str(self.path), headers, body)
            self.send_response(response_tuple[1])
            try:
                for key in response_tuple[3]:
                    self.send_header(key, response_tuple[3][key])
            except:
                import traceback
                traceback.print_exc()
            self.end_headers()
            self.wfile.write(response_tuple[4])
        except:
            self.send_error(500)

    def do_DELETE(self):
        try:
            body = self.parse_body()
            conn = HttpConnection.get_single_instance()
            headers = dict()
            for key in self.headers:
                headers[key] = self.headers[key]
            response_tuple = conn.connect(str(self.command), str(self.path), headers, body)
            self.send_response(response_tuple[1])
            try:
                for key in response_tuple[3]:
                    self.send_header(key, response_tuple[3][key])
            except:
                import traceback
                traceback.print_exc()
            self.end_headers()
            self.wfile.write(response_tuple[4])
        except:
            self.send_error(500)

    def do_TRACE(self):
        try:
            body = self.parse_body()
            conn = HttpConnection.get_single_instance()
            headers = dict()
            for key in self.headers:
                headers[key] = self.headers[key]
            response_tuple = conn.connect(str(self.command), str(self.path), headers, body)
            self.send_response(response_tuple[1])
            try:
                for key in response_tuple[3]:
                    self.send_header(key, response_tuple[3][key])
            except:
                import traceback
                traceback.print_exc()
            self.end_headers()
            self.wfile.write(response_tuple[4])
        except:
            self.send_error(500)


class ThreadServer(ThreadingMixIn, HTTPServer):
    pass
        
if __name__ == '__main__':
    # server = ProxyServer()
    # server.setDaemon(True)
    # server.start()
    # while True:
    #     pass

    server = ThreadServer(('localhost', 7890), HttpHandler)
    Logger.log('Starting server at 7890')
    server.serve_forever()

    # h = HttpConnection.get_single_instance()
    # h.connect('GET', 'http://www.zhihu.com', None)