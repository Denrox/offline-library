# Using a Return Loss Bridge and Nano VNA to measure amplifier characteristics

*Tags: amplifier, measurement, testing, nanovna, vna · score 5*

## Question

One of the difficulties of measuring active devices like LNA and IF amplifiers with the Nano VNA is the care needed to avoid over-driving the amplifier input and, more importantly perhaps, to avoid blowing up the CH1 port during S21 (gain) measurements.

A common approach to avoid these problems is to place attenuation on both the input (CH0) and amplifier output into CH1. This seems reasonable and I'm sure it'll work just fine, although I haven't tried it myself (yet).

However, I recently purchased a low-cost Return Loss Bridge from a vendor in the Ukraine (see image below) and I was wondering if I could press it into action to help measure amplifiers.

While browsing for information about this subject, I came across an interesting thread (Nano VNA Forum Thread). About halfway down this thread a user makes the following comment:

This is a tricky case as the power out can overload the device.

The solution I use is attenuate the output, run S21 and use an external return loss bridge with an amplifier on the return port to the channel 1 input. With known gains and attenuation its easy to get return loss, input impedance, and then input SWR

Same methods used for receiver inputs, with care to insure the input is below overload.

It's an old thread, so I can't ask the OP for clarification but I'm hoping someone more knowledgeable than I am can parse this comment and help me understand how the RLB is helping in this situation.

Some of the questions I would have are:

**What does the layout look like? What are the connections?** When he says: "attenuate the output" does he mean the output of the VNA (i.e., CH0) or the amp? What exactly is the "return port" of the RLB?

**What exactly can you measure with this technique?** Can you measure gain, for example?

**Is this external RLB method superior to using the attenuation method? Why so?**

Thankyou!

## Answer (score 4, by Dave Johnson)

The quoted poster in the linked thread is suggesting to use an external reflection bridge but it is confusing why. The NanoVNA has a built-in directional coupler on Ch0 with maximum 0dbm output (and input), and 0dbm maximum input on Ch1 for S21 measurements. With these known limits, combined with the expected characteristics of your LNA, you can simply add the appropriate attenuators to the Ch0 and Ch1 connectors and dispense with the external reflection bridge and the extra processes and pitfalls required to calibrate the unknown thru characteristics of the bridge altogether.

Regarding the functional use of the reflection bridge, this is a topic not thoroughly capable of being answered here as it is a manual-filling topic since the device requires various connection patterns during the process (calibration, bridge insertion loss measurement, reference calibration, DUT measurement, etc).

Yes, you can measure gain, but only after fully characterizing the bridge (unknown through) and with it comes additional pitfalls. It is a good exercise to attempt, for educational purposes, but it is certainly a process and not a simple "connect like this and measure" answer.

The reflection bridge measurement method will not offer superior results than using the built-in directional coupler of the NanoVNA for characterizing your simple LNA. However, a reflection bridge can offer additional features that a simple directional coupler does not. For example, with a theoretically perfect reflection bridge, you can characterize devices designed for any impedance such as 75-ohm, or dynamic devices that have changing impedance via feedback through the reference port on the bridge, but these are rare cases in the amateur RF hobby and if you require such measurements, you likely require much higher sensitivity or frequency range than the NanoVNA can provide (e.g. in designing a PCIe Gen4 retimer, PCIe Bifurcation Switch etc).

Regardless, using the NanoVNA as designed with internal directional coupler (which I believe you refer to as *the attenuator method*), the physical connections are as:

- Ch0 (S1) =>
- => [Attenuator to protect LNA input] =>
- => [LNA] =>
- => [Attenuator to protect Ch1 input] =>
- => Ch1 (S2)

VNA should be set to measure S21 (through) and calibrated with both attenuators. Attenuators must be chosen accordingly so that Ch0, Ch1, and LNA power limits are honored.

An optional additional would be DC-blocks in series with each attenuator, especially if testing hyper-cost-optimized LNAs that do not include DC blocking capacitors on the i/o ports.

The following links provide additional information relevant to the exercise of calibrating and using your bridge to perform the same attenuated S21 NanoVNA measurements (arguably outside the scope of a Stack Exchange "answer"):

- QSL newsletter Build a Return Loss Bridge
- *Filter Measurement* (pp63-65) of the Absolute Beginners Guide to the NanoVNA
- Agilent Technologies application note AN 1287-6 Using a Network Analyzer to Characterize High-Power Components
- Agilent Technologies application note AN 1287-3 Applying Error Correction to Network Analyzer Measurements
- Agilent application note M6-1, 2006 Advanced Calibration Techniques for Vector Network Analyzers
- Building a reflection bridge project in The A.R.R.L. Handbook

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18732/using-a-return-loss-bridge-and-nano-vna-to-measure-amplifier-characteristics, by Buck8pe, Dave Johnson. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
