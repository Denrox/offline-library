# Rubber ducky antenna

The **rubber ducky antenna** (or rubber duck aerial) is an electrically short [monopole antenna](Monopole%20antenna.md), invented by Richard B. Johnson, that functions somewhat like a base-loaded [whip antenna](Whip%20antenna.md). It consists of a springy wire in the shape of a narrow helix, sealed in a rubber or plastic jacket to protect the antenna. The rubber ducky antenna is a form of normal-mode [helical antenna](Helical%20antenna.md).

Electrically short antennas like the rubber ducky are used in portable handheld radio equipment at [VHF](Very%20high%20frequency.md) and UHF frequencies in place of a quarter-wavelength [whip antenna](Whip%20antenna.md), which is inconveniently long and cumbersome at these frequencies. Many years after its invention in 1958, the rubber ducky antenna became the antenna of choice for many portable radio devices, including [walkie-talkies](Walkie-talkie.md) and other portable [transceivers](Transceiver.md), scanners and other devices where safety and robustness take precedence over electromagnetic performance. The rubber ducky is quite flexible, making it more suitable for handheld operation, especially when worn on the belt, than earlier rigid telescoping antennas.

### Origin of the name

The term rubber duck stems from the rubberized protective coating commonly seen on handheld radios and police radios. An alternative name is based on the short stub format: the "stubby antenna".

### Description

Before the rubber ducky, antennas on portable radios usually consisted of quarter-wave [whip antennas](Whip%20antenna.md), rods whose length was one-quarter of the wavelength of the radio waves used. In the [VHF](Very%20high%20frequency.md) range where they were used, these antennas were 0.6 or 0.9 m (2 or 3 feet) long, making them cumbersome. They were often made of telescoping tubes that could be retracted when not in use. To make the antenna more compact, electrically short antennas, shorter than one-quarter wavelength, began to be used. Electrically short antennas have considerable capacitive reactance, so to make them [resonant](Antenna%20%28radio%29.md) at the operating frequency an inductor (loading coil) is added in series with the antenna. Antennas which have these inductors built into their bases are called base-loaded whips.

The rubber ducky is an electrically short quarter-wave antenna in which the inductor, instead of being in the base, is built into the antenna itself. The antenna is made of a narrow helix of wire like a spring, which functions as the needed inductor. The springy wire is flexible, making it less prone to damage than a stiff antenna. The spring antenna is further enclosed in a plastic or rubber-like covering to protect it. The technical name for this type of antenna is a [normal-mode helix](Helical%20antenna.md). Rubber ducky antennas are typically 4% to 15% of a wavelength long; that is, 16% to 60% of the length of a standard quarter-wave whip.

### Effective aperture

Because the length of this antenna is significantly smaller than a wavelength the effective aperture, if 100% efficient, would be approximately:

$$
A_e = \frac{3 \lambda ^2 }{8 \pi}
$$

Like other electrically short antennas the rubber ducky has poorer performance (less gain) due to losses and thus considerably less gain than a quarter-wave whip. However it has somewhat better performance than an equal length base loaded antenna. This is because the inductance is distributed throughout the antenna and so allows somewhat greater current in the antenna.

### Performance

Rubber ducky antennas have lower gain than a full size quarter-wavelength antenna, reducing the range of the radio. They are typically used in short-range two way radios where maximum range is not a requirement. Their design is a compromise between antenna gain and small size. They are difficult to characterize electrically because the current distribution along the element is not sinusoidal as is the case with a thin linear antenna.

In common with other inductively loaded short monopoles, the rubber ducky has a high Q factor and thus a narrow bandwidth. This means that as the frequency departs from the antenna's designed center frequency, its [SWR](Standing%20wave%20ratio.md) increases and thus its efficiency falls off quickly. This type of antenna is often used over a wide frequency range, e.g. 100–500 MHz, and over this range its performance is poor, but in many mobile radio applications there is sufficient excess signal strength to overcome any deficiencies in the antenna.

### Design rules

- If the coils of the spring are wide (a large diameter), relative to the length of the array, the resulting antenna will have narrow bandwidth.
- Conversely, if the coils of the spring are narrow, relative to the length of the array, the resulting antenna will have its largest possible bandwidth.
- If the antenna is resonant, and the spring has a large diameter, the impedance will be well below 50 Ω, tending towards 0 Ω with large inductors as the structure starts to resemble a series-tuned circuit with little radiation resistance.
- If the antenna is resonant, and the spring has a small diameter, the impedance will increase towards 70 Ω.

From these rules, one can surmise that it is possible to design a rubber ducky antenna that has about 50 Ω impedance at its feed-point, but a compromise of bandwidth may be necessary. Modern rubber ducky antennas such as those used on cell phones are tapered in such a way that few performance compromises are necessary.

### Variations

Some rubber ducky antennas are designed quite differently than the original design. One type uses a spring only for support. The spring is electrically shorted out. The antenna is therefore electrically a linear element antenna. Some other rubber ducky antennas use a spring of non-conducting material for support and comprise a collinear array antenna. Such antennas are still called rubber ducky antennas even though they function quite differently (and often better) than the original spring antenna.

---

*Source: Wikipedia, Rubber ducky antenna (https://en.wikipedia.org/wiki/Rubber_ducky_antenna), by Wikipedia contributors, CC BY-SA 4.0.*
