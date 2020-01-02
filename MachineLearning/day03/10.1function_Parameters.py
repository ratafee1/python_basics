#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 17:31
# @Author  : Z
# @Email   : S
# @File    : 10.1function_Parameters.py
#默认参数
def SayHello(name,age=12):
    print "name is:{},age is {}".format(name,age)
SayHello("lisi")
SayHello("lisi",13)
#关键字参数
def addThreeNumber(a,b,c):
    print a+b+c
addThreeNumber(1,2,3)
addThreeNumber(a=1,b=2,c=3)
addThreeNumber(1,2,c=3)
addThreeNumber(b=1,c=2,a=3)
#VarArgs参数-*tuple **dict
def printFunction(fparameters,*tuple1,**dict1):
    print fparameters
    print tuple1
    print dict1
printFunction(1,2,3,3,45,name="zhangsan",age=90)