# ベースイメージの指定
FROM python:3.10

# 作業ディレクトリの設定
WORKDIR /code

# 依存関係のインストール
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y libmariadb-dev build-essential
RUN pip install mysqlclient

# コンテナのポート設定
EXPOSE 8000

# コンテナ起動時のコマンド実行
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
