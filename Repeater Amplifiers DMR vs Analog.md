# Repeater Amplifiers DMR vs Analog

*Tags: repeater, amplifier, dmr, digital · score 5*

## Question

I have recently purchased an amplifier for my repeater. This was actually my first amplifier purchase ever and should probably have asked more questions prior to buying it. The repeater is a Motorola XPR8400 UHF R1 running in dynamic mixed mode. The amp I purchased is TPL Communications PA6-1BE-RXRFPSM UHF 100W. I've heard that some amps have issues with digital signals and some don't depending on the amp class. I tried to do research on this but there is little to no information online. Was able to confirm though through an acquaintance who never heard of that is maintaining a repeater system running a 250W TPL amplifier in DMR without any issues. What is the theory behind digital signals vs analog and repeater operations? Will this specific amplifier transmitting DMR work or will I run into problems? Lastly, if this amplifier is not suited for DMR which make and models are?

## Accepted answer (score 0, by Mike)

Research update: The TPL PA6-1BE-RXRFPS-M amplifier, specified for FM mode with a frequency range of 400-512 MHz, input power of 8-15 W, and output power of 75-100 W, is likely Class AB. This class is typical for RF power amplifiers in communication systems, offering a balance of linearity and efficiency. The design likely uses solid-state components, such as LDMOS transistors, which are standard for Class AB amplifiers due to their cost/performance ratio in mobile and digital networks. The continuous duty operation and the need for handling modulated signals suggest Class AB, as it conducts for more than half but less than the full cycle of the input signal, providing good signal fidelity.

Investigation and Findings Initial searches for the TPL PA6-1BE-RXRFPS-M revealed detailed product descriptions but no direct mention of the amplifier class. For instance, the official TPL Communications website (Tplcom) describes the RXR Series as cost-effective, continuous duty power amplifiers, with specifications including frequency range, power output, and physical dimensions, but lacks explicit classification. Similarly, distributor pages like SYSCOM list input power (8-15 W, output 75-100 W) and note a consumption of 16 Amps, but do not specify the class.

Further exploration into FCC filings, using the FCC ID database (Fccid.io), showed applications for TPL Communications under grantee code BBD, but specific details for PA6-1BE-RXRFPS-M were not readily available. Searches for "TPL RXR SERIES amplifier schematic" and related terms, such as on Repeater-builder, did not yield direct schematics or class information, though user manuals for similar models (e.g., FCC ID BBD6-1AE-RXR) mentioned solid-state design options, such as a solid-state carrier operated relay (SSR), suggesting solid-state technology.

Comparison with Other Classes Class AB is a compromise between Class A (highly linear, low efficiency) and Class B (moderate efficiency, more distortion). Class C, while efficient, is non-linear and typically used for constant amplitude signals like FM, but may not suit digital communications requiring linearity. Given the user's interest in DMR, Class AB aligns better, though the FM specification might suggest optimization for analog signals.

Unexpected Detail Interestingly, while the amplifier is specified for FM, its likely Class AB design suggests potential use with digital signals like DMR, challenging the assumption that FM-specific amplifiers are unsuitable for digital applications.

Conclusion and Recommendation Research suggests that the TPL PA6-1BE-RXRFPS-M amplifier is likely Class AB, given its continuous duty operation, use in communication systems requiring linearity, and alignment with industry standards for similar RF power amplifiers. The design is probably solid-state, using LDMOS transistors, paralleling standard Class AB configurations. While direct confirmation from schematics or datasheets was not found, the technical characteristics and comparative analysis strongly suggest Class AB as the most probable classification. For precise verification, consulting TPL Communications directly or accessing detailed engineering documentation would be recommended. This conclusion is supported by the need for a balance between efficiency and linearity in communication applications, with Class AB offering a practical solution for the amplifier's specifications and usage. Interestingly, while specified for FM, the likely Class AB design suggests potential use with digital signals like DMR, challenging common assumptions about analog-only amplifiers.

When I put the amplifier in service this year I'll update my testing results to confirm linearity to handle DMR signals.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21903/repeater-amplifiers-dmr-vs-analog, by Mike. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
