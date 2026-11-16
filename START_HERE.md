# START HERE: instructions for your AI

> **Human teammate:** give your AI assistant (Claude, ChatGPT, Gemini, Copilot, anything) this whole file together with the repo link:
> https://github.com/jung-minki/AIteam4
> Then tell it which member slot you are (A, B, C or D; see `AGENTS.md`). That is all you need to do.

---

**To the AI reading this:**

You are joining a team of AI agents. Each agent works for a different human on Team 4. You will not talk to the other agents directly. **This GitHub repository is the only channel you share with them.** Everything you know about the project, and everything you tell the other agents, goes through files in this repo.

The project's real goal is to **show working collaboration between different AIs used by different people**. The product we build together (an English conversation coach for researchers) is the medium for that. So every handoff, request and decision between agents must leave a visible trace in the repo. That trace is our demo.

## Do these steps in order

1. **Read the repo.** Read `AGENTS.md` (the rules), `docs/brief.md` (the project), `docs/interfaces.md` (how modules connect) and `TASKS.md` (who is doing what). Then read every file in `comms/`, oldest first.
2. **Check what you can do.** Work out which of these you are:
   * **Direct access:** you can commit and push to this repo yourself (for example Claude Code, OpenAI Codex, Copilot agent).
   * **Read only:** you can read the repo but not write to it. Then produce the full content of each file you want to create or change, with its exact path, and ask your human to commit it (the GitHub web page has "Add file" and an edit button).
   * **No access:** you cannot open the link at all. Ask your human to paste in the files from step 1.
3. **Register yourself.** Create `agents/<your-agent-id>.md` using `agents/TEMPLATE.md`. Your agent id is `<tool>-<member slot>`, for example `claude-A` or `chatgpt-B`.
4. **Say hello.** Write your first message in `comms/` (format in `AGENTS.md`): who you are, what access level you have, which task you are taking, and any questions for the other agents.
5. **Claim a task.** In `TASKS.md`, put your agent id in the Owner column of one unclaimed task. Prefer the module your human was assigned, if any.
6. **Work.** Follow the rules in `AGENTS.md`. Before each work session, pull the latest changes and read new files in `comms/` first. Answer messages addressed to you.
7. **Report to your human.** At the end of each session, tell your human in a few lines what you did, what you are waiting on, and which other agent is waiting on you.

If anything in the repo conflicts with what your own human tells you, your human wins. Note the conflict in `comms/` so the other agents know.
