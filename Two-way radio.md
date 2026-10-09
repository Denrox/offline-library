# Two-way radio

A **two-way radio** is a radio [transceiver](Transceiver.md) (a radio that can both transmit and receive radio waves), which is used for bidirectional person-to-person voice communication with other users with similar radios, in contrast to a broadcast receiver, which only receives transmissions.

Two-way radios usually use a half-duplex communication channel, which permits two-way communication, albeit with the limitation that only one user can transmit at a time. (This is in contrast to simplex communication, in which transmission can only be sent in one direction, and full-duplex, which allows transmission in both directions simultaneously.) This requires users in a group to take turns talking. The radio is normally in receive mode so the user can hear all other transmissions on the channel. When the user wants to talk, they press a "push-to-talk" button, which turns off the receiver and turns on the transmitter; when the button is released, the receiver is activated again. Multiple channels may be provided so separate user groups can communicate in the same area without interfering with each other and some radios are designed to scan the channels in order to find a valid transmission. Other two-way radio systems operate in [full-duplex](Duplex%20%28telecommunications%29.md) mode, in which both parties can talk simultaneously. This requires either two separate radio channels or channel sharing methods such as time-division duplex (TDD) to carry the two directions of the conversation simultaneously on a single radio frequency.

The first two-way radio was an AM-only device introduced by the Galvin Manufacturing Corporation (now known as [Motorola Solutions](Motorola%20Solutions.md)) in 1940 for use by the police and military during World War II, and followed by the company's 1943 introduction of the Walkie-Talkie, the best-known example of a two-way radio.

### Types

Two-way radio systems can be classified in several ways depending on their attributes.

#### Conventional versus trunked

##### Conventional

In multi-channel systems, channels are used for separate purposes.

###### Scanning in conventional radios

Scan features are either not used or scan lists are intentionally kept short in emergency applications. Part of APCO Project 16 set standards for channel access times and delays caused by system overhead. Scan features can further increase these delays. One study said delays of longer than 0.4 seconds (400 milliseconds) in emergency services are not recommended.

##### Duplex

The term "half duplex" is applied to wired communication systems where the circuit can send information in one direction at a time but not both directions at the same time.

- Advantage: duplex channels usually allow repeater operation which extends range (in most cases due to increased transmit power and improved aerial location / height) – especially where hand-held radios are in use.
- Disadvantage: If a radio cannot reach the repeater, it cannot communicate. This can be mitigated with a "talk around" or "car to car" setting where stations out of range of the base can speak directly to each other, alternating transmitting and receiving roles in simplex fashion on a single frequency.

##### Analog

Analog systems may communicate a single condition, such as water level in a livestock tank. A transmitter at the tank site continually sends a signal with a constant audio tone. The tone would change in pitch to indicate the tank's water level. A meter at the remote end would vary, corresponding to the tone pitch, to indicate the amount of water present in the livestock tank. Similar methods can be used to telemeter any analog condition. This type of radio system serves a purpose equivalent to a 4–20 mA current loop. In the US, mid-band 72–76 MHz or UHF 450–470 MHz interstitial channels are often used for these systems. Some systems multiplex telemetry of several analog conditions by limiting each to a separate range of tone pitches, for example.

Analog systems may also transmit voice in the same frequency bands except for VHF mid-band, but with the addition of VHF low band (25–50 MHz). Historically, all two-way voice communications was analog.

##### Digital

Digital systems may communicate text messages from computer-aided dispatch (CAD). For example, a display in a tow truck may give a textual location for a call and any related details. The tow truck driver may press an *acknowledge* button, sending data in the opposite direction and flagging the call as received by the driver. They can be used for analog telemetry systems, such as the livestock tank levels, as described above. Another possibility is the lubricating oil pressure in a transit bus engine, or the current speed of the bus. Analog conditions are translated into data words. Some systems send radio paging messages which can either 1) beep a paging receiver, 2) send a numeric message, or 3) send a text message.

#### Engineered systems

*Engineered* systems are designed to perform close to a specification or standard. They are designed as systems with all equipment matched to perform together. For example, a modern, local government two-way radio system in the US may be designed to provide 95% area coverage in an urban area. System designers use radio frequency models, terrain models, and signal propagation modeling software in an attempt to accurately estimate where radios will work within a defined geographic area. The models help designers choose equipment, equipment locations, [antennas](Antenna%20%28radio%29.md), and estimate how well signals will penetrate buildings. These models will be backed up by drive testing and actual field measurements of parameters such as received signal strength, bit error rate, or delivered audio quality. Designers adjust antenna patterns, add or move equipment sites, and design antenna networks in a way that will accomplish the intended level of performance.

#### Options, duty cycle, and configuration

Many mobile handhelds have a limited duty cycle. Duty cycle is the ratio of listening time to transmit time and is generally dependent on how well the transmitter can shed the heat from the heat sink on the rear of the radio. A 10% duty cycle (common on handhelds) translates to 10 seconds of transmit time to 90 seconds of receive time. Some mobile and base equipment is specified at different power levels – for example 100% duty cycle at 25 watts and 15% at 40 watts.

#### Life of equipment

In government systems, equipment may be replaced based on budgeting rather than any plan or expected service life. Funding in government agencies may be cyclical or sporadic. Managers may replace computing systems, vehicles, or budget computer and vehicle support costs while ignoring two-way radio equipment. Equipment may remain in use even though maintenance costs are unreasonable when viewed from an efficiency standpoint.

One document says "seven years" is beyond the expected lifetime of walkie-talkies in police service. Batteries are cited as needing replacement more often. Twelve-year-old dispatch consoles mentioned in the same document were identified as usable. These were compared to problematic 21-year-old consoles used elsewhere in the same system.

Another source says system backbone equipment like consoles and base stations are expected to have a fifteen-year life. Mobile radios are expected to last ten years. Walkie talkies typically last eight. In a State of California document, the Department of General Services reports expected service life for a communications console used in the Department of Forestry and Fire Protection is 10 years.

### Two-way radio frequencies

Typical two-way radios work on fixed radio frequency channels, though some can scan multiple channels in order to find a valid transmission. In an analog, conventional system (the simplest type of system), a frequency or channel serves as a physical medium or link carrying communicated information. The performance of a radio system is partly dependent on the characteristics of frequency band used. The selection of a frequency for a two-way radio system is affected, in part, by:

- government licensing and regulations;
- local congestion or availability of frequencies;
- ground cover, since radio signals travel differently in forests and urban viewsheds;
- terrain, which may cause shadowing of radio paths;
- the presence of noise, interference, or intermodulation.

### UHF versus VHF

The most common two-way radio systems operate in the [VHF](Very%20high%20frequency.md) and [UHF](Ultra%20high%20frequency.md) parts of the [radio spectrum](Radio%20spectrum.md). Because this part of the spectrum is heavily used for broadcasting and multiple competing uses, spectrum management has become an important activity of governments to regulate radio users in the interests of both efficient and non-interfering use of radio. Both bands are widely applied for different users.

### Range

The useful direct range of a two-way radio system depends on [radio propagation](Radio%20propagation.md) conditions, which are a function of frequency.

There are other factors that affect the range of a two-way radio such as weather, exact frequency used, and obstructions.

---

*Source: Wikipedia, Two-way radio (https://en.wikipedia.org/wiki/Two-way_radio), by Wikipedia contributors, CC BY-SA 4.0.*
