@echo off
<<<<<<< HEAD
echo Checking Python installation...

:: 檢查 Python 是否安裝
python --version >nul 2>&1
if errorlevel 1 (
    echo [31mPython is not installed![0m
    echo [33mWould you like to download Python now? (Y/N)[0m
    choice /c yn /n
    if errorlevel 2 (
        echo Installation cancelled.
        pause
        exit /b 1
    ) else (
        echo Opening Python download page...
        start https://www.python.org/downloads/
        echo [32mPlease install Python and run this script again.[0m
        echo [33mMake sure to check 'Add Python to PATH' during installation![0m
        pause
        exit /b 1
    )
)

:: 檢查 pip 是否可用
py -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [31mPip is not available![0m
    echo [33mWould you like to install pip now? (Y/N)[0m
    choice /c yn /n
    if errorlevel 2 (
        echo Installation cancelled.
        pause
        exit /b 1
    ) else (
        echo Installing pip...
        python -m ensurepip --default-pip
        if errorlevel 1 (
            echo [31mFailed to install pip.[0m
            echo Please install pip manually or reinstall Python.
            start https://pip.pypa.io/en/stable/installation/
            pause
            exit /b 1
        )
    )
)

echo [32mPython and pip are properly installed.[0m
echo Installing required packages...

:: 使用 python -m pip 代替直接使用 pip
python -m pip install requests
python -m pip install base58
python -m pip install bit
python -m pip install hdwallet
python -m pip install rich
python -m pip install pycoin

echo [32mAll packages installed successfully![0m
echo [33mRunning the program...[0m
=======
echo Installing required packages...

pip install requests
pip install base58
pip install bit
pip install hdwallet
pip install rich
pip install pycoin

echo Running the program...
>>>>>>> 9a40a0a9eb3e2705cb48a7443bd7e86791b76a7d
python Pro2WordTrial_c.py
pause
