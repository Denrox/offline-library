# Why do 9:1 ununs use type 2 material for the core?

*Tags: hf, balun, ferrite, transformer · score 6*

## Question

I do not understand how a 9:1 unun wound on a T200-2 works. I understand the transformer voltage and current ratios. I have wound several toroid chokes and 49:1 ununs and know how they work. What is throwing me is that all designs I see use type 2 material powdered iron, for example, a T200-2 core.

The permeability is so low the 9-turns at 2 MHz produce roughly 12-ohms impedance. 30 MHz is not much better at 180 ohms. I was taught the impedance of the windings at a minimum is 10X the circuit impedance or at least 500 ohms, and greater than 500 is better.

It seems to me if one uses type 2 material would take 100 or more turns to get the impedance high enough. Why not use type 43 or 61 material for the core? Impedance will range from 1 to 15K ohms. What am I overlooking?

## Answer (score 7, by hobbs - KC2G)

I was taught the impedance of the windings at a minimum is 10X the circuit impedance or at least 500 ohms, and greater than 500 is better.

That sounds like a good guideline for an isolation transformer, but as I understand it, an autotransformer can live with poorer magnetic coupling because the primary and secondary windings are partially the *same* winding.

That said, you certainly *can* build a 9:1 on a higher-permeability core, and you *can* use a ferrite like type 43 without too much worry about core loss. Compare these three designs investigated by VK6SYF:

- T200-2 iron core
- Jaycar LO-1238 core (L15 NiZn, somewhere between #43 and #77 in characteristics, and pretty close to FT140 in size)
- FT-140-43 core

The two wound on ferrites require fewer turns and have lower SWR over a wider frequency range. The LO-1238 unun has significantly lower loss than the T200 unun. The FT-140-43 one didn't have its loss measured but we can infer from the overall similarity in design and other parameters to the LO-1238 one that it's also superior to the T200.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22468/why-do-9-1-ununs-use-type-2-material-for-the-core, by hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
