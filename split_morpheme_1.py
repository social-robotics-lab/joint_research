"""
Janomeを使って、テキストファイルの最後の列を分かち書きして出力するサンプルコード
Janomeのインストール方法: pip install janome
入力ファイルの形式は以下のように、タブ区切りで複数列があるとします。
列1    列2    列3...    分かち書きするテキスト
出力ファイルの形式は以下のようになります。
列1    列2    列3...    分かち書きしたトークン
"""
from janome.tokenizer import Tokenizer

input_file = "sample.txt"
output_file = "output_1.txt"
tokenizer = Tokenizer()

with open(input_file, "r", encoding="utf-8") as f_in, \
     open(output_file, "w", encoding="utf-8") as f_out:
    # 1行目だけそのまま出力する
    first_line = next(f_in)
    f_out.write(first_line)
    # 2行目以降を処理する
    for line in f_in:
        # 改行を削除
        line = line.rstrip("\r\n")
        # タブで分割して列を取得
        cols = line.split("\t")
        # 列がない場合はスキップ
        if len(cols) == 0:
            continue
        # Upperの列（最後から3番目）が空でない場合は分かち書きして置換
        if cols[-3]:
            tokens = tokenizer.tokenize(cols[-3])
            cols[-3] = " ".join(token.surface for token in tokens)
            f_out.write("\t".join(cols) + "\n")
        # Lowerの列（最後から2番目）が空でない場合は分かち書きして置換
        elif cols[-2]:
            tokens = tokenizer.tokenize(cols[-2])
            cols[-2] = " ".join(token.surface for token in tokens)
            f_out.write("\t".join(cols) + "\n")
        # Cutの列（最後の列）が空でない場合はそのまま出力
        elif cols[-1]:
            f_out.write(line + "\n")
