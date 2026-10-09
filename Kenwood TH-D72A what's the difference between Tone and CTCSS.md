# Kenwood TH-D72A: what's the difference between Tone and CTCSS?

*Tags: vhf, kenwood, tone-squelch · score 6*

## Question

Kenwood TH-D72A supports 3 types of tone: Tone, CTCSS and DCS.

What is the difference between Tone and CTCSS?

As far as I know CTCSS is basically a continuous transmission of a given low frequency signal mixed with the voice. So it's basically a simple tone, isn't it?

## Accepted answer (score 8, by hobbs - KC2G)

"Tone", displayed as "T" on the main screen, selects tone encoder + carrier squelch (your HT will send a tone, selected by the TONE Freq menu, and receive any strong-enough signal, regardless of whether it has a tone.) The transmitted tone is necessary to "open up" most repeaters so that you can talk on them.

"CTCSS", displayed as "CT" on the main screen, selects tone encoder + tone squelch (your HT will send a tone, and only open the squelch on receive if the incoming signal contains the same tone).

The CTCSS option has some advantages, in that it will ignore interference, or a far-away repeater on the same frequency that uses the same tone, and on some repeaters will also silence the repeater ident. Especially helpful if you use scanning mode and you only want the scan to stop on actual conversations.

However, there are also reasons to use the Tone option. Not every repeater has tone on its output. For the ones that don't, you can't use tone squelch, so Tone is the only valid option. Also, tone squelch might cut off a very weak signal that comes in too staticky for the tone to be heard clearly. In this case, switching to Tone might provide slightly better reception.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14829/kenwood-th-d72a-what-s-the-difference-between-tone-and-ctcss, by Aleksander Alekseev - R2AUK, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
