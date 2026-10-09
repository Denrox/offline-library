# I would like to listen to a red roadster in space

*Tags: satellites, swl, telemetry · score 5*

## Question

I have been listening for signals (any) of the Space-X Falcon Heavy. Just out of curiosity. And I am wondering if anyone has received any.

According to the Falcon-9 User Guide table 4.6 looks like this:

Although it mentions "Falcon launch vehicles" without further model specification, I am not 100% sure if the Falcon-Heavy frequencies are the same as the Falcon-9

Here are my questions:

- Has anyone found a frequency table/chart for the Falcon-Heavy? or confirmation that the Falcon-9 frequencies are applicable for the Falcon-Heavy?
- Has anyone received a signal which potentially is from the Falcon-Heavy? If you have, please describe your setup.
- What software (other than GNU radio) is capable of decoding the telemetry with PCM/FM encoding/modulation?

Meanwhile I will continue my quest using various search engines, and offcourse listening in...

My setup for this cheap-ish attempt is:

- Airspy SDR
- "Direct TV" down converter for 2.4GHz
- Wifi yagi 13dBi (I had nothing else in the 2.2GHz range)
- "tested" with a signal generator (from friend), this setup can receive 2.2GHz

## Answer (score 5, by tomnexus)

Good find of all the frequencies and powers, it sounds like you have all the right basic equipment.

But sadly for the roadster, you're too late, it's out of range. The video link is designed for a few hundred km, and it's probably half a million km away already.

Assuming the batteries on the spacecraft are still OK. It's transmitting 44 dBm. The path loss at 2221 MHz, 500,000 km (at time of writing, 10 km/s for 14 hours) will be something like 210 dB. A receiver with a 100 Kelvin system temperature and 3 MHz bandwidth has a background noise power of -114 dBm, and needs -100 dBm to achieve modest SNR. So you need a 66 dBi antenna, which is 100 m diameter. At 500 km the same equation yields 6 dBi, which you get from a little patch antenna.

There's nothing (technical) to stop you trying on the next launch. Legal... it depends where you live.

## Answer (score 2, by Mike Waters)

The batteries are now dead and there is no onboard power source, so we cannot listen to it. See the comments at https://space.stackexchange.com/questions/25010/current-position-of-starman

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9857/i-would-like-to-listen-to-a-red-roadster-in-space, by Edwin van Mierlo, tomnexus, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
