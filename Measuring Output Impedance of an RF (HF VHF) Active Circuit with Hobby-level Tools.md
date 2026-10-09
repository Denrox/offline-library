# Measuring Output Impedance of an RF (HF/VHF) Active Circuit with Hobby-level Tools

*Tags: impedance · score 5*

## Question

Is there a simple (by simple, I mean a hobby friendly method that trades some accuracy for expense) method of measuring the "actual" output impedance of an active or "hot" RF (HF to VHF) circuit?

As an amateur radio enthusiast, I often find myself in a situation where I'd like to measure the actual output impedance of some amplifier or oscillator (type of amplifier). Right now, I have an oscillator operating in the low VHF region and I'd like to match its output to a mixer that has a well defined input impedance. But that's just one example, I've had plenty others in the past. I can calculate the output impedance theoretically, but it would be nice to confirm the theory with a practical measurement.

I have some hobby or entry grade tools to hand, including an oscilloscope and a NanoVNA. Is there a reasonably accurate measurement method using these tools? One that doesn't damage the measurement device (especially the VNA).

One I read somewhere that made some kind of sense was to match the output with a (passive) device that varied the resistance, inductance and capacitance (a type of complex load). You could use a power meter to find the match point. Then measure the input impedance of the device/load with a VNA and use the conjugate as the output impedance.

Sounds simple enough, but I'm guessing the devil is in the construction of the complex load. What other methods are there?

**UPDATE:** Since asking this on EE SE, I've solved my immediate problem by using the two measurement technique (wonderfully explained in this video by W2AEW). However, I believe this approach becomes less accurate at RF frequencies and I have a continuing interest in discovering a practical, simple and inexpensive solution - if it exists!?

## Answer (score 2, by Brian K1LI)

According to *Microwaves101*, the "load pull" technique may fulfill your need:

Load pull involves varying the load impedance presented to a device under test and monitoring a single or set of performance parameters. When used in conjunction with a signal source and signal analyzer (spectrum analyzer, power meter, vector receiver…), load pull can be used to measure parameters such as output power, gain, and efficiency as a function of load impedance presented to the DUT.

Relying on the maximum power theorem, the load will see maximum power when it represents a "conjugate match" to the source. Matching the output of your circuit to a known load value using an SWR meter would allow you to "back out" the impedance of the generator. At UHF and above, the lumped matching network you would use at HF and, probably, VHF is replaced by a transmission-line based "microwave impedance tuner."

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16857/measuring-output-impedance-of-an-rf-hf-vhf-active-circuit-with-hobby-level-too, by Buck8pe, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
