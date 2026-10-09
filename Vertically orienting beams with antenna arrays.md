# Vertically orienting beams with antenna arrays

*Tags: phased-array · score 4*

## Question

Referring to the above picture, can an antenna array mounted on Node A direct beams towards Node B and Node E, **without** the need for an antenna rotator (or manually orienting the antenna array towards the respective nodes)? In other words, can the antenna array orient its beam along the vertical direction (along the line joining Node B and Node E)?

The motive for this question is related to the upcoming IEEE 802.11ad standard. By operating at 60 GHz, users communicate with one another through directional beams pointing at each other. Without the use of mechanical rotators for the antennas, how could these users possibly orient their beams in a changing/moving environment?

## Accepted answer (score 2, by Glenn W9IQ)

A practical approach for steerable patterns at these frequecies is to use electronically steerable arrays. These can take on various forms but a simple example consists of 2 or 4 vertical elements that are phased to steer the major lobe in the desired direction.

On the other hand, a dish or high gain yagi on 60 GHz has a very small footprint. This could be placed inside a radome and turned with a simple servo motor arrangement. Since the entire antenna is protected from the elements, no special considerations for a motor enclosure is warranted.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10282/vertically-orienting-beams-with-antenna-arrays, by V-Red, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
