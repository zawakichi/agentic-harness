# Agentic Harness

Codex と Claude Code 向けの、自律的な作業を支援する Plugin の初期版です。共通の Skill と SessionStart Hook で構成します。

- `autonomous-run` Skill: 受け入れ条件の設定、実装、検証、失敗からの修正、結果報告を指示します。
- SessionStart Hook: 自律実行が求められた際に Skill を参照するよう、セッションに短いコンテキストを追加します。

Skill はエージェントへの指示であり、検証成功を強制するランタイムや、セッションを再開するスケジューラではありません。権限、承認、セッションの寿命は各ホストの設定に従います。

## Claude Code で試す

リポジトリを clone し、対象プロジェクトから `claude --plugin-dir /path/to/agentic-harness` で起動します。`/autonomous-run` を明示してタスクを依頼することもできます。

## Codex で使う

Codex の Plugin としてローカルからインストールします。Hook は手動インストールされた Codex desktop Plugin でサポートされ、実行前に内容の確認と信頼が必要です。詳細は [Plugin のパッケージング](https://developers.openai.com/plugins/build/plugins) を参照してください。

## 構成

`.codex-plugin/plugin.json` と `.claude-plugin/plugin.json` は各ホストの Plugin 定義、`skills/` と `hooks/` は両者で共有する実装です。Hook スクリプトの実行には Python 3 が必要です。

## Docker Sandboxes

Docker Sandboxes と static mode の MCP Gateway を使う方針です。導入手順、Codex の起動時の注意、権限の境界は [Docker Sandboxes の手順](docs/docker-sandboxes.md)を参照してください。
