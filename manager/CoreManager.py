# -*- coding: utf-8 -*-
import threading
import Queue
from dao.DataUtil import DataUtil
from util.SetUtil import SetUtil
__author__ = 'shadowmydx'


class CoreManager(threading.Thread):

    manager_instance = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.cmd_queue = Queue.Queue()

    @staticmethod
    def get_single_instance():
        if CoreManager.manager_instance is None:
            CoreManager.manager_instance = CoreManager()
        return CoreManager.manager_instance
    
    def send_cmd(self, cmd, sender):
        self.cmd_queue.put((cmd, sender))
    
    def run(self):
        while True:
            cmd, sender = self.cmd_queue.get()
            if cmd == 'exit':
                break
            self.execute_cmd(cmd, sender)

    # Command Type：
    # 0. Send proxy IP to who ask one.
    # 1. Boost up specify module to collect proxy IP online.
    # 2. Refresh bad proxy IP
    # 3. Delete bad proxy IP
    def execute_cmd(self, cmd, sender):
        if cmd.startswith('request'):
            self.execute_request(cmd, sender)
            
    def execute_request(self, cmd, sender):
        cmd_array = cmd.split(' ')
        result = list()
        if len(cmd_array) < 2:
            return
        dao = DataUtil.get_single_instance()
        for i in xrange(1, len(cmd_array)):
            options = cmd_array[i].split(',')
            tmp_res = dao.search_proxy_item_by_fields((options[0], options[1]), options[2])
            result.append(tmp_res)
        result = SetUtil.merge_set(result)
        sender.recieve(result)
