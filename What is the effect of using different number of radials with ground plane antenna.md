# What is the effect of using different number of radials with ground plane antenna

*Tags: antenna, radial · score 14*

## Question

I'm new to electronics and telecommunication at all, I having trouble with understanding the difference between 2, 3 and 4 radials, as I've searched online I've learned that I can use only 1 radial(and it makes sense) but when using 2, 3 or 4 its to supply a counterpoise to the ground(**balance?**).

Other source talked about 2 radials:

The object of the two radials is to produce a canceling signal in the horizontal plane. They do this by being driven together. However, they must radiate a canceling field. That means they must be matched to radiate.

Is the above quote also apply to 4 radials and anyway what is true is it only for **balance** or **canceling** maybe I'm confused and its about both, if anyone can help me make sense from all I will be very thankful.

## Accepted answer (score 20, by Phil Frost - W8II)

An ideal vertical doesn't have radials: it's half a dipole sitting upon a perfectly conductive, infinite plane. Under these idealized conditions, its radiation pattern is identical to a dipole's radiation pattern that's been sliced in half (like a bagel), and the vertical's feedpoint impedance is exactly half that of a dipole.

When the plane under the vertical deviates from this ideal, the effect is generally that radiation at low angles is reduced, and the antenna becomes less efficient due to resistive losses in the ground. This happens if the ground plane isn't very conductive (like dirt), or if it isn't infinitely long.

Here are some simulated results to illustrate, thanks to JSH:

*http://www.hamradio.me/wp-content/uploads/2016/01/40m_MonoPole_SXC.png*

More radials, and longer radials, moves you closer to the ideal. Less radials, or shorter radials, moves you closer to a dummy load. If you have no radials at all then the feedline will be the radial and you end up with something not unlike a dipole (albeit a very oddly shaped one).

With just two radials, then if you view the antenna from one side (perpendicular to the radials), you have a pretty good ground plane to the left and to the right. But if you walk 90 degrees around the antenna so that the radials are coming at you, there are no radials at all to the left and the right, and consequently in those directions you'll get less radiation. Such an antenna isn't perfectly omnidirectional, but it can be good enough. A mag-mount on a balcony railing is essentially this.

Once you have three radials, the pattern is more or less omnidirectional. Of course this is still very far from an ideal, infinite ground plane, but modeling and empirical evidence have shown that if the radials are elevated (to minimize interaction with the ground) and trimmed to resonant lengths, the results are for practical purposes very good.

If your radials are in the ground, then 16 is sufficient to have a good ground plane. The lengths don't matter too much since they will be detuned by the ground anyway. Anything longer than a quarter-wave is good.

## Answer (score 6, by JSH)

### Elevated radials not equal to ground plane

A common misconception is elevated radials (as counterpoise) perform the role of "ground plane" in an antenna system including dominating the far field effects from real ground over which the antenna resides.

Radials perform two roles: a conductive path for the inner shield currents and a method to ensure the radiation from this new path is cancelled in the far field. Your research is correctly touching on these realities, but let's dig further by examining the two roles.

### A conductive path for inner shield currents

Almost everyone knows the RF currents within a coaxial transmission line have two equal and opposite polarity components. The current from the center conductor energizes the monopole... easy enough. The current on the inside of the shield has many more pathways to follow. Notably, the outside of the coax can entice the current to flow depending on what impedance it presents to the antenna feedpoint. If the antenna electrically connects to the mounting structure, it too can entice currents to flow.

Enter a single radial...

A conductor trimmed to 1/4 wavelength at the operating frequency is a form of impedance transformer. Since the free end of the radial is open, it maintains a high impedance by definition. Following the transformer logic, this high impedance transforms to a low impedance at the other end. If we connect this Low Z point to the shield/mounting-structure at the feedpoint, it will provide a low impedance and tend to draw a large proportion of the inner shield current to itself. This radial, thus energized, radiates. We have solved half the problem with monopoles... namely we have reduced the current flow on the outer transmission line and mounting structure by monopolizing the current flow into the radial with its manufactured low impedance at said feedpoint. This logic doesn't necessarily hold true if the outer shield of the feedline or mounting structure also presents a Low Z in parallel with the radials, but let's assume for the moment the radials win the "current" battle. With current flowing upon it, the single radial is free to radiate its energy exactly like the monopole element.

### Canceling far field effects by adding another radial...

If we add a second radial opposite the first, the same action occurs with both receiving the lion's share of current divided equally between them. The symmetric orientation of the two radials is such each both radiate, but because their polarities are opposite each other by way of orientation, the far field summation from both is negligible. It isn't zero, but is so small to be of no consequence so long as the radials are 1/4 wavelength or less.

### Two problems solved

Thus providing two radials, one opposite the other, solves two problems for us: manhandling the shield inner current and ensuring this current doesn't affect the far field of the antenna pattern.

### What tests have to say

Simulation and direct measurement both confirm just two radials of 1/4 wavelength or less result in almost zero perturbation of the monopole far field radiation pattern leaving the monopole element alone in determining the radiation circular symmetry.

Note the induction fields (stored energy fields) of each radial are not balanced in the near-field. Thus it is possible to greatly perturb the far-field balance if one radial is too close to some mounting structure or another conductive object. With each radial containing half the shield current energy, they are each more sensitive to nearby conductors.

### Add more radials

Continuing the theme, adding more radials almost completely eliminates any microscopic deviation from a pure circular far-field pattern. Three or four radial monopole antennas are the most popular configuration.

One interesting consequence of adding still more symmetrical radials to the base of a monopole antenna is raising the capacitance between the radials and monopole. The net effect of this is each radial can now be a bit shorter in length. See "Hats, Number of Spokes, and Capacitance" and "Two Radials are Enough" in the article about the AHVD antenna for more details...

http://www.hamradio.me/antennas/asymmetrical-hatted-dipole-antenna.html

More radials also means if the energy present in one is perturbed by placing a conductor in its induction fields, the net effect is "out voted" by the numerous non-perturbed radials.

### The consequence of radials

One particularly unwanted byproduct of using radials, and one that caught me by surprise when I finally figured it out, is the raising of the elevation angle. I've suggested above that radials contribute little to no effect on the important far-field pattern in azimuth. What about elevation. Measure any classic 1/4 wave ground plane antenna and you will see elevation on the primary lobe. Look at figure 5 in this web page...

http://www.hamradio.me/antennas/slimjim-vs-traditional-j-pole-antenna.html

Note the measurements (not simulations) of two monopoles (one over a metal place, the other with four radials). They both exhibit an upward tilt.

If one simulates the radial monopole with a source right on the feedpoint, but without any mast or feedline component, the far field elevation pattern looks like the classic doughnut shape you get from a standalone dipole, less a bit of gain.

So why the difference.

If you add the feedline outer conductor and/or a mast to the simulation model you wind up tilting the pattern upwards and get agreement with measurements. The problem is the radials induce currents into the mast/feedline, encourage a mast current and thus tilt the elevation pattern.

This fascinating effect is often erroneously credited to the radials somehow "reflecting" the signal upwards just like a metal sheet, but is in fact due to induced energy on the mast/feedline beneath the antenna.

This is easy to confirm in any antenna simulation tool.

### Conclusion

Two or more radials shorter than a 1/4 wavelength and arranged symmetrically produce little to no effect on the circularity of the monopole azimuth far field pattern.

Radials induce energy to the mounting structure and/or feedline generating the typical up-tilt in the elevation far field pattern.

## Answer (score 3, by Richard Fry)

Below are NEC4.2 analyses showing the intrinsic, free space radiation patterns of (1) a ground plane antenna having two pairs of co-linear, λ/4, horizontal radials spaced at ±90°, and (2) a comparison of the free space elevation pattern of the ground plane antenna to that of a λ/2, center-fed dipole.

The λ/2 dipole has about 0.7dB more gain than the λ/4 ground plane, but otherwise their radiation patterns are very similar, and would be similarly affected by the propagation environment (e.g., reflections from the earth and/or other surfaces).

***Graphic 1**Graphic 2***

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3675/what-is-the-effect-of-using-different-number-of-radials-with-ground-plane-ante, by Aviel Fedida, Phil Frost - W8II, JSH, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
