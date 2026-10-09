# With solid-state equipment, when would one use a dummy load?

*Tags: dummy-load · score 3*

## Question

With vacuum-tube-based transmitters, you'd need to tune the output finals to achieve maximum power output, and this was commonly done into some sort of dummy load (either a purpose-made dummy load or something simple like a light bulb) while aiming for maximum power output on or near the desired operating frequency.

However, solid state equipment doesn't need the finals tuned to the operating frequency. On the other hand, they are much more sensitive to antenna impedance mismatches.

Seeing that antenna impedance mismatches are not caught or solved by first tuning into a dummy load, **in what situations is a dummy load useful with a purely solid-state transmitter** (where any external amplifier is considered part of the transmitter)?

## Accepted answer (score 6, by Dan KD2EE)

Any time you don't want to transmit RF. For example, if you have an oscilloscope and spectrum analyzer and would like to test the output of your transmitter (e.g. to make sure it's on frequency, that the waveform is OK and not getting cut off, that you don't have any spurious signals being transmitted) you might want to transmit into a dummy load rather than an antenna to prevent interfering with another transmittion and taking up bandwidth that you don't really need.

It can also be helpful to test your transmitter's power output in the absence of any SWR mismatch or reflected signal.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/394/with-solid-state-equipment-when-would-one-use-a-dummy-load, by user, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
