import datetime
import requests
import json
import sys

API_URL = "http://localhost:8000/todos"
#
#
#
def todo_add_message(message: str) -> str:
    print("--- Tool: todo_add_message が呼び出されました ---")
    print(f"  [抽出された引数] message='{message}'")

    # --- ここからが外部API実行のシミュレーションです ---
    # TODO: あなたの実際のAPIエンドポイントURLに置き換えてください
 
    # 送信するメッセージ
    payload = {
        "title": message,
    }

    print(f"  [Webhook送信] URL: {API_URL}")
    print(f"  [Webhook送信] データ: {payload}")

    try:
        # 実際のAPI呼び出しを行う場合は、以下のコメントを解除します。
        # HTTP POSTリクエストを送信
        response = requests.post(
            API_URL,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )
        print("status_code=" + str(response.status_code))

        # このサンプルでは、API呼び出しが成功したと仮定します。
        print("  [登録結果] 成功したと仮定します。")
        # メッセージを送信する実処理
        return f"承知いたしました。「{message}」をメッセージを送信しました。"

    except requests.exceptions.RequestException as e:
        # API呼び出しでネットワークエラーなどが発生した場合の処理
        print(f"  [API結果] エラーが発生しました: {e}")
        return f"申し訳ありません。システムの通信エラーにより、登録に失敗しました。"
    except Exception as e:
        # その他の予期せぬエラーが発生した場合の処理
        print(f"  [API結果] 予期せぬエラーが発生しました: {e}")
        return f"申し訳ありません。予期せぬエラーにより、登録に失敗しました。"
    finally:
        print("--- Tool: 処理を終了します ---")
    # --- ここまでが外部API実行のシミュレーションです ---

#
#
#
if __name__ == "__main__":
    args = sys.argv
    print(f"実行ファイル名: {args[0]}")
    if len(args) > 1:
        #print(f"最初の引数: {args[1]}")
        print(f"引数 2: {args[2]}")
        message = args[2]
        todo_add_message(message)
        #print(resp)
    else:
        print("error, nothing args")

