# ScanTOTP

A one-time password (OTP) is a dynamic password valid for only one login session or transaction, enhancing security over traditional passwords. Many implementations include two-factor authentication, requiring both something a person has (like a keyring fob, smartcard, or cellphone) and something a person knows (such as a PIN).

> [!warning]
> This project is not compatible with FIDO hardware devices.

> [!important]
> This repository is currently paused and will only receive security updates and bug fixes.

## Installation

Clone this repository

```shell
git clone https://github.com/kremilly/ScanTOTP.git
```

Enter the path

```shell
cd ScanTOTP
```

Install all dependencies, using *pip*

```shell
pip install -r requirements.txt
```

## Quick started

### QR Code

Read a local QR Code image

```shell
python scantotp -a qrcode -m file -i qrcode.png
```

Read a remote QR Code image

```shell
python scantotp -a qrcode -m url -i https://example.com/qrcode.png
```

Read a QR Code image using webcam

```shell
python scantotp -a qrcode -m webcam
```

### Decode a OTP code

Decode a OTP code using QR Code local

```shell
python scantotp -a otp -m file -i qrcode.png
```

Decode a OTP code using QR Code remote

```shell
python scantotp -a otp -m url -i https://example.com/qrcode.png
```

Decode a OTP code using QR Code on webcam

```shell
python scantotp -a otp -m webcam
```

## Flags

| Name                    | Description      | Default    | Required | Value type             | Allow value |
| ----------------------- | ---------------- | ---------- | -------- | ---------------------- | ----------- |
| `-m`, `--mode`      | Mode of scan     | `None`   | Yes      | `String`             | Yes         |
| `-i`, `--input`     | Input of QR Code | `None`   | Yes      | `String`             | Yes         |
| `-a`, `--action`    | Action of runing | `qrcode` | Yes      | `String`             | Yes         |
| `-w`, `--webcam`    | Select a webcam  | `0`      | No       | `Integer (unsigned)` | Yes         |
| `-c`, `--copy`      | Copy OTP code    | `None`   | No       | `None`               | No          |
| `-hk`, `--hide-key` | Hide OTP code    | `None`   | No       | `None`               | No          |
