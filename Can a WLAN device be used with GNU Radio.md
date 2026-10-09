# Can a WLAN device be used with GNU Radio?

*Tags: software-defined-radio, gnuradio, wifi, linux · score 4*

## Question

Can I use my wireless ethernet card with GNU Radio? I have a Broadcom BCM4311 mini PCIe, and Debian / Kali 2.0 Linux.

## Accepted answer (score 3, by Kevin Reid AG6YO)

No. Most radio peripherals will not pass raw RF samples to or from the host computer, but only fully decoded packets. I'm not familiar with that particular card, but I'm sure if it had such capabilities people would be talking about it.

(The so-called “RTL-SDR” TV tuner device *does* have this mode of operation, which is why it is so popular for cheap SDR receiver applications.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5264/can-a-wlan-device-be-used-with-gnu-radio, by motoku, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
