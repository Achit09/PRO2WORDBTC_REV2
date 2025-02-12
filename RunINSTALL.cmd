@echo off
echo Installing required packages...

pip install requests
pip install base58
pip install bit
pip install hdwallet
pip install rich
pip install pycoin

echo Running the program...
python Pro2WordTrial_c.py
pause
