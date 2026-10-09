# Can the reactance on a transformer load, be "corrected" on the transformer primary, to improve transformer efficiency?

*Tags: impedance-matching, transformer, efficiency · score 4*

## Question

The following question is regarding the ability of a transformer, UnUn or BalUn, to be efficient, if the transformer (UnUn in my case), is feeding a load with reactance, and what can be done about the reactive load, on the transformer's input (primary):

1. Is the reactance on the output of a transformer, that is connected to a reactive load, seen on the input of the transformer?
2. If the transformer does transfer the reactive component, can that reactance be tuned out on the input side?
3. I'm trying to ascertain if reactance of an antenna, can be tuned-out on the input of an UnUn, to conserve the UnUns efficiency, or make it as efficient, as it would be if the UnUn were feeding a purely resistive load?
4. If reactance carries through to the primary, in the case of an UnUn, does reactance also carry through in the case of transformers that have no ports in common, i.e., transformers where the primary and secondary terminals are not physically connected? Would that type of transformer present a purely resistive, higher impedance, at the primary?

Schematic of question example:

**Transmitter|Coax|Antenna_Tuner|UnUn|Antenna_with_reactance**

I know I've asked the question several ways; so as not to be misconstrued.

## Accepted answer (score 4, by hobbs - KC2G)

Is the reactance on the output of a transformer, that is connected to a reactive load, seen on the input of the transformer?

Yes (transformed by the transformer's impedance ratio, and modified by any non-ideality of the transformer).

If the transformer does transfer the reactive component, can that reactance be tuned out on the input side?

Yes. We do this all the time in amateur radio. You might have a folded dipole connected to a 4:1 balun. On almost every frequency, that antenna will have some reactance, but that reactance can be matched by a tuner on the input side.

I'm trying to ascertain if reactance of an antenna, can be tuned-out on the input of an UnUn, to conserve the UnUns efficiency, or make it as efficient, as it would be if the UnUn were feeding a purely resistive load?

Not quite. If the load is reactive, and the matching is on the "other side" of the transformer, then that necessarily means that there is reactive power flowing through the transformer, and that reactive power is eligible to be turned into heat by any losses in the transformer, while not doing any useful work.

If reactance carries through to the primary, in the case of an UnUn, does reactance also carry through in the case of transformers that have no ports in common, i.e., transformers where the primary and secondary terminals are not physically connected?

Yes, it doesn't particularly matter whether it's an isolation transformer (a "transformer with no ports in common"), an autotransformer (unun), or a transmission-line transformer (many current baluns). All of them will *ideally* transform an impedance in the same way, although their non-idealities are probably different.

Would that type of transformer present a purely resistive, higher impedance, at the primary?

No. A complex impedance is transformed into another complex impedance.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22685/can-the-reactance-on-a-transformer-load-be-corrected-on-the-transformer-primar, by Louis Seaman, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
