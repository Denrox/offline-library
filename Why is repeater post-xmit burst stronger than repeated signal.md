# Why is repeater post-xmit "burst" stronger than repeated signal?

*Tags: repeater · score 3*

## Question

I have no problem triggering GB3LW, and after I release PTT I get the strong burst from the repeater confirming that it "heard me".

But if I use two radios, the receive-only one will *only* hear that burst, with default settings, not me talking. If I hold down "monitor" on it, or set the SQL down to lowest setting, then I hear myself loud and clear.

I have also made contact over this repeater, so it should not be a matter of me having misconfigured both radios.

The baofeng UV-5RE lights up green if receiving, and activates the speaker if the tone is present. My talking doesn't light it up on the other radio (because SQL / signal strength), but the post-talking burst does.

It should therefore not be "trigger audio frequency not received, so not activating speaker".

So my question is: Why is "my talking" not being repeated as strongly enough to activate radio, but the post-talking burst is?

## Accepted answer (score 5, by Glenn W9IQ)

You are probably experiencing what is called "desense". The strong signal of your transmitting radio is getting into the receiver on the receiving radio and blocking its ability to receive the repeater even though they are on different frequencies. As soon as you stop transmitting, the desense is gone so your receive radio can now hear the squelch tail of the repeater.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7582/why-is-repeater-post-xmit-burst-stronger-than-repeated-signal, by Thomas, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
