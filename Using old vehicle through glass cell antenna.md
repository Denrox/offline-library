# Using old vehicle through glass cell antenna

*Tags: antenna · score 4*

## Question

My old (2001) Seville had a cell phone with antenna mounted on the rear glass. The coax connects inside the glass, with signal passing through the glass to the whip mounting plate.

I'm wondering if I can use the old cell antenna mount (through glass) and just replace the whip to make a dual band 70cm/2m antenna. I discovered that the old cell radios in this car were on 800-850MHz, which would make a full wavelength antenna 0.35m long. Which is approx 1/2 wavelength for 440MHz, and <1/4 wave for 140Mhz

Has anyone done this before? The base inside the glass is more than a piece of metal I suspect, perhaps a loading coil. Any advice is appreciated.

## Accepted answer (score 2, by user10489)

These types of antennas are typically capacitively coupled. They will not work on metal tinted glass or glass with near by wires in it.

They have to be calibrated for glass thickness and dielectric constant. If it was meant to be used generically rather than on a specific vehicle, there may be a set screw or something to adjust the calibration. Likely the external antenna and mount need to be matched to the inside piece, but you might be able to calibrate for that.

You would need an antenna analyzer for the frequency in question (or a VNA) to do this right.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21212/using-old-vehicle-through-glass-cell-antenna, by TSG, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
