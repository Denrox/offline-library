# Why were "PARIS" and "CODEX" considered "typical words"?

*Tags: cw · score 5*

## Question

In the context of wondering how to convert characters per minute to words per minute, it was pointed out that CODEX and PARIS are used as typical words for measuring speed of CW operators.

As the wikipedia states:

There are two common typical words: "PARIS" and "CODEX".  
PARIS mimics a word rate that is typical of natural language words and reflects the benefits of Morse code's shorter code durations for common characters such as "e" and "t".  
CODEX offers a word rate that is typical of 5-letter code groups (sequences of random letters). Using the word PARIS as a standard, the number of dot units is 50 and a simple calculation shows that the dot length at 20 words per minute is 60 milliseconds. Using the word CODEX with 60 dot units, the dot length at 20 words per minute is 50 milliseconds.

I'll argue that neither PARIS nor CODEX are themselves typical in morse communication. The assumed typical length of five letters seems, at least for English, unfounded, too:  
Even if we assume that a keyer would omit articles like "the" and "a" regularly, prepositions ("on", "at", "by", "for"…) should be rather common and are much shorter. Longer words tend to get abbreviated.

So, since the wikipedia doesn't actually cite its sources:

- Who (and: when) decided CODEX and PARIS would be appropriate for words-per-minute estimates?

and

- Are there statistics to back this up?

## Accepted answer (score 7, by hotpaw2)

Answering the 2nd part:

There seem to be many research articles and business documents reporting statistics on average word lengths, in characters, which seem to vary with language, dialect, corpus, and even over time. The lengths reported seems to cover a range between 4 and 6 letters, which makes rounding to integer 5 (at some point in history) a reasonable compromise (for large English and German corpuses).

There also exist many tables of statistics of relative letter frequencies in various Western languages (see various cryptography books), which could be converted into an average dot length for a given length word. A quick Monte Carlo simulation I ran seems to show that 5 letters randomly chosen using the statistical distribution from a Wikipedia table of relative letter frequencies in English, will average somewhere around 50 to 51 dot times in duration, using International Morse Code.

The word "PARIS" seems to fit within these statistical ranges for word lengths and letter frequencies.

A random selection of search results:

- https://arxiv.org/pdf/1208.6109.pdf
- https://diuna.biz/length-of-words-average-number-of-characters-in-a-word/
- http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/

Specialized abbreviations seem to be a performance optimization or data compression process, not included in the pre-encoded corpus. Also, short words might **seem** more common; but that might be due to an "availability bias" error in human cognition.

As a random additional factoid, according to Wikipedia: International Morse Code was standardized at the International Telegraphy Congress in 1865 in **Paris** and was later made the standard by the International Telecommunication Union (ITU). There exists a newer ITU document on International Morse Code encoding, however it doesn't mention speed of encoding in words.

Although this question is being asked in a radio related forum, note that 1865 was well before Hertz and Marconi demonstrated the existence and usefulness of radio waves. So the International Morse Code specification was targeted towards land-line telegram messages (clicking sounders and tape printers), not CW operation (as electromagnetic waves, unknown at the time, or even as audio tones).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12413/why-were-paris-and-codex-considered-typical-words, by Marcus Müller, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
