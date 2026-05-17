# ファイルを読み込んで表示するサンプルコード
input_file = "sample.txt"
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        # 改行を削除
        line = line.rstrip("\n")
        print(line)
