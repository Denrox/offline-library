# Does scanning take much more battery than listening on one channel?

*Tags: battery · score 9*

## Question

I have a couple of HTs with channel scanning features. I imagine setting the radio to scan mode takes more power than just listening to a single channel, but what rough order of magnitude? Will I lose 1%, 10% or 50% of my battery life? Are some brands or models notably better than others for power efficiency while scanning?

## Accepted answer (score 6, by tomnexus)

There are a few states of listening that you should think about:


listening with the squelch closed, the receiver is probably off for 95% of the time, turned on a couple of times a second to check for a signal. This is the lowest power state.


receiving a signal, squelch open, the receiver is fully on.  
Also the loudspeaker takes some power, not much if it's soft, but more than the receiver if the volume is loud.


scanning at full speed, the receiver is on all the time. Re-tuning won't increase its power consumption significantly (there is some time wasted while the tuner settles, but this is just part of scanning).

So I estimate that scanning, with the squelch closed, takes the same or less power than listening to a busy channel at low volume, but many times more than monitoring an empty channel.

Why not do an experiment? Disconnect the battery, power the HT from an external source, and monitor the current that it draws. You might have to do some work to smooth out the pulses of current in monitoring mode, something like this:

## Answer (score 2, by hotpaw2)

I would not be surprised if the audio amp used more power than the rf front, tuner osc, and signal detect combined. Thus listening at some reasonable speaker volume, and using energy to vibrate a physical mass, might consume more power than just retuning and monitoring some level.

But measuring your particular radio is much better than guessing.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14577/does-scanning-take-much-more-battery-than-listening-on-one-channel, by K0SWE, tomnexus, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
