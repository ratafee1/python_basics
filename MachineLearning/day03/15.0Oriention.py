#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 18:01
# @Author  : Z
# @Email   : S
# @File    : 15.0Oriention.py
class Arithmatic(object):
    def __init__(self,X,Y):
        self.NewX=X
        self.NewY=Y
    def add(self):
        return self.NewX+self.NewY
    def sub(self):
        return self.NewX-self.NewY
    def mul(self):
        return self.NewX*self.NewY
    def div(self):
        return self.NewX/self.NewY
#类-对象
input1=input("please input your A number:")
input2=input("please input your B number:")
arith=Arithmatic(input1,input2)
print arith.add()
print arith.sub()
print arith.mul()
print arith.div()