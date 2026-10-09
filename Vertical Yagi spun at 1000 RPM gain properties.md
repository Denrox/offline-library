# Vertical Yagi spun at 1000 RPM: gain properties?

*Tags: antenna-theory · score 4*

## Question

If I were to mount my 10 m vertical Yagi on a pole with a motor attached at the bottom with the appropriate fastening and coax mounted via electrical brushes, if the Yagi is spun at say 1000 RPM would that make it have its rated gain in all directions ?

## Accepted answer (score 14, by Kevin Reid AG6YO)

As has already been stated, this will add amplitude modulation to your signal — you will "achieve its rated gain in all directions" but only at the *peak* of the modulation; the *average* will be much less, equivalent to an antenna with no azimuth gain but a similar elevation gain pattern.

You and other readers might be interested to learn that **this modulation has actually been used *intentionally*, in the aircraft navigation system VHF Omnidirectional Range (VOR).** This system allows an aircraft to, by receiving signals from a ground station, determine the compass direction in which the aircraft lies relative to the ground station.

The system in its original form worked by spinning a directional antenna at 30 Hz, causing amplitude modulation of the signal. The station also transmits, on the same carrier frequency but from a non-directional antenna, a subcarrier also frequency modulated at 30 Hz (like FM stereo encoding or AFSK). By comparing the phase of the amplitude modulation (varies with direction of the receiver) to the phase of the frequency modulation (does not vary), the direction can be obtained.

Later VOR stations replaced the rotating antenna with a circular phased array, so that the mechanical rotation could be replaced with electronic, but the signal is received and decoded the same way.

## Answer (score 6, by hotpaw2)

Depending on the gain characteristics of your Yagi antenna, you’ll be adding an amplitude modulation of 16.7 or 33.3 Hz to your signal, plus a similar phase modulation. These added modulation sidebands will also add to the bandwidth used. This rotational modulation will have different phases to your original signal modulation in different directions, so your resulting signal will likely not be symmetric in all directions. If you want, control and/or synchronize to this asymmetry, you could use this for some sort of directional beacon or radar.

## Answer (score 4, by Marcus Müller)

rated gain in all directions ?

No. And a lot more problems. Primarily, for any thinkable use case, this is a bad idea.

What rotating the antenna will do is of course rotate the antenna pattern, "averaging out" (over the curse of a multiple of a rotation period) the antenna pattern to look like a circle, i.e. equally good (or bad) in all directions; the **average** gain of the original Yagi's radiation pattern, not the **maximum** gain.

If you wanted that, using a high-gain antenna type like a Yagi would be a terrible idea – just use the dipole (the driven element in your yagi), and you'd instantly have an omnidirectional antenna for a fraction of the effort, cost, maintenance, complexity and hazard!

1000 rpm = 116.7 Hz would be far too slow for anything useful: Let's focus on the transmit side for a second here; since antennas are reciprocal, the exact same things apply to receive.

So, you're transmitting with your antenna. That means that your antenna's main beam sweeps around. A receiver in a specific direction will hence see "strong signal" when he's in the main beam's direction 16.7 times per second, and all the other times they'd see little signal power at all.

- For any signal that has a bandwidth significantly larger than 16.7 Hz, this simply constitutes slow fading over a cyclostationary signal: The "very strong for short, bad rest of the time, 16.7 times per second" is typically harder to solve than an averagely moderately low receive power, because it contains an element of temporal change in addition to the majority-of-time-bad receive power. In essence, for a **looooong** duration, your signal will be unusable, if you needed any gain to begin with, and from the short duration where it's good, you'd need to reconstruct the lost part.
- For any signal that has a bandwidth lower than 16.7 Hz, this constitutes fast fading, i.e. the channel changes within the duration of one *symbol*; for anything that requires coherency (FM, PSK, most FSK, QAM, …), that simply means broken transmission. For power-detection only systems (e.g. AM, OOK, PPM), that might be workable by averaging out, but still not really desirable.
- For any system that has a signal bandwidth of roundabout 16.7 Hz, this is kind of neither and kind of both, and you'd really want to avoid that situation, because your rotation influence becomes statistically indistinguishable from your signal, and then no communication will be possible.

Basically all useful communication systems fall in the first category.

You can also look at this from the perspective of Doppler: by rotating the antenna, you'd constantly be shifting the phase center of the antenna, relative to a fixed direction. That means that you're modulating the phase of the signal with a periodic function – and that's a frequency shift, just like a Doppler effect caused by your communication partner moving rapidly towards you and away from your 16.7 times per second.

The only use case I could make out for this is in an indoor scenario with a lot of multipath propagation, you could get some temporal diversity for a diversity combination scheme. But that wouldn't incorporate "masts", and it would be at much higher frequencies (2 GHz and upwards), and it would happen at not about 17, but 100,0000 to 1 million rotations per second, and it wouldn't happen through rotating a physical antenna, but through digital beamforming or antenna switching.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15503/vertical-yagi-spun-at-1000-rpm-gain-properties, by Andrew, Kevin Reid AG6YO, hotpaw2, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
