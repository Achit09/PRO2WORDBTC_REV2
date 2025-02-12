#!/bin/bash

# 更新系統
sudo apt-get update && sudo apt-get upgrade -y

# 安裝 Python 套件
pip3 install requests base58 bit hdwallet rich pycoin

# 運行程式
python3 Pro2WordTrial_c.py
