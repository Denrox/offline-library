# Dipole Center Spacing

*Tags: antenna-theory, antenna-construction, dipole · score 5*

## Question

I have a question about dipole construction. I am working with a turnstile, but building dipoles to validate my system with linearly polarized transmission before moving on to circular.

My design has a turnstile deploying from a cubesat, but the elements are spaced apart by the width of the cubesat face (about 4 inches). I'm referring to the center gap, between feedpoints. This is a common design, so I know it's viable. What I want to know is how spacing the elements apart physically affects feedpoint impedance and other characteristics. I haven't been able to find literature on this.

A solid explanation of how this would affect my antenna and/or links to good references would be appreciated.

EDIT:

UHF antenna centered on 433MHz

Copper plated Spring Steel elements

## Accepted answer (score 4, by Kevin Reid AG6YO)

If you model your feed point as being the two points where your antenna meets the body of the satellite, then you have a secondary problem which you will also have to solve: how does the signal pass between your transmitter and those two points? What are the impedances there?

I think you are better off *modeling the satellite's structure as part of the antenna,* as well as whatever internal conductors bring the two antenna elements to a single point where they can be joined to a transmission line (or directly to the transmitter's output port). This is a harder problem, likely answered not generically by theory but with the use of antenna simulation software (and some empirical testing to validate your model), but it is the problem you actually need to solve.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6906/dipole-center-spacing, by Kontakt, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
