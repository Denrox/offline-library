# Is it practical to use a magnetic amplifier as an AM modulator in a transmitter?

*Tags: modes, electronics, vacuum-tubes · score 4*

## Question

If I'm building a vacuum tube HF transmitter (say, 40 m band), obviously the simplest mode to build is CW; it's common to key the oscillator input to the final (in order to keep the oscillator running stably, minimizing chirp and drift).

If I want to add AM to this simple transmitter, one method of modulating the output might be to use a saturable reactor, aka "magnetic amplifier," to boost the output of a microphone to be added to the B+ plate voltage (coupled through a suitable capacitance, to keep high voltage DC off the microphone); the fluctuation of the plate voltage would control the gain of the PA, modulating the output.

I don't see plate modulation used much in radio circuits I've found, so there must be some disadvantage, but I don't see offhand what that would be; I think it's just simpler in a "normal" circuit to feed the output of one stage to the grid of the next.

Is there a big problem with using a magnetic amplifier to modulate the plate voltage this way?

## Accepted answer (score 3, by PeterH)

An interesting question. Not sure I can properly answer it but I'll contribute what I know.

**AM modulation methods**

Changing the RF output tube plate voltage was a very common way of producing AM when I was learning about ham radio in the 1960s. It was usually achieved by using a modulation transformer driven by an audio amp of the same output power as the unmodulated RF carrier, and should give symmetrical upwards and downwards modulation. This works extremely well with a final RF amp operating in the simple and efficient class C mode. There are other methods that eliminate the transformer but they have various disadvantages.

The problem with modulating an earlier stage is that the following RF stages must be linear amplifiers (less efficient, more difficult to achieve) or the transmission becomes spread across the spectrum in a very undesirable way.

With the rising popularity of SSB, where the SSB signal is produced at a low level and then amplified to output power using linear amplifier stages, transmitters already had the linear amp, so AM could be produced in a similar way with no extra complication. So your statement "I don't see plate modulation used much in radio circuits I've found", which was slightly surprising to me, might be the result of linear amplifiers becoming common...

**Magnetic Amplifiers**

A magnetic amplifier uses the change in inductance that occurs when an inductor's core is magnetically saturated (with a relatively small DC current through a high number of turns on the same core) to control an AC current.

This works because the inductor (L1) is designed to have high impedance at the frequency of the current that it is required to control when no control current is flowing, and low impedance if sufficient DC control current is flowing.

Due to the use of a core material with the right saturation characteristics it is possible to reduce or remove the magnetic effect of the core by passing a DC control current through a second winding and progressively saturating the core, so that the core contributes less and less to the inductance of L1. This lowers the inductance of L1 and therefore the impedance to the controlled ac. The resistance of L1 to DC is not changed.

There are several ways to stop induced emf from the (controlled) ac current from feeding back into the control circuit, all involving 2 magnetic fields or 2 emfs cancelling each other  
e.g. 2 identical magnetically separate saturable core inductors with the control windings in series and oppositely phased.

For in depth information about mag amps to control RF see the (pdf) thesis submitted by E. W. Steffen, Jr. Lieutenant Commander, United States Navy in 1948, found at https://calhoun.nps.edu/handle/10945/31621

**Controlling RF output amplitude**

From what I understand it is possible to use a mag amp to vary (at audio frequencies) the output power of an RF output stage. This requires a magnetic amplifier that can control the RF current flowing through the anode circuit and/or the power being coupled to the antenna.

This will present a varying anode load impedance which could cause other complications (e.g. instability) if not done carefully.

I would guess that placing L1 in the cathode circuit might also be worth a bit of good old amateur radio experimentation.

The magnetic amp would not be able to supply extra energy to the RF output (as a transformer coupled modulator can) so it would need to be carefully set up if symmetrical upwards/ downwards modulation is to be achieved.

One of the disadvantages of this modulation method is noted as the inefficiency due to losses in the core. Availability of suitable core material to work effectively at the carrier frequency limits the maximum useful operating frequency, but mag amps have been used to modulate high power **long wave** transmissions in the past (https://en.wikipedia.org/wiki/Magnetic_amplifier#Applications).

With robust high power solid state devices becoming available and cheap the advantages of mag amps (reliability, robustness, high voltage/current/power handling, good isolation) have diminished and the disadvantages (bulk, weight, cost) have comparatively increased, so it seems it would not be a competitive method of modulating a final.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14674/is-it-practical-to-use-a-magnetic-amplifier-as-an-am-modulator-in-a-transmitte, by Zeiss Ikon, PeterH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
