#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: YiMin-Chan|cyimin@tianjianpro.com
# @Date:   2022-05-23 14:26:47
# @version:  1.0.0
# @filename:  二进制文件读取
# @file_path:  D:\ChenYiMin\TJFJ\PYTHON_EXP1\Python-1\1.二进制文件操作\二进制文件读取.py
# @Last Modified by:   YiMin-Chan
# @Last Modified time: 2022-06-01 10:27:38
import pickle
def binaryread():
    B = open("studrec.dat", "rb")
    stud = pickle.load(B)
    print(stud)

    # prints the whole record in nested list format
    print("contents of binary file")

    for ch in stud:
        Rno = ch[0]
        Rname = ch[1]  # due to unpacking the val not printed in list format
        Rmark = ch[2]
        print(Rno, Rname, Rmark, end="\n")
        B.close
binaryread()
