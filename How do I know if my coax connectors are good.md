# How do I know if my coax connectors are good?

*Tags: coaxial-cable, connectors, pl259-so239-connector · score 4*

## Question

In installed a couple of compression style PL-259 connectors to the ends of RG8/U FOAM coax. It's about 16 feet in length. Here is an example of one of the connectors:

How do I know if the coax is "good"? The multi-meter test for shorts doesn't seem like it's a complete test. It lets you know for sure if there's a problem when there's a short. But it doesn't necessarily tell you everything is good when there's an open.

I used my NanoVNA to perform a sweep on the cable with the 50 ohm load at the end. The VSWR and RL tends to go up and down from 1MHz to 500MHz. Is this normal?

Other than those sweeps, is there any kind of "red light; green light" test to make sure a piece of coax and the connectors are good?

## Answer (score 4, by Marcus Müller)

So, what your measurement indicates is two things:

1. yep, the thing is somehow connected. The deep dips in the return loss are points when the characteristic impedance of the connector+cable+connector+termination look like the source impedance of the VNA
2. yep, it's a terrible non-constant complex impedance seen from the perspective of the VNA that's everything but 50 Ω. A "good" cable starts at a return loss of -20 dB, but typically, general-purpose pre-configured coax cabling has more like -30 dB to -50 dB of loss. Your connector reflects power, and pretty strongly so! That's no surprise: In the 1930s, it was designed as a *cheap* connector for frequencies below 100 MHz, mostly for low power systems. It doesn't have a constant (or even defined) impedance and thus no general guarantees about its performance [can be made](PL-259%20SO-239%20vs%20N%20Type%20vs%20BNC%20which%20is%20best%20connector%20to%20use%20when.md). The tolerances of the connectors, and the lack of mechanical design specification, in fact *force* the connector to be bad: there's no way to produce a connector that has constant characteristic impedance over a significant range of frequencies with arbitrary counterparts.

So, sorry, I can't tell you based on these measurement if that cable is "as good as it can be". I can tell you, however, that you really can't *rely* on PL-259 for UHF (even if it's called "UHF connector"; UHF meant > 30 MHz back when it was invented). You might find one PL-259 jack that works beautifully up to 400 MHz with a given PL-259 connector, and another one that looks like your measurements or even worse.

Really, if you can: replace PL-259 with BNC or Type-N or SMA.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17096/how-do-i-know-if-my-coax-connectors-are-good, by Paul, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
