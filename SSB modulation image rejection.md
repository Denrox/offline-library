# SSB modulation image rejection

*Tags: ssb, transmitter, mixer · score 3*

## Question

I'm trying to figure out how SSB transmitters manage to get rid of the images created when mixing up audio frequencies. For example, when mixing a 1KHz signal with a 7MHz one you will end up with two signals, one at 7.001Mhz and one at 6.999Mhz. Creating a filter with such a narrow cutoff sounds infeasible so how is it done?

## Accepted answer (score 3, by jcoppens)

Well, there are two relatively simple methods and one slightly more complicated.

In the analog world, SSB signals are created in two ways: The filter method and and phasing method.


**The filter method** does just what you suggested - a very selective filter eliminates one sideband. Using piezoelectric crystals, filters can be made what can do that. Mostly between 4 and 12 MHz, combining crystals can form a nice filter that just passes the audio band (or so). As the frequency of the crystal filter is not easy to change, this is done at a fixed frequency (frequently 9 MHz) and the resulting SSB signal is then mixed up or down.


**The phasing method** is more difficult to explain, and needs some math to do it properly. Basically, both the RF and the audio signal are split into two parts, which are 90 degrees out-of-phase. Then one of the audio signals is modulated onto one of the RF signals to produce DSB (Double sideband). Same for the other audio/RD pair. Adding the two will eliminate one of the sidebands (subtracting eliminates the other one :)

**The more complicated way**, and which needs a fast processor, implements the phasing method purely by algorithms with both signals converted to digital. The phase shifting of the audio is accomplished with an algorithm called the Hilbert Transform, which creates two output signals with 90° phase shift.

The graphics are not too good here: http://www.daenotes.com/electronics/communication-system/ssb-transmission

This one's much better and mentions some of the math: http://www.dsprelated.com/showarticle/176.php

Here's the actual presentation of the phasing method. It's frequently called the 'third method' (It's old though - uses vacuum tubes :) : http://www.h4.dion.ne.jp/~ja5fp/weaver.pdf

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2159/ssb-modulation-image-rejection, by s3c, jcoppens. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
