# ISS APRS Digipeater with Kam XL and ICOM IC-910H

*Tags: aprs, icom · score 4*

## Question

I am trying to use the ISS APRS digipeater which transmits at 437.55MHz.

Hardware setup consists of the following

1. ICOM IC-910H.

The transceiver has been connected to a Windows PC running a HAM deluxe software package called Satellites. Basically, satellites tracks all spacecraft of known TLEs and perform doppler prediction. The output is then fed directly into the ICOM transceiver which has been set to "SATELLITE MODE". Analogue modulation is set to FM

1. Kantronics KAM XL TNC

I connected the TNC to my linux laptop via USB-to-serial adapter. I used the screen command the serial communication

sudo screen /dev/ttyUSB0 19200

In command mode I use the following settings

mycall XXXXXX

passall on, monitor on, mcon on, flow on,

paclen 70

axdelay plus txdelay >= 3

After I switched to converse mode (k) then I sent these simple messages and my location (not shown)

.> Hello ISS

:CQ :Hello ISS

Unfortunately neither my location nor my messages showed up on ariss.net . I captured the signal by using a Tektronix PC-based spectrum analyser and got the following

Each box is 6khz wide. This means that at -10dB, the bandwidth is around 12000Hz which is more than I expected. So here are my two questions

1.

Question 1:

I have verified that the 9600 bps mode is switched off on the ICOM. How come the signal is that wide?

2.

Question 2

Is the baud rate of my AFSK 1200 audio tones dictated by ICOM or by the TNC? If it is dictated by the TNC, then which command should I use to set it to 1200?

Thanks in advance.

## Accepted answer (score 1, by James NF8I)

The Kantronics KAM XL uses the HBAUD command to set the baud rate for the radio ports. HBAUD 1200/1200 will set the baud rate to 1200 on both ports.

Also, I don't see what you've set your UNPROTO destination to be. For the ISS digipeater, your messages need to be sent via ARISS to trigger the digipeater. For keyboard contacts, you would set UNPROTO CQ VIA ARISS

KAM manual: https://kantronics.com/wp-content/uploads/2018/10/KAM-XL-Manual-RevE.pdf

Info on ARISS packet usage: https://www.ariss.org/uploads/1/9/6/8/19681527/k9jkm_2012_symposium_ver2.pdf

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7199/iss-aprs-digipeater-with-kam-xl-and-icom-ic-910h, by Moses Browne Mwakyanjala, James NF8I. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
