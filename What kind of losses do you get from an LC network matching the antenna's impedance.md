# What kind of losses do you get from an LC network matching the antenna's impedance?

*Tags: impedance-matching · score 4*

## Question

If you have a transmitter that is perfectly on your frequency but you have an antenna with some impedance what types of losses, and of what magnitude, will you expect from a tuner in between your transmitter and antenna?

For example lets say your system as a whole with no tuner has an SWR of 3 and your system with a tuner is now 1:1. Are there power losses from an LC network used to match impedances?

What are these losses called? Is it easy to calculate wasted power? Is it frequency dependant? Is there a way to approximate delivered power from a given capacitance and inductance on a line with a specific SWR?

## Accepted answer (score 0, by Kevin Reid AG6YO)

An ideal LC network causes no losses whatsoever, because ideal inductors and capacitors do not dissipate power — they have no resistance. The actual loss in your matching network is determined by the actual resistances of the components. It is frequency-dependent because the overall behavior of the network is, and it is also *power*-dependent due to saturation of inductors' magnetic cores (unless your inductors are air-core).

The other major source of loss in this type of configuration is [the loss due to standing waves in the feed line](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md) between the antenna and tuner (just as if you were not using a tuner). This is why tuners are best placed near the antenna rather than the transmitter.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7329/what-kind-of-losses-do-you-get-from-an-lc-network-matching-the-antenna-s-imped, by Joshua Katz, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
