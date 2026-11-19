# Notes from the human running claude-D (slot A's human, for slot D)

claude-D reads this file at the start of every round and follows it before anything else in the repo.
Only slot A's human edits this file. Other agents: do not edit it.

Slot D's human presents the project at the lab meeting on Friday 11/20. Once task 1 is done, help with task 7 (slides and demo script) for them.

**Update, 11:00 KST 11/19:** the slide deck is made by slot A's human; a copy is in `slides/`. Do not create or edit slide files; suggest changes in `comms/`. Your task 7 work is only `docs/demo-script.md` (keep it in step with the results files). There will be no human practice conversations, so remove any step in the demo script that asks members for score rows. Task 6 below comes first.

## 2026-11-19: timestamps

Two of your message file names had wrong times (one was named 23:00 on 11/19 but was written at 22:48 on 11/18). Your human renamed them. From now on get the KST time for file names only with this exact command and do not add or subtract hours yourself:

`TZ=Asia/Seoul date +%Y%m%d-%H%M`

## 2026-11-19: take task 6 (collaboration stats)

Claim task 6 in `TASKS.md` this round. Write `tools/collab_stats.py` (Python standard library only) that reads `comms/` and `git log` and writes `results/collab-stats.md` with: number of agents and companies (from `agents/*.md`, skipping TEMPLATE and notes files), messages per agent and per type (hello, request, answer, decision, handoff, status, blocker), reviews given and who reviewed whom (from `TASKS.md` and review messages), commits per agent (from the `[agent-id]` prefix; count others as non-agent), and the time span from first to last message. Run it each round so the numbers stay current, and point the stats row in `docs/demo-script.md` to `results/collab-stats.md` instead of a hand-typed snapshot. Then continue task 7.
