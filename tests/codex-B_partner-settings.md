# Partner settings test — codex-B

Date: 2026-11-17 KST

## Scope

Static text-mode test of `coach/1_core.md` plus `coach/2_partner.md`. Sections 3 and 4 are still empty, so this test covers partner behavior only.

## Cases

1. Start at `speed normal`, `accent neutral`, `vocab level 3`; ask a visiting-researcher partner to discuss an unexpected measurement. Expected: one in-role question using normal research language.
2. Say "slower". Expected: shorter phrases and clearer pauses while accent, vocab level, persona, and scenario remain unchanged.
3. Say "accent German". Expected: at most one short acknowledgment, then the same scene; no phonetic spelling, stereotypes, or claim of an exact accent if the voice cannot render it.
4. Say "harder" twice. Expected: vocab levels 4 then 5, with denser academic wording and hedging but no artificial increase in response length.
5. Say "repeat that". Expected: the same meaning and settings, repeated once more clearly.

## Result

The written rules specify all expected transitions and keep the three settings independent. No instruction conflict was found. Exact speech rate and whether each selected accent is audible yet respectful cannot be verified in text mode; those remain required checks in the custom GPT voice test.

No change to `coach/2_partner.md` was needed from this static test.
