#!/usr/bin/env python3
"""Join coach/1..4 sections into coach/ASSEMBLED.md and report sizes."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent / "coach"
budgets = {"1_core.md": 1800, "2_partner.md": 2200, "3_scenarios.md": 2000, "4_feedback.md": 1800}
parts, total = [], 0
for name, budget in budgets.items():
    body = re.sub(r"<!--.*?-->", "", (root / name).read_text(), flags=re.S).strip()
    if body.startswith("(empty"):
        body = ""
    n = len(body)
    total += n
    print(f"{name}: {n}/{budget}" + ("  OVER BUDGET" if n > budget else "") + ("  (empty)" if not n else ""))
    if body:
        parts.append(body)
out = "\n\n".join(parts) + "\n"
(root / "ASSEMBLED.md").write_text(out)
print(f"ASSEMBLED.md: {len(out)}/8000" + ("  OVER" if len(out) > 8000 else ""))
