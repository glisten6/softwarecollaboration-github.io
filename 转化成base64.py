# -*- coding: utf-8 -*-
"""
Created on Mon May 16 20:26:53 2022

@author: 符磊fl
"""


import base64
f=open(r'D:\新建文件夹 (4)\1.jpg','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
print(ls_f)