# SMA connector

SMA connector

**Figure 1.** Standard male SMA connector: male body (inside threads) with male inner pin

- Type  RF coaxial connector
- General specifications
- Diameter  Male: 0.312 in (7.9 mm) HEX
- Cable  Coaxial
- Passband  Typically 0–18 GHz,  
some up to 26.5 GHz

**SMA** (*SubMiniature version A*) connectors are semi-precision coaxial RF connectors developed in the 1960s as a minimal connector interface for [coaxial cable](Coaxial%20cable.md) with a screw-type coupling mechanism. The connector has a 50 Ω impedance. SMA was originally designed for use from DC (0 Hz) to 12 GHz, but this has been extended over time and variants are available to 18 GHz and 26.5 GHz. There are also mechanically compatible connectors such as the K-connector which operate up to 40 GHz. The SMA connector is most commonly used in microwave systems, hand-held radio and mobile telephone antennas and, more recently, with WiFi antenna systems and USB [software-defined radio](Software-defined%20radio.md) dongles. It is also commonly used in radio astronomy, particularly at higher frequencies (5 GHz+).

### Connector design

The interface dimensions for SMA connectors are listed in MIL-STD-348. The SMA connector employs a 1⁄4 inch (6.35 mm) diameter, 36-thread-per-inch threaded barrel; the male is equipped with a captive hex nut measuring 5⁄16 inch (0.3125 inch / 7.9 mm) across opposite flats, thus taking the same wrench as a #6 SAE hex nut. The center pin is the same diameter as the center of RG402 Coax so that connections can be made with no impedance discontinuity.

The gender assignment of the SMA connector is determined by the outer conductor (the shield or screen), an SMA male connector has polytetrafluoroethylene (PTFE) dielectric flush with the end of the outer conductor while the mating female connector has a recessed dielectric and the conductor is sized to be a sliding fit over the male. The male connector also has a rotating nut or knurled barrel with an internal thread, while the female connector has a non-rotating external thread; the threads are for retention only with electrical contact made through the sliding conductors immediately adjacent to the dielectric.

A *standard-polarity* SMA male connector has a 0.9 mm diameter center pin projecting from the dielectric, while the standard SMA female connector has a center socket flush with the dielectric. There are also *reverse-polarity* ("RP") SMA connectors in which the pin and socket are swapped so that the male RP-SMA has a center socket flush with its dielectric, while the female RP-SMA has a center pin projecting from its dielectric: see below for a fuller description.

The SMA connector uses a polytetrafluoroethylene (PTFE) dielectric that contacts along the mating plane. Variability in the construction and the mating of the connectors limits the repeatability of the connector impedance. For that reason and because they are just rated for a limited number of connection cycles, an SMA connector is not usually a good choice for metrological applications.

SMA connectors are rated for up to 500 mating cycles, but to achieve this it is necessary to properly torque the connector when making the connection. A 5⁄16 inch torque wrench is required for this, set to 3–5 in·lbf (0.3 to 0.6 N·m) for brass, and 7–10 in·lbf (0.8 to 1.1 N·m) for stainless steel connectors. Flats are sometimes also provided on the cable side of the connector assembly so that a second wrench can be used to prevent it from rotating and damaging the joint to the cable. It is also advisable to inspect and clean out loose debris from the internal surfaces with compressed air or a gas duster can before mating.

SMA connectors must not be confused with the standard household 75-ohm type F coax connector (diameters: male 7⁄16 inch (11 mm) circular or hex; female 3⁄8 inch (9.5 mm) external threads), as there is only about a 2 mm difference overall in the specifications. Type F cannot be mated with SMA connectors without the use of an adapter.

### Variations

The SMA connector is typically rated for mode-free operation from DC to 18 GHz, though some proprietary versions are rated to 26.5 GHz. For performance above this, other SMA-like connectors are used. These include the 3.5 mm connector, rated to 34 GHz, and the 2.92 mm (also known as 2.9 mm, K type, or SMK), good up to 46 GHz. These connectors keep the same outside thread as the SMA, so they can potentially be cross-mated, but the precision connector can be easily damaged when mating with low-grade SMA connectors. The precision versions use an air dielectric with appropriately scaled center conductors.

Beyond 46 GHz, the 2.4 mm (also known as T type), 1.85 mm (also known as V type) and 1.0 mm (also known as W type) connectors exist. These are similar to the SMA connector, but with the geometries incompatibly scaled, and a metric thread to prevent accidental intermating. (But 2.4 mm and 1.85 mm connectors are compatible to each other.) These offer mode-free operation to 50, 65, and 110 GHz respectively.

### Reverse polarity

Reverse-polarity SMA (RP-SMA or RSMA) is a variation of the SMA connector specification that reverses the gender of the interface, as shown in Figures 1 and 2. The term "reverse polarity" here refers only to the gender of the connector's contact pin, not in any way to the signal polarity.

The female RP-SMA connector has the same external housing as a standard or conventional female SMA connector, which consists of an outer shell with the threads on the outside; however, the center receptacle is replaced by a male pin.

Similarly, the RP-SMA male has threads on the inside like a conventional male, but has a center receptacle instead of the male pin in the middle. Normal SMA connectors are incompatible with RP-SMA connectors.

Occasionally, the opposite convention is used to designate the gender of an RP connector: In this situation the female connector has a socket (or sleeve) contact and threads on the outside. Users should take care to check drawings and specifications carefully.

- Center pin   Center receptacle
- Internal thread   SMA male/plug   RP-SMA male/plug
- External thread   RP-SMA female/jack   SMA female/jack

Wi-Fi equipment manufacturers have widely used RP-SMA connectors to comply with specific national regulations, such as those from the FCC, which are designed to prevent consumers from connecting antennas that provide additional gain and therefore breach Part 15 compliance. However, by 2000, the FCC regarded the connectors as readily available, though delaying its ruling indefinitely. As of 2018, leading manufacturers such as Netgear and Linksys are still using RP-SMA connectors on their Wi-Fi equipment.

---

*Source: Wikipedia, SMA connector (https://en.wikipedia.org/wiki/SMA_connector), by Wikipedia contributors, CC BY-SA 4.0.*
