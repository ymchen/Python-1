#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: YiMin-Chan|cyimin@tianjianpro.com
# @Date:   2022-05-23 11:16:51
# @version:  1.0.0
# @filename:  login_密码登录
# @file_path:  D:\ChenYiMin\TJFJ\PYTHON_EXP1\Python-1\login_密码登录.py
# @Last Modified by:   YiMin-Chan
# @Last Modified time: 2022-05-23 11:21:06
import os
from getpass import getpass
# This is Logo Function
def logo():
    print(" ──────────────────────────────────────────────────────── ")
    print(" |                                                        | ")
    print(" |   ########    ##  #########  ##       ##      ###      | ")
    print(" |   ##     ##   ##  ##         ##       ##    ##   ##    | ")
    print(" |   ##     ###  ##  ##         ##       ##   ##     ##   | ")
    print(" |   ##     ###  ##  #########  ###########  ##########   | ")
    print(" |   ##     ###  ##         ##  ##       ##  ##      ##   | ")
    print(" |   ##     ##   ##         ##  ##       ##  ##      ##   | ")
    print(" |   ########    ##  #########  ##       ##  ##      ##   | ")
    print(" |                                                        | ")
    print(" \033[1;91m|   || Digital Information Security Helper Assistant ||  | ")
    print(" |                                                        | ")
    print(" ──────────────────────────────────────────────────────── ")
    print("\033[1;36;49m")


# This is Login Funtion
def login():
    # for clear the screen
    os.system("clear")
    print("\033[1;36;49m")
    logo()
    print("\033[1;36;49m")
    print("")
    usr = input("Enter your Username : ")
    # This is username you can change here
    usr1 = "chenym"
    psw = getpass("Enter Your Password : ")
    # This is Password you can change here
    psw1 = "123456"
    if usr == usr1 and psw == psw1:
        print("\033[1;92mlogin successfully")
        print("\033[1;36;49m")
        logo()
    else:
        print("\033[1;91m Wrong")

        login()


# This is main function
if __name__ == "__main__":
    login()
