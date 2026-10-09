# How to make an inductor?

*Tags: receiver, fm, inductor · score 4*

## Question

I am a high school student and am making a project on FM receiver for class 11. I am following this circuit diagram:

The L2 in this diagram is a 22µH RF Choke. The part listed in the website has the configuration provided below in its datasheet.

```
L= 22uH +/-5%
Q= 51
Test Freq.= 2.5 MHz
SRF= 13
DCR Max.=2.28 Ohm
I, DC= 229 mA
Dim. A Max.= 0.16 inch
Dim. B +/-0.03= 0.25 inch
Core Material= iron

```

I know how to make inductors but some properties such as the thickness of the copper wire (in SWG), whether enameled or not, no. of turns to use and the diameter and length of the inductor is confusing me.

And as an additional note can u please mention the number of turns in the L1 and the thickness of the copper wire to be used that will be suitable for the circuit diagram.

## Accepted answer (score 1, by AndrejaKo)

First thing first: Whenever you make an inductor, wire must be insulated for the working voltage of the circuit or higher. Otherwise, you get shorted turns and your inductor turns into jut normal conductor.

Next, since you're high-school student, my advice would be to just use one of the calculators for coil inductance and get the results from there. One I used to use is here. Most of the calculators I've seen work a bit backwards from what you need: You give them physical properties of your coil, and they give you back inductance. Here is one that will let you enter inductance and will give you number of turns needed.

In general, it's the best to just buy the recommended part, but I fully understand that it may be difficult or impossible to source that component in reasonable amount, in reasonable time-frame and for reasonable price. Therefore, some experimentation may be needed if you must manufacture the part by yourself.

In general, the math behind the calculators is quite complex, so I do not consider it reasonable to calculate all properties of an inductor by hand. Still, there's this formula sheet at Wikipedia that has some useable formulas for inductance calculations. It can be very useful for tweaking the input parameters of calculators.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2299/how-to-make-an-inductor, by Aniruddha Sarkar, AndrejaKo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
