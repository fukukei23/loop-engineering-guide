# 🔄 ループエンジニアリング教科書

2026年のAI活用パラダイム「ループエンジニアリング」を、概念→設計→実践→運用の4部14章で読み解く教科書。自分自身の学習・実践整理。

🌐 **公開**: https://fukukei23.github.io/loop-engineering-guide/

## 構成（4部14章）

- **第1部 概念**: ループエンジニアリングとは / AI活用の進化 / Boris Cherny「write loops, not prompts」 / キーパーソン
- **第2部 設計**: 5要素 / 状態の記録（土台）/ 作るAIと検証AIの分離 / ループの1日
- **第3部 実践**: 自分のClaude Code環境を5要素でマップ / OpenClaw・Claude Code・Codex比較
- **第4部 運用と移行**: 3つの落とし穴 / プロンプト→ループ移行ロードマップ / エンジニアであり続ける / 参考資料

## 姉妹ページ: 私の運用ガイド（具体手順）

- [🔧 私のLoop Engineering運用ガイド](https://fukukei23.github.io/loop-engineering-guide/operation.html)（`operation.html`） — 概念教科書（本ページ）が「ループエンジニアリングとは何か」を学ぶものなのに対し、こちらは自分のClaude Code環境で毎日どう運用するかの具体手順（Daily Triage・承認ゲート・state.json・トラブル対応）。原本は SSOT `00_SYSTEM/共通ルール/自律開発ループ.md`。

## 生成元

- [解説動画「ループエンジニアリングを知ってみよう」](https://www.youtube.com/watch?v=Cps2LgY-ENE)（Gemini APIで解析）
- Web調査: [Addy Osmani原典](https://addyosmani.com/blog/loop-engineering/)・[Cobus Greyling](https://cobusgreyling.medium.com/loop-engineering-62926dd6991c)・[The AI Corner](https://www.the-ai-corner.com/p/loop-engineering-coding-agents-2026)
- 自分のClaude Code環境の棚卸し

## 関連ガイド

- [OpenClaw Stack Guide](https://fukukei23.github.io/openclaw-stack-guide/) — ループの象徴的実装
- [Claude Code Guide](https://fukukei23.github.io/claude-code-guide/) — hooks/skill/MCP/subagent の機能詳細
- [ガイド集](https://fukukei23.github.io/guides/)

## 技術

単一 `index.html` + `assets/style.css`（共通デザイン流用）。アコーディオン展開・ダーク/ライト切替・モバイル対応・外部CDN不使用。

設計・計画: `docs/superpowers/specs/`・`docs/superpowers/plans/`
