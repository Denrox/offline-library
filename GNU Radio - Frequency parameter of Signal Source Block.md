# GNU Radio - Frequency parameter of Signal Source Block

*Tags: gnuradio, fm, usrp · score 3*

## Question

I designed an analog FM transmitter with GNU Radio Companion in order to understand the tool better. The hardware I use is an USRP B200. The carrier was built with a Signal Source block and the baseband was obtained from a .wav file. The last block of the diagram is a UHD: USRP Sink block with Center Freq set to 98.4 MHz (*this does not matter much, could be any frequency between 88 MHz and 108 MHz*).

The thing is that in order for the design to work I have to set the Frequency parameter of the Signal Source block to 0 and the Center Freq parameter in USRP Sink in the one I am interested in (*in this case 98.4 MHz*). With this setup the transmitter works perfectly.

On the other hand, if I set up the Frequency parameter of the Signal Source block to 98.4 MHz (*which i think is the right thing to do*) the trasmitter does not work, it transmits the original audiofile with a lot of background noise, like if the signal source is messing with the baseband signal. Can someone please explain the reason of this behaviour? I don't understand how it can work if the output of the Signal Source is a signal of frequency 0 and constant amplitude.

This is my flow graph in GNU Radio:

## Answer (score 4, by Phil Frost - W8II)

For a complex-valued sampled stream, the sample rate must be greater than twice the signal represented. The sample rate in your graph is set to 384k, so it's not possible to represent a 98400 kHz signal.

GNU Radio won't stop you, though. Mathematically, when you try to generate a sampled signal that's too high, you get aliasing. As an experiment, try creating a graph with a signal source going into a frequency sink, and observe what happens when you try generating a signal at or above the sample rate.

While you could theoretically increase the sample rate, this would be computationally inefficient. If you sampled at (for example) 200 MHz, you could represent signals anywhere between but not including -100 MHz and 100 MHz. The bandwidth of your signal is probably much less than 200 MHz, and all the bandwidth that isn't occupied by your signal contains no information. Thus you use a lot of compute resources calculating nothing.

So most radios, with the exception of those that work at frequencies low enough where the computational overhead isn't too high, include a frequency mixer to convert a "baseband" input (often at 0 Hz, or sometimes a little higher to avoid negative frequencies) up to RF, in your case 98.4 MHz. A mixer can also perform the opposite operation on receive so a signal at some high radio frequency can be mixed down to a lower baseband frequency for more efficient processing.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16955/gnu-radio-frequency-parameter-of-signal-source-block, by karstarkastro, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
