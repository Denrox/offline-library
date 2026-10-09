# What happens in a low loss feed-line with a high SWR

*Tags: feed-line, transmission-line, impedance · score 8*

## Question

I was recently reading an interesting article from the ARRL to get a better understanding of the SWR.

The following case is still unclear: A low loss feed-line with an impedance that doesn't match the antenna's impedance and the receiver's impedance.

In this case a large part of the signal should "bounces" back and forth into the feed-line due to the impedance mismatch. At this point the article states that:

The energy bounces back and forth inside the cable until it’s all radiated by the antenna for a lossless transmission line. An important point to realize is that with extremely low loss transmission line, no matter what the SWR, most of the power can get delivered to the antenna.

I understand that during each "bounce", due to the impedance mismatch, some amount of energy will be transmitted and the rest reflected.

I don't understand how this transmitted power could be useful. After "bouncing" back and forth the part of the signal that will be transmitted will probably be out of phase with the signal sent by the transmitter. Even if by any luck the reflected signal and the signal currently sent by the transmitter happened to be in phase, the information conveyed wouldn't be the same.

So to me, even if almost of the power is transmitted, due to the high SWR most of this power should be just noise and don't improve the quality of the transmission in any case. But it's not what the article seems to explain. What did I miss ?

## Accepted answer (score 8, by Phil Frost - W8II)

For many modulations, the modulation is very slow compared to the propagation delay of the feedline. For example, SSB is typically limited to no more than 4 kHz. That corresponds to a wavelength of of 75 km. As long as the feedline is significantly shorter than this, then the delay due to the feedline is negligible.

It may be easier to understand intuitively in a digital case. For example, PSK31 sends 31.25 symbols per second. 31.25 Hz corresponds to 9600 km, meaning by the time you are sending a bit, the previous bit is 9600 km away.

This breaks down for very high-speed modulations. For example, 8VSB modulation used by HDTV broadcasts transmits 10.76 million symbols per second, equivalent to a 29 meter wavelength. At these speeds, a feedline is long enough to introduce significant delay, which could come out looking like multipath distortion. Then again, TV channels are 6 MHz wide. Most amateur transmissions are several orders of magnitude narrower. Protip: don't operate your commercial TV broadcast station with a poorly matched feedline.

But for most amateur transmissions, we can consider the transmission as a pure sine wave, which is a reasonable approximation given the timescales dictated by the length of the feedline and the modulation. Then, it helps to visualize what a standing wave in the feedline looks like. From Wikipedia:

If we regard the transmitter to be on the left and the antenna to be on the right, then the blue wave represents the transmitted wave, and the red wave the reflected wave.

Now here's the thing to realize: this particular image depicts a *complete* standing wave on a *lossless* transmission line. In this case, we are delivering 0 power to the antenna, the VSWR is infinite, and the transmitter's finals are probably about to explode. This doesn't happen in practice because our antennas always accept at least *some* of the power.

In practice, only *some* of the power is reflected back, and the result is a *partial standing wave*. Dan A Russel has a page of great animations, like this one:

In the case of a *partial* standing wave, we can see that the envelope (outlined by the dotted lines) does not reach 0 amplitude at the nodes. In this case, some power is transferred. This is also a good visualization of VSWR: it is the ratio of the voltage amplitude at the antinodes (envelope maximums) to the voltage amplitude at the nodes (envelope minimums).

Notice also that the reflected wave might arrive back at the transmitter in any phase, depending on the length of the feedline and the antenna's reflection coefficient. It may or may not be in phase, but it will be a *constant* phase, not just noise. By adding an antenna tuner we can reflect the reflected wave back at the antenna, and adjust the phase of this re-reflected wave to be whatever we want, within the limits of the tuner's capabilities of course.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2297/what-happens-in-a-low-loss-feed-line-with-a-high-swr, by ITChap, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
