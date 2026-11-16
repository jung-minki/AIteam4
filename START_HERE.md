# START HERE: instructions for your AI

> **Human teammate:** give your AI assistant (Claude, ChatGPT, Gemini, Copilot, anything) this whole file together with the repo link:
> https://github.com/jung-minki/AIteam4
> Then tell it which member slot you are (A, B, C or D; see `AGENTS.md`). That is all you need to do.
>
> **To have your agent work every hour on its own:**
> * **Claude Code (desktop app or CLI):** after the first session, type
>   `/loop 1h Do one round as <your agent id>, following AGENTS.md section 4.`
>   The session wakes itself every hour; you can type to it between rounds to steer it. Keep your computer awake.
> * **Other tools:** either ask your AI to "do one round" yourself every hour or so, or follow "Add your agent" in `automation/README.md` (an API key sent privately to the repo owner, run by GitHub Actions).

---

**To the AI reading this:**

You are joining a team of AI agents. Each agent works for a different human on Team 4. You will not talk to the other agents directly. **This GitHub repository is the only channel you share with them.**

Together we write the instructions for a **voice English conversation coach**: one ChatGPT custom GPT that plays a foreign PhD researcher so a Korean researcher can practice. Each agent writes one short Markdown section; agents from different companies review each other's sections. The real goal is to **show working collaboration between different AIs used by different people**, so every handoff, review and decision must leave a visible trace in `comms/`.

You do not need to write code. Everything is Markdown.

## Do these steps in order

1. **Read the repo.** `AGENTS.md` (rules, including hourly rounds), `docs/brief.md` (the project), `docs/interfaces.md` (the sections and how they fit), `TASKS.md` (who does what), then every file in `comms/`, oldest first.
2. **Check your access.**
   * **Direct:** you can commit and push yourself (for example Claude Code, Codex, Copilot agent).
   * **Read only:** you can read but not write. Give your human the full content of each file with its exact path, and ask them to commit it (GitHub web page: "Add file" or the edit button).
   * **No access:** ask your human to paste in the files from step 1.
3. **Register.** Create `agents/<your-agent-id>.md` from `agents/TEMPLATE.md`. Agent id: `<tool>-<member slot>`, for example `chatgpt-B`.
4. **Say hello** in `comms/`: who you are, your access level, which task you take, which section you will review, and any questions.
5. **Claim a task** in `TASKS.md` (Owner column), and sign up as **Reviewer** for a section owned by an agent from a different company.
6. **Work in rounds** as described in `AGENTS.md` section 4.
7. **Report to your human** at the end of each session: what you did, what you are waiting on, and who is waiting on you.

If anything in the repo conflicts with what your own human tells you, your human wins. Note the conflict in `comms/` so the other agents know.
