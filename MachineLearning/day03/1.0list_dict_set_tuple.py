#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 15:20
# @Author  : Z
# @Email   : S
# @File    : 1.0list_dict_set_tuple.py
#1.list列表-异质数据，有序，根据下标进行查询
#1.1list创建
l1=[1,2,3,4]
print l1
print type(l1)
l2=[1,2,3,4,"chuanzhi"]
print l2
# [1, 2, 3, 4]
# <type 'list'>
l3=[1,2,3,4,"chuanzhi",[8,9,10]]
print l3
#1.2list查询
print l1[0]
print l3[5][0]
#1.3list增加元素
l3.append("banana")
print l3
#1.4list删除元素
l3.remove("banana")
print "l3 element remove:",l3
del l3[0]
print "l3 element remove:",l3
#1.5list删除列表
# del l3
# print l3 #NameError: name 'l3' is not defined
#3.tuple元祖-异质数据，有序，根据下标进行查询,数据一定确定不能进行删除、更新、修改等操作
#1.1tuple创建
t1=(1,2,3,4,"china")
print t1
print type(t1)
#1.2tuple查询
print t1[0]
#1.3tuple增加元素-TypeError: 'tuple' object does not support item assignment
# t1[0]="apple"
# print t1
#1.4tuple删除元素-TypeError: 'tuple' object doesn't support item deletion
# del t1[0]
#1.5tuple删除元祖-NameError: name 't1' is not defined
# del t1
# print t1
#4.dict字典--无序类型的、通过key查询数据的数据结构
#1.1dict创建
d1={"apple":1,"pear":2,3:"banana"}
print d1
print type(d1)
#1.2dict查询
print d1["apple"]
#1.3dict增加元素
d1["orange"]=100
print d1
#1.4dict删除元素
del d1["orange"]
print d1
#1.5dict删除列表NameError: name 'd1' is not defined
# del d1
# print d1
#2.set集合
#1.1set创建
s1={1,2,3,4}
print s1
print type(s1)
#1.2set查询
#1.3set增加元素
#1.4set删除元素
#1.5set删除列表
