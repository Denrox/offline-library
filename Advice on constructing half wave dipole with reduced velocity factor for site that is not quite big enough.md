# Advice on constructing half wave dipole with reduced velocity factor for site that is not quite big enough?

*Tags: antenna, antenna-construction, dipole · score 3*

## Question

I want to construct an antenna competent on the 160m band, but I haven't got quite enough space, here's my thinking, please let me know if/what you agree/disagree with.

I have a plot of land with three sides closed totaling 56.5 metres. At a typical velocity factor I'd need a little under 80m, maybe 77m, so I found this article:

https://www.hamuniverse.com/10metercoaxdipole.html

The author claims to have constructed a dipole with cheap coax at a velocity factor of .66, making the antenna 53m long, which I can fit, and other references cite lower velocity factors for RG85 coax as low as .535, so there might be a lottery as to whether you get the RG85 A/B/C variant, and I might have to do some trimming on the antenna to find the correct resonance if the Amazon listing says RG58 but means RG58B for example, but if the velocity factory is <~ .66 I'm good for length, though I might have to turn an end at 90 degrees for a few metres worst case.

If you inspect the link above, it shows the feed point in the centre connected only to the coax centre conductor, and the outer ends shorted together, the author claims to have QSOs from Brazil to Italy and Bulgaria on his first night.

I've given up on quarter wave end fed because the grounding system I would need is too much trouble, and 1/2 wave dipole doesn't need grounding, also the QWEF would need to be 40m above ground which I can't do... am I correct in saying that the dipole I propose could be 5-10 metres above ground varying along its length without much problem?

How difficult would it be to fashion or buy traps to install in the antenna to make it comprehensively multiband?

## Answer (score 4, by tomnexus)

Velocity factor is something that applies inside the coax, where the fields are all inside the dielectric medium. Antennas in the air are not subject to "velocity factor".

A plastic coating on an antenna does load it a bit, and reduce its length, but this is mostly relevant at much higher frequencies. For example in printed circuit antennas at 2.4 GHz, where the PCB is a relevant fraction of a wavelength, the shortening effect can be 10 or 15%. Also if you get a build-up of ice on UHF yagi antennas, maybe even VHF, they can be detuned enough to stop working. At 160 metres, a realistic thickness of plastic will make no significant difference to the resonant frequency.

The dipole on the website is described badly. It may work, by using the coax to do two things - 1) as the antenna itself and 2) as a short-circuit stub which provides an inductive load at the open end, near the feedpoint. Now coax is not a good antenna material, it's heavy, high wind resistance, not very strong and will be damaged by water if it gets the slightest cut in the jacket. And inductors are best made with coils of wire, but a stub will work and may have advantages on other bands. You might choose to coil it up so the weight is at the centre, and extend the antenna with strong thin wire. Finally it has no balun. So I don't recommend this design.

To suggest some things for 160 m in a limited space:


Loading, in the form of inductors, will shorten any antenna. It doesn't make a short antenna more efficient, but that's just the deal at 160 m. You could reduce the antenna size to about half of full size before this becomes impractical.


Monopole-type antennas are half the size of dipoles, so consider a "long wire" or "inverted L" or similar, fed against a ground stake or mesh. Full length would be 40 metres of wire but with an inductor at the feed, 20-30 metres would be enough. Depending on your ground, you will also need some further matching, either your ATU or a parallel capacitor and some tuning of the inductor.


Height above ground is not a hard rule. At 160 it's impractical to be half a wavelength high anyway, so work with what you have.


If you make a dipole, you should include a balun, otherwise the coax will radiate (which doesn't matter) and you will have RF in your shack, affecting your computers and other things. A monopole doesn't have a balun but depends on a good ground.

## Answer (score 2, by hobbs - KC2G)

This technique basically works, in that you can get a resonant antenna at a shorter length than you would with plain wire. It's a form of linear loading.

But, it's a worse (lower efficiency) antenna than the one you would get if you simply made a dipole out of the same length of wire and added loading coils to bring it into resonance. You can find calculators to help with coil-loaded dipoles, but the best thing is to build and test. On 160m you can tolerate a low SRF (down to around 4MHz) which means that the optimum arrangement is a couple of really big coils about 80% of the way from the center, with 20% of wire beyond them, but if that's mechanically impractical you can use smaller coils closer to the center, at a bit of a cost in efficiency

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22184/advice-on-constructing-half-wave-dipole-with-reduced-velocity-factor-for-site-, by spl, tomnexus, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
