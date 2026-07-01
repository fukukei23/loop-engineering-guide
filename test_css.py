"""未定義CSS変数検出テスト — 文字消失（ダーク/ライトで文字が見えない）の再発防止.

【仕様・共通】claude-code-guide/test_convert.py の TestNoUndefinedCssVars と同一アルゴリズム。
  物理共通化は両repoの構造差（convert経由 vs 手書きHTML）に対し過剰コストのため見送り（YAGNI）。
  代わりに本ファイルと ccg 側で「同一仕様」を維持する。アルゴリズムを変える時は両方直すこと。

背景: html-guide スキルで --fg / --bg-raised 等の未定義変数を書き、operation.html の文字が
消えたバグが反復した。本テストは CI（static.yml の pytest ステップ）で push をガードする。

判定基準:
  - fallback なしの var(--xxx) で xxx が style.css or インライン<style> に未定義 → FAIL
  - fallback 付き var(--xxx, #fff) は許容（文字は見えるため再発リスクなし）
"""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).parent
CSS_PATH = ROOT / "assets" / "style.css"
_VAR_USE_RE = re.compile(r'var\((--[A-Za-z0-9_-]+)\s*(,[^)]+)?\)')


def _extract_defined_css_vars(text: str) -> set:
    """CSS / HTML テキストから --var 定義名を抽出（:root/[data-theme]/インライン問わず）."""
    return set(re.findall(r'(--[A-Za-z0-9_-]+)\s*:', text))


def _extract_var_uses_without_fallback(text: str) -> set:
    """fallback なしの var(--xxx) 使用の変数名を抽出."""
    return {m.group(1) for m in _VAR_USE_RE.finditer(text) if not m.group(2)}


class TestNoUndefinedCssVars:
    """全HTMLで、style.css 未定義のCSS変数を fallback なしで使っていないか検証."""

    def test_no_undefined_css_vars_without_fallback(self):
        css_text = CSS_PATH.read_text(encoding="utf-8")
        defined = _extract_defined_css_vars(css_text)

        problems = []
        for html_file in sorted(ROOT.glob("*.html")):
            content = html_file.read_text(encoding="utf-8")
            # 各HTMLのインライン <style> 定義も定義元に追加
            local_defined = defined | _extract_defined_css_vars(content)
            undefined = _extract_var_uses_without_fallback(content) - local_defined
            if undefined:
                problems.append(f"{html_file.name}: {sorted(undefined)}")

        assert not problems, (
            "未定義CSS変数(fallbackなし)を検出 — 文字消失リスク:\n  "
            + "\n  ".join(problems)
        )
