#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: YiMin-Chan|cyimin@tianjianpro.com
# @Date:   2022-05-24 09:44:06
# @version:  1.0.0
# @filename:  二进制文件更新记录
# @file_path:  D:\ChenYiMin\TJFJ\PYTHON_EXP1\Python-1\1.二进制文件\二进制文件更新记录.py
# @Last Modified by:   YiMin-Chan
# @Last Modified time: 2022-05-24 10:46:40
# updating records in a bnary file

import pickle


def update():
    F = open("studrec.dat", "rb+")
    value = pickle.load(F)
    found = 0
    roll = int(input("输入更新序号:"))
    for i in value:
        if roll == i[0]:
            print("姓名", i[1])
            print("得分", i[2])
            i[1] = input("输入姓名")
            i[2] = int(input("输入得分"))
            found = 1

    if found == 0:
        print("记录未找到!")

    else:
        F.seek(0)
        pickle.dump(value, F)
    F.close()


update()


F = open("studrec.dat", "rb")
val = pickle.load(F)
print(val)
F.close()
