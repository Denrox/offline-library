# Antenna Efficiency

*Tags: antenna-theory, impedance · score 5*

## Question

Intuitively, we all understand that an antenna at fractional wavelengths will not radiate well even with perfect impedance matching systems.

From what I understand the efficiency of antenna has a few factors:

- Conduction losses (due to finite conductivity of the metal that forms the antenna)
- Dielectric losses (due to conductivity of a dielectric material near an antenna)
- Impedance mismatch loss

This still does not explain why a 1-foot long dipole antenna on 160 meters does not radiate well.

If I have 100 Watts RF input, and a theoretical perfect matching system to transform my radios independence to the very high impedance of <1/10 fractional wavelength antenna such that there is no reflected power and no ohmic losses in the antenna, where does this 100 watts go, and why is it not all radiated in the form of RF energy as well as that of say a 1/4 wavelength vertical?

## Accepted answer (score 12, by Glenn W9IQ)

In theory, if you had lossless conductors in the antenna and a lossless matching network, your shortened, 1 foot dipole would have a gain of only ~0.7 dB less on 160 meters than the gain of a full size 1/2 wavelength dipole. But the world is far from perfect.

The efficiency of an antenna is defined as:

$$\text {Efficiency}=\frac {R_r}{R_r+R_l} \tag 1$$

where $R_r$ is the radiation resistance of the antenna and $R_l$ is the resistive losses of the antenna.

As an antenna becomes shorter, its radiation resistance drops significantly. As you can see from formula 1, this causes the otherwise negligible resistive losses to significantly impact the efficiency of the antenna. Any inefficiency is simply dissipated as heat.

The gain of an antenna is defined as:

$$\text {Gain}=\text {Directivity}*\text {Efficiency} \tag 2$$

As the antenna is shortened, the directivity drops slightly from 1.64 for a 1/2 wavelength dipole to 1.50 for an infinitesimal dipole. This, combined with the lowered efficiency, results in an overall drop in gain.

So now let's plug your example into the above formulas.

The radiation resistance of a free space shortened dipole is given as:

$$R_r=197L_\lambda^2 \tag 3$$

where $L_\lambda$ is the length of the dipole expressed as a fraction of the wavelength (length in meters / 160 meters in this case).

Your 1 foot 160 meter dipole antenna example would therefore have an $R_r $ of only ~0.7 milliohms.

The RF resistance of 1 foot of 12 gauge wire at 1.8 MHz is ~17 milliohms (ref. http://chemandy.com/calculators/round-wire-ac-resistance-calculator.htm).

[Note: The following paragraph and the subsequent formula results are the result of Phil's critique of my original answer regarding resistive losses.]

The RMS current distribution in a very short dipole without end loading decays linearly from the maximum at the center point to zero at the ends of the antenna. As a result, the *average* RMS current of the short dipole is 1/2 that of the feedpoint current. Since resistive heat losses are the result of current squared, we must apply a 0.25 correction factor (0.5 squared) to the calculated calculated RF resistance of the wire in order to account for this RMS current slope along the length of the short dipole. The effective resistance of the wire in this shortened dipole is therefore ~4.3 milliohms.

Populating formula 1 tells us that the antenna will have a 14% efficiency. This means that 86 of your 100 watts of applied power goes to waste as heat. Formula 2 tells us that the antenna will have a free space gain of 0.21 or -6.8 dBi. For comparison, an efficient, full 1/2 wave dipole in free space has 2.2 dBi of gain.

Finally, a shortened antenna has a reactive component at its feedpoint that must be dealt with. This, in combination with a low resistive component, can be difficult to match to normal amateur transmission lines resulting in additional losses in the matching circuit and a corresponding reduction in antenna system gain. Of course if the matching circuit does not provide a match to the $Z_o$ of the transmission line, there will be additional losses in the transmission line and a possible reduction in the transmitter output power.

You mentioned dielectric losses. These are normally minimal at HF frequencies in a properly designed matching network.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10227/antenna-efficiency, by Skyler 440, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
