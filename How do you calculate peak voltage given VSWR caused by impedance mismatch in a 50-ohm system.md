# How do you calculate peak voltage given VSWR caused by impedance mismatch in a 50-ohm system?

*Tags: rf-power, impedance-matching, transmission-line, voltage · score 3*

## Question

I would like to choose a feedline that is safe for the wattage at a given VSWR to avoid coax arcing.

How do you calculate peak voltage given a peak power in watts and maximum expected VSWR from impedance mismatch in a 50-ohm system?

I've found many examples that discuss how VSWR is calculated or how reverse wattage can be determined, but how do you calculate the peak max voltage at a given VSWR and wattage when there is a mismatch?

if $VSWR = \frac{V_{fwd}+V_{rev}}{V_{fwd}-V_{rev}}$ then solving for a $VSWR=25$ and $V_{fwd} = 273$ we get a $V_{rev}=252$

Is the max peak then $252+273=525$?

## Accepted answer (score 5, by hobbs - KC2G)

Before going forward I want to make a quick note: your example of 273V is the *RMS* voltage it takes to put 1500W into 50 ohms — but if you're concerned about dielectric breakdown then you actually want to be thinking about the *peak* voltage, which is a factor of $\sqrt{2}$ higher, i.e. 386 volts. I'll be using that value later on.

Wikipedia actually has the formula you need: $V_{max} = (1 + |\Gamma|)V_{fwd}$, where $|\Gamma|$, the magnitude of the reflection coefficient, is $\frac{\mathrm{SWR} - 1}{\mathrm{SWR} + 1}$. This ends up being 525 V for your example, as you worked out, but you don't need to solve any systems of equations; just multiply by $1 + \frac{\mathrm{SWR}-1}{\mathrm{SWR}+1}$.

The worst case you have to deal with is a 2x voltage on the line for infinite SWR, assuming forward power is held constant. If that sounds weird, remember that infinite SWR occurs with complete reflection ($\Gamma = 1$ or $\Gamma = -1$), which makes $V_{rev} = V_{fwd}$. The two voltages cancel to 0 when out of phase, and add to $2 \cdot V_{fwd}$ when in phase, and it's the 0 in the denominator that makes SWR infinite.

But note that "if forward power is held constant" caveat from above. If you instead try to make *net* power $P_{fwd} - P_{rev} = \frac{V_{fwd}^2 - V_{rev}^2}{R}$ constant, e.g. by putting a matching network at the transmitter end of the feedline, then that means that $V_{fwd}$ has to increase along with SWR.

So, 386Vp is what it takes to get 1500W forward power into 50 ohms. But if SWR = 25, and $|\Gamma| = 0.923$, then you need $V_{fwd}$ to be 1003V to get 1500W out, in which case $V_{max}$ on the coax is 1930V, which is a bit more substantial. And of course in the limit of infinite SWR you end up needing infinite voltage to put any power into the load. The additional factor you need to add is $\frac{1}{\sqrt{1 - |\Gamma|^2}}$ or $\frac{\mathrm{SWR}+1}{\sqrt{(\mathrm{SWR}+1)^2 - (\mathrm{SWR}-1)^2}}$, e.g. $\frac{26}{\sqrt{26^2 - 24^2}} = 2.6$ for a 25:1 SWR.

## Answer (score 4, by tomnexus)

For amateur use, breakdown from overvoltage is probably not something you need to worry about. The main limits to power handling of a cable come from resistive heating and dielectric heating.

Arcing in coax is only going to be a problem for very low duty cycle applications, with modest average power and high peak power. Things like RADAR, where you have several kW but for only a few microseconds at a time, average power of tens or a hundred watts. Also for carrying DC power if that's your thing.

Well-specified cables have both specifications; let's take a look at an old favourite, LMR-400:  
Its basic electrical specifications are pretty impressive when it comes to voltage:  
  
2.5 kV between inner and outer. Also the DC resistance is amazing, a few ohms per kilometre!

But on page two, the power limits are much lower:  
At 150 MHz, the 2 metre band, the average power it can carry is 1.5 kW, for an RMS voltage of 274 or a peak of 383 V, which is only 1/10th of the maximum DC voltage. This is for ideal conditions: stated as VSWR=1.0; Ambient = +40°C; Inner Conductor = 100°C (212°F); Sea Level; dry air; atmospheric pressure; no solar loading.

For infinity:1 SWR the voltage and current are doubled, (at different places on the line), meaning you have to reduce power by four times for the same heating (some assumptions!). You will also find the cable gets hot just in a few places, half a wavelength apart. I've felt this on RG316 cable at quite modest power, 10 watts or so.

The thermal time constant of the cable is probably longer than a second, so for morse code you could use the average power, not the peak. SSB also has a fairly high peak to average ratio, perhaps 4:1, again you could probably get away with using the average, as long as you never say "Haaaaaaaalo" for too long!

In summary, for high power operation, you need to choose a cable by its published power handling rating, not its DC spark-over voltage. Derate it by up to 4 times, if the SWR is going to be high, and some more for safety. Buy cables and connectors from a reputable manufacturer that has this detail on its datasheet.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20393/how-do-you-calculate-peak-voltage-given-vswr-caused-by-impedance-mismatch-in-a, by KJ7LNW, hobbs - KC2G, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
