# Module interfaces (the contract between agents)

Each module belongs to one agent. A module is a Python function that takes a dict and returns a dict, matching the shapes below. Change this file only through a `decision` message in `comms/` (see `AGENTS.md`).

These are **starting proposals**. The first agent to own a module may refine its shape by posting a `decision`.

## Shared types

```python
Difficulty = {
    "speed": "slow" | "normal" | "fast",          # used by speech output, and as a hint to keep turns short at "slow"
    "accent": "us" | "uk" | "indian" | "german" | "chinese" | "french" | "neutral",   # style hint for text, voice choice for speech
    "vocab_level": 1 | 2 | 3 | 4 | 5              # 1 = simple everyday words, 5 = dense academic language
}

Turn = {"speaker": "coach" | "user", "text": str}
```

## Module 1: Scenario generator → folder `app/scenario/`

```python
def suggest_scenarios(req: dict) -> dict
# req:  {"user_profile": {"field": str, "goals": [str]}, "past_feedback": [Feedback] | [], "n": int}
# returns: {"scenarios": [{"id": str, "title": str, "setting": str,
#                           "partner_role": str, "user_goal": str, "opening_line": str}]}
```

## Module 2: Conversation partner → folder `app/partner/`

```python
def next_turn(req: dict) -> dict
# req:  {"scenario": Scenario, "difficulty": Difficulty, "history": [Turn]}
# returns: {"text": str, "done": bool}
```

## Module 3: Feedback coach → folder `app/feedback/`

```python
def give_feedback(req: dict) -> dict
# req:  {"scenario": Scenario, "difficulty": Difficulty, "history": [Turn]}
# returns: Feedback = {
#   "scores": {"fluency": 1-5, "grammar": 1-5, "vocabulary": 1-5, "appropriateness": 1-5},
#   "corrections": [{"original": str, "better": str, "why": str}],
#   "tips": [str],
#   "suggested_next_difficulty": Difficulty
# }
```

## Module 4: App and integration → folders `app/` (main loop), `app/llm.py`, `app/speech/` (optional)

* `app/llm.py`: `complete(prompt: str, system: str = "", provider: str = "openai" | "anthropic" | "google") -> str`, reading keys from environment variables.
* `app/main.py`: command line loop: pick scenario → converse → feedback → next session uses the suggested difficulty.
* Optional speech: text to speech with the speed and accent settings, speech recognition for the user's turns.

## Testing each module alone

Every module folder should contain `example_input.json` and a way to run it alone, for example `python -m app.scenario example_input.json`, so other agents can try it without the rest of the app.
