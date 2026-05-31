# claude-playground

Claude と GitHub MCP の連携を試すための実験リポジトリです。

## 概要

このリポジトリは、Claude Desktop から GitHub を直接操作する MCP (Model Context Protocol) の動作確認や、各種スクリプト・コードのお試し実装に使用します。

## 構成

```
claude-playground/
├── aarm-sdk/            # AARM SDK パッケージ (pip install -e で使う)
│   ├── pyproject.toml
│   └── src/aarm/
│
├── agent/               # エージェントとデモ (aarm-sdk を外部依存として使う)
│   ├── requirements.txt # -e ../aarm-sdk
│   └── demo.py
│
├── mermaid_samples/     # Mermaid 図サンプル集
├── web_research_agent/  # Web リサーチエージェントサンプル
└── aarm/                # 旧ディレクトリ (deprecated → aarm-sdk/ に移行済み)
```

## セットアップ (AARM デモ)

```bash
cd agent
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_api_key
python demo.py
```

## 環境

- Claude Desktop
- GitHub MCP Server (`@modelcontextprotocol/server-github`)

## ライセンス

MIT
