# Can one send data over Short-wave frequencies?

*Tags: mf, lf · score 4*

## Question

I have an inkling of an idea- a modem system communicating over Short-wave. I know that WiMAX already exists, but the difference is that, while WiMAX works on the Gigahertz frequencies, and most concepts for Ham Radio ones think Megahertz frequencies would be ideal, My idea was to make it work on kilohertz, AM, possibly even long-wave frequencies (3Mhz-150KHz). The only thing I have to go on is a Bell 103 300-Baud time code broadcasting from CHU every day.

My question is, can you send Modem signals of a higher quality & baud rate(1200 Baud?) over regular Short-wave and AM broadcast frequencies? If so, how would it work? Is it even legal? Practical? could it be two way?

## Answer (score 9, by rclocher3)

Modern digital systems communicating over HF (aka short-wave) are legal in the US and practical, and in fact one such system is in routine daily use. Have a look at the Winlink system. (The official web site is here, but the Wikipedia article provides a better general overview.) It uses the PACTOR and WINMOR modes. Winlink messages are formatted as email; the Winlink system is connected to the internet (when the internet works), and a Winlink user can choose to send and receive messages via HF, VHF/UHF, or internet. Because Winlink messages may be sent over a low-bandwidth connection, messages should be short; small attachments are allowed. Winlink is an excellent tool for emergency communications, and is also often used by mariners at sea. (An amateur radio license is required.)

Digital communication on the HF bands is inherently more difficult than on VHF, UHF, and higher bands, due to noise, fading, and many other issues; the bit rate varies according to the signal-to-noise ratio. The newer versions of PACTOR offer better performance than WINMOR, but those newer PACTOR modes require an expensive terminal node controller (TNC), whereas WINMOR is free and implemented in software.

By the way, digital modes are legal in the US and other countries on the 160m band, which is close to the AM broadcast band and is considered a medium-frequency (MF) band. But the noise on 160m is generally much higher than on any HF band, so 160m is not generally used for Winlink.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6146/can-one-send-data-over-short-wave-frequencies, by Rory Yammomoto, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
