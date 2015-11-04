# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import socket
import threading
import random
from util.Logger import Logger
from Interface import Interface
__author__ = 'shadowmydx'


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
            Logger.log(str(tmp_chunck))
            if len(tmp_chunck) == 0:
                break
            s.sendall(tmp_chunck)
        Logger.log('end')
        while True:
            tmp_chunck = s.recv(1024)
            Logger.log(str(tmp_chunck))
            if len(tmp_chunck) == 0:
                break
            self.clientsocket.sendall(tmp_chunck)        

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
    server = ProxyServer()
    server.setDaemon(True)
    server.start()
    while True:
        pass