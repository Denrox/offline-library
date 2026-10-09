# Morse code for hash (#)

*Tags: cw, morse-code · score 4*

## Question

Is there a morse code for a hash character? If so, what is that morse code? My thoughts where that there is morse code for an @ but why not for a #?

## Accepted answer (score 9, by Phil Frost - W8II)

There isn't one. Why? Because it's not defined in the standard.

"#" isn't the only symbol in common computer use which is not defined in Morse code. For example, Morse code can't distinguish upper and lower case letters. Nor does it have codes for any of {*^&_. The reason is likely that Morse code is intended to be memorized and decoded by a human, and each additional code makes that harder. How much harder would it be if instead of the 26 basic letters, a little punctuation and a few prosigns, you had to learn 128 codes for the entire basic ASCII character set? Or, 113,021 codes to cover all of Unicode 7?

Let's also not forget that Morse code predates ASCII by about 130 years and its intended application is sending telegrams.

Of course there are modern encodings which are more similar to modern computer technology. For example, PSK31 can encode all 127 characters of basic ASCII. And there are any number of digital modulations which just send arbitrary strings of bytes, so with a suitable encoding like UTF-8, you can encode any character in Unicode, just like a modern web page.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4926/morse-code-for-hash, by Thealon, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
