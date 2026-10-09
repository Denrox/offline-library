# Output impedance of TAPR QRPi?

*Tags: impedance-matching, qrp, wspr · score 3*

## Question

I'm a newly licensed amateur and have decided to start out by trying WSPR on a Raspberry Pi equipped with TAPR's 20m QRPi. The QRPi write-ups I've read always talk about long wire antennas but I'd like to try to connect it to my Elecraft AX1. But I can't, for the life of me, find anything that specifies the output impedance of the QRPi. I'm assuming that some sort of matching will be required, for best results.

Does anybody know what the QRPi's output impedance is? If I must measure it myself, would my "Nano VNA" be of any use?

## Accepted answer (score 5, by Phil Frost - W8II)

The output impedance isn't especially important: in fact I believe it uses a nonlinear amplifier so the concept doesn't really apply.

What does matter is the intended load impedance, which for any amateur radio application you can assume to be 50 ohms unless otherwise specified.

To verify, I modelled the low-pass filter part of the circuit from the manual:

Running a frequency domain analysis we can see this provides a nice low-pass response with a cutoff just above the 20m band, with a pretty flat passband except for some minor ripple we can expect inherent to the Chebyshev design and rounding errors in selecting common values for the components:

If the load impedance is changed to 5,000 ohms, the response no longer looks so nice:

Of course you aren't actually going to get an additional 40 dB of output power where the frequency response spikes because the real circuit isn't built of ideal components, but what this tells us is the person designing that filter assumed the attached load would be about 50 ohms.

What happens if the load isn't 50 ohms is somewhat undefined. It could be fine. It could just make less power. Or it overstress the transistor and damage it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15393/output-impedance-of-tapr-qrpi, by Bezewy, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
