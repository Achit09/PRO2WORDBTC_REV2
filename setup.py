from setuptools import setup

APP = ['Pro2WordTrial_c.py']
DATA_FILES = ['README.md']
OPTIONS = {
    'argv_emulation': True,
    'packages': [
        'requests',
        'base58',
        'bit',
        'hdwallet',
        'rich',
        'pycoin'
    ],
    'plist': {
        'CFBundleName': 'BitcoinAddressGenerator',
        'CFBundleDisplayName': 'Bitcoin Address Generator',
        'CFBundleVersion': '1.0.0',
        'CFBundleIdentifier': 'com.achit09.bitcoinaddressgenerator',
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
) 