# TASKS

Claim a task by writing your agent id in the Owner column and committing. Never take a task someone else owns; send them a `request` in `comms/` instead. Status: `open`, `doing`, `review`, `done`, `blocked`.

Every section (tasks 1 to 4) is **reviewed by an agent from a different company** before it counts as done. The reviewer posts an `answer` in `comms/` with concrete suggestions; the owner applies them or explains why not.

| # | Task | Owner | Reviewer | Status | Notes |
|---|------|-------|----------|--------|-------|
| 1 | Scenario section (`coach/3_scenarios.md`) | claude-D | codex-B | review | base it on the list in `docs/brief.md` |
| 2 | Partner section: persona, accent, speed, vocab levels (`coach/2_partner.md`) | codex-B | claude-A | done | the accent setting is our key feature |
| 3 | Feedback section: spoken feedback, scores, adaptation (`coach/4_feedback.md`) | claude-C | codex-B | review | must end with the SCORES line, see `docs/interfaces.md` |
| 4 | Core section, assembly into `coach/ASSEMBLED.md`, set up the custom GPT, voice test | claude-A | codex-B | doing | a v0 of `coach/1_core.md` exists; owner may rewrite it |
| 5 | Results: write `results/protocol.md`, collect before/after scores and the vocab level comparison | | | open | from Tuesday |
| 6 | Collaboration stats: count agents, companies, messages, reviews, commits per agent from `comms/` and git log | | | open | for the slides |
| 7 | Slides and demo script | | | open | humans plus any agent |
