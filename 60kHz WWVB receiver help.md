# 60kHz WWVB receiver help

*Tags: antenna, receiver, ferrite, lf, wwv · score 4*

## Question

I have built a large ferrite loopstick antenna based off this video. I live in Washington state and am trying to receive and decode WWVB. I can get my antenna to resonate at 60kHz with ~700 pF of capacitance. I am lost on the receiver/preamp portion, I have tried to build receivers but I seem to just get noise on the other end. I tried using this design, but I get noise on the other end. Does anyone know why this design didn't work? At the time I implemented it on a protoboard so maybe it was parasitic elements?

I also tried this design, but at the time I was using a small antenna and couldn't get it to work. At this point I have a general idea of how to design my own receiver, but was wondering if anyone had some books to recommend or some good example circuits. I think designing my own receiver from scratch might be necessary, but am a little confused where to start. I want to shy away from superheterodyne receivers/ using crystals because I don't quite understand that, and I don't have the parts. I have been told a TRF design should work, but I've had no success. I have confirmed my antenna works in lab using a signal generator, but I can't see the WWVB signal on an oscilloscope with my receiver design attempts.

I used a JFET input op amp in an open loop configuration as a amplifier. On a spectrometer I was able to see the 60kHz peak. When hooked up to an oscilloscope the signal was just garbage, this isn't surprising because of the lack of filtering. This signals to me that I can receive the signal at least, but as I mentioned before I can't get a clean signal to look at.

## Answer (score 3, by glen_geek)

One problem with breadboard construction involves the high-gain TRF signal chain @ 60 kHz...you get 60kHz feedback from breadboard back to loop antenna. It may help to put a low-gain amplifier at the antenna (enough to drive a 60 kHz signal driving a shielded cable) to the remote amplifier chain.  
It also helps to look for WWVB signal at night when signal levels rise, and when local noise sources tend to be quieter. Below is a plot showing WWVB signal amplitude versus time. Each amplitude point is plotted at the end of each second:  
The signal amplifier chain here was embedded in a metal box, and fed to a microcontroller where A-to-D conversion was done, and amplitude output at the end of each second.  
It appears that three plots are overlaid, but be aware that a "sync" (or "marker") symbol has lowest accumulated amplitude, a "one" symbol has intermediate amplitude, and a "zero" symbol has highest amplitude.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21861/60khz-wwvb-receiver-help, by Max686, glen_geek. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
