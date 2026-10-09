# Determining whether signal meets the 12 dB SINAD voltage

*Tags: antenna, receiver, wire-antenna, rf-power, voltage · score 3*

## Question

The specification for a certain radio receiver says: Typically 12dB SINAD NBFM for 0.15uV at 145MHz. If I understand correctly, this means that the received radio wave should have a voltage level of at least 0.15uV for the receiver to produce a signal with a quality of 12dB SINAD. I know how to calculate the signal power with the link equation, I can also calculate the electric field intensity of the EM wave, but I don't see how I can calculate the voltage level of a signal. How do I verify that my transmitted radio wave will meet this voltage requirement?

## Accepted answer (score 2, by tomnexus)

The specification means $0.15\ \mu\text{V}$ at the input terminals of the receiver, so this voltage across a $50\ \Omega$ load.

Power in a resistor can be calculated with  
$P={V^2}/{R}$  
so $0.15\text{ }\mu\text{V}$ is a power of ${(0.15 \times 10^{-6})^2 } /{50} = 4.5 \times 10^{-16} \text{ W}$ (or ask google)

This is -123.5 dBm into the receiver.

For interest, if the receiver is 25 kHz wide, and needs about 6 dB S/N to achieve that SINAD, then the receiver noise figure is an amazing 3 dB. Put another way, thermal noise at room temperature, in 25 kHz, is already -127 dBm, so the receiver is about as sensitive as it could possibly be for terrestrial communications.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14479/determining-whether-signal-meets-the-12-db-sinad-voltage, by Stasevicius, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
