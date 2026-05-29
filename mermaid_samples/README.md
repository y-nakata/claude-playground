# Mermaid 図サンプル集

GitHub の Markdown で使える Mermaid 図のサンプルです。

---

## 1. フローチャート

システムのリクエスト処理フローの例。

```mermaid
flowchart TD
    A([ユーザー]) -->|リクエスト| B[ロードバランサー]
    B --> C[Webサーバー]
    C --> D{キャッシュあり?}
    D -->|Yes| E[キャッシュから返す]
    D -->|No| F[DBクエリ]
    F --> G[レスポンス生成]
    G --> H[キャッシュに保存]
    H --> E
    E -->|レスポンス| A
```

---

## 2. シーケンス図

OAuth 2.0 認証フローの例。

```mermaid
sequenceDiagram
    actor User
    participant App
    participant AuthServer
    participant ResourceServer

    User->>App: ログインボタンをクリック
    App->>AuthServer: 認証リクエスト
    AuthServer->>User: ログイン画面を表示
    User->>AuthServer: ID / パスワードを入力
    AuthServer->>App: 認可コードを発行
    App->>AuthServer: アクセストークンをリクエスト
    AuthServer->>App: アクセストークンを発行
    App->>ResourceServer: APIリクエスト（トークン付き）
    ResourceServer->>App: リソースを返す
    App->>User: コンテンツを表示
```

---

## 3. ER図

ブログアプリのデータモデルの例。

```mermaid
erDiagram
    USER {
        int id PK
        string name
        string email
        datetime created_at
    }
    POST {
        int id PK
        int user_id FK
        string title
        text body
        datetime published_at
    }
    COMMENT {
        int id PK
        int post_id FK
        int user_id FK
        text body
        datetime created_at
    }
    TAG {
        int id PK
        string name
    }
    POST_TAG {
        int post_id FK
        int tag_id FK
    }

    USER ||--o{ POST : "投稿する"
    USER ||--o{ COMMENT : "コメントする"
    POST ||--o{ COMMENT : "持つ"
    POST ||--o{ POST_TAG : "タグ付けされる"
    TAG ||--o{ POST_TAG : "使われる"
```

---

## 4. 状態遷移図

ECサイトの注文ステータス遷移の例。

```mermaid
stateDiagram-v2
    [*] --> 注文受付
    注文受付 --> 支払い待ち : 注文確定
    支払い待ち --> 準備中 : 支払い完了
    支払い待ち --> キャンセル済み : 期限切れ
    準備中 --> 発送済み : 発送処理
    準備中 --> キャンセル済み : キャンセル申請
    発送済み --> 配達完了 : 配達
    配達完了 --> 返品受付 : 返品申請
    返品受付 --> 返金済み : 返金処理
    配達完了 --> [*]
    キャンセル済み --> [*]
    返金済み --> [*]
```

---

## 5. ガントチャート

Webアプリ開発プロジェクトのスケジュール例。

```mermaid
gantt
    title Webアプリ開発スケジュール
    dateFormat YYYY-MM-DD
    section 要件定義
        ヒアリング          :a1, 2025-06-01, 7d
        要件定義書作成      :a2, after a1, 5d
    section 設計
        UI/UXデザイン       :b1, after a2, 10d
        DB設計              :b2, after a2, 7d
        API設計             :b3, after b2, 5d
    section 開発
        フロントエンド       :c1, after b1, 20d
        バックエンド        :c2, after b3, 20d
    section テスト
        結合テスト          :d1, after c1, 7d
        UAT                 :d2, after d1, 5d
    section リリース
        本番デプロイ        :e1, after d2, 2d
```
