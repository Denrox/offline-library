# Packet radio

**Packet radio** is the application of packet switching techniques to digital radio communications.

Packet radio is frequently used by [amateur radio](Amateur%20radio.md) operators. The [AX.25](AX.25.md) (Amateur X.25) protocol was derived from the X.25 protocol and adapted for amateur radio use. Every AX.25 packet includes the sender's amateur radio callsign, which satisfies the United States Federal Communications Commission (FCC) requirements for amateur radio station identification. Using AX.25, it is possible for any packet station to act as a digipeater, linking distant stations with each other through ad hoc networks. This makes packet radio especially useful for emergency communications.

### Concepts

Packet radio can be differentiated from other digital radio switching schemes by the following attributes:

- Transmitted data is broken into packets, each of which contains a destination (and typically the source) address
- A transmitted message may be broken into a sequence of packets before transmission, which are then reassembled into the original message upon reception
- Packets for multiple destinations can be transmitted on the same radio link in an asynchronous fashion
- A packet may be addressed to all possible recipients rather than a specific one (broadcast)
- A packet may be stored and subsequently forwarded towards its destination by a network node

This is very similar to how packets of data are transferred between nodes on the Internet.

One of the first challenges faced by amateurs implementing packet radio is that almost all amateur radio equipment (and most surplus commercial/military equipment) has historically been designed to transmit voice, not data. Like any other digital communications system that uses analog media, packet radio systems require a modem. Since the radio equipment to be used with the modem was intended for voice, early amateur packet systems used AFSK modems that followed telephone standards (notably the Bell 202 standard). While this approach worked, it was not optimal, because it used a 25 kHz FM channel to transmit at 1,200 baud. When using a direct [FSK](Frequency-shift%20keying.md) modulation like G3RUH's packet radio modem, a 9,600 baud transmission is easily made in the same channel. In addition, the baseband characteristics of the audio channel provided by voice radios are often quite different from those of telephone audio channels. This led to the need in some cases to enable or disable pre-emphasis or de-emphasis circuits in the radios and/or modems.

Another problem faced by early "packeteers" was the issue of asynchronous versus synchronous data transfer. At the time, most personal computers had asynchronous RS-232 serial ports for data communications between the computer and devices such as modems. The RS-232 standard specifies an asynchronous, start-stop mode of data transmission where data is sent in groups (characters) of 7 or 8 bits. Unfortunately, the simple AFSK modems typically used provide no timing signal to indicate the start of a packet frame. That led to the need for a mechanism to enable the receiver to know when to start assembling each packet frame. The method used is called asynchronous framing. The receiver looks for the "frame boundary octet," then begins decoding the packet data that follows it. Another frame boundary octet marks the end of the packet frame.

A number of data "conversations" are possible on a single radio channel over a finite period.

A basic packet radio station consists of a computer or dumb terminal, a modem, and a [transceiver](Transceiver.md) with an antenna. Traditionally, the computer and modem are combined in one unit, the terminal node controller (TNC), with a dumb terminal (or terminal emulator) used to input and display data. Increasingly, personal computers are taking over the functions of the TNC, with the modem either a standalone unit or implemented entirely in software. Alternatively, multiple manufacturers (including [Kenwood](Kenwood%20Corporation.md) and Alinco) now market handheld or mobile radios with built-in TNCs, allowing connection directly to the serial port of a computer or terminal with no other equipment required. The computer is responsible for managing network connections, formatting data as AX.25 packets, and controlling the radio channel. Frequently, it provides other functionality as well, such as a simple bulletin board system to accept messages while the operator is away.

### Layers

Following the OSI model, packet radio networks can be described in terms of the physical, data link, and network layer protocols on which they rely.

#### Physical

Modems used for packet radio vary in throughput and modulation technique, and are normally selected to match the capabilities of the radio equipment in use. Most commonly used method is one using audio frequency-shift keying (AFSK) within the radio equipment's existing speech bandwidth. The first amateur packet radio stations were constructed using surplus Bell 202 1,200 bit/s modems, and despite its low data rate, Bell 202 modulation has remained the standard for VHF operation in most areas. More recently, 9,600 bit/s has become a popular, although more technically demanding, alternative. At [HF](High%20frequency.md) frequencies, Bell 103 modulation is used, at a rate of 300 bit/s.

Due to historical reasons, all commonly used modulations are based on an idea of minimal modification to the radio itself, usually just connecting the computer's audio output directly to the transmitter's microphone input and receiver's audio output directly to the computer's microphone input. Upon adding a *turn the transmitter on* output signal ("PTT") for transmitter control, one has made a *radio modem*. Due to this simplicity, and just having suitable microchips at hand, the *Bell 202* modulation became the standard way to send the packet radio data over the radio as two distinct tones. The tones are 1,200 Hz for Mark and 2,200 Hz for space (1,000 Hz shift). In the case of *Bell 103* modulation, a 200 Hz shift is used. The data is differentially encoded with a NRZI pattern, where a data zero bit is encoded by a change in tones and a data one bit is encoded by no change in tones.

Ways to achieve higher speeds than 1,200 bits/s, include using telephone modem chips via the microphone and audio out connectors. This has been proven to work at speeds up to 4,800 bit/s using fax V.27 modems in half-duplex mode. These modems use phase-shift keying, which works fine when there is no amplitude-shift keying, but at faster speeds, such as 9,600 bit/s, signal levels become critical, and they are extremely sensitive to group delay in the radio. These systems were pioneered by Simon Taylor (G1NTX) and Jerry Sandys (G8DXZ) in the 1980s. Other systems, which involved small modification of the radio, were developed by James Miller (G3RUH) and operated at 9,600 bit/s.

1,200 bit/s AFSK node controllers on 2 meters (144–148 MHz) are the most commonly found packet radio. For 1,200/2,400 bit/s UHF/VHF packet radio, amateurs use commonly available narrow band FM voice radios. For HF packet, 300 bit/s data is used over single sideband ([SSB](Single-sideband%20modulation.md)) modulation. For high speed packet (9,600 bit/s upwards), special radios or modified FM radios must be used.

Custom modems have been developed which allow throughput rates of 19.2 kbit/s, 56 kbit/s, and even 1.2 Mbit/s over amateur radio links on FCC permitted frequencies of 440 MHz and above. However, special radio equipment is needed to carry data at these speeds. The interface between the "modem" and the "radio" is at the *intermediate frequency* part of the radio as opposed to the audio section used for 1,200 bit/s operation. The adoption of these high-speed links has been limited.

In many commercial data radio applications, audio baseband modulation is not used. Data is transmitted by altering the transmitter output frequency between two distinct frequencies (in the case of FSK modulation, other alternatives exist).

The 2.4 GHz "Wi-Fi" band partially overlaps an amateur radio band, so commercial Wi-Fi hardware can be adapted and used by licensed amateur radio operators at higher power levels, although restrictions on amateur radio limit the appeal of using packet radio to connect to the internet. US FCC regulations do not allow amateur radio communications to be encrypted or private, in addition to other content restrictions.

#### Data link

Packet radio networks rely on the [AX.25](AX.25.md) data link layer protocol, derived from the X.25 protocol suite and intended specifically for amateur radio use. Despite its name, AX.25 defines both the physical and data link layers of the OSI model. (It also defines a network layer protocol, though this is seldom used.)

#### Network

Packet radio has most often been used for direct, keyboard-to-keyboard connections between stations, either between two live operators or between an operator and a bulletin board system. No network services above the data link layer are required for these applications.

To provide automated routing of data between stations (important for the delivery of electronic mail), several network layer protocols have been developed for use with AX.25. Most prominent among these network layer protocols are NET/ROM & TheNET, ROSE, FlexNet and TexNet.

In principle, any network layer protocol may be used, including the ubiquitous Internet Protocol.

### Implementations

Many commercial operations, particularly those that make use of vehicle dispatch (e.g., taxis, tow trucks, police), were quick to note the value of packet radio systems to provide simple mobile data systems. This led to the rapid development of a number of commercial packet radio systems:

- MDI (1979)
- DCS (1984)
- DRN (1986)
- Mobitex (1986)
- ARDIS (1990)
- CDPD allowed packet data to be carried over AMPS analog cellular telephone networks
- GPRS is the packet data facility provided by the GSM cellular telephone network

### Other uses

Packet radio can be used in mobile communications. Some mobile packet radio stations transmit their location periodically using the [Automatic Packet Reporting System](Automatic%20Packet%20Reporting%20System.md) (APRS). If the APRS packet is received by an *i-gate* station, position reports and other messages can be routed to an Internet server and made accessible on a public web page. This allows amateur radio operators to track the locations along with telemetry and other messages of vehicles, hikers, high-altitude balloons, etc., around the world.

Some packet radio implementations also use dedicated point-to-point links such as TARPN. In cases such as this, new protocols have emerged, such as Improved Layer 2 Protocol (IL2P), supporting forward error correction for noisy and weak signal links.

---

*Source: Wikipedia, Packet radio (https://en.wikipedia.org/wiki/Packet_radio), by Wikipedia contributors, CC BY-SA 4.0.*
