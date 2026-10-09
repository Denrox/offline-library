# Multi-band Crystal Receiver?

*Tags: equipment-design, crystal-radio · score 3*

## Question

I'm just getting into radio (inspired by YouTube videos), and like many, I plan to start by building a crystal set (or multiples) before moving up to vacuum tubes (which I prefer over transistors).

All the crystal set schematics I've seen, however, are aimed at AM Broadcast band (540-1610 kHz). I'd like to build one that covers a broader band selection -- ideally, up to 80 m or even 40 m.

Am I correct in understanding that simply tapping the main tuning coil isn't sufficient to extend the working frequency up into the 7 MHz range? Is it even possible to do this without physically switching coils? Or are signals in 40 m and 80 m likely to be too weak to receive with a crystal set, or impossible to separate without making a receiver as complex as a tube regen set?

## Accepted answer (score 4, by Glenn W9IQ)

A crystal radio generally consists of a simple LC network and a diode detector. So in theory, altering the LC network would allow you to tune higher frequencies. The real issue is that signals you will find in the higher bands, simply do not have enough power to be detected without additional amplification.

You have an even larger obstacle, however. A CW signal will not be properly demodulated by a simple diode detector even if the signal is sufficiently strong. CW is simply the turning on and off of a carrier. If you were to listen to this with a simple diode detector you would hear the carrier when a dit or dah is being sent - this would be denoted by the absence of background noise. The space in between a dit or dah would be denoted by the sudden rise of background noise. So instead of a nice CW tone of 800 hertz or so, an "S" sent via CW would sound like Silence-Pffft-Silence-Pfft-Silence and then prolonged Pfft. To overcome this, a CW receiver creates a side tone through various techniques. This is beyond the scope of a simple crystal radio.

The same problem exists for the SSB voice modes on 80 meters and 40 meters. Your best hope is to catch the occasional AM QSO and then only if the signals are strong enough - you will probably lose patience quickly.

If you are interested in a simple CW receiver kit, for example, there are many on the market that are inexpensive and simple to build. Here is one example from Four State QRP Group:

An Internet search will reveal many kits for SSB/CW receivers, transceivers, and multi-band versions with a wide variety of features and price ranges.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12574/multi-band-crystal-receiver, by Zeiss Ikon, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
