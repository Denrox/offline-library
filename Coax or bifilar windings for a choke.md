# Coax or bifilar windings for a choke?

*Tags: impedance, balun, choke-balun · score 6*

## Question

Making a common mode choke out of bifilar windings has proven rather difficult. For me the difficulty lies in getting the impedance to remain a constant 50 ohms from on the HF bands. I've tried 14 gauge enameled and I've tried 18 gauge PTFE. The wires seem very sensitive to any kind of change in position.

I've been modeling the choke after the one shown on this tutorial. Also what's the deal with that design? It's like someone took a 4:1 guanella and just cut the connection that makes it 4:1. Turning it into to parallel 1:1 chokes.

Is there any disadvantage to simply using coax windings instead of bifilar? Can I just wrap 11 or 12 turns of RG-316 around a toroid? How much more choking impedance do you get from a bifilar choke?

The application here primarily on the 40m band. I was looking to build a simple in-line choke (SO-239 on both ends) as well as choke "balun" (SO-239 on one end and balanced terminals on the other). I was also entertaining the idea of a choke "unun" for use with an elevated quarter wave vertical. I would have a top lug connected to the center conductor; the shield would split off to two side lugs.

## Accepted answer (score 7, by Glenn W9IQ)

In most multi-band balun applications, there is rarely a need to maintain a perfect 50 ohm impedance within the balun. The feedpoint or input impedance is varying widely so another impedance bump in the mix typically has no detrimental effect.

I highly recommend the use of coaxial wound over bifilar style for a 1:1 balun. Comparatively, the coaxial and bifilar design can be made to have equivalent common mode choking.

The bifilar style will couple some of the energy traveling on the parallel lines into the core - much like getting a parallel transmission line too close to metal objects. This creates an unnecessary loss and it promotes heating of the core due to the complex permeability of the core material.

It is also very difficult to fabricate a true bifilar 50 ohm line. The design is so touchy that even minor changes in the wire coating thickness or failure to keep the lines adjacent will cause impedance discontinuities. Due to this marginal construction, the voltage withstand rating of this type of transmission line is much lower than what can be attained through the application of a coaxial transmission line.

The coaxial wound style will keep all but the common mode current from creating a flux in the core. This is the ideal behavior of a transmission line transformer of this type. Do estimate the losses in this length of transmission line in order to project the effect on core heating. If heating of the core due to coax loss is a design constraint, consider using higher impedance coaxial cable (e.g. 75 ohm) as this will reduce the loss compared to the same size/class of 50 ohm cable.

Selection of the correct core material is essential. Generally, type 31 is suitable for the lower HF bands and type 43 for the upper HF bands. Look at the complex permeability curves and use a material where the $\mu$''s is greater than $\mu$'s for the frequencies of interest.

You may find some practical information regarding the number of turns of coax vs the core material on the G3TXQ (now an SK) site. Here are some examples of his analysis:

The K9YC 2018 Cookbook also features type 31 material balun designs.

## Answer (score 4, by Cecil - W5DXP)

The advantage of using coax for a 1:1 choke-balun is the constant Z0 of 50 ohms. As can be seen in the following graphs, the only time a 1:1 choke-balun accomplishes a 1:1 transformation is when it sees 50 ohms at its output. Any other impedance at the output causes an impedance transformation because the SWR is not 1:1.

## Answer (score 2, by Brian K1LI)

I strongly recommend "Building and Using Baluns and Ununs" by Jerry Sevick, W2FMI. I have built dozens of coaxial- and bifilar-wound transformers and chokes for use in high-power amplifiers and antenna systems based on the easy-to-understand information in this book. Specific mention is made of how to make reproducible bifilar-wound units over a wide range of impedance levels. They differ in important ways from the units shown in the "splash screen" of the video you cite.

It's certainly easier to use coax to build a 1:1 choke for use in a coax-based system. Rather than adding separate units to choke currents on the shield, I find it cheaper and more convenient to wind as many turns of the feedline as possible through stacks of "large" diameter ferrite toroids. This also avoids the possibility of water-intrusion and other failures that can occur at the coax-coax joints needed to insert separate units. K9AY describes this configuration in, "Ham's Guide to RFI, Ferrites, Baluns, and Audio Interfacing."

In the category of "better is the enemy of good enough," it's important to understand the problem you're trying to solve. While operating recently in a DX location, I had to make do with a heavily compromised antenna installation. Observing unstable SWR readings and watching the mouse wander all over the screen of my laptop when transmitting, I surmised that RF was traveling down the outside of the coax shield. Simply winding a few turns of the coax feedline into a coil lying on the ground solved the problem.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13005/coax-or-bifilar-windings-for-a-choke, by Paul, Glenn W9IQ, Cecil - W5DXP, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
