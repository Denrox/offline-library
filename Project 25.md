# Project 25

**Project 25** (**P25** or **APCO-25**) is a suite of standards for interoperable [Land mobile radio system](Land%20mobile%20radio%20system.md) (LMR) systems designed primarily for public safety users. The standards allow analog conventional, digital conventional, digital [trunked](Trunked%20radio%20system.md), or mixed-mode systems. P25 was originally developed for public safety users in the United States but has also gained acceptance for security, public service, and some [commercial applications](Professional%20mobile%20radio.md) worldwide. P25 radios are a replacement for analog [UHF](Ultra%20high%20frequency.md) (typically [FM](Frequency%20modulation.md)) radios, adding the ability to transfer data as well as voice for more natural implementations of encryption and text messaging. P25 radios are commonly implemented by dispatch organizations, such as police, fire, ambulance and emergency rescue service, using vehicle-mounted radios combined with [repeaters](Repeater.md) and handheld [walkie-talkies](Walkie-talkie.md).

Starting around 2012, products became available with the newer Phase II modulation protocol. The older protocol known as P25 became P25 Phase I. P25 Phase II (or P25II) products use the more advanced AMBE2+ vocoder, which allows audio to pass through a more compressed bitstream and provides two TDMA voice channels in the same RF bandwidth (12.5 kHz), while Phase I can provide only one voice channel. However, P25 Phase II infrastructure can provide a "dynamic transcoder" feature that translates between Phase I and Phase II as needed. In addition to this, Phase II radios are backwards compatible with Phase I modulation and analog [FM](Frequency%20modulation.md) modulation, per the standard. (Phase I radios cannot operate on Phase II trunked systems. However, Phase II radios *can* operate on Phase I systems or conventional systems.) The European Telecommunications Standards Institute (ETSI) has created the Terrestrial Trunked Radio (TETRA) and [Digital mobile radio](Digital%20mobile%20radio.md) (DMR) protocol standards, which fill a similar role to Project 25.

### Suite of standards overview

#### Introduction

Interoperable emergency communication is integral to initial response, public health, community safety, national security and economic stability. Of all the problems experienced during disaster events, one of the most serious is poor communication due to lack of appropriate and efficient means to collect, process, and transmit important information in a timely fashion. In some cases, radio communication systems are incompatible and inoperable not just within a jurisdiction but within departments or agencies in the same community. Non-operability occurs due to use of outdated equipment, limited availability of radio frequencies, isolated or independent planning, lack of coordination, and cooperation, between agencies, community priorities competing for resources, funding and ownership, and control of communications systems. Recognizing and understanding this need, Project 25 (P25) was initiated collaboratively by public safety agencies and manufacturers to address the issue with [emergency communication systems](Emergency%20communication%20system.md). P25 is a collaborative project to ensure that [two-way radios](Two-way%20radio.md) are interoperable. The goal of P25 is to enable public safety responders to communicate with each other and, thus, achieve enhanced coordination, timely response, and efficient and effective use of communications equipment.

P25 was established to address the need for common digital public safety radio communications standards for first-responders and homeland security/emergency response professionals. The Telecommunications Industry Association's TR-8 engineering committee facilitates such work through its role as an ANSI-accredited standards development organization (SDO) and has published the P25 suite of standards as the TIA-102 series of documents, which now include 49 separate parts on Land Mobile Radio and TDMA implementations of the technology for public safety.

Project 25 (P25) is a set of standards produced through the joint efforts of the Association of Public Safety Communications Officials International (APCO), the National Association of State Telecommunications Directors (NASTD), selected federal agencies and the National Communications System (NCS), and standardized under the Telecommunications Industry Association (TIA)... The P25 suite of standards involves digital Land Mobile Radio (LMR) services for local, state/provincial and national (federal) public safety organizations and agencies...

P25 is applicable to LMR equipment authorized or licensed, in the U.S., under NTIA or FCC rules and regulations.

Although developed primarily for North American public safety services, P25 technology and products are not limited to public safety alone and have also been selected and deployed in other private system application, worldwide.

P25-compliant systems are being increasingly adopted and deployed throughout the United States, as well as other countries. Radios can communicate in analog mode with legacy radios, and in either digital or analog mode with other P25 radios. Additionally, the deployment of P25-compliant systems will allow for a high degree of equipment interoperability and compatibility.

P25 standards use the proprietary Improved Multi-Band Excitation (IMBE) and Advanced Multi-Band Excitation (AMBE+2) voice codecs which were designed by Digital Voice Systems, Inc. to encode/decode the analog audio signals. It is rumored that the licensing cost for the voice-codecs that are used in P25 standard devices is the main reason that the cost of P25 compatible devices is so high.

P25 may be used in "talk around" mode without any intervening equipment between two radios, in conventional mode where two radios communicate through a repeater or base station without trunking or in a trunked mode where traffic is automatically assigned to one or more voice channels by a [Repeater](Repeater.md) or Base Station.

The protocol supports the use of Data Encryption Standard (DES) encryption (56 bit), 2-key Triple-DES encryption, three-key Triple-DES encryption, Advanced Encryption Standard (AES) encryption at up to 256 bits keylength, RC4 (40 bits, sold by Motorola as *Advanced Digital Privacy*), or no encryption. The RC4 Advanced Digital Privacy can withstand casual attackers. It is supposed to offer 40-bit security, where an attacker must test the 2 to the power of 40 possible keys to find the right one. This level of encryption offers no real protection and there is software that allows you to find the key.

The protocol also supports the ACCORDION 1.3, BATON, Firefly, MAYFLY and SAVILLE Type 1 ciphers.

#### Standards development process

The P25 User Needs Working Group (UNWG), which represents P25 users, identifies user needs for the P25 standards, which are communicated to the P25 Steering Committee. The P25 Steering Committee adds identified P25 user needs to the Statement of P25 User Needs (SPUN) document. The TIA TR-8 Engineering Committee and its subcommittees, which represents manufacturers in the P25 industry, is then expected to develop TIA-102 standards that satisfy identified P25 user needs.

Once developed, TIA-102 standards may also subsequently be adopted by the P25 Steering Committee as P25 standards, and adopted by ANSI as American National Standards; however, TIA-102 standards do not automatically become P25 standards, and some TIA-102 standards have never been adopted by ANSI. The TIA-102 standards, P25 standards, and associated ANSI standards have not been adopted by ISO as de jure international standards; however, P25 systems have been deployed in 83 countries, so they nonetheless serve as one set of de facto international standards alongside other international Land Mobile Radio (LMR) standards such as [TETRA](TETRA.md) and [DMR](Digital%20mobile%20radio.md).

#### P25 open interfaces

P25's Suite of Standards specify eight open interfaces between the various components of a land mobile radio system. These interfaces are:

- Common Air Interface (CAI) – standard specifies the type and content of signals transmitted by compliant radios. One radio using CAI should be able to communicate with any other CAI radio, regardless of manufacturer
- Subscriber Data Peripheral Interface – standard specifies the port through which mobiles and portables can connect to laptops or data networks
- Fixed Station Interface – standard specifies a set of mandatory messages supporting digital voice, data, encryption and telephone interconnect necessary for communication between a Fixed Station and P25 RF Subsystem
- Console Subsystem Interface – standard specifies the basic messaging to interface a console subsystem to a P25 RF Subsystem
- Network Management Interface – standard specifies a single network management scheme which will allow all network elements of the RF subsystem to be managed
- Data Network Interface – standard specifies the RF Subsystem's connections to computers, data networks, or external data sources
- Telephone Interconnect Interface – standard specifies the interface to Public Switched Telephone Network (PSTN) supporting both analog and ISDN telephone interfaces.
- Inter RF Subsystem Interface (ISSI) – standard specifies the interface between RF subsystems which will allow them to be connected into wide area networks
- Key Fill Interface (KFI) - standard messaging protocol for bidirectional update of encryption keys via transfer of unencrypted and encrypted key variables from a Key Fill Device (KFD) to the equipment containing the encryption service
- Inter-KMF-Interface (IKI) - interface for encrypted interoperability between radios managed by different Key Management Facilities (KMF)
- KFD-KMF Interface - interface between KFD and KMF for radios managed by different KMF (under development)

#### P25 phases

P25-compliant technology has been deployed over two main phases with future phases yet to be finalized.

##### Phase I

Phase I radio systems operate in 12.5 kHz digital mode using a single user per channel access method. Phase 1 radios use Continuous 4 level FM (C4FM) modulation—a special type of 4[FSK](Frequency-shift%20keying.md) modulation—for digital transmissions at 4,800 baud and 2 bits per symbol, yielding 9,600 bits per second total channel throughput. Of this 9,600, 4,400 is voice data generated by the IMBE codec, 2,800 is forward error correction, and 2,400 is signaling and other control functions. Receivers designed for the C4FM standard can also demodulate the "Compatible quadrature phase shift keying" (CQPSK) standard, as the parameters of the CQPSK signal were chosen to yield the same signal deviation at symbol time as C4FM. Phase I uses the IMBE voice codec.

These systems involve standardized service and facility specifications, ensuring that any manufacturers' compliant subscriber radio has access to the services described in such specifications. Abilities include backward compatibility and interoperability with other systems, across system boundaries, and regardless of system infrastructure. In addition, the P25 suite of standards provides an open interface to the radio frequency (RF) subsystem to facilitate interlinking of different vendors' systems.

##### Phase II

To improve spectrum use, P25 Phase II was developed for trunking systems using a 2-slot TDMA scheme and is now required for all trunking systems in the 700 MHz band. Phase II uses the AMBE+2 voice codec to reduce the needed bitrate so that one voice channel will only require 6,000 bits per second (including error correction and signaling). Phase II is not backwards compatible with Phase 1 (due to the TDMA operation), although multi-mode TDMA radios and systems are capable of operating in Phase I mode when required, if enabled. A subscriber radio cannot use TDMA transmission without a synchronization source; therefore direct radio to radio communication resorts to conventional FDMA digital operation. Multi-band subscriber radios can also operate on narrow-band FM as a lowest common denominator between almost any two way radios. This makes analog narrow-band FM the de facto "interoperability" mode for some time.

Originally, the implementation of Phase II was planned to split the 12.5 kHz channel into two 6.25 kHz slots, or Frequency-Division Multiple Access (FDMA). However it proved more advantageous to use existing 12.5 kHz frequency allocations in Time Division Multiple Access (TDMA) mode for a number of reasons. It allowed subscriber radios to save battery life by only transmitting half the time which also yields the ability for the subscriber radio to listen and respond to system requests between transmissions.

Phase II is what is known as 6.25 kHz "bandwidth equivalent" which satisfies an FCC requirement for voice transmissions to occupy less bandwidth. Voice traffic on a Phase II system transmits with the full 12.5 kHz per frequency allocation, as a Phase 1 system does, however it does so at a faster data rate of 12 kbit/s allowing two simultaneous voice transmissions. As such subscriber radios also transmit with the full 12.5 kHz, but in an on/off repeating fashion resulting in half the transmission and thus an equivalent of 6.25 kHz per each radio. This is accomplished using the AMBE voice coder that uses half the rate of the Phase 1 IMBE voice coders.

##### Beyond Phase II

From 2000 to 2009, the European Telecommunications Standards Institute (ETSI) and TIA were working collaboratively on the Public Safety Partnership Project or **Project MESA** (Mobility for Emergency and Safety Applications), which sought to define a unified set of requirements for a next-generation aeronautical and terrestrial digital wideband/broadband radio standard that could be used to transmit and receive voice, video, and high-speed data in wide-area, multiple-agency networks deployed by public safety agencies.

The final functional and technical requirements have been released by ETSI and were expected to shape the next phases of American Project 25 and European DMR, dPMR, and TETRA, but no interest from the industry followed, since the requirements could not be met by available commercial off-the-shelf technology, and the project was closed in 2010.

During the United States 2008 wireless spectrum auction, the FCC allocated 20 MHz of the 700 MHz UHF radio band spectrum freed in the digital TV transition to public safety networks. The FCC expects providers to employ LTE for high-speed data and video applications.

### Conventional implementation

P25 systems do not have to resort to using in band signaling such as [Continuous Tone-Coded Squelch System](Continuous%20Tone-Coded%20Squelch%20System.md) (CTCSS) tone or Digital-Coded Squelch (DCS) codes for access control. Instead they use what is called a Network Access Code (NAC) which is included outside of the digital voice frame. This is a 12-bit code that prefixes every packet of data sent, including those carrying voice transmissions.

The NAC is a feature similar to CTCSS or DCS for analog radios. That is, radios can be programmed to only pass audio when receiving the correct NAC. NACs are programmed as a three-hexadecimal-digit code that is transmitted along with the digital signal being transmitted.

Since the NAC is a three-hexadecimal-digit number (12 bits), there are 4,096 possible NACs for programming, far more than all analog methods combined.

Three of the possible NACs have special functions:

- 0x293 ($293) – the default NAC
- 0xf7e ($F7E) – a receiver set for this NAC will pass audio on any decoded signal received
- 0xf7f ($F7F) – a repeater receiver set for this NAC will allow all incoming decoded signals and the repeater transmitter will retransmit the received NAC.

### Adoption

Adoption of these standards has been slowed by budget problems in the US; however, funding for communications upgrades from the Department of Homeland Security usually requires migrating to Project 25. It is also being used in other countries worldwide including Australia, New Zealand, Brazil, Canada, India and Russia. As of mid-2004 there were 660 networks with P25 deployed in 54 countries. At the same time, in 2005, the European Terrestrial Trunked Radio (TETRA) was deployed in sixty countries, and it is the preferred choice in Europe, China, and other countries. This was largely based on TETRA systems being many times cheaper than P25 systems ($900 vs $6,000 for a radio) at the time. However P25 radio prices are rapidly approaching parity with TETRA radio prices through increased competition in the P25 market. The majority of P25 networks are based in Northern America where it has the advantage that a P25 system has the same coverage and frequency bandwidth as the earlier analog systems that were in use so that channels can be easily upgraded one by one. Some P25 networks also allow intelligent migration from the analog radios to digital radios operating within the same network. Both P25 and TETRA can offer varying degrees of functionality, depending on available radio spectrum, terrain and project budget.

While interoperability is a major goal of P25, many P25 features present interoperability challenges. In theory, all P25 compliant equipment is interoperable. In practice, interoperable communications isn't achievable without effective governance, standardized operating procedures, effective training and exercises, and inter-jurisdictional coordination. The difficulties inherent in developing P25 networks using features such as digital voice, encryption, or trunking sometimes result in feature-backlash and organizational retreat to minimal "feature-free" P25 implementations which fulfill the letter of any Project 25 migration requirement without realizing the benefits thereof. Additionally, while not a technical issue per se, frictions often result from the unwieldy bureaucratic inter-agency processes that tend to develop in order to coordinate interoperability decisions.

#### Naming of P25 technology in regions

- Statewide P25 systems in Australia were deployed using the name Government Radio Network (GRN) in New South Wales, South Australia, and Tasmania; Government Wireless Network (GWN) in Queensland; Territory Radio Network (TRN) in the Australian Capital Territory; and Melbourne Metropolitan Radio (MMR) and Rural Mobile Radio (RMR) in Victoria. In New South Wales, the GRN is now called the Public Safety Network (PSN).

### Project 25 Compliance Assessment Program (P25 CAP)

The United States DHS's Project 25 Compliance Assessment Program (P25 CAP) aims for interoperability among different vendors by testing to P25 Standards. P25 CAP, a voluntary program, allows suppliers to publicly attest to their products' compliance.

Independent, accredited labs test vendor's P25 radios for compliance to P25 Standards, derived from TIA-102 Standards and following TIA-TR8 testing procedures. Only approved products may be purchased using US federal grant dollars. Generally, non-approved products should not be trusted to be meet P25 standards for performance, conformance, and interoperability.

P25 product labeling varies. "P25" and "P25 compliant" mean nothing while high standards apply for a vendor to claim a product is "P25 CAP compliant" or "P25 compliant with the Statement of Requirements (P25 SOR)"

### Security flaws

#### OP25 Project—Encryption flaws in DES-OFB and ADP ciphers

At the Securecomm 2011 conference in London, security researcher Steve Glass presented a paper, written by himself and co-author Matt Ames, that explained how DES-OFB and Motorola's proprietary ADP (RC4 based) ciphers were vulnerable to brute force key recovery. This research was the result of the OP25 project which uses [GNU Radio](GNU%20Radio.md) and the Ettus Universal Software Radio Peripheral (USRP) to implement an open source P25 packet sniffer and analyzer. The OP25 project was founded by Steve Glass in early 2008 while he was performing research into wireless networks as part of his PhD thesis.

The paper is available for download from the NICTA website.

#### University of Pennsylvania research

In 2011, the *Wall Street Journal* published an article describing research into security flaws of the system, including a user interface that makes it difficult for users to recognize when transceivers are operating in secure mode. According to the article, "(R)esearchers from the University of Pennsylvania overheard conversations that included descriptions of undercover agents and confidential informants, plans for forthcoming arrests and information on the technology used in surveillance operations." The researchers found that the messages sent over the radios are sent in segments, and blocking just a portion of these segments can result in the entire message being jammed. "Their research also shows that the radios can be effectively jammed (single radio, short range) using a highly modified pink electronic child's toy and that the standard used by the radios 'provides a convenient means for an attacker' to continuously track the location of a radio's user. With other systems, jammers have to expend a lot of power to block communications, but the P25 radios allow jamming at relatively low power, enabling the researchers to prevent reception using a $30 toy pager designed for pre-teens."

The report was presented at the 20th USENIX Security Symposium in San Francisco in August 2011. The report noted a number of security flaws in the Project 25 system, some specific to the way it has been implemented and some inherent in the security design.

##### Encryption lapses

The report did not find any breaks in the P25 encryption; however, they observed large amounts of sensitive traffic being sent in the clear due to implementations problems. They found switch markings for secure and clear modes difficult to distinguish (∅ vs. o). This is exacerbated by the fact that P25 radios when set to secure mode continue to operate without issuing a warning if another party switches to clear mode. In addition, the report authors said many P25 systems change keys too often, increasing the risk that an individual radio on a net may not be properly keyed, forcing all users on the net to transmit in the clear to maintain communications with that radio.

##### Jamming vulnerability

One design choice was to use lower levels of error correction for portions of the encoded voice data that are deemed less critical for intelligibility. As a result, bit errors may be expected in typical transmissions, and while harmless for voice communication, the presence of such errors force the use of stream ciphers, which can tolerate bit errors, and prevents the use of a standard technique, message authentication codes (MACs), to protect message integrity from stream cipher attacks. The varying levels of error correction are implemented by breaking P25 message frames into subframes. This allows an attacker to jam entire messages by transmitting only during certain short subframes that are critical to reception of the entire frame. As a result, an attacker can effectively jam Project 25 signals with average power levels much lower than the power levels used for communication. Such attacks can be targeted at encrypted transmissions only, forcing users to transmit in the clear.

Because Project 25 radios are designed to work in existing two-way radio frequency channels, they cannot use [spread spectrum](Spread%20spectrum.md) modulation, which is inherently jam-resistant. An optimal spread spectrum system can require an effective jammer to use 1,000 times as much power (30 dB more) as the individual communicators. According to the report, a P25 jammer could effectively operate at 1/25th the power (14 dB less) than the communicating radios. The authors developed a proof-of-concept jammer using a Texas Instruments CC1110 single chip radio, found in an inexpensive toy.

##### Traffic analysis and active tracking

Certain metadata fields in the Project 25 protocol are not encrypted, allowing an attacker to perform traffic analysis to identify users. Because Project 25 radios respond to bad data packets addressed to them with a retransmission request, an attacker can deliberately send bad packets forcing a specific radio to transmit even if the user is attempting to maintain [radio silence](Radio%20silence.md). Such tracking by authorized users is considered a feature of P25, referred to as "presence".

The report's authors concluded by saying "It is reasonable to wonder why this protocol, which was developed over many years and is used for sensitive and critical applications, is so difficult to use and so vulnerable to attack." The authors separately issued a set of recommendations for P25 users to mitigate some of the problems found. These include disabling the secure/clear switch, using Network Access Codes to segregate clear and encrypted traffic, and compensating for the unreliability of P25 over-the-air rekeying by extending key life.

### Comparison between P25 and TETRA

P25 and TETRA are used in more than 53 countries worldwide for both public safety and private sector radio networks. There are some differences in features and capacities:

- TETRA is optimized for high population density areas, and has spectral efficiency of 4 time slots in 25 kHz. (Four communications channels per 25 kHz channel, an efficient use of spectrum). It supports full-duplex voice communication, data, and messaging. It does not provide simulcast.
- P25 is optimized for wider area coverage with low population density, and also supports simulcast. It is, however, limited with respect to data support. There is a major subdivision within P25 radio systems: Phase I P25 operates analogue, digital, or mixed mode in a single 12.5 kHz channel. Phase II uses a 2-timeslot TDMA structure in each 12.5 kHz channel.

---

*Source: Wikipedia, Project 25 (https://en.wikipedia.org/wiki/Project_25), by Wikipedia contributors, CC BY-SA 4.0.*
