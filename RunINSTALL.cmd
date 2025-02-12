@echo off
setlocal enabledelayedexpansion

:: 設置顏色代碼
set "RED=[91m"
set "GREEN=[92m"
set "YELLOW=[93m"
set "RESET=[0m"

echo Checking Python installation...

:: 檢查 Python 是否安裝
python --version >nul 2>&1
if errorlevel 1 (
    echo %RED%Python is not installed!%RESET%
    echo %YELLOW%Would you like to download Python now? (Y/N)%RESET%
    choice /c yn /n
    if errorlevel 2 (
        echo Installation cancelled.
        pause
        exit /b 1
    ) else (
        echo Opening Python download page...
        start https://www.python.org/downloads/
        echo %GREEN%Please install Python and run this script again.%RESET%
        echo %YELLOW%Make sure to check 'Add Python to PATH' during installation!%RESET%
        pause
        exit /b 1
    )
)

:: 檢查 pip 是否可用
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo %RED%Pip is not available!%RESET%
    echo %YELLOW%Would you like to install pip now? (Y/N)%RESET%
    choice /c yn /n
    if errorlevel 2 (
        echo Installation cancelled.
        pause
        exit /b 1
    ) else (
        echo Installing pip...
        python -m ensurepip --default-pip
        if errorlevel 1 (
            echo %RED%Failed to install pip.%RESET%
            echo Please install pip manually or reinstall Python.
            start https://pip.pypa.io/en/stable/installation/
            pause
            exit /b 1
        )
    )
)

echo %GREEN%Python and pip are properly installed.%RESET%
echo Installing required packages...

:: 使用 python -m pip 代替直接使用 pip
python -m pip install requests
python -m pip install base58
python -m pip install bit
python -m pip install hdwallet
python -m pip install rich
python -m pip install pycoin

echo %GREEN%All packages installed successfully!%RESET%
echo %YELLOW%Running the program...%RESET%
python Pro2WordTrial_c.py
pause
