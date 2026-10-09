# BFSK with huge spacing, why?

*Tags: rtty · score 5*

## Question

I recently bought one of the classic USB dongles to experiment with SDR. At 460MHz (Europe, CH) I constantly see many digital transmission that use BFSK. What is strange to me is that:

- the frequency spacing is about 9KHz, instead of the much lower values used for example in RTTY (170Hz). Is this a known protocol spacing?
- The baud rate doesn't look standard to me: 510 baud. What could be an explanation?

Before sending the actual payload (1140 bits) I see 575 alternating bits. Is that some kind of CSMA? The full content is:

```
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101010
10101010101010101010101010101011
00000110010110111101010001001111
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001001001001100011011011011000
10111111010010111110010100011110
01000011011011000011100110110111
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001000000000000011100010001011
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001010111011000111110011010001
00001000000000000011100010001011
111111111111111111

```

- I see that there is a pattern that repeats every 32bits in the payload. Any guess about the protocol? Is it legal to tx with a proprietary protocol on HAM frequencies?

## Accepted answer (score 5, by AndrejaKo)

Let's see if I can answer your question:

Shift:  
The usual theory says that we need spacing between frequencies that is at least equal to symbol rate (or 1/2 of symbol rate for coherent detection). This automatically eliminates the 170 Hz spacing we have in some RTTY implementations. This tells us why not 170 Hz, but it doesn't say why 9 kHz. In my opinion, this would be useful shift that could deal nicely with bad carrier. Basically, the actual middle frequency of the BFSK system might not be exactly the one that has been assigned to the system and could easily have some offsets and is likely to drift with time and temperature. At 460 MHz, 1 ppm of drift would be 460 Hz, the entire spacing of a short-wave RTTY system. By using 9 kHz, we have more room for transmitter imperfections. I also believe that it could be very possible that whoever is running the system needs to get at least a 12.5 kHz channel for it. If that's the case, then there's no reason why to be saving up all that spectrum, when you don't have to.

Baud rate:  
Well it does look very unusual, but I'd say that the intended rate is perhaps 512 Bd instead of 510 Bd. This would then be very close a usual symbol rate. Since you asked about protocol, I think this is probably POCSAG used for pagers. I'm in Germany right now and the town that I'm in has 3 paging frequencies around 466 MHz. They run BFSK with 9 kHz spacing and 512 Bd is a POCSAG baud rate. There's a POCSAG decoder called PDW that you can play around with, to see if it's really POCSAG or not.

CSMA:  
I don't really think this is CSMA. I mean, we're trying to sense if there's a carrier or not and we won't do that by transmitting directly. To me, this more looks like a synchronization step for the receiver. You measured the symbol rate of 510 Bd. It's relatively easy to add a pre-amble that will synchronize the transmitter's and receiver's symbol clocks together, so that when the actual data transfer starts, the receiver knows the real symbol rate and knows when a new symbol starts. Furthermore, by having a pre-amble, you can train the adaptive filters used in receiver equalizer to the particular channel that we have. This way, receiver can try to compensate for environment effects. This is commonly used in digital wireless technologies today.

32 bits:  
I'm not really an expert in POCSAG, so I don't know why they have those 32 bits. I think that they can be used as a sort of rudimentary error correction, they can be used to separate parts of message and give knows ending points for say Viterbi decoder and also to update equalizer channel estimation. Finally, I'm pretty sure that 460 MHz is outside of amateur radio bands in Switzerland. Here's a nice illustrated guide to licensing basics from their government website which says that the 70 cm band is 430 MHz to 440 MHz, like in many parts of the Europe, so 460 MHz would be a commercial part of the band.  
To answer your question more directly, I'm not really sure if proprietary protocols are allowed or not in CH and this is an ongoing debate in ham radio community as a whole, since there are certain interests that are pushing for mutually not-very-open digital voice standards right now. In general case, encryption is banned, but proprietary, or not very known, standards aren't automatically considered encryption. Do note that in some countries POCSAG is explicitly allowed in ham radio. For example, Germany has reserved frequencies for POCSAG in 70 cm amateur band. It's at 439.9875 MHz, if I remember correctly.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6354/bfsk-with-huge-spacing-why, by MarcoM, AndrejaKo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
