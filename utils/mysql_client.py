#!/usr/bin/python3
import time
import os, sys
import pymysql
import pymysql.cursors


class MysqlClient:

    def __init__(self):
        db = pymysql.connect(host='localhost',
                             user='USER',
                             password='PASSWORD',
                             db='DATABASE',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
        self.cursor = db.cursor()

    def insert(self, table, params):
        sql = "INSERT INTO %s(code) VALUES ('%s')" % (table, params)
        try:
            cursor.execute(sql)
            db.commit()
            except:
               db.rollback()

    def select_one(self, table, params):
        sql = "SELECT * FROM %s WHERE code = '%s'" % (params)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result

    def select_all(self, table, params):
        sql = "SELECT * FROM %s WHERE code = '%s'" % (params)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results







