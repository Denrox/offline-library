# Does the phase of an impedance mismatch matter?

*Tags: antenna, antenna-theory, smith-chart · score 4*

## Question

Given two antennas with the same SWR of 1.5:1, is there any advantage to the one having an impedance mismatch that is closer to pure resistive (e.g. a resonant dipole in free space with an impedance of around 73 Ohms), versus an antenna with a geometry that is capacitive or inductive which causes the 1.5:1 mismatch to a 50 Ohm feedline system at some given transmit frequency?

e.g. what difference might it make when a point on a Smith chart from an antenna measurement is horizontally some distance from the 50 Ohm referenced center of the Smith chart, versus a point above or below the horizontal (non-reactive) line, but the same distance from center?

If there is a difference, does that difference somehow affect radiation "efficiency", or just affect the transmitter in some way?

## Answer (score 2, by Ryuji AB1WX)

There are two different factors here. Mismatch loss, which you can calculate from the SWR, and radiation loss, which is directly related to how the antenna operates (regardless of feedline match or mismatch) and has nothing to do with SWR.

The mismatch loss is directly calculated from SWR. If the SWR is 1.5, you lose 4% of the power regardless of the phase of the reflection.

The radiation loss is really specific to the antenna and how it's deployed, but let's just give a simple example.

If you are dealing with a well-designed symmetric antenna like a dipole or a loop, whether the radiation impedance is 33 ohm or 75 ohm, pure resistive, the radiation loss is not going to change very much, as the dominant cause of the loss is the wire's ohmic loss.

However, if you are dealing with a vertical monopole or similar asymmetric antenna, the radiation efficiency is generally better when the radiation impedance is 75 rather than 33 (purely resistive) in both cases because the dominant cause of the loss is the ground loss, and the ground resistance is a smaller portion of the total antenna system when the radiation impedance is 75.

The above example also illustrates why one should not use SWR to measure antenna performance.

I should also add that the "radiation efficiency" is unrelated to the "effective aperture" or "gain" of the antenna. Also, the total radiated power needs to factor in the total power delivered to the radiation resistance (not the nominal transmitter output power times the efficiency because real transmitters likely deliver different watts depending on the total load impedance).

Which reflection angle is least burdensome to the transmitter is a different question and the most practical answer is we don't know, prepare for the worst case. That is because the reflection's angle also changes through the LPF and matching network inside the transmitter, but what matters is the phase angle at the final amp transistor's collector/drain/plate/anode.

Which reflection angle is easier to match with the least loss... that is when Z = 50 +jX (requires one series capacitor to match) or Y = 0.02 + jB (requires one shunt capacitor to match). The latter technique is useful when you use 1/4 wavelength vertical on seawater ground (radiation impedance is about 35 ohm, SWR about 1.5), because you can make the antenna more inductive by making it slightly longer, and then add a shunt capacitor to bring it to 50 + j0.

If you were to use a proper L-match, then turn to the constant-Q curves on the Smith chart (they are not printed on the chart - but any decent RF engineering textbook will show them). As you see, Q is the lowest near the real (resistance) axis. Staying within that range is least lossy when you build an L-match. When you were to use pi- or T-match, a greater Q (which is a design parameter) is experienced by the network, which contributes to a larger loss, given the equal component quality. Generally, pi-networks work well with loads in the lower than 50 ohm side and T-networks higher.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22988/does-the-phase-of-an-impedance-mismatch-matter, by hotpaw2, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
