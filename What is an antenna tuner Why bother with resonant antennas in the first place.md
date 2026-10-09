# What is an antenna tuner? Why bother with resonant antennas in the first place?

*Tags: antenna-system, antenna-tuner · score 14*

## Question

There are a lot of antenna tuners on the market that have various capabilities in terms of how they can allow random radiators to work with our transceivers.

What exactly do they do? My understanding is that they can neutralize the imbalance between inductive and capacitive reactance so the transceiver can couple the most power out (or in) even though an antenna might not be resonant on a particular operating frequency, since overall impedance (Z) consists of three parts, two of which are reactance dependent on frequency: X(sub)L and X(sub)C, and R, the radiation resistance of the whole system. And the transmitters do not work as well into a non-resistive load.

With a resonant antenna these are in balance such that the characteristic radiation resistance of the antenna is presented to the transmitter. For a plain dipole that tends to be roughly 72 ohms. And there are many antenna analyzers out there that can assist in the physical pruning of antennas in order to reduce the SWR on the feedlines.

(I remember using light bulbs to tune up old tube-type transmitters because they were mostly resistive and non-reactive at HF)

300-ohm ladder line to a dipole requires a 4:1 balun to bring the impedance down to a range the transmitter can handle, which is typically 50-75 ohms, resistive, to keep the transmitters within their limits.

So what does an antenna tuner do? Does it reduce the SWR (loss) on the feedlines? Or does it simply ensure a match for the transmitter so it can operate at maximum efficiency regardless of whether a signal is coupled from the antenna to the outside world?

To further complicate the question, there is the matter of Q - the measure of the bandwidth for which the antenna will most efficiently accept transmitter power and radiate it. My understanding is that the best resonant antennas have a high Q which means a very narrow bandwidth for which they are most effective.

I've often used tuners when using 80-meter dipoles on the 75-meter phone section of the band, in order to reduce indicated SWR.

Similar to using 40-meter antennas on 15 meters, though that is more problematic since the harmonics don't line up as closely and it takes a better tuner than my current travel model.

So the question is in two parts:

What is an antenna tuner? If it is mounted at the transmitter is it actually tuning the antenna itself? Does it reduce the SWR in the feedline to a non-resonant antenna, for instance? Should the tuner be placed at the antenna instead of at the transmitter in order to reduce SWR loss (heating) in the feedline?

And if it is possible to use a tuner to make a transmitter feed power into a coat hanger then why do we worry about making resonant antennas in the first place?

## Accepted answer (score 13, by Glenn W9IQ)

And if it is possible to use a tuner to make a transmitter feed power into a coat hanger then why do we worry about making resonant antennas in the first place?

In a word - efficiency.

Consider that a full size 40 meter, 1/2 wavelength dipole is approximately 65 feet (19.8 meters) long. A dipole that is only 2 feet (0.6 meters) long, would have a gain of only 0.5 dB less than the 65 foot dipole. This would hardly be a noticeable difference on the air. But the problem is we cannot make the *antenna system* efficient enough to realize that minor 0.5 dB loss. The system inefficiencies often result in substantial losses compared to a full size dipole.

But we also should not be obsessed with resonant antennas - it makes little difference with practical antennas if we properly deal with their non-resonant effects. A 10/8 wave dipole has nearly double the gain of a 1/2 wave dipole. It is not resonant but can easily be matched to a transmission line with a simple matching network. A Yagi antenna is not resonant without the addition of a matching network. Also consider that many resonant antennas are not resonant at the impedance of the feedline anyway - for example, an ideal 1/4 wave ground plane vertical is resonant at approximately 34 ohms.

Here are some typical sources of *antenna system* inefficiencies:

**Radiation Resistance vs Resistive Losses**

Radiation resistance is an often misunderstood and misapplied term. The radiation resistance *of an antenna* is caused by the radiation of electromagnetic waves. For a free space, 1/2 wave, center fed dipole of reasonable construction, the radiation resistance is ~73 ohms. Any resistive losses (power that is not radiated) in the antenna add to this radiation resistance to contribute to the feed point impedance. In the case of this dipole, there will be a very small amount of RF resistance due to the wires that make up the dipole. If we use 14 gauge (1.45 mm) wire to construct the antenna, the RF resistance will be ~2.7 ohms. The total feed point impedance would then be 75.7 ohms in this example.

The efficiency of an antenna is given by the formula:

$$Efficiency = \left( \frac{R_r}{R_r+R_l} \right)$$

where Rr is the radiation resistance and Rl is the resistive losses.

So if we apply this to our dipole example above, the efficiency would be 96.4%. By contrast, the two foot dipole will have an Rr of approximately 0.04 ohms and a comparative Rl of 0.08 ohms resulting in an efficiency of 33%.

To complete this part of the efficiency picture, consider that:

$$ Gain = Directivity \times Efficiency $$

A full size dipole has a directivity of 1.65. Multiply this times the 96.4% efficiency of the above example and the gain becomes 1.59 (2.02 dBi). For the short dipole, the directivity is 1.5. Multiply this times the 33% efficiency of the above example and the gain becomes 0.5 (-3.01 dBi). So we already have a 5 dB difference between the two antennas and there still are other *system* losses that must be taken into account.

**Matching Networks / Tuners**

In the example of our 1/2 wave dipole, the feed point impedance of the antenna is ~ 75 ohms. If we are attempting to drive this with a 50 ohm source, we may wish to have a tuner or matching network that does the transformation between the two largely resistive impedances. In this case, a well built tuner or matching network will have an efficiency in the 80-95% range (less than 1 dB of loss).

In the case of our short dipole example, the situation is a bit more complex. We need to both cancel the capacitive reactance of the dipole and match the very low feed point impedance. Without going through laborious calculations of matching network efficiencies, it would not be unreasonable to expect less than 10% efficiency (>10 dB loss) from the matching network. This means that at least 90% of the applied power or signal will be lost to heat in the matching network alone. Our short dipole *system* now has a gain of -13 dBi which is more than 15 dB down from our full size dipole example. This is the equivalent to comparing the signal strength of a 100 watt transmitter to a 3 watt transmitter.

**Transmission Line Loss**

All real world transmission lines exhibit loss. This in itself is a reduction in efficiency. The specification for the transmission line lists the loss for the transmission line at a given frequency assuming that the transmission line is terminated in its characteristic impedance. When the transmission line is not terminated in its characteristic impedance, the loss of the transmission line increases (the efficiency further decreases).

By placing a tuner or matching network close to the antenna to provide a match to the characteristic impedance of the transmission line, the additional losses due to a transmission line mismatch can be avoided. This maximizes the efficiency of a given transmission line.

There is a secondary effect when the transmission line is not connected to a load that matches its characteristic impedance - the transmission line will no longer exhibit its characteristic impedance. Another way of saying this is it becomes an impedance transformer. For example, our 75 ohm dipole impedance in the early example when connected to 23 feet of RG213 will be transformed to 34 ohms at the transmitter end of the transmission line. The total losses in the transmission line will be 0.119 dB, of which only 0.009 dB is due to the mismatched load. A free program such as TLDetails makes quick work of these calculations:

In some cases, this transformation can be used to our advantage by transforming the antenna impedance to something that is more usable from a system efficiency perspective. In other cases, it can worsen the system efficiency. But do consider this transforming effect in light of transmitter output efficiency.

**Transmitter Output Efficiency**

The final efficiency factor to be considered is the output power of the transmitter. Most amateur transmitters are designed to deliver their rated output power when connected to a 50 ohm resistive load. Any deviation from this load will typically result in lower output power from the transmitter. This loss of transmitter output power effectively reduces the efficiency of the system.

For example, a 100 watt, 50 ohm source impedance transmitter that is connected to the 23 feet of RG213 that is terminated with our 75 ohm dipole, will output 96 watts (if no protection circuits kick in). This is an output efficiency of 96% (a 0.17 dB loss). Note that this is most likely more efficient, in this example, than using an antenna tuner at the transmitter to match the transmitter impedance to the feedline impedance (even though this is a 1.5:1 SWR).

**SWR**

SWR is based on the relationship of the transmission line characteristic impedance to the impedance of the load on the transmission line. In the case of a transmitting system, the load is typically the antenna. In the case of a receiving system, the load is typically the receiver input impedance.

Since we have already dealt with the relationship of the transmission line characteristic impedance to the load impedance in the earlier transmission line section, we need not consider SWR as another source of inefficiency.

## Answer (score 10, by Phil Frost - W8II)

My understanding is that they can neutralize the imbalance between inductive and capacitive reactance so the transceiver can couple the most power out (or in) even though an antenna might not be resonant on a particular operating frequency, since overall impedance (Z) consists of three parts, two of which are reactance dependent on frequency: X(sub)L and X(sub)C, and R, the radiation resistance of the whole system. And the transmitters do not work as well into a non-resistive load.

It some cases, it's not a question of coupling power into the load. For some impedances, a mismatched load may enable *more* power to be coupled into the load, however this would destroy the transmitter! Thus, the purpose of the tuner is also to present an impedance to the transmitter that allows it to work within the limits of its maximum current and voltage.

Radiation resistance also depends on frequency, and the tuner doesn't necessarily just cancel reactance. Consider an extreme example: a 1-wavelength long wire dipole has a radiation resistance around 4500 ohms and no reactance. That doesn't mean there's nothing for the tuner to do: the tuner needs to step down that impedance to 50 ohms.

300-ohm ladder line to a dipole requires a 4:1 balun to bring the impedance down to a range the transmitter can handle, which is typically 50-75 ohms, resistive, to keep the transmitters within their limits.

That's not the only way to use 300-ohm ladder line. If it's used in 1/2 wavelength multiples of length, then the ladder line will have no effect on the load impedance seen by the transmitter. The impedance step-down can also be accomplished with a network of inductors or capacitors, either fixed, or variable as in a tuner.

Or if the antenna wasn't matched to start, the right length of 300-ohm ladder line might result in a matched impedance at the transmitter. Using controlled lengths of feedline to match loads is called stub matching. Given the ability to pick the transmission line length and impedance, any load can be matched. If the transmission line impedance can't be picked, then any load can be matched with no more than two lengths of transmission line.

there is the matter of Q - the measure of the bandwidth for which the antenna will most efficiently accept transmitter power and radiate it. My understanding is that the best resonant antennas have a high Q which means a very narrow bandwidth for which they are most effective.

Antenna losses reduce Q, so for example a vertical with a poor ground plane will have a lower Q and wider bandwidth. A dummy load has a Q of zero and infinite bandwidth.

But losses are not the only factor. A vertical shortened by loading coil has a higher Q than one a full 1/4 wavelength long, yet the shortened vertical is generally a poorer antenna. A 1/2 wave dipole made of thicker wires, or made of a cage of wires, or thickened as in a folded dipole, has a lower Q than one made of thin wire, and yet is just as effective.

I've often used tuners when using 80-meter dipoles on the 75-meter phone section of the band, in order to reduce indicated SWR.

Tuners are often required on 80/75-meters due to two factors:

- electrically shortened antennas (loading coils, for example) are frequently used to make the otherwise very large antennas manageable, and
- the fractional bandwidth of that band is very large.

What is an antenna tuner?

It's any network of components designed to match one impedance to another, with variable components to accommodate use at a number of frequencies or with a variety of antennas. Frequently, it's a PI network:

If it is mounted at the transmitter is it actually tuning the antenna itself?

No. Arguably, if it's mounted at the antenna it's not actually tuning the antenna either, although such an arrangement can avoid additional losses in the feedline due to increased SWR.

It just depends on how you define "the antenna". As far as the transmitter is concerned, all that matters is the impedance appearing at its terminals. Some antennas could be said to contain feedlines, such as those with stub matches, or phased arrays using transmission lines for phasing delay. Are those transmission lines part of "the antenna"? What if a transmission line is an integral part of the antenna, such as in a zepp, or a gamma match, or a folded dipole?

Does it reduce the SWR in the feedline to a non-resonant antenna, for instance?

Not if it's mounted at the transmitter.

Should the tuner be placed at the antenna instead of at the transmitter in order to reduce SWR loss (heating) in the feedline?

Should the tuner be placed in the shack so the knobs can be adjusted without going outside? The answer will depend on individual circumstances. Automatic tuners are significantly more expensive. While placing the tuner at the antenna does reduce mismatch losses in the feedline, those losses may not be high enough to justify the cost of a remote tuner. See [What is the actual loss in a feed line with high SWR?](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md) Reducing the SWR on the feedline also reduces the peak voltage and current on the line and any components along it such as surge supressors, which may become a limiting factor when operating at high power.

And if it is possible to use a tuner to make a transmitter feed power into a coat hanger then why do we worry about making resonant antennas in the first place?

A coat hanger at HF would be a challenging antenna to match, since its extremely small length relative to wavelength would present such an extreme mismatch that most tuners would not be able to match it.

Resonant antennas are just one of many possible antenna designs. Not requiring a tuner reduces costs.

## Answer (score 3, by Mike Waters)

Simply put:

If it is mounted at the transmitter is it actually tuning the antenna itself?

No, it is *not* tuning the antenna. It just matches the resistance and reactance at the tuner end of the feedline to your transmitter.

Does it reduce the SWR in the feedline to a non-resonant antenna?

No, it does *not* change the VSWR on the feedline.

Should the tuner be placed at the antenna instead of at the transmitter in order to reduce SWR loss (heating) in the feedline?

Ideally, yes. However, that is usually not practical. It's often better to use a low-loss feedline.

300-ohm ladder line to a dipole requires a 4:1 balun to bring the impedance down

That **sometimes** works for one (maybe two) bands, but not if you want to cover 80-10.

My understanding is that the best resonant antennas have a high Q which means a very narrow bandwidth for which they are most effective.

*Not necessarily so.* A dipole with less Q and a wider bandwidth can be very effective indeed! One way of doing this is to replace a single wire with a "cage", greatly increasing the effective diameter of the element(s).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9044/what-is-an-antenna-tuner-why-bother-with-resonant-antennas-in-the-first-place, by SDsolar, Glenn W9IQ, Phil Frost - W8II, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
