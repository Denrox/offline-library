# How does the antenna noise temperature vary with antenna elevation?

*Tags: antenna, uhf, noise · score 3*

## Question

I'm using a 14 element cross Yagi antenna in my system. For my link budget calculations, what antenna noise temperature should I consider? How does this vary with elevation?

## Answer (score 2, by tomnexus)

It's expected that the total noise temperature to vary with elevation.

Three major effects to consider:

- Sidelobe pickup of noise from the ground, this is the dominant effect
- Variation of atmospheric loss at different elevations, not really relevant for UHF frequencies
- The sky temperature itself, which varies mainly depending on whether you're on or off the galaxy. This sets a minimum for your system noise.

Here's a graph from Phil Perillat of Arecibo, about a 12 m dish.  
  
The sidelobes of a yagi will look quite different so the curve will be different, but it'll probably have a minimum when you're pointing straight up, and be nearly 300K when you're pointing at the horizon. When taking these curves, you need to be careful you don't cross the plane of the galaxy.

Here's a map of the sky temperature at [UHF from Lambda/gsfc:

They say "*Log scale from 10 to 250 K*" so it's safe to assume you could have from as little as no significant contribution from the sky, to a completely dominant contribution, depending on where you point your antenna.

QST has a whole long article about sky noise at 433 MHz. Read it here

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6773/how-does-the-antenna-noise-temperature-vary-with-antenna-elevation, by heisenburg007, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
