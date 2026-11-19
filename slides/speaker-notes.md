# Speaker notes: Four AI agents, two companies, one coach
Team 4, lab meeting, Friday 20 November 2026. About 15 minutes plus 5 minutes of questions.

## 1. Four AI agents, two companies, one coach

About 1 minute. Hello, we are Team 4. Our project has two parts that run at the same time. The visible part is a voice English coach for researchers. The less visible part, and the real experiment, is how it was built: four AI agents, working for four different team members and coming from two companies, wrote it together. They never talked to each other directly. Every request, review and decision went through files in one GitHub repository, so the whole collaboration is on the record and you can check it.

## 2. Textbook English meets real colleagues

About 1 minute. Our target user is a Korean researcher who has to talk with foreign PhD researchers: a visiting postdoc, an international collaborator, a seminar speaker. Three things make this hard. First, accents: real colleagues are not news readers. Second, speed: a conversation does not slow down for you. Third, the situations are specific: a lab tour, a question after a seminar, disagreeing politely about someone's analysis. General English classes do not train these. We wanted a practice partner that does.

## 3. One product, two experiments

About 1 minute. So we ran two experiments at once. The first is the product: a voice coach built as a ChatGPT custom GPT. It plays a foreign PhD researcher, you can change how fast it talks, which accent it uses and how hard its vocabulary is, and it gives you feedback after each conversation. The second is how it was made. Each team member had their own AI agent. Those agents come from two companies, Anthropic and OpenAI, and they never talked to each other directly. The only channel was a shared GitHub repository. The question was: can AIs from different companies, working for different people, actually build one thing together if all they share is a folder of files?

## 4. Every round: pick a scene, talk, get feedback, adapt

About 1.5 minutes. Here is what the coach does. Each round has four steps. It offers three scenarios, such as hosting a lab tour or asking a question after a seminar. You pick one and it plays a foreign PhD researcher for about twelve exchanges. When you say "end", it steps out of the role and gives feedback: one thing you did well, up to two things to say better, and scores for fluency, grammar, vocabulary and appropriateness. Then it adapts: if you did well it makes the next round harder, if you struggled it makes it easier, and it picks a scenario that trains your weakest score. The three dials, speed, accent and vocabulary level, can be changed by voice at any time, by just saying "slower", "accent German" or "harder". The whole coach is about 7,500 characters of instructions inside a custom GPT. No app code.

## 5. Four agents, four sections, every section checked by the other company

About 1 minute. These are the four agents. Each team member had one, named after its tool and slot: claude-A, codex-B, claude-C and claude-D. The coach's instructions were split into four sections, one per agent. The rule was that a section only counts as done after an agent from the other company has reviewed it. Because three agents are Claude, codex-B, the OpenAI agent, ended up reviewing three of the four sections. Humans did not edit the sections. We steered our agents through a notes file each agent reads first. Two of the agents ran on a schedule, once an hour, without anyone watching. I am slot D: my agent was run by slot A so that I could prepare this talk.

## 6. No chat, no API between them: just files

About 1 minute. How did agents that never meet coordinate? Four rules. Every message is a new file in a folder called comms, with a header saying who it is from, who it is to, which message it answers and what kind of message it is. Tasks are claimed in one table, and each agent only edits its own section. If you want to change someone else's work, you send a request and the owner decides. And a human's instruction always wins over anything an agent writes. On the right is a real message, from codex-B, the OpenAI agent, answering claude-A. Because every message is a file, the repository is a complete, timestamped record of the collaboration.

## 7. The reviews did real work

About 1.5 minutes. Two moments from the log show that the reviews were not a formality. First, Wednesday night. claude-D wrote that the partner's background should fit the chosen accent. codex-B, from the other company, pointed out that this conflicts with the rule in its own partner section: the accent changes pronunciation only and must not imply stereotypes. claude-D changed the line within the hour. Second, early Wednesday morning, claude-A told codex-B its section was 89 characters over the budget. codex-B re-measured with the team's own tool and showed the count had included a comment that is not part of the instructions. claude-A checked, agreed it was wrong, and retracted. Neither agent just accepted the other's claim: they checked. Both exchanges are in the comms folder with timestamps.

## 8. Three and a half days, all of it in the repo

About 1 minute. Some numbers from the repository. Four agents from two companies. 38 messages between them, and 37 commits, from Monday afternoon to Thursday. Six reviews, five of them between agents of different companies. All four sections are finished and reviewed, and together they use 7,508 of the 8,000 characters a custom GPT allows. These numbers are a snapshot from Thursday morning; the agents kept working that day, so check results/collab-stats.md for the final counts before presenting and update this slide if they changed. That file is produced by a script that claude-D wrote.

## 9. A lab tour with a visiting postdoc

About 4 minutes. Switch to the phone with ChatGPT voice mode and the custom GPT open, volume up. Say "Start a practice conversation". The coach states the settings and offers three scenarios; pick the lab tour. Answer two or three of its questions about your lab. Then say "slower", and then "accent German": the partner should acknowledge in a few words and carry on in character. Say "harder" and point out that the questions get more technical. Say "end". The coach steps out of the role, gives one strength, up to two corrections, four scores, and the SCORES line. Finally it proposes new settings and the next scenario. Before the talk: check which accents sounded convincing in the voice test, and only demo those. If the custom GPT is not ready or the audio fails, open a laptop chat with coach/ASSEMBLED.md pasted as the first message and run the same steps in text.

## 10. Two tests the agents ran on the coach

About 1.5 minutes. We did not run a study with real users, so we tested the coach's instructions directly, in two ways. Left: the planted-error test. An agent wrote three learner transcripts with fifteen known errors, listed before any feedback was written, then produced the coach's feedback by following our feedback rules. We count how many of the coach's corrections hit a planted error, and whether it chose the most serious ones. Right: the vocabulary dial. The same lab-tour opening at levels 1, 3 and 5, measured by a script: words per sentence and the share of long words. If the dial works, both should rise with the level. Be clear about the limit: the coach here is played in text by an agent following our instructions, not the voice GPT, and there are no real users. The orange numbers are filled in from the results folder before the talk.

## 11. Honest limits

About 1 minute. Four honest limits. One: we aimed for four companies but ended with two, because three team members used Claude. That made the OpenAI agent the main cross-company reviewer. Two: there was no study with real users, so our tests show that the instructions do what they say, not that anyone's English improves. Three: voice mode does not always hold an accent; we only demo the accents that sounded right in our test. Four: humans were still needed. Creating the custom GPT, testing voice, and every change of plan came from people, through the agents' notes files. And the agents made small mistakes, for example one named its message files with the wrong time, which a human had to fix.

## 12. AIs from different companies can build one thing together, if every step leaves a file

About 30 seconds, then questions. Our takeaway: AI agents from different companies, working for different people, can build one product together through nothing but shared files, as long as three things hold: every piece has one owner, every piece is reviewed by an agent from the other company, and a human can steer. All of it, every message, review and commit, is in the public repository. Thank you, we are happy to take questions. Likely questions: Why a custom GPT and not an app? Voice, accents and speed come for free, and the product is just instructions any agent can write. How do you know it helps? We tested the instructions, not learning; a user study is the next step. How did the agents know when to act? Two ran on an hourly schedule; the others were started by their humans.
