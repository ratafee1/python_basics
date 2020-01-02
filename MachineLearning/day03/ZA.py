#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 18:06
# @Author  : Z
# @Email   : S
# @File    : ZA.py
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