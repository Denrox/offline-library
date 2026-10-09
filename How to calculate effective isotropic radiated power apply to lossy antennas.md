# How to calculate effective isotropic radiated power apply to lossy antennas

*Tags: antenna · score 4*

## Question

If a band allows one watt EIRP and I have an antenna that is 1% effective could I legally run 100 watts into the antenna because only one watt is radiated?

If that same antenna also has a gain would I then have to include this as well in the calculation?

How about feed line losses, do I then just multiply these factors together?

## Answer (score 2, by tomnexus)

If the antenna *gain* is 1%, then yes.

If you have a 1% *efficiency* antenna, but it's a dipole, then no, as your EIRP would be 1.6 W from the dipole gain of 2 dBi.

**Gain** is the property of the antenna most easily measured at the terminals, and covers the effective performance of the antenna.

EIRP is simply the product of the transmitter power and the gain of the antenna, so 100 W into a 0.01× gain antenna is an EIRP of $100\,\mathrm{W} \cdot 0.01 = 1\,\mathrm{W} $

Antennas have two relevant properties which make up gain: Directivity (the degree to which the radiation is concentrated in a particular direction) and Efficiency $\eta$ (the fraction of the total input power that is radiated). $ Gain = Directivity \cdot \eta$

**Feedline losses** act simply to reduce the transmitter power. So if your feedline loss is 3 dB, then the transmitter power is multiplied by $10^{-3/10}$ or $ 0.5 $

**For example**: A short loaded dipole, 8.7 ft long, has an efficiency at 7 MHz of about 4%. It has a directivity of about 1.8 dB (a short dipole has slightly less directivity than a 1/2wave dipole).  
It is fed with a coaxial line with 2 dB of loss. With 100 W input, it will produce, *at the peak of its radiation pattern* an EIRP of $$\mathit{EIRP} = 100\,\mathrm{W} \cdot 10^{-2/10} \cdot 10^{1.8/10} \cdot {4 \over 100} = 3.8\,\mathrm{W} $$.  
By the way, I like to use Google Calculator for these sorts of things, it knows the constants and calculates with units. Try it.

**A note about licensing restrictions**: some countries have a restriction on power into the feedline, and even DC power into the final amplifiers, so study your own regulations. An EIRP limit is rare, I've only seen it on the 600 m band.  
For example, in South Africa:

**"Carrier wave power"** means the average power that is supplied by the transmitter to the antenna transmission line and is measured during one radio-frequency cycle in conditions of no modulation;

**Transmitter Power Output of Amateur Radio Stations**  
The maximum power output of the transmitter, as measured at the antenna port, must not exceed the levels specified in the national radio frequency plan for the relevant licence classes ...

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6433/how-to-calculate-effective-isotropic-radiated-power-apply-to-lossy-antennas, by Arthur, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
