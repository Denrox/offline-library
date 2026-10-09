# Is there a technical reason to sell an LNA without advertising its gain?

*Tags: rf-power, lna, path-loss, gain, link-budget · score 4*

## Question

I recently bought a couple SPF5189 low-noise amplifier boards via an online marketplace. One thing that struck me is that while nearly all the listings highlighted the LNA as having a noise figure of 0.6 dB, very few listings actually specified its gain (which datasheet I found says is 18.7 dB typical) at all.

Maybe I shouldn't read too much into it [half of these listings were from sellers with screennames like "toecare best ecogreen 2015"] but is there a technical reason that the noise figure specification would be more important than the gain figure?

Clearly the "low noise" aspect is important but isn't the "amplification" the first thing I should know when inserting a block into a signal chain?

## Accepted answer (score 6, by Digiproc)

The gain becomes an issue only if its ridiculously low. The main purpose of an LNA is to lift the signal well above any noise of the following stages, and often that can be done with a gain of several dB. However, the fact that they didn't advertise it, makes it suspect.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12980/is-there-a-technical-reason-to-sell-an-lna-without-advertising-its-gain, by natevw - AF7TB, Digiproc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
