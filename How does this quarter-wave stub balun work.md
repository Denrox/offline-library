# How does this quarter-wave stub balun work?

*Tags: antenna, antenna-theory, balun · score 5*

## Question

I was searching for 1:1 balun designs that would be efficient at VHF yet could easily be made from commonly available materials when I came across these two:

While the design on the right seems pretty straightforward, the workings of the left one are a bit of a mystery to me. A quarter-wave shorted stub will, as far as I understand, look like an open circuit at the resonant frequency, so it seems like it shouldn't have any effect, at least if treated as a perfect transmission line...

So how (if at all) does it function as a balun, and what are the necessary conditions?

- Is it important for the coax from which the stub is made to have the same impedance as the antenna (75 ohms)?
- Is the crossover (i.e. connecting the shield of the stub to the feedline's center conductor and vice versa) important, or will the balun also work without it?
- Does the stub have to be oriented in a particular manner relative to the main feedline in order for it to work?

## Accepted answer (score 2, by Phil Frost - W8II)

I've never seen a balun design like this and and I'm not entirely certain it works. But if it does, here's how I think it could work:

As you say, a shorted quarter-wave stub appears like an open circuit. So the stub is a parallel open circuit to the differential mode: it has no effect.

To the common-mode, the stub and the parallel section of feedline make a quarter-wave transmission line.

Hm, a quarter-wave transmission line at the feedpoint sounds like a sleeve or bazooka balun. These baluns are made from coaxial, not balanced feedlines. And they can be open or short on the feedline end: if they are open, the sleeve radiates. If they are closed, the sleeve does not radiate.

I suspect (though I'm not entirely certain) this is the same idea. If you try to make a sleeve balun that's short on the feedline end and thus does not radiate but with balanced rather than coaxial transmission line, you get a [folded balun](How%20does%20a%20folded%20balun%20work.md). If you make it open on the feedline end, you get this design.

It works because the common-mode sees, from the perspective of the feedpoint, a short (because the transmission line is open 1/4 wavelength away). This ensures the voltage at each leg of the dipole is symmetrical, which is good. But what's making them symmetrical is common-mode current on that 1/4 wave section of balanced transmission line, which is probably not the best since that means the final 1/4 wavelength of the feedline is radiating and that's probably not what you want. There won't be any common-mode currents on the rest of the feedline, at least.

Again, not entirely certain this is correct. But maybe someone can show that I'm right or wrong in the comments.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16981/how-does-this-quarter-wave-stub-balun-work, by Ivan R2AZR, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
