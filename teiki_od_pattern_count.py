import os
import sys
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


def get_all_files(input_directory, file_extension):
    # 再帰的に指定フォルダ内の全ファイルを取得する
    return list(Path(input_directory).rglob(f'*{file_extension}'))


def process_files(input_directory, output_directory, file_extension, include_header):
    # 開始時刻を記録
    start_time = datetime.now()

    # 対象フォルダ内のすべてのファイルを取得
    all_files = get_all_files(input_directory, file_extension)
    all_files.sort()

    # 各ファイルのパスをログファイルに書き出す
    with open(os.path.join(output_directory, 'log.csv'), mode='w', newline='', encoding='shift-jis') as log_file:
        log_writer = csv.writer(log_file)
        log_writer.writerow(['読み込みファイル'])

        for file_path in all_files:
            log_writer.writerow([str(file_path)])

    # 重複データを格納する辞書を初期化
    stats = defaultdict(lambda: [0, 0, 0])

    # 各ファイルを処理
    for file_path in all_files:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)

            # ヘッダー行を読み飛ばす場合
            if include_header:
                next(reader, None)

            # 各行を処理
            for row in reader:
                key1 = '_'.join(row[3:5] + row[8:10])
                key2 = '_'.join(row[12:14] + row[17:19])
                # print(key1)
                # print(key2)
                tsukin = row[19]
                tsugaku = row[20]
                goukei = row[21]
                tsukin_without_commas = tsukin.replace(",", "")
                tsugaku_without_commas = tsugaku.replace(",", "")
                goukei_without_commas = goukei.replace(",", "")
                stats[key1][0] += int(tsukin_without_commas)
                stats[key1][1] += int(tsugaku_without_commas)
                stats[key1][2] += int(goukei_without_commas)
                stats[key2][0] += int(tsukin_without_commas)
                stats[key2][1] += int(tsugaku_without_commas)
                stats[key2][2] += int(goukei_without_commas)

        print("入力済みファイル: " + str(file_path))

    # 重複データを出力ファイルに書き出す
    with open(os.path.join(output_directory, 'teiki_od_pattern_count.csv'), mode='w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['区間開始駅事業者名', '区間開始駅名', '区間終了駅事業者名',
                        '区間終了駅名', '通勤枚数', '通学枚数', '合計枚数'])

        for key, values in stats.items():
            if '___' not in key:
                writer.writerow(key.split('_') + values)

    # 終了時刻を記録し、所要時間を計算
    end_time = datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()

    # 結果を表示
    print(
        f"正常に終了しました\n\n開始時刻： {start_time}\n終了時刻： {end_time}\n所要時間： {elapsed_time / 60:.2f}分")


if __name__ == '__main__':
    input_directory = './data'  # 入力ディレクトリを指定
    output_directory = './out'  # 出力ディレクトリを指定
    file_extension = '.csv'  # 読み込むファイルの拡張子を指定
    include_header = True  # ヘッダー行を読み飛ばす場合はTrue、そうでない場合はFalse

    # process_files関数を呼び出して処理を実行
    process_files(input_directory, output_directory,
                  file_extension, include_header)
