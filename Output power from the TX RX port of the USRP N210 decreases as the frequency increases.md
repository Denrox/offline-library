# Output power from the TX/RX port of the USRP N210 decreases as the frequency increases

*Tags: antenna, rf-power, gnuradio, frequency, usrp · score 3*

## Question

I am trying to build an FMCW radar using a USRP N210 with a CBX40 daughterboard. I generate a sweep from 1.5GHz to 5GHz. According to their respective datasheets, the daughterboard and the USRP should work fine up to 6GHz. However, as the frequency increases, the output power from the TX/RX port decreases significantly, even though the transmitted power and gain are constant in GNURadio.

I attach a frequency domain graph of the received signal's power when connecting a wire between them. The wire could introduce some losses, but still the power decrease with frequency is very evident.

I would appreciate if you could tell me the reason why this is happening, and if you know the way to solve it.

Thanks in advance,

## Answer (score 8, by Marcus Müller)

That's an expected phenomenon: Real-world physical systems tend to be frequency-selective (i.e. not constant over frequency), and "at large scale" low-pass systems.

This applies to amplifiers, mixers, oscillators, and even transmission lines and connectors.

So that's normal.

Ettus even publishes exactly such measurements at https://files.ettus.com/performance_data/cbx/.

When you see a device that doesn't have such behaviour, there's either something very expensive going on – that's why high-end spectrum analyzers are way more expensive than USRPs – or someone measured this and then applied correction for that. Usually, it's a mix of both.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17485/output-power-from-the-tx-rx-port-of-the-usrp-n210-decreases-as-the-frequency-i, by Fati, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
