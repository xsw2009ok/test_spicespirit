#coding=utf-8
__author__ = 'Administrator'

import time as t
import MySQLdb

class Utils():

    '''默认静默1秒'''

    def wait(self,time=1):
        t.sleep(time)

    '''获取明天的时间'''

    def getTomorrowDate(m=86600):
        return t.strftime('%Y-%m-%d',t.localtime(t.time()+m))

    '''数据库地址，用户名，密码，数据库名称，sql语句'''

    def execSelectSql(localhost,user,passwd,dbname,sql):
        result = []
        db = MySQLdb.connect(host=localhost,user=user,passwd=passwd,db=dbname,charset='utf8')
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        try:
            data = cursor.execute(sql)

            for i in cursor.fetchall():
                result.append(i)
        except:
            db.close()
        db.close()
        return result

    '''数据库地址，用户名，密码，数据库名称，sql语句'''

    def execInsertSql(localhost,user,passwd,dbname,sql):
        db = MySQLdb.connect(host=localhost,user=user,passwd=passwd,db=dbname,charset='utf8')
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()

if __name__ == '__name__':
    Utils()