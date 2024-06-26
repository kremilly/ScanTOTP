#!/usr/bin/python3

from classes.startup import Startup

if __name__ == '__main__':
    Startup('E.g.: python scantotp -a qrcode -m file -i qrcode.png', [
        {'short': 'm', 'long': 'mode', 'help': 'Mode of scan', 'required': True},
        {'short': 'i', 'long': 'input', 'help': 'Input of QR Code', 'required': False},
        {'short': 'w', 'long': 'webcam', 'help': 'Select a webcam', 'default': '0', 'required': False},
        {'short': 'a', 'long': 'action', 'help': 'Action of runing', 'default': 'qrcode', 'required': True},
        {'short': 'c', 'long': 'copy', 'help': 'Copy of OTP code', 'action': 'store_true', 'required': False},
        {'short': 'hk', 'long': 'hide-key', 'help': 'Hide OTP code', 'action': 'store_true', 'required': False},
    ]).run()
