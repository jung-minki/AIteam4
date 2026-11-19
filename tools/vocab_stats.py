#!/usr/bin/env python3
"""Text complexity stats for the vocab-level samples.

Usage: python3 tools/vocab_stats.py results/samples/level*.txt

Measures (written text only, simple and reproducible):
- avg sentence length: words per sentence (sentences split on . ! ?)
- avg word length: letters per word
- long-word share: words with 3 or more syllables, estimated by counting
  vowel groups (rough, English-only heuristic, silent 'e' dropped).
- type/token ratio is not used: too noisy for ~80 word samples.
"""
import re
import sys


def syllables(w):
    w = w.lower()
    if w.endswith("e") and not w.endswith(("le", "ee")) and len(w) > 3:
        w = w[:-1]
    return max(1, len(re.findall(r"[aeiouy]+", w)))


def stats(text):
    sents = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    words = re.findall(r"[A-Za-z']+", text)
    n = len(words)
    return {
        "words": n,
        "sentences": len(sents),
        "avg_sentence_len": n / len(sents),
        "avg_word_len": sum(len(w.replace("'", "")) for w in words) / n,
        "long_share": sum(syllables(w) >= 3 for w in words) / n,
    }


def main(paths):
    print("| sample | words | sentences | avg sentence length | avg word length | share of words with 3+ syllables |")
    print("|---|---|---|---|---|---|")
    for p in paths:
        s = stats(open(p, encoding="utf-8").read())
        print(f"| {p.split('/')[-1]} | {s['words']} | {s['sentences']} | {s['avg_sentence_len']:.1f} | {s['avg_word_len']:.2f} | {s['long_share']*100:.0f}% |")


if __name__ == "__main__":
    main(sys.argv[1:])
