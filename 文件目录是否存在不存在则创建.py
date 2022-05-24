#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: YiMin-Chan|cyimin@tianjianpro.com
# @Date:   2022-05-23 17:13:00
# @version:  1.0.0
# @filename:  文件目录是否存在不存在则创建
# @file_path:  D:\ChenYiMin\TJFJ\PYTHON_EXP1\Python-1\文件目录是否存在不存在则创建.py
# @Last Modified by:   YiMin-Chan
# @Last Modified time: 2022-05-23 17:13:21
import os  # Import the OS module

MESSAGE = "The directory already exists."
TESTDIR = "testdir"
try:
    home = os.path.expanduser(
        "~"
    )  # Set the variable home by expanding the user's set home directory
    print(home)  # Print the location

    if not os.path.exists(
        os.path.join(home, TESTDIR)
    ):  # os.path.join() for making a full path safely
        os.makedirs(
            os.path.join(home, TESTDIR)
        )  # If not create the directory, inside their home directory
    else:
        print(MESSAGE)
except Exception as e:
    print(e)
