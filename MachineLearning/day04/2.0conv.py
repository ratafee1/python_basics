#-*- coding: utf-8 -*-
# @Time    : 2018/9/29 15:04
# @Author  : Z
# @Email   : S
# @File    : 2.0conv.py
#定义卷积
import scipy as sp
print(sp.convolve([1,2,3,4],[4,5,6]))
# [ 4 13 28 43 38 24]

def convDemo(lst1,lst2):
    length1=len(lst1)
    length2=len(lst2)
    lst1.reverse()
    result=[]
    for  i in range(1,length1+1):
        t=lst1[length1-i:]   #str1=[1,2,3]  str2=[4,5,6,7]
        #len(str1)=3 i=1, 3-1=2下标 str1=[1,2,（3）]
        #len(str1)=3 i=2, 3-2=1下标 str1=[1,（2,3）]
        #len(str1)=3 i=3, 3-3=0下标 str1=[（1,2,3）]
        re1=sum([item1*item2 for item1,item2 in zip(t,lst2)])
        result.append(re1)
    for i in range(1,length2):
        t=lst2[i:]
        re2=sum([item1*item2 for item1,item2 in zip(lst1,t)])
        result.append(re2)
    return result
result=convDemo([1,2,3,4],[4,5,6])
print(result)