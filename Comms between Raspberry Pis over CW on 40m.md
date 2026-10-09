# Comms between Raspberry Pis over CW on 40m

*Tags: cw · score 3*

## Question

I'm completely new to amateur radio, so please forgive me if this is a silly question.

I'm looking at these devices: Assembled HAM RADIO 40M CW HF QRP Pixie Transmitter Receiver 7.023-7.026MHz DIY on eBay

What I would like to know is how feasible is it to use these CW transceivers to create a (low baud) data connection over, say fifty miles, between two Raspberry Pis?

I appreciate that these transceivers are the absolute cheapest that I could find, but this is the point: I would like this project to be dirt cheap.

If you know of any links or guides that you could point me at, I would be most appreciative - if you can think of a better, cheaper, way to do this then I'd love to hear about it!

Thanks.

## Answer (score 2, by Ted)

A Raspberry PI (preferrably a model 2) could run "fldigi", a free open source digital mode software. You might have to rig up some form of CW keying also

Fldigi can run a multitude of digital modes including CW, PSK and Olivia. It can also be programmed to transfer email, formatted and pre-canned messages both in keyboard to keyboard and automatic mode. Each transceiver would require a bidirectional audio interface, such as a low cost USB sound dongle. Pi's only come equipped with audio out.

These non-CW modes rquire a SSB transceiver though.

The low cost "Pixie" transceivers only do CW, but could be "keyed" with an cheap transistor using the circuit included in the fldigi documentation.

Most SSB transceivers are somewhat more expensive, but by using the more advanced digital modes instead of CW, you could greatly improve accuracy and speed in difficult propagation conditions.

You might also look at the low cost (~$30) Baofeng (or similar) 2m/70cm HT's that could probably transmit in MT-63 mode with only a microphone and speaker on the Pi held close the the HT. Some FM repeaters might have sufficient bandwidth to give you 50 mile coverage. Otherwise a yagi directional antenna and tower could provide a strong enough signal without a repeater.

73

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5788/comms-between-raspberry-pis-over-cw-on-40m, by roger, Ted. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
