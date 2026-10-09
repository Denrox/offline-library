# Minimum thickness of whip antenna

*Tags: antenna, antenna-construction, wire-antenna, antenna-theory · score 5*

## Question

I'm looking at designing a communication system using very low power transmitter (0.1 W) and operating in the 400 Mhz range. For my uses I think a quarter wave whip antenna would work well, so I've calculated the length of the antenna to be 187.5 mm.

So far so good (I hope). Now I'm looking at how light I can make this antenna. My understanding is that an antenna of this sort is essentially just a bit of wire of the appropriate length (187.5 mm), but I can't figure out if there's a minimum thickness of the wire. The only limitation I can think of is a thinner wire has higher resistance and hence will heat more quickly (causing more noise). Is this really the limitation? I've never seen a very thin whip antenna and I fear there may be a reason behind this.

## Accepted answer (score 3, by Phil Frost - W8II)

At such a low power, durability is probably more of a concern than anything else. A few simplifying assumptions and quick calculations will demonstrate this.

The impedance of a quarter-wave whip is highest at the tip and lowest at the base. That is to say, the current is lowest at the tip, and highest at the base. So if we can demonstrate that the wire gauge is sufficient at the base, where current is highest, then it should be sufficient for the rest of the antenna, also.

Given your transmit power:

$$ P = 0.1\:\mathrm W $$

And the impedance of a quarter-wave vertical at its base:

$$ R = 36\:\Omega $$

And Joule's first law:

$$ P = I^2 R $$

We can solve this system of equations for $I$ and figure out what the current at the antenna base must be:

$$ 0.1\:\mathrm W = I^2 \cdot 36\:\Omega $$

$$ \frac{0.1\:\mathrm W}{36\:\Omega} = I^2 $$

$$ \sqrt{\frac{0.1\:\mathrm W}{36\:\Omega}} = I $$

$$ 0.053\:\mathrm A = I $$

So the question is now how small a wire can you use to carry (at maximum) 53 mA. You can look at a wire gauge chart and see the answer is "pretty damn small", especially considering we calculated the current at the maximum and it is less everywhere else in the wire.

There's another way you might approach the problem: you can calculate (again referencing a wire gauge chart) the resistance of some proposed wire. Then compare that resistance to the $36\:\Omega$ radiation resistance of a whip to get an estimation antenna efficiency:

$$ \text{antenna efficiency} = \frac{36\:\Omega}{36\:\Omega + \text{resistance of wire}} $$

I say estimation, because to properly apply this formula you must transform all the impedances to the impedance they would have at the feedpoint, but remember since the impedance is at a minimum at the feedpoint, were you to go through the trouble of doing that you would end up with a smaller resistance and a higher efficiency.

And so you can look at this and see that even if your wire has a $1\:\Omega$ resistance, you still have at least a 97% efficient antenna. And a wire that's a quarter-wave long at 440 MHz and has a resistance of 1 ohm is a really thin wire.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5404/minimum-thickness-of-whip-antenna, by FraserOfSmeg, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
