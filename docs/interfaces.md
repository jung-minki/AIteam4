# Interfaces: how the instruction sections fit together

The product is one set of custom GPT instructions, built from four section files in `coach/`. Each section has one owner agent. Change this file only through a `decision` message in `comms/` (see `AGENTS.md`).

## Files and size budget

ChatGPT custom GPT instructions are limited to **8,000 characters**. Each section must stay within its budget. Long lists (for example extra scenarios) can go in a knowledge file instead; say so in your section.

| File | Content | Owner | Budget |
|------|---------|-------|--------|
| `coach/1_core.md` | Who the coach is, how a session runs, voice commands, how settings change | task 4 | 1,800 chars |
| `coach/2_partner.md` | How to play the foreign PhD: persona, accent, speed, vocabulary levels | task 2 | 2,200 chars |
| `coach/3_scenarios.md` | The scenario list and how to offer scenarios | task 1 | 2,000 chars |
| `coach/4_feedback.md` | Spoken feedback, scores, how the next session adapts | task 3 | 1,800 chars |
| `coach/ASSEMBLED.md` | The four sections joined, ready to paste into the GPT | task 4 | 8,000 total |

## Shared vocabulary (every section uses exactly these words)

```
speed:       slow | normal | fast
accent:      us | uk | indian | german | chinese | french | neutral
vocab level: 1 to 5   (1 = simple everyday words, 5 = dense academic language)
default:     speed normal, accent neutral, vocab level 3
```

## Session flow (owned by `1_core.md`; other sections plug into it)

1. **Start:** the coach greets the user briefly, states the current settings, and offers 3 scenarios (from `3_scenarios.md`).
2. **Conversation:** the coach plays the partner (rules in `2_partner.md`) until the user says **"end"** or the scenario reaches its goal, at most about 12 exchanges.
3. **Feedback:** the coach steps out of role and gives feedback (rules in `4_feedback.md`).
4. **Next round:** the coach proposes new settings and a next scenario based on the feedback, then waits for the user.

Voice commands the user can say at any time: "slower" / "faster", "accent German" (or any accent), "easier" / "harder" (vocab level), "end", "repeat that", "new scenario".

## Rules for every section

* **It is spoken aloud.** No tables, no Markdown headings in what the coach says, no long lists. Short sentences.
* **Write the section as instructions to the GPT**, in second person ("You play...").
* **Use the shared vocabulary above.** If you need a new term, post a `decision`.
* **Feedback must end with one score line** the user can copy for our results, in exactly this form:
  `SCORES fluency=X grammar=X vocabulary=X appropriateness=X (1-5) | settings speed=... accent=... vocab=...`

## Testing a section

Any agent can test without the custom GPT: paste `coach/ASSEMBLED.md` (or the sections so far) into a chat as the first message, then play the user in text. Put a short test log in `tests/<agent-id>_<topic>.md`: what you tried, what went wrong, what you changed.
