#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 17:38
# @Author  : Z
# @Email   : S
# @File    : 11.0lambda.py
#匿名函数 lambda 变量：表达式
g=lambda x,y,z:x+y+z
print g(1,2,3)
g=lambda x,y,z=0:x+y+z
print g(1,2)
print (lambda x,y,z=0:x+y+z)(1,2)
#在map函数中使用lambda函数
print map(lambda x:x*x,range(10))
print list(map(lambda x:x*x,range(10)))
#map使用
def add(a,b):
    return a+b
print map(add,range(10),range(10))
#reduce函数-累计求和
print reduce(add,range(10))