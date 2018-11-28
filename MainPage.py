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
        self.inputPage = InputFrame(self.root)  # 创建不同Frame
        self.queryPage = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)
        self.inputPage.pack()  # 默认显示查询界面

        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        fileMenu = Menu(menubar)

        menubar.add_cascade(label="菜单", menu=fileMenu)

        fileMenu.add_command(label='查询单词', command=self.inputData)
        fileMenu.add_command(label='查询历史记录', command=self.queryData)
        fileMenu.add_command(label='我的收藏', command=self.countData)
        fileMenu.add_command(label='注销', command=self.logout)
        fileMenu.add_command(label='退出', command=self.inputPage.quit)
        # fileMenu.add_command(label='关于', command=self.aboutDisp)


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
        login = LoginPage.LoginPage(self.root)

