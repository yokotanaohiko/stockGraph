stockGraph
==========


# 使い方

## 概要
djangoのファイル構成になっている

### 構成
コントローラー kabup/itempage/views.py
ビュー kabup/src/templates/page/ここにhtmlなどを置いてます
モデル kabup/itempage/model.py （使ってない）
データは、kabup/static/kabuka_data/ここに<銘柄番号>.csvとして株価データを置いてます

### 使い方 
#### サーバー起動
コンソールで、
stockGraph/kabup/manage.py runserver
でサーバー起動

#### jsonで日足情報を取得
localhost:8000/kabuka_json/<株価番号>
#### jsonで週足情報を取得
localhost:8000/week_json/<株価番号>
#### jsonで月足情報を取得
localhost:8000/month_json/<株価番号>
#### 株価チャートを表示
localhost:8000/d3sample

### 最新の株価データを取得



連絡を頂けるとコラボレーターに追加します
