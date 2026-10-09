# Is it possible to generate rf by directly programming a pc parallel port?

*Tags: transmitter, software-development · score 3*

## Question

From what info I've found, it seems a pc parport has a max speed of ~2meg /sec ?

So transmission on medium wave, to ~160 meters should be possible ?

With antenna than possibly a small wire, I would think transmission range would only be a few feet at best ?

However, I've also found info to suggest that trying to program the port under any non real time os is going to yield only a few hundred Khz at best.

If so, I'm thinking maybe a custom boot program that might be the solution ?

I've found a few examples of RF / AM, FM transmitting using microcontrollers, and I then wondered if a PC could do something similar with either the parallel, USB or serial ports for either medium wave or ham frequencies.

Serial looks too slow, and USB not doable without some kind of USB dev board / custom device, so that leaves the parallel port.

## Answer (score 3, by Edwin van Mierlo)

"Is it possible to generate rf by directly programming a pc parallel port?"

Yes, you can.

In fact any "alternating current" will produce RF, and a "port" (parrallel or other) from a "computer" can do this...

but... (there is always one, isn't there?)

You will have to ensure that you are filtering intermodulation, harmonic's and so on so forth, before the signal will be clean enough to amplify and transmit.

You don't have to re-invent the wheel either; an article was written on how to transmit FM (and other modes) using a Raspberry-Pi, here: http://www.rtl-sdr.com/transmitting-fm-am-ssb-sstv-and-fsq-with-just-a-raspberry-pi/

This is not taking away the requirement of filtering, but fear not; someone thought of that as well, see here: http://shop.languagespy.com/products/pi-tx-transmitter-kit-for-the-raspberry-pi?variant=11348563589

Disclaimer: I have no affiliation with either product/shop/site, and I have not personally used either product; so the obligatory "YMMV" applies.

HTH.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6079/is-it-possible-to-generate-rf-by-directly-programming-a-pc-parallel-port, by mstram, Edwin van Mierlo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
