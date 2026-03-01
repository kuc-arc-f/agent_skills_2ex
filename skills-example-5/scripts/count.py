import chromadb
import os

# --- 設定 ---
# データベースファイルのパス
DB_PATH = "./my_chroma_db"

# 調査したいコレクション名
COLLECTION_NAME = "my_document_collection"
# ----------------

# 1. クライアントの初期化
client = chromadb.PersistentClient(path=DB_PATH)

# 2. コレクションの取得
# 埋め込み関数は件数を取得するだけなら不要ですが、既存のコレクションを取得するためには名前が必要です。
try:
    collection = client.get_collection(name=COLLECTION_NAME)
    print(f"コレクション '{COLLECTION_NAME}' を取得しました。")
    
    # 3. 件数の調査
    # collection.count() を呼び出します
    item_count = collection.count()

    print("\n==================================")
    print(f"コレクション '{COLLECTION_NAME}' に登録されている件数: {item_count} 件")
    print("==================================")

except ValueError:
    # 指定されたコレクションが存在しない場合のエラー処理
    print(f"エラー: コレクション '{COLLECTION_NAME}' は存在しません。")