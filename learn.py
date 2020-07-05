# -*- Coding: utf-8 -*-
# Author: Yu

## 该程序将字符串进行倒序
## 先将字符串转化为列表list，方便后续进行倒序
n = "hello"
Newlist = []
for i in n:
    Newlist.append(i)

result = ''  ## 设置一个空字符串，后续来接受列表里面的数字
n = 4  ## 循环四次，从Newlist[4]开始读取，这样就可以倒序

while n >= 0:  ## 每次减一，直到小于0，就不循环了
    result = result + Newlist[n]  ## 装成字符串 比如第一次循环： ''+'o' = 'o'
    n = n -1
