#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: YiMin-Chan|cyimin@tianjianpro.com
# @Date:   2022-05-24 10:19:22
# @version:  1.0.0
# @filename:  �����������ļ���ʼ��
# @file_path:  D:\ChenYiMin\TJFJ\PYTHON_EXP1\Python-1\1.�������ļ�\�����������ļ���ʼ��.py
# @Last Modified by:   YiMin-Chan
# @Last Modified time: 2022-05-24 10:46:46
import pickle

F = open("studrec.dat", "wb")
lista = [[1, 'biancaa', 100.0]
, [2, 'Biancaa', 100.0]
, [3, 'binkoo', 100.0]
, [4, 'chenym', 23],[5, 'nini', 63]]

pickle.dump(lista, F)
F.close()
