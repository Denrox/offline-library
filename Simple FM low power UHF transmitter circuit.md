# Simple FM low power UHF transmitter circuit

*Tags: diy, transceiver · score 3*

## Question

I want to build an low power transceiver on 33cm or 23cm (or 2 meters, but not recommended because of all the other activity interfering with my stuff) I would like to use FM and just have enough power for the nearby block to receive, kind of like a FRS radio but maybe even less power.

Are there any very simple circuits out there that will allow me to do this? I am thinking something really simple like the micro power FM broadcast transmitters. I would like to be able to fit it into something close to handheld and the reason I don't want to use 70cm is because my half-duplex AllStar repeater link will cause desensitization on that band.

I will link this up with a Simplex AllStar node so I can transceive around the house.

## Answer (score 3, by Chris 2M0FFY)

Microwave design is often far from simple, since stuff starts to behave significantly differently from how it would at HF or even VHF. Parasitics and the like become a serious problem.

That said, there are two designs I know of off the top of my head:

There's this one based on the MAX2750 VCO. You'd need to vary the input into TUNE with the audio output, and you would get an frequency-modulated signal out of K1. It's for 13 cm though; I believe Maxim make an alternative part for the 23 cm band as well.

There's also PE1JPD's design which, while more complex, is a complete transceiver, and about as simple in terms of two-way communications at 1 GHz as you're going to get.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3639/simple-fm-low-power-uhf-transmitter-circuit, by Skyler 440, Chris 2M0FFY. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
