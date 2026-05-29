# Web リサーチエージェント

Claude の `web_search` ツールを使って、指定したテーマを自動調査して要約レポートを生成するシンプルなエージェントです。

## セットアップ

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_api_key
```

## 使い方

```bash
# テーマを引数で渡す
python agent.py "量子コンピュータの最新動向"

# 引数なしだとデフォルトテーマで実行
python agent.py
```

## 出力例

```
テーマ: 量子コンピュータの最新動向

[検索中] 量子コンピュータ 2025 最新動向
[検索中] quantum computing breakthrough 2025

## 量子コンピュータの最新動向

### 概要
...
```

## 仕組み

1. ユーザーからテーマを受け取る
2. Claude が `web_search` ツールで検索クエリを生成・実行
3. 検索結果をもとに Claude が要約レポートを生成
4. ツール呼び出しが終わるまでエージェントループを継続
