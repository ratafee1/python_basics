#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 15:37
# @Author  : Z
# @Email   : S
# @File    : 2.0listOperation.py
#list创建[]
l1=[1,2,3,4]
#如果在Python3下面实践在range前面添加list函数
l2=list(range(10)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l2)
#其他三种数据结构能否转化为list
l3=list((1,2,3,4))
print l3
print type(l3)
# [1, 2, 3, 4]
# <type 'list'>
l4=list({"apple":1,"pear":2})
print l4
print type(l4)
l5=list({"apple":1,"pear":2}.values())
print l5 #[2, 1]
l6=list({"apple":1,"pear":2}.items())
print l6 #[('pear', 2), ('apple', 1)]

#切片操作[start:stop:step]
l7=range(10)
print l7
#取值
print l7[0:]
print l7[1:]
print l7[1:4] #1, 2, 3, 4
print l7[0:9]
print l7[-2]
print l7[::-1]
print l7[::2] #[0, 2, 4, 6, 8]
print l7[1::2] #[1, 3, 5, 7, 9]