# Understanding coax radiation and "current on the shield"

*Tags: rfi, coaxial-cable, transmission-line, balun · score 8*

## Question

I'm having trouble understanding what seems to be the fundamental principle behind baluns (and probably other related topics).

Perhaps some of my confusion comes from an audio background, where one has "balanced" and "unbalanced" cabling in a way that is easier for me to understand: an unbalanced cable is simply a signal and ground wire, while a *balanced* cable actually has a ground wire and *two* conductors whose voltages are opposite. Balanced cables are used — it is said — so that external interference that raises the voltage across the cable as a whole does not affect the *difference* between the two signal lines. [Although now I'm questioning why just the two wires of an unbalanced cabled can't be measured "differentially" too…]

Now in ham radio lore, it seems a ladder line usually would serve as a balanced transmission line while a coax is unbalanced. But in both there's just two conductors. And in both cases, according to Kirchhoff's current law, the current entering one conductor of either type of line should equal the current exiting the other conductor…right?

Yet I read things like [this](Using%20a%20balun%20with%20a%20resonant%20dipole.md):

you need equal and opposite currents in coax to make it not radiate

And even the wide-spread term:

shield-current-induced noise

(Isn't there always current going through the shield?)

Similarly, in this handbook on RFI, in a section that seems relevant if I could only understand it:

Several cable defects (essentially manufacturing tolerances) certainly can and do convert this "common mode" antenna current to a differential signal (that is, a voltage between the signal conductors), but that is rarely the most powerful coupling mechanism.

(Isn't there also always a voltage between the inner conductor and the coax shield?)

What is it about coax that makes it different than ladder line as far as signal "balance" goes? And what makes coax radiate in some circumstances but not others? It seems the reasons that coax would radiate (namely: current in the shield, or a voltage between the two conductors) are *always* present — whether or not there's a balun or choke, or open or short or perfect load, at the end of it.

## Accepted answer (score 5, by Phil Frost - W8II)

Perhaps some of my confusion comes from an audio background, where one has "balanced" and "unbalanced" cabling in a way that is easier for me to understand: an unbalanced cable is simply a signal and ground wire, while a balanced cable actually has a ground wire and two conductors whose voltages are opposite.

That's not entirely accurate. What makes a balanced audio connection "balanced" is that there are two connections, and each has *equal impedance* (to each other, and the wire's surroundings). It's not about having equal and opposite voltages, or currents. See What makes a “balanced” audio signal?

And that's why simply measuring the two wires of an unbalanced audio cable isn't useful. It's how unbalanced audio equipment works: the shield is ground, and the signal is the difference between ground and some other wire. But since the *impedance* of the wires are not equal, noise picked up from external sources isn't necessarily common-mode, and so isn't rejected by the difference amplifier.

And in both cases, according to Kirchhoff's current law, the current entering one conductor of either type of line should equal the current exiting the other conductor…right?

I think you misunderstand the KCL, which says that the sum of all current entering a node is equal to the sum of all current exiting a node. A "node" is any place wires connect on a schematic. Unless you short the two wires of a transmission line together somewhere (which would make it pretty worthless as a transmission line), they don't necessarily share a common node, so the KCL isn't of much help.

you need equal and opposite currents in coax to make it not radiate

Radio transmissions work by detecting changes in the electromagnetic fields from a distant source. So to radiate, we need to make electromagnetic fields which extend to infinity (though they will necessarily get weaker with distance according to the inverse square law). By reciprocity, we also know that something good at transmitting will be good at receiving.

So conversely, if we can show that the electromagnetic fields don't extend to infinity, then we can't be radiating.

So consider that we have a short section of coax. At this very instant, there is an excess of electrons on the shield:

and an excess of electron holes on the center conductor:

I've drawn electrons as blue, and electron holes as red. And the arrows represent the electric field. If you were a positive electric charge floating about, the arrows point in the direction you'd feel a push. You'd be attracted to the shield, because positive charges are attracted to the negative charge of electrons. And likewise, you are repelled from the center conductor.

As you get farther away, the push you feel becomes less, but it never fully goes away. These fields extend to infinity, so if we can make these electric fields oscillate, we'd probably have a good antenna.

However, there are exactly as many electrons as there are electron holes in this diagram. Consequently, the fields are equal in magnitude: they are just opposite in direction. So if you put the two together:

Now the electric field exists only inside the coax. A floating positive charge outside the coax simultaneously feels a push and a pull that are equal. That is, it doesn't feel anything at all. The field does not extend to infinity: the coax does not radiate (or receive, by reciprocity).

In practice these extra electrons and electron holes are there as a result of the RF current on the transmission line. When the currents are equal and opposite as they are here, we call these *differential-mode currents*.

If the currents weren't exactly equal and opposite, then we can factor out some amount of current that's the difference. We call that *common-mode current*. Since the electric charge associated with this portion of the current isn't cancelled by an equal but opposite amount of charge, the associated fields extend to infinity and the transmission line radiates.

Also by reciprocity, if only common-mode currents radiate, then anything *received* by the transmission line (and not by the antenna at the end) will *also* be common-mode. That may seem odd, but just keep it in mind.

Let's say I divide all the currents on some coax into three components:

- $I_a$ is the current on the center conductor.
- $I_b$ is the portion of current on the shield which is equal and opposite $I_a$. These are the differential-mode currents.
- $I_c$ is whatever current is left over: the common-mode current. It can be of any direction or magnitude, independently of $I_a$ and $I_b$.

Notice that $I_c$, the common-mode current, is on the outside of the shield. There's no provision for a common-mode current on the center conductor, because it can't happen (for RF currents, anyway).

The reason is skin effect. Normally we talk about skin effect as causing the RF current to flow on or near the outer surface of a solid conductor. However, the electric and magnetic fields responsible for skin effect can reach across the dielectric of the coax as well: any common-mode current on the center conductor will create eddy currents that cancel the center conductor's current, replacing it with a current on the shield.

Also, notice that $I_b$, the shield's half of the differential-mode current, is drawn on the inside of the shield. That's because the charges associated with this current are attracted to the opposite charges associated with the current on the center conductor.

And this is how ultimately common-mode noise is rejected in a coax system. When eventually this coax terminates at a receiver, that receiver will be in a metal box. And that metal box functions as an extension of the coax shield. Common-mode currents will continue to flow around the *outside* of the metal box, because of skin effect, and because they don't have an opposite charge on the center conductor to draw them to the inside. So consequently, these common-mode currents can't enter any of the receiver circuitry inside the box.

Of course, all of this is true only to the extent that the shield is a perfectly solid, perfect conductor. Real shields have some resistance, and making flexible coax requires thin foil or a braid, which isn't ideal. That's what the other is talking about when he writes of "shield-current-induced noise".

## Answer (score 2, by Martin Ewing AA6E)

One point to make is that at radio frequencies, the **skin effect** is important. That is, the RF currents are present only on the surfaces of conductors -- actually in a thin layer whose depth (the "skin depth") gets lower as frequency goes up.

So the picture is that an ideal coaxial cable has a current +I on the surface of the inner conductor and a current -I on the **inner** surface of the shield. (at any give location and moment of time) From the **outside** of the coax, you don't see any electric or magnetic fields -- they are contained inside the shield. [Shields aren't perfect, so in reality there is some leakage.]

If the (balanced) antenna is fed with a balun that transforms the impedance correctly, the power is transmitted on the inside of the coax and all is well. The shield (outside) stays at ground potential, and there no outside current flow. But if the antenna or balun is not symmetrical, the current will divide between the inside and the outside of the coax shield. On transmit, this means that your coax is radiating power and distorting the radiation pattern of your antenna and possibly getting into TVs or other equipment in nasty ways. On receive, it means that noise from household appliances, the power line, etc. can couple **into** the coax and make extra noise in your receiver. (Shield leakage has a similar effect.)

Balanced open wire lines or ladder lines have some of the same problems, although the electric and magnetic fields are not confined as nicely as in coax. If the antenna is symmetrical (balanced) and the balanced lines are really balanced (no nearby conductors like drain spouts, for example), the current on one leg is +I and on the other it is -I. This means that the fields cancel out when seen from a good distance (many times the conductor spacing), and there is little if any radiation from the feed line itself. If the antenna or feed line are imbalanced, the feed line will radiate on transmit and noise will be coupled into the feed line on receive. That is the same problem as with coax lines.

The big advantage of balanced lines is low attenuation, so they can operate OK with fairly high SWR. Coax is usually easier to work with, since you can route it as needed without worrying so much about nearby structures, etc. Balanced lines have to be accurately spaced with wire separation a small fraction of a wavelength. Coax is generally used at very high frequencies, because balanced lines with very narrow spacings are hard to construct.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5522/understanding-coax-radiation-and-current-on-the-shield, by natevw - AF7TB, Phil Frost - W8II, Martin Ewing AA6E. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
