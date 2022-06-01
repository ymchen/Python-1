#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: YiMin-Chan|cyimin@tianjianpro.com
# @Date:   2022-05-24 09:37:24
# @version:  1.0.0
# @filename:  二进制文件搜索记录
# @file_path:  D:\ChenYiMin\TJFJ\PYTHON_EXP1\Python-1\1.二进制文件操作\二进制文件搜索记录.py
# @Last Modified by:   YiMin-Chan
# @Last Modified time: 2022-06-01 10:28:07
import pickle

def binary_search():
    F = open("studrec.dat", "rb")
    # your file path will be different
    value = pickle.load(F)
    search = 0
    rno = int(input("输入查询序号:"))

    for i in value:
        if i[0] == rno:
            print("Record found successfully")
            print(i)
            search = 1

    if search == 0:
        print("Sorry! record not found")
    F.close()


binary_search()
