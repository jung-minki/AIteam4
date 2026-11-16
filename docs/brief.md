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

**Main claim:** AI agents used by different people, built by different companies, can collaborate on one project through a shared GitHub repo, with no direct connection between them.

**The medium:** together, those agents build an **English conversation coach for researchers**, a bot that runs realistic practice conversations and coaches the user afterwards.

How this maps to the judging:
* **Creativity:** the team itself is an AI experiment. Four AIs coordinate through files.
* **AI usage:** each module is owned by a different AI. The `comms/` folder and git history show every handoff.
* **Results:** a working coach demo, plus the collaboration record as evidence (message count, handoffs, decisions, which agent wrote what).

## The coach: features from the team's idea notes

1. **Adjustable difficulty** along three axes:
   * **Speed** of speech
   * **Accent / intonation**
   * **Vocabulary level**
2. **Feedback loop:** after each conversation the coach gives concrete feedback, and the next session adapts to it.
3. **Varied scenarios:** the coach suggests many different practice situations.
4. **Agents cooperating** inside the product as well (scenario agent, conversation partner agent, feedback agent).

## Target user (decided 2026-11-16)

The user is a Korean researcher practicing real conversations **with foreign PhD researchers**: visiting scholars, international collaborators, seminar speakers. The bot plays the foreign PhD.

Scenario examples:
* Hosting a visiting researcher: lab tour, explaining your equipment and research
* Asking questions after a seminar given by a foreign speaker
* Video meeting with an international collaborator: progress update, next steps
* Politely disagreeing about data or an analysis
* Small talk over lunch or dinner with a visiting professor
* Explaining your own research in two minutes to someone from a different field

The **accent** setting matters most here: the partner should sound like real international colleagues (for example German, Indian, Chinese, French, US, UK English), not only native speakers.

## How we show results are real

Pick at least one before Thursday:
* Each team member does one conversation before and one after a feedback round. Compare feedback scores and self ratings.
* Show that the vocabulary level setting really changes output (for example a readability score or word frequency band per level).
* Collaboration stats from the repo: number of agents, providers, messages, handoffs, commits per agent.

## Schedule

| Day | Goal |
|-----|------|
| Mon 11/16 | Repo set up. Every agent registered and has said hello. Tasks claimed. |
| Tue 11/17 | Each module works on its own with sample input. |
| Wed 11/18 | Modules connected end to end (text only). |
| Thu 11/19 | Working demo by noon. Then results measurement, slides, rehearsal. Speech only if time allows. |
| Fri 11/20 | Present. |
