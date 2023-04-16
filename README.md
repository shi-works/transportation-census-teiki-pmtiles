# transportation-census-teiki-pmtiles
- 本データは、政府統計窓口（e-stat）にて公開されている、[第13回大都市交通センサスの定期券発売実績調査データ](https://www.e-stat.go.jp/stat-search/files?page=1&toukei=00600020&tstat=000001103355)の開始駅終了駅間定期枚数を集計するとともに、集計データを[tippecanoe](https://github.com/felt/tippecanoe)で[PMTiles形式](https://github.com/protomaps/PMTiles)に変換したデータになります。
- オープンソースソフトウェアで構築

# デモサイト（MapLibre GL JS）
- 使用データ：集計データ（PMTiles形式）※定期枚数500枚以上を表示
- https://shi-works.github.io/transportation-census-teiki-pmtiles/
- サンプル画像

# データの加工
## teiki_od_pattern_count.py
- 定期券発売実績調査データから開始駅終了駅間定期枚数（以下、集計データ）の集計を行うプログラムです。
### 使用データ
- 定期券発売実績調査データ
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/teiki/03_teiki/data/%E7%AC%AC13%E5%9B%9E%E5%A4%A7%E9%83%BD%E5%B8%82%E4%BA%A4%E9%80%9A%E3%82%BB%E3%83%B3%E3%82%B5%E3%82%B9%E5%AE%9A%E6%9C%9F%E5%88%B8%E7%99%BA%E5%A3%B2%E5%AE%9F%E7%B8%BE%E8%AA%BF%E6%9F%BB.csv`,139.7MB
### 出力結果
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/teiki/03_teiki/out/teiki_od_pattern_count.csv`,44.3MB

## csvfile-add-coordinate.py
- 集計データに国土数値情報の鉄道データの駅座標を付与するプログラムです。
- なお、駅座標データは、国土数値情報の鉄道データのラインデータを重心に変換したデータになります。
### 使用データ
- 国土数値情報の鉄道データ（重心）  
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/teiki/04_teiki_od_pattern_count_add_coordinate/data/N02-21_Station_Centroid.csv`,737.9KB
- 集計データ
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/teiki/03_teiki/out/teiki_od_pattern_count.csv`,44.3MB
### 出力結果
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/teiki/04_teiki_od_pattern_count_add_coordinate/out/teiki_od_pattern_count_add_coordinate.csv`,78.1MB

## LineStringWKTCre.py
- 駅座標を付与した、集計データについて、開始駅座標及び終了駅座標をもとに、WKT形式（LINESTRING）のデータに変換するプログラムです。
### 使用データ
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/teiki/04_teiki_od_pattern_count_add_coordinate/out/teiki_od_pattern_count_add_coordinate.csv`,78.1MB
### 出力結果
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/teiki/04_teiki_od_pattern_count_add_coordinate/out/teiki_od_pattern_count_add_coordinate.wkt`,91.4MB

## GeoJSON形式
- WKT形式（LINESTRING）の集計データをGeoJSON形式に変換したデータです。
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/teiki/04_teiki_od_pattern_count_add_coordinate/out/teiki_od.geojson`,271.8MB

## PMTiles形式（ベクトルタイル）
- GeoJSON形式の集計データを[tippecanoe](https://github.com/felt/tippecanoe)で[PMTiles形式](https://github.com/protomaps/PMTiles)に変換したデータです。
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/transportation-census/teiki/04_teiki_od_pattern_count_add_coordinate/out/teiki_od.pmtiles`,457.9MB

# ライセンス
本データセット（使用データ及び出力結果）は[CC-BY-4.0](https://github.com/shi-works/traffic-accident-pmtiles/blob/main/LICENSE)で提供されます。使用の際には本レポジトリへのリンクを提示してください。

また、本データセットは、第13回大都市交通センサスの3次ODデータを加工して作成したものです。本データセットの使用・加工にあたっては、[国土交通省のリンク・著作権・免責事項](https://www.mlit.go.jp/link.html)を必ずご確認ください。

# 免責事項
利用者が当該データを用いて行う一切の行為について何ら責任を負うものではありません。
