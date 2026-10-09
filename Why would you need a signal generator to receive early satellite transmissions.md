# Why would you need a signal generator to receive early satellite transmissions?

*Tags: receiver, satellites, oscillator · score 11*

## Question

I recently watched, on You Tube, a NOVA program about the British school masters and students who were the first to publish the news that the Soviets had started launching satellites from a new launch site back in 1958. (School Boys Who Cracked the Soviet Secret). Early in the program (about 8:35, if you watch it), one schoolmaster asks another what he would need in order to receive and record the transmissions from the early Soviet satellites. He was told three items were needed: a receiver, a tape recorder, and a signal generator.

Why would you need a signal generator? The program is short on technical information.

Although interested in radio, I am not an expert, so please excuse me if I have asked a dumb question.

## Accepted answer (score 15, by Zeiss Ikon)

The earliest Soviet satellites, like Sputnik 1, transmitted what amounted to a CW stream -- just pulsed RF at pretty low power (later Sputniks transmitted data by pulse width modulation, still essentially CW). In order to hear it, you needed a Beat Frequency Oscillator -- a BFO -- and with a common radio receiver, the signal generator was standing in for the BFO. If you had a ham receiver or transceiver that could tune the correct frequency, switching to CW mode would do the same job, and a few "world" radios (multiband AM/SW sets) had a BFO function.

The BFO makes the unmodulated signal audible by mixing it with another signal at a few hundred Hertz different frequency. The two signals will reinforce and cancel, forming a "beat", and they'll do it at a frequency equal to the difference between the two (or their sum, but the difference is chosen to be in the audio range, while the sum is radio frequency). This "beat frequency" is then filtered out of the mixed RF and amplified by the receiver. This is the same process used to make a radiotelegraphy signal audible, or to reconstruct a Single Side Band audio signal.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12822/why-would-you-need-a-signal-generator-to-receive-early-satellite-transmissions, by John Warren, Zeiss Ikon. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
