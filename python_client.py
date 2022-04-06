#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import base64
import time

dir = 'test.jpg'
# read floor plan image as base64
with open(dir, 'rb') as f:
    base64_data = base64.b64encode(f.read())
    s = base64_data.decode()
    data = 'data:image/jpeg;base64,%s' % s
    # print(data)


# call house parser service to get json result
# you should change the 'xxx' to your account (contact universe.will@gmail.com to buy an account)
paras = {'image':(None, data), 'user_name':(None, 'xxx'), 'password':(None, 'xxx')}
ret = requests.post('http://222.67.185.0:9595/house_parser_json', files=paras)

print('house parser json result:')
print(ret.text)
