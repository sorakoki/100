import os
import openai

# GitHub Secretsに登録したAPIキーを環境変数から取得
openai.api_key = os.getenv("OPENAI_API_KEY")

# ==== ここに要約したい不動産資料の内容を入れてください ====
text = """
東京都港区の中古マンション売買契約書。
価格5000万円、築2010年、専有面積70㎡。
駅徒歩5分、南向き、ペット可、管理費・修繕積立金あり。
"""
# ==========================================================

# OpenAI APIを使って要約
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "あなたは不動産業務に詳しいアシスタントです。"},
        {"role": "user", "content": f"次の不動産資料を簡潔に要約してください:\n{text}"}
    ],
    max_tokens=300,
    temperature=0.5
)

summary = response.choices[0].message["content"]

# 実行結果を表示
print("===== 要約結果 =====")
print(summary)

# コメント投稿や他処理に使う場合はファイルに保存も可能
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)
