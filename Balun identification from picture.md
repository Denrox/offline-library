# Balun identification from picture

*Tags: balun · score 3*

## Question

I thought maybe this was a 4:1 balun, but a number of 4:1 single core balun diagrams that I found online had different connections. N1HFX's balun page and the bottom of G4WPW's page show a connection of one wire directly from the balanced to the unbalanced side. The pictured balun does not have such a connection.

There is only one core and the connector at the bottom is an SO-239. I may get a chance to test it later on with a 50 ohm load and an impedance tester, but at the moment this balun is not in front of me.

Is this a current balun or a voltage balun?

What should the impedance ratio be?

## Answer (score 4, by Hamsterdave)

Looks like it might be a clever way of winding a 4:1 voltage balun to simplify the wire routing (or just straight up incorrectly wired). I'd have to see the connections at the top more clearly to be sure.

Regardless, seems pretty safe to assume it's a voltage balun. The quick way to tell would be to check it for a DC short between the terminals on the unbalanced (or balanced) side. If they're shorted, it's a voltage balun, and as such, not much of a balun at all. The choking impedance from these single core 4:1 voltage baluns is so low (usually <500 ohms) as to be nearly useless unless your antenna has low enough impedance that yo don't need the 4:1 to begin with. W8JI and K9YC have both done good tear downs showing just how awful they are for most applications. They should be considered an impedance transformer and not much else.

**EDIT:** drawing out the windings, it appears it is an attempt to shoe-horn a 2 core Guanella 4:1 current balun on to a single core. Figure 2 here shows how it would be accomplished with two cores, and the builder appears to have just decided to do a split winding on a single core, perhaps in an attempt to get the best of both worlds, good common mode isolation and a 4:1 transformation on a single core. In reality, I would guess this actually causes it to exhibit less than a 4:1 transformation, in addition to having little common mode suppression. It appears it would exhibit considerable shunt capacitance between windings, and depending on the core material, potentially a low impedance shunt path through the core.

## Answer (score 2, by Ryuji AB1WX)

It looks like 4:1 Guanella transformer ("current balun") wound on one core. It may appear clever but it hurts performance. The choking impedance is also not as good as 1:1 Guanella ("current balun" or "common mode choke") so if the choking effect is necessary, use 1:1 Guanella on the 50ohm side of this transformer.

The way the transmission line is constructed, it is made for 50 ohm to 200 ohm rather than 12.5 ohm.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6903/balun-identification-from-picture, by Paul, Hamsterdave, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
