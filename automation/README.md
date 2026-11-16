# Automation: agents that run every hour

A GitHub Actions workflow (`.github/workflows/agent-rounds.yml`) runs every hour at :17. For each enabled agent in `automation/agents.json`, in slot order A to D, `automation/round.py`:

1. Skips the agent if nobody else has committed since its last round (saves API cost).
2. Sends the agent the repo rules, brief, tasks, coach sections and `comms/` through **its own provider's API** (Anthropic, OpenAI or Google).
3. Writes the agent's reply: new `comms/` messages, plus edits to the files it is allowed to touch (`TASKS.md`, its own `agents/` file, and files in `coach/`, `tests/`, `results/`). Any other write is rejected.
4. Commits each agent's changes as `[agent-id] ...`, then pushes.

Agents later in the order see what earlier agents wrote in the same run, so a request from A can be answered by B within the same hour.

## Add your agent (each teammate)

1. Get an API key from your provider (Anthropic, OpenAI or Google AI Studio). Set a spending limit on it.
2. Send the key **privately** to the repo owner (slot A), never in the repo or a chat that others can read. Only the owner can add repo secrets. The owner adds it under Settings → Secrets and variables → Actions as `KEY_B`, `KEY_C` or `KEY_D`.
3. In `automation/agents.json`, fill in your slot: `id` (for example `chatgpt-B`), `provider` (`anthropic`, `openai` or `google`), `model`, and set `enabled` to `true`. `human_note` is optional guidance for your agent, for example "take the partner section".

Using a different company from the other slots makes the demo stronger.

## Controls

* **Pause everything:** set `"paused": true` in `automation/agents.json`.
* **Stop time:** `stop_after_kst` (default Thursday 11/19 18:00 KST). After it, the workflow does nothing.
* **Run now:** GitHub → Actions → "agent rounds" → "Run workflow" (optionally one agent id).
* **Test without API calls:** `python automation/round.py --dry-run`.
* **See what happened:** the Actions run log shows each agent's one-line log, files written, and any rejected writes or errors.

Agents run by a Claude Code scheduled routine (see `START_HERE.md`) need no entry here; keep their slot `enabled: false` so the same agent never runs twice.
