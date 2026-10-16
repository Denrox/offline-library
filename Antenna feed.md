# Antenna feed

A radio transmitter or [receiver](Radio%20receiver.md) is connected to an [antenna](Antenna%20%28radio%29.md) which emits or receives the radio waves. The **antenna feed system** or **antenna feed** is the cable or conductor, and other associated equipment, which connects the transmitter or receiver with the antenna and makes the two devices compatible. In a radio transmitter, the transmitter generates an alternating current of radio frequency, and the feed system feeds the current to the antenna, which converts the power in the current to radio waves. In a radio receiver, the incoming radio waves excite tiny alternating currents in the antenna, and the feed system delivers this current to the receiver, which processes the signal.

To transfer radio frequency current efficiently, the *feedline* connecting the transmitter or receiver to the antenna must be a special type of cable called transmission line. At microwave frequencies, waveguide is often used, which is a hollow metal pipe carrying radio waves. In a parabolic (dish) antenna the feed is usually also defined to include the *feed antenna (feed horn)* which emits or receives the radio waves. Particularly in transmitters, the feed system is a critical component which impedance matches the antenna, feedline, and transmitter. To accomplish this, the feed system may also include circuits called *antenna tuning units* or *matching networks* between the antenna and feedline and the feedline and transmitter. On an antenna the *feed point* is the point on the driven antenna element at which the feedline is connected.

### Components

In a transmitter, the antenna feed is considered to be all components between the transmitter's final amplifier and the antenna's feedpoint. In a receiver, it is all components between the antenna and the receiver's input terminals. In some cases such as parabolic dishes it is also defined to include the feed antenna or feed horn.

In some radios the antenna is attached directly to the transmitter or receiver, such as the [whip antennas](Whip%20antenna.md) mounted on walkie talkies and portable FM radios, the sleeve [dipole antennas](Dipole%20antenna.md) of wireless routers, and the PIFA antennas inside cellphones. In this case the feed system just consists of an impedance matching circuit (if needed) between the antenna and transmitter or receiver, which matches the impedance of the antenna to the radio.

In other cases the antenna is located separately from the transmitter or receiver, such as broadcast television antennas and satellite dishes mounted on the roofs of residences, the sector antenna on cell towers of cellular base stations, the rotating radar antennas at airports, and the antenna towers of radio and television stations. In this case the antenna is connected to the transmitter or receiver with a cable called a feedline. To carry the radio frequency (RF) current efficiently, the feedline is made of specialized cable called transmission line. The advantage of transmission line is that it has a uniform characteristic impedance to avoid abrupt impedance steps which cause the radio energy to be reflected backward down the line. The main types of transmission line are parallel wire line (Twin lead), [coaxial cable](Coaxial%20cable.md), and for microwaves waveguide.

### Feed line

In a radio [antenna](Antenna%20%28radio%29.md), the **feed line** (**feedline**), or **feeder**, is the cable or other transmission line that connects the antenna with the radio transmitter or [receiver](Radio%20receiver.md). In a transmitting antenna, it feeds the radio frequency (RF) current from the transmitter to the antenna, where the energy in the current is radiated as radio waves. In a receiving antenna it transfers the tiny RF voltage induced in the antenna by the radio wave to the receiver. In order to carry RF current efficiently, feed lines are made of specialized types of cable called transmission line. The most widely used types of feed line are [coaxial cable](Coaxial%20cable.md), [twin-lead](Twin-lead.md), ladder line, and at microwave frequencies, waveguide.

Particularly with a transmitting antenna, the feed line is a critical component that must be adjusted to work correctly with the antenna and transmitter. Each type of transmission line has a specific characteristic impedance. This must be matched to the impedance of the antenna and the transmitter, to transfer power efficiently to the antenna. If these impedances are not matched it can cause a condition called standing waves on the feed line, in which the RF energy is reflected back toward the transmitter, wasting energy and possibly overheating the transmitter. This adjustment is done with a device called an [antenna tuner](Antenna%20tuner.md) in the transmitter, and sometimes a matching network at the antenna. The degree of mismatch between the feedline and the antenna is measured by an instrument called an SWR meter (standing wave ratio meter), which measures the *[standing wave ratio](Standing%20wave%20ratio.md)* (SWR) on the line.  
Cabling characteristics of a  
few common feedline types
- Cable  
type   Nominal impedance  
(Ω)   Velocity  
factor  
(% c)
- [radio coax](Coaxial%20cable.md)   50   66 (solid)  
80 (foam)
- [video coax](Coaxial%20cable.md)   75
- [twin-lead](Twin-lead.md)  
ribbon line   300   82
- [window line](Twin-lead.md)   450   95–99
- ladder line  
open wire line   500–600

#### Twin-lead

Source:

Twin lead is used to connect FM radios and television receivers with their antennas, although it has been largely replaced in the latter application by coaxial cable, and as a feedline for low power transmitters such as [amateur radio](Amateur%20radio.md) transmitters. It consists of two wire conductors running parallel to each other with a precisely constant spacing, molded in polyethylene insulating material in a flat ribbon-like cable. The distance between the two wires is small relative to the wavelength of the RF signal carried on the wire. The RF current in one wire is equal in magnitude and opposite in direction to the RF current on the other wire. Thus, far from the line, the radio waves radiated by one wire will be opposite in phase and will cancel the waves radiated by the other wire.

For the same reason, twin lead is also largely immune to radio noise and radio frequency interference (RFI), as long as both wires are kept equally far from any large metal objects or other parallel wires. Any unwanted external radio waves induce equal magnitude currents in the same direction (in phase) on both wires. Since as long as the receiver input is balanced it only responds to differential (opposite) currents, the noise currents are cancelled out.

Twin lead is commonly called a type of "balanced line", however, this needs to be moderated with common sense: All types of cabling, either parallel wire or coaxial, are able to carry balanced current, and all can carry unbalanced current, which will radiate. For that reason every type of feedline requires some attention to make it "balanced", and can become "unbalanced" if neglected; all should be fed with balanced current and connected through current-type [baluns](Balun.md) (or "line isolators") at a few points along the line, to remove the noise brought in as unbalanced current.

#### Coaxial cable

Coaxial cable is probably the most widely used type of feedline, used for frequencies below the microwave (SHF) range. It consists of a wire center conductor and a braided or solid metallic "shield" conductor, usually copper or aluminum surrounding it. The center conductor is separated from the outer shield by a dielectric, usually plastic foam, to keep the separation between the two conductors precisely constant. The shield is covered with an outer plastic insulation jacket. In *hard coax* cable, used for high power transmitting applications like television transmitters, the shield is a rigid or flexible metal pipe containing a compressed gas such as nitrogen, and the internal conductor is held centered with periodic plastic spacers.

Coax is called "unbalanced line", since the shield conductor is usually connected to electrical ground, however the currents that flow along the center conductor are balanced by opposite currents that skim along the interior surface of the shield; only the current flowing on the exterior surface of the coaxial shield is actually unbalanced. If that current can be blocked, then the coax becomes a "balanced line". Coaxial cable's great advantage is that the enclosing shield conductor isolates the cable's interior currents from external electromagnetic fields. If the currents flowing on external surface are blocked, coax becomes unaffected by nearby metal objects and immune to interference.

#### Waveguide

Waveguide is used at microwave (SHF) frequencies, at which other types of feedline have excessive power losses. A waveguide is a hollow metallic conductor or pipe. It can have a circular or square cross-section. Waveguide runs are often pressurized with nitrogen gas to keep moisture out. The RF signal travels through the pipe similarly to the way sound travels in a tube. The metal walls keep it from radiating energy outwards and also prevent interference from entering the waveguide. Because of the cost and maintenance waveguide entails, microwave antennas often have the output stage of the transmitter or the RF front end of the receiver located at the antenna, and the signal is fed to or from the rest of the transmitter or receiver at a lower frequency, using coaxial cable. A waveguide is considered an unbalanced transmission line.

### Impedance matching

Particularly with a transmitting antenna, the antenna feed is a critical component that must be adjusted to function compatibly with the antenna and transmitter. The transmitter output terminals, the transmission line, and the antenna each has a specific characteristic impedance, which is the ratio of voltage to current at the terminals of the device. To transfer maximum power between the transmitter and antenna the transmitter and feedline must be impedance matched to the antenna. This means the transmitter and antenna must have the same resistance and equal but opposite reactance. The feedline must also be impedance matched to the transmitter. If this condition is met, the antenna will absorb all the power supplied by the feedline. If the impedances at either end of the line do not match, it will cause a condition called “standing waves" (high VSWR) on the feedline, in which some of the RF power is not radiated by the antenna but is reflected back toward the transmitter, wasting energy and possibly overheating the transmitter. Most transmitters have a standard output impedance of 50 ohms, designed to feed 50 ohm coaxial cable.

The transmitter is matched to the feedline by a device called an *[antenna tuner](Antenna%20tuner.md)*, *antenna tuning unit*, or *matching network*, which may be a circuit in the transmitter, or a separate piece of equipment connected between the transmitter and feedline. There may be another matching network between the antenna and feedline, to match the feedline to the antenna. In consumer wireless devices that operate at fixed frequencies the matching network is not adjustable and is enclosed in the device's case. In large transmitters like broadcasting stations and transmitters that may operate on different frequencies like shortwave stations, the antenna tuner is adjustable. Changes in the transmitter frequency or adjustments to the transmitter output stage or antenna typically change the impedance, so after any work is done on the transmitter or antenna the SWR must be checked and the matching network adjusted. To adjust the matching network the simplest instrument to measure the degree of mismatch between the feedline and the antenna is called an SWR meter (standing wave ratio meter), which reports the *[standing wave ratio](Standing%20wave%20ratio.md)* (SWR) on the line: The ratio of the adjacent maximum and minimum voltage or current on the line. A ratio of 1:1 indicates an impedance match, meaning that the load is completely resistive so all of the power is absorbed and none is reflected. A higher ratio indicates a mismatch and reflected power. The matching network is adjusted until the SWR is below an acceptable limit. Other more advanced instruments are impedance bridges and [antenna analyzers](Antenna%20analyzer.md).

Since in an impedance matched transmitter, the transmitter's source resistance is equal to the feedline impedance and the antenna load resistance, and both are in series on the feedline and consume equal power, the maximum power that can be delivered to the antenna is 50% of the transmitter's output power; the other 50% is dissipated as heat by the resistance in the transmitter's output stage. (The matched feedline does dissipate a small amount of power through a small resistance, but the majority of its apparent resistive impedance is merely the voltage required to overcome the inductive and capacitive reactances of the feedline, which in and of themselves cause no loss.)

In radio receivers an impedance mismatch with the antenna causes a similar reduction in the signal energy from the antenna that reaches the receiver, which is also a maximum of 50% of the power of the intercepted signal, and power delivered to the receiver is far less when the line is mismatched and SWR is high. However, loss at frequencies below 10~20 MHz is not much of a problem, because the thermal noise floor in receivers is far below atmospheric noise already embedded in the signal, so a weak signal from the antenna can simply be amplified in the receiver to compensate for power lost from any mismatch, without noticeably contaminating it with noise. At frequencies above 20 MHz atmospheric noise radiates freely into space, and so is low enough in received signals that it approaches the level of the receiver's own internally generated noise; at those VHF and UHF frequencies, amplification degrades the signal to noise ratio, and receive signal impedance matching is an important concern for receiving faint signals.

### Balanced and unbalanced feeds

Transmission lines and their attached components can be classified as either balanced, in which both sides of the line have the same impedance to ground, for example [dipole antennas](Dipole%20antenna.md) and parallel wire lines, or unbalanced, in which one side of the line is connected to ground, for example [monopole antennas](Monopole%20antenna.md) and [coaxial cable](Coaxial%20cable.md). To connect balanced and unbalanced components, a two port device called a [balun](Balun.md) is used. A balun is a transformer that couples between balanced and unbalanced transmission line components. For example, to feed a dipole antenna from an unbalanced feedline like coaxial cable, the feedline is connected to the antenna through a [balun](Balun.md). Without the balun, the unbalanced part of the current will flow on the outside of the coaxial cable shield, causing the outer surface of the shield to act as an antenna.

### Other feed components

More complicated feeds may have other components besides the feedline and matching networks:

A receiving antenna with a long feedline may have an amplifier at the antenna, called a low-noise amplifier (LNA) which increases the power of the weak radio signals to compensate for attenuation in the feedline.

At microwave frequencies ordinary types of transmission line have excessive power losses, so for low losses microwaves must be carried by waveguide, a hollow metal pipe which conducts the radio waves. Due to the high cost and maintenance requirements, long waveguide runs are avoided, and the parabolic antennas used at microwave frequencies often have the RF front end of the receiver, or parts of the transmitter, located at the antenna. For example, in satellite dishes the feedhorn on the dish which collects the microwaves is attached to a circuit called a low-noise block downconverter (LNB or LNC), which converts the high microwave frequency to a lower intermediate frequency, so it can be carried into the building using a cheaper coaxial cable feedline.

Radar and satellite communications antennas may handle radio waves of multiple frequencies and polarizations, and may be used as both transmitting and receiving antennas, so the feed system carries radio signals traveling in both directions. Therefore, these antennas often have more complicated feeds that include specialized components like

- directional couplers, which couple out radio waves moving in one direction but not the other, to separate the received signal from the transmitted signal
- polarizers which pass radio waves of one polarization
- orthomode transducers which combine or separate radio signals of different polarizations
- diplexers which combine or separate two different frequencies
- phase shifters, which alter the phase of the radio waves
- waveguide switches
- waveguide rotary joints

An *array antenna* or *antenna array* consists of multiple antennas which are connected to a single transmitter or receiver which work together to emit or receive the radio waves. The feed systems of array antennas are understandably more complex than single antennas. The feed network must divide the transmitter power evenly between the antennas. To emit a plane wave the individual antennas *(elements)* of a transmitting array must be fed current with a specific phase relationship. Similarly with receiving arrays the currents from each element may need to be phase shifted so that they combine in phase in the receiver. This may require phase shifting networks at each element. In phased array antennas, a type of array antenna in which the beam can be steered electronically to different directions, each antenna element is fed current through a programmable phase shifter, which are controlled by a computer.

---

*Source: Wikipedia, Antenna feed (https://en.wikipedia.org/wiki/Antenna_feed), by Wikipedia contributors, CC BY-SA 4.0.*
