#!/usr/bin/env python
# -*- coding:utf-8 -*-

#mysql配置
MYSQL_HOST = 'localhost'
MYSQL_DB = 'dictionary'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'
MYSQL_CHARSET = 'utf8'


#当前请求次数
REQUEST_NUM = 0

USERNAME = ''

#请求多少次后换IP配置
CHANGE_IP = 0

#代理IP
IP = ''

START_URL = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={datetime}&leftTicketDTO.from_station={start}&leftTicketDTO.to_station={end}&purpose_codes=ADULT'


#是否开启代理
PROXY_SWITCH = False
#是否使用cookies
COOKIES_SWITCH = False
#请求最大出错次数
ERROR_MAX = 3

#请求头配置
HEADERS = {
    'connection': "keep-alive",
    'cache-control': "max-age=0",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}
