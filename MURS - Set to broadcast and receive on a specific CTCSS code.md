# MURS - Set to broadcast and receive on a specific CTCSS code

*Tags: baofeng, tone-squelch · score 3*

## Question

Context

- Using a Baofeng UV5RA
- Would like to transmit on MURS (e.g., 151.880 MHz) using a CTCSS code for more private discussions
- All of the online guides talk about *scanning* for CTCSS

Question

- Rather than scanning, is it possible to just *explicitly set* both the transmitting radio, as well as the receiving radio, to use one of the 38 tones?
- If so, how do you choose and set one of these?

Thanks so much for any guidance

## Answer (score 5, by AndrejaKo)

Here on StackExchange we call what you asked an XY problem.

You're asking how to set up CTCSS, but what you really want is to have privacy. Those are two different things.

First of all, a tiny bit of theory about CTCSS. The name means Continuous Tone-Coded Squelch System. It's not a privacy system, it's a squelch system! It works by sending a tone-code continuously while you're transmitting.  
So here comes the failure of the privacy idea: When it's sending the tone, what the radio is doing is basically **kindly asking** other radios that do not have that code set on their receive not to open their squelch. If your receiver has no CTCSS code set, you'll hear everything since the squelch will just open.

So for more private conversations, you'll need a radio with a scrambler. This won't make your conversations secret, but it will make it a tiny bit harder for other people to listen in.

Finally, for your CTCSS question. I don't have a Baofeng right now, so I can't test, but from what I can see, you should go to menu 13, which should be called CTCSS, and set up the code there. There's an explanation for example here in comments.

The other option would be to get a programming cable and use CHIRP to set up channels and CTCCSS codes.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6594/murs-set-to-broadcast-and-receive-on-a-specific-ctcss-code, by David, AndrejaKo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
