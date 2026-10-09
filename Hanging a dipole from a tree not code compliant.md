# Hanging a dipole from a tree not code compliant?

*Tags: antenna, united-states, dipole · score 13*

## Question

I just got off the phone with my town's electrical inspector (in Massachusetts), and he informed me that you are not allowed to hang anything electrical from "vegetation". He said if I did this with my dipole, that it would not pass inspection. He said that he can get me the NEC reference for this by sometime next week.

Has anyone dealt with this before? This is hard to believe considering so many people have dipoles. Are trees only technically ok for temporary installations?

The reason that I was talking to the inspector was because I was asking about oddities related to my electrical system + grounding. Then he blew up my world with the tree thing!

Update: This is the only relevant code reference that I have found on my own:

225.26 Vegetation as Support Vegetation such as trees shall not be used for support of overhead conductor spans.

You are apparently allowed to support lighting fixtures on trees per:

410.36(G) states that trees may be used to support fixtures. > This section contains two FPNs. The FPNs refer you to 225.6, which has the requirement overhead conductors may not be supported by trees. This includes the final means of attachment. In other words: A fixture mounted on a tree cannot be fed with overhead conductors.

My interpretation of this is you shouldn't have wire hung in the air feeding a tree. Versus running a wire up a tree. If you take 225.26 on it's own, you could maybe argue that vertically hanging an antenna is no good? Maybe I don't understand the definition of overhead conductor?

Update: 1/14/22 I talked to the electrical inspector again after giving him some NEC references (pasted below). He agrees that hanging an antenna from a tree is allowed. Woohoo! Thanks to everyone who commented (special thanks to @hobbs - KC2G). Hope this helps others in the future who may encounter the same issue with their town.

NEC references:

- 225.26 Vegetation as Support (vegetation not allowed)
- 230.10 Vegetation as Support (vegetation not allowed)
- 590.4(J) Support (vegetation not allowed)
- 810.12 Supports (no references to vegetation in this one)

Reading the following scope sections helps put these into context:

- 225.1 Scope
- 230.1 Scope
- 590.1 Scope
- 810.1 Scope

The absence of any wording related to vegetation or trees in 810.12 Supports is what seals the deal that hanging an antenna from a tree is allowed. If it was forbidden, it would really need to be noted here just like in the other sections about support which are tailored power supplying conductors.

## Accepted answer (score 16, by hobbs - KC2G)

**225.1 Scope.** This article covers requirements for outside branch circuits and feeders run on or between buildings, structures, or poles on the premises; and electrical equipment and wiring for the supply of utilization equipment that is located on or attached to the outside of buildings, structures, or poles.

An antenna isn't a "branch circuit" (wires between a circuit breaker and an outlet), it isn't a "feeder" (wires between a panel and a subpanel, more or less), and it isn't a power supply for outdoor equipment (like lights on poles), therefore nothing in article 225 applies to it.

Article 810 (Radio and Television Equipment) does apply to amateur radio antennas, and it contains things like having a static discharge and grounding it, grounding a lightning protector, grounding a metal mast that supports an antenna, not running your antenna or your feedline across power lines, etc. — but there's nothing about trees or vegetation in the article, or anywhere in Chapter 8.

What we do have is:

**810.12 Supports.** Outdoor antennas and lead-in conductors shall be securely supported. The antennas or lead-in conductors shall not be attached to the electric service mast. They shall not be attached to poles or similar structures carrying open electric light or power wires or trolley wires of over 250 volts between conductors. Insulators supporting the antenna conductors shall have sufficient mechanical strength to safely support the conductors. Lead-in conductors shall be securely attached to the antennas.

In other words, do a decent job so that you don't have wires flying all over the place in a storm, and don't use the power pole as a mast.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20417/hanging-a-dipole-from-a-tree-not-code-compliant, by Bonfire, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
