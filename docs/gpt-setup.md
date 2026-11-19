# Custom GPT setup notes (task 4, claude-A)

A human must do these steps; no agent has done them yet.

1. Run `python3 tools/assemble.py` (or open `coach/ASSEMBLED.md` on main after the last section is merged). Check it prints under 8,000 characters and no section says OVER BUDGET.
2. In ChatGPT: Explore GPTs > Create > Configure.
3. Name: "Research English Coach". Instructions: paste all of `coach/ASSEMBLED.md`.
4. Conversation starters: "Start a practice conversation", "Host a visiting researcher", "Ask a question after a seminar".
5. Capabilities: web search and image generation are not needed. If the host requires file/data-analysis tools to inspect PDF/PPT/PPTX, enable those for material-based practice.
6. Save as "Only me" or link-sharing for the team.
7. Test in the mobile app voice mode: say "slower", "accent German", "harder", "end". Log results in `tests/humanX_voice.md`.
8. Voice mode may ignore the exact accent. Note in the log which accents are convincing; the demo should use those.

## Using the Markdown in another chat

Use the entire current `coach/ASSEMBLED.md`, not just the partner or feedback section. In a new chat, paste its contents as the operating instructions (or attach it and explicitly ask the model to follow it), then start voice mode. Say "Let's start" and choose a scenario, or name your own situation. The Markdown supplies the conversation rules; the host provides voice input and output.

The coach must stay in character during practice, including after short or imperfect answers. It must not give model answers, praise the quality of each sentence, or ask for a retry. Say "end", "feedback", "끝", or "피드백" to receive feedback on the whole conversation. A scene also ends naturally when its goal is complete or after about twelve exchanges. "new scenario" switches scenes without scoring.

After updating the file, replace the old instructions and test in a new chat. Use `tests/codex-B_conversation-first.md` for the regression checklist. Voice behavior still needs a real run in the target host.

## Poster and presentation practice

Load the full current `coach/ASSEMBLED.md`, then upload the poster or presentation as PDF, PPT or PPTX in the same chat before starting voice mode. For example: "이 자료를 읽은 학회 참석자라고 생각하고 영어로 대화해줘." If the host supports attaching files during voice, material can also be introduced mid-conversation.

The partner first inspects accessible content and then asks relevant questions as a poster visitor or talk attendee, following up on your answers. It keeps using the material in the next round unless you switch topics. It does not summarize the entire file or interrupt with language corrections. If file access or figure visibility is unavailable, supply readable excerpts or slide images in a supported format; the partner must not claim to have read unseen content.

At the end, scores appear in the chat as a table: `항목 | 점수(1–5) | 근거`, with fluency, grammar, vocabulary and appropriateness as the four rows. Voice also gives a brief spoken score summary without reading Markdown symbols. The existing `SCORES ...` line remains below the table for results logging and must match its values. These are conversation scores, not a scientific review grade for the uploaded work.

See `tests/codex-B_materials-score-table.md` for the target-host checklist. PDF/PPT parsing, visual access and display of a written table depend on the host; verify them in the actual session.
