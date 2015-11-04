# -*- coding: utf-8 -*-
import sqlite3
__author__ = 'shadowmydx'


class DataUtil:

    util_instance = None

    def __init__(self):
        self.db = None
        self.conn = None

    @staticmethod
    def get_single_instance():
        if DataUtil.util_instance is None:
            DataUtil.util_instance = DataUtil()
        return DataUtil.util_instance

    def set_db(self, db):
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.init_db()

    def insert_proxy_item(self, item):
        sql = '''
            insert into proxy values (
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s'
            );
        ''' % item
        self.conn.execute(sql)
        self.conn.commit()

    # fields: (field, value)
    def search_proxy_item_by_fields(self, fields, is_equal):
        sql = '''
            select *
            from proxy
            where %s = '%s'
        ''' % fields
        sql = sql.replace('=', is_equal)
        result = self.conn.execute(sql)
        return [row for row in result]

    # ip_address: (ip_address, port)
    def delete_proxy_item(self, ip_address):
        sql = '''
            delete from proxy
            where ip_address='%s' and port='%s'
        ''' % ip_address
        self.conn.execute(sql)
        self.conn.commit()

    # conditions: [(fields, new, old), ...]
    def update_proxy_item_by_conditions(self, conditions):
        sql = '''
            update proxy
            set [fields]
            where [olds]
        '''
        fields = [item[0] for item in conditions]
        new_val = [item[1] for item in conditions]
        old_val = [item[2] for item in conditions]
        sql = sql.replace('[fields]', ','.join([str(fields[i]) + "='" + str(new_val[i]) + "'" for i in range(len(fields))]))
        sql = sql.replace('[olds]', ' and '.join([str(fields[i]) + "='" + str(old_val[i]) + "'" for i in range(len(fields))]))
        self.conn.execute(sql)
        self.conn.commit()

    def init_db(self):
        sql = '''
            create table proxy (
                ip_address  TEXT,
                port TEXT,
                speed TEXT,
                area TEXT,
                effect TEXT,
                anonymous TEXT,
                type TEXT
            );
        '''
        try:
            self.conn.execute(sql)
            self.conn.commit()
        except sqlite3.OperationalError:
            pass

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    item = [('ip_address', '345.132.123.123', '123.123.123.123'), ('port', '8080', '80')]
    test = [('123.123.123.123', '80', '100', 'china', 'true', 'true', 'http'),
            ('123.123.123.127', '80', '100', 'china', 'true', 'true', 'https')
            ]
    util = DataUtil()
    util.set_db('test.db')
    # for key in test:
    #     util.insert_proxy_item(key)
    print util.search_proxy_item_by_fields(('type', 'https'), '=')
    util.update_proxy_item_by_conditions(item)
    print util.search_proxy_item_by_fields(('type', 'http'), '=')
    util.delete_proxy_item(('123.123.123.127', '80'))
    print util.search_proxy_item_by_fields(('type', 'https'), '=')
    util.close()


