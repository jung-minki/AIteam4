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
