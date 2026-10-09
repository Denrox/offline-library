# What is a simple kind of amateur radio transceiver I could try to build, as a beginner?

*Tags: diy, transceiver, equipment-design, equipment · score 3*

## Question

I am new to amateur radio, and I'm trying to learn the basics of the hobby.

I would like to build a simple radio transceiver from scratch (i.e. not from a kit).

I have searched the Internet for references, but most of them seem complicated and costly.

So what is the best kind of radio to look at building? From my searches I found that many people are recommending *QRP* radios. But even in that area of the hobby there are many variants.

## Accepted answer (score 1, by Zeiss Ikon)

Assuming you want to build from a kit, the simplest kits will be those that use a minimum number of components, avoid having to wind coils, and have only through-hole component mounts. On that basis, and from my own recent experience building one, I'd recommend a Cricket (QRP CW transceiver, includes a built-in key).

The Cricket series (they've been available at various times on 80, 40, 30, and 20m bands) have the inductors etched directly on the circuit board, so you don't have to wind coils or mount toroids. They're crystal controlled, using a common crystal type that's readily available. They put out roughly 1W on a fresh 9V battery. Mine took just about two hours to assemble, taking my time and working one component at a time.

The instructions are very good, almost Heathkit quality (individual check boxes for each component), though not perfect (they left out the step of actually installing the crystal, for instance). There's an option to install a connector in place of the simple key to use an external key or keyer.

I haven't been able to try mine on the air, yet (I don't have an antenna -- need a BNC connector and some coax to connect to the wire I have), but the tests I can make with a frequency counter seem to indicate it's working.

However: For a beginner to build a radio (transmitter/receiver or combined transceiver) from scratch without already knowing how they work is hardly different from building a kit, except with poorer odds of success. Build kits (plural/multiple) first, learn how they work, then build a radio from scratch.

## Answer (score 4, by Scott Earle)

You say you are "not supposed to build with a kit". Who has set this limitation? This is beginning to sound like a homework assignment.

Are you actually expected to design and build a radio receiver and transmitter without looking at other people's prior work? And on top of this, you say in another question that you do not have an amateur radio licence, which means that while you can build and test a radio receiver (and use it on the air to make sure it works as expected), you would not be able to test a transmitter, outside of connecting it to a dummy load and making sure that no radio waves are actually transmitted.

My recommendation would be to get an amateur radio licence, and use the knowledge that you gain from that process to design a simple transmitter first. You only need to transmit a few milliwatts, to show a proof of concept. (Internally, this is what all commercial transmitters do - generate the signal at a very low level, then put it through a preamplifier and a final power amplifier [PA] stage).

I recommend building a transmitter first, simply because it is **much** easier to build a CW transmitter (that you would use to transmit Morse code) than it is to build even a simple receiver - a transmitter is basically an oscillator with a buffer, and some cleverness so it does not drift in a range of input voltage conditions. It can be a single frequency using a crystal for stability to start with, and you could later replace it with a VFO (a *variable frequency oscillator*).

Building a receiver would be slightly more complicated, unless you wanted to try a TRF (Tuned Radio Frequency) receiver to receive AM. Unfortunately, receiving CW or SSB is a little more complicated, as they require mixers and the like. But again - build something simple first, and work your way up to something more usable.

Limiting yourself to not using a kit really does make it more tricky, but if this is an assignment then you have to work within those parameters. If you really **can't** use a kit, then how about looking at the circuit diagram of a kit, and see if you can redesign it slightly to fit your purposes. Technically it's probably cheating, but it could be argued that asking a load of people on the internet is cheating as well, so ...

**EDIT:** I noticed on your profile that you are a keen programmer. Another aspect of amateur radio that is becoming more popular, and now has mainstream hardware available, is that of the Software Defined Radio (SDR).

There are several commercially-built amateur radio transceiverss that have a traditional user interface (knobs and buttons), but underneath they are pure software. Good examples are the Icon IC-7300 and the Icom IC-7610. These radios are extremely popular, largely because of the flexibility that an SDR can provide, but still having a 'traditional' user interface.

Building SDR receivers is so trivially simple, with such inexpensive parts, that I would recommend that you have a look at some of these just to see if there is anything you can learn from them. Transmitters are not horribly complicated, but there is a lot to do about filtering that would need some care.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13316/what-is-a-simple-kind-of-amateur-radio-transceiver-i-could-try-to-build-as-a-b, by Sumithran, Zeiss Ikon, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
