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
# list tuple dict set
# l1 = [1, 2, 3, 4,"ok",[5,6,7]]
# print(l1)
# print(type(l1))
# print(l1[0])
# print(l1[5][2])
#
# l1.append("apple")
# print(l1)
# l1.remove("apple")
# print("l1 element remove",l1)
# del l1[0]
# print(l1)
# del l1
# print(l1)
# t1=(1,2,3,4,"ok")
# print(t1)
# print(type(t1))
# print(t1[0])
# print(t1)
# del t1
# d1={"apple":1,"pear":2,3:"banana"}
# print(d1)
# print(type(d1))
# print(d1["apple"])
# d1["orange"]=100
# print(d1)
# del d1["orange"]
# print(d1)
# del d1
# s1={1,2,3,4}
# print(s1)
# print(type(s1))
# l1 =[1,2,3,4]
# l2=list(range(10))
# print(l2)
# l3=list((1,2,3,4))
# print(l3)
# print(type(l3))
# l4=list({"apple":1,"pear":2})
# print(l4)
# print(type(l4))
# l5=list({'apple':1,'pear':2}.values())
# print(l5)
# print(type(l5))
# l6=list({'apple':1,'pear':2}.items())
# print(l6)
#
# l7=list(range(10))
# print(l7)
#
# print(l7[0:])
# print(l7[1:])
# print(l7[1:4])
# print(l7[-2])
# print(l7[::-2])
# z=zip([1, 2, 3], [4, 5, 6])
# for each in z:
#     print(each)
# print(dir(z))
# print(list(enumerate(range(10),5)))
