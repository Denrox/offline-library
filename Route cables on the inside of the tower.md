# Route cables on the inside of the tower?

*Tags: antenna, lightning, tower · score 3*

## Question

I was visiting a customer site who had their equipment fried by lightning and granted they forgot to install surge protection, so that's most likely what did it, however I also noticed they had the transceiver electronics mounted to the outside of the tower and the cable (Ethernet/POE) was routed on the outside of the tower from top to bottom. Since the tower is of course made out of metal I was thinking all the energy of the lightning would go down on the outside because of the skin effect. Looking at pictures of antenna towers I see it done both ways so I'm not sure how significant the effect would be and if I should tell them to move the whole thing to the inside (other than the antenna itself) or if they shouldn't worry about it once surge protection is in place. Any thoughts?

## Accepted answer (score 7, by KD9UQE CRAIG)

Without exceptional grounding of each leg of the tower with heavy straps and grounding rods and an unshielded 4ga ground wire from the antennas the Electromagnetically induced surges are severe on any conductor inside or out.

Under direct strikes to the tower/line, the voltage rises quickly at the contact point. Current and voltage propagate in the form of traveling waves in both directions. If the voltage exceeds the line-to-ground voltage of system insulation, it can produce an insulation flashover and a surge.

The primary purpose of ground wires is to shield conductors, capturing the lightning strikes. The degree of protection depends on the location of the ground wires relative to the conductors.

When lightning current travels in both directions along the ground wire and tower, it induces traveling waves in the conductors. When a traveling wave reaches the ground through a high inductance tower and the footing resistance is high, a flashover may occur. Having the signal conducters inside the tower is not going to prevent the damage. Besides the Antennas being disconnected from equipment to prevent the path of current the grounding prevents the flashover

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21110/route-cables-on-the-inside-of-the-tower, by pgibbons, KD9UQE CRAIG. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
