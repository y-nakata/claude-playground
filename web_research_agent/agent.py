"""シンプルな Web リサーチエージェント

Claude の web_search ツールを使って、指定したテーマを調査して要約を返す。
"""

import anthropic
import json

MODEL = "claude-sonnet-4-20250514"

TOOLS = [
    {
        "type": "web_search_20250305",
        "name": "web_search",
    }
]

SYSTEM_PROMPT = """あなたは優秀なリサーチアシスタントです。
ユーザーから調査テーマを受け取ったら、web_search ツールを使って情報を収集し、
以下の形式で日本語の要約レポートを作成してください。

## {テーマ}

### 概要
（3〜5文でテーマの概要を説明）

### 主なポイント
（箇条書きで重要な情報を列挙）

### 参考情報
（参照した情報源のタイトルと URL）
"""


def research(theme: str) -> str:
    """テーマを受け取り、リサーチ結果を返す。"""
    client = anthropic.Anthropic()

    messages = [{"role": "user", "content": f"次のテーマについて調査してください: {theme}"}]

    # エージェントループ: ツール呼び出しが終わるまで繰り返す
    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )

        # アシスタントの返答を履歴に追加
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            # ツール呼び出しが終了 → テキスト応答を返す
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text

        elif response.stop_reason == "tool_use":
            # ツール結果を収集して次のターンへ
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"[検索中] {block.input.get('query', '')}")
                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": json.dumps(block.input),  # 実際の結果は API が処理
                        }
                    )
            messages.append({"role": "user", "content": tool_results})

        else:
            break

    return "リサーチを完了できませんでした。"


if __name__ == "__main__":
    import sys

    theme = sys.argv[1] if len(sys.argv) > 1 else "2025年の生成AI最新動向"
    print(f"テーマ: {theme}\n")
    result = research(theme)
    print(result)
