#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *
from view import *  # 菜单栏对应的各个子页面
import LoginPage



class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.index = Frame(self.root)
        Button(self.index, text='查询',command=self.inputData).pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(self.index, text='历史记录',command=self.queryData).pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(self.index, text='我的收藏',command=self.countData).pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(self.index, text='注销',command=self.logout).pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(self.index, text='退出',command=self.index.quit).pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.index.pack(side=LEFT, fill=BOTH, expand=YES)

        self.inputPage = InputFrame(self.root)  # 创建不同Frame
        self.queryPage = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)

        self.inputPage.pack(side=LEFT, padx=10)  # 默认显示查询界面


    def inputData(self):
        self.inputPage.pack()
        self.inputPage.createPage()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def queryData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack()
        self.queryPage.createPage()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def countData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack()
        self.countPage.createPage()
        self.aboutPage.pack_forget()

    def aboutDisp(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack()

    def logout(self):
        self.inputPage.destroy()
        self.queryPage.destroy()
        self.countPage.destroy()
        self.aboutPage.destroy()
        self.index.destroy()
        login = LoginPage.LoginPage(self.root)

