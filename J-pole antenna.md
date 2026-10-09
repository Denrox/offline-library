# J-pole antenna

The **J-pole antenna**, more properly known as the **J antenna**, is a vertical [omnidirectional](Omnidirectional%20antenna.md) transmitting [antenna](Antenna%20%28radio%29.md) used in the shortwave frequency bands. It was invented by Hans Beggerow in 1909 for use in Zeppelin airships. Trailed behind the airship, it consisted of a single one half wavelength long wire radiator, in series with a quarter-wave parallel transmission line tuning stub that matches the antenna impedance to the feedline. By 1936 this antenna began to be used for land-based transmitters with the radiating element and the matching section mounted vertically, giving it the shape of the letter "J", and by 1943 it was named the *J antenna*. When the radiating half-wave section is mounted horizontally, at right-angles to the quarter-wave matching stub, the variation is usually called a **Zepp antenna**.

### How it works

The J-pole antenna is an end-fed [omnidirectional](Omnidirectional%20antenna.md) half-wave [antenna](Antenna%20%28radio%29.md) that is matched to the feedline by a shorted quarter-wave parallel transmission line stub. For a transmitting antenna to operate efficiently, absorbing all the power provided by its feedline, the antenna must be impedance matched to the line; it must have a resistance equal to the feedline's characteristic impedance. A half-wave antenna fed at one end has a current node at its feedpoint, giving it a very high input impedance of around 1 000–4 000 ohms. This is much higher than the characteristic impedance of transmission lines, so it requires an impedance matching circuit between the antenna and the feedline.

A shorted quarter-wave stub, a transmission line one quarter of the wavelength long with its conductors shorted together at one end, has a similar high impedance node at its open end, making a good match to the antenna. The input impedance seen at a point along the stub varies continuously, decreasing monotonically from this high value to zero at the shorted end. So any value of input impedance can be obtained by connecting the feedline to the proper point along the stub. One arm of the stub is extended a half wavelength to make the antenna. By attaching the antenna's feedline to the proper point along the transmission line, the stub will transform this impedance down to match the lower feedline impedance, allowing the antenna to be fed power efficiently. During construction the proper attachment point for the feed-line is found by sliding the connection of the feedline back and forth along the stub while monitoring the [SWR](Standing%20wave%20ratio.md) until an impedance match (minimum SWR) is obtained.

#### Gain and radiation pattern

Primarily a dipole, the J-pole antenna exhibits a mostly omnidirectional pattern in the horizontal (H) plane with an average free-space gain near 2.2 dBi (0.1 dBd). Measurements and simulation confirm the quarter-wave stub modifies the circular H-plane pattern shape increasing the gain slightly on the side of the J stub element and reducing the gain slightly on the side opposite the J stub element. At right angles to the J-stub, the gain is closer to the overall average: about 2.2 dBi (0.1 dBd). The slight increase over a dipole's 2.15 dBi (0 dBd) gain represents the small contribution to the pattern made by the current imbalance on the matching section. The pattern in the elevation (or E plane) reveals a slight elevation of the pattern in the direction of the J element while the pattern opposite the J element is mostly broadside. The net effect of the perturbation caused by quarter-wave stub is an H-plane approximate gain from 1.5 to 2.6 dBi (-0.6 dBd to 0.5 dBd).

#### Environment

Like all antennas, the J-pole is sensitive to electrically conductive objects in its induction fields (aka reactive near-field region) and should maintain sufficient separation to minimize these near field interactions as part of typical system installation considerations. The quarter wave parallel transmission line stub has an external electromagnetic field with strength and size proportional to the spacing between the parallel conductors. The parallel conductors must be kept free of moisture, snow, ice and should be kept away from other conductors including downspouts, metal window frames, flashing, etc. by a distance of two to three times the spacing between the parallel stub conductors. The J-pole is very sensitive to conductive support structures and will achieve best performance with no electrical bonding between antenna conductors and the mounting structure.

### Construction

The antenna consists of two parallel straight metal conductors, one ⁠3/4⁠ of a wavelength and the other ⁠1/4⁠ of a wavelength long at the operating frequency, shorted together at the bottom. Typical construction materials include metal tubing, ladder line, or [twin-lead](Twin-lead.md). Since the matching section must act as a transmission line, the parallel conductors should be no more than .02 wavelength apart.

The J-pole antenna and its variations may be fed with balanced line. A coax feed line may be used if it includes a means to suppress feed-line RF currents. The feed-point of the J-pole is somewhere between the closed low-impedance bottom and open high-impedance top of the J stub. Between these two extremes a match to any impedance between the low to high impedance points is available.

The J-pole design functions well when fed with a balanced feed (via [balun](Balun.md), transformer or choke) and no electrical connection exists between its conductors and surrounding supports. Historical documentation of the J antenna suggests the lower end of the matching stub is at zero potential with respect to earth and can connect to a grounding wire or mast with no effect on the antenna's operation. Later research confirms the tendency of the mast or grounding wire to draw current from the antenna potentially spoiling the antenna pattern. A common approach extends the conductor below the bottom of the J-pole resulting in additional and undesirable RF currents flowing over every part of the mounting structure. This modifies the far field antenna pattern typically, but not always, raising the primary lobes above the horizon reducing antenna effectiveness for terrestrial service. J-pole antennas with electrical connection to their supports often fare no better, and often much worse, than the simpler [monopole antenna](Monopole%20antenna.md). A mast decoupling stub reduces mast currents.

### Variations

#### Slim Jim antenna

A variation of the J-pole is the **Slim Jim** antenna, also known as **2BCX Slim Jim**, that is related to the J-pole in a similar way to how a folded dipole is related to a [dipole](Dipole%20antenna.md). The Slim Jim is one of many ways to form a J-Pole. Introduced by Fred Judd (G2BCX) in 1978, the name was derived from its slim construction and the J type matching stub (**JI**ntegrated **M**atching).

The Slim Jim variation of the J-pole antenna has characteristics and performance similar to a simple or folded half-wave antenna and identical to the conventional J-pole construction. Judd reported that the Slim Jim produces a lower takeoff angle and better electrical performance than a ⁠5/8⁠ wavelength ground plane antenna, however others' tests and analyses show Slim Jim antennas to have no performance advantage over a conventional, single-wire J-pole antenna. Slim Jim antennas made from ladder transmission line use the existing parallel conductor for the folded dipole element, but in the copper pipe variation, the Slim Jim requires almost twice as much material, for which it returns no performance benefit.

The approximate gain in the H-plane of the Slim Jim is from 1.5 to 2.6 dBi (−0.6 dBd to 0.5 dBd).

#### Super-J antenna

The Super-J variation of the J-pole antenna adds another collinear half-wave radiator above the conventional J and connects the two with a phase stub to ensure both vertical half-wave sections radiate in current phase. The phasing stub between the two half-wave sections is often of the Franklin style.

The Super-J antenna compresses the vertical beamwidth and has more gain than the conventional J-pole design. Both radiating sections have insufficient separation to realize the maximum benefits of collinear arrays, resulting in slightly less than the optimal 3 dB over a conventional J-pole or halfwave antenna.

The approximate gain in the H-plane of the Super-J antenna is from 4.6 to 5.2 dBi (2.4 dBd to 3.1 dBd).

#### Collinear J antenna

The collinear J antenna improves the Super-J by separating the two radiating half-wave sections to optimize gain using a phasing coil. The resulting gain is closer to the optimum 3 dB over a conventional J-pole or halfwave antenna.

The approximate gain in the H-plane of the Collinear J antenna is from 4.6 to 5.2 dBi (2.4 dBd to 3.1 dBd).

#### E-plane gain patterns of the variations

The graph compares the E-plane gain of the above three variations to the conventional J antenna.

The conventional J antenna and SlimJIM variation are nearly identical in gain and pattern. The Super-J reveals the benefit of properly phasing and orienting a second radiator above the first. The Collinear J shows slightly higher performance over the Super-J.

#### Dual-band operation near 3rd harmonic

The basic J antenna resonates on the third harmonic of its lowest design frequency. Operating a ⁠3/2⁠ wavelengths this way produces an antenna pattern unfavorable for terrestrial operation.

To address the pattern change a variety of techniques exist to allegedly constrain a J antenna operating at or near the third harmonic so only one half-wave is active in the radiator above the stub. All involve the use of a high impedance choke at the first voltage loop. These methods fall short of the goal as choking a high impedance point with a high impedance allows energy to pass the choke.

---

*Source: Wikipedia, J-pole antenna (https://en.wikipedia.org/wiki/J-pole_antenna), by Wikipedia contributors, CC BY-SA 4.0.*
