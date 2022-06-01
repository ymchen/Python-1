#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: YiMin-Chan|cyimin@tianjianpro.com
# @Date:   2022-05-24 10:19:22
# @version:  1.0.0
# @filename:  二进制数据文件初始化
# @file_path:  D:\ChenYiMin\TJFJ\PYTHON_EXP1\Python-1\1.二进制文件操作\二进制数据文件初始化.py
# @Last Modified by:   YiMin-Chan
# @Last Modified time: 2022-06-01 10:27:59
import pickle

F = open("studrec.dat", "wb")
lista = [[1, 'biancaa', 100.0]
, [2, 'Biancaa', 100.0]
, [3, 'binkoo', 100.0]
, [4, 'chenym', 23],[5, 'nini', 63]]

pickle.dump(lista, F)
F.close()
