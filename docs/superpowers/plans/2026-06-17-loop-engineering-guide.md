# ループエンジニアリング教科書 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** ループエンジニアリングを主題とした独立教科書 `loop-engineering-guide`（4部14章フル版・単一HTML）を公開する。

**Architecture:** `textbook-guide` スキル（newモード）で単一 `index.html` + `assets/style.css` の骨組みを生成し、14章のコンテンツを素材（動画解析 + Web調査 + 自分の環境）から執筆。既存ガイド群と相互リンクし、GitHub Pages で公開。

**Tech Stack:** HTML / CSS（アコーディオン展開・ダーク/ライト切替・モバイル対応） / GitHub Pages / textbook-guideスキル

**Spec:** `docs/superpowers/specs/2026-06-17-loop-engineering-guide-design.md`

---

## ファイル構成

- `index.html` — 単一・全14章アコーディオン（作成）
- `assets/style.css` — スタイル（アコーディオン・ダークモード・モバイル）（作成）
- `README.md` — リポジトリ説明・公開URL・相互リンク（作成）
- `docs/superpowers/specs/2026-06-17-loop-engineering-guide-design.md` — 設計（既存）
- `docs/superpowers/plans/2026-06-17-loop-engineering-guide.md` — 本計画（既存）

## 素材ソース（全タスク共通）

- **動画解析**: `obsidian-ssot/30_RESEARCH/Claude-Code機能/2026-06-17_ループエンジニアリング概念.md`
- **Web調査リンク**: spec「参考リンク」セクション（Addy Osmani・Cobus Greyling・The AI Corner・Lushbinary・DataScienceDojo）
- **自分の環境**: `~/.claude/`（skills/scripts/hooks）・`obsidian-ssot/`（handoff/日記/state）

---

## Task 1: textbook-guide で骨組み生成

**Files:**
- Create: `index.html`（骨組み・14章の見出しのみ）
- Create: `assets/style.css`
- Create: `README.md`

- [ ] **Step 1: textbook-guide スキル起動（newモード）**

`textbook-guide` スキルを呼び出し、以下を指定:
- リポジトリ: `/home/yn4416/projects/loop-engineering-guide`（既にgit init済み・spec/planあり）
- タイトル: 「ループエンジニアリング教科書」
- 章構成: 4部14章（spec「章構成」の見出しをそのまま登録）
- モード: new

- [ ] **Step 2: 生成結果確認**

以下が生成されたことを確認:
- `index.html`（14章の見出しアコーディオン骨組み）
- `assets/style.css`
- `README.md`

- [ ] **Step 3: HTMLバリデーション**

Run: `python3 -c "from html.parser import HTMLParser; p=HTMLParser(); p.feed(open('/home/yn4416/projects/loop-engineering-guide/index.html').read()); print('OK')"`
Expected: `OK`

- [ ] **Step 4: 目視確認**

ブラウザ（または `head -50 index.html`）で骨組みが表示されることを確認。

- [ ] **Step 5: Commit**

```bash
git -C /home/yn4416/projects/loop-engineering-guide add index.html assets/ README.md
git -C /home/yn4416/projects/loop-engineering-guide commit -m "feat: textbook-guide骨組み生成（14章アコーディオン）"
```

---

## Task 2: 第1部 概念（Ch1-4）執筆

**Files:**
- Modify: `index.html`（第1部セクション）

各章の要点（原稿は実装時に展開・各200-500字）:

**Ch1 ループエンジニアリングとは**
- Addy Osmani原典の定義を引用: 「ループエンジニアリングは、エージェントにプロンプトを出す自分自身を置き換えること。代わりにそれを行うシステムを設計する」
- ループ＝「AIが自律的に次のタスクを考え実行し続ける仕組み」
- 出典リンク: https://addyosmani.com/blog/loop-engineering/

**Ch2 AI活用の進化**
- 4段階を図解: Prompt Engineering → Context Engineering → Harness Engineering → Loop Engineering
- 各段階の1行定義（Prompt=指示の工夫 / Context=文脈管理 / Harness=環境整備 / Loop=自律ループ設計）

**Ch3 パラダイムシフト（Boris Cherny）**
- 直引用: 「自分の仕事はプロンプトを書くことではなく、ループを書くこと（write loops, not prompts）」
- Boris = Anthropic・Claude Code作者
- 出典: https://cobusgreyling.medium.com/loop-engineering-62926dd6991c

**Ch4 キーパーソン**
- Addy Osmani（Google）: 概念体系化
- Boris Cherny（Anthropic）: Claude Code実装
- Peter Steinberger（OpenClaw）: 普及
- Cobus Greyling: 実装パターン（GitHub repo）

- [ ] **Step 1: 第1部4章を index.html に執筆**

上記要点を原稿化。各章に見出し・本文・出典リンク。

- [ ] **Step 2: HTMLバリデーション**

Run: `python3 -c "from html.parser import HTMLParser; p=HTMLParser(); p.feed(open('/home/yn4416/projects/loop-engineering-guide/index.html').read()); print('OK')"`
Expected: `OK`

- [ ] **Step 3: 引用元の正確性確認**

各章の出典リンク（Addy原典・Cobus Medium）が正しく記載されているか確認。

- [ ] **Step 4: Commit**

```bash
git -C /home/yn4416/projects/loop-engineering-guide add index.html
git -C /home/yn4416/projects/loop-engineering-guide commit -m "content: 第1部 概念（Ch1-4）"
```

---

## Task 3: 第2部 設計（Ch5-8）執筆

**Files:**
- Modify: `index.html`（第2部セクション）

各章の要点:

**Ch5 ループの5要素**
1. Clear goal（明確で検証可能な目標）
2. Context management（反復間の状態維持）
3. Verification（自己評価・検証）
4. Tool use（ツール・テスト実行）
5. Termination conditions（停止条件）
- 出典: The AI Corner / Lushbinary

**Ch6 状態の記録（土台）**
- 記憶の外在化: セッションごとに記憶を失うAIの性質を、外部ファイル（状態ファイル）で補完
- 進捗・次ステップを書き残してリレー

**Ch7 作るAIと検証AIの分離**
- 同じAIに自己チェックさせると判断が甘くなる
- 「作る役」と「検証役」を独立させる設計がベストプラクティス

**Ch8 ループの1日**
- 朝: 自動起動 → 状況整理AIが前日状況読込 → タスクリスト生成
- 昼: タスクごとの作業部屋で「作るAI」実装 → 「検証AI」が規約・テストで厳格チェック
- 夕: MCP経由でチケット更新・PR作成・チャット通知。解決不能は人間ボックスへ
- 夜: 状態ファイルに1日の成果・残課題を保存 → 翌朝リレー

- [ ] **Step 1: 第2部4章を index.html に執筆**
- [ ] **Step 2: HTMLバリデーション**（Task 2 Step 2と同じコマンド）
- [ ] **Step 3: 5要素の図解確認**（リスト/表で5要素が揃っているか）
- [ ] **Step 4: Commit**

```bash
git -C /home/yn4416/projects/loop-engineering-guide add index.html
git -C /home/yn4416/projects/loop-engineering-guide commit -m "content: 第2部 設計（Ch5-8）"
```

---

## Task 4: 第3部 実践（Ch9-10）執筆

**Files:**
- Modify: `index.html`（第3部セクション）

**Ch9 自分のClaude Code環境を5要素でマップ**

対応表（実装時に表組で記載）:

| 5要素 | 自分の実装 |
|---|---|
| Clear goal | Issue・handoffの「次にやること」 |
| Context management | git worktree（作業部屋分離）・CLAUDE.md |
| Verification | subagent（code-reviewer/silent-failure-hunter）・テスト |
| Tool use | MCP（brave-search/github/playwright/context7）・hooks |
| Termination | next-issue.py（pending空で停止）・state.active=false |

加えて「土台」: handoff.md / SSOT日記 / state.json

**Ch10 他者実装比較**

3実装の比較表:

| 観点 | OpenClaw | Claude Code | Codex |
|---|---|---|---|
| 提供元 | Peter Steinberger | Anthropic(Boris Cherny) | OpenAI |
| ループの単位 | （要調査・素材のWebリンク参照） | hooks+cron+subagent | （要調査） |

※ 未調査部分はWeb調査で補完（The AI Corner記事が Claude Code/Codex 両方を扱っている）

- [ ] **Step 1: 第3部2章を index.html に執筆**
- [ ] **Step 2: 必要に応じてOpenClaw/Codexの追加Web調査**（WebSearch・The AI Corner・Cobus Greyling GitHub）
- [ ] **Step 3: HTMLバリデーション**
- [ ] **Step 4: Commit**

```bash
git -C /home/yn4416/projects/loop-engineering-guide add index.html
git -C /home/yn4416/projects/loop-engineering-guide commit -m "content: 第3部 実践（Ch9-10）"
```

---

## Task 5: 第4部 運用と移行（Ch11-14）執筆

**Files:**
- Modify: `index.html`（第4部セクション）

**Ch11 3つの落とし穴**
1. 検証: 人間の目が必須（AI自己検証は甘くなる）
2. コスト: 並行処理で計算コスト増大
3. 理解の借金: AI超高速生成で人間がシステムを説明できなくなる

**Ch12 プロンプト→ループ移行ロードマップ**

段階的5ステップ:
1. プロンプトの再利用化（スキル化）
2. 状態の記録開始（handoff・ログ）
3. 自己検証の導入（subagent・テスト）
4. ツール連携（MCP・hooks）
5. 完全自律ループ（cron・Stop Hook）

**Ch13 エンジニアであり続ける**
- 人間は「ボタン押し係」でなく、全体俯瞰し判断を下す技術者
- ループが自動化を担うほど、審美眼と責任が重要

**Ch14 参考資料・リンク集**
- Addy Osmani原典: https://addyosmani.com/blog/loop-engineering/
- Cobus Greyling: https://cobusgreyling.medium.com/loop-engineering-62926dd6991c
- The AI Corner: https://www.the-ai-corner.com/p/loop-engineering-coding-agents-2026
- Lushbinary: https://lushbinary.com/blog/loop-engineering-ai-coding-agents-guide/
- DataScienceDojo: https://datasciencedojo.com/blog/agentic-loops-explained-from-react-to-loop-engineering-2026-guide/
- Cobus Greyling GitHub: https://github.com/cobusgreyling/loop-engineering
- 元動画: https://www.youtube.com/watch?v=Cps2LgY-ENE

- [ ] **Step 1: 第4部4章を index.html に執筆**
- [ ] **Step 2: HTMLバリデーション**
- [ ] **Step 3: 全リンクの切れ確認**（リンク集のURLが全て記載されているか）
- [ ] **Step 4: Commit**

```bash
git -C /home/yn4416/projects/loop-engineering-guide add index.html
git -C /home/yn4416/projects/loop-engineering-guide commit -m "content: 第4部 運用と移行（Ch11-14）"
```

---

## Task 6: スタイル・UI調整

**Files:**
- Modify: `assets/style.css`
- Modify: `index.html`（必要ならclass調整）

- [ ] **Step 1: アコーディオン動作確認**

各章がクリックで展開/折り畳みできるか確認。動かない場合は `assets/style.css` と index.html のJS/CSS を修正（make-song-guide/matt-pocock-skills-guideのstyle.css を参照）。

- [ ] **Step 2: ダーク/ライト切替確認**

トグルボタンでテーマが切り替わるか確認。

- [ ] **Step 3: モバイル表示確認**

ブラウザのレスポンシブ表示（または幅を狭める）でレイアウト崩れがないか確認。

- [ ] **Step 4: Commit**

```bash
git -C /home/yn4416/projects/loop-engineering-guide add assets/ index.html
git -C /home/yn4416/projects/loop-engineering-guide commit -m "style: アコーディオン・ダークモード・モバイル調整"
```

---

## Task 7: 相互リンク設定

**Files:**
- Modify: `index.html`（フッター/導入部に相互リンク）
- Modify: `README.md`（関連ガイド欄）
- Modify: `/home/yn4416/projects/openclaw-stack-guide/index.html`（逆リンク）
- Modify: `/home/yn4416/projects/guides/index.html`（ハブ登録） ※構造確認後

- [ ] **Step 1: loop-engineering-guide 側に相互リンク追加**

index.html のフッター/関連欄に:
- openclaw-stack-guide（OpenClaw＝ループの象徴的実装）
- claude-code-guide（Claude Code機能詳細）

README.md の関連ガイド欄にも記載。

- [ ] **Step 2: openclaw-stack-guide に逆リンク追加**

`/home/yn4416/projects/openclaw-stack-guide/index.html` の関連欄に loop-engineering-guide へのリンクを追加（構造を確認して既存パターンに倣う）。

- [ ] **Step 3: guides ハブへの登録確認**

`/home/yn4416/projects/guides/` の構造を確認。ガイド一覧があれば loop-engineering-guide を追加。

- [ ] **Step 4: Commit（各リポジトリ）**

```bash
git -C /home/yn4416/projects/loop-engineering-guide add index.html README.md
git -C /home/yn4416/projects/loop-engineering-guide commit -m "docs: 相互リンク設定"
git -C /home/yn4416/projects/openclaw-stack-guide add index.html
git -C /home/yn4416/projects/openclaw-stack-guide commit -m "docs: loop-engineering-guideへの逆リンク"
```

---

## Task 8: GitHub公開

**Files:** なし（リモート設定・Pages）

- [ ] **Step 1: GitHub リモート作成**

```bash
gh repo create fukukei23/loop-engineering-guide --public --source=/home/yn4416/projects/loop-engineering-guide --description "ループエンジニアリング教科書 — AI活用のパラダイム転換"
```

- [ ] **Step 2: push**

```bash
git -C /home/yn4416/projects/loop-engineering-guide push -u origin main
```

- [ ] **Step 3: GitHub Pages 有効化**

```bash
gh api repos/fukukei23/loop-engineering-guide/pages -X POST -f "build_type=legacy" -f "source[branch]=main" -f "source[path]=/"
```

API 403の場合（既知問題）: ユーザーに「Settings → Pages → main / root」の手動設定を依頼。

- [ ] **Step 4: 公開URL確認**

https://fukukei23.github.io/loop-engineering-guide/ にアクセスし表示されるか確認（Pages反映に数分）。

- [ ] **Step 5: SSOT記録**

`01_DECISIONS/claude-code/2026-06-17_ループエンジニアリング教科書作成.md` に成果記録・日記追記。

---

## Self-Review

**1. Spec coverage:**
- 目的・読者（自分用学習+実践整理）→ Task 2-5 の内容が対応 ✓
- 形態（独立リポジトリ・単一HTML・textbook-guide）→ Task 1 ✓
- 章構成4部14章 → Task 2-5 ✓
- 素材ソース → 各Task冒頭に明記 ✓
- 相互リンク → Task 7 ✓
- 公開 → Task 8 ✓

**2. Placeholder scan:**
- 「要調査」は Task 4 Ch10（OpenClaw/Codex比較）にあり → WebSearchで補完する手順を明記済み（Step 2）。
- 各章の「要点」は具体的。完全原稿は実装時に展開（コンテンツ作成の性質上、planに全原稿は不当に巨大になるため、要点+素材で実行可能）。

**3. 整合性:**
- 5要素の名称（Clear goal/Context management/Verification/Tool use/Termination）は Task 3 Ch5 と Task 4 Ch9 で同一 ✓
- 自分の環境の実装名（handoff/worktree/skills/MCP/subagent/state）は spec と Task 4 で同一 ✓

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-06-17-loop-engineering-guide.md`.
