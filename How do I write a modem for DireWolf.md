# How do I write a modem for DireWolf?

*Tags: packet, software-development, modem, direwolf, tnc · score 3*

## Question

I was looking at the selection of modem bauds for DireWolf and it seems the highest baud modem is 9600 baud, and I am using a sound card that can reach 48 khz. Is there any way that I can write a modem for DireWolf to utilize the 48 khz capabilities of the sound card?

## Accepted answer (score 4, by hobbs - KC2G)

Actually, direwolf already supports higher data rates since 2017; it will use the G3RUH modem for a speed of 9600 *or higher*. As shipped it can be configured up to 40000 bps.

But it's a mistake to think that 9600bps isn't making use of a 48kHz sample rate. The author has done some testing which shows that 9600bps is about the highest rate that works reliably with 48KHz (and in fact it benefits slightly from 96kHz); 14.4kbps and 19.2kbps require 96kHz sampling to work respectably, and higher rates require 192kHz.

You can, of course, attempt to write your own modem that performs better; I can't provide much advice on how to do it, except... do it. Look at demod_afsk.c (300 and 1200), demod_psk.c (2400 and 4800), and demod_9600.c (9600+), make your own with a corresponding set of public functions, wire it into demod.c and config.c, and give it a try. The included gen_packets and atest utilities will be helpful for testing.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18046/how-do-i-write-a-modem-for-direwolf, by Steve Mucci, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
