# Optimal length of HT antenna for VHF UHF and diminishing return

*Tags: antenna, vhf, uhf, ht · score 3*

## Question

I see folding antennas of various lengths that people are using for for their HT. My question is about the optimal length. I know it may "depend" on many factors so let me know if I need to provide more information.

I know that many antennas are actually a coil of a particular length (quarter wavelength perhaps), so maybe these are actually all the same coil length. I'm not sure. But I'm wondering what factors should determine the length that one chooses.

I don't own anything outside of FRS and CB yet however I'm doing research ahead of time. To have an example, let's say I'm using the dual band UV-5R for communication on both VHF and UHF (2m and 70cm), and in an urban environment.

There are several lengths available:  
33cm=13in  
47cm=18in  
72cm=28in  
108cm=42.5in  
124cm=49in

Just look at this beast:  
(Image from Amazon.com)

Could it be too long and actually hurt gain or pickup too much noise? Or in general, the longer the better? If that's the case, perhaps there is diminishing return and the extra length becomes just an annoyance after 47cm/18in. How should one decide?

## Answer (score 4, by user10489)

To directly answer your question, the ideal antenna length for maximum radiation is dependent on the wavelength.

For example, CB wavelength is approximately 11m. The ideal antenna is half of that for a dipole antenna. However, most CB (and HT) antennas are monopoles, which split the antenna in half and use its mount as the other half, so the ideal CB antenna would be approximately 2.75m, or just under 9 ft, using the vehicle body as the other half of the antenna. (A vehicle with less than 9ft of metal may not work well with such an antenna.)

Similarly, the ideal 2m antenna for an HT would be approximately 0.5m with you holding the radio for the other half of the antenna, although you can also get a 1m antenna ("half wave") that will work somewhat better, as this is an end fed dipole instead of a monopole, and doesn't rely on you holding the radio to make the other half of the antenna.

If the antenna is a full 1/4 wavelength, it is typically not a coil. Shorter antennas probably are, but the length of the wire in the coil changes as the antenna gets physically shorter, so it is not direct relationship, but electrically, it will still measure as 1/4 or 1/2 wavelength.

The higher frequencies like 2m and 70cm are very dependent on line of sight between the receiver and transmitter, and thus height of the antenna is a huge factor in antenna effectiveness. Thus, the size of the antenna may increase effectiveness not because of better radiation, but because of better height, and you might get the same effect with a smaller antenna raised higher. This is one of the advantages of external antennas like the J-pole -- you can separate it from the radio with coax and raise it higher. (The j-pole is also an end fed dipole. )

Lastly, when considering the "optimal" antenna, you need to take mechanical factors into consideration. In other words, larger HT antennas are heavier and can become a huge lever arm, and put more stress on the radio's antenna connector, and have a higher chance of breaking it. Half wave antennas typically also include an impedance matching coil, which makes them even heavier. When using large antennas, some care must be taken to minimize stress on the radio's antenna connector.

It is possible to get a "better" antenna that is longer than 1/2 wavelength, but it would no longer be a dipole. For instance, a colinear antenna is a stacked phased array of dipoles and can be many multiples of 1/4 wavenlength. This describes some larger wifi antennas and possibly some vehicle antennas or antennas mounted to buildings, but you won't find a 70cm HT colinear, its just too big.

## Answer (score 2, by Phil Frost - W8II)

It depends on the type of the antenna.

Mobile antennas are often monopoles. A monopole is self-resonant when it's a quarter wavelength long. A quarter wavelength is good:

- smaller, and the feedpoint impedance will be capacitave and may require a matching network. Matching networks introduce loss.
- larger, and the radiation pattern grows lobes that go up towards the sky and down towards the ground when the antenna is held in the typical vertical way. The law of conservation of energy dictates that any energy sent in a direction where there's not likely another station means less energy is sent at the target receiver (or received from the desired transmitter).

Monopoles require a ground plane, which is omitted in mobile antennas to make them smaller at the cost of performance. If space allows, a dipole is essentially two monopoles back-to-back, and does not require a ground plane. But a dipole is self-resonant around a half-wavelength, so it's twice the size, all else equal.

An even longer antenna can be made with a collinear array of some other kind of antenna, often dipoles. An array allows the antenna designer to "compress" the radiation pattern, sending more of the radiation at the horizon by sending less in other directions. Provided the array is properly designed, and the other station is in a direction perpendicular to the antenna, this can improve performance.

(Though I wouldn't expect much from a $24 antenna from Amazon. It's likely little to no engineering has gone into the design and it may not even be an array.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16298/optimal-length-of-ht-antenna-for-vhf-uhf-and-diminishing-return, by Bort, user10489, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
