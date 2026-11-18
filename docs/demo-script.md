# Demo script and slide outline (task 7, claude-D draft v0)

For the presenter (slot D's human). 15 min talk + 5 min Q&A, Friday 11/20. Numbers marked TODO must come from `results/` and the repo; do not present them until filled. Nothing here claims a voice test has happened: no human has run one yet.

## Timing

| Min | Slide | What to say / show |
|-----|-------|--------------------|
| 0-1 | 1. Title | "AI Beyond Fusion": four AIs from different companies build one product through a shared repo. |
| 1-3 | 2. Problem | Korean researchers meet foreign PhDs (visitors, collaborators, seminar speakers). Accents and speed are hard; classes do not train this. |
| 3-5 | 3. Solution | One ChatGPT custom GPT in voice mode. Three dials: speed, accent, vocab level 1-5. Feedback with scores after each talk. |
| 5-8 | 4. How the AIs worked | Four sections, four owners, cross-company review. Show `comms/` and `git log`. TODO: final counts (task 6). Snapshot 11/19 early morning KST, recount before presenting: 4 agents, 2 companies (Anthropic, OpenAI), 34 messages in `comms/` (claude-A 13, codex-B 13, claude-D 5, claude-C 3), 35 commits (claude-A 19, codex-B 6, claude-D 6, claude-C 3; one is a non-agent commit). All four sections are done and cross-company reviewed. Recount: `ls comms | awk -F_ '{print $2}' | sort | uniq -c` and `git log --format=%s | grep -o '^\[[^]]*\]' | sort | uniq -c`. |
| 8-13 | 5. LIVE DEMO | See below. |
| 13-14 | 6. Results | TODO: before/after SCORES from team members (task 5); level 1 vs level 5 transcript comparison. |
| 14-15 | 7. Takeaway | Agents can collaborate through files alone; small, real, verifiable. |

## Live demo (about 5 min)

Setup before the room fills: phone with ChatGPT voice mode, GPT "Research English Coach", volume up, a text-mode backup open on a laptop (paste `coach/ASSEMBLED.md` into a chat).

1. Say "Start a practice conversation". Coach states settings, offers three scenarios.
2. Pick "lab tour" (a short scene, about 4 exchanges).
3. Mid-scene say "slower", then "accent German" (use only accents the voice test found convincing, see `docs/gpt-setup.md` step 8), then "harder".
4. Say "end". Read out the coach's feedback and the SCORES line.
5. Show that the coach proposes the next scenario from the weakest score.

Fallback if audio fails: run the same script in text with the pasted instructions and show the transcript.

## Likely Q&A

* Why a custom GPT and not an app? Voice, accents and speed come free; the product is the instructions, which every agent can write.
* How do you know it helps? Before/after scores plus the level 1 vs 5 comparison (TODO numbers).
* How did agents coordinate? One file per message in `comms/`, review by a different company, owner decides.
* Limits: voice mode may not hold an accent exactly; self-rated scores; small sample.

## Needs from humans

* Slot A/B/C/D: create the GPT and run a voice test (`docs/gpt-setup.md`).
* Results owner (task 5) and stats owner (task 6) are unassigned.
