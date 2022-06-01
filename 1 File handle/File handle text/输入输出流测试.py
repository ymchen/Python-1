#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: YiMin-Chan|cyimin@tianjianpro.com
# @Date:   2022-05-24 10:57:07
# @version:  1.0.0
# @filename:  输入输出错误信息
# @file_path:  D:\ChenYiMin\TJFJ\PYTHON_EXP1\Python-1\1 File handle\File handle text\输入输出错误信息.py
# @Last Modified by:   YiMin-Chan
# @Last Modified time: 2022-05-25 09:37:57
# practicing with streams
import sys

sys.stdout.write("Enter the name of the file")

#sys.stdout是python中的标准输出流，默认是映射到控制台的，即将信息打印到控制台。
file = sys.stdin.readline()
print(file)
F = open(file.strip(), "r")
print(F.readlines())
while True:
    ch = F.readlines()
    for i in ch:
        print(i, end="")

F.close()
