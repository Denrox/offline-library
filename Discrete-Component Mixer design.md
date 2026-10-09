# Discrete-Component Mixer design

*Tags: receiver, electronics, mixer · score 4*

## Question

I was building a radio receiver for FM waves (87.5-108MHz), I want to build every block on my own (oscillators, mixers, demodulators) and then put them together. I was now designing a mixer and i choose a Gilbert-Cell Mixer. I wanted to know

1. If it's possible to build a Gilbert-Cell Mixer using discrete components and get it working on either a breadboard or a PCB
2. Resources for design of Gilbert-Cell Mixer (I did try googling, but not sure which are the reliable sources.)
3. Do you have any suggestions for other mixers that I could use?

What are some problems I might face while implementing it in hardware?

## Answer (score 5, by Marcus Müller)

If its possible to build a Gilbert-Cell Mixer using discrete components

Guess what Gilbert did! Yes, that's possible :)

and get it working on either a breadboard or a PCB

yes. Note that at frequencies this high, solderless breadboard is probably a bad choice, because the parasitic effects of the long metal bars inside will be larger than the values of some of the capacitors or inductors you need.

Note that discrete transistors are inherently bandwidth-limited. You will need to read the datasheets of your transistors very carefully to make sure your $\beta$ is high enough at the frequencies you need to work at! As a general guess: if it's available in a through-hole component package, its gain-bandwidth product will *probably* not be high enough for conversion in the 100 MHz region (and this kind of rules out soldered bread board). If it has "TIP" or "BC" in its name, it's going to be too slow. (Also: Get transistors for which you have a good simulation model, see below.)

Resources for design of Gilbert-Cell Mixer (I did try googling, but not sure which are the reliable sources.)

I'd start with Wikipedia (even if that muddies the waters a bit between what Jones designed and what Gilbert designed). It links to Gilbert's original paper, which is honestly easier to understand whilst still being correct than a lot of hobbyist literature out there.

Other than that, learn to use a circuit simulator! Gilbert did a lot of analysis with a pen on paper, and probably verified things numerically (with pen and paper and a lot of calculations); you don't have that time, but you have access to SPICE software, so learn that. You *will* not want to build circuits with transistors before being sure you're operating them all in the right point.

Also, plan for multiple prototype iterations: First you go for individual transistors to prove the concept, and be able to probe the signals using your oscilloscope. (You *need* to have some way to measure what you're doing!)

Second iteration would be more compact, and probably replace the individual transistors with matched pairs in the same package (for thermal equalization, see Gilbert's mixer paper referring to his own amplifier paper on having to make sure an equal amount of self-heating happens in both).

Do you have any suggestions for other mixers that I could use.

A couple (maybe 6 or so).

But for you, I think there's only one sensible other architecture: That would be a switching "chopper" mixer, which uses a square wave as multiplying waveform instead of depending on nicely linearized components for a continuous multiplication.

(there's many others, really, and I wonder whether you might have forgotten to read the "obvious" sources like wikipedia on frequency mixers, but you want an architecture that works well without too much tweaking. For example, a ring modulator with a high-power LO can be understood as very similar to a switching modulator, but you will need to understand how to measure, filter and isolate LOs if your carrier is sinusoidal, because diodes in real world aren't ideal, and you explicitly said you don't want to use an integrated component, where some manufacturer took care to choose transformers, diodes, and compensation elements for you).

I would call a switching mixer easier to build (at least approximately), and square waves are easy to generate well with CMOS technology (at least at the edge qualities that you would need), but you need to think about harmonics (after all, you might not even be using the fundamental of your square wave as LO!). But often, that's no problem, because your FM receiver is probably a superheterodyne architecture, so you choose an appropriate IF and filters, anyways.

However, fast edges then need you to put some amount of care into board layout, and might mean a few more transistors are necessary for high gains. I've never thought about building CMOS circuits from discrete transistors, as the "elementary" component no longer is the single transistor, but at least the complementary transistor pair, or rather the logic gate (and integrating that into an IC is a very good idea, for bandwidth reasons).

## Answer (score 4, by Ryuji AB1WX)

A good resource on Gilbert cell mixer online is here:

https://www.qsl.net/va3iul/RF%20Mixers/RF_Mixers.pdf

I would use a single-balanced version, as it simplifies the circuit and implementation. Using fast transistors like BFR193 or 2SC3355, you should be able to make one that operates at 100MHz but not on a breadboard!

However, building Gilbert cells in discrete components offers little appeal to me, especially for the FM broadcast receiver frontend. You could use an IC like NJM2594 or SA602 or TA7320P.

In particular, TA7320P is an IC from the 1980s specifically made for FM broadcast tuner frontend. You can buy a deadstock at a premium price, but there is no need to buy such unless you repair vintage equipment. However, you can study the data sheet and design examples that used that IC. Toshiba had several frontend, IF amp, and detector ICs in that era.

However, if I were to design an all-custom FM broadcast receiver, I would build the mixer using a single-balanced diode mixer circuit using two Schottky diodes. It requires the LO power to be about +7dBm, but that power is easily obtained at 100MHz, compared to the additional complications coming from implementing Gilbert cell in discrete components.

Both raw Gilbert cell and balanced diode mixer require an input transformer. That needs to be designed and built carefully.

Both Gilbert cell and balanced diode mixers operate in switching modes, where the LO voltage/power switches the transistor/diode. The key performance figure to pay attention for FM receiver is IIP3 or the measure of unwanted distortion. Gilbert cell is at a disadvantage here. The conversion gain/loss and NF are somewhat important but uncritical for broadcast receivers. (Gilbert cell is also at a disadvantage in the NF department.) That is why I would rather use a single-balanced diode mixer. You could, of course, use a double-balanced diode mixer if you want to minimize the LO power leakage, and especially if you are to use a DBM sold as a component, but 10.7MHz and 70MHz are far enough that a simple LC filter can attenuate the LO component leaking through the mixer rather easily, so I would slightly prefer the simplicity of single balanced mixer.

Other mixer options include a dual-gate MOSFET mixer (feed RF to G1, inject LO to G2), cascode amplifier (same principle as dual-gate MOSFET mixer). Those operate rather similarly to a single-balanced Gilbert cell without the differential operation. Those circuits were (notice the past tense!) commonly used in FM receivers, VHF TV tuners, and many low- to mid-range amateur radio equipment. Those would still work adequately for FM broadcast receivers.

Less preferred options are to use a transistor or a diode as a nonlinear device and cause cross-product. That just leads to other headaches, so I would not use it in practice unless the lowest cost is required. The last common example of such a mixer I know of was an analog UHF TV frontend. Also, these mixers are still used above several GHz where building a proper single-balanced mixer is more challenging.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23256/discrete-component-mixer-design, by Chiranka K, Marcus Müller, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
