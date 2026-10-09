# 1:4 Guanella unun current balun

*Tags: balun, transformer · score 3*

## Question

I am having trouble understanding the 1:4 Guanella current balun here. So at DC, or low frequencies, I think the current path would be a short to ground. At higher frequencies, I am getting confused on how the current path through the lower coax's inner conductor, whose return path is along the shield of the outer conductor, behaves. I get the concept that power is conserved, so if the voltage doubles, the resistance must quadruple (P=V^2/R). But, why does the voltage double? Does the extra current returning on the shield of the upper coax lower the ground potential? Or does it double the returning current on the shield while the inner conductors current is left unchanged?

## Answer (score 3, by Phil Frost - W8II)

It may help to consider that this:

is equivalent to this:

The lines above the transmission line indicate it is wound on a ferrite. Because only the common mode affects the electromagnetic fields outside the coax, the ferrite increases the common mode impedance but does not affect the differential mode. To simplify analysis we can assume the common-mode impedance is infinite, and so the common-mode current must be zero.

The second diagram indicates two separate windings instead of coax. Because a differential current in the windings creates opposite magnetic fields that cancel, differential current doesn't "see" the core, and differential mode impedance is unchanged, whereas common mode current "sees" the core and a higher (assumed infinite) impedance. The mechanism is slightly different but the effect is the same.

Having accepted the equivalence of these two constructions, you should be able to follow [other explanations of a Guanella balun](How%20does%20a%201%204%20current%20balun%20work.md).

## Answer (score 2, by tomnexus)

The voltage doubles because the two coaxial cables are connected in *parallel* on the input side, but in *series* on the right hand side.

In the diagram, there shouldn't be a little i in the middle of the upper coax, no common-mode current can flow there.

This trick doesn't work with batteries at DC, it just shorts out the supply, but at RF the choke, shown as the dotted lines on the upper coax, effectively disconnects it from the rest of the circuit. The coax through that choke, or wound around that core, is like a magic non-connected tunnel between left and right.

The twin-coax unun has very good high frequency performance because the two coax lines mean that the added voltages on the output *are always in phase*. The low frequency limit is where the choke no longer provides an impedance that is several times the output impedance, which depends on the ferrite, but within reason *there is no impact on the high frequency performance by using a larger core and/or more turns*. If the high frequency performance isn't important, say you only need 1.8 to 14 MHz, then the lower coax can be omitted entirely. This is also what you get from a 1:4 bifilar-wound unun on a single core.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18347/1-4-guanella-unun-current-balun, by Erik McKee, Phil Frost - W8II, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
