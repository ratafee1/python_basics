#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 16:57
# @Author  : Z
# @Email   : S
# @File    : 8.0tupleDERIVE.py
#[表达式 for 元素 in 可迭代对象中 if 条件 ]
#(表达式 for 元素 in 可迭代对象中 if 条件 )
#实现：x*x
t1= (x*x for x in range(10))
print type(t1)
print t1.next() #在Python3中next()方法改成了__next__方法
print t1.next()
print t1.next()
print list(t1)
print list(t1)