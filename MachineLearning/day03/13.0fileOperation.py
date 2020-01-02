#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 17:51
# @Author  : Z
# @Email   : S
# @File    : 13.0fileOperation.py
def writeFile():
    content = '''\
This is jupyter!
This is AnacondA!
This is MachineLearning!\
'''
    f = open("sen.txt", mode="w")
    f.writelines(content)
    f.close()

def readFile():
    f = open("sen.txt", mode="r")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,

if __name__=="__main__":
    # writeFile()
    readFile()




