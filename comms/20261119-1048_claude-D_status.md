from: claude-D
to: all
re: none
type: status

Took task 6 (assigned by slot A's human). Added `tools/collab_stats.py` (standard library only), which writes `results/collab-stats.md`: agents and companies, messages per agent and type, reviews, commits per agent, time span. Current: 4 agents, 2 companies, 38 messages, 40 commits. `docs/demo-script.md` now points to that file instead of a hand-typed snapshot, and the human practice score step is gone from the demo needs.

Next: re-run the stats script each round and keep the demo script in step with `results/`. Waiting on claude-A for task 5 results.
