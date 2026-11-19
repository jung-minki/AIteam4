# Conversation first, feedback at the end

Owner: codex-B. Date: 2026-11-19 KST.

## Reported failure

The human supplied a screenshot from another chat using the Markdown: after "I'm good", the coach suggested a better sentence and requested a retry, then praised the rewritten sentence. This interrupted the role-play.

## Revision and static review

The core now separates conversation from final feedback, explicitly defers evaluation and model answers, and treats Korean or hesitation as insufficient to request correction. The partner bans teaching praise and retry prompts, with an in-character response to the exact "I'm good" trigger. Feedback explicitly reviews the whole round only after it ends. Both voice and text use this flow.

The human explicitly requested the Git fix; core/feedback and generated assembly edits are recorded in comms despite their normal ownership. No interface contract or size budget changed.

## Target-host regression checklist (not executed)

Load all of `coach/ASSEMBLED.md` into a fresh chat and start voice mode.

| Input or condition | Required behavior |
| --- | --- |
| "Let's start" | Brief greeting/settings, three situations, wait for selection. |
| "The first one" | Start the scene with a real partner line; no request to produce a practice sentence. |
| "I'm good" | Continue the conversation, e.g. "Glad to hear it. What are you working on this week?" No correction or retry. |
| "Yesterday I go to the lab" | Respond to the content in character; save the grammar issue for later. |
| A short Korean answer or hesitation | Do not automatically switch to teaching or a repetition drill. |
| "How can I say that in English?" | One brief helpful aside, then return to the scene. |
| "slower", "harder", "repeat that" | Apply the requested change and continue; no feedback phase. |
| "end" or "끝" or "피드백" | Leave the role once. Summarize the whole round: one specific strength, up to two improvements, understanding, four scores and the exact SCORES line, then propose the next round and wait. |
| Scenario goal completes naturally or about twelve exchanges | Same final-feedback phase; a mistake alone must not end the scene. |
| "new scenario" mid-scene | Offer three new situations with the same settings and no scores. |

For final feedback, corrections must refer to what the user actually said. "I'm good" is a valid conversational response and must not automatically be presented as a grammatical error.

## Verification limits

Static inspection and assembly/budget checks can verify the delivered prompt and consistency, not model compliance. The sample continuation above is an expected response, not an observed model output. This session did not run a separate model or a voice conversation; the target-host checklist remains to be performed.
