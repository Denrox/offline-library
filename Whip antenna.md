# Whip antenna

A **whip antenna** is an [antenna](Antenna%20%28radio%29.md) consisting of a straight flexible wire or rod. The bottom end of the whip is connected to the [radio receiver](Radio%20receiver.md) or transmitter. A whip antenna is a form of [monopole antenna](Monopole%20antenna.md). The antenna is designed to be flexible so that it does not break easily. Whip antennas for portable radios are often made of a series of interlocking telescoping metal tubes, so they can be retracted when not in use. Longer whips, made for mounting on vehicles and structures, may be made of a flexible fiberglass rod around a wire core.

The length of a whip antenna is determined by the wavelength of the radio waves it is used with. Their length varies from compact electrically short antennas ⁠1/ 10 ⁠ wavelength long, up to ⁠ 5 /8⁠ wavelength to improve directivity. The most common type is the *quarter-wave whip*, which is approximately ⁠ 1 /4⁠ wavelength long.

Whips are the most common type of [monopole antenna](Monopole%20antenna.md), and are used in the higher frequency [HF](High%20frequency.md), [VHF](Very%20high%20frequency.md) and [UHF](Ultra%20high%20frequency.md) radio bands. They are widely used as the antennas for hand-held radios, cordless phones, [walkie-talkies](Walkie-talkie.md), FM radios, boom boxes, and Wi-Fi enabled devices, and are attached to vehicles as the antennas for car radios and [two-way radios](Two-way%20radio.md) for wheeled vehicles and for aircraft. Larger versions mounted on roofs, balconies and radio masts are used as base station antennas for [amateur radio](Amateur%20radio.md) and police, fire, ambulance, taxi, and other vehicle dispatchers.

### Radiation pattern

The whip antenna is a [monopole antenna](Monopole%20antenna.md), and like a vertical dipole has an [omnidirectional](Omnidirectional%20antenna.md) radiation pattern, radiating equal radio power in all azimuthal directions (perpendicular to the antenna's axis), with the radiated power falling off with elevation angle to zero on the antenna's axis. Whip antennas less than one-half wavelength long, including the common quarter wave whip, have a single main lobe, and with a perfectly conducting ground plane under it maximum field strength is in horizontal directions, falling monotonically to zero on the axis. With a small or imperfectly conducting ground plane or no ground plane under it, the general result is to tilt the main lobe up so maximum power is no longer radiated horizontally but at an angle into the sky.

Antennas longer than a half-wavelength have patterns consisting of several conical "lobes"; with radiation maxima at several elevation angles; the longer the electrical length of the antenna, the more lobes the pattern has.

A vertical whip radiates vertically polarized radio waves, with the electric field vertical and the magnetic field horizontal.

Vertical whip antennas are widely used for nondirectional radio communication on the surface of the Earth, where the direction to the transmitter (or the receiver) is unknown or constantly changing, for example in portable FM radio receivers, [walkie-talkies](Walkie-talkie.md), and [two-way radios](Two-way%20radio.md) in vehicles. This is because they transmit (or receive) equally well in all horizontal directions, while radiating little radio energy up into the sky where it is wasted.

### Length

Whip antennas are normally designed as resonant antennas; the rod acts as a resonator for radio waves, with standing waves of voltage and current reflected back and forth from its ends. Therefore, the length of the antenna rod is determined by the wavelength ($$\lambda$$) of the radio waves used. The most common length is approximately one-quarter of the wavelength ($$\tfrac{1}{4}\lambda$$), called a "quarter-wave whip" (although often shortened by the use of a loading coil; see Electrically short whips below). For example, the common quarter-wave whip antennas used on FM radios in the USA are approximately 75 cm (2.5 feet) long, which is roughly one-quarter the length of radio waves in the FM radio band, which are 2.78 to 3.41 m (9 to 11 feet) long.

Half-wave whips ($$\tfrac{1}{2}\lambda$$ long) which have greater gain, and five-eighth wave whips ($$\tfrac{5}{8}\lambda$$ long) which have the maximum horizontal gain achievable by a monopole, are also common lengths.

### Gain and radiation resistance

The gain and input impedance of the antenna is dependent on the length of the whip element, compared to a wavelength, but also on the size and shape of the ground plane used (if any). A quarter wave vertical antenna working against a perfectly conducting, infinite ground will have a gain of 5.19 [dBi](Decibel.md) and a radiation resistance of about 36.8 ohms. However this gain is never approached in actual antennas unless the ground plane is many wavelengths in diameter. 2 dBi is more typical for a whip with a ground plane of $$\tfrac{1}{2}\lambda~.$$ Whips mounted on vehicles use the metal skin of the vehicle as a ground plane. In hand-held devices usually no explicit ground plane is provided, and the ground side of the antenna's feed line is just connected to the ground (common) on the device's circuit board. Therefore, the radio itself serves as a rudimentary ground plane. If the radio chassis is not a good deal larger than the antenna itself, the combination of whip and radio functions more as an asymmetrical [dipole antenna](Dipole%20antenna.md) than as a [monopole antenna](Monopole%20antenna.md). The gain will be somewhat lower than a dipole, or a quarter-wave whip with an adequate size ground plane.

Whips not mounted on the radio itself are usually fed with [coaxial cable](Coaxial%20cable.md) feedline of 50 ohm or 75 ohm impedance. In transmitting antennas the impedance of the antenna must be matched to the feedline for maximum power transfer.

A half wave whip antenna (length of $$\tfrac{1}{2}\lambda$$) has somewhat higher gain than a quarter wave whip, but it has a current node at its feedpoint at the base of the rod so it has very high input impedance. If it was infinitely thin the antenna would have an infinite input impedance, but the finite width gives typical, practical half wave whips an impedance of 800–1,500 ohms. These are usually fed through an impedance matching transformer or a quarter wave stub matching section (e.g. the [J-pole antenna](J-pole%20antenna.md)). An advantage is that because it acts as a dipole it does not need a ground plane.

The maximum horizontal gain of a monopole antenna is achieved at a length of five eighths of a wavelength $$\tfrac{5}{8}\lambda$$ so this is also a popular length for whips. However at this length the radiation pattern is split into a horizontal lobe and a small second lobe at a 60° angle, so high angle radiation is poor. The input impedance is around 40 ohms.

### Ground plane antenna

In a whip antenna not mounted on a conductive surface, such as one mounted on a mast, the lack of reflected radio waves from the ground plane causes the lobe of the radiation pattern to be tilted up toward the sky so less power is radiated in horizontal directions, undesirable for terrestrial communication. Also the unbalanced impedance of the monopole element causes RF currents in the supporting mast and on the outside of the ground shield conductor of the coaxial feedline, causing these structures to radiate radio waves, which usually has a deleterious effect on the radiation pattern.

To prevent this, with stationary whips mounted on structures, an artificial "ground plane" consisting of three or four rods a quarter-wavelength long connected to the opposite side of the feedline, extending horizontally from the base of the whip, is often used. This is called a *ground plane antenna*. These few short wire elements serve to receive the displacement current from the driven element and return it to the ground conductor of the transmission line, making the antenna behave somewhat as if it has a continuous conducting plane under it.

The radiation resistance of a quarter wave ground plane antenna with horizontal ground wires is around 22 ohms, a poor match to [coaxial cable](Coaxial%20cable.md) feedline, and the main lobe of the radiation pattern is still tilted up toward the sky. Often *(see pictures)* the ground plane rods are sloped downward at a 45-degree angle, which has the effect of lowering the main lobe of the radiation pattern so more of the power is radiated in horizontal directions, and increases the input impedance for a good match to standard 50-ohm [coaxial cable](Coaxial%20cable.md). To match 75-ohm coaxial cable, the ends of the ground plane can be turned downward or a folded monopole driven element can be used.

### Electrically short whips

To reduce the length of a whip antenna to make it less cumbersome, an inductor (loading coil) is often added in series with it. This allows the antenna to be made much shorter than the normal length of a quarter-wavelength, and still be resonant, by cancelling out the capacitive reactance of the short antenna. This is called an electrically short whip. The coil is added at the base of the whip (called a base-loaded whip) or occasionally in the middle (center-loaded whip). In the most widely used form, the [rubber ducky antenna](Rubber%20ducky%20antenna.md), the loading coil is integrated with the antenna itself by making the whip out of a narrow helix of springy wire. The helix distributes the inductance along the antenna's length, improving the radiation pattern, and also makes it more flexible. Another alternative occasionally used to shorten the antenna is to add a "capacity hat", a metal screen or radiating wires, at the end. However all these electrically short whips have lower gain than a full-length quarter-wave whip.

Multi-band operation is possible with coils at about one-half or one-third and two-thirds that do not affect the aerial much at the lowest band, but it creates the effect of stacked dipoles at a higher band (usually ×2 or ×3 frequency).

At higher frequencies the feed coax can go up the centre of a tube. The insulated junction of the tube and whip is fed from the coax and the lower tube end where coax cable enters has an insulated mount. This kind of vertical whip is a full dipole and thus needs no ground plane. It generally works better several wavelengths above ground, hence the limitation normally to microwave bands.

### Image gallery

---

*Source: Wikipedia, Whip antenna (https://en.wikipedia.org/wiki/Whip_antenna), by Wikipedia contributors, CC BY-SA 4.0.*
