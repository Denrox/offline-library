# Resonant RF Transformer Substitution

*Tags: equipment-design, filter · score 6*

## Question

I'm looking at a RF transformer filter design that appears to be using the primary-side transformer inductance as part of a second-order band-pass filter (first schematic). This isn't the only filter in the design, but I believe I have isolated it properly. The center frequency is approximately 14MHz. My understanding is that the transformer is providing the inductance necessary for the filter as well as presenting the load impedance in parallel.

Now I'd like to use a generic "pulse" transformer, like those used in Ethernet or ADSL modems, but those have much higher winding inductances that make it practically impossible to design as part of a HF resonant circuit (e.g. 100µH or more). To compensate for that, I would need to add a separate inductor to get the effective parallel inductance to be correct (as shown in the second schematic). This eliminates the economy of the transformer acting as the inductor, but what else do I lose?

As requested, I went ahead and simulated the circuit using LTSpice, assuming a perfect magnetic coupling. The -6dB is due to the source impedance of the source. *As modeled,* the simulation results are identical.

## Answer (score 2, by jcoppens)

It seems an excellent idea. The only possible problem I could imagine, is maybe the internal capacitance of the 1:1 pulse transformer -I've seen numbers in the order of 30 - 50 pF. This isn't a problem in non-resonant (ethernet) apps, but you might have to adjust your 220 pF to compensate.

Just found another datasheet with only 15pF inter-winding capacitance.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2037/resonant-rf-transformer-substitution, by W5VO, jcoppens. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
