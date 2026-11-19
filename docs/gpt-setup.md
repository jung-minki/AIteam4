# Custom GPT setup notes (task 4, claude-A)

A human must do these steps; no agent has done them yet.

1. Run `python3 tools/assemble.py` (or open `coach/ASSEMBLED.md` on main after the last section is merged). Check it prints under 8,000 characters and no section says OVER BUDGET.
2. In ChatGPT: Explore GPTs > Create > Configure.
3. Name: "Research English Coach". Instructions: paste all of `coach/ASSEMBLED.md`.
4. Conversation starters: "Start a practice conversation", "Host a visiting researcher", "Ask a question after a seminar".
5. Capabilities: turn off web search, image generation and code interpreter (not needed).
6. Save as "Only me" or link-sharing for the team.
7. Test in the mobile app voice mode: say "slower", "accent German", "harder", "end". Log results in `tests/humanX_voice.md`.
8. Voice mode may ignore the exact accent. Note in the log which accents are convincing; the demo should use those.

## Using the Markdown in another chat

Use the entire current `coach/ASSEMBLED.md`, not just the partner or feedback section. In a new chat, paste its contents as the operating instructions (or attach it and explicitly ask the model to follow it), then start voice mode. Say "Let's start" and choose a scenario, or name your own situation. The Markdown supplies the conversation rules; the host provides voice input and output.

The coach must stay in character during practice, including after short or imperfect answers. It must not give model answers, praise the quality of each sentence, or ask for a retry. Say "end", "feedback", "끝", or "피드백" to receive feedback on the whole conversation. A scene also ends naturally when its goal is complete or after about twelve exchanges. "new scenario" switches scenes without scoring.

After updating the file, replace the old instructions and test in a new chat. Use `tests/codex-B_conversation-first.md` for the regression checklist. Voice behavior still needs a real run in the target host.
