# How does the baofeng radio eliminate squelch tail?

*Tags: baofeng, squelch · score 10*

## Question

All tests are performed in Carrier Squelch mode on all radios without any sub-audible tone or digital squelch involved.

Scenario 1: The Baofeng handheld radio Keys up. Another Baofeng is listening. When the transmitting Baofeng un-keys, the receiving baofeng does not hear any squelch tail, and has a smooth un-key.

Scenario 2: The Baofeng handheld radio Keys up. A different brand radio is used to receive. When the Baofeng un-keys, the squelch tail is heard through the speaker of the other radio. I have tested this on Kenwood, Alinco, and ICOM.

Scenario 3: A different brand radio keys up. The Baofeng is listening. When the radio un-keys, I hear the squelch tail through the Baofeng speaker.

What is it that Baofeng uses to eliminate squelch tails on the radios where no other brand inhibits this property?

I have confirmed it is NOT chicken burst (ending the PL tone early) , or reverse burst (phasing the PL tone 180 degrees) , and there is something special about the Baofeng radio's "End-Of-Transmission" squelch tail eliminator.

## Answer (score 11, by glibdud)

According to the detailed menu descriptions on the Miklor site:

35 - STE

Transceiver - Squelch Tail Elimination

This function is used eliminate squelch tail noise between UV-5Rs that are communicating directly (no repeater). Reception of a 55 Hz or 134.4 Hz tone burst mutes the audio long enough to prevent hearing any squelch tail noise.

Note: When enabled and T-DCS is set to OFF the radio sends a 55 Hz tone for about 1/4 second when the PTT key is released.

Note: When enabled and T-DCS is not set to OFF the radio sends a 134.4 Hz tone for about 1/4 second when the PTT key is released.

Note: Set to OFF before communicating through a repeater.

Note: Recommended setting is OFF

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3771/how-does-the-baofeng-radio-eliminate-squelch-tail, by Skyler 440, glibdud. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
