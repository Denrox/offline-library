# Why prefer LC oscillators rather than RC oscillators in RF design?

*Tags: oscillator · score 10*

## Question

I don't recall ever seeing an RC oscillator driven RF transmitter or receiver.

What prevents people from choosing RC oscillators in RF design?

## Accepted answer (score 10, by Phil Frost - W8II)

I'm going to discuss *filters* and not *oscillators*, because the reasons are pretty much the same. An oscillator is just a filter with enough gain to put it on the edge of stability.

It certainly is possible to use RC filters in RF design, and sometimes you do see them in non-critical filters, especially those that don't require a steep filter or high power handling, such as AC coupling between stages. Reasons you might not want to use inductors:

- They are expensive to manufacture
- Real inductors have significant non-ideal properties

 - saturation current
 - series resistance
 - inter-winding capacitance (for transformers, a special case of inductor)
 - leakage inductance

Resistors and capacitors also have non-ideal properties (lead inductance) and aren't free, but the magnitude of these problems is less.

Reasons you might want to include inductors in your circuits:

- A LC circuit has two [poles](What%20is%20meant%20by%20poles%20when%20discussing%20filters.md), where an RC filter has only one. You can get two poles with two RC circuits, but often that's just more components.
- An inductor's impedance increases with frequency, while a capacitor's inductance decreases with frequency. For many filter topologies you need both kinds of impedance (for example, a Pi network). You can simulate an inductor from a capacitor and an inductor using a circuit called a gyrator, but this has additional disadvantages:

 - The simulated inductance must have some resistance also, limiting Q factor
 - It increases complexity, and requires an op-amp capable of RF operation, which can be hard or expensive at higher frequencies
- Related to the previous point, if you have a capacitive impedance (such as all RC filters have), and you want to transform that to a purely resistive impedance (usually, 50Ω), then you need an inductor. Try playing with a Smith chart to see why.
- Resistors convert electrical energy to heat, where (ideal) inductors do not. Obviously you wouldn't want anything turning your transmit energy into heat instead of electromagnetic radiation.

## Answer (score 2, by hotpaw2)

The transient response of an RC circuit driven to oscillation by negative feedback generates a much higher proportion of harmonics than a similar LC circuits response. These harmonics have to be either filtered out with additional circuitry, or the oscillation needs a significant amount of post-processing (such as using it to clock an SDR or a digital synthesizer), in order to produce a clean enough waveform to meet legal requirements for RF transmission.

PLLs in receivers may or may not need as clean a waveform, depending on the receiver design.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1596/why-prefer-lc-oscillators-rather-than-rc-oscillators-in-rf-design, by Adam Davis, Phil Frost - W8II, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
