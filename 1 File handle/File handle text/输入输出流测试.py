#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: YiMin-Chan|cyimin@tianjianpro.com
# @Date:   2022-05-24 10:57:07
# @version:  1.0.0
# @filename:  �������������Ϣ
# @file_path:  D:\ChenYiMin\TJFJ\PYTHON_EXP1\Python-1\1 File handle\File handle text\�������������Ϣ.py
# @Last Modified by:   YiMin-Chan
# @Last Modified time: 2022-05-25 09:37:57
# practicing with streams
import sys

sys.stdout.write("Enter the name of the file")

#sys.stdout��python�еı�׼�������Ĭ����ӳ�䵽����̨�ģ�������Ϣ��ӡ������̨��
file = sys.stdin.readline()
print(file)
F = open(file.strip(), "r")
print(F.readlines())
while True:
    ch = F.readlines()
    for i in ch:
        print(i, end="")

F.close()
