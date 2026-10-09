# How come wifi repeaters aren't just amplifiers?

*Tags: repeater · score 3*

## Question

Not sure if in scope for ham SE. I'm very new to this.

Most wifi repeaters contain an actual router and two radios set up to receive and transmit at different frequencies.

Why can't we have a wifi repeater that literally takes the wifi EM band, amplifies it, and spits it back out?

## Accepted answer (score 7, by Kevin Reid AG6YO)

This type of repeater is sometimes called a **linear transponder**, particularly when it is installed on amateur radio satellites (I don't know of other uses). There are several problems with using it in the application you propose.


Such a repeater cannot *improve the signal quality*. Whatever noise it receives, it transmits. Therefore, the signal-to-noise ratio coming out of it will always be worse than going into it. A repeater which demodulates/decodes the signal and re-modulates it can clean up the signal. Even an analog FM repeater as used by all sorts of two-way radios will do this — it inherently takes advantage of the “FM capture effect” to produce less RF noise than it received. Digital transmissions can do this even better because the received bits (more precisely, symbols) are detected and then re-modulated from scratch, so none of the received noise passes through the repeater at all (whereas in the analog FM case the audio will degrade somewhat).

Additionally, decoding and validating a digital packet ensures that *if* it is unusable for any reason (too much noise or other transmissions to decode, or the transmitter was just not obeying the protocol) the repeater will not retransmit it, thus helping efficiently use the available spectrum.


WiFi famously works in the same 2.4 GHz band as microwave ovens. Such a repeater would retransmit the leakage from any nearby microwave oven. (This is just a particular example of the general case of not being able to avoid retransmitting noise.)


Retransmitting on another frequency requires that you have two separate frequencies designated for this purpose. If these are chosen arbitrarily for each network setup, then you could create a feedback loop between separately administered repeaters. If the protocol specifies pairs of frequencies, reserved for "devices" and "repeaters", then multi-hop repeater networks wouldn't work.

Broadly speaking, simply repeating a band is **not an efficient use of spectrum,** particularly when you have many devices and repeaters, uncoordinated, all trying to use the *same* bands.

I mentioned above that this technique is used in some amateur radio satellites. In this case, the input and output frequencies are widely separated, and unlike WiFi there are no other nearby un-coordinated repeaters using the same frequencies, so there is no feedback loop problem.

The advantages (that I can recall) of a linear transponder are:


Many users can use it at the same time — it just repeats a band of the RF spectrum it receives, so many signals can occupy different frequencies within that band. (As long as nobody transmits too strongly.)


It can be used with any mode (modulation), even ones that were invented after the satellite was launched. Most amateur satellite repeaters are basically FM repeaters, and thus support only one voice channel.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14542/how-come-wifi-repeaters-aren-t-just-amplifiers, by i_am_goose, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
