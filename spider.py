#!/usr/bin/env python
# -*- coding:utf-8 -*-

import download
import json

class Spider(object):
    def __init__(self):
        self.down = download.Download()

    def get_dic(self,kw,eng='0'):
        url = 'https://fanyi.so.com/index/search?query={kw}&eng={eng}'.format(kw=kw,eng=eng)
        response = self.down.get_html(url)
        if response:

            json_obj = json.loads(response.text)
            fanyi = json_obj['data']['fanyi']
            phonetic = ''
            translation = ''
            try:
                phonetic = json_obj['data']['explain']['phonetic']
                translation = json_obj['data']['explain']['translation']
            except:
                pass
            # obj = {
            #     'fanyi':{'翻译':fanyi},
            #     'phonetic':{'发音':phonetic},
            #     'translation':{'其他':translation},
            # }
            obj = {
                'fanyi':  fanyi,
                'phonetic': str(phonetic).replace('{','').replace('}',''),
                'translation':str(translation).replace('{','').replace('}',''),
            }
            return obj
        else:
            return False
