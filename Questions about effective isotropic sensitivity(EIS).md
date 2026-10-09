# Questions about effective isotropic sensitivity(EIS)

*Tags: antenna, antenna-theory, measurement, jargon · score 3*

## Question

Recently, I read something about **EIS (effective isotropic sensitivity)** and **TIS (total isotropic sensitivity).** I'm trying to understand the concept, but I find it's quite hard for me.

In the book ***Antenna Design for Mobile Devices***, there is a vague definition, which is

**EIS** and **TIS** are analogous to **EIRP** and **TRP**. The **EIS** test method is similar to the **EIRP** method; in that, the range reference measurement is used to correct the unknown performance of a device back to values relative to that of a theoretical isotropic receiver.

For **EIRP**, I can understand it can also be thought of as the amount of power a perfectly isotropic antenna would need to radiate to achieve the measured value.

However, for **EIS**, I don't know how to connect it with the performance of an isotropic receive antenna. And what does this term actually define? Does it define the minimum input power of the antenna?

## Accepted answer (score 3, by Phil Frost - W8II)

If you were designing a link budget, EIS is the minimum power required at the receiver, assuming the receiver is an ideal isotropic receiver. The EIS encapsulates the effects of both the receiver's sensitivity and antenna system.

A link budget might look like this:

1. transmitter power
2. +/- adjustment due to antenna mismatch
3. - transmitter feedline loss
4. + transmitter antenna gain
5. - path loss
6. + margin for interference, fading
7. + receiver antenna gain
8. - receiver feedline loss
9. + margin for self-interference, antenna efficiency, and other practical details
10. >= receiver sensitivity

The objective is to ensure the final sum (item 10) is at least the receiver's sensitivity, otherwise the BER will be too high and communication unreliable.

But all this detail in the link budget can be complicated, so EIRP and EIS exist to simplify the parts specific to the radios and the antennas.

EIRP encapsulates items 1 through 4. Essentially, EIRP tells you how much power is actually radiated from the transmitter, including all the details of the antenna and how that antenna interacts with the transmitter.

Similarly, EIS encapsulates items 7 through 10, including everything about the receiver's antenna, the receiver's sensitivity, and all the details about how that antenna actually interfaces with that receiver.

So if you know EIRP and EIS, the link budget calculation simplifies to:

1. EIRP
2. - path loss
3. + margin for interference, fading
4. >= EIS

EIS (like EIRP) applies to only a single direction and polarization. If that's not specified, then it's the "best" direction possible. That is, the minimum EIS over all possible directions and polarizations. Which is probably (but not necessarily) the direction of maximum antenna gain.

EIS might seem a little silly, if it's just sensitivity + antenna gain - feedline loss. But it also incorporates subtle details that might otherwise escape attention.

For example, the receiver generates some amount of noise which will be picked up by its own antenna, raising the noise floor and degrading sensitivity. A simple measurement of receiver sensitivity, which involves applying a test signal directly to the receiver module's terminals, would not account for this effect because there is no antenna to receive noise from the receiver (and whatever device it may be a part of).

Or, the presence of the receiver module or the feed arrangement may unintentionally alter the antenna's radiation pattern.

In other words, receiver sensitivity and antenna gain are idealized numbers, whereas EIS represents the actual performance of the combination which may be less.

To measure EIS, a test signal source is set up to produce a known signal. The field intensity is measured at the position where the device under test (DUT, which will be a receiver and its antenna) will be located. From this field intensity, the power that would be received by an ideal isotropic receiver is calculated.

Let's say that's calculated to be -60dBm. The DUT is put in position, the test signal transmitted, and the bit error rate (BER) calculated. If the BER is above the specified threshold, the power is reduced in increments, -61 dBm, -62 dBm, etc. until the BER falls below the threshold.

The EIS is the minimum such power where the BER is still above the threshold.

Because the EIS is measured with an actual receiver and antenna combination in an anechoic chamber, it will represent the full and actual performance of that particular combination of devices.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17029/questions-about-effective-isotropic-sensitivity-eis, by tyrela, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
