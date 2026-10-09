# What's the difference between "minimum SWR" and "resonance"?

*Tags: antenna, antenna-theory, impedance, jargon · score 9*

## Question

Is the point of minimum SWR equivalent to resonance? Exactly what does resonance mean, anyway?

## Accepted answer (score 4, by K7PEH)

Good questions. But, I think another question to add is: What is more important, SWR or resonance?

Given that this is the "Amateur Radio" forum, I think answers that are most meaningful to amateur radio operators are more justified in this discussion. The reason I say this is that resonance and SWR as testified by several exchanges and questions are debatable things.

For example, I operate regularly on 80, 40, 30, 20, 15, 12, and 10 meter bands. I sometimes visit 17 meters once in a great while. But, given all those bands and the frequencies I operate NONE of my antennas are resonant. That is because true resonance is at a single frequency for a given antenna (e.g. Dipole). But, if the SWR is within reasonable limits or it handled by an antenna tuner (aka match coupler) then the antennas are very effective even when not resonant.

There are several definitions of resonance. In general, if the antenna impedance at a given frequency is purely resistive, with zero reactance (or, near zero) then that antenna can be considered resonant at that frequency. This resistance is not usually the same as the typical 50-ohm output of a transmitter. In fact, a perfect dipole (with no ground effects) has a radiation resistance of approximately 71 ohms. Thus, this perfect resonant antenna does not have a SWR of 1:1 because the resistance is not 50 ohms.

But, SWR is important too for two different reasons. First, to protect the PA circuits of a solid state transmitter (or, amplifier). Reflected voltage can destroy the output transistors so low SWR helps protect the solid-state circuitry. Most modern transmitters (transceivers) have protection circuits to roll back power to safe levels when the SWR is too high. My own Elecraft K3 starts this when faced by an SWR at a little over 2:1.

The second reason SWR is important is to limit the losses in transmission line between the transmitter/transceiver/receiver and the antenna. The higher SWR causes the losses to increase There are calculators available on-line (and the ARRL TransmissionLine application) to compute the losses given the input and load SWR or actual $R+jX$ impedance. I have written my own in Mathematica.

In addition, SWR is often an indicator of problems in an antenna system. Monitoring SWR is something that should be done by ham operators as it will show problems. One afternoon I was preparing for a CW Traffic Net schedule and did a quick key down merely to look at my SWR. It spiked with the alert beep sounding plus red LED lights blinking. I looked out into the back yard and saw that my 80 meter dipole was laying on the ground. One of my anchor point ties had failed.

Minimum SWR (as asked in the question) has nothing to do with resonance (by itself). If I tune up on the 160 meter band using my 80 meter dipole I can find a minimum SWR and that minimum is on the order of 250:1 or so. My tuner is good but it can't handle that wide of an SWR. But, a resonant antenna should have a low SWR and likely at the likely minimum at the resonant frequency. But, as I mentioned earlier for the dipole, this low SWR will not usually be 1:1 as the actual radiation resistance for the antenna is almost always not the same as the 50 ohms expected by the transmitter.

Personally, when I am building antennas, managing and designing for minimum SWR across the frequencies I want to operate is the most important thing. Minimum SWR is hopefully under 3:1 for most of a band but even my 80 meter dipole has a higher SWR at the high end of the band (3.9 MHz) with an SWR about 5:1 (my tuner matches this with no problems but I do have to pay for that higher SWR in the transmission loss to the antenna which is the reason I use LMR400 low loss coaxial cable. One of my Mathematica programs will do a full 3 to 30 MHz sweep (all frequencies in 20 KHz steps) of my antennas I am designing (in concert with solutions produced by NEC4) and I compute the SWR, smooth interpolate it, and then plot the results. Visually I can see all the low SWR (under 3:1) spots for a given length of wire of the antenna.

## Answer (score 4, by Phil Frost - W8II)

*Resonance* is at a particular frequency where reactance is zero, and thus current and voltage are in phase. To illustrate, here's a plot of the feedpoint resistance, (R) reactance (X), and impedance magnitude (|Z|) of my backyard trap vertical on 30 meters:

Notice how at resonance the resistance is not 50Ω, so the SWR here is something higher than 1:1.

There's another resonance around 10.62 MHz, but here the resistance is off the chart. As we'll see in the next chart, although the antenna is resonant here, the SWR is very bad.

Here are the same data, but plotted as SWR:

The minimum of the SWR dip is not quite at the same frequency as resonance.

(You can also see that I need to go out there and tune this antenna!)

A Smith chart is a nice way to visualize both impedance and SWR on the same chart. Here are the same data again:

The horizontal line in the middle represents all the resonant points, that is, all the points where reactance is zero.

The very center of the chart represents 50+0jΩ, and a 1:1 SWR. SWR is measured by the distance from the center, and that bullseye in the middle represents an SWR of 1.6 or better.

And you can see the curve gets *a little bit* closer to the center just a bit away from resonance. The difference is small enough to barely matter in practice.

You can also see the curve continue around until it hits the middle line again: that's the other resonance with a bad SWR.

It's possible to have an antenna which dips into that 1:6 SWR circle from above or below, and never crosses the 0 reactance line at all. With self-resonant dipoles and verticals the resonant impedance is a decent match and will be near the center, but with other kinds of antennas there might be a matching network involved which creates a very different trajectory through the Smith chart.

The addition of a feedline also changes the picture. As the feedline length varies, the impedance at any one frequency rotates about the center of the Smith chart. The SWR of that point remains constant, but for each half-wavelength of feedline added, the point makes a full rotation. So it's possible with the right length feedline to make *any* impedance resonant. It's also possible to take any resonant impedance which is not a perfect match and make it non-resonant.

## Answer (score 3, by Communicationantennas.com)

The antenna impedance is $R+jX$ where $R$ denotes the real part and $X$ denotes the imaginary part of the impedance. Resonance means the imaginary part is exactly zero.

Most antenna designs do not have an impedance of exactly 50 Ω, and their resonance is somewhere close to 50 Ω. For example the resonance may be at 40 Ω, but the minimum SWR may be at $(45+5j) \,Ω$, which is closer to 50 Ω as seen on a Smith chart.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2482/what-s-the-difference-between-minimum-swr-and-resonance, by Phil Frost - W8II, K7PEH, Communicationantennas.com. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
