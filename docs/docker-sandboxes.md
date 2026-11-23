# Docker Sandboxes と MCP Gateway

このプロジェクトはローカルの Docker Sandboxes を実行境界とし、MCP Gateway を static mode で使う方針です。対象リポジトリ単位で workspace を共有し、各タスクに必要な MCP サーバーのみを接続します。Docker Desktop の MCP Toolkit と Sandboxes の MCP 登録は別です。

## 準備

[Docker のインストール手順](https://docs.docker.com/ai/sandboxes/install/)に従って `sbx` をインストールし、Docker にサインインします。macOS の場合:

```sh
brew trust docker/tap
brew install docker/tap/sbx
sbx login
sbx --version
```

Codex の認証方法は [Codex ガイド](https://docs.docker.com/ai/sandboxes/agents/codex/)を参照してください。ホストの `~/.codex` 設定は Sandbox 内に自動で引き継がれません。

**Codex 側の Sandbox を維持したい間は、デフォルトの `sbx run codex` を実行しないでください。** Docker の Codex 用デフォルト起動は `--dangerously-bypass-approvals-and-sandbox` を使用します。Codex 側の Sandbox を後で OFF にする方針のため、その変更と起動方法は別途確認してから実施します。

## MCP サーバーの準備

ホスト側で必要な MCP サーバーを登録し、必要な OAuth 等を設定します。以下の名前と URL は利用するサーバーのものに置き換えます。

```sh
sbx mcp add <server-name> --url <server-url>
sbx mcp ls
```

Sandbox 作成時に `--static-mcp <server-name>` で登録済みのサーバーを指定します。複数の場合はカンマ区切りです。サーバーを付けず、動的な探索も無効にする場合は `--static-mcp none` を使います。既存 Sandbox の状態は `sbx inspect <sandbox-name>` で確認します。利用開始時は実際に MCP mode と接続サーバーを確認してください。

static mode でもホストから後でサーバーを追加できます。名前付き static set からすべてのサーバーを外した場合、Docker Sandboxes daemon の再起動後に動的探索が有効になる場合があります。サーバーなしの static を維持したい場合は `--static-mcp none` で作成します。詳細は [MCP Gateway](https://docs.docker.com/ai/sandboxes/mcp-gateway/) を参照してください。

## 権限の境界

直接共有した workspace への変更はホストに即時反映されます。対象リポジトリだけを共有し、必要に応じて clone mode を使います。MCP ツールはそのサーバーに与えられた権限で外部操作を行えます。ローカル stdio サーバーはホスト上で動くため、VM の内側に閉じ込められているとは限りません。GitHub 等には必要なリポジトリと操作に絞った認証情報を使い、ネットワークと MCP 権限を個別に確認します。
