# Handheld Dipoles

*Tags: antenna, grounding · score 13*

## Question

A problem with handheld devices is poor grounding. I read from [someone else's question](What%20is%20the%20proper%20way%20to%20ground%20your%20station%27s%20antenna.md) that dipoles don't need a ground. Why don't they make little handhelds with two antennas instead of one, or a little T antenna, which has extendable arms?

```
_ _  Little dipole arms, which can extend out, and collapse for portability
|
HT

```

## Answer (score 8, by Phil Frost - W8II)

A dipole is twice as long as the equivalent monopole. However if the size of a dipole isn't a problem, then certainly it's possible to use one.

As Michael Kjörling mentions, you want (by convention) a vertically polarized antenna on VHF, not horizontal as the "T" you have drawn would be. But that's no problem -- we can make a vertical dipole also. The tricky bit is just getting the feedline into the middle in such a way that the feedline doesn't mess up the antenna.

There's a trivial solution: run the feedline *inside* the antenna. Such a thing can easily be constructed from a piece of coax:

The design is quite simple: cut a piece of coax to the length of a dipole. Then, strip the shield off half of it. If you want to be fussy, you might cut the coax-side of the dipole a bit short, since the HT body effectively makes it a bit longer. If you don't do this, you are effectively feeding the dipole a little off center, so the feedpoint impedance will be a bit higher. Not a big deal.

This design exploits a thing usually undesired in coax-fed dipoles: common-mode currents on the "feedline". You don't [need a balun](Using%20a%20balun%20with%20a%20resonant%20dipole.md) with this design, because the common-mode currents on the feedline are very intentionally half the dipole. Normally we don't want the feedline to be part of the antenna. Here, it *is* the antenna.

Alternately, you could argue this design is a case of an infinite balun.

To support the coax, you might attach it to a fiberglass rod with some heat-shrink tubing, or use semi-rigid coax that doesn't need additional support.

Thanks to a comment by user2338215, I have a great example of commercial antennas built this way. They are 2.4 GHz antennas, where even a full-length dipole is really small.

This antenna is so small that the feedline even extends up into the body. You can see here that the shield has been removed from the final quarter-wavelength of the line (that's one half of the dipole), and the other half of the dipole is made by a sleeve folded back over the feedline. You can construct the same thing by folding the coax shield back over itself, although the cable jacket makes for a relatively lossy dielectric.

This is a kind of sleeve or bazooka balun. The sleeve plus the coax shield make a coaxial transmission line. Usually they are shorted on the end at the left, which has the effect of making the sleeve not radiate. But they can be shorted on the other end (as in this picture), and then the sleeve does radiate, which is exactly what's desired in this case.

## Answer (score 4, by Forest)

Isn't one building a vertical dipole when they make a 'tiger tail' for their HT?

For an example and plans see this: http://www.hamuniverse.com/htantennamod.html

## Answer (score 2, by user)

There is one major reason why what you are suggesting isn't done, and it isn't the size of a two-part dipole versus a single (possibly shortened) quarter-wave utilizing the radio and operator as a ground plane.

**Polarization.**

Most of what you'd do with a handheld transceiver on VHF/UHF is probably FM, and with that combination, it's almost all vertically polarized. The setup you are suggesting, unless it's being held at an awkward angle (and putting huge stress on the antenna connector) would be horizontally polarized, which means you instantly lose about 20 dB to the cross-polarization on both transmit and receive. You'd also suffer from the dipole's radiation pattern: a little over 2 dBi broadside to the antenna, meaning that if you turn 90° you will suddenly lose a fair amount of signal strength.

Now, of course a vertically polarized dipole is perfectly doable; I would hazard a guess that it's a fairly common setup for a repeater antenna. However, there is one additional problem in that case: you need to get the antenna some distance away from the feedline, to avoid coupling leading to RFI and all kinds of strange resonance effects. You'd want to get the antenna at least half a wavelength from the feedline, and one wavelength if possible.

That means you have to have something (likely attached to the transceiver) which can support the weight of not only the antenna, but also a supporting structure to hold it at about a meter or farther out horizontally.

This is going to place a lot of stress on whatever supporting structure is being used, which in turn means it needs to be built to allow for that stress. That makes it relatively bulky, or in other words heavy. And you really don't want it falling off the radio; imagine the stress that would place on the antenna connector.

**Of course, you could make an antenna that comes with a simple ground plane.** Quite a few people do that, especially when using a handheld transceiver in a semi-fixed setup with an external microphone; they attach a wire to something they can insert in the shield part of the antenna connector, and then mount the antenna "on top of" that. That provides a ground plane, while maintaining the vertical polarization and thus avoiding the cross-polarization issue.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/644/handheld-dipoles, by Skyler 440, Phil Frost - W8II, Forest, user. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
