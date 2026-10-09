# Testing for 'Bad' Coax

*Tags: diy, coaxial-cable, testing · score 6*

## Question

I have a lot of 'donated' coax that has been given to me with unknown provenance. I'm wondering what things I can do that can determine whether I keep it or send to the tip? Some of the things I have thought about doing are:

- Physical inspection - look for oxidisation of shielding braid, damage to plastic sheath
- Continuity testing, short circuits between inner and outer.
- plug into dummy load and do an SWR sweep
- Measure cable loss and compare against specifications

The big one is cable loss - Any thoughts on how I can measure that cheaply? I don't have any calibrated test equipment for that?

Any other tests I should think about?

## Accepted answer (score 6, by Mike Waters)

You're on the right track with the first items in your list. Assuming that you have a wattmeter and a dummy load that both match the impedance of the coax, it's a simple matter to measure the loss.

Measure the power with the wattmeter at the source, and then measure it again at the load. The difference between the two wattmeter readings is your loss.

$$N_{dB} = 10\log_{10}\left(\frac{P_2}{P_1}\right)$$

Note that this technique depends on the calibration of the wattmeter, and does not itself detect if the coax has damage leading to reflection rather than dissipation (you would want to verify the SWR is as good as without the coax, before assuming the watt figures are good).

## Answer (score 4, by Phil Frost - W8II)

A cursory physical inspection and an SWR sweep are usually sufficient.

Blatant physical damage, like internal shorts or breaks in continuity, will be found by the SWR sweep. So in your physical inspection you're looking for things which might not impact the SWR, like outer insulation that's cut or damaged which may eventually lead to water ingress.

You could measure loss, but I can't think of any likely mechanisms of loss that wouldn't also lead to anomalies on the SWR sweep, so I wouldn't worry about it too much.

In my experience, the problems with salvaged coax are most usually the connectors. Hams are notorious for buying cheap connectors and then installing them incorrectly. I'll wiggle the connections while the SWR sweep is running: any mechanical issues will show up as extreme spikes in the SWR. If the connectors are at all questionable I'll install new ones, and this also affords an opportunity to inspect the conductors for oxidization, an indicator of water ingress.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12285/testing-for-bad-coax, by Ben Short, Mike Waters, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
