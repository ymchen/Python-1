#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: YiMin-Chan|cyimin@tianjianpro.com
# @Date:   2022-05-24 09:44:06
# @version:  1.0.0
# @filename:  �������ļ����¼�¼
# @file_path:  D:\ChenYiMin\TJFJ\PYTHON_EXP1\Python-1\1.�������ļ�\�������ļ����¼�¼.py
# @Last Modified by:   YiMin-Chan
# @Last Modified time: 2022-05-24 10:46:40
# updating records in a bnary file

import pickle


def update():
    F = open("studrec.dat", "rb+")
    value = pickle.load(F)
    found = 0
    roll = int(input("����������:"))
    for i in value:
        if roll == i[0]:
            print("����", i[1])
            print("�÷�", i[2])
            i[1] = input("��������")
            i[2] = int(input("����÷�"))
            found = 1

    if found == 0:
        print("��¼δ�ҵ�!")

    else:
        F.seek(0)
        pickle.dump(value, F)
    F.close()


update()


F = open("studrec.dat", "rb")
val = pickle.load(F)
print(val)
F.close()
