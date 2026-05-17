"""
Janomeを使って、テキストファイルの最後の列を分かち書きして行ごとに分割して出力するサンプルコード
Janomeのインストール方法: pip install janome
入力ファイルの形式は以下のように、タブ区切りで複数列があるとします。
列1    列2    列3...    分かち書きするテキスト
出力ファイルの形式は以下のようになります。
列1    列2    列3...    分かち書きしたトークンの1つめ
列1    列2    列3...    分かち書きしたトークンの2つめ
列1    列2    列3...    分かち書きしたトークンの3つめ
...
"""
from janome.tokenizer import Tokenizer

input_file = "sample.txt"
output_file = "output_2.txt"
tokenizer = Tokenizer()

with open(input_file, "r", encoding="utf-8") as f_in, \
     open(output_file, "w", encoding="utf-8") as f_out:

    for line in f_in:
        # 改行を削除
        line = line.rstrip("\n")
        # タブで分割して列を取得
        cols = line.split("\t")

        if len(cols) == 0:
            continue

        # 最後の列を分かち書き
        tokens = tokenizer.tokenize(cols[-1])

        for token in tokens:
            # 分かち書きしたトークンを最後の列に追加して出力
            f_out.write("\t".join(cols[:-1] + [token.surface]) + "\n")

