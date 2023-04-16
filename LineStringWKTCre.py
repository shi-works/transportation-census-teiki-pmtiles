# -*- coding: utf-8 -*-
import csv
import pandas as pd

# 出力WKTファイルオープン
output_csvfile = "./out/teiki_od_pattern_count_add_coordinate.wkt"
with open(output_csvfile, 'a', encoding='utf-8') as f:
    # ヘッダー行出力
    fieldnames = ['geom', '区間開始駅事業者名', '区間開始駅名', '区間終了駅事業者名',
                  '区間終了駅名', '通勤枚数', '通学枚数', '合計枚数']
    csvfile_writer = csv.DictWriter(
        f, fieldnames=fieldnames, lineterminator='\n')
    csvfile_writer.writeheader()

    # CSVファイルをリストに格納
    data = pd.read_csv(
        "./out/teiki_od_pattern_count_add_coordinate.csv").values.tolist()

    for i in range(len(data)):
        e_lnglat = str(data[i][3]) + " " + str(data[i][2])
        d_lnglat = str(data[i][7]) + " " + str(data[i][6])
        geom = "LINESTRING(" + e_lnglat + "," + d_lnglat + ")"
        # 出力CSVファイルに書き込む
        csvfile_writer.writerow({
            'geom': geom,
            '区間開始駅事業者名': data[i][0],
            '区間開始駅名': data[i][1],
            '区間終了駅事業者名': data[i][4],
            '区間終了駅名': data[i][5],
            '通勤枚数': data[i][8],
            '通学枚数': data[i][9],
            '合計枚数': data[i][10]
        })

print(u'処理終了')
