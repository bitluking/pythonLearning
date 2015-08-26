#coding:utf-8
#list 集合
#list集合中元素可以不是一类的数据类型。广义的集合？

classMates = ['john','conna','jenna']

#获取list的长度
print len(classMates),'\n'


#在末尾追加元素
classMates.append('luke')
print classMates,'\n'

#在末尾弹出元素
classMates.pop()
print classMates,'\n'

#在指定位置插入元素
classMates.insert(0,'zeus')
print classMates,'\n'

#删除指定位置的元素
classMates.pop(0)
print classMates,'\n'

#在list中插入非字符串元素
classMates[1] = 1
print classMates,'\n'
