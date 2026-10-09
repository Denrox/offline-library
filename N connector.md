# N connector

Type N

Type N connector (male)

- Type  RF coaxial connector
- Production history
- Designer  Paul Neill
- Designed  1940s
- General specifications
- Diameter  **Male:** 2.03 cm (0.80 in)  
**Female:** 1.57 cm (0.62 in)  
*(outer, typical)*
- Cable  [Coaxial cable](Coaxial%20cable.md)
- Passband  0–11 GHz, often up to 18 GHz

The **N connector** (also, **type-N connector**) is a threaded, weatherproof, medium-size RF connector used to join [coaxial cables](Coaxial%20cable.md). It was one of the first connectors capable of carrying microwave-frequency signals, and was invented in the 1940s by Paul Neill of Bell Labs, after whom the connector is named.

### Design

The interface specifications for the N and many other connectors are referenced in MIL-STD-348. Originally, the connector was designed to carry signals at frequencies up to 1 GHz in military applications, but today's common Type N easily handles frequencies up to 11 GHz. More recent precision enhancements to the design by Julius Botka at Hewlett-Packard have pushed this to 18 GHz. The male connector is hand-tightened (though versions with a hex nut are also available) and has an air gap between the center and outer conductors. The coupling has a 5⁄8-24 UNEF thread. Amphenol suggests tightening to a torque of 15 inch-pounds (1.7 N⋅m), while Andrew Corporation suggest 20 inch-pounds (2.3 N⋅m) for their hex nut variant. As torque limit depends only on thread quality and cleanliness, whereas the main operational requirement is good RF contact without significant steps or gaps, these values should be seen as indicative rather than critical.

### Power rating

The *peak* power rating of an N connector is determined by voltage breakdown/ionisation of the air near the center pin. The *average* power rating is determined by overheating of the centre contact due to resistive insertion loss, and thus is a function of frequency. Typical makers' curves for a new clean connector with a perfect load (VSWR=1.0) give limits of ≈5000 W at 20 MHz and ≈500 W at 2 GHz. This square root frequency derating law is expected from the skin depth decreasing with frequency. At lower frequencies the same maker recommends an upper bound of ≈1000 V RMS. To achieve reliable operation in practice over an extended period, a safety factor of 5 or more is not uncommon, particularly when generic parts may be substituted, or the operating environment is likely to lead to eventual tarnishing of the contacts.

### Impedance options

The N connector follows MIL-STD-348, a standard defined by the US military, and comes in 50 and 75 ohm versions. The 50 ohm version is widely used in the infrastructure of land mobile, wireless data, paging and cellular systems. The 75 ohm version is primarily used in the infrastructure of cable television systems. Connecting these two different types of connectors to each other can lead to damage, and/or intermittent operation due to the difference in diameter of the center pin.

Unfortunately, many type N connectors are not labeled, and it can be difficult to prevent this situation in a mixed impedance environment. The situation is further complicated by some makers of 75 ohm sockets designing them with enough spring yield to accept the larger 50 ohm pin without irreversible damage, while others do not. In general a 50 ohm socket is not damaged by a 75 ohm pin, but the loose fit means the contact quality is not guaranteed; this can cause poor or intermittent operation, with the thin 75 ohm male pin only barely mating with the larger 50 ohm socket in the female.

The 50 ohm type N connector is favored in microwave applications and microwave instrumentation, such as spectrum analyzers. 50 ohm N connectors are also commonly used on [amateur radio](Amateur%20radio.md) devices (e.g., [transceivers](Transceiver.md)) operating in UHF bands.

### Variations

#### SnapN

**SnapN** was originally designed by Rosenberger Hochfrequenztechnik in 2006 and is a quick locking replacement for the threaded interface of the widely applied Type N connector. Though part of the Quick Lock Formula Alliance (QLF), engineers at Rosenberger independently designed the SnapN in order to correct the performance problems of QLF's version of the quick lock N connector, QN. This design achieves better electronic performance because, unlike the QN, this new version maintains the basic structural parameters of the original Type N in which the inner dimensions of the outer conductor are 7.00 mm, and the inner conductor's outer dimensions are 3.04 mm. A male N-connector can plug into a female SnapN.

#### Left-hand thread

The left-hand thread, or reverse thread, uses the same 5⁄8-24 UNEF thread size but threaded in the opposite direction. These are used for some wireless LAN systems.

#### Reverse-polarity N

The reverse-polarity connectors use the same outer shell, but change the gender of the inner pin. These are used for some wireless LAN systems.

#### HN

The **HN** connector is slightly larger (¾"-20 thread) and is designed for high-voltage applications.

### Applications

Type N connectors find wide use in many lower frequency microwave systems, where ruggedness and/or low cost are needed. Many spectrum analyzers use such connectors for their inputs, and antennas which operate in the 0-11 GHz range often connect to a coaxial cable with type N connections.

N connectors were historically used with 10BASE5 "thicknet" Ethernet. Some Medium Attachment Units had both male and female N connectors, allowing the MAU to come in between two N connector-capped thick coaxial cables for effective passthrough. However, MAU attachment to uninterrupted cables via vampire taps was more typical.

---

*Source: Wikipedia, N connector (https://en.wikipedia.org/wiki/N_connector), by Wikipedia contributors, CC BY-SA 4.0.*
