# Why there is no AFSK in FLDIGI

*Tags: digital-modes, modes, fldigi · score 4*

## Question

I was expecting to see an AFSK option in the Fldigi "Op Mode" menu (as there is one option for CW, i.e.), why isn't it there?

Basically, I want to get the data send according to this.

## Accepted answer (score 7, by Phil Frost - W8II)

Fldigi is largely intended for HF operation. From the beginner's guide:

Fldigi is a computer program intended for Amateur Radio Digital Modes operation using a PC (Personal Computer). Fldigi operates (as does most similar software) in conjunction with a conventional HF SSB radio transceiver, and uses the PC sound card as the main means of input from the radio, and output to the radio.

AFSK, as used by APRS and packet radio, is not very popular on HF. A few people do it for sure, but having tried it personally I can tell you it's not a very robust mode with all the noise and fading in a typical HF channel. Since the mode is typically deployed with no FEC at all, it's usual for any HF packet frequencies to be clogged with nothing but retransmit attempts.

Fldigi is also focused on "chat" modes, like PSK31. Again from the beginner's guide:

In this context, we are talking about modes used on the HF (high frequency) bands, specifically chat modes, those used to have a regular conversation in a similar way to voice or Morse, where one operator talks for a minute or two, then another does the same. These chat modes allow multiple operators to take part in a net.

So I suspect the reason you do not find AFSK in Fldigi is that it's neither popular (or really effective) on HF, and it's not a chat mode.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5448/why-there-is-no-afsk-in-fldigi, by KcFnMi, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
