#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 17:57
# @Author  : Z
# @Email   : S
# @File    : 14.0exception.py
# print 2/0 #ZeroDivisionError
# hello*4 #NameError: name 'hello' is not defined
try:
    # print 2/0 #ZeroDivisionError
    hello*4 #NameError: name 'hello' is not defined
except:
    print "div 0 exception!"

try:
    hello*2222

except:
    print 'sss'
