# What is the difference between antenna input impedance and its radiation resistance?

*Tags: rf-power, impedance-matching, impedance, radiation · score 4*

## Question

I got to know that the input impedance of the halfwave dipole antenna is given as:

Zin=1/Im* sin(β(H-|Z|))

where Im is the maximum current on the antenna( when excited with a 1 volt supply),

H is the half-length of the antenna,

Z is the position on the antenna and β is wave number.

Apart from the input impedance there is another parameter called as radiation resistance calculated by dividing the I2m from the power radiated by the antenna.

Now my doubts are:

1. Are both radiation resistance and input impedance one and the same?
2. If I take a full wave dipole (β*H=π) then at Z=0 ( input terminal) the input impedance value becomes infinite which is similar to open circuit condition so does that mean there wouldn't be any radiation by the antenna?
3. If I consider the current distribution of the antenna for the full wave dipole (as given in the figure, the current standing wave value becomes zero at the input end of the antenna how can there be a distribution of the current on the antenna if the input current is zero?

I seem to have confused myself a lot. kindly clarify me on this doubt.Thank you in advance.

## Accepted answer (score 5, by Andrew)

Antenna input impedance and radiation resistance are two different characteristics however they are intimately related.

The input impedance of an antenna is a complex quantity, with a real part Resistance R and an imaginary part Reactance X.

Only the real part of the impedance can absorb RF energy and result in EMF radiation, and so most antennas are designed to have no reactance at resonance. The input impedance is determined largely by the dimensions of the antenna, the impedance of free space, the frequency of operation, and is the same during transmission and reception.

Radiation resistance is usually only mentioned with reference to transmission, and is a virtual resistance which is presented to the current from the transmitter as a result of the absorption by the antenna of the applied RF energy as radio waves are being radiated.

Wikipedia says "The radiation resistance is typically defined as the value of resistance that would dissipate the same amount of power (as radiated heat) as is dissipated by the radio waves emitted from the antenna, with the same input current passing through it."

For center fed lossless dipoles with antenna elements which have zero resistance, the real part of the input impedance is equal to the radiation resistance only for antenna lengths which are integral multiples of odd numbers of wavelengths of the frequency of operation.

For even multiples the relationships is more complex.

If the input impedance is infinite, then zero current will flow into the antenna and no radiation will occur, similarly if the impedance is zero then maximum current will flow but there is no resistance to dissipate any power and no work can be done and so no radio waves are produced.

The typical dipole current and voltage distribution pictures you see everywhere such as the one in your question are very confusing and never explained well at all.

What you are looking at is a snapshot in time of the actual current profile in space along the antenna elements at the instant that the current is at a peak. This waveform is an interference pattern or standing wave which is produced by the initial application of RF energy at the feed point and the addition of that to the reflection from the ends. You cannot see the incident and reflected waves, each is obscured by the other, all you can see is the resultant standing wave, the amplitude of which is oscillating in time in sinusoidal fashion at the frequency of the applied RF signal.

What you say is exactly correct, for an ideal full wave dipole, if the input impedance is infinite then antenna current must be zero, that picture contradicts itself and just gives you the current profile assuming the input impedance wasn't zero and the length was one wavelength.

There are other explanations around which show a resonant series center feed half wave dipole with the voltage across the center feed points as always being zero. These are also confusing as the voltage across the center can't be always be zero otherwise you have a short circuit. They neglect to mention the fact that the voltage of the applied RF source at the feed point adds vectorily to that presented by the standing wave at the feed point, and the RMS value of this voltage never actually reaches zero, but is rather :

Vfeedpoint = Vapplied + Vstandingwave = Iantenna x radiation resistance

It is in fact the difference in phase between Vapplied and Vstandingwave, as determined by how far the ends of the antenna are away from the center feed point, which determines the value of reactance present in the feed point impedance, but that is another discussion for another day.

Hope that helps !

## Answer (score 4, by hobbs - KC2G)

1.

No, they're separate. Radiation resistance *contributes* to the real part of input impedance, but so does ohmic loss (heating), and non-radiative coupling with the EM field produces the imaginary part of the impedance. It's useful to remember, however, that eventually 100% of the net power reaching the feedpoint is either spent in the radiation resistance (making radio waves) or spent in the ohmic loss (making heat), so efficiency means keeping $\frac{R_{rad}}{R_{loss}}$ high.

2.

Ideally, yes. If the antenna has infinite input impedance then there is no current flow into it. But this can only happen with an ideal dipole in free space. In the real world, if you consider coupling with the surroundings, impedance is never truly infinite, although for a full-wave dipole it can still be quite high (thousands of ohms).

3.

This is a point that has caused a lot of confusion, and [there's a Q&A on this site relating to it](How%20can%20the%20voltage%20at%20the%20center%20of%20a%20resonant%20half%20wave%20dipole%20be%20zero%20if%20the%20input%20impedance%20is%2075%20ohms.md). I'll try to come up with a semi-satisfying answer in two parts. Part one is that the standing wave current being zero at the center is no more problematic than the standing wave current being zero at the ends. In both cases energy is being stored in an external EM field, so we don't expect proportionality of voltage and current to hold at a point. Part two is that the *total* current isn't zero at the feedpoint (unless the input impedance is infinite, which it generally is not). But the feedpoint is connected to a transmission line, which carries equal-and-opposite currents away from the antenna, so it "counts for zero" towards the standing wave current. I'll admit that I'm just kind of feeling my way here, and someone with better theoretical grounding might be able to come up with a clearer explanation, but I haven't seen one yet.

## Answer (score 2, by hotpaw2)

1.

No. A standard 50 Ohm non-inductive resistor (e.g. dummy load) can have 50 Ohms of real impedance, but zero radiation resistance.

2.

Ideal full wave dipoles are a mathematical fiction. Real dipoles have parasitics and other finite dimensions, which allow some small amount of radiation.

3.

The feed point and ends of a resonant dipole act like capacitors (no real current directly through them, but potentially lots of EM displacement current. See Maxwell). If you manage to charge them up, they can later discharge though any connected wires of a different voltage potential (with or without a connected feedline). That discharge will have a current distribution, and depending on the wire's length, parasitic inductance, and termination impedance, a resonant frequency.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20871/what-is-the-difference-between-antenna-input-impedance-and-its-radiation-resis, by Moulee, Andrew, hobbs - KC2G, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
