# If the data port on a Yaesu FT-7800R only communicates FM signals, why does the manual mention the port having a bit rate?

*Tags: bandwidth, packet · score 3*

## Question

I was wondering how the Radio interfaced with a TNC. I thought the computer sent digital data (in a serial format) to the data port on the radio, but from what I read online, it is **not** a data port.  
From http://www.wa8lmf.net/6-Pin-MiniDin-Data-Connector/index.htm

This jack is variously called "data", "packet", "auxiliary", etc, but actually there are no data connections on this connector. This IS NOT a serial data or RTTY direct FSK port. Only various forms of receive and transmit audio are present. The connector provides receive audio output at a fixed level of about 100-300mV, transmit audio input at about the same level, transmit PTT keying, receiver squelch status (COR), and ground/common.

But on the yaesu's manual, it mentions about packet data rates. So if the signal received by the radio over the data port is good ol' FM, how can it have a bit rate?

## Accepted answer (score 5, by Phil Frost - W8II)

The data port does not carry FM signals: it carries demodulated audio. The radio performs FM demodulation and de-emphasis, and the output is heard on the speaker and is also present on the 1200 baud data output. On most multi-mode radios this port caries the demodulated audio for other mode selections as well.

The data input is similar, but in reverse. The only difference from the microphone input is the level.

The 9600 baud data output is similar, but bypasses the de-emphasis.

These connections are named "1200 baud" or "9600 baud" because they were first developed to interface to a 1200 or 9600 baud TNC. The convention has stuck, even after other uses for these ports have been developed.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17059/if-the-data-port-on-a-yaesu-ft-7800r-only-communicates-fm-signals-why-does-the, by rsn, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
