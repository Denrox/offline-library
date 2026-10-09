# Is ladder line necessary when using a non-resonant dipole through a tuner?

*Tags: wire-antenna, antenna-tuner, impedance-matching · score 4*

## Question

I've heard if I have a dipole of some arbitrary length, or a random wire, the SWR can be very bad. An antenna tuner can present a decent match to the transmitter, but the SWR on the feedline will be very high, and thus ladder line is required.

Is ladder line really required, as opposed to coax? What are the essential properties of a feedline in this application?

## Answer (score 4, by Phil Frost - W8II)

This can indeed be a fine setup. With a suitably low-loss feedline, and a good tuner, just about anything can be made to function as an effective antenna.

There are two factors that determine the losses in this situation:

1. the matched loss of the feedline, a function of length and the attenuation specified in the datasheet, and
2. the operating SWR on the feedline, which depends on the ratio of the feedline and load impedances.

When the SWR is greater than 1:1, some fraction of the power is reflected from the antenna, back towards the transmitter. The antenna tuner then re-reflects this reflected power back at the antenna.

Eventually, all the energy is either radiated by the antenna, absorbed by the feedline, or absorbed by the tuner. Since each parcel of energy is making multiple "bounces" between the tuner and the antenna, it's subject to the feedline loss multiple times. Obviously, lower feedline loss means less loss. A lower SWR means fewer bounces back and forth, so again less loss. See [What is the actual loss in a feed line with high SWR?](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md)

Ladder-line does not intrinsically have lower loss than coax. For example, this 300 ohm ladder line sold by DX Engineering has a loss of 0.668 dB per 100 feet at 30 MHz. Compare to Times Microwave LMR-400 at 0.7 dB for the same. There's better coax, and there's better ladder-line, but generally the performance of a transmission line is a function of the dielectric and conductor resistance (mostly the latter at HF), not whether it's coax or ladder-line.  
*specified attenuation for DX Engineering ladder-line per 100 feet*  
*specified attenuation for LMR-400*

Note the significantly higher loss when the ladder-line is damp. Coax maintains its performance when wet, covered in snow, ice, or dirt, when buried, run through conduit, attached directly to a tower, etc. This is why commercial installations overwhelmingly prefer coax.

Ladder-line does tend to have a higher characteristic impedance, somewhere between 300 and 600 ohms for common designs. This is important.

A resonant dipole is at an impedance minimum, around 72 ohms. So when the dipole isn't resonant, the impedance will be higher, with a typical maximum around 5000 ohms.

Modelling software and antenna analyzers will give an SWR, but this is not the SWR on the feedline unless the feedline has a characteristic impedance of 50 ohms. Given our dipole which may be between 72 and 5000 ohms, this gives a possible SWR from 1.44:1 to 100:1.

With 300 ohm ladder-line, the antenna analyzer will still say the SWR is 100:1 in the worst case. But actually the SWR is only:

$$ { 5000\:\Omega \over 300\:\Omega } = 16.7:1 $$

This is why ladder-line tends to have a lower loss in this antenna system. Not because it is an inherently lower-loss feedline, but because the SWR is reduced.

However, if you wish to use coax, it's an easy problem to solve. A 4:1 balun on 75 ohm coax divides the load impedance by 4. So again calculating the SWR at the worst case 5000 ohm load:

$$ { 5000\:\Omega\:/\:4 \over 75\:\Omega } = 16.7:1 $$

That's the same SWR as the 300 ohm ladder-line. If the coax and ladder-line have equal matched loss, their total losses will be the same also.

A balun with a higher transformation ratio will reduce the SWR further, and losses with it. If the antenna impedance could be anywhere between 72 and 5000 ohms depending on operating frequency, then the best "compromise" feedline impedance is:

$$ \sqrt{5000\:\Omega \cdot 72\:\Omega} = 600\:\Omega $$

This gives a worst-case SWR at the extremes of high and low antenna impedance of:

$$ {600\:\Omega \over 72\:\Omega} = {5000\:\Omega \over 600\:\Omega} = 8.3:1 $$

Not such a horrible SWR. This could be realized with:

- 600 ohm ladder-line, or
- 300 ohm ladder-line and a 2:1 balun, or
- 75 ohm coax and an 8:1 balun, or
- 50 ohm coax and a 12:1 balun.

So, in summary:

- Ladder line is not necessarily lower loss, but it does have a higher characteristic impedance.
- Non-resonant antennas tend to have higher feedpoint impedances.
- With an impedance transforming balun, coax can have the same SWR as ladder-line.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9037/is-ladder-line-necessary-when-using-a-non-resonant-dipole-through-a-tuner, by Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
