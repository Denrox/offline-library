# Demodulation based on external frequency source

*Tags: equipment-design · score 5*

## Question

I saw a design for a walkie talkie that used a mixer that mixed the TX freq to the RX path before demod. Looking at the SA616 chip, demod is acomplished by Gilbert cell quadrature detector that is downstream from this.

The simplest FM detector is a phase locked loop but the issue is that injection of the TX frequency at the demod stage rather than the mixer stage in this case I cannot do.

I want to use the TX frequency to demodulate the on incoming signal, thus reducing the complex circuitry.

My first inclination is to go with the SA616 offered by NXP but I cannot inject the TX frequency. If I go the PLL route I need to somehow translate the frequency to an equivalent resistance in order to control the VCO that resides with in the Phase locked loop.

Im trying to work with 1.8Mhz to 222Mhz band ranges.

Relevent datasheet

https://www.nxp.com/part/SA616BS#/

Am I doing something wrong or am I overthinking things?

Here is a diagram

## Answer (score 3, by Scott Earle)

One of the problems with a superheterodyne design is you need two frequency generators: one for Tx that operates at the intended Tx frequency, and one that operates at (the intended Rx frequency plus-or-minus the IF).

As suggested by Brian K1LI in the comments, if you take the received signal and mix it with the intended receive frequency, you end up with ‘baseband’ out, and you just made a direct-conversion receiver. This can be made to work, but it’s probably trickier at FM than it is for AM or even SSB (it would be a nightmare for CW!).

So I am confused as to why you would have a superheterodyne receiver design and then skip the IF altogether.

EDIT:

As I added in my comment below, I now understand that you actually are asking about how to bypass the whole idea of using an IF, thus creating a direct conversion receiver.

I’m not saying that this is a bad idea in itself, but if you read about the history of radio, you will see that the direct-conversion receiver was one of the earliest receiver designs, followed by the regenerative receiver. After that came the superheterodyne receiver, and then that became the standard for about a century.

While I’m not trying to discourage you from your design (it would be interesting to see how well it performs), I would take a lesson from history and have a look at *why* the superheterodyne design was used for so long (and still is today).

It has the advantage that you can have multiple bands in a single receiver, although you have to pick your first IF carefully for that, simply by having switched front-ends, and all the heavy lifting of the filtering etc. is done at the first IF, and that is the same for all bands.

It has the advantage that demodulating more esoteric modes (such as FM, which requires more work than AM) is relatively straightforward at the last IF (which can be the same as the first IF in a single-conversion superheterodyne design) - a simple PLL will do the job nicely for demodulating FM, rather than having to have a much more complex PLL to demodulate at baseband.

The only real disadvantage is that it requires two mixing stages and two local oscillators (although the IF oscillator is fixed, and in your diagram is implemented with a very simple crystal oscillator - so that’s just a couple of extra components).

So why did the superheterodyne design ‘win’? And effectively win for an entire century? Its advantages outweigh its disadvantages.

Today, if you’re not going to make a superheterodyne receiver, it’s probably because you will do it in software. Because that is what will cause the demise of the superhet: the SDR.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16149/demodulation-based-on-external-frequency-source, by Ben Madison KO4UXC, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
