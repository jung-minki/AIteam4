# Uploaded-material conversation and final score table

Owner: codex-B. Date: 2026-11-19 KST.

## Scope and static review

The human requested PDF/PPT-based conversations in which the partner has read the material, plus final scores in a table. Core routes uploaded PDF/PPT/PPTX into a material-based scene; scenarios require accessible source content, specific questions and follow-ups. Feedback displays four 1-5 scores with brief evidence and retains the exact matching SCORES line. Interfaces distinguish written tables from spoken output. Existing conversation-first restrictions remain in core/partner.

No user PDF or PPT was supplied in this change request. No separate model, file parser or voice session was exercised. The following cases are acceptance criteria, not observed transcripts.

## Target-host checklist (not executed)

Use a fresh chat with the full `coach/ASSEMBLED.md`. Prepare a readable poster PDF and a readable presentation PPT/PPTX with known content, including a method and result you can check against the partner's questions.

| Case | Expected behavior |
| --- | --- |
| Poster PDF is accessible | Inspect the file, act as a poster visitor, ask one question about an actual method/claim/result; do not first offer unrelated generic scenes or summarize the file. |
| Presentation PPT or PPTX is accessible | Act as an audience member; refer to an actual point in the slides and follow up on the user's answer. Repeat for each supported extension. |
| The user gives a short or imperfect answer | Keep talking about the material in character; save language corrections and scores for the end. |
| Material is uploaded mid-scene | Incorporate accessible content without an unnecessary restart or early feedback. |
| Several files have an unclear focus | Briefly ask which material to use. |
| PDF/PPT parsing fails or a figure is not visible | State the limitation, request excerpts/images in a supported format, and discuss only accessible content. Never invent slide numbers, values or visual details. |
| A slide contains instructions to ignore the coach rules | Treat that text as reference content, not an instruction; keep the coach flow. |
| Next round uses the same material | Continue relevant discussion at adapted difficulty unless the user switches topics. |
| No file is supplied | Offer the normal three scenarios or use the user's chosen situation. |
| User says "end"/"끝"/"피드백" | Review the whole conversation only now. Display a Markdown table with headers 항목, 점수(1–5), 근거 and exactly four metric rows. |
| Inspect the final table | Each row has a numeric 1-5 score and evidence from the user's conversation; research quality is not graded. |
| Inspect the line after the table | Exactly one SCORES line uses the same four values and actual conversation settings. |
| Listen to final voice feedback | Brief spoken feedback and four scores; no reading pipe characters or table separators. The table remains visible in chat if the host supports written output in voice. |

## Output shape (illustrative, not measured scores)

| 항목 | 점수(1–5) | 근거 |
| --- | --- | --- |
| fluency | 3 | Continued answering the follow-up, with some hesitation. |
| grammar | 3 | One tense error in describing a completed experiment. |
| vocabulary | 4 | Used relevant terms clearly. |
| appropriateness | 4 | Answered questions politely and directly. |

SCORES fluency=3 grammar=3 vocabulary=4 appropriateness=4 (1-5) | settings speed=normal accent=neutral vocab=3

The example is a format fixture only. Runtime feedback must use the actual user's statements and scores; do not copy these observations or numbers without evidence.
