# Significance of 1/4 wavelength with respect to antennas

*Tags: antenna, antenna-construction, electronics · score 4*

## Question

I am a new to the radio design field.

My question is, 'What is so significant about 1/4 wavelength with respect to antennas.'

From the information I have gathered from various sources, it is my impression that a 1/4 wavelength antenna is the most used on account of its performance.

I am looking forward to an answer, elucidating the significance in simple terms that I could understand.

Referred Link

## Answer (score 6, by Phil Frost - W8II)

The first part of why a quarter wavelength is special is actually understanding that it's not a quarter wavelength, but a half wavelength.

Consider a quarter-wavelength monopole. If a wavefront originates at the feedpoint, a quarter-cycle later it will have reached the end of the monopole. Here "something interesting" happens, because the antenna ends. That "interesting event" must then propagate back down the antenna to the feedpoint before it can affect the feedpoint impedance. So a quarter-wave element is a half-wavelength round trip.

What then is the "interesting thing" that happens at the end of the antenna? The thing to realize is at the first instant something happens at the feedpoint, the feedpoint doesn't "know" the antenna is going to abruptly end some distance away. Even though the antenna is an open circuit, some current will initially flow, starting a wave propagating down the length of the antenna. When this wave reaches the end of the antenna, another wave starts in the opposite direction.

To develop some intuition for how this works, I suggest reading How does the current know how much to flow, before having seen the resistor? and these excellent animations by Daniel Russell.

The reflections take a half cycle to make their round trip, so by the time the reflection (of opposite polarity) reaches the feedpoint, the feedpoint has also reversed polarity. Thus the current in the reflected wave reinforces the current driven by the feedpoint. This current reinforcement means the feedpoint can drive a larger current with a lower voltage. In other words, it has a low impedance. And this is why an antenna which is an open circuit at DC can be a low impedance around 50 ohms at RF.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16687/significance-of-1-4-wavelength-with-respect-to-antennas, by Newbie, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
