# Does an SWR higher than 1:1 necessarily cause additional heat in the transmitter?

*Tags: impedance-matching · score 7*

## Question

Each of the 3 answers to [SWR of 1.5 -- use internal antenna tuner or not?](SWR%20of%201.5%20--%20use%20internal%20antenna%20tuner%20or%20not.md) in one way or another suggest that an SWR of 1.5:1 will cause additional heat in the transmitter:

The radio may heat up a bit more during transmit with a 1.5:1 SWR, however i imagine that all Icom radios are designed to easily handle the slight increase in temperature without problems.

It is probably easier on the radio to use the tuner. The disadvantage of the tuner it that it decreases efficiency slightly. But with the swr fixed by the tuner, the radio may be able to put out a higher power without overheating, which should more than make up for the efficiency loss.

If you do use the tuner, you move the mismatch from the PA to the tuner circuitry, and instead of heating up the PA transistor(s) you will be heating up the tuner components. The cooling fan will be used to remove the heat.

Reading these answers, one could get the impression that an SWR greater than 1:1 *always* causes additional heat in the transmitter, and this additional heat is the reason we might want to minimize SWR. Is that correct, or might the effects and dangers of a high SWR be something else?

## Accepted answer (score 7, by Phil Frost - W8II)

A mismatched load might make the transmitter hotter, but it might also make it relatively cooler. It might also precipitate other failure modes, such as flashes, smoke, bangs, oscillation, spurious emissions, low output power, or locusts. OK probably not locusts, but a high VSWR is bad not because it will necessarily overheat the transmitter, but because the transmitter's specifications are only valid when the load meets specifications. Operating the transmitter outside these specifications results in "undefined behavior", which depends on the specific load impedance encountered, and the design of the transmitter.

As others have stated, VSWR is a property of the line and the load, not the transmitter. One could for example have a 50 ohm antenna on a 400 ohm feedline, a VSWR of 8:1, but the transmitter still sees a 50 ohm load.

That's probably not what's often meant however. For the purposes of this question we probably assume a 50 ohm feedline, so a VSWR greater than 1 means the transmitter sees something other than the 50 ohms it was designed for. The feedline is actually irrelevant, except that it's part of what determines the impedance seen by the transmitter.

Now if the VSWR is greater than 1, this means there's some reflected power in the transmission line. The common assumption seems to be that this reflected power makes it back to the transmitter, where it is necessarily converted to heat, somehow.

But how can this be if the transmitter sees only an impedance? In other words, the transmitter doesn't "know" if it's seeing an impedance of 40+15j ohms because there's a 75+0j ohm load at the end of some length of transmission line, or if there's a 40+15j impedance connected directly at the antenna terminal.

So this notion of "reflected power being converted to heat" has to go. Instead we should be asking if a load other than 50+0j ohms, as seen at the transmitter's antenna connector, makes the transmitter hotter.

Transmitters are not magic circuits. A linear transmitter consists of some voltage source (or you could model it as a current source, if you prefer) with some impedance $Z_{src}$, driving some load of some impedance $Z_{load}$. The source impedance is determined by the transistor or tubes used and things like the resistance of the traces or wires connecting them, as well as filters and transformers and relays that might interface those transistors to the antenna connector. Still, no matter how complicated the transmitter, if it's linear, at a given frequency, its operation can be fully modeled by a voltage source and a series impedance:

The question is this: when $Z_{load} \ne 50\:\Omega$, is the power dissipated in $Z_{src}$ necessarily greater?

No. There are a couple interesting cases:

1. If $\Re[Z_{src}] = 0\:\Omega$, no power can be dissipated in the transmitter at all, and so there is no heat generated in the transmitter for any load impedance. Unfortunately, such a transmitter is not practically realizable.
2. If $Z_{load} = Z_{src}^*$ then efficiency is 50%. That is, for each joule of energy delivered to the load, the transmitter has to do something with 1 joule of thermal energy. One might be inclined to say something about the maximum power transfer theorem, but that theorem is somewhat misleadingly named. More power can be transferred at a higher efficiency by reducing $Z_{src}$. A more appropriate name may be the "Maximum power transfer (assuming you can't reduce the source impedance and you don't care about efficiency and your components are indestructible) theorem", or MPTAYCRTSEIAYDCAEAYCAIT.

The question is incompletely posed: does a mismatched load cause the transmitter to get hotter, assuming what else is held constant? If we just take any transmitter and without adjusting any knobs change the load impedance, it's rather hard to say. Changing the load impedance may cause the transmitter to produce more or less power. So if changing the load impedance causes the transmitter to get 5% hotter but deliver 15% more power to the load, is that good or bad?

So let's frame the question in terms of efficiency:

$$ \text{efficiency} = {\text{energy delivered to load} \over \text{energy drawn from power supply}} $$

Where here, "the load" refers to everything past the antenna connector, and so includes the feedline (because remember, the transmitter can't really tell there's a feedline).

Any energy drawn from the power supply but not delivered to the load will in practice be converted to heat since there isn't really any other place to go.

So then, does a load impedance other than 50 ohms always result in reduced efficiency?

## No.

Efficiency is determined by the ratio of the real parts (resistance) of the source and load impedance:

- zero source resistance, zero load resistance: no real power can be transfered, efficiency not an especially useful concept
- zero source resistance, nonzero load resistance: 100% efficiency
- low source resistance, high load resistance: high efficiency
- source and load resistance equal: 50% efficiency
- high source resistance, low load resistance: low efficiency

Minimizing reactance also improves efficiency because it reduces reactive power, which minimizes unnecessary voltage and current.

When a load is specified as just a VSWR, there are infinitely many impedances which that could be. Of all of those, one will have maximum efficiency and be more efficient than the matched case, one will have minimum efficiency and be less efficient, and all the rest will be somewhere in between. So, for some cases of a mismatch the result might be *less* waste heat in the transmitter.

So does this mean there is a "better" impedance than 50 ohms? The answer is again probably no, because while there may be some load impedance which is *more efficient*, efficiency probably isn't the only concern. As the load impedance increases efficiency goes up, but also maintaining the same power requires a higher voltage. Since the transmitter can't generate an infinite voltage, this might mean the transmitter is unable to develop its rated power into this high impedance, high efficiency load.

Or more generally, the transmitter just may not work as specified when the impedance is outside the design range. It might not develop full power, or it might arc, or it might drive the MOSFETs into avalanche breakdown, or it might oscillate. Or it might overheat, but this is just one of several possible failure modes.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19921/does-an-swr-higher-than-1-1-necessarily-cause-additional-heat-in-the-transmitt, by Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
