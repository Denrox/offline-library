# Carrier wave timing

*Tags: receiver · score 3*

## Question

I'm not really too technical when it comes to radio, but I understand that in AM, a shortwave radio generates the carrier frequency so that it can mixed with the received station and then removed, leaving the signal which was modulated with the carrier wave during broadcast. What's keeping the two carrier waves (broadcaster and receiver) in sync? Won't there be phase problems if they are not in sync?

## Accepted answer (score 1, by Glenn W9IQ)

The simplest of AM receivers is called a crystal detector. Here there is no mixing of frequencies at all. The received RF energy is directly converted back to an audio frequency by a simple diode. It is such a simple design, that many of as children received a crystal radio kit to put together. It generally had less that six parts to assemble and it didn't even require a battery. But the shortcoming of this type of receiver is that it is not very sensitive. So while it could receive local AM stations, there was no chance of it receiving foreign AM stations, for instance.

In order to improve the sensitivity of receivers, the heterodyne receiver was developed. Here it takes in the AM station's carrier frequency and mixes it with another frequency. This mixing action produces a new (third) intermediate frequency which is then amplified inside the receiver and finally converted to audio again through something as simple as a diode or other more efficient means. The advantage of this design is that a very high gain, efficient amplifying chain can be designed for the intermediate frequency. In fact, this amplifying stage is called the IF stage (for Intermediate Frequency).

In a typical AM receiver, the IF works at a frequency of 455 kHz (455,000 Hertz). So the AM station carrier frequency is mixed with another frequency whose difference is 455 kHz. This results in the conversion of the carrier frequency to 455 kHz. As an example, if we are trying to receive an AM station that is broadcasting at 620 kHz, we can mix that with a frequency of 1,075 kHz to convert the 620 kHz to 455 kHz (1075-620=455). If we then wish to tune in an 800 kHz station, the mixing frequency would be 1255 kHz so that the resulting frequency would again be the 455 kHz IF frequency.

With regard to phasing problems, there is no worry. We really don't care at all about the phase of the carrier frequency or the phase of the IF chain relative to the carrier frequency since our goal is only to recover the audio that is contained in the amplitude (the envelope) of the carrier wave.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9796/carrier-wave-timing, by Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
