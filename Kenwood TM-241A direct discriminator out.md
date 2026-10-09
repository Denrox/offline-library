# Kenwood TM-241A direct discriminator out

*Tags: diy, equipment-design, kenwood, audio-interface · score 3*

## Question

I am going to do a simple SIMPLEX all-star node, using the URIx USB radio interface, which I just got. I have a Kenwood TM-241A transceiver.

I was told the speaker out jack is not sufficient:

The goal is access to output not influenced by the radio squelch or volume controls.

I was also told that there are high-pass filters in many radios which will eliminate most CTCSS, so I can't use the CTCSS_DET pin.

Does the Kenwood tm-241a have a place in it I can find with discriminator out, which I could solder some audio wires to?

## Answer (score 2, by HarveyB)

Typically a good place to get discriminator audio is the "high" end of the squelch control. Unfortunately the TM-241A does not have a conventional squelch control, making it necessary to tap onto the board itself. Pin 9 of IC1, an MC3372, is the output of the discriminator. If you can locate and solder to this pin it should give you the desired signal. If at all possible you should check the signal with a scope before soldering to it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1687/kenwood-tm-241a-direct-discriminator-out, by Skyler 440, HarveyB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
