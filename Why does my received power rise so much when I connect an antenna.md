# Why does my received power rise so much when I connect an antenna?

*Tags: antenna, rfi, amplifier, noise, link-budget · score 5*

## Question

I am in early stages of making a narrow-band radio receiver (block diagram below). To give you an idea, I am using a simple CP-FSK based modulation scheme, and have achieved 5dB SNR with a Tx signal of -118 dBm on wires (feeding signal via an R&S VSG instead of an antenna). Given a bandwidth of 30 kHz, the kTB noise is around -130 dBm. Considering a noise figure of around 8 dB, I am assuming my thermal noise floor is around -122dBm. I am using a VGA to ensure good dynamic range for my ADC; I adjust my VGA gain such that the output signal from ADC results in a certain target energy level. That way, the VGA gain word gives me a good indication of received signal power. I have verified a negative linear relationship between the input power in 30 kHz band and VGA gain word in the FPGA. To illustrate:

- Gain word 60 corresponds to rx power of -115 dBm or below.
- For a -110 dBm VSG signal emulating 30 kHz AWGN noise, the target ADC energy level is met with a VGA gain word of 55.
- For a -100 dBm VSG signal emulating 30 kHz AWGN noise, the target ADC energy level is met with a VGA gain word of 45.

On the wires, everything seems fine. But I am facing things I don't understand when I connect the antenna.

Soon as I connect an antenna, the average VGA gain word required to achieve the average target ADC energy level becomes 45. This indicates that the antenna is receiving around -100 dBm signal power in the 30kHz pass band. I have done the following to qualify this received power:

1. On changing the Rx frequency, the received signal power changes, but not by much. Say, about 3 dB max.
2. I inserted a BPF of 140 MHZ to 160 MHz between the antenna and the radio. No power rise was seen in the stop band (VGA gain word to maximum). The power rise was still seen in the pass-band. This indicates that the source of power is antenna.
3. Antennas of smaller sizes result in lower received power. It seems that the received power expectedly depends on antenna sizes. This further bolsters point 2.
4. I have tried to put the VGA in an AGC configuration, i.e., in a loop-back fashion, and have also manually controlled it from FPGA. Both methods result in the same VGA gain word for a desired ADC target energy level. This indicates that the issue is not with the settling time of AGC/VGA.
5. When I tune into valid FM bands in my area, or transmit some signal locally, the VGA gain word falls drastically, indicating high Rx power. Also, I can't see this much noise all over the spectrum on a spectrum analyzer with low RBW. In fact, in the band from 237 MHz to 300 MHz, the received power trace for antenna overlaps the spectrum analyzer DANL trace, with an RBW of 300 Hz.

I have not been able to get my hands on an anechoic chamber yet. What I wanna ask is:

1. Isn't -100 dBm of received power on antenna too high in absence of a transmitter?
2. If this much power is expected, shouldn't I calculate my link margin using this received power instead of the thermal noise floor, since -100 dBm is much larger than -122 dBm.
3. What could be the source of this excess energy that I receive with my antenna? How can I verify any possible hypotheses regarding the sources?
4. While I try to get access to an anechoic chamber, should I experiment with making a Farady's cage locally with some metal sheets? Is this reasonable to pursue?

## Accepted answer (score 4, by tomnexus)

I suspect the background noise is from your FPGA development board, coupled to the antenna via the cables. You should see plenty of signals in that band but there should also be places where you get only your amplifier noise.

Wide-band amplifiers can often be oveloaded by the FM band signals, but your BPF test addresses this.

The closed-system tests you're doing sound perfectly reasonable. I don't think you would need an anechoic chamber or shielded chamber - and the source of noise is probably in your receiver prototype itself. Use or make a small antenna (10 cm piece of wire on a connector) with a spectrum analyser, and hold it near the cables, boards and computer to see what you find).

If you want to sample the background RF near your lab, run a cable of at least 5 metres to a window and put the receiving antenna there. Clip at least 10 ferrite beads to the cable, spread along it, also to the power and network cables of the radio boards.

Building a shielded box for the receiver, to prevent it from radiating like this, might be necessary, though you should first address it at the board level. If you want to experiment, you need to manage every wire going out of the box. Something like this:

- A shielded box, which I would make out of some bare PCB material and some aluminium foil, or all PCB material, partially soldered and partially taped with copper/aluminium tape
- SMA barrel connectors, so the shield is connected to the walls of the box
- feedthrough capacitors for the power rails
- optical ethernet converters, widely available, would be the simplest way of getting communication to the board. Or for this test, install a small display and read it through a hole in the enclosure.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21688/why-does-my-received-power-rise-so-much-when-i-connect-an-antenna, by Kraken, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
