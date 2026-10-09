# Beverage antenna

The **Beverage antenna**, a very early type of *wave antenna* or *traveling wave antenna*, is a long-wire receiving [antenna](Antenna%20%28radio%29.md) mainly used in the low frequency and [medium frequency](Medium%20frequency.md) radio bands, invented by H.H. Beverage in 1921. It is used by [amateur radio](Amateur%20radio.md) operators, shortwave listeners, longwave radio DXers, and for military applications.

A Beverage antenna consists of a horizontal wire from one-half to several wavelengths long (tens to hundreds of meters / yards for shortwaves; up to several kilometres / miles for longwaves) suspended above the ground, with the feedline to the receiver attached to one end, and the other end of the wire terminated through a resistor to ground. The antenna has a unidirectional radiation pattern with the main lobe of the pattern at a shallow angle into the sky off the resistor-terminated end, making it ideal for reception of long distance [skywave](Skywave.md) (skip) transmissions from stations over the horizon which reflect off the [ionosphere](Ionosphere.md). However the antenna must be built so the wire points in the direction of the transmitter(s) to be received.

The advantages of Beverage antennas are their excellent [directivity](Directional%20antenna.md), wider bandwidth than conventional resonant antennas, and the ability to clearly receive distant and overseas transmitters. Their disadvantages are very long physical size, requiring considerable land area, and because of the length, being unfeasible to rotate to different reception directions. As a work-around, antenna installations often use multiple Beverage antennas to provide wide azimuth coverage.

### Description

The Beverage antenna consists of a horizontal wire one-half to several wavelengths long, suspended close to the ground, usually 3 to 6 m (10 to 20 feet) high, pointed in the direction of the signal source. At the end toward the signal source, which the induced signal travels away from, the wire is shorted to ground through a resistor whose electrical resistance is close to the value of the characteristic impedance of the antenna wire (modeled as a transmission line), which is typically 400~800 Ohms. At the end that the arriving waves travel towards, the antenna is connected to the receiver through a transformer ("[balun](Balun.md)") to the receiver's [feed line](Antenna%20feed.md). The tranformer matches the antenna's 400~800 Ohm impedance to the line's impedance, conventionally either 50 or 75 Ohms.

### Operation

Unlike other wire antennas such as [dipole](Dipole%20antenna.md) or [monopole antennas](Monopole%20antenna.md) which are typically used on their resonant frequencies, with the radio currents traveling in both directions along the element, bouncing back and forth between the ends as standing waves, the Beverage antenna is a traveling wave antenna; the radio frequency current travels in one direction along the wire, in the same direction as the radio waves.  The lack of resonance gives it a wider bandwidth than resonant antennas. It receives vertically polarized radio waves, but unlike other vertically polarized antennas it is suspended horizontally and close to the ground, and requires some resistance in the ground to work.

The Beverage antenna relies on "wave tilt" for its operation. At low and medium frequencies, a vertically polarized radio frequency electromagnetic wave traveling close to the surface of the earth with finite ground conductivity sustains losses that are greater nearer the ground; the reduction near the ground causes the net wavefront to "tilt over" at a small angle. Where this happens, the electric field is no longer perpendicular to the ground, but inclined at an angle. Because of its inclination, the radio wave has a small component to its electric field parallel to the Earth's surface. The horizontal wire of the Beverage is suspended close to the Earth, and approximately parallel to the wave's direction, and the small horizontal electric field generates a horizontal wave of RF electrical current in the wire, propagating in the same direction as the external radio waves. The RF electrical current traveling along the wire add in phase and amplitude throughout the length of the wire, cumulatively producing the maximum signal strength where the current reaches the far end of the antenna, where the antenna wire connects to the matching transformer that smoothly feeds (no retro-reflection) the electrical current into the line to the receiver.

The antenna wire and the ground under it together can be thought of as a "leaky" transmission line which absorbs energy from the radio waves. The velocity of the electrical waves in the antenna wire is less than the speed of light through the air, due in part to capacitance between the wire and the nearby ground. The velocity of the wavefront along the wire is also less than the speed of light due to its angle. At a certain angle, θmax, the two velocities are equal. At this angle the gain of the antenna is maximum, so the radiation pattern has a main lobe at this angle. The angle of the main lobe is given by

$$
\ \theta_\mathsf{max} = \arccos\biggl(1 - \frac{\lambda}{\ 2\ \ell\ } \biggr)\ ,
$$

where  
$$\ \ell\ $$ is the length of the antenna wire,  
$$\ \lambda\ $$ is the receiving wavelength.

The antenna has a one-directional reception pattern, because RF signals coming from the direction behind the feedpoint, traveling toward the terminated far end, induce currents that propagate into the resistor and are shorted through it to the ground. The amount of resistance used for the termination is yet another instance of impedance matching, which prevents any unmatched part of signals from the unwanted direction from reflecting backwards off the far end, towards the feed point.

### Gain

While Beverage antennas have excellent directivity, because they are close to lossy Earth, they do not produce absolute [gain](Gain%20%28antenna%29.md); their gain is typically from −20 to −10 dBi. This is rarely a problem, because the antenna is used at frequencies where there are high levels of atmospheric radio noise: At these frequencies so far below the 10–20 MHz transition frequency in the middle shortwaves, weak signals from all antennas can be freely amplified in the receiver without adding any significant extra noise.

In long- and medium-waves, natural atmospheric noise is the limiting factor that sets the signal-to-noise ratio (SNR), rather than the noise generated by the receiver's own circuitry that is troublesome for VHF and UHF. The amplified signal retains the same strength, relative to the amplified noise, so an inefficient antenna such as a Beverage can be used for receiving, and the Beverage's excellent directivity becomes the deciding factor for good SNR: Noise comes from all directions, but although the Beverage receives all of the arriving signal, it only receives the small part of the noise coming from the same direction.

Directivity increases with the length of the antenna. Useful directivity begins to develop at a length of only ⁠1/ 4 ⁠ wavelength; it becomes more significant at one wavelength and improves steadily until the antenna reaches a length of about two wavelengths, depending on the soil and the antenna height. For Beverages longer than two wavelengths, its directivity no longer improves, since the slightly slower electrical waves in the antenna wire cannot remain in phase with the slightly faster radio waves in the air.

Although excellent receiving antennas, Beverage antennas are rarely used to transmit, since doing so would waste a large amount of transmitter power as heat in the terminating resistor.

### Implementation

A single-wire Beverage antenna is typically a single straight copper wire, between one-half and two wavelengths long, run parallel to the Earth's surface in the direction of the desired signal. The wire is suspended by insulated supports above the ground. A non-inductive resistor approximately equal to the characteristic impedance of the antenna wire, about 400~600 Ohms, is connected from the far end of the wire to a ground rod. The other end of the wire is connected to the feedline to the receiver.

A dual-wire variant is sometimes utilized for rearward null steering or for bidirectional switching. The antenna can also be implemented as an array of 2 to 128 or more elements in broadside, endfire, and staggered configurations, offering significantly improved directivity otherwise very difficult to attain at these frequencies. A four-element broadside / staggered Beverage array was used by AT&T at their longwave telephone receiver site in Houlton, Maine. Very large phased Beverage arrays of 64 elements or more have been implemented for receiving antennas for over-the-horizon radar systems.

The driving impedance of the antenna is equal to the characteristic impedance of the wire with respect to ground, somewhere between 400~800 Ohms, depending on the height of the wire and its thickness. On the opposite end of the wire, a matching transformer is typically used to join the high-impedance antenna wire to a low-impedance feedline to the receiver, most often either a 50 Ohm or 75 Ohm [coaxial cable](Coaxial%20cable.md), although high impedance line that matches the antenna's impedance was often used in the past.

---

*Source: Wikipedia, Beverage antenna (https://en.wikipedia.org/wiki/Beverage_antenna), by Wikipedia contributors, CC BY-SA 4.0.*
