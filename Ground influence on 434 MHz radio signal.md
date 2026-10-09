# Ground influence on 434 MHz radio signal

*Tags: propagation · score 8*

## Question

I have read in a paper that ground acts as reflector for radio signals in 434 MHz band. Why is that the case?

## Answer (score 2, by Phil Frost - W8II)

Radio waves reflect from the ground because the ground is a big, flat surface that's conductive enough. It reflects for the same reason that a mirror reflects light.

For a simplified explanation, let's assume the ground is an infinite, flat, perfectly conductive plane. As a wave approaches the ground, the conductivity of the ground constrains the electric field to 0 (you can't develop a voltage if there's no resistance to work against).

The mechanism is identical to a wave reflecting off a short at the end of a transmission line, except the wave is free to move in all three dimensions.

For illustration, I'm going to borrow an animation from Dan Russel's excellent page on wave reflection:

An analogous system which might be more intuitive is a string incident upon a free boundary, like a massless ring sliding without friction on a rod. The lack of friction or mass is analogous to the lack of resistance or inductance in an electrical material. Dan Russel says it better than I can:

The animation [...] shows a wave train moving toward the right, incident upon a free boundary. A free boundary means that there is no force to limit the displacement. Mathematically, this results in the string having zero slope at the boundary.

This limit means the wave can't penetrate the material, nor can the material absorb the wave. The energy must go somewhere, and the only solution given these constraints is reflection.

Now, this shows a wave orthogonal to a plane, reflecting back in the same direction from which it came, forming a standing wave. But if the wave is at an oblique angle (as is more usually the case with radio waves and the ground), then we can think of the wave as separate and independent horizontal and vertical components. Only the vertical component is reflected, because it is perpendicular to the ground. The horizontal component continues unchanged. Just like an ordinary mirror, which works the same way, but at a much higher frequency.

And of course, the ground isn't perfectly conductive, so some fraction of the radio wave will be absorbed. And the ground is also not perfectly flat, so the reflection is distorted to some degree.

Still, it's reflective enough at most radio frequencies to significantly alter propagation. See for example the two-ray ground reflection model and image antennas.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2356/ground-influence-on-434-mhz-radio-signal, by Nexy_sm, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
