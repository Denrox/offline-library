# What is the largest gauge (thinnest diametre) wire I may use as an antenna?

*Tags: antenna-construction, wire-antenna · score 9*

## Question

A follow-up to [Good wire for wire antenna?](Good%20wire%20for%20wire%20antenna.md)

I'm QRT at present - thanks to fooling around with just a couple of diodes and PVC capacitors instead of a well-regulated supply. The antenna I used earlier was a mono-bander inverted-vee for 20M. I may be able to get a 40M inverted-vee, possibly even a 40M dipole on the premises but the lower bands are out of the question ... which is where I'd like to try out sometime.

I'm toying with the idea of an **end-fed catenary** held aloft. Perhaps a weather balloon, or two may provide the necessary lift capacity. A relative rigid wire such as the SWG16/14/12 might puncture the balloon though, and prove a difficult lift to boot. The rig I used (on loan from an elmer) is capable of 20W. On the 160 though I'd like to try no more than 5W.

*To the best of my knowledge there is no restriction on gauge hereabouts (VU), as there **may be** in other parts of the world.*

Given the **constraints**

- QRP
- Antenna wire flexibility

**Assuming** the antenna may be reasonably matched

What guage wire can I use without the wire itself giving up the ghost on Tx?

## Answer (score 7, by Phil Frost - W8II)

You can make the wire as thin as you want. There are two non-obvious things to point out:

Firstly, as you make it thinner, resistive losses go up. You could make a worst-case calculation of the resistive losses by assuming the current is at a maximum everywhere in the antenna. If you put 20W into a 50Ω antenna, the current will be:

$$ \begin{align} I^2 R &= P \\ I^2 (50\Omega) &= 20\text{W} \\ I^2 &= \frac{20\text{W}}{50\Omega} \\ I &= \sqrt{\frac{20\text{W}}{50\Omega}} \\ I &\approx 632\text{mA} \end{align}$$

That should give you some idea of the kind of conductor you need. Of course, this is the current only at the point where the impedance is 50Ω; if we are talking about a center-fed dipole, the impedance approaches infinity at the ends, and consequently the voltage approaches infinity, and the current approaches zero. Consequently, your resistive losses will be lower than what this suggests, but it's a simple calculation that will give you a rough idea.

Another way to approach it: the antenna efficiency, if we assume there are no losses but resistive losses can be defined as:

$$ \text{efficiency} = \frac{R_\text{radiation}}{R_\text{radiation}+R_\text{conductor}} $$

If the resistance you add with your thin wire isn't significant compared to the radiation resistance, then you aren't significantly impacting the antenna's efficiency.

The other concern is this: some materials (namely iron) exhibit magnetic hysteresis, which represents another significant loss at RF. This rules out most steel cables, though you may find a stainless steel cable that works. Finding data on the magnetic properties of a cable at the hardware store will be difficult, however, so it might be simplest to avoid all steel.

## Answer (score 5, by Walter Underwood K6WRU)

The "rule of thumb" for keeping the skin effect at bay is to use conductors that have a diameter greater the twice 3-5 skin depths. Twice the depth because if you can envision the wire having RF current develop a tapered current density from the surface inwards to the center, you go half way in and half way out, 2x. So for 1-skin depth in copper of 1.37 mils at 3.5 MHz, 3-5 skin depths is 4-6.8 mils. Doubling 6.8 (to be conservative) you get 14 mils diameter. That diameter is 27AWG wire.

For 7 MHz, the skin depth is 0.97 mils. 3-5 skin depths is 2.9-4.9 mils, and doubled, that is 10 mils, giving 30AWG wire.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/588/what-is-the-largest-gauge-thinnest-diametre-wire-i-may-use-as-an-antenna, by VU2NHW, Phil Frost - W8II, Walter Underwood K6WRU. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
