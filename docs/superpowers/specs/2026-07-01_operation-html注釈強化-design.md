# operation.html / index.html 注釈強化 — 設計

## 目的

`loop-engineering-guide` リポジトリの `operation.html`（運用ガイド）と `index.html`（概念教科書）は専門用語密度が高く、数ヶ月放置すると未来の自分でも用語の前提を忘れて読みにくくなる。本仕様は**用語を残したまま**「なぜ・どういう意味か」の解説を厚くし、未来の自分（数ヶ月後）が迷わず読めるようにする。

## 対象読者

未来の自分（数ヶ月後）。用語自体は残す（完全な初心者向けへの日常語全翻訳はしない）。要点と「なぜこうなっているか」の注釈を厚くする。

## 方針

- **現ページ直接編集**（別ページ分離しない）。1ページで完結・管理一元化。
- 既存のアコーディオン・表・コード構成は維持。
- 既存CSS変数（`--accent`, `--border` 等）・クラス（`.concept-box`, `.part-h2`）を流用。新規スタイルも同系色で。

## 編集範囲

- `operation.html`（主・厚く）
- `index.html`（従・薄く。概念教科書は既に平易なため控えめ）

## 3つの注釈要素

### 1. 冒頭「ひと目でわかる」フロー図（operation.html）

既存の「全体像」セクション（L76〜86）の `<pre><code>` ブロックを視覚的なフロー図に拡張。Flexboxの矢印図で表現。既存のテキストフローは維持しつつ視覚化。

```html
<div class="flow-diagram">
  <div class="flow-node">Daily Triage（朝6:07自動）<br><small>バックログ＋手付タスクをAIが集めてリスト化</small></div>
  <div class="flow-arrow">↓</div>
  <div class="flow-node">人間承認（approve.py）<br><small>どれをやるか人間が選ぶ</small></div>
  <div class="flow-arrow">↓</div>
  <div class="flow-node">自律実行連鎖<br><small>OK→次へ / NG→停止</small></div>
</div>
```

`.flow-diagram`, `.flow-node`, `.flow-arrow` のCSSを `assets/style.css` に追加。

### 2. ホバー解説（.term / .term-popup）

`add-term-tooltip` スキルの .term/.term-popup パターンを採用。両ページに適用。

- 対象用語（operation.html 例）: `Daily Triage`, `state.json`, `承認ゲート`, `run-task.sh`, `next_issue.py`, `verify-result.txt`, `Stop hook`, `SessionStart hook`, `handoff`, `pending/current/completed/blocked`, `marker`, `per-task repo`
- 構造:
  ```html
  <span class="term">Daily Triage</span><span class="term-popup">朝6:07に自動実行されるAI判定タスク。バックログ＋手付タスクを優先度順にリスト化します</span>
  ```
- 解説は1-2行・「なぜ」も簡潔に含める（最大2行・3行禁止で冗長化防止）。
- **モバイル/a11y対策（必須）**: ホバーだけでなく**タップ/フォーカスでもポップアップ表示**。`aria-describedby` で紐付け・キーボードフォーカス時にも表示。タップ外で閉じる。スマホ・スクリーンリーダー・キーボード利用でも解説が読める。
- 実装時、同一用語が複数箇所に出現する場合は add-term-tooltip スキルの仕様（一意化するか毎回定義か）を確認して從う（MiniMax指摘E）。
- CSS（`assets/style.css` に追加）:
  ```css
  .term { color: var(--accent, #7c3aed); text-decoration: underline dotted; cursor: help; }
  .term-popup { /* ホバー + フォーカス + タップで表示・add-term-tooltip スキル既定パターン準拠 */ }
  .term:focus .term-popup, .term:hover .term-popup { display: block; }
  ```

### 3. 「なぜ必要」box

既存の `.concept-box` と同系で小型の `.why-box` クラスを新設。

```html
<div class="why-box">
  <strong>なぜ Daily Triage？</strong>
  人間が毎朝バックログを読み直すのは時間がかかる。AIに優先度判定を任せ、人間は「どれをやるか」だけ判断すればよくなる。
</div>
```

CSS:
```css
.why-box {
  background: rgba(124,58,237,.05);
  border-left: 3px solid var(--accent, #7c3aed);
  border-radius: 6px;
  padding: .7rem 1rem;
  margin: .8rem 0;
  font-size: .88rem;
}
```

配置箇所（operation.html）— **限定（MiniMax指摘B・冗長化防止）**:
- 「全体像」直後（loop全体の存在意義）
- 第2部「アーキテクチャ」内（コンポーネント設計の意図）
- **①〜⑤の各アコーディオン内には置かない**（本文=事実とwhy-box=理由の二重化を避ける・各ステップの必要性はホバー解説で十分）

配置箇所（index.html）:
- 各章末（控えめに）

## index.html への適用（従・薄く）

- ホバー解説（用語は operation より少ない想定）
- 各章末に「なぜこの仕組み？」box
- フロー図は operation のみ（index は概念中心なので不要）

## 実装上の注意

- `add-term-tooltip` スキルの実装パターン（.term/.term-popup）に準拠。必要に応じてスキルを呼んで自動付与。
- 既存の `assets/style.css` に追記（上書きしない）。
- `html-guide` スキルのルール（CSS変数・ダーク/ライトモード対応・視認性チェック・CI テスト通過）に準拠。
- operation.html 既存のOG/meta・フッタ・JS（アコーディオン・テーマ切替）は変更しない。

## 完了条件

- operation.html にフロー図・ホバー解説（主要用語）・なぜbox（要所）が入る。
- index.html にホバー解説・なぜbox（控えめ）が入る。
- `assets/style.css` に新規クラスが追加され、ダーク/ライト両モードで視認性OK。
- GitHub Pages で公開後、ホバー**およびタップ/フォーカス**で解説が表示されることを目視確認。

### 目視チェックリスト（MiniMax指摘C・完了前に実施）
- [ ] ダーク/ライト両モードでフロー図・why-box・term-popup の視認性OK（devtools で切替確認）
- [ ] CSS競合チェック: 新規 `.term` `.term-popup` `.why-box` `.flow-*` クラスが既存クラスと衝突しない
- [ ] 用語整合: ホバー解説を付けた用語と本文の表記ゆれがない
- [ ] モバイル幅（375px想定）でフロー図が崩れない・term-popup が画面端で見切れない
- [ ] キーボードフォーカス（Tab）で term-popup が表示される
