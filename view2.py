#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
from db import MysqlClient
import config
import spider
import time
import json

class InputFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.word = StringVar()
        self.mean = StringVar()
        self.createPage()
        self.mysqlClient = MysqlClient()
        self.spider = spider.Spider()

    def createPage(self,query_res={'fanyi':'','phonetic':'','translation':''}):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='请输入: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.word,width=40).grid(row=2, stick=W)

        Label(self, text='结果如下: ').grid(row=4,stick=W, pady=10)
        Label(self, text=query_res['fanyi'],height=2,width=40,justify = 'left').grid(row=5, stick=W, pady=10)
        Label(self, text=query_res['phonetic'],height=2,width=40,justify = 'left').grid(row=6, stick=W, pady=10)
        Label(self, text=query_res['translation'],height=2,width=40,justify = 'left').grid(row=7, stick=W, pady=10)
        # Entry(self, textvariable=self.mean).grid(row=3, column=1, stick=E)
        # Text(self, height=5, width=50).grid(row=4, column=1, stick=W)

        Button(self, text='查询',command=self.query_word).grid(row=10, column=1, stick=E, pady=10)
        Button(self, text='收藏',command=self.collect_word).grid(row=10, column=2, stick=E, pady=10)

    def query_word(self):
        #插入到历史查询记录
        word = self.word.get()

        eng = '1'
        # 是中文
        if '\u4e00' <= word[0] <= '\u9fff':
            eng = '0'
        query_res = self.spider.get_dic(word,eng=eng)
        self.createPage(query_res)

        #添加到历史查询记录
        name = config.USERNAME
        mean = json.dumps(query_res['fanyi'])
        mytime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        timestamp = int(time.time())
        sql = "insert into history(word,mean,name,time,timestamp) values('%s','%s','%s','%s','%s')"%(word,mean,name,mytime,timestamp)
        print(sql)
        self.mysqlClient.save(sql)

    def collect_word(self):
        word = self.word.get()

        eng = '1'
        # 是中文
        if '\u4e00' <= word[0] <= '\u9fff':
            eng = '0'
        query_res = self.spider.get_dic(word, eng=eng)
        self.createPage(query_res)

        # 添加到我的收藏
        name = config.USERNAME
        mean = json.dumps(query_res)
        mytime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        timestamp = int(time.time())
        sql = "insert into collection(word,mean,name,time,timestamp) values('%s','%s','%s','%s','%s')" % (
        word, mean, name, mytime, timestamp)
        save_res = self.mysqlClient.save(sql)
        if save_res:
            showinfo(title='成功', message='收藏成功')
        else:
            showinfo(title='失败', message='收藏失败！')

#历史查询
class QueryFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.mysqlClient = MysqlClient()
        # self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='单词名称').grid(row=1, column=1, stick=W, pady=10)
        Label(self, text='查询时间').grid(row=1, column=2, stick=W, pady=10)
        results = self.get_history()

        row_num = 2
        for res in results:
            Label(self, text='      ').grid(row=row_num, column=1, stick=W, pady=10)
            Label(self, text='      ').grid(row=row_num, column=2, stick=W, pady=10)
            row_num += 1

        row_num = 2
        for res in results:
            word = res[1]
            time = res[2]
            Label(self, text=word).grid(row=row_num, column=1, stick=W, pady=10)
            Label(self, text=time).grid(row=row_num, column=2, stick=W, pady=10)
            row_num +=1

    def get_history(self):
        name = config.USERNAME
        sql = "select * from history where(name='%s') order by id DESC limit 5"%(name)
        mysqlClient = MysqlClient()
        find_res = mysqlClient.find_all(sql)
        return find_res


#我的收藏
class CountFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.mysqlClient = MysqlClient()
        # self.createPage()


    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='单词名称').grid(row=1, column=1, stick=W, pady=10)
        Label(self, text='收藏时间').grid(row=1, column=2, stick=W, pady=10)
        Label(self, text='释义').grid(row=1, column=3, stick=W, pady=10)
        results = self.get_collection()

        row_num = 2
        for res in results:
            word = res[2]
            mean = res[3]
            time = res[4]
            Label(self, text=word).grid(row=row_num, column=1, stick=W, pady=10)
            Label(self, text=time).grid(row=row_num, column=2, stick=W, pady=10)
            Label(self, text=mean).grid(row=row_num, column=3, stick=W, pady=10)
            row_num += 1

    def get_collection(self):
        name = config.USERNAME
        sql = "select * from collection where(name='%s') order by id DESC limit 5" % (name)
        mysqlClient = MysqlClient()
        find_res = mysqlClient.find_all(sql)
        return find_res

class AboutFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self, text='关于').pack()
