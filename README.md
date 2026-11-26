# Agentic Harness

Codex と Claude Code 向けの、品質属性に基づく自律作業 Plugin です。エージェントに具体的な工程を強制せず、仕様の正本・機能契約・独立検証・人間の理解可能性を守りながら、要求された品質を合理的なコストで実現することを目指します。

## 設計と判断

6 つの原則は Quality Attribute Driven、Semantic Integrity、Human Understandability、Agent Autonomy、Independent Verifiability、Evolution Adaptability です。適用方法、Plugin の事前条件・不変条件・事後条件、セキュリティ境界は [設計の正本](docs/design.md) にあります。作業指針の正本は [autonomous-run Skill](skills/autonomous-run/SKILL.md) です。導入先の既存仕様・受入基準・権限設定は置き換えません。

参考実装から、品質シナリオ、機能契約、アーキテクチャ判断、ハーネス評価の様式と実行例を採用しました。QAW・ADD・ATAM・CBAM は必要に応じて利用し、全タスクに工程や文書の作成を強制しません。例は契約の説明用であり、本番の認可実装ではありません。

既存の Skill と SessionStart Hook は両方維持しています。Hook は Skill の存在を知らせるだけで、制御・認可・検証を強制しません。参考実装の AGENTS.md や空のプロジェクト仕様を導入先へ自動配置しないのは、既存の正本や指示を重複・上書きしないためです。Hook と Skill の効果は未測定であり、[評価計画](docs/evaluation.md)に基づいて測定し、モデル進化時に見直します。

## インストール

### Codex

```sh
codex plugin marketplace add zawakichi/agentic-harness
codex plugin add agentic-harness@agentic-harness
```

clone 済みの場合は Marketplace の引数にローカルのリポジトリパスを使えます。Codex の Hook はホストの対応と信頼設定が必要です。Sandbox 内の Plugin 読み込みと Hook 実行は未検証です。

### Claude Code

clone 済みの Plugin を `claude --plugin-dir /path/to/agentic-harness` で読み込みます。`/agentic-harness:autonomous-run` で Skill を指定できます。実際のセッションでの Skill と Hook の実行は未検証です。

## 検証

Python 3.10 以上で次を実行します。Plugin の定義と Hook の出力を確認し、別途、参考実装の機能契約に対する小さな実行例を検証します。

```sh
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s examples/document-delete -v
claude plugin validate .
```

これらはホストへの Plugin 読み込み、モデルの行動、安全性や有効性の証明ではありません。独立した基準と比較実験の方法は [評価計画](docs/evaluation.md) を参照してください。

## 実行環境

Docker Sandboxes と static mode の MCP Gateway を利用する方針です。[導入手順と権限の境界](docs/docker-sandboxes.md)を参照してください。Skill と Hook は Sandbox、CI、承認、権限制御の代わりにはなりません。
