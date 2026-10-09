# How can i adjust the IF strip in a single conversion SSB receiver which has a product detector?

*Tags: electronics, ssb · score 3*

## Question

I have an analog 27 MHz transceiver which i am planning to convert to 10 m. The radio is an AM / SSB unit with a single conversion superhet receiver with an IF of 7.8 MHz using a crystal filter. This radio does not have any faults due to component failure, and I'm trying to align the receiver and have a problem understanding one aspect of the alignment.

Normally with other radios of this type, alignment of the IF strip generally involves connecting a signal generator to the antenna socket and then peaking coils and transformers for maximum signal level.

However when i do that with this model radio (i have 4 and they all do the same thing), the local oscillator used to inject carrier into the product detector used for SSB receive seems to appear as a signal on the S meter. I have to adjust the first transformer in the IP strip off to the side of the point where i see maximum signal generator level on the meter and then it seems to work properly, however with reduced receiver sensitivity.

Other radios I have aligned don't show this behavior and you just set the alignments in the IF strip for maximum signal and you never see the local BFO appear as a signal on the S meter.

Can anyone explain to me what is going on when I am aligning this radio ?

In the schematic below, the 7.8 MHz IF strip is Q201, Q202, Q203, and you can see the IF output from the IF transformer T203 at the top middle going to T401 and then to the SSB product detector Q405 and Q406 at the lower right. The product detector has an input from a 7.8 MHz local oscillator which you can't see in the picture at the junction of Q405 and Q406 emitters. The 7.8 MHz crystal filter FL-1 is at the top left. The separate detector for AM are the diodes at the top right. The audio outputs from the 2 detectors are connected to R419 which connects to the audio amp input.

## Accepted answer (score 2, by Andrew)

It looks like no one is going to answer this question and in the mean time i've found out was what wrong anyway so i am posting my own answer.

Firstly after some more thinking it became obvious to me that the local oscillator has nothing to do with what the S meter reads, as the BFO injection is done in the product detector which outputs an audio signal and this circuit doesn't impact on RF reception, the AGC circuit or anything else that affects the S meter reading.

It became apparent that this particular radio has a mechanical design fault whereby the output from the local 7.8 MHz oscillator is erroneously coupled via various wires, PCB tracks, stray capacitance or lack of proper RF shielding into the path of the 7.8 MHz IF.

The design of this transceiver uses the local 7.8 MHz oscillator for the single receive IF, the AM transmit carrier oscillator and for the BFO injection for SSB reception. While this design minimizes the number of components used and aids in keeping everything on the correct frequency, it also allows for this fault where the local oscillator output is picked up or received by the radio's IF because the IF was chosen to be the same frequency as the local oscillator for that reason of simplifying transceiver design. Because of the erroneous or stray IF pickup, the local oscillator signal appears as a real signal which shows on the S meter.

I solved the problem by adding a 100 nF ceramic capacitor between a point on the PCB where an incoming + 9V supply connects via a red wire to the IF circuitry, and a nearby ground pad. That got rid of the signal completely, so the 7.8 MHZ was getting in via the IF + 9 V supply rail. Now i can adjust the IF strip for maximum sensitivity as per usual.

I'm surprised that this radio got to production and units were actually sold in large numbers while having this fault, but there you go.

Almost forgot to mention the radio model, which is an SBE Sidebander V 27 MHz CB AM/SSB transceiver made by NDC of Japan in about 1978.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15885/how-can-i-adjust-the-if-strip-in-a-single-conversion-ssb-receiver-which-has-a-, by Andrew. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
