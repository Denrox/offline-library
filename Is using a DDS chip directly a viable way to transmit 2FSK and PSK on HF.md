# Is using a DDS chip directly a viable way to transmit 2FSK and PSK on HF?

*Tags: digital-modes, hf, electronics, transmitter · score 5*

## Question

I'm thinking of building an HF transmitter for data (AX.25 or PSK31). Rather than using an IF stage, I'm thinking of generating the RF frequencies (or phases) directly with a Direct Digital Synthesis chip.

The chip I'm thinking of is the Analog Devices AD9834. It can output a 0 - 37.5MHz sine wave (that covers most of the HF bands). It picks one of two programmed frequencies based on a digital input (high--one frequency, low--the other frequency). Thus, I can get 2FSK out of it. I can do the same thing with another digital input and two programmed phases for PSK. The output power is 20 mW, so I'll need to hook it up to a power amplifier.

I've never heard of anyone building a digital transmitter this way. Usually an intermediate stage is involved. Is there something I'm missing?

## Accepted answer (score 2, by Phil Frost - W8II)

Your question is directly answered on page 23:

One of the areas where the AD9834 is suitable is in modulation applications. The part can be used to perform simple modulation such as FSK. More complex modulation schemes such as GMSK and QPSK can also be implemented using the AD9834.

There's no need for an LO and a mixer if the AD9834 can generate a sufficiently high frequency on its own. Many HF SDRs have a similar architecture, with a high-speed DAC directly generating the RF. You may need some filtering before amplification.

## Answer (score 3, by Glenn W9IQ)

You could probably build a DDS exciter from this chip.

Be aware though that output power is closer to 1.8 mW. You were quoting the total chip power consumption. To get to any reasonable power level, it will require cascaded amplifiers. You will most likely want to think about an filtering as part of the amplification chain.

Normally, an LO (local oscillator) is used when the DDS cannot make the frequency range necessary for the output signal. In this case, mixing the DDS output frequency with another frequency preserves the modulation scheme while allowing a higher frequency of operation. This is in contrast to using a harmonic of the DDS where the modulation scheme can be affected by the frequency multiplication.

In your case, the DDS has sufficient range over the HF band that you should not require an LO or multiplier module in your architecture. Have fun with the project!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7809/is-using-a-dds-chip-directly-a-viable-way-to-transmit-2fsk-and-psk-on-hf, by watkipet, Phil Frost - W8II, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
