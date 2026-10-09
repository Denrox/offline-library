# Remote SDR on the internet other than WebSDR?

*Tags: software-defined-radio, internet · score 10*

## Question

Besides WebSDR, what remote Software-Defined-Radio stations (for shortwave or amateur bands) might be available for open public access over the internet?

What protocols do these SDR stations use to stream data over the internet? Do any of these SDR stations use open source or published standard APIs for control and data?

## Answer (score 4, by JayC)

OpenWebRX is another way to monitor an SDR online.

http://sdr.hu/openwebrx

If you go to http://sdr.hu/ you can also see a list of receivers you can listen in to.

(As to your other questions, those might be better split out. These days there exist many ways to handle the needs of a remote monitoring client written for the browser. I would guess both WebSDR and OpenWebRX use WebSockets to constantly push data to the clients but other than that I'm not sure what you're asking.)

## Answer (score 4, by Wayne Hamilton)

The question specifies "SDR", but if all you want is to listen to signals in a distant location, you might try http://www.globaltuners.com/.

## Answer (score 4, by hotpaw2)

To answer my own question:

WebSDR seems to stream demodulated audio via using private (closed) API for control.

A couple other possible solutions for streaming remote SDR data over the internet include:

rtl_tcp : You can build your own remote SDR station with an RTL-SDR (or similar SDR) on a tiny server (Raspberry Pi 3, et.al.), and stream data over the network using the rtl_tcp protocol. See: https://github.com/steve-m/librtlsdr

OpenWebRX: http://sdr.hu/openwebrx

Cloud-SDR: http://www.cloud-sdr.com/

These all seem to use open protocols and/or open source software.

Added:

rsp_tcp is a rtl-tcp workalike for SDRPlay RSP receivers/devices.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2281/remote-sdr-on-the-internet-other-than-websdr, by hotpaw2, JayC, Wayne Hamilton. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
