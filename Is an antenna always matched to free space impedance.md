# Is an antenna always matched to free space impedance?

*Tags: antenna, antenna-theory, antenna-system, impedance, impedance-matching · score 5*

## Question

In this thesis the following model for an antenna is proposed:

It is seen as a 2 port network, in which only port 1 is accessible (port 2 is an imaginary connection between the antenna and the free space). Precisely:

- $Z_0$ is the feed line impedance.
- $jX_a$ is the antenna reactance.
- $R_l$ is the antenna parasitic resistance (which accounts for losses).
- $Z_{fs}$ is the free space impedance (377 Ohm)
- The transformer represents what an antenna really does: it transforms the free space impedance $Z_{fs}$ to a radiation resistance (which is the impedance seen at the primary of the transformer.

This description is quite clear. But then, the author says:

Since free space represents a matched termination, there would not be any reflection occurring ($\Gamma_L = 0$).

It does not seem too obvious for me.

As seen above, an antenna may be seen as a two - port network in which port 2 is closed on 377 Ohm. I'd say that usually there exists a mismatch on port 2, and so there is reflection at port 2. This doesn't mean there will be reflection at port 1 too, it depends if the antenna is able to match those 377 Ohm to the feed line impedance.

But I don't understand why there shouldn't be reflection at port 2. Maybe the author is considering a specific assumption he hasn't written, even because I've read somewhere that reflection along (not at the feeding port) some antennas exists and is a problem.

For instance, an infinite biconical antenna is perfectly matched to free space because it's like an infinite transmission line

A real biconical antenna is not matched to free space because it's truncated.

## Answer (score 3, by tomnexus)

I don't think the "matching to free space" should be taken so literally. I've never seen an actual equivalent circuit in a textbook or used it to derive any property of an antenna.

Sure an antenna is the *interface* between the transmission line and free space. And they both have an impedance with units of ohms, *but they're of a completely different nature*.  
On the transmission line, impedance Z=V/I, the ratio of the voltage and currents, while the impedance of a travelling wave, in free space or something else, is Z=E/B the ratio of the electric and magnetic field strengths *of the TEM wave*).

But the behaviour of an antenna is well described by solving the field equations near the antenna. Some antennas can be solved or approximated analytically, and then the solutions contain the permittivity and permeability of free space and the speed of light.

As for solving transmission line equations - you generally work from right to left, transforming the impedance, until the input impedance is found. So in this model you'd take 377 $\Omega$, then apply some transformer and some RLC network, and that would yield the input impedance of the antenna. There's no transmission line, so no need to talk about reflections, it's just impedances being transformed by circuit elements. (until you connect it to a piece of 50 $\Omega$ coax, then you can calculate the reflected power etc. if that's what you need).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17872/is-an-antenna-always-matched-to-free-space-impedance, by Kinka-Byo, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
