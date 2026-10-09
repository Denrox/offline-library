# USRP Safe Gain Values

*Tags: gnuradio, rf-power, usrp, gain · score 3*

## Question

I am working with USRP N210 and USRP B200 radios with GNURadio. I have connected the TX/RX port of one radio to the RX2 port of the other with an RF cable as a simulated radio link. In GNURadio, I have been setting my transmitter gain and receiver gain to 10 dB in the UHD: USRP Source and Sink blocks.

I recently heard that when connecting my radios to a signal generator, I should set the output power to -10 dBm to protect the radios' RF front end components.

Have I been setting my gain too high / frying my radios? How high is too high? What gain settings should I use in my link mockup? If I connect to a signal generator or antenna link, what power attenuator should I use?

Thanks for any and all help!

## Accepted answer (score 3, by Marcus Müller)

I have connected the TX/RX port of one radio to the RX2 port of the other with an RF cable as a simulated radio link.

**DO NOT DO THAT.**

Always, always, always, in any case, under all circumstances, use an attenuator when directly connecting the output of one radio to the input of the other.

Have I been setting my gain too high / frying my radios?

Ettus specifies -15 dBm as the maximum damage-free input power for nearly all of their radio frontends, with the B200 being a bit of an exception and taking a couple dB more. Depending on the daughterboard in your N210, your frequency, sampling rates and of course the signal you're sending, the other radio might be producing up to 20 dBm. That's more than **2000 times** the damage-free maximum input power.

This is *damage-free*. Not *sensible input*; **stop what you're doing now, use an attenuator, there's no excuse**.

How high is too high? What gain settings should I use in my link mockup?

Depends on your N210 daughterboard, and the signal you're transmitting. On https://files.ettus.com/ you'll find *performance charts*, which give *very rough* output powers for a single tone signal at full amplitude given frequency and gain for the common daughterboards.

If I connect to a signal generator or antenna link, what power attenuator should I use?

There can't be no general answer to that, but the obvious one: enough attenuation to guarantee your input power stays solidly below -15 dBm.

## Answer (score 2, by Phil Frost - W8II)

According to the Ettus Research Knowledge Base:

The maximum input power for the B200/B210/B200mini/B205mini is 0 dBm.

and

Power Output >10dBm

10 dBm to 0 dBm is a difference of 10 dB, so an attenuator of *at least* 10 dB would be advisable.

More would probably be a good idea, since the specifications specify a minimum performance: transmitter output may be more than 10 dBm.

Furthermore, even 0 dBm is an extremely high power to receive in practice from an antenna. A lower input power is more realistic, and will likely result in better performance due to decreased nonlinear distortions.

If you like, you could [calculate path loss](What%20is%20a%20link%20budget%2C%20and%20how%20do%20I%20make%20one.md) for some situation of antennas, transmit power, and frequency, and introduce an attenuator of a similar value to what would be encountered in practice.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11594/usrp-safe-gain-values, by rytse, Marcus Müller, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
