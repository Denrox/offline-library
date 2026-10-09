# RF Antenna - V pole - Should one leg go to ground and the other to signal?

*Tags: antenna, antenna-construction · score 5*

## Question

I'm attempting to follow this white paper in order to build an antenna. This is my first antenna and as such I have a rather simple question.

DIY 137 MHz APT Weather satellite antenna by Adam-9A4QV

https://www.youtube.com/watch?v=9WNmhfpWxdk

Should one of these legs go to ground and the other to signal from the coaxial cable? It's unclear to me from the diagram:

Whether or not the terminal block is conductive through the center horizontal plane. IE is the top and bottom legs of the antenna separated and thus one goes to signal and one to ground or are they connected in which case they both are connected to both (which I admit makes no sense)?

## Accepted answer (score 7, by Kevin Reid AG6YO)

One leg of the antenna goes to the center conductor and the other leg of the antenna goes to the braided shield of the coaxial cable. The terminal block is just a way to make the connections, and it has two electrically separate positions. You can use any means of making the connection you have handy, as long as it is small compared to the wavelength.

(Vocabulary tip: the junction between the cable (*feed line*) and the antenna is called the *feed point*.)

However, it's worth noting that this is a poor design. Specifically, it has no *balun* — a device for converting between a *balanced* device (the antenna, which as you can see is symmetric) and an *unbalanced* one (the coaxial cable, which has an inside and outside conductor that are very different). This means that the shield of the coaxial cable will act as part of the antenna, and the performance will vary depending on how the cable is routed. It may pick up common-mode noise traveling from your receiving equipment along the cable, which can be a consideration when trying to receive weak signals from sources such as satellites.

You can read more about what a balun is and how it works in this application in the question [Using a balun with a resonant dipole](Using%20a%20balun%20with%20a%20resonant%20dipole.md).

## Answer (score 3, by Richard Fry)

It doesn't matter which wire is connected to which side of the V-dipole, as they both carry the same signal information (just 180 degrees out of phase with each other).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12244/rf-antenna-v-pole-should-one-leg-go-to-ground-and-the-other-to-signal, by Cody Smith, Kevin Reid AG6YO, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
