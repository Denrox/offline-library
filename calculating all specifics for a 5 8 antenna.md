# calculating all specifics for a 5/8 antenna

*Tags: antenna, vertical-antenna · score 8*

## Question

So, I've built a couple 1/4λ ground plane antennas for Airband and Marine band.

I don't transmit, I'm just listening, etc.

So, constructing ground plane antennas with the radials and getting the impedance to be 50Ω is rather easy, not so for the 5/8λ it would seem.

I couldn't find decent formulas or calculations to calculate the coil at the foot of the vertical element.

The radials are supposed to be 1/4λ, while the vertical active element should be 5/8λ, with a velocity factor of 0.98. However, when measuring the vertical antenna element: should the 5/8λ length be measured from the top of the coil up to the top of the element, or including the coil?

And how to determine the diameter, the number of windings, and the flare-ing (how tightly the coil should be wound) for the coil? I only found dodgy formulas and tables for 20m and other bands like that, but they never depend on the frequency or wavelength, they just use a couple constants out of nowhere.

I'd like to calculate the dimensions myself by using the actual formulas, that depend on the frequency or wavelength, etc. if that makes sense.

## Accepted answer (score 7, by Glenn W9IQ)

I congratulate you on your interest in working out the design issues from the ground up. Understanding the theoretical and comparing this to the field results is the beginning of a life long enjoyment of antenna experimentation.

**The Antenna**

By way of background, a 5/8 wave antenna is the [highest directivity, single element, linear antenna that you can construct](What%20makes%20a%205%208%20wavelength%20vertical%20desirable.md). But the construction details are important in order to efficiently convert directivity into gain. Paying attention to the effect of the ground plane, using the right materials and matching the impedance of the antenna to the impedance of the coax and the coax impedance to the receiver impedance can all play a role in wringing out the last drop of gain from the antenna.

The 5/8 wave antenna is a non-resonant antenna. This means that when perfectly constructed, it will have an impedance that is made up of a real part and an imaginary part. Generally the imaginary part will be capacitive and the real part will not match 50 ohms.

**Steps**

Here are the steps that I would follow in planning a 5/8 wave antenna:

1.) Model the antenna to maximize the gain and calculate the complex impedance.

2.) Engineer a matching network to convert the complex impedance of the antenna to the characteristic impedance of the coax.

3.) Construct and contrast field results with the models. Tweak as needed.

Way back when I was an engineering student, we did all of these calculations in long form (OK, not a slide rule but with a calculator and graphing paper). Today it is much more efficient to use modeling tools and then compare these results with some manual calculations if desired.

**Modeling the Antenna**

There is a free antenna modeling program called EZNEC that can be used to model your antenna. Other than consulting tables in text books, this is the only practical way of estimating the gain and feedpoint impedance of your antenna.

You can adjust parameters such as element lengths, type of material, gauge of material, frequency, height above ground, etc. within the model to see how these parameters affect the results.

If you are looking for a good reference book on antenna theory and construction, I recommend the ARRL Antenna Book. If you are more interested in the pure theory and mathematics associated with antennas, the seminal text is Antennas by John D Kraus.

**Designing a Matching Network**

There are several web sites and stand alone tools that can calculate the matching network. My favorite site is Le Leivre. With this tool you can enter the complex input and output impedances and it will show all possible L type matching networks that will do the job along with the correct component values.

If you wish to wind your own inductor for the matching network, the approximate formula for a single layer, air wound inductor is:

$$L=\frac{(n^2*d^2)}{(18*d+40*l)} \tag 1$$

where L is the inductance in microhenries, d is the coil diameter in inches, l is the coil length in inches, and n is the number of turns.

You can expand or contract the length of the coil a bit to fine tune the inductance.

This formula is the Wheeler formula for English units that was empirically derived in the early 1900's. Since it is an empirical formula, the effect of $\mu_o$ and $\mu_r$ is factored within the constants. The above version of the formula is generally valid when the diameter of the coil is much larger than the diameter of the wire and where the spacing between turns is minimal.

More than 50 years later, Wheeler and others used computer modeling to derive a much more precise formula:

$$L=0.0002\pi D_kN^2*\ln{(1+\frac{\pi}{2k})}+\left(2.3004+3437k+1.7636k^2-\frac{0.047}{(0.755+\frac{1}{k})^{1.44}}\right)^{-1} \tag 2$$

where Dk is the coil diameter in mm, N is the number of turns and k is the ratio of the winding diameter to length.

## Answer (score 3, by Phil Frost - W8II)

[The impedance of a 5/8 monopole is around (75−425j)Ω](What%20is%20the%20impedance%20of%20a%201.25%20%CE%BB%20dipole%20antenna.md), although it's sensitive to the diameter of the element(s), size of the ground plane, etc. You won't find formulas because it's the sort of thing that's easier to get approximately correct and then adjust empirically.

Modelling your antenna first will yield a better approximation of the impedance, and allow optimization of other parameters. You'll still need to tweak it at the end.

(75−425j)Ω isn't a great match to a 50Ω system, so you will need some kind of matching network. Generally, the solution is to add a series inductance of 425jΩ which cancels the reactance, leaving a 75Ω feed impedance which is close enough.

Reactance and inductance are related by frequency:

$$ X_{L}=2\pi fL$$

Having determined the necessary inductance, the inductor can be designed with any number of online calculators, or this formula:

$$ L= {n^2 d^2 \over 18d+40l} $$

As Glenn W9IQ explains, this is an empirical formula so the constants don't have any deeper meaning. $d$ and $l$ are the diameter and length in inches, and $n$ is the number of turns. Generally aiming for the diameter and length to be approximately equal is a good starting point.

Also strive to use a sufficiently thick conductor that losses are low, otherwise the inductor losses will more than offset the improvement in directivity.

However, when measuring the vertical antenna element: should the 5/8λ length be measured from the top of the coil up to the top of the element, or including the coil?

For a theoretical construction, the matching inductor has zero size and so it doesn't matter. In practice the inductor should still be small so it should not matter much. Consider it just one of many variables that will require empirical adjustment.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9780/calculating-all-specifics-for-a-5-8-antenna, by polemon, Glenn W9IQ, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
