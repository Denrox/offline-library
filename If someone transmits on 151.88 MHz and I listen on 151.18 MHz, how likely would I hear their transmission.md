# If someone transmits on 151.88 MHz and I listen on 151.18 MHz, how likely would I hear their transmission?

*Tags: receiver, baofeng, uv-5r · score 10*

## Question

I have a cheap baofeng uv-5r, and I sometimes hear an intermittent transmission which pulses past the squelch threshold with periods of dead space between, roughly 0.75 seconds or less.

My job uses a repeater and radioreference.com lists the used frequency as 151.18 MHz.

I have trouble hearing them on the baofeng, but not my alinco dj500t, a question I'm sure for a separate post as to why.

Anyways I hear this pulse on both the work frequency and MURS channel 1 (151.88 MHz). Can anyone shed light on this?

In summation of the question, is it possible someone transmitting on a nearby frequency is being picked up?

To add to the final question, it seems to me that listening on 151.00 MHz could potentially monitor the whole 151. MHz area, based on the way my alinco functions, of this I'm very unsure, and don't want to seem unintelligent, but I am very new, is that possible?

## Accepted answer (score 2, by hotpaw2)

It's possible for a strong enough interfering RF signal to overload the front end amplifier(s) of a receiver. Once overloaded into a non-linear range, all bets are off as to the resulting bandwidth of the interfering signal, which could then splatter into many nearby channels.

If the stop-band attenuation of any of a receiver filters is poor, it's possible for a strong enough signal in a stop-band to blast right through the stop-band, above the squelch or demodulation threshold, and then possibly alias down to a different or image frequency during any heterodyning, digital sampling or processing.

It's also possible for a strong enough interfering RF signal to couple into a receiver's wiring past any RF or IF filtering stages (even directly into the audio amplifier or the DC power supplies), thus potentially turning the receiver into a wide band demodulator of some sort.

## Answer (score 4, by ESP32)

In theory, this is a question of the bandwidth - or better said of 2 bandwidths. In practice it's much more complex. But let's have a look at bandwidth theory first:

1. the bandwidth of your transceiver
2.

the bandwidth of the signal interfering you.

 - Let's assume you have your receiver on 151,180,000 Hz.
 - Let's further assume your receiver has a bandwidth on FM of 15 kHz.

This means that you will receive signals between 151,180,000 +/- 7.5 kHz which means that whenever a signal is transmitted between 151,172,500 and 151,187,500 you will receive it.

The other part is the transmitting signal:

You also have a bandwidth there. So let's assume you have a signal on 151,880,000 with a bandwidth of 1 MHz (maybe for transmitting digital data). Thus it will interfere between 151,380,000 and 152,380,000 (+/- 500 kHz).

The question is - will you be interfered by this signal on your frequency 151,180?

The answer is: it depends. In theory no, because the interfering bandwidth does not touch your receiver frequency (see above). In practice your receiver is not ideal - and speaking about Baofeng, it's as far from ideal as it can be - by still working more or less.

There are many reasons why even good and expensive receivers have troubles with signals on other frequencies. In a nutshell **it's just a question of the signal strength of the other signal and of the filter quality of the receiver**. Also the frequencies of both signals matter, because they might be mixed up into new frequencies in the reception path of the transceiver. I assume that the signal on 151,88 is very strong.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12406/if-someone-transmits-on-151-88-mhz-and-i-listen-on-151-18-mhz-how-likely-would, by Wolfgang Steele, hotpaw2, ESP32. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
