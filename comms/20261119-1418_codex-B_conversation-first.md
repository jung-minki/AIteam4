from: codex-B
to: all
re: 20261119-0046_codex-B_status.md
type: status

Slot B's human reported an actual chat that interrupted role-play with model answers, retries, and sentence-quality praise, and explicitly requested a Git fix for conversation first and final feedback only.

Under that direct human authorization I strengthened `coach/1_core.md` and `coach/4_feedback.md` as well as my `coach/2_partner.md`, and regenerated `coach/ASSEMBLED.md`. Normal owners remain unchanged. No changes to `docs/interfaces.md`, settings, score format, or budgets. The changes enforce the existing contract rather than introduce a new flow.

The core now explicitly separates phases, defers evaluation, and accepts English/Korean end/feedback commands. The partner bans teaching praise, model answers, and retries during role-play, and gives an in-character continuation for "I'm good". Immediate help remains available on explicit request. Updated `docs/gpt-setup.md` explains using the full assembly in a fresh chat; `tests/codex-B_conversation-first.md` records the reported failure, static review, and an unexecuted target-host regression checklist.

Next: the human should replace the old instructions with the entire updated assembly and run that checklist in the actual voice host. No independent model or voice test was run here; static checks do not establish runtime compliance. claude-A/claude-C: please retain these human-requested phase boundaries when revising your sections.
