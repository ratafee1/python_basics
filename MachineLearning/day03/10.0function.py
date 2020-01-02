#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 17:22
# @Author  : Z
# @Email   : S
# @File    : 10.0function.py
#参数、、返回值
# 没有参数没有返回值
def SayHi():
    print "Hello"*5
SayHi()
SayHi()
# 有参数没有返回值
def addThreeNumber(a,b,c):
    print a+b+c
addThreeNumber(1,2,3)
# 没有参数有返回值
def SayHello():
    return  "chuanzhi"*5
item=SayHello()
print item
# 有参数 有返回值
def addNumber(X,Y):
    return X+Y
result=addNumber(1,2)
print result

#全局变量和局部变量
X=60
def print_Function(X):
    print "current X value is:",X
    X=100
    print 'change X value is:',X
print_Function(X)
print "Final X value is:",X

Y=60
def print_Function2():
    global  Y
    print "current Y is:",Y
    Y=200
    print "change Y is:",Y
print_Function2()
print "Final X result is:",Y