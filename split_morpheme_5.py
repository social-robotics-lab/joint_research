"""
Janomeを使って、テキストファイルの最後の列を分かち書きして行ごとに分割し品詞を合わせて出力するサンプルコード
Janomeのインストール方法: pip install janome
入力ファイルの形式は以下のように、タブ区切りで複数列があるとします。
列1    列2    列3...    分かち書きするテキスト
出力ファイルの形式は以下のようになります。
列1    列2    列3...    分かち書きしたトークンの1つめ    品詞,その他情報...
列1    列2    列3...    分かち書きしたトークンの2つめ    品詞,その他情報...
列1    列2    列3...    分かち書きしたトークンの3つめ    品詞,その他情報...
...
"""
from janome.tokenizer import Tokenizer

input_file = "sample.txt"
output_file = "output_5.txt"
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
            for token in tokens:
                pos = token.part_of_speech
                # 分かち書きしたトークンを最後の列に追加して出力
                f_out.write("\t".join(cols[:-3] + [token.surface]) + "\t\t\t" + pos + "\n")
        # Lowerの列（最後から2番目）が空でない場合は分かち書きして置換
        elif cols[-2]:
            tokens = tokenizer.tokenize(cols[-2])
            for token in tokens:
                pos = token.part_of_speech
                # 分かち書きしたトークンを最後の列に追加して出力
                f_out.write("\t".join(cols[:-2] + [token.surface]) + "\t\t" + pos + "\n")
        # Cutの列（最後の列）が空でない場合はそのまま出力
        elif cols[-1]:
            f_out.write(line + "\n")
