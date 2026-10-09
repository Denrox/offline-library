# Do chokes at the antenna feedpoint stop the coax from receiving signals as well, or just transmitting?

*Tags: rfi, choke-balun · score 3*

## Question

It seems common knowledge that a choke at the antenna feedpoint stops the outside of the coax shield from radiating when transmitting into the antenna. But what about stopping the outside of the coax shield from picking up noise and sending it to the receiver? Will that feedpoint choke do anything in that case? Or does one need another choke at the receiver end as well?

## Accepted answer (score 6, by Phil Frost - W8II)

By the principle of reciprocity, if it works for transmit, it works for receive also.

Possibly if your receiver and transmitter are separate devices you may end up with a situation where no common-mode current was detectable on transmit, and yet common-mode signals did appear in the receiver. However with modern equipment having both receiver and transmitter in the same shielded enclosure, I don't expect this is likely to occur.

If you have any doubt, it should not be difficult to test. [How to detect common-mode currents or “RF in the shack”?](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md) describes a way to make a common-mode current detector with a clamp-on ferrite bead. Replacing the diode detector with an oscillator turns it into a common-mode current injector. You could then clamp this injector somewhere on the feedline and measure the received power, then repeat with it clamped around something on the other side of the choke.

The difference of these measurements will give you a rough estimate of the common-mode isolation. While none of this is calibrated and the measurement setup is also subject to all kinds of leakage paths which will skew the results, you then at least have some number which can demonstrate some improvement if the tests are repeated again after adding an additional choke, running the feedline underground, or undertaking any other measures to suppress or isolate common mode currents.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16997/do-chokes-at-the-antenna-feedpoint-stop-the-coax-from-receiving-signals-as-wel, by Paul, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
