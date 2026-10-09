# What does dBi mean?

*Tags: antenna-theory · score 3*

## Question

Can someone tell me what dB gain over an isotropic radiator means?

Let's say I have a 3 element vertically polarized 10 m Yagi (which I do) which is meant to have 7.5 dBi gain.

Which of the following is correct?

1.

If I measure the signal strength 1 km away in line with the boom in the direction in which the Yagi is pointing, and in exactly the same plane as the elements, and then compare that to the signal from an isotropic radiator, the yagi will have a signal which is 7.5 dB stronger.

2.

If I do a 3 dB azimuth plot of both antennas and then compute the surface area of both plots and relatively compare them in dB, then I get 7.5 dB difference.

3.

If I do a 3 dB 3 dimensional plot of both antennas a then compute the Volume of both and compare them in a relative way then I get 7.5 dB.

4.

Some other method I don't know about yet.

## Accepted answer (score 1, by Phil Frost - W8II)

If I measure the signal strength 1 km away in line with the boom in the direction in which the Yagi is pointing, and in exactly the same plane as the elements, and then compare that to the signal from an isotropic radiator, the yagi will have a signal which is 7.5 dB higher.

Theoretically correct. In practice you'll have some trouble actually performing this measurement. Firstly, isotropic radiators don't exist. Secondly, if the specified gain of 7.5 dBi is in free space, the antenna installed over ground will have different characteristics. The location of the mast or tower on which the antenna is mounted, feedline, and other nearby antennas can also perturb the pattern, sometimes very significantly.

Your other two examples seem to involve in some way integrating the power radiated by the antenna over all possible directions. You'll find most antennas likely to be used for amateur radio transmitting will give about the same total power as an isotropic radiator.

The reason should be fairly intuitive considering the law of conservation of energy: if a directional antenna radiates more strongly in a particular direction, it must radiate less strongly in some other direction. To do otherwise would require creating additional energy from somewhere.

The relevant metric comparing total power radiated in all directions is called antenna *efficiency*. It's not difficult to achieve efficiencies above 99%. Consider a simple wire dipole: the wire has very low resistance, so there isn't anywhere for a significant amount of energy to be lost: it has nowhere to go but into electromagnetic radiation. A mobile HF antenna has lower efficiency: the electrical shortening increases the current in the antenna, making the resistive losses in the antenna and the loading coil much more significant. A vertical installed without radials has lower efficiency due to the high resistance of the soil. But antennas that aren't shortened, and are properly installed, can have efficiencies that are very nearly 100%.

## Answer (score 4, by Kevin Reid AG6YO)

If I measure the signal strength 1 km away in line with the boom in the direction in which the Yagi is pointing, and in exactly the same plane as the elements, and then compare that to the signal from an isotropic radiator, the yagi will have a signal which is 7.5 dB stronger.

This is correct. The others are incorrect; antenna gain is always considered in some specific direction, and if you sum it up all around then you have thrown out the information about directivity and the number you have left is only the antenna *efficiency* (how much power it transmits vs. turning into heat).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12879/what-does-dbi-mean, by Andrew, Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
