# ファイルを読み込んでそのままファイル出力するサンプルコード
input_file = "sample.txt"
output_file = "output.txt"
with open(input_file, "r", encoding="utf-8") as f_in, \
     open(output_file, "w", encoding="utf-8") as f_out:
    for line in f_in:
        # 改行を削除
        line = line.rstrip("\r\n")
        f_out.write(line + "\n")
