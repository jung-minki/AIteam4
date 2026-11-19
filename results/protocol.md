# Results protocol

All tests below are run by claude-A (an AI agent) in **text mode**. The coach is claude-A itself following `coach/ASSEMBLED.md` pasted as instructions, not the voice custom GPT. There are no human practice conversations and no human score rows. Nothing here says how the voice GPT sounds, or whether real users improve.

## Test 1: planted-error test (`results/planted-errors.md`)

- **Measures:** whether the feedback rules in `coach/4_feedback.md` find real mistakes and produce the exact SCORES line.
- **How:** claude-A writes 3 short learner transcripts (lab tour, seminar question, polite disagreement), about 8 turns each, as a Korean researcher might speak. Exactly 5 known errors are planted in each (grammar, wrong word, too casual or too blunt). The planted errors are listed before any feedback is written. The feedback is then written by following `coach/4_feedback.md` exactly. We count how many planted errors the corrections name, whether they are the most serious ones, and whether the SCORES line matches the required format.
- **Limits:** the transcripts and the feedback are written by the same agent, so errors may be easier to catch than real ones. The coach may name at most two errors by its own rules, so a catch rate of 2 of 5 is the ceiling. Three transcripts is a tiny sample. Text only, so pronunciation is not covered.

## Test 2: vocab level comparison (`results/vocab-levels.md`)

- **Measures:** whether vocab level 1, 3 and 5 make the partner's language measurably different.
- **How:** the same opening (lab tour, accent neutral, speed normal) is generated at levels 1, 3 and 5, about 80 words each, following `coach/ASSEMBLED.md`. `tools/vocab_stats.py` computes average sentence length, average word length and the share of long words for each sample.
- **Limits:** one scenario, one sample per level, generated in text, so one run may differ from another. The numbers show written complexity only, not how a listener hears it. Speed and accent are not tested.

## Not covered

Voice quality, accent rendering, speed in words per minute, and learning gains for real users. These need the voice GPT and humans.
