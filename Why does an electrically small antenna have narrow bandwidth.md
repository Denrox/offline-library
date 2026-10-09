# Why does an "electrically small" antenna have narrow bandwidth?

*Tags: antenna, antenna-theory, magnetic-loop, small-loop · score 4*

## Question

Reading this interesting piece on magnetic loop antennas, the author explains that a magnetic loop has great efficiency even at small size, but the the price you pay is very narrow bandwidth. Why is this?

It seems counter-intuitive (and miraculous) to me that efficiency doesn't suffer, but bandwidth does when antenna size is much much smaller than wavelength.

## Accepted answer (score 12, by Phil Frost - W8II)

Short answer: electrically small antennas have a relatively low radiation resistance. With less resistance, the resonance is less damped, meaning a higher Q factor and consequently less bandwidth.

To expand on that a bit, consider a children's playground variety swing. It's essentially a pendulum, and depending on the length of the swing and the mass of the child it will swing at a particular frequency. By shifting one's weight at exactly this frequency, it's possible to get the swing going very high with very minimal (but well-timed) energy inputs.

The swing works because the work of each pump adds more energy, while relatively little is lost to friction. Thus with the proper timing, the work from each pump adds to the work of the previous until the swing is very high.

When the energy lost to friction is low compared to the stored energy, we say the swing has a high Q. The swing will continue swinging for quite a while even if the rider stops pumping. And the timing is very important, so it has low bandwidth.

Now imagine a swing submersed in a very viscous goo. The work of each pump goes almost entirely into the friction, and very little is stored in the swing. If the rider stops pumping the swing stops almost immediately (low Q). And the timing of the pumps hardly matters since all the work is lost to friction (high bandwidth).

A dummy load is analogous to this swing in goo: it stores no energy at all, and all the input energy is converted immediately to heat in the resistance. Thus a dummy load has *very low Q and very high bandwidth*.

Something like a resonant dipole is somewhere in the middle of these examples. Instead of alternating between kinetic and potential energy, it alternates between energy stored in a magnetic and electric field. However with each cycle some of this energy is lost to radiation, and this appears at the feedpoint as radiation resistance. This appears to a transmitter as an ordinary resistance just as the dummy load did, but this work is going into radiation, not heat.

This radiation resistance dampens the resonance, giving this example a *moderate Q, and a moderate bandwidth*.

As the dipole gets shorter it becomes less effective at radiating. Less energy is lost to radiation on each cycle. So if we want to radiate the same power, we must store more energy. A higher stored energy to energy lost ratio means a *higher Q, and a lower bandwidth*.

## Answer (score 2, by Richard Fry)

The prime reason that antennas electrically small in terms of wave length **also** have useful SWR bandwidths that are relatively small is due to the low value of capacitance of those small antennas to the radiation environment.

That low capacitance results in relatively higher capacitive reactance across their feedpoint terminals, which changes more rapidly for each unit change of operating frequency.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6723/why-does-an-electrically-small-antenna-have-narrow-bandwidth, by bcattle, Phil Frost - W8II, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
