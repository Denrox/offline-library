# Professional mobile radio

**Professional mobile radio** (also known as **private mobile radio** (**PMR**) in the UK) are person-to-person [two-way radio](Two-way%20radio.md) voice communications systems which use [portable](Walkie-talkie.md), mobile, base station, and dispatch console radios. PMR systems are based on such standards as MPT-1327, [TETRA](TETRA.md), [APCO 25](Project%2025.md), and [DMR](Digital%20mobile%20radio.md) which are designed for dedicated use by specific organizations, or standards such as [NXDN](NXDN.md) intended for general commercial use. These systems are used by police, fire, ambulance, and emergency services, and by commercial firms such as taxis and delivery services. Most systems are half-duplex, in which multiple radios share a common radio channel, and only one can transmit at a time. Transceivers are normally in receive mode, the user presses a [push-to-talk](Push-to-talk.md) button on his microphone when he wants to talk, which turns on his transmitter and turns off his receiver. They use channels in the [VHF](Very%20high%20frequency.md) and UHF bands, giving them a limited range, usually 3 to 20 miles (5 to 30 km) depending on terrain. Output power is typically limited to 4 watts. [Repeaters](Repeater.md) installed on tall buildings, hills or mountain peaks are used to increase the range of systems.

### Introduction

When private- or professional-mobile-radio (PMR) first started the systems simply consisted of a single base station with a number of mobiles that could communicate with this single base station. These systems are still in widespread use today with taxi firms and many others using them for communication. Now facilities such as DTMF and CTCSS provide additional calling selection. Because the [antenna](Antenna%20%28radio%29.md) may be mounted on a high tower, coverage may extend up to distances of fifty kilometres (30 miles). This is helpful especially when there is no signal in a GSM mobile phone.

Licenses are allocated for operation on a particular channel or channels. The user can then have use of these channels to contact the mobile stations in their fleet. The base station may be run by the user themselves or it may be run by an operating company who will hire out channels to individual users. In this way a single base station with a number of different channels can be run by one operator for a number of different users and this makes efficient use of the base station equipment. The base station site can also be located at a position that will give optimum radio coverage, and private lines can be provided to connect the users control office to the transmitter site. As there is no incremental cost for the transmissions that are made, individual calls are not charged, but instead there is a rental for overall use of the system. For those users with their own licences they naturally have to pay for the licence and the cost of purchase and maintenance of that equipment.

The term PMR is often used by the public and magazine publishing to refer to the low power (500 milliwatt) [PMR446](PMR446.md) license exempt radio systems that consist of sixteen FM frequencies between 446.00625 and 446.19375 MHz for analog FM and thirty-two FDMA (digital) channels between 446.003125 and 446.196875 MHz. These are used for personal or business communications where they are legal. Split frequency repeaters are not allowed on these frequencies and these radios do not communicate with licensed PMR systems. PMR446 radios are much cheaper than those used for the licensed PMR systems.

### Modulation

In general narrow band frequency modulation is the chosen form of modulation, although airport services use [amplitude modulation](Amplitude%20modulation.md). Typically a deviation of 2.5 kHz is used for FM and this enables a channel spacing of 12.5 kHz to be implemented. As the demands for PMR are high, it is necessary to make effective use of the channels available. This is achieved by re-using the frequencies in different areas. Base stations must be located sufficiently far apart so that interference is not experienced, and also selective calling techniques such as CTCSS and DTMF are used to ensure that as many mobiles as possible can use a given channel.

### Selective calling

The simplest systems operate with all the radios on a frequency channel being able to hear all the calls being made. In some applications this may not be desirable and a system of selective calling may be required, in which two radios on a channel can have a private conversation which is not received by the others, or in which a specific radio can be promptly contacted and made to "ring" almost like an ordinary phone. Two widely used systems are Dual Tone Multiple Frequency (DTMF), and Continuous Tone Coded Squelch System (CTCSS).

#### DTMF

A DTMF selective signaling PMRS system uses a code sequence of discrete audible tones, representing numbers, transmitted at the beginning of each voice message to address the transmission to a specific station or group of stations. The DTMF (dual tone multifrequency) code is used, which is also universally used for touch-tone dialing in the worldwide public telephone network. The eight audio frequencies used in DTMF are 697, 770, 852, 941 Hz which are called the "low tones" and 1,209; 1,336; 1,477; and 1,633 Hz which are the "high tones". Pairs of one high and one low tone transmitted together represent a decimal number. Each station is assigned a unique DTMF callsign, consisting of several numbers. The [squelch](Squelch.md) circuit in each radio decodes the tones and turns the receiver audio on if the transmission is addressed to that radio. There is also a code for "broadcast" transmissions, which causes the transmission to be received by all the radios on the channel.

A disadvantage of this system is that since the DTMF code is sent only once at the beginning of a message, if the receiver does not pick up the code due to temporary noise or bad signal conditions the receiver will not turn on and it will miss the entire message. This can be a significant disadvantage because mobile stations often lose the signal for short periods as they are on the move.

#### CTCSS

Another widely used system is the [Continuous Tone-Coded Squelch System](Continuous%20Tone-Coded%20Squelch%20System.md) (CTCSS) also referred to as subaudible tones or PL tones (a Motorola trademark). This uses single audio tones in the range from 67 to 257 Hz to address each message to a specific radio or a group (or fleet) of radios. Each radio or group is assigned a different tone frequency. The code tone is transmitted continuously throughout the audio transmission along with the voice modulation. Since the tones are below the audio passband of the receiver, roughly 300–3,000 Hz, they are filtered out in the receiver's audio amplifier and therefore not heard.

Only when the correct tone for the required station is transmitted will the [squelch](Squelch.md) for that receiver (or group) be opened and the transmitted audio be heard. The advantage of this system is that the code tone is transmitted during the entire transmission, instead of just at the beginning as in the DTMF system above, so the system works in spite of noise or signal dropouts. Systems typically are able to provide from 32 to 50 different tones between 67 Hz and 254.1 Hz, allowing multiple separately addressable radios or groups of radios.

### TETRA

**TETRA** is a modern standard for digital private mobile radio (PMR) and public access mobile radio (PAMR).

Work started on the development of the TETRA standards in 1990 and has relied on the support of the European Commission and the ETSI members. Experience gained in the development of the GSM cellular radio standard, as well as experience from the development and use of trunked radio systems has also been used to fashion the TETRA standard. In addition to this the process has gained from the co-operation of manufacturers, users, operators and industry experts. With this combined expertise the first standards were ready in 1995 to enable manufacturers to design their equipment to interoperate successfully.

TETRA allocates the channels to users on demand in both voice and data modes. Additionally national and multi-national networks are available and national and international roaming can be supported. For civil systems in Europe the frequency bands 410–430 MHz, 870–876 MHz / 915–921 MHz, 450–470 MHz, 385–390 MHz / 395–399.9 MHz, have been allocated for TETRA. Then for the emergency services in Europe the frequency bands 380–383 MHz and 390–393 MHz have been allocated. In addition to this, the whole or appropriate parts of the bands between 383–385 MHz and 393–395 MHz can be utilized.

Low speed packet data as well as circuit data modes are available, along with some form of encryption. The systems makes use of the available frequency allocations using time-division multiple access (TDMA) technology with four user channels on one radio carrier with 25 kHz spacing between carriers.

The first ruggedized high-speed smartphone based on the [TETRA](TETRA.md) network was launched on 26 May 2011

### PMR trunking using MPT1327

A trunked version of the private mobile radio (PMR) concept that is defined under the standard MPT 1327 (MPT1327) is widely used and provides significant advantages over the simpler single station systems that are in use. MPT1327 enables stations to communicate over wider areas as well as having additional facilities. In view of the very high cost of setting up trunked networks, they are normally run by large leasing companies or consortia that provide a service to a large number of users. In view of the wider areas covered by these networks and the greater complexity, equipment has to be standardised so that suppliers can manufacture in higher volumes and thereby reduce costs to acceptable levels. Most trunked radio systems follow the MPT1327 format.

To implement trunked PMR a network of stations is set up. These stations are linked generally using land lines, although optical fibers and point to point radio are also used. In this way the different base stations are able to communicate with each other.

In order to be able to carry the audio information and also run the variety of organisational tasks that are needed the system requires different types of channel to be available. These are the control channels of which there is one in each direction for each base station or Trunking System Controller (TSC).

A number of different control channels are used so that adjacent base stations do not interfere with one another, and the mobile stations scan the different channels to locate the strongest control channel signal. In addition to this there are the traffic channels. The specification supports up to 1,024 different traffic channels to be used. In this way a base station can support a large number of different mobile stations that are communicating at the same time. However, for small systems with only a few channels, the control channel may also act as a non-dedicated traffic channel.

The control channels use signalling at 1,200 bits per second with fast frequency shift keying (FFSK) subcarrier modulation. It is designed for use by two-frequency half duplex mobile radio units and a full duplex TSC.

For successful operation it is essential that the system knows where the mobiles are located so that calls can be routed through to them. The TSC (Trunking System Controller) gains this information by mobiles "registering" on a control channel. The MPT1327 standard describes several registration mechanisms, aimed at limiting the load on the control channel caused by mobiles roaming. Registrations may be explicit or implicit. An explicit registration may be initiated by the control channel demanding that a mobile issues a registration request; or initiated by a mobile which has roamed to a new registration area. It is also possible for a mobile to implicitly register, where the TSC will update its registration records when the mobile makes a call attempt. It is possible that the TSC's record does not match the mobile's location. This can occur, for example, where a mobile is switched off and then moved within coverage of a different site.

To make an outgoing call the mobile transmits a request to the base station as requested in the control channel data stream from the base station. The mobile transmits its own code along with that of the destination of the call, either another mobile or a control office. The control software and circuitry within the base station and the central control processing area for the network sets up the network so that a channel is allocated for the audio (the traffic channel). It also sets up the switching in the network to route the call to the required destination.

To enable the mobile station to receive a call, it is paged via the incoming control channel data stream to indicate that there is an incoming call. Channels are allocated and switching set up to provide the correct routing for the call.

There is no method described within the standard to "handover" the mobile from one base station to the next if it moves out of range of the base station through which a call is being made. In this way the system is not a form of cellular telephone. It is therefore necessary for the mobile station to remain within the service area of the base station through which any calls are being made.

The control channel discipline is Slotted Aloha where the forward or downlink channel (that received by the mobiles) provides timeslots within which a mobile may transmit a request in the uplink channel. In general, a mobile may only transmit on the control channel if invited to by TSC. This invitation may be explicitly addressed to a mobile or a group; or it may be random access. Random access timeslots will be used when a mobile user initiates a call, or when a mobile registers on the TSC. On a heavily loaded control channel, it is likely that two or more mobile radio units will try to transmit at the same time on the same random access timeslot. This is detected by mobile, when the expected reply from the TSC is not received within a certain timeout. The mobile may then retry its request in another random access slot. The timeouts and number of retries is configured in the mobile when it is set up for the network.

Signalling on the forward control channel is nominally continuous with each slot comprising 64 bit code words. The first type is the Control Channel System Codeword (CSCC). This identifies the system to the mobile radio units and also provides synchronization for the following address codeword. As mentioned the second type of word is the address codeword. It is the first codeword of any message and it defines the nature of the message. It is possible to send data over the control channel. When this occurs, both the CSCC and the address codewords are displaced with the data appended to the address codeword. The mobile radio unit data structure is somewhat simpler. It consists fundamentally of synchronism bits followed by the address codeword.

There are a number of different types of control channel messages that can be sent by the base station to the mobiles:

- Aloha messages — Sent by the base station to invite and mobile stations to access the system
- Requests — Sent by radio units to request a call to be set up
- "Ahoy" messages — Sent by the base station to demand a response from a particular radio unit. This may be sent to request the radio unit to send his unique identifier to ensure it should be taking traffic through the base station.
- Acknowledgments — These are sent by both the base stations and the mobile radio units to acknowledge the data sent.
- Go to channel messages — These messages instruct a particular mobile radio unit to move to the allocated traffic channel.
- Single address messages — These are sent only by the mobile radio units.
- Short data messages — These may be sent by either the base station or the mobile radio unit.
- Miscellaneous messages — Sent by the base station for control applications

Although the data is transmitted as digital information, the audio or voice channels for the system are analogue, employing FM. However some work has been carried out to develop completely digital systems. The main systems are by Motorola, by Ericsson (EDACS) and Johnson (LTR). These systems have not gained such widespread acceptance.

---

*Source: Wikipedia, Professional mobile radio (https://en.wikipedia.org/wiki/Professional_mobile_radio), by Wikipedia contributors, CC BY-SA 4.0.*
