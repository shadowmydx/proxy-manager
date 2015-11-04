# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import threading
import Queue
from manager.CoreManager import CoreManager
__author__ = 'shadowmydx'


class Interface(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.resp_queue = Queue.Queue()
        
    def recieve(self, result):
        self.resp_queue.put(result)
        
    def send_cmd(self, cmd):
        CoreManager.get_single_instance().send_cmd(cmd, self)
