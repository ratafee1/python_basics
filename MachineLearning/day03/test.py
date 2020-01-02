#-*- coding: utf-8 -*-
# @Time    : 2020/1/2 11:54
# @Author  : Z
# @Email   : S
# @File    : test.py
# import operator
# a =2
# b=3
# print(operator.lt(a, b))
# operator.le(a, b)
# operator.eq(a, b)
# operator.ne(a, b)
# operator.ge(a, b)
# operator.gt(a, b)
# operator.__lt__(a, b)
# operator.__le__(a, b)
# operator.__eq__(a, b)
# operator.__ne__(a, b)
# operator.__ge__(a, b)
# operator.__gt__(a, b)

# print ord('a')
# print [x*x for x in range(10)]
# vec=[[1,2,3],[4,5,6],[7,8,9]]
# print [num*ele for ele in vec for num in ele]
# arr=[1,2,3,4,0,-1,-3,-100,100]
# print [num for num in arr if num>50]
#
# print [(x,y) for x in range(10) for y in range(10) if x!=y]
# print [[row[i] for row in vec ]for i in range(3)]
# t1=zip([1,2,3],[4,5,6],[7,8,9])
# print t1
# print zip(*vec)
# print "--------------------"
# print map(list,t1)
# a =[1,2,3]
# print type(a)
#
# print [p for p in range(2,101) if 0 not in [p%q for q in range(2,p)]]

# def sayHi():
#     print "hello"*5
#
# sayHi()
#
# def addThreeNumber(a,b,c):
#     print a+b+c
#
# addThreeNumber(1,4,7)
#
# def sayHello():
#     return "hel"*5
#
#
# hello = sayHello()
# print hello
#
# def addNumber(x,y):
#     return x+y
#
# num=addNumber(5,7)
# print num



#全局变量和局部变量
# X=60
# def print_Function(X):
#     print "current X value is:",X
#     X=100
#     print 'change X value is:',X
# print_Function(X)
# print "Final X value is:",X
#
# Y=60
# def print_Function2():
#     global  Y
#     print "current Y is:",Y
#     Y=200
#     print "change Y is:",Y
# print_Function2()
# print "Final X result is:",Y
#
# x=20
# def print_x(x):
#     print x
#     x=30
#     print x
#
# y=11
# def print_y():
#     global y
#     print y
#     y=99
#     print y
#
#
# print_x(x)
# print x
# print_y()
# print y

# def sayHello(name,age=12):
#     print name,age
#
# sayHello('22',33)
#
# def addThreeNumber(a,b,c):
#     print a+b+c
# addThreeNumber(a=4,c=2,b=99)

# def printFunction(fparameters,*tuple1,**dict1):
#     print fparameters
#     print tuple1
#     print dict1
# printFunction(1,2,3,3,45,name="zhangsan",age=90)
#
# def print_tuple_anddict(a,*b,**c):
#     print a
#     print b
#     print c
#
# print_tuple_anddict(3,6,7,'8',4,name='abc',age=333)
#


# g=lambda x,y,z:x+y+z
#
# print g(2,5,7)
#
# g=lambda x,y,z=0:x+y+z
# print g(1,2)
#
# print (lambda x,y:x+y)(77,88)

# print map(lambda x:x*x,range(10))
# print list(map(lambda x:x*x,range(10)))
#

# def add(a,b):
#     return a+b
# # print map(add,range(10),range(99))
# print map(add,range(10),range(100))
#
# print reduce(add,range(10))

# def writeFile():
#     content='''
#     hello world
#     '''
#     a=open('a.txt',mode='w')
#     a.write(content)
#     a.close()
# def readFile():
#     while True:
#         a=open("sen.txt",mode='r')
#         a.readline()
#         if(len(a)==0):
#             break
#     a.close()
#
# writeFile()
# readFile()

x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""


def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2})
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})


func()