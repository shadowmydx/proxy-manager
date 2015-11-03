# -*- coding: utf-8 -*-
import threading
import Queue
from dao.DataUtil import DataUtil
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

    def run(self):
        while True:
            cmd = self.cmd_queue.get()
            if cmd == 'exit':
                break
            self.execute_cmd(cmd)

    # Command Type：
    # 0. Send proxy IP to who ask one.
    # 1. Boost up specify module to collect proxy IP online.
    def execute_cmd(self, cmd):
        pass

