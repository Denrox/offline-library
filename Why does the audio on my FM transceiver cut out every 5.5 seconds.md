# Why does the audio on my FM transceiver cut out every 5.5 seconds?

*Tags: fm, icom, equipment-operation, d-star, weather · score 15*

## Question

Specifically, my Icom ID-4100a.

What's interesting, is that this happens in MR and VFO modes... but NOT when using the built-in WX stations. For example listening to WX-01 (162.550 MHz), no problem. Listening to 162.550 via VFO and I get the problem.

I first noticed it during a local repeater QSO and thought it was the other station experiencing an intermittent fault... and then noticed it with another station later that day, so it had to be me. Opening up the squelch let me catch it in the act, and it seemed so regular that I thought to time it: every 5.5 seconds on the nose.

If you have any thoughts or suggestions for further diagnosis and remediation, I'd love to hear it! My instinct is to first try a Partial Reset followed by an All Reset before cracking open the case on the workbench.

## Accepted answer (score 33, by webmarc)

It's a feature not a bug.

When turned on, the **weather alert** function checks the local NOAA station for its alert tone every 5 seconds for half a second... doing so takes over the receiver.

I'd turned it on, and forgotten I'd done so; and how that feature is implemented never registered in my mind. Turning it off solves my "problem."

Thanks to reddit user /u/hobbified for the answer!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17205/why-does-the-audio-on-my-fm-transceiver-cut-out-every-5-5-seconds, by webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
