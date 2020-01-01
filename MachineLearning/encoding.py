# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 23:41
# @Author  : Z
# @Email   : S
# @File    : encoding.py
# import sys
#
# print("python3 encoding:", sys.getdefaultencoding())
#
# str = "世界"
# encode = str.encode()
# print(encode)  # b'\xe4\xb8\x96\xe7\x95\x8c'
# print(b'\xe4\xb8\x96\xe7\x95\x8c'.decode())
# print(str.encode('gbk'))  # b'\xca\xc0\xbd\xe7'
# print(b'\xca\xc0\xbd\xe7'.decode('gbk'))
#
# import os
#
# print(os.getcwd()) #D:\PycharmProject\MachineLearning
# os.chdir("D:\\PycharmProject")
# print(os.getcwd())
#
# import requests
#
# get = requests.get("http://www.baidu.com")
# print(get.encoding)
# print(get.text)
# print(get.url)
#
# import math
# print(math.sin(10))
#
# from math import sin
# print(sin(10))
#
# from math import sin as f
# print(f(10))
#
# import numpy as np
#
# rand = np.random.rand()
# print(rand)
# a = 123
# print(type(a))
# print(id(a))
# b = 112
# c = 112
# print(id(112))
# print(id(b))
# print(id(c))
# print(complex(1,2))
# print(complex(1,2)**2)
# print(3**3)
# print(6//3)
# a=3
# b=5
# a+=b
# a**=b
# print(a)
# a=5 #0101
# b=3 #0011
# print(a|b) #0111
# print(a&b) #0001
# print(a^b) #0110
# print(a<<1)
# a="pear"
# b='apple'
# c='''\
# this is an apple!
# this is my love!
# this is last tiime!\
# '''
# print(a)
# print(b)
# print(c)
#
# print(78)
# print(3.14e2)
# print(3.14e-2)

# import random
# print(random.random())
# print(random.randint(1,10))
# print(random.randrange(1,10,2))
# X=[1,2,3,4]
# random.shuffle(X)
# print(X)
#
# import numpy as np
#
# randn = np.random.randn(4, 4)
# print(randn)
# np.random.rand(3,3)

# s = int(input("please input your name:"))
# print(s)
# print(type(s))

# name="zhangsan"
# age=12
# print("name:",name,"age",age)
# print("name:"+str(name)+"age"+str(age))
# print("name:{},age:{}".format(name,age))
# print("name:{0},age:{1}".format(name,age))
# print("name:%s,age:%d"%(name,age))

# for i in range(10):
#     print(i,end=" ")
