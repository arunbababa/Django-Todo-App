# 簡易的なタスク管理アプリケーションをDjangoで作成
## 以下の流れの大枠と詳細をきちんと理解し、他フレームワークへ流用するためのひな形としても意味のあるコードとなる

## 前提条件
* 環境はLinux

## 環境構築手順

### 仮想環境の作成
* python3 -m venv venv(ここは好きな仮想環境名で良い)

### 使用するパッケージのインストール
* pip install -r req.txt

### DB作成
* python3 manege.py makemigrations
* python3 manege.py migrate

### 動作検証
* python3 manege.py runserver 
* http://127.0.0.1:8000/login/ へアクセス
* ログイン画面が見えたらOK