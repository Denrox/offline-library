# What is the advantage of making an antenna resonant?

*Tags: antenna-theory · score 11*

## Question

I am constructing a small loop antenna; apprx 4' diameter, will be used with an antenna tuner (mounted at the feedpoint) and 100W transmitter, and hope to use it on 20m, 40m, and maybe other bands if possible. I can add a tuning capacitor to make it resonate on one of the bands but cannot help wondering... what does that get me?

Is a resonant antenna more efficient? I would assume so, but seem to recall that the increased efficiency is not really all that much.

The Question [What is an antenna tuner? Why bother with resonant antennas in the first place?](What%20is%20an%20antenna%20tuner%20Why%20bother%20with%20resonant%20antennas%20in%20the%20first%20place.md) seems to address what I am asking, but the answer is still unclear.

In case it matters, it is not a continuous loop, there is a break opposite the feed point (where the tuning capacitor would be placed). The antenna uses a gamma match to better align the feed point impedance to the line impedance. The main purpose is to learn what to expect from these sorts of loops as I plan to build a much larger one and would prefer to make my mistakes on a small scale first.

## Accepted answer (score 8, by Glenn W9IQ)

Resonance or non-resonance does not have a direct effect on the efficiency or gain of the antenna. A resonant antenna is one that has only resistance without any reactance (capacitive or inductance) at its feedpoint.

To transfer the maximum available (or rated) power from a transmitter to its load (the antenna system in this case), the impedance of the antenna system must match the specified load impedance of the transmitter. Most transmitters specify a 50 ohm load without any reactance. If the antenna system has reactance (i.e. it is not resonant) the transmitter will not be able to put out its rated power. This is the primary reason we tend to try to "resonate" the antenna.

Imagine if transmitter manufacturers specified a 50 ohm resistive with 23 ohms of inductive reactance (50+j23) as the required load impedance. We would all be working to "non-resonate" our antenna systems to meet this specification in order to put out the rated power!

It is important to note that most antennas, even when resonant, do not have a 50 ohm impedance. It is therefore often required to add some type of matching network to the antenna system to transform the impedance to 50 ohms so that the transmitter can put out its rated power. The matching circuit may be designed to cancel out any reactance in addition to transforming the resistive component of the antenna system to 50 ohms.

One more point about non-resonant antennas. We generally consider a 1/2 wavelength dipole to be essentially resonant. When we extend its length to 10/8 of a wavelength long, it is no longer a resonant antenna. Yet this length of a dipole has the highest gain of any dipole configuration. Clearly antenna resonance and gain bear no direct relationship.

**The Small Loop Resonance Question**

The small loop the OP referenced, without any matching network, will have a feedpoint impedance with a very low radiation resistance (<<1 ohm on 40 meters) and a very high inductive reactance (>>500 ohms). To put this in perspective, this amounts to an SWR50>5,000:1 - well out of bounds for a typical antenna tuner.

If such an impedance were connected to the end of a piece of 50 ohm coax cable that is connected to a transmitter rated for a 50 ohm load, there would be high losses in the cable due to the high SWR and the transmitter would put out a fraction of its power (if it doesn't shut down all together) due to the load being far from 50 ohms resistive. A well designed small loop antenna will have a gain of < -15 dBi. The coax and transmitter losses under this scenario could easily attribute another 20 dB of loss rendering the station communications ability very ineffective. So a matching network is generally required.

The matching network in a typical small loop consists of the feedline connected to a smaller loop that magnetically couples to the larger loop. This portion of the matching circuit effectively acts as a transformer that raises the low radiation resistance of the larger loop to close to 50 ohms in the smaller loop. The other part of the matching network is a variable capacitor across a break in the larger loop. This capacitor is adjusted such that it largely cancels out the inductive reactance present in the large loop with an equal, but opposite, capacitive reactance. The net result is typically an SWR50 of <2:1. Due to the high Q of a small loop antenna, the capacitor will require adjustment for relatively small changes in the operating frequency.

It should be noted that the small loop matching network described does not appreciably change the gain of the small loop. The gain of the small loop is largely constrained by its relatively small dimension compared to the wavelength involved and due to its very low radiation resistance that lowers its efficiency. The matching circuit loss is negligible compared to the latter so there is no practical change in efficiency, and thus gain, of the antenna. As explained earlier, the real advantage of the matching circuit is to allow the transmitter to output its rated power and for the losses in the coax to be minimized. The math related to efficiency and gain are given in my answer to the SE question that the OP referenced earlier.

## Answer (score 4, by on4aa)

## Bandwidth

**Non-resonant antennas** typically have a high input reactance $X_\text{in}$. This results in a higher loaded $Q$ and, by consequence, a reduced bandwidth $BW$.

$${Q_\text{loaded}\uparrow}\equiv\frac{X_\text{in}\uparrow}{R_\text{in}+R_\text{source}}\quad\textrm{and}\quad Q_\text{loaded}=\frac{f_\text{res}}{BW}\quad\Rightarrow\quad{BW\downarrow}\,=\frac{f_\text{res}}{Q_\text{loaded}\uparrow}$$

However, for **extremely short, active receiving antennas** this does not matter as these are matched against an extremely high load impedance of a MOSFET RF amplifier. In this case, the loaded $Q$ hardly changes.

$${Q_\text{loaded}}\equiv\frac{X_\text{in}\uparrow\uparrow}{R_\text{in}+R_\text{load}\uparrow\uparrow}$$

**Resonant off-center fed dipole (OCFD) antennas** exploit this effect by being fed at a higher input resistance $R_\text{in}$ from a source with a higher internal resistance $R_\text{source}$. Consequently, OCFDs achieve much broader bandwidths at their fundamental resonant frequency than their center-fed counterparts.

$${Q_\text{loaded}\downarrow}\equiv\frac{X_\text{in}}{R_\text{in}\uparrow+R_\text{source}\uparrow}\quad\textrm{and}\quad Q_\text{loaded}=\frac{f_\text{res}}{BW}\quad\Rightarrow\quad{BW\uparrow}\,=\frac{f_\text{res}}{Q_\text{loaded}\downarrow}$$

For example, here is a graph of the 80m VSWR bandwidth of my multiband CL-OCFD.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12508/what-is-the-advantage-of-making-an-antenna-resonant, by Chris K8NVH, Glenn W9IQ, on4aa. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
