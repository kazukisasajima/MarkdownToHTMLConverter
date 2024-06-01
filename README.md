# MarkdownToHTMLConverter

## 概要

マークダウンを HTML に変換する Python スクリプトです。このプロジェクトはコンピュータサイエンス学習サービス[Recursion](https://recursion.example.com)の課題で取り組みました。

## インストール

- スクリプトを実行するには[python-markdown](https://pypi.org/project/Markdown/)をインストールする必要があります。

```sh
python pip install -r requirements.txt
python pip install markdown
```

## 実行方法

- 以下のコマンドを使用して、マークダウンファイルを HTML ファイルに変換できます。

```sh
python file_converter.py markdown sample.md index.html
```

## イメージ

例えば、以下のようなイメージを、
![マークダウンファイルの画像](<img width="377" alt="sample_md_file" src="https://github.com/kazukisasajima/MarkdownToHTMLConverter/assets/99520758/10a55970-7d37-4be3-a790-16927654afb2">)

以下のような HTML ファイルに変換します。
![HTMLファイルの画像](<img width="377" alt="sample_html_file" src="https://github.com/kazukisasajima/MarkdownToHTMLConverter/assets/99520758/93a30bd1-5843-45e8-ac58-ad572706c566">)

変換した HTML をブラウザで表示すると、
![HTMLをブラウザで表示させた画像](<img width="410" alt="sample_brouser_file" src="https://github.com/kazukisasajima/MarkdownToHTMLConverter/assets/99520758/c5ce365a-104d-4599-9a93-ff9debc4ed02">)
のようになります。
