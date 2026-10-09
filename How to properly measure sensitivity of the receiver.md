# How to properly measure sensitivity of the receiver?

*Tags: measurement · score 5*

## Question

I have Kenwood TH-D72 2m/70cm HT. According to the manufacturer the sensitivity is "Less than 0.18 uV". I would like to check this, since the radio is not new and I'm not it's first owner.

To do this I decided to use the tracking generator of my Rigol DSA815-TG and a bunch of SMA attenuators (120 dB in total), because I don't have any other way to reliably generate a few uV signal. Naturally, zero span was used. I discovered that a -127 dBm signal opens the squelch on both 2m and 70cm and with squelch turned off I can hear the presence of -133..-134 dBm signal.

What surprises me is that if my calculations are correct -127 dBm is **much less** than 0.18 uV RMS:

```
>>> from math import pow, log10
>>> 10*log10(1000*pow((0.18/1000/1000),2)/50)
-121.88424994129406
>>> 10*log10(1000*pow((0.05/1000/1000),2)/50)
-133.0102999566398

```

I decided to check my HF QRP transceiver Xiegu X5105 as well and got similar results - the sensitivity is about 0.05 uV although the manufacturer promises only 0.25 uV.

Are my measurements wrong? Or maybe it's a common practice among radio manufacturers to specify worst-case sensitivity? According to the spectrum analyzer attenuators are fine. Also a -73 dBm signal gives S9 level on a S-meter as expected.

## Accepted answer (score 5, by tomnexus)

Quite likely the signal generator, and the radio, are too leaky to do this experiment on one bench top. So the signal received by the radio is not as small as you think it is.

The solution would be to eliminate the leak path, by shielding one or both ends. You'll get good results with aluminium foil: Power the HT from its battery only. Connect some of the attenuators directly to the HT. Wrap the whole thing tightly in foil, a few layers. Where the attenuators stick out, put a tight cable tie or wrap of wire twisted so the foil makes good contact with the attenuator body. Repeat the cable tie in two more places. Poke some small holes if you need to hear or see the LED.

You could also try more distance, with a cable between Tx and Rx, but  
a) watch out for leakage through the cable - it must be double-screened like RG214, RG223, etc, otherwise the signal will just leak in there instead, and  
b) watch out for currents on the outside, carrying RF from the leaky generator to be picked up by the leaky receiver. Some ferries distributed over its length will help.

Even if you can't fix all the leakage, trying one of these tests will show you if there is a leakage problem or not.

It's also possible that the squelch opens at a lower power than is required for intelligible speech. A professional radio test box uses a frequency modulated RF signal, and evaluates the signal-to-noise ratio of the audio output. This wouldn't be a whole 10 dB different from what you're measuring though.

## Answer (score 3, by hotpaw2)

To reduce direct coupling between chassis (generator and DUT), I use a long antenna coax (10 to 20 meters or more), and put the RF source plus attenuators on the far side of the building, with the attenuator chain some distance from the RF source on another coax. You may or may not need to take into account the loss on the coax (which might be less than the tolerances on your attenuators).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15963/how-to-properly-measure-sensitivity-of-the-receiver, by Aleksander Alekseev - R2AUK, tomnexus, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
