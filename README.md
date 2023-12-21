# OOP2-11-web-image

オブジェクト指向及び演習 第11週講義用課題プログラム

画像のアップロードを行うWebインターフェースと、アップロードされた画像に処理を行うバックエンド側のプログラム

## Initial Setting

```zsh
$ git clone https://github.com/2023AIT-OOP2-G03/OOP2-11-web-image.git
$ cd OOP2-11-web-image.
$ python -m venv .env
$ source .env/bin/activate
(.env) $ pip install -r requirements.txt
```

## Require

- Python version : 3.11.5 or higher
- OpenCV version : 4.8.1 or higher

```
Flask==3.0.0
opencv-python==4.8.1.78
watchdog==3.0.0
```

## Usage

このシステムは、演習の都合上Webインターフェイスと画像処理プログラムを別個で起動する必要があります。

### Webインターフェイスの起動

```zsh
$ source .env/bin/activate
(.env) $ python /web/main.py
```

### 画像処理プログラムの起動

```zsh
$ source .env/bin/activate
(.env) $ python main.py
```