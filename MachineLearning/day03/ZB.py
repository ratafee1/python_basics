#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 18:06
# @Author  : Z
# @Email   : S
# @File    : ZB.py
from ZA import Arithmatic
#类-对象
input1=input("please input your A number:")
input2=input("please input your B number:")
arith=Arithmatic(input1,input2)
print arith.add()
print arith.sub()
print arith.mul()
print arith.div()