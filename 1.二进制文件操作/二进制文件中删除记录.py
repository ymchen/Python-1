#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: YiMin-Chan|cyimin@tianjianpro.com
# @Date:   2022-05-23 14:23:02
# @version:  1.0.0
# @filename:  二进制文件中删除记录
# @file_path:  D:\ChenYiMin\TJFJ\PYTHON_EXP1\Python-1\1.二进制文件\二进制文件中删除记录.py
# @Last Modified by:   YiMin-Chan
# @Last Modified time: 2022-05-24 10:43:38
import pickle


def Bdelete():
    # 打开数据文件 & 加载
    F = open("studrec.dat", "rb")
    stud = pickle.load(F)
    F.close()

    print(stud)

    # 接受需要删除的序号
    rno = int(input("删除输入对应的序号: "))
    F = open("studrec.dat", "wb")
    rec = []
    for i in stud:
        if i[0] == rno:
            continue
        rec.append(i)
    pickle.dump(rec, F)
    F.close()


Bdelete()