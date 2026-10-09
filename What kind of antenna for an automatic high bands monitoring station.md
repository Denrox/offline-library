# What kind of antenna for an automatic high bands monitoring station?

*Tags: antenna, propagation, wspr · score 4*

## Question

I would like to monitor NCDXF beacons, and WSPR. What kind of antenna would be good for reception in the bands of 6, 10, 12, 15, 17 and 20M?

Some antennas I considered:

- A trapped dipole, with traps for each band. This could get tricky with the close proximity of the frequencies.
- A fan dipole. Doable, but I've tried a couple of times to build one without success.
- A vertical with an active tuner: a bunch of coils and capacitors, to match the multiple bands. I can build this with some relays and arduino, but I'd rather have a passive receiver.
- A loop, but as far as I know, these are single band and very narrow.
- A Random Wire: tried one, with a 1:9 balun. Reception wasn't great anywhere.
- That 20M dipole I no longer use, and hope for the best

My goal is to be able to monitor propagation at my QTH, and have a reasonable idea of the conditions, without relying on propagation report websites like WSPRnet or similar.

If possible, I'd also like to be able to transmit WSPR, that's why a resonant antenna with reasonable SWR would be desired, but this isn't a priority for me.

## Answer (score 3, by Scott Earle)

I’m going to throw the HF vertical’s hat in the ring, too. Something like an R5 or R7 (or HF9V or similar), that can be used on the higher HF bands and 6m. They’re omnidirectional, which is either a good thing or a bad thing, and with a good set of radials they perform well for both receive and transmit. They might be a little expensive for a simple multiband receiver, but you could also use them as reasonable DX antennas.

I’d say that by the criteria given in Phil’s answer (equally bad on all bands), a multiband HF vertical is an excellent fit.

## Answer (score 2, by Phil Frost - W8II)

A short dipole or small loop is a good choice for a receive-only antenna that works over many bands simultaneously.

The trick is to make an antenna that's equally bad everywhere. If you try to match a short dipole with a loading coil, or a small loop with a tuning capacitor, you end up with a very narrow-band antenna. So instead you don't try to match it at all, and just focus on extracting the maximum signal possible. For receiving you don't necessarily need optimal power transfer.

For a short dipole, that means having a preamplifier with an extremely high input impedance. And for a loop, an extremely low input impedance.

For example, LZ1AQ has such a preamplifier kit. There are many others available, sold as "active antennas".

If you also want to transmit, your ideas of traps, fans, and switchable matching networks all sound like viable options, perhaps even in combination. You can for example have a trap dipole or monopole, but with stubs added for bands not covered by the traps. For example, DX engineering makes a 17 meter add-on for the Huster BTV that works like this. You can find commercial kits, or you can make your own with a little trial and error.

## Answer (score 2, by Brian K1LI)

This sounds like a perfect application for the Discone antenna:

"Skeletonizing" the disc and the skirt make it amenable to construction with wire and/or tubular elements. The skirt is insulated from the disc and is angled downward from the horizontal plane; this insulator is the location of the feedpoint. There are several commercial suppliers of similar antennas which may work for you.

According to an article in *Electronics Notes*, the element lengths should be 0.175$\lambda$ for the disc and 0.25$\lambda$ for the skirt, at the lowest frequency of operation and the skirt should be angled at 60$^{\circ}$ from the plane of the disc. Using 13MHz, this results in element lengths of 79.4-inches for the disc and 227-inches for the skirt. I simulated this antenna in NEC2 with 1-inch elements:

With the feedpoint 0.5$\lambda$ above "real", medium-conductivity ground the SWR is:

Section 10.4.6 of the *ARRL Antenna Book* gives different equations for the dimensions: $\lambda$/4 for the *height* of the cone and disc width *0.7 times the width of the base of the skirt*. At a lower frequency of 13MHz, these equations result in element lengths of 90.8-inches for the disc and 263-inches for the skirt. This improves the match over the frequency range:

Replacing the elements with 14-gauge wire further "skeletonizes" the antenna, adversely affecting the SWR, but it is still more than adequate for monitoring:

Doubling the number of wires smooths out the SWR curve at nearly 2.5:1 from 14MHz to 30MHz.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16458/what-kind-of-antenna-for-an-automatic-high-bands-monitoring-station, by hjf, Scott Earle, Phil Frost - W8II, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
