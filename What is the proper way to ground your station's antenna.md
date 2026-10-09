# What is the proper way to ground your station's antenna?

*Tags: antenna, propagation, rfi, grounding · score 8*

## Question

I don't understand how you would go about giving an RF ground to your antenna. Would it not become an additional radial and affect the signal?

What is the proper way to ground your station's antenna?

## Accepted answer (score 5, by WPrecht)

To answer your first question, yes, it will affect the signal, but it's a good thing.

What you do to (RF) ground your antenna(s) depends on what type of antenna you are using. For instance, dipoles do not require a ground. Typical vertical antennas do require a graound though some types such as the GAP Challenger use 3 wires insulated from ground (in this application they are referred to as a *counterpoise*).

In a typical vertical antenna installation, your radiator is λ/4 tall (electrically at least, it might be physically shorter through the use of coils or whatever). This is referred to as a monopole and is half of a good antenna. You make the ground be the other half of the antenna but creating a ground plane with radials. This creates a virtual image antenna that completes the overall antenna effect. These radials are usually buried just below the surface or stapled down to the ground and grass is allowed to grow through them to hold them down.

That's your RF ground. In addition, it's usually desirable to have an electrical ground for lightning and static electricity protection. This is achieved by making a lower impedence path to ground than you feedline presents. Usually one or more 8' copper-clad rods are pounded into the ground at the base of the antenna and bound to it. The area of effect of this is *below* the ground plane and doesn't detract from the signal.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/390/what-is-the-proper-way-to-ground-your-station-s-antenna, by David Anastasio, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
