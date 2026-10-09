# Twin-lead

**Twin lead** cable is a two-conductor flat cable used as a balanced transmission line to carry radio frequency (RF) signals. It is constructed of two, stranded copper wires, or solid copper-clad steel wires. The wires are held a fixed distance apart by a plastic ribbon that is a good insulator at radio frequencies (usually polyethylene). It is also called (two wire) **ribbon cable**. The uniform spacing of the wires is the key to the cable's function as a transmission line: Any abrupt change in spacing would cause some of the signal to reflect back toward the source, rather than passing through. The plastic also covers and insulates the wires.

The name **twin lead** is most often used to refer specifically to 300 Ω (Ohm) ribbon cable, the most common type, but on occasion, *twin lead* is used to refer to any type of **parallel wire line**. Parallel wire line is available with several different values of characteristic impedance such as *twin lead ribbon cable* (75 or 300 Ω), *window line* (300 Ω, 350 Ω, or 450 Ω), and *open wire line* or *ladder line* (500~650 Ω).

Twin lead is mainly used as an antenna feedline at shortwave and [VHF](Very%20high%20frequency.md) frequencies, to connect [radio receivers](Radio%20receiver.md) and transmitters to their [antennas](Antenna%20%28radio%29.md). It can have significantly lower signal loss than flexible [coaxial cable](Coaxial%20cable.md), the main alternative type of feedline at these frequencies; for example, type RG-58 coaxial cable loses 6.6 dB per 100 metres (330 ft) at 30 MHz, while 300 Ω twin-lead loses only 0.55 dB. 300 Ω twin lead is widely used to connect FM radios to their antennas, and was previously used to connect television antennas to televisions until it was replaced by coaxial cable.

The reason for the fallen popularity of parallel-wire cable came about in part because of an influx of inexpensive military surplus coaxial cable, which is far easier to use: Parallel-wire cable is unshielded, so much more vulnerable to interference; proximity to metal objects will inject signals into any type of parallel wire line that would be blocked out by more convenient / more popular shielded [coaxial cable](Coaxial%20cable.md). Those same metal objects will also distort the impedance of unshielded cable running near them, causing some signal power to be reflected backwards from that point along the line. Twin-lead therefore requires wide routing around rain gutters, and spacing away from metal fences, exterior wall siding, and metal roofs, and to be mounted on 1~2 foot standoff insulators when run up the sides of metal antenna masts.

### Characteristics and uses

Twin lead and other types of parallel-conductor transmission line are mainly used to connect radio transmitters and [receivers](Radio%20receiver.md) to their [antennas](Antenna%20%28radio%29.md). Parallel transmission line has the advantage that its losses per unit length are an order of magnitude smaller than that of [coaxial cable](Coaxial%20cable.md), the main alternative form of transmission line. Its disadvantages are that it is more vulnerable to interference, and must be kept away from metal objects which can cause power losses and impedance distortion (hence back-reflected waves). For this reason, when installed along the outside of buildings and on antenna masts, standoff insulators must be used. It is also common practice to twist the twin lead on long free standing lengths to further average out any imbalance induced on the line.

**Parallel-wire line** (the generic sense of *twin lead*) is supplied in several different sizes, with characteristic impedance values of

- 600 Ω, 500 Ω (ladder line),
- 450 Ω, 350 Ω (window line),
- 300 Ω (window line, ribbon cable), and
- 75 Ω (ribbon cable).

300 Ω twin-lead ribbon cable was the most common type in the middle-20th century, when it was widely used to connect television sets and FM radios to their receiving antennas. Since the last quarter of the middle-20th century, 300 Ω twin lead ribbon cable has been largely replaced with 75 Ω [coaxial cable](Coaxial%20cable.md) for television installations. Multiple forms of parallel wire line are used in [amateur radio](Amateur%20radio.md) stations as feedline for balanced transmission of radio frequency signals, most often as 450 Ω window line, instead of twin lead ribbon cable.

The characteristic impedance of twin lead is a function of the insulating material and its thickness, and the wire diameter and its spacing; in the most common type, 300 Ω twin-lead ribbon cable, the wire is usually AWG 20 or 22 (0.52 or 0.33 mm), about 7.5 millimetres (0.30 in) apart. This is well matched with the natural impedance of a folded dipole antenna, which is normally around 275 Ω. Twin lead generally has higher impedance than the other common transmission wiring, [coaxial cable](Coaxial%20cable.md) (coax). The widely used RG-6 coax has a characteristic impedance of 75 Ω, which requires the use of a [balun](Balun.md) to match impedance when used with common antenna types.

### How it works

**Twin lead** (in the specific sense of ribbon cable) is a form of parallel wire balanced transmission line. The separation between the two wires in twin-lead is small compared to the wavelength of the radio frequency (RF) signal carried on the wire. The RF current in one wire is equal in magnitude and opposite in direction to the RF current in the other wire. Therefore, in the far field region far from the transmission line, the radio waves radiated by one wire are equal in magnitude but opposite in phase (180° out of phase) to the waves radiated by the other wire, so the overlapping opposite waves cancel each other out. The result is that almost no net radio energy is radiated by the line.

Similarly, any interfering external radio waves will induce equal, in phase RF currents, traveling in the same direction, in the two wires, as long as they each maintain the same impedance. Since the load at the destination end is connected *across* the wires, nominally, only *differential*, oppositely-directed currents in the wires create a current in the load. Thus the interfering currents are canceled out, so twin lead does not tend to pick up radio noise.

However, if a piece of metal is located sufficiently close to a twin-lead line, within a distance comparable to the wire spacing, it will be significantly closer to one wire than the other. As a result, the RF current induced in the metal object by one wire will be greater than the opposing current induced by the other wire, so the currents will no longer cancel. Thus nearby metal objects can cause power losses in twin lead lines, through energy dissipated as heat by induced currents. Similarly, radio noise originating in cables or metal objects located near the twin-lead line can induce unbalanced currents in the wires, coupling noise into the line. Therefore, the line must be kept at a distance from metal objects such as metal roofs or siding, house wiring, gutters, and antenna masts.

In order to prevent power from being reflected from the load end of the line, causing high [SWR](Standing%20wave%20ratio.md) and inefficiency, the load must have an impedance which matches the characteristic impedance of the line. This causes the load to appear electrically identical to a continuation of the line, preventing reflections. Similarly, to transfer power efficiently into the line, the source must also match the characteristic impedance. To connect a balanced transmission line to an unbalanced line like [coaxial cable](Coaxial%20cable.md), a device called a [balun](Balun.md) must be used.

### Window line and ladder line

In addition to twin lead ribbon cable, two-conductor parallel wire line comes in two additional forms: **window line** and **ladder line** (a.k.a. *open wire line*).

#### Window line

**Window line** is a bulkier variety of parallel wire line than twin lead ribbon cable; it is similarly built to a wider size, except that the polyethylene ribbon between them holding the wires apart has regularly spaced rectangular openings ("windows") cut in it.

Among the advantages to cutting "windows" in the ribbon is that the manufacturer can adjust the size of the cuts to make fine adjustments to the feedline's electrical properties. The windows lighten the line, and reduce the amount of surface on which dirt and moisture can accumulate, making window line somewhat less vulnerable to weather-induced changes in its characteristic impedance. The most common type is nominal 450 Ω window line, which has a conductor spacing of about an inch (25 mm); its actual impedance may be closer to 400 Ω. It is also made in nominal 350 Ω impedance (which may actually be closer to 300 Ω).

#### Ladder line

**Ladder line** is an older, simpler form of parallel-wire line, often called **open wire line**. The configuration looks like a rope ladder, hence the name. It can either be purchased already made by a cable company, or home-made; the construction is easy, though tedious, and originally all radio amateurs made their own open wire line. It consists of two wires, usually either clad in a DC insulator or coated with a durable lacquer, held a constant distance apart by insulated spacers.

The "ladder rung" spacers can be made out of any convenient insulating material – at present, usually short pieces cut from plastic plumbing pipe – formerly either long, thin ceramic insulators or dowel stubs of water-proofed wood were used. The "rungs" hold the wires at constant spacing, somewhere between a constant two to 5 inches (13 cm) apart, depending on the wire and the desired impedance. The rungs are spaced about every 5 to 12 inches (13–30 cm). Although it is important to ensure the wire separation is uniform, it doesn't matter if distances between the rungs is erratic, as long as the separation remains nearly constant in gusts of wind.

The ratio of chosen wire spacing to wire diameter determines the line's characteristic impedance – usually 500~600 Ω, but also depends on the wire insulation's relative permittivity and conductive loss in the rung insulators, if significant. For example, for a 500 Ω line, two bare or lacquered wires should be spaced 32× the wires' individual diameters apart – about 4 inches (10 cm) in the case of common ⁠1/ 8 ⁠″ diameter wire (0.125 inches (3 mm)). If the wires are insulated, the separation may need to be a little wider, depending on the insulating plastic. To get 600 Ω parallel line, the same wires would be spaced 9 inches (23 cm); 600 Ω is roughly the practical limit for transmission lines made with wire rather than thicker copper-clad steel cable, or with rigid aluminum or copper pipe.

### Impedance matching

As a transmission line, transmission efficiency will be maximum when the impedance of the antenna, the characteristic impedance of the twin-lead line and the impedance of the equipment are the same. For this reason, when attaching a twin-lead line to a coaxial cable connection, such as the 300 Ω twin-lead from a domestic television antenna to the television's 75 ohm coax antenna input, a [balun](Balun.md) with a 4:1 ratio is commonly used. Its purpose is double: First, it transforms twin-lead's 300 Ω impedance to match the 75 Ω coaxial cable impedance; and second, it transforms the balanced, symmetric transmission line to the nominally unbalanced coax input. In general, when used as a feedline, twin-lead (especially ladder line versions) has a higher efficiency than coaxial cable when there is an impedance mismatch between the feedline and the source (or sink). For receive-only use this merely implies that the system can communicate under slightly less optimal conditions; for transmit use, this can often result in significantly less energy lost as heat in the transmission line.

Twin-lead also can serve as a convenient material with which to build a simple [folded dipole](Dipole%20antenna.md) antenna. Such antennas may be fed either by using a 300 Ω twin-lead feeder or by using a 300-to-75 Ω balun and using coaxial feedline and will usually handle moderate power loads without overheating.

### Characteristic impedance

The characteristic impedance of a parallel-wire transmission line like twin lead or ladder line depends on its dimensions; the diameter of the wires $$\ d\ $$ and their separation $$\ D ~.$$ This is derived below.

The characteristic impedance $$\ Z_\mathsf{o}\ $$ of any transmission line operating at frequency $$\ f\ $$ or radian frequency $$\ \omega = 2\ \pi\ f \ ,$$ is given by

$$
Z_\mathsf{o} = \sqrt{ \frac{R + j\ \omega\ L }{\; G + j\ \omega\ C\;}\ }
$$

where for twin-lead line the primary line constants are

$$
R = \frac{\ 2\ R_\mathsf{s}\ }{ \pi\ d }
$$

$$
L = \frac{\mu}{\ \pi\ }\ \operatorname{arcosh} \left( \frac{\ D\ }{d} \right)
$$

$$
G = \frac{ \pi\ \sigma }{\ \operatorname{arcosh} \left( \frac{\ D\ }{d} \right)\ }
$$

$$
C = \frac{\ \pi\ \varepsilon\ }{\ \operatorname{arcosh} \left( \frac{\ D\ }{d} \right)\ }
$$

where $$\ d\ $$ is the wire diameter and $$\ D\ $$ is the separation of the wires measured between their centre-lines; $$\ \epsilon\ $$ is the absolute permittivity between the wires; $$\ \mu\ $$ is the absolute permeability; $$\ \sigma\ $$ is the surface conductivity between the wires; and where the surface resistance of the wires is given by

$$
R_\mathsf{s} = \sqrt{ \frac{\ \pi\ f\ \mu_\mathsf{c}\ }{ \sigma_\mathsf{c} } \; } ~.
$$

Neglecting the wire resistance $$\ R\ $$ and the leakage conductance $$\ G\ ,$$ this gives

$$
Z_\mathsf{o} = \frac{ \zeta_\mathsf{o} }{\ \pi \sqrt{\varepsilon_\mathsf{R}\ }\ }\ \operatorname{arcosh}\left( \frac{\ D\ }{d} \right) = \frac{ \zeta_\mathsf{o} }{\ \pi \sqrt{\varepsilon_\mathsf{R}\ }\ }\ \ln\!\Biggl[ \left( \frac{\ D\ }{ d } \right)\!\left( 1 + \sqrt{\ 1 - \left( \tfrac{ d }{\ D\ } \right)^2 ~}~ \right) \Biggr]\ 
$$

$$
\quad = \frac{ \zeta_\mathsf{o} }{\ \pi \sqrt{\varepsilon_\mathsf{R}\ }\ }\ \Biggl[\ \ln \left( \frac{\ 2\ D\ }{ d } \right) + \ln \left[\ \tfrac{\ 1\ }{ 2 } \left(\ 1 + \sqrt{ 1 - \left( \tfrac{ d }{\ D\ } \right)^2 ~}\; \right) \right] \Biggr]\ 
$$

$$
\quad = \frac{ \zeta_\mathsf{o} }{\ \pi \sqrt{\varepsilon_\mathsf{R}\ }\ } \left[\ \ln\left( \frac{\ 2\ D\ }{ d } \right) - \left( \frac{d}{\ 2\ D\ } \right)^2 - \operatorname{\mathcal{O}} \left\{\left( \tfrac{d}{\ 2\ D\ } \right)^4 \right\}\ \right]
$$

$$
\quad \approx \frac{\ 119.92\ \mathsf\Omega\ }{ \sqrt{\varepsilon_\mathsf{R}\ } } \left[ \ln \left( \frac{\ 2\ D\ }{d} \right) - \left( \frac{d}{\, 2\,D\,} \right)^2 \right] \approx \frac{\ 119.92\ \mathsf\Omega\ }{ \sqrt{ \varepsilon_\mathsf{R}\ } }\ \ln\left(\frac{\ 2\ D\ }{d} \right) ~.
$$

where $$\ \zeta_\mathsf{o}\ $$ is the impedance of free space (approximately 376.74 Ω), and $$\ \varepsilon_\mathsf{R}\ $$ is the relative permittivity (which for air is 1.00054).

When the separation $$\ D\ $$ is many times greater than the wire diameter $$\ d\ $$ then the  arcosh  function can be approximately replaced by a natural logarithm (with its argument doubled):

$$
Z_\mathsf{o} = \frac{ 119.92\ \mathsf{\Omega} }{\ \sqrt{\varepsilon_\mathsf{R}\ }\ }\ \operatorname{arcosh}\left( \frac{\ D\ }{ d } \right) \approx \frac{\ 119.92\ \mathsf{\Omega}\ }{\ \sqrt{ \varepsilon_\mathsf{R}\ }\ }\ \ln \left( \frac{\ 2\ D\ }{d} \right) \approx \frac{\ 276.13\ \mathsf\Omega\ }{\sqrt{ \varepsilon_\mathsf{R}\ } }\ \log_{10} \left( \frac{\ 2\ D\ }{d} \right) ~.
$$

The exact and approximate formulas for the separation needed to achieve some given characteristic impedance $$\ Z_\mathsf{o}\ $$ through a pair of wires are therefore

$$
D = d\ \cosh \left( \frac{\ \pi\ Z_\mathsf{o} \sqrt{\varepsilon_\mathsf{R}\ }\ }{ \zeta_\mathsf{o} } \right) \approx \tfrac{\ 1\ }{ 2 }\ d\ \exp \left( \frac{\ Z_\mathsf{o} \sqrt{\varepsilon_\mathsf{R}\ }\ }{\ 119.92\ \mathsf{\Omega}\ } \right) ~.
$$

The dielectric material between the two conductors with either twin-lead or ladder line is not *all* air: The effect of a "mixed" dielectric, part air and part polyethylene or other plastic, is that the actual impedance will fall somewhere between the value calculated assuming all air or all polyethylene. Carefully measured or published values for $$\ Z_\mathsf{o}\ $$ will typically be more accurate than estimates from formulas.

### Antennas

Twin-lead can be connected directly to a suitably designed antenna:

**Windom antenna**  — A multiply-resonant antenna whose resonant impedances cluster around 300 Ω.

**[Folded dipole](Dipole%20antenna.md)**  — Double-wire dipole whose characteristic impedance in free space is around 300 Ω.

**[Dipole](Dipole%20antenna.md)**  — Although the center impedance at resonance is approximately 73 Ω in free space, in actual use it varies between 30 and 100 Ω, depending on height above ground, so with high-impedance feedline a T-match or Y-match feed will probably be necessary.

**[Yagi–Uda antenna](Yagi%20Uda%20antenna.md)**  — Yagi and the simpler [Moxon antenna](Moxon%20antenna.md), and other [directional antennas](Directional%20antenna.md); some special impedance matching arrangement at the feedpoint is necessary for any cabling, since interference between the typically close-spacing of the parallel near-resonant antenna segments causes low feedpoint resistance as well as making the antenna more directional.

---

*Source: Wikipedia, Twin-lead (https://en.wikipedia.org/wiki/Twin-lead), by Wikipedia contributors, CC BY-SA 4.0.*
