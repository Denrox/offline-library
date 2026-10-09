# When and why does the size of a ground plane or radials matter?

*Tags: antenna-theory, mobile, vertical-antenna, radial, counterpoise · score 9*

## Question

Consider these three cases:

1.

My understanding is that when building or installing an antenna designed to operate over a ground plane (e.g. a quarter-wave vertical), the size of the ground plane does not matter (e.g. the earth, possibly coupled using additional radial wires, or a car roof of unspecified size), provided that it is sufficiently large compared to the wavelength. This is commonly described as the ground plane acting as a reflector, so that there is effectively a second quarter-wave element “below the ground plane”. If this analogy is accurate, then obviously the larger the better.

2.

Designs involving self-supporting radials, flat or downward-sloping, may use a specific length of radials.

3.

A vertical resonant center-fed dipole must have a quarter-wave lower element — having the same symmetry as case 1 but physically instantiated.

On the continuum of antenna designs between a ground plane antenna and a coaxial vertical dipole, why is it that sometimes there is a well-defined optimum size of the ground plane, or rather the antenna element which is not pointing upward, whereas sometimes it doesn't seem to matter much?

*This question is not about the size of ground-level radial networks*, but about comparing designs which have “at least this big” ground planes such as a car roof or the Earth augmented with wires, with free-standing designs which have specific lengths of conductors.

## Accepted answer (score 7, by Phil Frost - W8II)

Perhaps consider that the objective of the ground plane is to present a low impedance. At the feedpoint, the hope is to have all the current go into the antenna, and none of it on the coax common-mode. The lower the impedance of the ground plane, the less current will be on the coax common-mode due to its relatively high impedance.

If the ground plane impedance is not very much lower than the coax common-mode, then there will be significant common-mode current, and what you have built is not the dipole or the vertical or whatever you were trying to build, but something else.

An infinite ground plane would be nice, but "as big as possible" will do. Current decreases with distance from the feedpoint, so at far distances the current is negligible, so it doesn't matter much what the situation with the ground plane (or lack thereof) is.

A car roof and a UHF antenna fit this model well. A roof 1.6 meters square is sufficient for a 440 MHz antenna to have about 1.14 wavelengths in any direction. At this size, the impact of the car geometry on the antenna may be detectable if carefully measured, but unlikely to be of any practical significance.

If the idea is to make the ground plane as small as possible, an electrical quarter wavelength radius is a good length. Consider a quarter-wave transformer: looking at an open through a 1/4 wave transmission line, the open is transformed into a short. The same concept applies to radials: imagine a radial and the monopole as a piece of twin-lead that have been pulled apart at one end to make an L.

This quarter-wavelength size is especially critical in elevated monopoles, that is those without radials buried in soil. Consider, soil can be used as an OK ground plane, although resistive losses make it inefficient. If the radials have minor deficiencies the soil can make up for them without much negative impact. However, air doesn't work as a ground plane at all. If the radials are deficient, then where will that current go? The feedline common-mode? The tower? Either may end up radiating fine, but such an arrangement strictly speaking isn't a monopole.

(Very long elevated radials would work as well, though would not be very practical.)

A vertical resonant center-fed dipole must have a quarter-wave lower element — having the same symmetry as case 1 but physically instantiated.

If the lower element isn't symmetrical, then it isn't a center-fed dipole anymore, by definition. But [off-center fed dipoles](How%20does%20moving%20a%20feedpoint%20off-center%20in%20a%20dipole%20affect%20the%20resonant%20frequency%20and%20resistive%20load.md) can work just fine. A center-fed dipole is balanced, and can be ideally fed with a balanced feedline with no need for a choke or balun. Feeding the dipole off center unbalances it, which would require a feedline unbalanced by the same ratio, or a choke.

However, in many vertical dipole designs, the feedline is concentric with the antenna, and half of the dipole is a radiating sleeve balun. The sleeve balun works by presenting a low impedance from the perspective of the feedpoint, and a high impedance from the perspective to the feedline. It must be an electrical quarter-wave to work, so again the length is critical. At a different length it may still make a fine radiating structure, but it would no longer intrinsically be a balun so the issue of isolating the feedline would need to be solved some other way.

## Answer (score 2, by SDsolar)

In broadcast AM radio it is standard practice to use quarter-wave towers (because half-wave towers are expensive and more of a maintenance headache). These towers require a ground plane to reflect the signal in such a way that it virtually provides an image of the rest of the half-wave that allows for lowest voltage and highest current at the feedpoint. (That's the how and why)

Radials are set 3 degrees apart, so there are 120 of them. Ideally it will be on nice conductive soil, and they are buried just deep enough for good coupling and also so lawn mowers can pass over without causing damage.

The radials are cut to a quarter wavelength plus 5%. It turns out that having the highest conductivity (the wires) provides the best match when it is at resonance. (Every station has a matching network, also). This is in order to provide the image necessary for lowest voltage and highest current at the feedpoint that you would find in a center-fed half-wave antenna.

As they couple more loosely into the ground the actual effective ground plane is much larger than the wires, which helps for ground-wave propagation. Soils vary in their conductivity, so the predictability of providing the resonant wires is the most important factor in impedance matching.

Ground planes are a maintenance issue, and the way they are soldered really matters. Corrosion gets to them and in order to pass my inspections (I did the VIP - the voluntary inspection program that prevents FCC surprise inspections - my reports went into the files at the stations and not to the FCC, and they liked me because I came with a toolbox to fix any deficiencies right then and there). I always wanted to see good solid ground connections at the antenna base, in particular. I always liked it when stations had a good wide low-resistance copper strap at the tower base, so even if some wires get damaged the rest would carry the freight.

Hustler has some excellent references for what they sggest for their 5BTV antennas, and they are similar except that no amateur is going to put out 120 wires. In fact, you can get quite a good ground plane with many fewer wires than that. My personal recommendation is for about 20-40 wires, and of course there are a lot of obstacles in the way of a typical ham vertical antenna installation.

Installation on a rooftop requires the creation of an artificial ground - a counterpoise. It should be tied to earth ground at the transmitter. I have designs for Part 15 LPAM stations that can reach out over a mile with a decent counterpoise of 20 wires. Those must by physical necessity be less than a quarter wavelength; the vertical element is limited by regulation to 10 feet from the ground. (I recommend the Procaster transmitter for this, which is FCC Type-accepted and includes an internal tuner, a bolted-on 9 foot antenna and a 1-foot grounding cable so it can be mounted above the counterpoise.)

Downsloped grounds for vertical antennas can work at about the same length as flat ones, a quarter wavelength plus 5%. Bandwidth is an issue for verticals that must cover an entire band like from 144-148 MHz, so you want the parts to be cut for the middle of the band range you intend to use it for in order to achieve the flattest SWR over the entire range of frequencies. NOAA weather radio antennas should be cut for 162.5 MHz.

So is bigger always better? It depends on your wavelength. VHF signals have little to no ground-wave propagation mode, and the sloped radials help launch the signals skyward. The vertical component holds the launch angle down, of course.

Performance varies slightly between coaxial dipoles and sloped-radial antennas, but not as much as you might think. Similar at UHF.

Beyond that (or even starting at 70CM) you will want to leave omni antennas behind as much as possible. Just ask any police department what their experience was when they shifted from VHF to UHF and they'll tell you it was better before.

Portable radios work best when they have 5/8 wave antennas so they have no need for a ground plane. Quarter-wave antennas in HTs operate under the assumption that the radio body will capacitatively couple to your body to provide a (lossy, loosely-coupled, irregularly-shaped) ground that can reflect the other quarter-wave that is missing from them (the so-called reflected image).

Impedance is a whole different topic, and involves more than just the feedpoint of the antenna, and it runs the gamut, including matching networks in the transmitter or radio shack, feedlines, etc. Magnetrons in microwave ovens come with an integral radiating element which matches the insides of the tube to the waveguide directly. Only the guys in the lab coats would be able to explain impedance in that situation. I will have to defer to others to give the math for all that.

To summarize the question about when ground plane size starts to matter: It always does. Even in a waveguide at 10.5 GHz. Resonance is always best. Compromises are made in the real world, and they all can be made to work to varying degrees. Bigger is not always better.

Impedance matching and resonance is king.

Matching impedance at the antenna is definitely better than matching it at the transmitter unless you want to cut your feed lines to be an odd multiple of a half wave.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7642/when-and-why-does-the-size-of-a-ground-plane-or-radials-matter, by Kevin Reid AG6YO, Phil Frost - W8II, SDsolar. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
