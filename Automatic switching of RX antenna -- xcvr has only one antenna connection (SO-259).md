# Automatic switching of RX antenna -- xcvr has only one antenna connection (SO-259)

*Tags: antenna, transceiver, loop-antenna · score 3*

## Question

I have a local noise problem that's pretty intractable, especially on low bands. I'd like to at least experiment with a loop-on-ground RX antenna -- I've got a 1/4 acre to play with. My IC-718 has only the one antenna connection, but it also has a ground-on-xmit socket on the back (18 VDC max) which I'm sure is meant for remote switching, but normally a linear....

What's modern best practice for automatic switching between RX and TX antennas? Usual T/R switches are designed for a separate xmitter and rcvr, and one antenna, and I'm looking at the opposite. (My prior experience with electronic T/R switches involve tubes, because I am a fossil.)

Store-bought is ok, though I am competent with non-SMD construction, and don't mind following a schematic.

## Accepted answer (score 3, by tomnexus)

To expand on my comment about timing / delays:

If you're only using SSB, or digital modes from a computer, the radio won't produce much RF power immediately on PTT, so all OK. If you're using CW or FM then it might produce full power immediately, while your relay is still switching.

The IC-718 manual just specifies the SEND relay output, and on p15 shows how it can be used to control a non-Icom linear amplifier. Presumably there's a small delay between the SEND output being activated, and full power appearing from the radio - for example the radio also needs to switch some relays.

You should probably check this before transmitting full power into your relay / RF switch, in case your relay is slower than the transceiver.

Other radios offer a variable delay, useful for more complex setups, transverters, EME, etc. Some enterprising hams measured this, eg DH1TW and helpfully found that there's a delay in the RF power of 7.7 ms (IC-7300) and 9.1 ms (IC-9700), even with the adjustable delay set to zero. Random small relays seem to have a 10 ms max switching time, so that's probably OK.

It wouldn't be difficult to replicate his setup - if you don't have a 60 dB 100 W attenuator, just use a scrap of wire as an antenna on one channel of the scope.  
If you don't have a scope, you could probably get the same result with an audio recording program like Audacity, and any (analog) receiver, to listen for the relay click and the transmitted tone.

Unfortunately KG3V found that the IC-7300 has a different problem, it releases the SEND output before it's finished transmitting. Maybe less of a problem in your case.

Finally, KV5R has a detailed page doing exactly what you're doing with two antennas. There he uses an opto-isolator for the SEND input to the box.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22417/automatic-switching-of-rx-antenna-xcvr-has-only-one-antenna-connection-so-259, by W1WFG, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
