# Tradeoffs: varicap vs. air variable capacitor for Rx bandpass?

*Tags: receiver, filter, components · score 3*

## Question

What might be the tradeoffs between choosing varicap diodes versus air variable capacitors in the design and construction of tunable bandpass filters for HF receivers?

## Answer (score 4, by Marcus Müller)

First and foremost, varicaps aren't mechanical. If you want a rapidly tunable thing, that's a necessity; even if you just want something tunable by electronics, it's very desirable (otherwise you'll need to motorize your air gap cap...).

Air gap capacitors can be made to withstand very high voltages, which makes them desirable for anything that has to handle power – like transmit filters to suppress harmonics. On the other hand, you often don't need high flexibility in that, as you'd rarely use the same antenna for an octave or more of spectrum, so that a simple fixed filter (and a low pass at that!) would suffice.

Varicaps, especially together with digitally controlled voltages (DACs!) are a cheaper way of getting reproducible values, which seems very desirable: when you tune your receiver, you want the RX bandpass to (roughly) follow, right?

However, being semiconductor devices, varicaps are in fact temperature-dependent. In higher-end devices, this gets compensated, usually per measuring temperature and having a table for temperature adjustments, or via holding components at a constant temperature.

Note how the temperature dependency of that varicap is in the low single-digit percentage region; I'm told there's high-quality large variable air gap capacitors that can be tuned reproducibly to the same capacity with a comparable accuracy, but keep in mind this is a 0.65€/piece varicap – again, with a temperature compensation loop, you could get these tolerances much lower, for a fraction of the price of something mechanical and good.

Also note that unless you somehow mechanically link your air gap capacitor, multiple variable stages of a higher-order filter will be kind of hard to get right. With a varicap, you could just implement both capacitors in a multiple-feedback active low-noise bandpass:

The image is from my favourite filter toolbox; try R1=470 kΩ, R2=100 kΩ, R3=5.1 kΩ; C1=5 pF, C2=5 pF to get a feeling for this topology; then, read Analog Device's MT-220 note on design of MFBBPFs:

it comes with design instructions. Use a low-noise opamp such as LT6233; you'll have to build the circuit in SPICE and vary C3=C4 to form a look up table for frequency to desired reverse voltage).

You'd want your DAC-generated voltage source V_DAC (you could also generate that with a potentiometer!) to have a high impedance (relative to R1, and to C3=C4 at HF) so that you don't cancel your signal with it.

As you can see, for variable receiver bandpasses, varicaps and modern Opamp offer an elegant implementation methodology that makes building multiple stage filters easier – the output here is buffered, and hence, it's easy to concatenate multiple of these stages for higher selectivity (can't do that as easily with passive RLCs - the second stage loads the first).

In a real-world flexible HF receiver: I'd probably go for a simple selection between fixed bandpasses for say half a band each, and then throw a relatively high-dynamic range ADC at the problem to directly sample and thereby oversample the bandwidth. The amounts of problems that in-band blockers pose for ADCs are usually overestimated in this hobby; 10€ ADCs do > 70 dB of spurious-free dynamic range at 40 MHz bandwidth; and for a 0.5 MHz wide band, that is an oversampling factor of 80, which will put your (noise-dithered) sensitivity into thermal noise regions of CW channels, even if there's a +10 dBm interferer in the same band!

If that's not enough, you'll have to go with frontend band passes, followed by one or multiple stages of superheterodyne mixing/filtering.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17368/tradeoffs-varicap-vs-air-variable-capacitor-for-rx-bandpass, by hotpaw2, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
