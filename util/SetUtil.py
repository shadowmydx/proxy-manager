# -*- coding: utf-8 -*-
__author__ = 'shadowmydx'


class SetUtil:
    
    @staticmethod
    def merge_set(input_set):
        result = dict()
        for key in input_set:
            result[key] = True
        return [item for item in result]