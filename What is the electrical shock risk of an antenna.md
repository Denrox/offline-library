# What is the electrical shock risk of an antenna?

*Tags: antenna, safety · score 9*

## Question

I've seen people refer to [avoiding touching](What%20are%20the%20most%20common%20RF%20connectors%20encountered%20in%20amateur%20radio.md) an antenna or bare transmission line that might be transmitting. What voltage potentials and currents are commonly found on typical ham radio antennas? Do both the voltage and current increase with increased transmitter power, or mainly one more than the other?

What are the general safety measures one should take concerning antennas, specifically from the power going into the antenna purposefully? Antenna safety around powerlines and other power sources is a different question.

## Accepted answer (score 2, by on4aa)

Most antennas have a standing wave along there length and are therefore effective impedance transformers. The feed impedance of a dipole might be of the order of 73Ω, at its ends, the impedance will be at least 2kΩ, if not higher.

Solving for voltage at the antenna ends, we will have:

$P=\frac{V^2}{R}\Rightarrow V_{rms}=\sqrt{P\cdot R}$

Peak voltage is indeed $\sqrt{2}\cdot V_{rms}$, but the voltages at the ends of a dipole antenna are balanced with respect to ground so: $V_{peak}=\frac{\sqrt{2}}{2}V_{rms}$, only half that value.

Assuming a transmitter power of 1kW: $V_{peak}=\frac{\sqrt{2}}{2}\sqrt{P\cdot R}=\sqrt{\frac{P\cdot R}{2}}=\sqrt{\frac{10^3 \cdot \not 2 \cdot 10^3}{\not 2}}=10^\frac{6}{2}=10^3=1kV$

If the antenna is loaded with a coil, the impedance will be transformed up to an even higher value. This is how a Tesla coil works. The resulting corona effect might be quite dramatic as shown in the picture below (1kW on 80m in short W4JRW dual-band dipole @ HB9DWU).

## Answer (score 3, by KD8TGR)

RF burns aside (these often occur without physical contact), the voltage on the antenna can reach very high levels. There is a good discussion of this at http://forums.qrz.com/showthread.php?243998-Voltage-at-antenna.

Paraphrasing the linked discussion, Ohm's law applies, so if you're dumping 50W into a 35 ohm load:

$P = I^2R$, so $I = \sqrt{\frac{50}{35}} = 1.195$

$V = IR = 1.195 \cdot 35 = 41.83 V_{RMS} \cdot \sqrt{2} = 59.16 V_{PEAK}$

Toward the tip of the antenna, the impedence changes, so the voltage can be orders of magnitude higher (and the current lower).

(Yes, I know V should be E, but old habits are hard to break. I also know that I'm using the RMS for a sine wave, but it's a reasonable approximation.)

## Answer (score 3, by Ron J. KD2EQS)

Touching a "live" (transmitting) antenna could impart a serious RF burn if the power level was high enough. This is different from the classic "electric shock" obtained by putting a finger into a live wall socket. Radio frequencies heat tissue (non-ionizing radiation), proximity and contact with high RF fields will cause a RF burn.

There is a risk of electrocution if the antenna is in contact with an overhead power line, although a well placed antenna should NOT be near any such hazards.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/861/what-is-the-electrical-shock-risk-of-an-antenna, by Adam Davis, on4aa, KD8TGR, Ron J. KD2EQS. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
