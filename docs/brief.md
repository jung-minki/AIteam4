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

## Open question (humans to decide)

The idea notes say the coach is for real conversations involving "overseas PhDs". This could mean:
* (a) Korean researchers preparing to go abroad (conferences, postdoc interviews, lab life), or
* (b) practicing conversations **with** foreign researchers (visiting scholars, collaborators).

The scenario list depends on this. Until decided, use academic scenarios that fit both: conference Q&A, poster session small talk, meeting a collaborator, lab meeting discussion, postdoc interview.

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
