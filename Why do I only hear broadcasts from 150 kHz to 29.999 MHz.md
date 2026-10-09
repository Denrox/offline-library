# Why do I only hear broadcasts from 150 kHz to 29.999 MHz?

*Tags: hf, receiver, equipment-troubleshooting · score 8*

## Question

I am currently studying for my amateur radio license. Until I'm licensed, I'm trying to use a Sony ICF-SW7600GR receiver to listen in on amateur radio "phone" transmissions. No matter what I do, however, I can't seem to locate any amateur radio conversations. Everything I manage to tune into is a broadcast, usually some news, music, or religious broadcasts. Since this receiver covers all MF and HF amateur bands, I really expected to pick up something. I've dialed directly into frequencies set aside for "phone" in Region 1 (I'm in Prague, Czech Republic), searched LSB under 10 MHz, USB above 10 MHz, normal AM, utilized the external SW antenna, dialed in directly to local stations, tried with and without synchronous detection, etc.

Maybe everyone is using FM or PM while my receiver only picks up AM?

## Accepted answer (score 12, by Kevin Reid AG6YO)

It doesn't sound like you're doing anything wrong. Most likely, you are simply only hearing strong stations; broadcasters put much more power into their transmissions than amateurs are legally allowed to, so you can hear them over a much wider range.

Advice on the practice of listening:


For finding signals, first of all, **always use SSB**. Even if it's the wrong mode to demodulate the signal correctly, you will hear *something* (often including a strong carrier tone), because SSB is just turning a slice of the RF spectrum into audio regardless of what it contains. The only way you can miss hearing a signal using SSB is if the signal is much wider bandwidth than 3 kHz (so that it sounds like just an increase in the noise floor). Once you have found something, you can try other modes to receive it correctly.


Try tuning to the CW band segments (using a CW mode if you have it, otherwise SSB), rather than phone. Even if you don't know Morse code, CW signals are much easier to pick out of the noise by ear, so you can tell whether you're receiving anything.


Make sure you're listening at the right time. Broadly speaking, propagation is better at night, so not only will you receive better, but more people will be transmitting. You should be able to hear the broadcasters more clearly as well. When you're studying for your license, read about the ionosphere and other kinds of propagation effects, and figure out when you should be listening to what band.

Advice on improving your reception:


You may have local noise sources which interfere with reception. They won't necessarily sound like anything other than the usual hiss of noise. Shut off all the electrical devices in your home temporarily and see whether they make a difference. (Instead of listening for signals you can't hear yet, listen for how clear the broadcasters are.) Or, especially if you're in an apartment building with many close neighbors, you could try going out to a park or other location with very little electronics.


Make sure you have a decent antenna. Since you are receiving, not transmitting, this is not critical, but it helps. According to some reviews, your model of radio comes with a reel of wire in addition to the telescoping antenna; use it. There are two basic approaches:


“Long wire”: Make your antenna wire as long as you can reasonably fit in the space you have. (Keep it away from large metal objects.)


Make it resonant on the band of interest. In particular, make it about 1/4 wavelength long, or possibly an odd multiple (3/4, 5/4, and so on). (Coiling up the free end will make it effectively shorter without needing to cut the wire.)

Maybe everyone is using FM or PM while my receiver only picks up AM?

Nobody uses FM on HF, because it is a waste of bandwidth. But if they did, then you could still hear it. Specifically:

- An AM receiver tuned exactly on a FM signal will produce silence (*not* noise).
- An AM receiver tuned slightly off the FM signal will produce decent audio, with excess noise.
- A SSB receiver tuned to an FM signal will produce a distorted sound which will still be recognizable as being voice-like (due to the timing of speech sounds), and possibly a tone from the carrier.

## Answer (score 2, by KC3FWL)

If your antenna is hanging down the side of the building that may be your very problem! Most DXing on HF is done on horizontal antennas. If yours is vertical then you be getting only a sliver sized cross section of the horizontal signals.

The station you did pick up may be driving a vertical antenna. The cheapest way to test this is to put up a horizontal dipole and see if it increases or decreases the reception of the known signal from the vertical antenna. (Always power down your rig before changing the antenna.) Don't forget to tune your antenna. If you have an antenna tuner or just a SWR meter then you're good to go. If not then be as exact as you can in measuring your wires.

You can tape it to the walls of your apartment near the ceiling for a temporary setup.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5457/why-do-i-only-hear-broadcasts-from-150-khz-to-29-999-mhz, by rcampbell, Kevin Reid AG6YO, KC3FWL. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
