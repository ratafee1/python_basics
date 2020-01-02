#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 16:08
# @Author  : Z
# @Email   : S
# @File    : 3.0tuple.py
#只有一个元素的tuple
t1=(1000,)
print t1
print type(t1)
#如果tuple中存在list部分
t2=(1,2,3,4,["apple","pear"])
print t2
print t2[4]
print t2[4][0]
t2[4][1]="orange"
print t2
#各个数据类型之间的转换
t3=tuple([1,2,3,4])
t4=tuple({1,2,3,4})
t5=tuple({"Apple":1,"pear":2})
print t3
print t4
print t5
#切片操作
t6=tuple(range(10))
print t6
print t6[::-1]
print t6[0:8]
#list----->tuple 冻结
#tuple-----》list 解冻

#多元素赋值-序列解包
a,b=1,2
print a,b
v=(1,2)
(a,b)=v
print a,b
