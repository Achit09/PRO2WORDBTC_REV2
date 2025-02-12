#!/bin/bash

# 清理之前的構建
echo "Cleaning previous builds..."
rm -rf build dist

# 安裝依賴
echo "Installing requirements..."
pip install -r requirements.txt

# 運行打包
echo "Building application..."
python setup.py py2app

echo "Build complete! The application is in the dist folder." 