# calculating power from directional coupler

*Tags: rf-power, directional-coupler · score 3*

## Question

I've designed an pulsed RF generator (50-100 MHz) and am using a directional coupler to measure power into a 50 ohm dummy load. The forward power from the coupler is plugged into a o-scope (hi Z input). The issue is that I calculate what seems to be too much power (more than expected) that, while possible, I doubt.

My calculation is as follows: on scope I see 100 mV RMS, so this calculates as (0.1 V)(0.1 V)/(50 ohms) = 0.2 mW. Since the coupler constant is 60 dB, this means the mainline power is (0.2)(1e6) = 200 W. This seems high as the cw power during design was 100 W, although the 10% duty cycle certainly could enable 200 W during the pulses. Does this seem correct?

Also of note: the coupler (an older Werlatone, no longer manufactured) is rated for 5 kW. Could my measurements be caused by not reaching some threshold (using too little of coupler's range)? Also I checked the forward-power port resistance using a DVM and got 19 ohms, which I cannot make any sense of- expected short, open, or 50 ohms for this DC measurement. Any thoughts/comments appreciated!

## Answer (score 3, by Phil Frost - W8II)

A directional coupler only works if the coupled port or ports are terminated in the characteristic impedance, usually 50 ohms. Otherwise it's not able to accurately distinguish between forward and reflected power. This is apparent from the math governing its operation.

If your scope has a 50 ohm termination option, use that and run coax directly into the scope. Don't use a probe at all.

If your scope has no such feature, put a T and a 50 ohm terminator at the scope, like so:

This works well until you get into high UHF, where the physical size of the T becomes an appreciable fraction of wavelength.

Note my directional coupler is bidirectional, so I've taken care to terminate the unused reflected port as well.

Just be sure the power isn't too high to damage the scope. With a 60 dB coupling factor this is unlikely.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7724/calculating-power-from-directional-coupler, by Tom DeQuincey, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
