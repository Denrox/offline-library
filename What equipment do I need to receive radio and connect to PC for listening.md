# What equipment do I need to receive radio and connect to PC for listening

*Tags: software-defined-radio, digital-modes, computer-aided-transceiver · score 3*

## Question

A great many moons ago, I spent a 24 hour period with a HAM radio connected to a PC, and listening to transmissions from a massive number of sources.

Some of the transmissions included Morse, RTTY, SSTV with some plain audio as well... on the PC, I could scroll through a large number of frequencies, looking for interesting signals to listen in to, and potentially 'decode' using the PC to display appropriate output. The software would decode the transmission live, if I had it set to the correct option.

What would I need to do this now? I'd obviously need some kind of antenna and a method of connection, but this is where my knowledge fails. I've done some googling, but not knowing much about current technology, I don't know what is relevant or not.

To be clear, I'm looking for a receive ONLY setup, with minimal financial outlay.

## Accepted answer (score 4, by hotpaw2)

A generic search term you might use is “Software Defined Radio” or SDR (a topic which covers much more than your specific question).

Equipment possibilities for your specific question includes SDR hardware that covers the frequency bands of interest and that can be connected to your PC via USB or Ethernet, SDR software compatible with the specific SDR hardware device, plus a suitable antenna.

There are many SDR hardware products and vendors that cover a wide spread of performance levels and price points, from RTL-SDR USB dongles (for on the order of a couple dozen USD), to high-end SDR boxes (that cost thousands). Which to choose depends on more specifics about your requirements (budget, frequency bands supported, sensitivity, bandwidth, broadcast and image rejection, software options, and etc.).

Using a cheap RTL-SDR USB stick on HF requires either one that supports Q mode direct sampling, or an additional upconverter box. (Note that when paying “as little as possible”, to some degree you get what you pay for in terms of signal reception.). Other less cheap but common USB connected SDR boxes might include Airspy HF+, SDRPlay, HackRF, LimeSDR, and others. High-end SDR units might include ones from Ettus Research. (Hopefully updates and any of my omissions will be added to the comments below).

You will also need SDR software running on your PC. Many of the SDR hardware choices support multiple software application options for the PC (or Mac, or Linux/Raspberry Pi/etc., even iPhone, iPad, and Android devices) that supports the operation you describe. Some of the SDR software applications are freeware or open source. Some are not.

Some amateur radio HF rigs also include built-in capability, or allow attaching panadapters, or allow connecting to PC software via USB or stereo sound card, which may support similar functionality.

## Answer (score 2, by ON5MF Jurgen)

I agree with *hotpaw2* but there's an even cheaper solution. You can also use the many different webSDR's that are around the world. With those you only need an internet connection. These are some places to start:

- http://www.websdr.org/
- https://sdr.hu/

Google will give you a ton of extra possibilities.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12290/what-equipment-do-i-need-to-receive-radio-and-connect-to-pc-for-listening, by Stese, hotpaw2, ON5MF Jurgen. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
