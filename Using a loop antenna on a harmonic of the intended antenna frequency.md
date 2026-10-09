# Using a loop antenna on a harmonic of the intended antenna frequency

*Tags: antenna-theory, magnetic-loop · score 5*

## Question

I bought a MFJ 1786 Magnetic Loop Antenna, which is made for 10 thru 30 MHz. It is not meant for use on 40 meters. The antenna has its own built in tuner. I have a Yaesu FT-890AT with built in antenna tuner. So my question is: could I tune the loop to a harmonic frequency of the frequency that I wish to work on 40 meters and then tune the Yaesu for the best SWR? Will it work even at somewhat less than optimal? This would allow me to work CW at night.

## Answer (score 3, by Phil Frost - W8II)

Dipoles are resonant on their fundamental frequency, and all odd harmonics. So a dipole resonant at 10 MHz is also resonant at 30, 50, 70 MHz and so on.

At the fundamental frequency it takes one cycle for a wave to travel the full length of the antenna and back. At odd harmonics it takes 3, 5, 7, and so on cycles. Only the odd harmonics are considered because on odd numbers the feedpoint in the middle falls on a low impedance point of the antenna. On even numbers the feedpoint is a high impedance and thus presents an extremely poor match.

This 10 MHz dipole is not resonant at any frequencies below 10 MHz. The antenna is simply too short.

Self-resonant, or full-wave loops are similar, being effectively folded dipoles.

But the MFJ 1786 is a different beast. It consists of a very small (relative to wavelength) loop, which presents an inductive impedance. A variable capacitor cancels that inductance, and the loop and the capacitor together are resonant.

As the loop becomes smaller relative to wavelength (in other words, as you move down in frequency), the impedance of the loop becomes more inductive, and thus requires more capacitance to tune it. The higher reactances involved also mean a higher Q, and a higher peak voltage across the capacitor.

There's a practical limit to how small the loop can be. While it's easy enough to make a larger capacitance, it's more difficult to make a capacitor with a sufficiently large capacitance while still withstanding the peak voltage.

If the antenna is designed to work down to 10 MHz it will not work at 7 MHz. The variable capacitor in it is not large enough, and if it were, it would not be able to handle the voltage without arcing. So at 7 MHz, the antenna will not present a good match.

It's possible you can compensate for this with an antenna tuner, but it's unlikely. The match is probably bad enough to be outside the tuner's capabilities.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6741/using-a-loop-antenna-on-a-harmonic-of-the-intended-antenna-frequency, by jim, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
