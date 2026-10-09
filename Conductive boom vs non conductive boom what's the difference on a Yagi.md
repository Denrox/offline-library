# Conductive boom vs non conductive boom: what's the difference on a Yagi?

*Tags: antenna, antenna-theory, yagi · score 13*

## Question

I designed a Yagi antenna using 4nec2, assuming that I would use a non conductive boom.

If I use an aluminum boom but I insulate the elements from the boom, can I keep the same design? How does it affect performance, in particular SWR?

It is a 2m (144-148mhz) designed to be a portable VHF / UHF (not mounted on a mast).

## Accepted answer (score 11, by Marcus Müller)

So, by design, the elements of any Yagi have a zero current going through the center point. That's pretty obvious be symmetry: assuming you excite the "left and right" halves of the driving dipole with exactly opposing voltages, everything should be symmetrical across the plane through the middle of that dipole.

Hence, if you approach that plane from left and right, you should see the same voltage, at any time. If two points have exactly the same potential, no current will flow. That's why Yagis work even if their elements are non-perfectly isolated from a metal boom.

The boom correction factor is really just the effect of having a metal object of non-zero left/right dimension in the way of your EM field – that will basically "swallow" a bit of E-field, but that effect should be relatively small for reasonably sized booms.

SWR will practically not be affected; the couple of millimeters you'd have to add to the driving dipole to compensate for a conductive boom are, from a matching perspective equivalent to using the antenna with a couple 0.001 mismatched cables – you'll be hardly pressed to find a matching circuit that is good enough to make the effect even measurable. Also, remember, you're not going to use that antenna for a CW of **exactly** the maximum efficiency frequency of that Yagi, but a couple of MHz around; now, "±1.5MHz around the optimal frequency" means your wavelength-to-antenna element ratio is off by around an easy percent, anyway – it's really no use to over-optimize your antenna here.

Things like non-perfect impedance, dielectric and ohmic losses, geometry imperfection, non-ideal free space impedance (funny fact: air moisture *does* change the $\epsilon_r$ of air) will probably outshadow this.

## Answer (score 3, by brian)

Without all the technical banter take a look at G0KSC site on Yagi design. Justin explains it quite well... The bottom line is when using a non conductive boom or simply isolating the element's from a conductive boom the Yagi becomes much much quieter as far as the signal to noise floor goes. A matter of hearing the someone or not?? My conclusion from building many different Yagi's for vhf/uhf/hf.... is I agree..

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6014/conductive-boom-vs-non-conductive-boom-what-s-the-difference-on-a-yagi, by GmodCake, Marcus Müller, brian. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
