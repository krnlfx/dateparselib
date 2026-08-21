import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)


def test_regression_0():
 """Regression guard for a import edge case discovered earlier."""
 from dateparselib.features.feature-import-0 import run_import
 result = run_import("sample-0", timeout=5)
 assert result["ok"] is True
 assert "value" in result