# Efficiency of short dipole receiving antenna

*Tags: antenna, receiver, dipole · score 7*

## Question

For a transmitting dipole antenna, its length is important. If it is close to half the wavelength, it will be efficient and most of the input power will be radiated. How important is the length of dipole in case of receiving antenna? Will a dipole of given length as inefficent as receiver as a transmitter? As far as receiving is concerned, how inefficient will a $\lambda$/10, $\lambda$\100 and $\lambda$\1000 dipole antenna relative to a $\lambda$\2 dipole?

## Answer (score 8, by Glenn W9IQ)

The efficiency of any antenna has a direct impact on the gain of the antenna. The gain of the antenna equally effects transmit and receive - a characteristic known as reciprocity.

The highest gain dipole is a 10/8 wave dipole. When you begin to shorten that dipole, its gain drops. When the dipole becomes very short (<<1/10 $\lambda$) it is called an infinitesimal dipole. Its gain drops significantly.

To see what why the gain of the dipole is dropping, we need to understand the primary factors that make up antenna gain (in linear form):

$$ \text{Gain} = \text{Directivity} \times \text{Efficiency} \tag 1$$

The directivity of the dipole antenna does not change a lot because of its size. For example, a 1/2 wavelength dipole has a directivity of 1.64 and an infinitesimal dipole has a directivity of 1.5.

The major factor impacting gain, in the case of this dipole question, is efficiency. Efficiency is defined as:

$$\text{Efficiency}=\frac{R_r}{R_r+R_l} \tag 2$$

where Rr is the radiation resistance and Rl is the resistive losses in the antenna.

The radiation resistance is the dominating factor in most cases. A 1/2 wave dipole in free space has a radiation resistance of 72 ohms. A 0.05 wavelength dipole has a radiation resistance of only 0.49 ohms. To see the effect this has, let us assume that the losses in the antenna are simply related to the length of wire. If the 1/2 wavelength antenna had say 1 ohm of losses, then the 0.05 wavelength antenna would have 0.1 ohms of losses since it is 1/10 the length of the 1/2 wave dipole. According to equation 2, this makes the efficiency of the 1/2 wave dipole 98.6% and the efficiency of the 0.05 wavelength dipole 83.1%. While this is not yet the complete efficiency story, if we pause here to plug these numbers into equation 1, the gains so far are are 1.63 (2.12 dBi) and 1.25 (0.98 dBi).

To complete the efficiency picture we need to look not just at the antenna but rather at the antenna system. This includes any matching network and transmission lines. For the latter, the calculations are fairly straight forward and it is length and frequency dependent so I will not address that here. But the matching network warrants some scrutiny.

The goal of the matching network is to transform the feedpoint impedance of the antenna into an impedance that minimizes the losses in the transmission line (when viewed from a transmitting perspective). In the case of a 1/2 wavelength dipole, as it is brought close to earth, its feedpoint impedance nearly matches the impedance of common coaxial cable (50 ohms) so no matching network is needed. Thus we can assign 100% efficiency to the matching network in this case.

The infinitesimal dipole is very short compared to a wavelength so its feedpoint impedance is dominated by capacitive reactance while the real part of its impedance is a fraction of an ohm (0.49 ohms in the earlier example). The matching network will therefore contain sufficient inductive reactance to neutralize the capacitive reactance and it will contain other reactive or transformative components to raise the real part of the impedance by a factor of 100 or so. Analyzing the efficiency of such a network requires a significant effort but efficiencies in the 20% range or less are not uncommon. Using this coarse estimate, this introduces another 7 dB or so of losses for the 0.05 wavelength infinitesimal dipole bringing its gain to 0.25 (-6.02 dBi).

To wrap up this analysis consider that the gain difference between the two antennas in this example is 8.17 dB. If 100 watts into the 1/2 wavelength antenna would barely allow another station to hear you, you would need to use more than 656 watts into the 0.05 wavelength dipole to achieve the same result. And to receive the other station, because of reciprocity, they would need to increase their power by nearly 7 times or you would need to find a receiver with 2.6 times more sensitivity (since sensitivity is expressed in field units such as $\mu$V and therefore the square root of power).

And finally, the radiation resistance of other lengths of infinitesimal dipoles is related by approximately the square of their fractional wavelength. So a 0.005 wavelength dipole has 1/100 the radiation resistance of our 0.05 wavelength dipole. Noting that the resistive losses only went down by 1/10, if all other things are equal, and without considering the matching network efficiency, the antenna efficiency has dropped to 33%.

## Answer (score 3, by hotpaw2)

As antenna geometry (including length) changes, so does its radiation gain pattern in 3D space. According to reciprocity, the pattern of receive efficiency has an equivalent change. So the receive efficiency also depends on the direction of the RF source.

Reciprocity implies that, just as one could increase transmit power to compensate for a less efficient transmit antenna, one could increase receiver gain to compensate for a less efficient receive antenna. However, even if both the received signal and received noise roughly scale together, and thus can be compensated for in a receiver by gain, at some point the lower signal level from a less efficient antenna will drop below the thermal noise (and other internal and nearby RF noise sources) of the receiver front-end or LNA, and gain won't help (the S/N).

## Answer (score 2, by Marcus Müller)

Will a dipole of given length as inefficent as receiver as a transmitter?

Yes, antennas are reciprocal.

There's the common theme in ham radio that "matching your antenna for TX is more important than for RX", which is based on the fact that 1/2 of the power put out by your transmit amplifier might be very much and damage your amplifier if reflected back, but:

From a pure link perspective, it doesn't matter whether you lose x dB at the transmitter or at the receiver.

While one could reasonably give you an answer to your "what's the efficiency of a $\frac\lambda{10}$ dipole", asking that question $\frac1{1000}$ of the wavelength makes no sense, since everything is an (potentially extremely ineffective) antenna for any wavelength; if you need your antenna to be $\frac1{1000}$ of the wavelength in size, you simply don't use a dipole.

Furthermore, when you cross three orders of magnitude, typically, physical effects that play no role at one wavelength become dominant. So, the questions related to high wavelength-to-antenna-size questions can only actually be answered sensibly when you say which bands you actually aim for. The methods and elements from which you can build a 200m antenna simply aren't the same as for 10 GHz...

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11865/efficiency-of-short-dipole-receiving-antenna, by thbnju, Glenn W9IQ, hotpaw2, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
