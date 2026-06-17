# ループエンジニアリング教科書（loop-engineering-guide）設計

> 作成日: 2026-06-17
> brainstorming → writing-plans → textbook-guide（実装）

## 概要

ループエンジニアリングを主題とした独立教科書。自分自身の**学習 + 実践整理**を目的とする。概念の体系化と、自分のClaude Code環境の棚卸しを1冊にまとめる。

## 背景

- 2026年6月、**Addy Osmani**（Google）が「ループエンジニアリング」を体系化
- **Boris Cherny**（Anthropic・Claude Code作者）: 「自分の仕事はプロンプトを書くことではなく、ループを書くこと（write loops, not prompts）」
- 進化の連鎖: Prompt → Context → Harness → **Loop Engineering**
- ユーザーは既にClaude Code環境でループを実践中（handoff / worktree / skills / MCP / subagent / state）

## 目的・読者

- **読者**: 自分自身（非IT公務員→AI実践中・コード読解力学習中）
- **目的**: 概念の体系化 + 自分のClaude Code環境の整理
- 外部公開は副次的（既存ガイド群と同じ立ち位置）

## 形態・技術

- **リポジトリ**: `fukukei23/loop-engineering-guide`（新設）
- **構成**: 単一 `index.html` + `assets/style.css`（textbook-guideパターン・make-song-guide/matt-pocock-skills-guideと同構成）
- **生成**: `textbook-guide` スキル（new モード）
- **UI**: アコーディオン展開・ダーク/ライト切替・モバイル対応
- **公開**: GitHub Pages（手動有効化・API 403の既知問題あり）

## 章構成（C案・4部14章）

### 第1部: 概念（なぜループか）
1. **ループエンジニアリングとは** — 定義・Addy Osmani原典
2. **AI活用の進化** — Prompt → Context → Harness → Loop
3. **パラダイムシフト** — Boris Cherny「write loops, not prompts」
4. **キーパーソン** — Addy / Boris / Peter Steinberger / Cobus Greyling

### 第2部: 設計（ループの中身）
5. **ループの5要素** — Clear goal / Context management / Verification / Tool use / Termination
6. **状態の記録（土台）** — 記憶の外在化
7. **作るAIと検証AIの分離**
8. **ループの1日** — 朝（起動・タスク抽出）→ 昼（実装・検証）→ 夕（連携・エスカレ）→ 夜（状態保存）

### 第3部: 実践（自分の環境マップ）
9. **自分のClaude Code環境を5要素でマップ** — handoff / worktree / skills / MCP / subagent / state
10. **他者実装比較** — OpenClaw / Claude Code / Codex

### 第4部: 運用と移行
11. **3つの落とし穴** — 検証・コスト・理解の借金
12. **プロンプト→ループ移行ロードマップ**（段階的ステップ）
13. **エンジニアであり続ける** — 人間の役割再定義
14. **参考資料・リンク集**

## 素材ソース

- **動画解析**: `obsidian-ssot/30_RESEARCH/Claude-Code機能/2026-06-17_ループエンジニアリング概念.md`
- **Web調査**: Addy Osmani原典・Cobus Greyling（Boris直引用）・The AI Corner・Lushbinary・DataScienceDojo
- **自分の環境**: `~/.claude/`（skills/scripts/hooks）・`obsidian-ssot/`（handoff/日記/state）

## 相互リンク（既存ガイド群）

- **`openclaw-stack-guide`** — OpenClaw＝ループの象徴的実装（最も近い）
- **`claude-code-guide`** — Claude Code機能の詳細解説
- **`guides`** — ガイド集ハブ

## スコープ外（YAGNI）

- Zenn等の外部記事化（別ストリーム・素材流用可）
- 多言語化
- インタラクティブデモ

## 成果物

- リポジトリ: `/home/yn4416/projects/loop-engineering-guide/`
- 公開URL: `https://fukukei23.github.io/loop-engineering-guide/`（Pages有効化後）

## 参考リンク

- Addy Osmani（原典）: https://addyosmani.com/blog/loop-engineering/
- Cobus Greyling（Boris発言を直引用）: https://cobusgreyling.medium.com/loop-engineering-62926dd6991c
- The AI Corner（Claude Code/Codex実装）: https://www.the-ai-corner.com/p/loop-engineering-coding-agents-2026
- Lushbinary（5要素の実践）: https://lushbinary.com/blog/loop-engineering-ai-coding-agents-guide/
- DataScienceDojo（ReAct→Loop Engineering）: https://datasciencedojo.com/blog/agentic-loops-explained-from-react-to-loop-engineering-2026-guide/
- Cobus Greyling GitHub（実装パターン）: https://github.com/cobusgreyling/loop-engineering
