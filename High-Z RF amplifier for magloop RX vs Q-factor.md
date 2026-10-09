# High-Z RF amplifier for magloop RX vs Q-factor

*Tags: antenna, antenna-construction, amplifier, magnetic-loop · score 5*

## Question

I've noticed that increasing load on magloop reduces it's Q-factor, it becomes less selective. Traditional way to approach this is reducing size of pickup loop, or alternatively, using transformer.

But is it possible/known approach to build FET high-Z preamp, which is connected to pickup loop? Being high-Z it should allow to reach maximum possible selectivity for magloop, as only minimal current will flow due to capacitance of the gate. One might even make it resonant.

I understand that high-Z would not be impedance-matched to 50-Ohm, but in this case it's not the goal. Goal is to let main loop oscillate with high-Q. This will increase field strength, and might allow good reception even with mismatched pickup loop.

**Magloop example:** This one is from KR1ST, but mine is similar. Depending on size of the small, low-Z coupling loop - looses in main loop increase and it becomes less selective.

## Answer (score 4, by Phil Frost - W8II)

Certainly it is possible to build a high-impedance amplifier. If you resonate the loop with a parallel capacitor (which perhaps includes the input capacitance of the amplifier), you've made a parallel LC circuit which at resonance has minimum current and maximum voltage. A high-impedance amplifier is what you'd want to best extract that signal.

But if your objective is to use the loop on a wide frequency range without retuning, this is the opposite of what you want. Instead, you want a low-impedance amplifier, the lower the better. You can think of the loop as a current source by Faraday's law of induction. The lower the input impedance of the amplifier, less impedance to this current. LZ1AQ has an example of such an amplifier:

In this design there is a passive filter at the input to attenuate the AM broadcast band and avoid overloading the amplifier. The low input impedance is achieved through the common-base Q3 and Q4, then Q1 and Q2 further buffer the signal and are designed to drive a twisted pair.

## Answer (score 2, by Brian K1LI)

If you prefer to purchase rather than build your own, high-input impedance preamps from Hi-Z Antennas sold by DX Engineering may work for you. Because they are often used to drive multi-element phased array systems at long wavelengths, they are designed to work with inexpensive 75-ohm coax, but should work fine with 50-ohm cable in your application.

Two bullet points from the manual may be important considerations for use with a small receiving loop:

- The amplifier input Resistance is approximately 54KOhms in parallel with 12 Picofarads
- The Antenna Ground input terminal is AC coupled to eliminate any ground related DC current

Many other features that you might value. I have no affiliation with Hi-Z Antennas or with DX Engineering.

## Answer (score 2, by Brian K1LI)

John Kaufmann, W1FV, published a two-part article in the September/October and November/December 2011 issues of the ARRL's *National Contest Journal* titled, "A Compact Dual-Band, 9 Circle Receiving Array." The phased-array system uses a simple amplifier with high input impedance:

The AD8055 op amp has a gain-bandwidth product of 300-MHz, so there's only about 10-dB of gain on the 10-meter band. Note that this "amplifier" is meant primarily to provide a wideband match between an electrically short antenna and a feedline. Its overall gain, as evidenced by the two 470-ohm resistors on the op amp inputs, is close to 0-dB.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17986/high-z-rf-amplifier-for-magloop-rx-vs-q-factor, by BarsMonster - R2AYN, Phil Frost - W8II, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
