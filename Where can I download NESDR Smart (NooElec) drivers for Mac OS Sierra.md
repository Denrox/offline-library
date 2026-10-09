# Where can I download NESDR Smart (NooElec) drivers for Mac OS Sierra?

*Tags: software-defined-radio, rtl-sdr · score 3*

## Question

Just bought this NESDR Smart USB dongle from Amazon in Canada. Wrote the company asking for drivers, but they sent links which didn't help. Anybody have a better place to download drivers for Mac OS Sierra? Thanks.

## Accepted answer (score 2, by Kevin Reid AG6YO)

Unlike Windows, **RTL-SDR on macOS (or Linux) does not require any separate driver installation.**

All applications bundle their own driver code (librtlsdr, often by way of gr-osmosdr and GNU Radio). All you need to do is install and run whichever SDR application(s) you wanted to run.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7305/where-can-i-download-nesdr-smart-nooelec-drivers-for-mac-os-sierra, by Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
