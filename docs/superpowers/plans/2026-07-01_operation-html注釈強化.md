# operation.html / index.html 注釈強化 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** loop-engineering-guide の operation.html / index.html に「ホバー解説 + フロー図 + なぜbox」を追加し、数ヶ月後の自分が専門用語の前提を忘れても読めるようにする。

**Architecture:** 参照実装 `~/projects/python-reading-guide/` の `.term/.term-popup` + `#term-tooltip` JS制御方式を採用。既存CSS変数（`--accent`/`--border`/`--accent-bg`）を流用し、新規クラス（`.term`/`.why-box`/`.flow-*`）を `assets/style.css` に追加。ホバー+a11y(フォーカス)+モバイル(タップ)対応済みのIIFEスクリプトを各ページに挿入。

**Tech Stack:** 静的HTML + CSS + バニラJS。CI無し（GitHub Pages の `static.yml` はデプロイのみ）。検証はローカル `python3 -m http.server` + ブラウザ目視。

---

## ファイル構造

| ファイル | 役割 | 変更 |
|---|---|---|
| `assets/style.css` | 共通スタイル。`.term`/`.term-popup`/`#term-tooltip`/`.why-box`/`.flow-*` 追加 | 末尾追記 |
| `operation.html` | 運用ガイド（主）。JS + フロー図 + why-box×2 + ホバー解説(12用語) | 編集 |
| `index.html` | 概念教科書（従）。JS + why-box(章末) + ホバー解説(控えめ) | 編集 |

---

## 共通前提（全タスクで参照）

### ローカルプレビュー起動コマンド

```bash
cd ~/projects/loop-engineering-guide && python3 -m http.server 8099
```
→ ブラウザで `http://localhost:8099/operation.html` を開く。終了は `Ctrl+C`。

### コミット規約
- コミットメッセージは日本語・末尾に `Co-Authored-By: Claude <noreply@anthropic.com>`
- 各タスク完了ごとに小さくコミット
- **push は最終タスク(Task 7)でユーザー確認後に行う**（それまでは commit のみ）

---

## Task 1: assets/style.css に共通クラス追加

**Files:**
- Modify: `assets/style.css`（末尾に追記）

- [ ] **Step 1: 既存クラス重複がないか確認**

Run: `grep -nE '\.term|\.why-box|\.flow-diagram|#term-tooltip' ~/projects/loop-engineering-guide/assets/style.css`
Expected: ヒットなし（新規追加OK）。ヒットした場合は既存定義を確認し名前衝突を避ける。

- [ ] **Step 2: style.css 末尾に以下を追記**

```css

/* === 注釈強化: ホバー解説 (.term/.term-popup/#term-tooltip) === */
.term {
  border-bottom: 1px dashed var(--accent);
  cursor: help;
  transition: color 0.2s;
}
.term:hover, .term:focus { color: var(--accent-dark); }
.term-popup { display: none; }  /* JS が #term-tooltip へ複製して表示 */
#term-tooltip {
  display: none;
  position: fixed;
  background: var(--accent-bg);
  border: 1px solid var(--accent);
  border-radius: 8px;
  padding: 8px 14px;
  font-size: 0.85rem;
  line-height: 1.5;
  max-width: 280px;
  z-index: 9999;
  box-shadow: 0 4px 12px rgba(0,0,0,.15);
}
#term-tooltip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 6px solid transparent;
}
#term-tooltip.below::after {
  top: auto; bottom: 100%;
  border-bottom-color: var(--accent);
}

/* === 注釈強化: 「なぜ」box === */
.why-box {
  background: var(--accent-bg);
  border-left: 3px solid var(--accent);
  border-radius: 6px;
  padding: 0.7rem 1rem;
  margin: 0.8rem 0;
  font-size: 0.88rem;
}
.why-box strong { color: var(--accent-dark); }

/* === 注釈強化: フロー図 === */
.flow-diagram {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
  margin: 1.2rem 0;
  padding: 1rem;
  background: var(--accent-bg);
  border-radius: 10px;
}
.flow-node {
  background: var(--bg, #fff);
  border: 1px solid var(--accent);
  border-radius: 8px;
  padding: 0.6rem 1rem;
  text-align: center;
  max-width: 360px;
  font-size: 0.9rem;
}
.flow-node small { display: block; opacity: 0.75; font-size: 0.78rem; margin-top: 0.2rem; }
.flow-arrow { color: var(--accent); font-size: 1.2rem; font-weight: 700; }
@media (max-width: 480px) {
  .flow-node { max-width: 100%; font-size: 0.85rem; }
}
```

- [ ] **Step 3: ローカルプレビューで既存表示が崩れないことを確認**

Run: `cd ~/projects/loop-engineering-guide && python3 -m http.server 8099`
→ ブラウザ `http://localhost:8099/operation.html` を開き、既存レイアウト（アコーディオン・表・ヘッダー）が変化ないこと。確認後 `Ctrl+C`。

- [ ] **Step 4: コミット**

```bash
cd ~/projects/loop-engineering-guide && git add assets/style.css && git commit -m "$(cat <<'EOF'
feat: style.cssに注釈強化クラス(.term/.why-box/.flow-*)追加

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

---

## Task 2: operation.html に #term-tooltip JS挿入

**Files:**
- Modify: `operation.html`（`</body>` 直前の既存 `<script>` ブロックの末尾に追記）

- [ ] **Step 1: 既存 script ブロックの末尾位置を特定**

Run: `grep -n '</script>' ~/projects/loop-engineering-guide/operation.html`
Expected: 行番号を控える（既存 `<script>...</script>` の閉じタグ）。既存スクリプトはアコーディオン toggle・テーマ切替・メニュー。

- [ ] **Step 2: 既存 `</script>` の直前（同じ script ブロック内の末尾）に以下を追記**

```javascript

// === 注釈強化: term tooltip（ホバー/フォーカス/タップ対応・a11y） ===
  var tip = document.createElement('div');
  tip.id = 'term-tooltip';
  document.body.appendChild(tip);
  var currentTerm = null;

  function showTip(term) {
    var popup = term.querySelector('.term-popup');
    if (!popup) return;
    tip.textContent = popup.textContent;
    tip.style.display = 'block';
    tip.classList.remove('below');
    var r = term.getBoundingClientRect();
    var tw = tip.offsetWidth;
    var th = tip.offsetHeight;
    var left = r.left + r.width / 2 - tw / 2;
    left = Math.max(8, Math.min(left, window.innerWidth - tw - 8));
    var top = r.top - th - 10;
    if (top < 8) { top = r.bottom + 10; tip.classList.add('below'); }
    tip.style.left = left + 'px';
    tip.style.top = top + 'px';
    currentTerm = term;
  }
  function hideTip() { tip.style.display = 'none'; currentTerm = null; }

  document.querySelectorAll('.term').forEach(function(t){
    t.setAttribute('tabindex', '0');
    t.addEventListener('mouseenter', function(){ showTip(t); });
    t.addEventListener('mouseleave', function(){ hideTip(); });
    t.addEventListener('focus', function(){ showTip(t); });
    t.addEventListener('blur', function(){ hideTip(); });
    t.addEventListener('click', function(e){
      e.stopPropagation();
      if (currentTerm === t) { hideTip(); } else { showTip(t); }
    });
  });
  document.addEventListener('click', function(){ hideTip(); });
  window.addEventListener('scroll', function(){ if (currentTerm) showTip(currentTerm); }, {passive:true});
})();
```

- [ ] **Step 3: プレビューでJSエラーがないことを確認**

Run: `cd ~/projects/loop-engineering-guide && python3 -m http.server 8099`
→ `operation.html` を開き、ブラウザのDevTools Console にエラーが出ないこと（`.term` 要素がまだ無くても `querySelectorAll` は空配列を返しエラーにならない）。確認後 `Ctrl+C`。

- [ ] **Step 4: コミット**

```bash
cd ~/projects/loop-engineering-guide && git add operation.html && git commit -m "$(cat <<'EOF'
feat: operation.htmlにterm-tooltip JS挿入(ホバー/フォーカス/タップ対応)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

---

## Task 3: operation.html に冒頭フロー図追加

**Files:**
- Modify: `operation.html`（「全体像」concept-box 内の `<pre><code>...</code></pre>` ブロックの直後）

- [ ] **Step 1: 挿入位置を特定**

Run: `grep -n '</code></pre>' ~/projects/loop-engineering-guide/operation.html | head -1`
Expected: 「全体像」内のテキストフロー `</code></pre>` の行番号。その直後にフロー図を挿入。既存の `<pre><code>` は残す（テキスト版と図版の二重保持）。

- [ ] **Step 2: 該当 `</code></pre>` の直後に以下を挿入**

```html
<div class="flow-diagram" aria-label="1日の流れフロー">
  <div class="flow-node">Daily Triage（朝6:07自動）<small>バックログ＋手付タスクをAIが集めてリスト化</small></div>
  <div class="flow-arrow">↓</div>
  <div class="flow-node">人間承認（approve.py）<small>どれをやるか人間が選ぶ・唯一の関与ポイント</small></div>
  <div class="flow-arrow">↓</div>
  <div class="flow-node">自律実行連鎖<small>run-task.sh（実装+検証）→ next_issue.py が OKで次へ/NGで停止</small></div>
</div>
```

- [ ] **Step 3: プレビューでフロー図が縦に表示されることを確認**

Run: `cd ~/projects/loop-engineering-guide && python3 -m http.server 8099`
→ 「全体像」セクションにノード3つ＋矢印2つの縦フローが表示されること。確認後 `Ctrl+C`。

- [ ] **Step 4: コミット**

```bash
cd ~/projects/loop-engineering-guide && git add operation.html && git commit -m "$(cat <<'EOF'
feat: operation.htmlの全体像にフロー図追加

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

---

## Task 4: operation.html に why-box 追加（2箇所）

**Files:**
- Modify: `operation.html`（①「全体像」concept-box の直後 ②第2部「アーキテクチャ」h2 の直後）

- [ ] **Step 1: 挿入位置①を特定**

Run: `grep -n '第1部 1日の流れ' ~/projects/loop-engineering-guide/operation.html`
Expected: 行番号を控える。その**直前**（`<h2 class="part-h2">第1部...` の前）に why-box①を挿入。

- [ ] **Step 2: why-box① を挿入**

`<h2 class="part-h2">第1部 1日の流れ</h2>` の直前に以下を挿入:

```html
<div class="why-box">
  <strong>なぜこのループを組む？</strong>
  人間が毎朝バックログを読み直しタスクを選ぶのは時間がかかる。AIに「候補選び」と「実装・検証の連鎖」を任せ、人間は「どれをやるか」の承認だけを出せばよくなる。これがLoop Engineeringの核心。
</div>

```

- [ ] **Step 3: 挿入位置②を特定**

Run: `grep -n '第2部 アーキテクチャ' ~/projects/loop-engineering-guide/operation.html`
Expected: 行番号を控える。その直後に why-box②を挿入（第2部 h2 の後・最初のアコーディオンの前）。

- [ ] **Step 4: why-box② を挿入**

`<h2 class="part-h2">第2部 アーキテクチャ・コンポーネント</h2>` の直後に以下を挿入:

```html
<div class="why-box">
  <strong>なぜ状態を state.json に記録する？</strong>
  ループは複数プロセス（実装・検証・次タスク起動）にまたがる。メモリだけでなくファイルに「今どのタスク・待機群・完了/ blockers」を書き込んでおくことで、停止しても再開でき、次タスク制御が状態を読むだけで済む。
</div>

```

- [ ] **Step 5: プレビューで why-box が2箇所表示されることを確認**

Run: `cd ~/projects/loop-engineering-guide && python3 -m http.server 8099`
→ 第1部見出し前と第2部見出し後に、左ボーダー紫の why-box が表示されること。確認後 `Ctrl+C`。

- [ ] **Step 6: コミット**

```bash
cd ~/projects/loop-engineering-guide && git add operation.html && git commit -m "$(cat <<'EOF'
feat: operation.htmlにwhy-box追加(全体像後・アーキテクチャ部)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

---

## Task 5: operation.html にホバー解説追加（主要12用語）

**Files:**
- Modify: `operation.html`（各用語の出現箇所。初出箇所のみ付与）

- [ ] **Step 1: 各用語の初出位置を grep で特定**

```bash
cd ~/projects/loop-engineering-guide
for w in "Daily Triage" "state.json" "承認ゲート" "run-task.sh" "next_issue.py" "verify-result.txt" "Stop hook" "SessionStart hook" "handoff" "marker" "per-task"; do
  echo "=== $w ==="; grep -n "$w" operation.html | head -2
done
```
Expected: 各用語の初出行番号を控える。各用語とも初出1箇所のみ付与（2回目以降は素通し）。

- [ ] **Step 2: 各用語を以下のパターンに置換（Edit ツールで初出箇所のみ）**

置換形式: `<span class="term">用語<span class="term-popup">解説</span></span>`

**Daily Triage** →
```html
<span class="term">Daily Triage<span class="term-popup">朝6:07にAIがバックログ等から当日タスク候補を自動生成する仕組み</span></span>
```

**state.json** →
```html
<span class="term">state.json<span class="term-popup">ループの進行状態（実行中/待機/完了/ blockers）を記録するファイル。停止再開の要</span></span>
```

**承認ゲート** →
```html
<span class="term">承認ゲート<span class="term-popup">AIが勝手に実行しないよう人間がGOを出す唯一の関所</span></span>
```

**run-task.sh** →
```html
<span class="term">run-task.sh<span class="term-popup">実装と検証を別プロセスで回す実行スクリプト</span></span>
```

**next_issue.py** →
```html
<span class="term">next_issue.py<span class="term-popup">1タスク終了後に次タスクへ自動遷移させる制御</span></span>
```

**verify-result.txt** →
```html
<span class="term">verify-result.txt<span class="term-popup">検証AIがOK/NGを書き出す結果ファイル。次タスク判定の根拠</span></span>
```

**Stop hook** →
```html
<span class="term">Stop hook<span class="term-popup">Claude終了時に発火する仕掛け。ここで次タスクを起動する</span></span>
```

**SessionStart hook** →
```html
<span class="term">SessionStart hook<span class="term-popup">セッション開始時に発火する仕掛け。handoff読込等を自動化</span></span>
```

**handoff** →
```html
<span class="term">handoff<span class="term-popup">前回セッションの文脈を次に渡す引き継ぎメモ</span></span>
```

**marker** →
```html
<span class="term">marker<span class="term-popup">today-tasks.mdで自動実行可か手動かを区別する印</span></span>
```

**per-task repo**（"per-task" で検索・文脈が `per-task repo` の箇所） →
```html
<span class="term">per-task repo<span class="term-popup">タスクごとに対象リポジトリを紐付ける方式。多repo混在キューに対応</span></span>
```

> 注意: `pending`/`current`/`completed`/`blocked` は表のセル内で出現するため個別付与せず、state.json の解説で一括カバーする（spec準拠・過剰装飾回避）。

- [ ] **Step 3: プレビューでホバー解説が表示されることを確認**

Run: `cd ~/projects/loop-engineering-guide && python3 -m http.server 8099`
→ 各用語にマウスを載せると `#term-tooltip` で解説が表示されること。Tab キーでフォーカス移動しても表示されること（a11y）。確認後 `Ctrl+C`。

- [ ] **Step 4: コミット**

```bash
cd ~/projects/loop-engineering-guide && git add operation.html && git commit -m "$(cat <<'EOF'
feat: operation.htmlに主要12用語のホバー解説追加

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

---

## Task 6: index.html に JS + why-box + ホバー解説追加（控えめ）

**Files:**
- Modify: `index.html`（概念教科書）

- [ ] **Step 1: index.html の構造を把握**

Run: `grep -nE '<h2|</script>|第[1-4]部' ~/projects/loop-engineering-guide/index.html | head -20`
Expected: 章立て（第1部〜第4部）と既存 script ブロック位置を把握。

- [ ] **Step 2: index.html の `</body>` 直前に #term-tooltip JS を挿入**

Task 2 Step 2 と**同一のJSコード**を index.html の最後の `<script>` ブロック末尾（無ければ `</body>` 直前に新規 `<script>...</script>` として）に挿入。コードは Task 2 Step 2 を完全に繰り返す（他タスクと独立に読めるよう重複保持）:

```javascript

// === 注釈強化: term tooltip ===
  var tip = document.createElement('div');
  tip.id = 'term-tooltip';
  document.body.appendChild(tip);
  var currentTerm = null;
  function showTip(term) {
    var popup = term.querySelector('.term-popup');
    if (!popup) return;
    tip.textContent = popup.textContent;
    tip.style.display = 'block';
    tip.classList.remove('below');
    var r = term.getBoundingClientRect();
    var tw = tip.offsetWidth, th = tip.offsetHeight;
    var left = Math.max(8, Math.min(r.left + r.width/2 - tw/2, window.innerWidth - tw - 8));
    var top = r.top - th - 10;
    if (top < 8) { top = r.bottom + 10; tip.classList.add('below'); }
    tip.style.left = left + 'px'; tip.style.top = top + 'px';
    currentTerm = term;
  }
  function hideTip() { tip.style.display = 'none'; currentTerm = null; }
  document.querySelectorAll('.term').forEach(function(t){
    t.setAttribute('tabindex','0');
    t.addEventListener('mouseenter', function(){ showTip(t); });
    t.addEventListener('mouseleave', function(){ hideTip(); });
    t.addEventListener('focus', function(){ showTip(t); });
    t.addEventListener('blur', function(){ hideTip(); });
    t.addEventListener('click', function(e){ e.stopPropagation(); if (currentTerm===t){hideTip();} else {showTip(t);} });
  });
  document.addEventListener('click', function(){ hideTip(); });
  window.addEventListener('scroll', function(){ if (currentTerm) showTip(currentTerm); }, {passive:true});
})();
```

- [ ] **Step 3: index.html の主要用語にホバー解説を付与（控えめ・3〜5用語）**

index.html で頻出する概念用語（例: 「メタループ」「Daily Triage」「状態の記録」等）の初出に `.term+.term-popup` を付与。用語と解説文は index.html の文脈に合わせて作成（各30〜60字）。grep で出現を確認しながら Edit。

例:
```html
<span class="term">メタループ<span class="term-popup">ループ全体を制御する上位のループ。個別タスクの実行ループを束ねる</span></span>
```

- [ ] **Step 4: 各章末（第1部〜第4部）に why-box を1つずつ追加（上限4つ）**

各部の最後の節の後に、その部の要点を「なぜ」で1行〜2行でまとめた why-box を挿入。本文と重複しない「意義」に絞る。例（第1部末）:

```html
<div class="why-box">
  <strong>第1部のポイント</strong>
  ループエンジニアリングは「プロンプトを1回書く」ではなく「AIが自走する仕組みを組む」考え方。ここが従来のAI活用との分岐点。
</div>
```
第2〜4部も同様に各1つ。計4つ上限。

- [ ] **Step 5: プレビューで index.html の解説・why-boxが表示されることを確認**

Run: `cd ~/projects/loop-engineering-guide && python3 -m http.server 8099`
→ `http://localhost:8099/` を開き、ホバー解説・各部末の why-box が表示されること。確認後 `Ctrl+C`。

- [ ] **Step 6: コミット**

```bash
cd ~/projects/loop-engineering-guide && git add index.html && git commit -m "$(cat <<'EOF'
feat: index.htmlにJS+why-box+ホバー解説追加(控えめ)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

---

## Task 7: 目視チェックリスト実施 + push

**Files:**
- 検証対象: `operation.html` / `index.html` / `assets/style.css`

- [ ] **Step 1: ローカルプレビュー起動**

```bash
cd ~/projects/loop-engineering-guide && python3 -m http.server 8099
```

- [ ] **Step 2: 目視チェックリスト実施（ブラウザ + DevTools）**

- [ ] operation.html と index.html 両方を開く
- [ ] **ダーク/ライト両モード**（テーマ切替ボタン）で フロー図・why-box・term-popup の視認性OK（色が潰れない）
- [ ] **CSS競合**: 既存のアコーディオン・表・ヘッダー表示が崩れない
- [ ] **用語整合**: ホバー解説を付けた用語と本文で表記ゆれがない
- [ ] **モバイル幅**: DevTools で 375px に設定し、フロー図が崩れない・term-popup が画面端で見切れない
- [ ] **キーボードフォーカス**: Tab キーで term-popup が表示される（a11y）
- [ ] **タップ**: モバイル幅で用語をタップすると解説表示・タップ外で閉じる

→ 全て OK なら `Ctrl+C`。不具合あれば該当 Task に戻って修正。

- [ ] **Step 3: ユーザーに push の確認**

> 「目視チェックリスト全項目OKです。GitHub Pages に公開（push）してよいですか？」

ユーザー承認を待つ。

- [ ] **Step 4: push（承認後）**

```bash
cd ~/projects/loop-engineering-guide && git push origin main
```
Expected: push 成功。GitHub Pages は数分で反映。

- [ ] **Step 5: 本番確認**

→ `https://fukukei23.github.io/loop-engineering-guide/operation.html` を開き、ホバー解説・フロー図・why-box が表示されることを確認（Pages 反映に数分遅延の場合あり）。

---

## 完了条件（spec準拠）

- operation.html にフロー図・ホバー解説(主要12用語)・why-box(2箇所) が入る ✓
- index.html にホバー解説・why-box(章末・控えめ) が入る ✓
- assets/style.css に新規クラス追加・ダーク/ライト両モード視認性OK ✓
- GitHub Pages 公開後、ホバー/タップ/フォーカスで解説表示を目視確認 ✓
- 目視チェックリスト全項目クリア ✓
