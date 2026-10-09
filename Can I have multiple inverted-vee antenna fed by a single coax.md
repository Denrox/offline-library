# Can I have multiple inverted-vee antenna fed by a single coax?

*Tags: antenna, antenna-construction, inverted-vee, antenna-system · score 10*

## Question

A friend who recently received his call is planning to setup an inverted-vee for 40/20m bands. Our take is the signal will take the path of least impedance into the correct length antenna wire.

Something like the image attached; it depicts two wires running right next to each other. The tab in the middle of the wire marks the end of the 20M, the other tab marks the end of the 40M length.

- Can the antenna wires for both bands be fed at a common point by the coax?

## Accepted answer (score 8, by Walter Underwood K6WRU)

Yes, this works fine. It is often called a "fan dipole".

There are separate resonant dipoles for each band, all fed from a common point. The wires should be separated by a foot or more. If you have enough tie points at the ends, you can run them in slightly different directions.

The resonant dipole will have a low impedance, around 50 Ohms. The non-resonant one will have a higher impedance and will not accept much signal.

The antennas will interact with each other, so you may need to tune them to length iteratively. Most people start by adjusting the length of the longer antenna first.

The 40m antenna will also be close to resonance on 15m, so you can probably use it on that band with an antenna tuner.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/299/can-i-have-multiple-inverted-vee-antenna-fed-by-a-single-coax, by VU2NHW, Walter Underwood K6WRU. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
