# Can I use my CB mobile antenna with a 10 meter radio also?

*Tags: antenna, hf, vertical-antenna, citizens-band · score 4*

## Question

I have a mobile mounted CB antenna that has an SWR of 1.5 on channel 20. Is it possible to use it with a 10 meter radio? I do not have enough room on my car for an additional antenna, so if it is possible to use my CB antenna for 10 meters, that would be great. If anyone here has done this before, I'd appreciate your insights on the experience!

My antenna is something like this one, which is described as being designed for 26–30 MHz and having a tuneable 48" (1.2 m) whip on top.

## Accepted answer (score 3, by Zeiss Ikon)

The same antenna won't be optimized for CB (~11 meter) and 10 meter ham bands at the same time, though that one appears to be tunable so could likely be used in either band. There are other considerations, though -- first, you shouldn't connect the two radios to the same antenna at the same time; the transmit power of one might damage the receiver in the other (an A-B switch for radio frequency should be sufficient).

Probably the most effective way to do this is to install an antenna matching unit (aka "antenna tuner") between the ham rig and the A-B switch so that you can physically tune the antenna for your CB rig, then when you switch it over to the 10 meter you can (one time, more or less) adjust the matching network to match the antenna to the ham rig's frequency. Then you just need to remember to set the switch to match which radio is powered up (it might also be prudent to build/buy the A-B switch so it can connect the radio not wired to the antenna to a dummy load, to avoid damage if things get crossed up).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20323/can-i-use-my-cb-mobile-antenna-with-a-10-meter-radio-also, by diodes123, Zeiss Ikon. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
