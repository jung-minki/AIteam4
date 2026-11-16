# Project brief: Team 4

## The competition

* **Event:** a lab internal AI Agent Challenge. Theme: **"AI Beyond Fusion"**. Each team picks a problem outside fusion plasma research and solves it with AI. Any kind of AI use counts: agents, skills, prompts, workflows.
* **Presentation:** Friday, **November 20, 2026**, during lab meeting. Up to **15 minutes** of presentation plus **5 minutes** of Q&A. Slides and live demo are both allowed.
* **Judging:** 5 judges, 30 points each:
  * **Problem definition and creativity (10):** is the problem clear and interesting? Is the AI approach new?
  * **AI usage and problem solving process (10):** were suitable AI tools and methods chosen and used well?
  * **Results and completeness (10):** is there a real, meaningful result that is convincing and **verifiable**?
  * Each team's highest and lowest scores are dropped and the remaining three are averaged.
* **Organizer's guidance:** show a real result of using AI, not just an idea. A small problem solved well is enough.

## Our pitch

**Main claim:** AI agents from different companies, working for different people, can build one product together through a shared GitHub repo, with no direct connection between them.

**The product:** a **voice English conversation coach for researchers**. It is one ChatGPT custom GPT, used in ChatGPT's voice mode. What makes it ours is its **instructions**, and those instructions are written section by section by different AI agents in this repo.

Why this design (decided 2026-11-16):
* Voice mode gives us live speech, speaking speed and accents for free. No app code to build or debug.
* Every agent can contribute, even one that can only read the repo, because a section is just Markdown.
* The repo still records every handoff, review and decision between agents. That record is half of our demo.

How this maps to the judging:
* **Creativity:** the team itself is an AI experiment. Four AIs coordinate through files to write one coach.
* **AI usage:** each instruction section is owned by one AI and reviewed by an AI from a different company. `comms/` and the git history show every step.
* **Results:** a live voice demo, a before and after measurement, and collaboration stats from the repo.

## The coach: what it must do

1. **Adjustable difficulty** along three axes: **speed** of speech, **accent**, **vocabulary level**. The user changes them by voice ("slower please", "switch to a German colleague", "harder words").
2. **Feedback loop:** after each conversation the coach gives short spoken feedback with scores, and the next conversation adapts to it.
3. **Varied scenarios:** the coach offers many realistic practice situations.

## Target user (decided 2026-11-16)

The user is a Korean researcher practicing real conversations **with foreign PhD researchers**: visiting scholars, international collaborators, seminar speakers. The coach plays the foreign PhD.

Scenario examples:
* Hosting a visiting researcher: lab tour, explaining your equipment and research
* Asking questions after a seminar given by a foreign speaker
* Video meeting with an international collaborator: progress update, next steps
* Politely disagreeing about data or an analysis
* Small talk over lunch or dinner with a visiting professor
* Explaining your own research in two minutes to someone from a different field

The **accent** setting matters most here: the partner should sound like real international colleagues (for example German, Indian, Chinese, French, US, UK English), not only native speakers.

## How we show results are real

See `results/protocol.md` (task 5). At least:
* Each team member does one conversation before and one after a feedback round. Compare the coach's scores and the member's own rating.
* Show that the vocabulary level setting really changes what the partner says (same scenario at level 1 and level 5, compare the transcripts).
* Collaboration stats from the repo: agents, companies, messages, reviews, commits per agent.

## Schedule (compressed: agents work in hourly rounds, see `AGENTS.md`)

| When | Goal |
|------|------|
| Mon 11/16 | Agents registered, tasks claimed, first draft of every section. |
| Tue 11/17 | Cross reviews done, instructions assembled, custom GPT set up and tested in voice mode. |
| Wed 11/18 | Fixes from voice testing. Results measured. |
| Thu 11/19 | Slides, demo script, rehearsal. |
| Fri 11/20 | Present. |
