# What is generally considered "too much" power for JT-65 on HF?

*Tags: hf, digital-modes, jt65 · score 12*

## Question

Recently, I have begun experimenting with JT-65A, mostly on 20 meters. I usually run about 5 watts with that mode, since I know that JT-65 is a weak-signal mode. Is that still too much power? What is generally considered excessive power on JT-65?

## Accepted answer (score 7, by Dan KD2EE)

5 watts is probably what most JT-65 purists will tell you to use, but in practice, I tend to aim for 20 watts. That gives you a good 6dB boost (every doubling of power is equal to +3dB) which is actually meaningful in JT-65. Any more than that, and you'll start finding certain problems. Note that the same is true for the WSPR family of protocols.

First, that since everyone else is using less power than you are, you'll have many cases of people hearing you, but you can't hear them.

That in turn means that you run the risk of interfering with a conversation that you can't even see, especially if you're running 100W and they're each at 5 or 20.

Finally, many transceivers will cause distortions in the JT-65 waveform when run at above a quarter to a half of their maximum power. Transceivers are meant to work with analog data, not the sharp frequency transitions of the digital signal. Overdriving them can cause clipping, which will cause you to actually waste power and may even make your transmission unreadable.

So to answer the question, the standard maximum is either 20 or 30 watts - and there's really no point in exceeding that. Many people win awards on the mode at 5 watts! Most transceivers will distort your waveform above a certain limit, and there's no point in risking it for another 2 or 3 dB.

## Answer (score 5, by James NF8I)

As you stated, JT-65 is a *weak signal* mode. This should not be confused with a *low power* mode. Depending on your antenna and location, the amount of power you need to conduct a successful contact may vary, just as in any other mode.

A good guideline would be to start at the lowest power setting you can, and if you're not able to work the stations you want (and can hear!), gradually increase power. If possible, use some of the online spotting networks (jt65.w6cqz.org or hamspots.net) to see what signal reports you are getting. If you are being received anywhere between -10 dB and -20 dB, you've nailed it! If you are consistently getting numbers between -10 dB and 0 dB, you can reduce power. If you aren't being heard or you get numbers below -20 dB, try increasing power.

I've worked stations using milliwatts who were booming in for me, and I've worked at least one station who claimed to be running 1 kilowatt. The kilowatt guy got a -10 dB report from me, so I guess he wasn't using too much power!

Good luck and 73!

## Answer (score 2, by Frank Johnson)

Re: "Finally, many transceivers will cause distortions in the JT-65 waveform when run at above a quarter to a half of their maximum power. Transceivers are meant to work with analog data, not the sharp frequency transitions of the digital signal."

K1JT has purposefully tailored the audio output of his software so it has none of the effects mentioned above. The "data" signal is an analogue signal with no such "sharp transitions". As only one tone is present at any time, there can be no intermodulation. In addition, since there is no AM component to the JT65 signal, the linearity of subsequent RF amplifiers is not critical. It is not necessary to de-rate output powers for the sake of linearity as is needed in PSK modes.

Re:"As you stated, JT-65 is a weak signal mode. This should not be confused with a low power mode."

Absolutely agreed!

There are no "low power" modes. Even WSPR will allow me to enter a power of 1kW. Not that I would ever do that but in this "low power mode", its not the low power that is important. It is the fact that the power level is known and can be taken into account when assessing results.

Frank, g0gsr

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/428/what-is-generally-considered-too-much-power-for-jt-65-on-hf, by krzysz00 KF5SOQ, Dan KD2EE, James NF8I, Frank Johnson. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
