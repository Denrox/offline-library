# Why does SSB have the hollow voice sound?

*Tags: ssb · score 17*

## Question

When I listen to SSB, it has the very familiar tunnel-voice sound. What properties make it sound like this? With a Carrier and an extra sideband as AM, I don't hear the tunnel-effect at all. Is there special equipment to get rid of the effect?

## Answer (score 22, by oh7lzb)

**NO CARRIER,** said the modem.

SSB has no carrier, and the transmitter does not transmit anything when the operator is not speaking. There is no way to transmit the presence of *silence* to the receiver. Instead, you'll hear atmospheric noise, local and remote electrical noise (arcing in relays, remote thunderstorms and all that), RF hash from computers and other electronics. All of that will mix with the transmitted voice.

**Receiver off frequency**

With SSB it's really hard to tune the receiver to exactly the same frequency as the transmitter. If the receiver and transmitter are on slightly different frequencies, the received voice will be tuned equally high or low. A very little difference will make the voice sound slightly strange, although communication is still easy.

Vocal sounds have natural harmonics, too. A vowel having a 400 Hz fundamental frequency will come out of your mouth with harmonics at precisely 800 and 1200 Hz (to *slightly* simplify the example). If an USB receiver is just 20 Hz low, the received tone set will be 420, 820 and 1220, which are no longer harmonically related (420*2 = 840, 420*3 = 1260). That can make a very small frequency difference sound strange.

**Audio bandwidth**

SSB receivers **and** transmitters generally have a more limited bandwidth. With modern DSP-filtered receivers you can easily tune the receiver's bandpass filter to be very wide, but that won't have any effect if the transmitter still uses a 2700 Hz filter. When testing, remember to adjust the transmitter too.

**Multipath effects**

Multiple SSB signals mix together nicely at the receiver, allowing you to hear the natural echo and reverb effects of multipath propagation. This effect can be heard on AM, too.

Sometimes they're less pronounced, creating just slightly spacious sound. If the receiver and transmitter are close to each other, the signal's "*ground wave*" can be heard directly, but its reflection from some upper layer of the atmosphere can be heard too. With a longer distance between stations, the same signal could be reflected at multiple points of the atmosphere at the same time.

Sometimes, with good propagation, the signal can travel the *short path* (shortest line around the planet), and *long path* (around the world in the "wrong" direction), and the signal which has travelled the long path will be clearly delayed. *Polar echo* is another variation on this subject.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/355/why-does-ssb-have-the-hollow-voice-sound, by Skyler 440, oh7lzb. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
