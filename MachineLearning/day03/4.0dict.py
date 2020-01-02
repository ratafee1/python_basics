#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 16:16
# @Author  : Z
# @Email   : S
# @File    : 4.0dict.py
#定义
d1={"apple":1,"banana":2}
print d1
#zip函数
d2=dict(zip(["apple","banana"],[1,2]))
print d2
#dict函数
d3=dict(apple=1,banana=2)
print d3
#字典的删除
# del d2
# print d2 #NameError: name 'd2' is not defined
#字典的清空
d2.clear()
print d2
#字典中key必须是具有hash值的类型----这种类型必须是不可变的类型---tuple
# print hash([1,2,3]) #TypeError: unhashable type: 'list'
# print hash((1,3,4))
d3={["Apple"]:"pear",1:"pear"}
print d3 #TypeError: unhashable type: 'list'
d4={("apple","pear"):"pear",1:"pear"}
print d4
#key不能重复
d5={"apple":1,"pear":2,"apple":3}
print d5