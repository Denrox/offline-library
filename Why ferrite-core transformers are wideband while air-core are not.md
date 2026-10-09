# Why ferrite-core transformers are wideband while air-core are not?

*Tags: antenna, impedance-matching, bandwidth, transformer · score 7*

## Question

While experimenting with end-fed antennas I've made two 1:49 transformers.

The first one has an air core, as shown in the article by John, M0UKD. This transformer doesn't even work as a transformer until you add a capacitor in parallel to the load. The secondary winding of the transformer and the capacitor should form an LC-circuit resonant on the desired frequency. The transformer works very well, but the bandwidth is narrow.

For the second one, I used FT240-43 ferrite core, as shown in the article by Rudy, N6DOZ. This transformer is wideband and works on 3-30 MHz. Although when loaded to 2450 Ohm non-inductive load (metal-oxide or metal-film resistor) instead of 50 Ohm we see a slightly inductive load:

From what I know this is because the large secondary winding works as an inductance in series with the load. This inductance can be compensated by placing a capacitor in parallel to the primary winding of the transformer. Here is the effect of placing a 57 pF capacitor (47 pF || 10 pF):

The part that I don't quite understand is why the transformers work so differently depending on the core material? Why the one that uses a ferrite core is so wideband while the first one doesn't even work as a transformer without an extra capacitor?

## Answer (score 3, by Antonio51)

"Why ferrite-core transformers are wideband while air-core are not?"

Air-core "transformer" is composed of 2 inductors "TUNED" with a magnetic coupling slightly less than 1. The resulting effect is a narrow bandwith "transformer".

Example with coupling coefficient of 0.01 to 0.5

Ferrite-core "transformer" is "same" thing except that magnetic coupling is quasi perfect. So it really has the behavior of a transformer with large bandwith.

I have made a simulation in 2 cases (resistor ad hoc on output, open output, same K ... k1=k2).

I think it would be more clear now. See that "coupling" K is quasi "1".

And here what happen when capacitors are also used.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20280/why-ferrite-core-transformers-are-wideband-while-air-core-are-not, by Aleksander Alekseev - R2AUK, Antonio51. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
