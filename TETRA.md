# TETRA

Terrestrial Trunked Radio
- Type Incentive
- Industry European Telecommunications Standards Institute  
[professional mobile radio](Professional%20mobile%20radio.md)  
[trunked radio system](Trunked%20radio%20system.md)
- Founded 1995  
Europe
- Headquarters Europe

**Terrestrial Trunked Radio** (**TETRA**; formerly known as **Trans-European Trunked Radio**), a European standard for a [trunked radio system](Trunked%20radio%20system.md), is a [professional mobile radio](Professional%20mobile%20radio.md) and two-way transceiver specification. TETRA was specifically designed for use by government agencies, emergency services, (police forces, fire departments, ambulance) for public safety networks, rail transport staff for train radios, transport services and the military. TETRA is the European version of trunked radio, similar to [Project 25](Project%2025.md).

TETRA is a European Telecommunications Standards Institute (ETSI) standard, first version published 1995; it is mentioned by the European Radiocommunications Committee (ERC).

### Description

TETRA uses time-division multiple access (TDMA) with four user channels on one radio carrier and 25 kHz spacing between carriers. Both point-to-point and point-to-multipoint transfer can be used. Digital data transmission is also included in the standard though at a low data rate.

TETRA Mobile Stations (MS) can communicate direct-mode operation (DMO) or using [trunked](Trunked%20radio%20system.md)-mode operation (TMO) using switching and management infrastructure (SwMI) made of TETRA base stations (TBS). As well as allowing direct communications in situations where network coverage is not available, DMO also includes the possibility of using a sequence of one or more TETRA terminals as relays. This functionality is called DMO gateway (from DMO to TMO) or DMO repeater (from DMO to DMO). In emergency situations this feature allows direct communications underground or in areas of bad coverage.

In addition to voice and dispatch services, the TETRA system supports several types of data communication. Status messages and *short data services* (SDS) are provided over the system's main control channel, while packet-switched data or circuit-switched data communication uses specifically assigned channels.

TETRA provides for authentication of terminals towards infrastructure and vice versa. For protection against eavesdropping, air interface encryption and end-to-end encryption is available.

The common mode of operation is in a group calling mode in which a single button push will connect the user to the users in a selected call group and/or a dispatcher. It is also possible for the terminal to act as a one-to-one walkie talkie but without the normal range limitation since the call still uses the network. TETRA terminals can act as mobile phones (cell phones), with a full-duplex direct connection to other TETRA Users or the PSTN. Emergency buttons, provided on the terminals, enable the users to transmit emergency signals, to the dispatcher, overriding any other activity taking place at the same time.

### Advantages

The main advantages of TETRA over other technologies (such as GSM) are:

- The much lower frequency used gives longer range, which in turn permits very high levels of *geographic* coverage with a smaller number of transmitters, thus cutting infrastructure costs.
- During a voice call, the communications are not interrupted when moving to another network site. This is a unique feature, which dPMR networks typically provide, that allows a number of fall-back modes such as the ability for a base station to process local calls. So called 'mission critical' networks can be built with TETRA where all aspects are fail-safe/multiple-redundant.
- In the absence of a network, mobiles/portables can use 'direct mode' whereby they share channels directly (walkie-talkie mode).
- Gateway mode - where a single mobile with connection to the network can act as a relay for other nearby mobiles that are out of range of the infrastructure. A dedicated transponder system isn't required in order to achieve this functionality, unlike with analogue radio systems.
- TETRA also provides a point-to-point function that traditional analogue emergency services radio systems did not provide. This enables users to have a one-to-one trunked 'radio' link between sets without the need for the direct involvement of a control room operator/dispatcher.
- Unlike cellular technologies, which connect one subscriber to one other subscriber (one-to-one), TETRA is built to do one-to-one, one-to-many and many-to-many. These operational modes are directly relevant to the public safety and professional users.
- Security TETRA supports terminal registration, authentication, air-interface encryption and end-to-end encryption.
- Rapid deployment (transportable) network solutions are available for disaster relief and temporary capacity provision.
- Network solutions are available in both reliable circuit-switched (telephone like) architectures and flat, IP architectures with soft (software) switches.

Further information is available from the TETRA Association (formerly TETRA MoU) and the standards can be downloaded for free from ETSI.

### Disadvantages

Its main disadvantages are:

- Security issues have been identified, although mitigations were quickly introduced in the TETRA security standard. There was an intentional weakening of the TEA1 cipher to meet export control criteria, allowing a break within a minute on consumer hardware. (See Description)
- Requires a linear amplifier to meet the stringent RF specifications that allow it to exist alongside other radio services.
- Data transfer is slow by modern standards.

Up to 7.2 kbit/s per timeslot, in the case of point-to-point connections, and 3.5 kbit/s per timeslot in case of IP encapsulation. Both options permit the use of between one and four timeslots. Different implementations include one of the previous connectivity capabilities, both, or none, and one timeslot or more. These rates are ostensibly faster than the competing technologies DMR, dPMR, and P25 are capable of. Latest version of standard supports 115.2 kbit/s in 25 kHz or up to 691.2 kbit/s in an expanded 150 kHz channel. To overcome the limitations many software vendors have begun to consider hybrid solutions where TETRA is used for critical signalling while large data synchronization and transfer of images and video is done over 3G / LTE / 5G.

### Technical details

#### Radio aspects

For its modulation TETRA, uses π⁄4 differential quadrature phase-shift keying. The symbol (baud) rate is 18,000 symbols per second, and each symbol maps to 2 bits, thus resulting in 36,000 bit/s gross.

As a form of phase shift keying is used to transmit data during each burst, it would seem reasonable to expect the transmit power to be constant. However it is not. This is because the sidebands, which are essentially a repetition of the data in the main carrier's modulation, are filtered off with a sharp filter so that unnecessary spectrum is not used up. This results in an amplitude modulation and is why TETRA requires linear amplifiers. The resulting ratio of peak to mean (RMS) power is 3.65 dB. If non-linear (or not-linear enough) amplifiers are used, the sidebands re-appear and cause interference on adjacent channels. Commonly used techniques for achieving the necessary linearity include Cartesian loops, and adaptive predistortion.

The base stations normally transmit continuously and (simultaneously) receive continuously from various mobiles on different carrier frequencies; hence the TETRA system is a frequency-division duplex (FDD) system. TETRA also uses FDMA/TDMA (see above) like GSM. The mobiles normally only transmit on 1 slot/4 and receive on 1 slot/4 (instead of 1 slot/8 for GSM).

Speech signals in TETRA are sampled at 8 kHz and then compressed with a vocoder using *algebraic code-excited linear prediction* (ACELP). This creates a data stream of 4.567 kbit/s. This data stream is error-protection encoded before transmission to allow correct decoding even in noisy (erroneous) channels. The data rate after coding is 7.2 kbit/s. The capacity of a single traffic slot when used 17/18 frames.

A single slot consists of 255 usable symbols, the remaining time is used up with synchronisation sequences and turning on/off, etc. A single *frame* consists of 4 slots, and a *multiframe* (whose duration is 1.02 seconds) consists of 18 frames. Hyperframes also exist, but are mostly used for providing synchronisation to encryption algorithms.

The downlink (i.e., the output of the base station) is normally a continuous transmission consisting of either specific communications with mobile(s), synchronisation or other general broadcasts. All slots are usually filled with a burst even if *idle* (continuous mode). Although the system uses 18 frames per second only 17 of these are used for traffic channels, with the 18th frame reserved for signalling, Short Data Service messages (like SMS in GSM) or synchronisation. The frame structure in TETRA (17.65 frames per second), consists of 18,000 symbols/s; 255 symbols/slot; 4 slots/frame, and is the cause of the *perceived* "amplitude modulation" at 17 Hz and is especially apparent in mobiles/portables which only transmit on one slot/4. They use the remaining three slots to switch frequency to receive a burst from the base station two slots later and then return to their transmit frequency (TDMA).

#### Radio frequencies

TETRA frequencies in South America
- Number  Frequency pair (MHz)
- Band 1  Band 2
- Emergency systems
- 1  380–383  390–393
- 2  383–385  393–395
- Civil systems
- 1  410–420  420–430
- 2  870–876  915–921
- 3  450–460  460–470
- 4  385–390  395–399.9

TETRA frequencies in other countries
- Country   Allocation   Frequency pairs (MHz)
- France   Civilian/private   410–430
- Emergency services   380–400
- Belgium   Emergency services/civilian   380–386.5, 390–396.5
- Commercial   410-420
- the Netherlands   Emergency services   380–386.5, 390–396.5
- Civil/Commercial   410–430
- Germany   Emergency services   380–385, 390–395, 406 - 410 for DMO
- Iceland    Emergency services/civilian   380–385, 390–395
- Ireland   Civilian/private   385–389.9, 395–399.9
- Emergency services   380–385, 390–395
- Italy   Emergency services / armed forces   380–390
- Civilian/private   462
- Norway   Emergency services   380–385, 390–395, 406.1–426, 870–876
- Slovenia   Emergency services   380-385 (MS), 390-395 (BS)
- South Africa   Emergency services, Public works   420–423
- Sweden   Emergency services   380-395
- Civilian/airport/public transportation   425-429
- UK   Airwave   390.0125–394.9875, 380.0125–384.9875
- Airwave (London only)   420.0125-421.9875, 410.0125–412.9875
- Prison service   450, 460 / 452, 462
- AirRadio   454, 464 or 460
- Offshore Oil platforms   423, 413
- Hong Kong   Emergency services   382.65–399.9, 410–430
- Civil/Private   806–818, 851–863
- Portugal   SIRESP - Public Safety   380–395
- Commercial/Private   420–430
- Saudi Arabia      350–370, 380–395, 385–399.99, 410–430, 450–470, 870–921

#### Air interface encryption

To provide confidentiality the TETRA air interface is encrypted using one of the *TETRA Encryption Algorithm* (*TEA*) ciphers. The encryption provides confidentiality (protect against eavesdropping) as well as protection of signalling.

Currently 7 different ciphers are standardized: TEA1 to TEA4 in TEA Set A and TEA5 to TEA7 in TEA Set B. These TEA ciphers should not be confused with the block cipher Tiny Encryption Algorithm. The TEA ciphers have different availability due to export control and use restrictions. In the past few details were published concerning these proprietary ciphers. Riess mentions in early TETRA design documents that encryption should be done with a stream cipher, due to the property of not propagating transmission errors. Parkinson later confirms this and explains that TEA is a stream cipher with 80-bit keys. The algorithms were later reversed and it appeared that TEA1 reduces its key strength to 32 bits to allow exportability under the Wassenaar arrangement. TEA1 and TEA4 provide *basic level* security, and are meant for commercial use. The TEA2 cipher is restricted to European public safety organisations. The TEA3 cipher is for situations where TEA2 is suitable but not available.

##### Security vulnerabilities of the air interface encryption

An in-depth review published in July 2023 by the company Midnight Blue B.V. of the TETRA standard and encryption algorithms, claims multiple security flaws, referred by the company as "TETRA:BURST". A total of 5 flaws were filed to the CVE database:

- The Air Interface Encryption (AIE) keystream generator is vulnerable to decryption oracle attacks due to the use of publicly-broadcast network time—keystream reuse can be triggered for acknowledged unicast communication when using static keys (security class 2). This is not applicable for group communication. Mitigations for this were introduced into version 4 of the TETRA standard.
- TEA1 contains a reduction step that effectively downgrades the cryptographic strength from 80 to 32 bits implemented to allow export under the Wassenaar convention, allowing anyone to break the cipher and subsequently decrypt the signal in as little as one minute using a modern-day consumer laptop. "There's no other way in which this can function than that this is an intentional backdoor," "This constitutes a full break of the cipher, allowing for interception or manipulation of radio traffic", according to the news report posted on *ComputerWeekly*. The reduction in strength of TEA1 seems to be known in intelligence circles and is referred to in the famous 2006 Wikileaks dump of US diplomatic communications.
- AIE contains no authentication for the ciphertext, making malleability attacks possible.
- The cryptographic anonymization scheme is weak and can be partially reversed to track users. A revised identity encryption scheme was introduced in version 4 of the TETRA standard in mitigation.
- The authentication algorithm theoretically allowed attackers to set the derived cipher key to 0 but not to decrypt traffic. Although this attack remains theoretical, mitigations were introduced in version 4 of the TETRA security standard.

In addition, the Midnight Blue B.V. team spots a "peculiarity regarding the TEA3 S-box", but further analysis has not been shown to lead to any weakness.

ETSI published TR 104 291 that addresses the additional measures put in place in the TETRA security standards for every perceived TETRA vulnerability. This allows TETRA operators and users to check with their TETRA system manufacturers and to perform a risk assessment to decide on the necessity or urgency of countermeasures.

The vulnerabilities related to algorithms remained publicly unknown for 28 years after TETRA's publication because TETRA did not initially make definitions of its cryptographic algorithms public, an example of security through obscurity, although details have now been made public. The Midnight Blue B.V. team gained access to TETRA's cryptographic code by attacking the trusted execution environment on a TETRA-enabled radio. The team points to a list of previously broken cryptographic systems relying on obscurity and argues that the Kerckhoffs's principle should have been followed: the system would have been safer when its structure is publicly known, despite common practice for encryption systems for government use to remain confidential.

#### Cell selection

##### Cell re-selection (or hand-over) in images

This first representation demonstrates where the slow reselect threshold (SRT), the fast reselect threshold (FRT), and propagation delay exceed parameters are most likely to be. These are represented in association with the decaying radio carrier as the distance increases from the TETRA base station.

From this illustration, these SRT and FRT triggering points are associated to the decaying radio signal strength of the respective cell carriers. The thresholds are situated so that the cell reselection procedures occur on time and assure communication continuity for on-going communication calls.

##### Initial cell selection

The next diagram illustrates where a given TETRA radio cell initial selection. The initial cell selection is performed by procedures located in the MLE and in the MAC. When the cell selection is made, and possible registration is performed, the *mobile station* (MS) is said to be attached to the cell. The mobile is allowed to initially select any suitable cell that has a positive C1 value; i.e., the received signal level is greater than the *minimum receive level for access* parameter.

The initial cell selection procedure shall ensure that the MS selects a cell in which it can reliably decode downlink data (i.e., on a main control channel/MCCH), and which has a high probability of uplink communication. The minimum conditions that shall have to be met are that C1 > 0. Access to the network shall be conditional on the successful selection of a cell.

At mobile switch on, the mobile makes its initial cell selection of one of the base stations, which indicates the initial exchanges at activation.

- Refer to EN 300 392 2 16.3.1 Activation and control of underlying MLE service
- Note 18.5.12 Minimum RX access level

The minimum receive access level information element shall indicate the minimum received signal level required at the SwMI in a cell, either the serving cell or a neighbour cell as defined in table 18.24.

##### Cell improvable

The next diagram illustrates where a given TETRA radio cell becomes *improvable*. The serving cell becomes improvable when the following occurs: the C1 of the serving cell is below the value defined in the radio network parameter cell reselection parameters, slow reselect threshold for a period of 5 seconds, and the C1 or C2 of a neighbour cell exceeds the C1 of the serving cell by the value defined in the radio network parameter cell reselection parameters, slow reselect hysteresis for a period of 5 seconds.

##### Cell usable

The next diagram illustrates where a given TETRA radio cell becomes *usable*. A neighbour cell becomes radio usable when the cell has a downlink radio connection of sufficient quality.

The following conditions must be met in order to declare a neighbour cell radio usable: The neighbour cell has a path loss parameter C1 or C2 that is, for a period of 5 seconds, greater than the fast reselect threshold plus the fast reselect threshold, and the service level provided by the neighbour cell is higher than that of the serving cell. No successful cell reselection shall have taken place within the previous 15 seconds unless MM requests a cell reselection. The MS-MLE shall check the criterion for serving cell relinquishment as often as one neighbour cell is scanned or monitored.

The following conditions will cause the MS to rate the neighbour cell to have higher service level than the current serving cell:

- The MS subscriber class is supported on the neighbour cell but not on the serving cell.
- The neighbour cell is a priority cell and the serving cell is not.
- The neighbour cell supports a service (that is, TETRA standard speech, packet data, or encryption) that is not supported by the serving cell and the MS requires that service to be available.
- The cell service level indicates that the neighbour cell is less loaded than the serving cell.

##### Cell relinquishable (abandonable)

The next diagram illustrates where a given TETRA radio cell becomes *relinquishable* (*abandonable*). The serving cell becomes relinquishable when the following occurs: the C1 of the serving cell is below the value defined in the radio network parameter cell reselection parameters, fast reselect threshold, for a period of 5 seconds, and the C1 or C2 of a neighbour cell exceeds the C1 of the serving cell by the value defined in the radio network parameter cell reselection parameters, fast reselect hysteresis, for a period of 5 seconds.

No successful cell reselection shall have taken place within the previous 15 seconds unless Mobility Management (MM) requests a cell reselection. The MS-MLE shall check the criterion for serving cell relinquishment as often as one neighbour cell is scanned or monitored.

##### Radio down-link failure

When the FRT threshold is breached, the MS is in a situation where it is essential to relinquish (or abandon) the serving cell and obtain another of at least *usable* quality. That is to say, the mobile station is aware that the radio signal is decaying rapidly, and must cell reselect rapidly, before communications are terminated because of radio link failure. When the mobile station radio-signal breaches the minimum receive level, the radio is no longer in a position to maintain acceptable communications for the user, and the radio link is broken.

Radio link failure: (C1 < 0). Using the suggested values, this would be satisfied with the *serving cell level* below −105 dBm. Cell reselection procedures are then activated in order to find a suitable radio base station.

Infrastructure TETRA parameters guide
- Coverage  Parameter  Distance (km)  Type of communication
- City   < 4  < 8  Pedestrian/metro
- Sub-urban   10–18  20–36  Bus/train
- Countryside   18–31  36–62  Inter-regional train
- In Air   > 32  > 64  In flight

### Man-machine interface (MMI)

#### Virtual MMI for terminals

Any given TETRA radio terminal using Java (Java ME/CLDC) based technology, provides the end user with the communication rights necessary to fulfil his or her work role on any short duration assignment.

For dexterity, flexibility, and evolution ability, the public transportation radio engineering department, have chosen to use the open sources, Java language specification administered by Sun and the associated work groups in order to produce a *transport application tool kit*.

Service acquisition admits different authorised agents to establish communication channels between different services by calling the service identity, and without possessing the complete knowledge of the ISSI, GSSI, or any other TETRA related communication establishment numbering plan. Service acquisition is administered through a *communication rights centralised service* or *roll allocation server*, interfaced into the TETRA core network.

In summary, the TETRA MMI aims are to:

- Allow any given agent while in exercise, to exploit any given radio terminal without materiel constraint.
- Provide specific transportation application software to the end-user agents (service acquisition, fraud, and aggression control).

This *transport application tool-kit* has been produced successfully and with TETRA communication technology and assures for the public transport application requirements for the future mentioned hereafter.

The *home* (*main*) menu presents the end user with three possibilities:

1. Service acquisition
2. Status SDS
3. End-user parameters

*Service acquisition* provides a means of virtually personalising the end user to any given radio terminal and onto TETRA network for the duration the end user conserves the terminal under his possession.

Status SDS provides the end user with a mechanism for generating a 440 Hz repeating tone that signals a fraud occurrence to members within the same (dynamic or static) Group Short Subscriber Identity (GSSI) or to a specific Individual Short Subscriber Identity (ISSI) for the duration of the assignment (an hour, a morning patrol or a given short period allocated to the assignment). The advantage being that each of the end users may attach themselves to any given terminal, and group for short durations without requiring any major reconfiguration by means of radio software programming tools. Similarly, the aggression feature functions, but with a higher tone frequency (880 Hz), and with a quicker repetitious nature, so to highlight the urgency of the alert.

The *parameters* tab provides an essential means to the terminal end-user allowing them to pre-configure the target (preprogrammed **ISSI** or **GSSI** ) destination communication number. With this pre-programmed destination number, the end-user shall liaise with the destination radio terminal or *roll allocation server*, and may communicate, in the group, or into a dedicated server to which the service acquisition requests are received, preprocessed, and ultimately dispatched though the TETRA core network. This simplifies the reconfiguration or recycling configuration process allowing flexibility on short assignments.

The parameters tab also provides a means of choosing between preselected tones to match the work group requirements for the purposes of fraud and aggression alerts. A possibility of selecting any given key available from the keypad to serve as an aggression or fraud quick key is also made possible though the transport application software tool kit. It is recommend to use the asterisk and the hash keys for the fraud and aggression quick keys respectively. For the fraud and aggression tones, it is also recommend to use 440 Hz slow repeating tone (blank space 500 milli-seconds) and 880 Hz fast repeating tone (blank space 250 milliseconds) respectively. The tone options are as follows: 440 Hz, 620 Hz, 880 Hz, and 1060 Hz.

The *parameters* page provides an *aid* or *help* menu and the last tab within parameters describes briefly the tool kit the version and the history of the transport application tool kit to date.

#### TETRA Enhanced Data Service (TEDS)

The TETRA Association, working with ETSI, developed the TEDS standard, a wideband data solution, which enhances TETRA with a much higher capacity and throughput for data. In addition to those provided by TETRA, TEDS uses a range of adaptive modulation schemes and a number of different carrier sizes from 25 kHz to 150 kHz. Initial implementations of TEDS will be in the existing TETRA radio spectrum, and will likely employ 50 kHz channel bandwidths as this enables an equivalent coverage footprint for voice and TEDS services. TEDS performance is optimised for wideband data rates, wide area coverage and spectrum efficiency.

Advances in DSP technology have led to the introduction of multi-carrier transmission standards employing QAM modulation. WiMAX, Wi-Fi and TEDS standards are part of this family.

Refer also to:

- JSR-118;
- Mobile Information Device Profile, JSR-37;
- Wireless Messaging API, JSR120;
- Connected Limited Device Configuration, JSR-139; and
- Technology for the Wireless Industry, JTWI-185.

### Comparison to Project 25

Project 25 and TETRA are utilised for the public safety Radio network and Private Sector Radio network worldwide however, it has some differences in technical features and capacities.

- TETRA: It is optimized for high population density areas, with spectral efficiency (4 time slots in 25 kHz: four communications channels per 25 kHz channel, an efficient use of spectrum). It is suitable for high population density areas and supports full duplex voice, data and messaging; but, it is generally unavailable for simulcast, VHF band - however particular vendors have introduced Simulcast and VHF into their TETRA platform..
- P25: it is optimized for wider area coverage with low population density, and support for simulcast. however, it is limited to data support. (Phase 1 P25 radio systems operate in a 12.5 kHz analogue, digital or mixed mode, and P25 Phase II will use a 2-timeslot TDMA structure in 12.5 kHz channels.)

Currently, P25 deployed to more than 53 countries and TETRA deployed to more than 114 countries.

### Professional usage

At the end of 2009 there were 114 countries using TETRA systems in Europe, Middle East, Africa, Asia Pacific, Caribbean and Latin America.

The TETRA system is in use in the following countries. Only TETRA network infrastructure installations are listed. TETRA being an open standard, each of these networks can use any mix of TETRA mobile terminals from a wide range of suppliers.

- Continent   Country   Supplier   Name   Agency   Status
- Asia   China mainland   EADS/Cassidian/Airbus   Shenyang Metro   Transport   In use: Line 1  
Rolling out: Line 2
- DAMM TetraFlex   Guangzhou Electric Power   Utility - Guangzhou Electric Power Emergency Communication   In use 2010
- EADS/Cassidian/Airbus   Shenzhen Metro   Transport   Ordered 5/2010
- EADS/Cassidian/Airbus   Guangzhou   16th Asian Games in 2010   Ordered 2010
- Hong Kong   EADS/Cassidian/Airbus   Hong Kong International Airport (HKIA)   2008 Beijing Olympics and Paralympic Games (Hong Kong Equestrian Event)   Used from July 2008 to October 2008
- EADS/Cassidian/Airbus   Hong Kong Fire Services Department   Fire service and ambulance   In use
- Motorola / Dimetra   Hong Kong Police Force   Police   In use
- Motorola   Correctional Services Department   Law enforcement   In use
- Motorola   Immigration Department   Law enforcement   In use
- Motorola   Mass Transit Railway (MTR)   Transport   In use
- Motorola / Dimetra   Hong Kong International Airport (HKIA)   Transport   In use since Feb 2009
- Motorola   CLP Power Hong Kong Limited   Electric   In use
- Hongkong Electric Co., Limited   Electric   In use
- Modern Terminals Limited   Container port   In use
- Hong Kong International Terminals Limited   Container port   In use
- Liaison Office of the Central People Government in the HKSAR   Diplomacy   In use
- India   Artevea   Military College of Telecommunication Engineering (MCTE)   Indian Army   In use since 2004 at Mhow, Indore, Madhya Pradesh
- Motorola / Dimetra   Delhi Metro Rail Corporation Ltd.   Transport   The First TETRA in India, in use since 2002
- DAMM TetraFlex / Consort Digital Pvt Ltd   Mumbai Mono Rail, Mumbai Metropolitan Region Development Authority (MMRDA)   Mass transport - India's first monorail project - Mumbai   Awarded 2010
- C-DAC   TETRA with Automatic Dial 100 (AD100)   Kerala police   In use by police, Trivandrum city, since 2008
- DAMM TetraFlex / Consort Digital Pvt Ltd   Tamil Nadu police   Police and internal security and safety   Awarded 2011
- HCL & Motorola   Secure Communication Network   Delhi government   Integrated Communication System used by various departments under government of Delhi and Delhi police since 2010.
- DAMM TetraFlex / Consort Digital Pvt Ltd   Gas Authority of India Limited (GAIL)   Gas pipeline - safety, telemetry and security   Awarded 2011
- THALES Portugal S A & Motorola   With PSTN call integration designed by Thales Group for BMRCL   BMRCL Bangalore Metro Corporation Limited   Transport, in use since March 2011
- Sepura & Rohde and Schwarz   TETRA with Automatic Dial 100 (AD100)   Gurgaon police   In use by police, Gurgaon city Since 2009. In Salem from August 2011.
- Sepura & Rohde and Schwarz   TETRA with Automatic Dial 100 (AD100)   Faridabad police   In use by police, Faridabad city, since 2012
- Indonesia   Motorola / Dimetra, installed & maintained by PT. Mobilkom Telekomindo   SCADA PT. Chevron Pacific Indonesia   HOOU   In use since 2009 at Duri, Riau, Indonesia.
- Rohde & Schwarz / Accessnet - T   Anti Corruption Agency   Anti Corruption Agency   Operational
- Rohde & Schwarz / Accessnet-T   Jakarta State Government Network   Jakarta Capital City Jakarta   Operational, Installed since 2007
- Kazakhstan   HMF Smart Solutions / ACCESSNET®-T IP   Kazakhstan Railways   Public Transport   In use
- Macao   Artevea   Melco-Crown Entertainment   Casino-Hotels: Altira (formerly Crown Macau), and City of Dreams   In use since 2007
- Motorola / Dimetra   Forças de Segurança de Macau   All emergency services   In use
- Malaysia   EADS/Cassidian/Airbus   Segi Maju (SEGI)   Public operator   In use
- Motorola / Dimetra   Sungai Buloh–Kajang line.   Transport   In use
- Motorola / Dimetra   Sungai Buloh–Serdang–Putrajaya line.   Transport   Operational 2021
- Maldives   Motorola / Dimetra   Maldives Police Service (MPS)   Police   In use
- Pakistan   Motorola / Dimetra   NITRS Nationwide Integrated Trunk Radio System Project for Police under Ministry of Interior, Government of Pakistan   Police   In use Since 2009
- Philippines   Motorola Dimetra/GA Technology and Systems Inc.   Shell Exploration   Oil and gas   In use October 2013, Phase 2 On Shore Gas Plant for Implementation
- Motorola Dimetra/GA Technology and Systems Inc.   Globe Telecom   Telecommunications carrier   Implementation on Going Project Finish Dec 2013
- Rohill (TetraNode) SynTech Systems Inc.   Meralco   Electric company   Implemented Nov 2014
- Rohill (TetraNode) SynTech Systems Inc.   Manila Line 2   Transport (Manila Light Rail Transit System Line 2)   Implemented Oct 2015
- Singapore   Leonardo   Singapore Metro   TETRA network for Cross Island Line   Awarded in 2025

Currently in deployment

- Leonardo   Singapore Metro   TETRA network for Jurong Line   Awarded in 2021

Currently in deployment

- South Korea   EADS/Cassidian/Airbus   Korea Electric Power Corporation (KEPCO)   Electricity   In use
- Taiwan   Leonardo   Taipei Rapid Transit Corporation Metro Service   TETRA network for Taipei Metro   Awarded in 2024

Currently in deployment

- Taiwan      Taiwan Railway   Transport   In use
- Taiwan High Speed Rail   Transport   In use
- Taipei Metro   Transport   In use
- Kaohsiung Mass Rapid Transit   Transport   In use
- Coast Guard Administration (Taiwan)   Republic of China Armed Forces   In use
- Thailand   Leonardo   Bangkok Metro   TETRA network for Orange Line   Awarded in 2025

Currently in deployment

- Africa   Algeria   Rohde & Schwarz   Sonatrach   Oil & gas company   In use since 2003.
- Sepura   Sonelgaz   Power utility   In use.
- Egypt   Motorolasolutions

Dimetra IP

MERC   Ministry of Interior, Suez Canal Authority, Oil& GAS and commercial users   In use, Nationwide
- Morocco   Rohill   ADM   Highway authority   Rolling out / Almost completed.
- Nigeria   Dizengoff/Motorola IL (Dimetra IP)   Nigeria LNG   Oil & gas   Since 2006
- Cisan International Limited/Rohill (TetraNode)   Mobil Ng   Oil   Since 2014
- Dizengoff/Motorola IL (Compact-Tetra IP)   Shell Ng   Oil   Since 2010
- Satcomm Integrated Resources LLC SatCom IRL/EADS      Nigerian Ports Authority, Nigeria (rolling out)   Rolling out
- Rohill (TetraNode)   Bayelsa State   Government   Since June 2012
- Briscoe Technologies / Hytera Accessnet   Lagos / Abuja / Port Harcourt   Oil industry / airports / security companies   In use Since 2006
- Namibia   Artevea   Namibian Police Force   Police   In use, nationwide
- South Africa   HMF Smart Solutions / ACCESSNET®-T IP   Sasol   Oil & Gas   In use
- Motorola Solutions DIMETRA   Police, traffic police   SAPS Gauteng   Gauteng province
- Motorola Solutions DIMETRA   Municipality, fire, and ambulance.   City of Cape Town   Cape Peninsula
- Rohill (TetraNode)   Mbombela Local Municipality   Nelspruit, Mpumalanga   Complete
- Rohill (TetraNode)   City Power   Johannesburg, Gauteng   Complete
- Rohill (TetraNode)   City of Tshwane Municipality   Pretoria, Gauteng   Complete
- Rohill (TetraNode)   Rustenburg Platinum Mine   Potgietersrus, Limpopo   Complete
- Sudan   Artevea   Ministry of Interior   Police   In use, nationwide
- Uganda   HMF Smart Solutions / ACCESSNET®-T IP   Entebbe international Airport   Airports   In use
- Europe   Austria   Motorola / Dimetra   TETRON   Police, fire, ambulance, and local train company.   In use
- HMF Smart Solutions / ACCESSNET®-T IP   Red Bull Arena, Salzburg   Events   In use
- Belgium   Airbus/Since 1998   nl:A.S.T.R.I.D. fr:A.S.T.R.I.D.   Police, fire, ambulance, customs, coast guard, hospitals, Red Cross, department of Justice, utility companies, airports, ports, lifeguard service, military.   Nationwide network
- Rohde & Schwarz since 2011/ ACCESSNET-T   ENTROPIA DIGITAL   Commercial & private security users.   Flanders & Brussels
- Croatia   Motorola / Dimetra   MUPNet   Police, fire brigades, ambulance service   Nationwide coverage (99,5%) in use
- Denmark   DAMM TetraFlex   DONG Energy Power Plants - 11 Power Plants across Denmark   Utilities - safety, security, telemetry   Awarded 2009
- Motorola / Dimetra   SINE   All emergency authorities, incl. police, fire, and ambulance.   Nationwide coverage (99,5%) in use
- Estonia   EADS/Cassidian/Airbus   ESTER   Police and border guard, fire, ambulance, and customs   Nationwide network
- Finland   Nokia; now EADS/Cassidian/Airbus   VIRVE   Police, fire, ambulance, customs, defence forces, and border guard   Nationwide network
- HelenNet   Energy company Helsingin Energia, tram operator HKL-Raitioliikenne, and several bus operators on HRTA's lines. Also used by some security guard companies, mostly securing HRTA's transport. Available for lease for various short-term uses.   In use, covers greater Helsinki region
- Germany   HMF Smart Solutions / ACCESSNET®-T IP   Stadtwerke Münster   Utilities   In use
- HMF Smart Solutions / ACCESSNET®-T IP   Würzburg Tramway   Public Transport   In use
- HMF Smart Solutions / ACCESSNET®-T IP   MIBRAG   Oil & Gas   In use
- Airbus   BOSNET   Police, fire, ambulance, customs, and coast guard.   Nationwide
- DAMM TetraFlex   Global Tech 1 Offshore Wind GmbH.   Utility Windfarm - Telemetry, Security and Safety Critical communications   Awarded 2012
- Hytera   Bremen Tramway   Transport   In use since 2018
- Greece   HMF Smart Solutions / Network Business Solutions   Piraeus Container Terminal   Ports   In use
- Motorola / Dimetra   COSMOTE TETRA Services  
Formerly branded OTElink (2009).   Business critical, public protection & disaster relief (PPDR) communications, public utility and oil-gas companies, seaports, airports, public and private transportation companies, public and private sector security personnel, other. Data applications nationwide including SCADA, AVL, M2M.   Extensive nationwide footprint, in use since 2002
- SEPURA   Teltronic   Police, Fire Services, Coast Guard   Nationwide roll-out in progress.
- Hungary   Pro-M Ltd.   EDR (acronym for Unified Digital Radiosystem)   Ambulance, army, Central Office for Administrative and Electronic Public Services, Civil Defence, Hungarian Prison Service, Hungarian Customs and Finance Guard, disaster management, fire, Hungarian Secret Services, Ministry of Environment and Water, and police   In-use
- HMF Smart Solutions / ACCESSNET®-T IP   Budapesti Közlekedési Vállalat (BKV)   Public Transport   In use
- Iceland   Motorola / Dimetra   TETRA Iceland   Police, fire services, ambulances, Search and Rescue units, Red Cross, bus service (Strætó Bs.), The Icelandic National Broadcasting Service, most utility companies, municipalities and private users such as excursion companies.   In-use
- Ireland   Motorola / Dimetra   TETRA Ireland   An Garda Siochana, HSE National Ambulance Service, Irish Prison Service, Irish Naval Service, Customs & Excise, civil defense (only a few units), Irish Coast Guard, mountain rescue (only a few units), Order of Malta Ambulance Corps, Irish Red Cross, St John Ambulance, National Emergency Office, Port of Cork, Revenue Commissioners and Office of Public Works.   Nationwide roll-out network complete. The fire services are planning to implement in the coming years. As of July 2011, TETRA Ireland now operates the national Paging System.
- Italy   HMF Smart Solutions/ Mobilcom   Priolo Servizi Consortium/Sicilia   Oil & Gas   In use
- Leonardo   MoI   Completion of the National PSS network (PIT)   Awarded in 2025

Currently in deployment

- Leonardo   Milan-Cortina Foundation   TETRA network for organisation and security services of Milano-Cortina Winter Olympics 2026   Awarded in 2025
- DAMM TetraFlex   Lombardi Ambulance Emergency Services   Ambulance - security, safety, communication   Awarded 2010
- SELEX ELSAG   Rete Interpolizie   Polizia di Stato (Italian state police), Carabinieri (military police), Guardia di Finanza (financial police), Polizia Penitenziaria (prison police), and Corpo Forestale Italiano (Italian forest brigades)   Rolling out
- DAMM TetraFlex   Rome International Airport   Airport - security, safety, commercial, fire, customs, police   Awarded 2009
- Latvia   Artevea   Ventamonjaks Serviss Ltd, Ventspils   Oil and gas   In use since 2007
- Motorola / Dimetra (SIA DAN Communications)   Riga Municipal Police   Local law enforcement in Riga   Ordered in 2016
- Motorola / Dimetra (SIA DAN Communications)   State Police   National law enforcement
- Luxembourg   Motorola / Dimetra   Renita   Government; police, fire brigade, ambulance services and others   Start building 2014, Operational since 2015
- Motorola / Dimetra   ConnectCom   Commercial network   Operational
- Motorola / Dimetra   ConnectCom   Public Transport, city of Luxembourg   Operational
- Motorola / Dimetra   ConnectCom   European Union   Operational
- North Macedonia   HMF Smart Solutions / ACCESSNET®-T IP   MoI   Public Safety   In use
- Hytera   Fire brigade of city Skopje   Fire department   In use
- Malta   Marconi      Civil Protection Force   July 2001
- Monaco   Motorola      Sûreté Publique (Police), Carabiniers (military police), fire brigades, ambulance   Nationwide coverage (including indoor public buildings)
- Montenegro   Motorola / Dimetra   Wireless Montenegro d.o.o.   Police, military, fire brigades, ambulance   In use since November 2012 Podgorica area only. Rolling out elsewhere.
- Netherlands   HMF Smart Solutions / ACCESSNET®-T IP   C2000   Police, fire, and ambulance   Nationwide network
- Motorola / Dimetra   ENTROPIA DIGITAL   Commercial users.   National license
- Motorola / Dimetra until 2019 ?, Hytera AccessNet-T since 2019 ??   HTM   Public transport The Hague   Regional network
- Motorola / Dimetra   CCTN / GVB   Public transport Amsterdam   Regional network
- Rohill   RET   Public transport Rotterdam   Regional network
- Rohill   Schiphol Airport   Schiphol Group, KLM, and other businesses   Local network
- Sepura   TATA steel Europe   Hoogovens   Local network
- Norway   Motorola / Dimetra   Norwegian Public Safety Radio   Police, fire, ambulance, civil defense and search and rescue   Nationwide rollout completed September 2015
- Motorola   Ruter/Sporveien   Public Transport, Oslo   Established before 2003
- Portugal   Motorola   SIRESP   Police (PSP and GNR), fire, ambulance and civil protection   Nationwide roll-out, in use since 2007
- Motorola   Lisbon International Airport (LPPT)   Transport - Ground operations   Local Network
- Poland   Motorola   Ministry of Interior, Polish army, and Warsaw police   Police, fire, public transport, airports, and army.   In use since 2000
- HMF Smart Solutions / ACCESSNET®-T IP   Chopin Airport, Warsaw   Airports   In use
- Rohill (TetraNode)   Szczecin, Warsaw and Kraków police   Roll-out ongoing.   Modern IP based TETRA solution for 3 cities
- Romania   Motorola / Dimetra   Special Telecommunications Service (STS)   Police, fire, and search and rescue   Nationwide
- Motorola   Dimetra   Ministry of Administration and Interior (MAI) / Romanian Border Police (RBP)   In use since 2008 for police, emergency and search and rescue agencies from Romanian border counties-wide
- EADS/Cassidian/Airbus   TETRA EADS   Ministry of Administration and Interior (MAI) / Romanian Border Police (RBP)   In use since 2010 for police, emergency and search and rescue agencies from Romanian border counties-wide
- Hytera/Motorola/Sepura   HamTetra Network Romania   Amateur radio users engage in both DMO (Direct Mode Operation) and TMO (Trunked Mode Operation) modes, both within the country and globally, connecting through gateways such as Zello and SVXLink.

Ham Tetra Romania Network Architecture was developed and published along with users map and equipment used on the YO8TEH website

Tetra gear in ham radio was initially introduced by YO8TEH in 2014 in DMO (Direct Mode Operation). Subsequently, it evolved into gateways through platforms like Zello and Teamspeak. In 2021, a part of the system was split and migrated to svxlink, along with its classic application. The first Tetra Repeater for Ham Radio use in Romania was licensed under the call sign YO8TEH-1, while the second TMO repeater was licensed under the call sign YO8Q.
- Russia   DAMM TetraFlex   Moscow Metro (second most heavily used rapid transport system in the world)   Transport - rail - telemetry, safety, security, police, ambulance, fire   Awarded 2011
- Sepura   Unified system of operational trunking radio (Единая Система Оперативной Транкинговой Радиосвязи)   Fire, ambulance and partially, police   Launched in 2008
- DAMM TetraFlex   Russias Kaliningrad Power Plant.   Utility power plant - safety and security - telemetry and commercial agents   Awarded 2009
- DAMM TetraFlex   St Petersburg and North West Russia.   Government - ambulance and emergency services, police, healthcare facilities, utility services, St. Petersburg Authorities and the regional civil defense   Awarded 2011
- Serbia   Motorola / Dimetra   Ministry of Interior   Police, fire brigades, ambulance   Fully rolled out as of 2009
- Slovenia   Selex/OTE/Marconi   Ministry of Interior   Police   In central Slovenia
- Spain   Motorola   Basque Country   Mainly police   In use since 2006
- Teltronic   Basque Country   Mainly municipalities and public services   In use since 2009
- EADS/Cassidian/Airbus   Catalonia   Police, fire brigades, civil protection, ambulances, forest guards, water agency, gas company, road maintenance service and other public agencies   In use since 2006
- Sweden   SAAB, Cassidian, Eltel Networks   RAKEL   Managed by the Civil Contingencies Agency - MSB. For use by the emergency services and others in the fields of civil protection, public safety and security, emergency medical services and healthcare, road services, nuclear facilities.   In operation, covering 99.8% of Sweden's population and 95% of its territory
- Motorola   Tetra   Stockholm public transport: used by transport security officers for dispatch internal communications, Transport Police ("Tunnelbanepolisen") and other police forces for liaison with transport officials. Roll-out stage for train operations on underground.   In operation / roll-out
- Rohde & Schwarz   Got1   Got1 is a modern IP based Tetra network used in the west parts of Sweden. Mainly in the Gothenburg region. With customers like SKF and Volvo Trucks.   In operation
- United Kingdom   Motorola / Dimetra / Sepura   Airwave   Police, fire, NHS ambulance services, Border Force, immigration enforcement, some armed forces, National Highways traffic officers, civil contingency services, HM Coastguard, St John Ambulance, St John Cymru, British Red Cross, Highland Council, and miscellaneous emergency services.   Full emergency service rollout complete
- Hytera   Tetra   Prison Service   Operational
- Motorola / Dimetra   Connect   Transport for London (London Underground)   Used by all Tube staff and relaying Airwave for BTP when underground
- AirRadio AR-en      Use by some services at some major airports   (Heathrow, Birmingham, Manchester, Glasgow, Aberdeen)
- Middle East   Israel   Motorola   Mountain Rose   Israel Defense Forces (IDF)   In use by IDF, country-wide
- Turkey   DAMM TetraFlex   Alacer Gold Mine   Mining - safety and security critical communications   Awarded 2012
- United Arab Emirates   EADS/Cassidian/Airbus   Nedaa   Police, emergency services, and professional communications   Dubai, Sharjah, Ajman, Umm Al-Qaiwain, Ras Al-Khaimah, and Fujairah operational
- EADS/Cassidian/Airbus   Polikom   Police, emergency services, and professional communications   Abu Dhabi
- Qatar   HMF Smart Solutions / ACCESSNET®-T IP   Ooredoo, nationwide network   Operator/Industry   In use
- EADS/Cassidian/Airbus      Ministry of Interior, army, police, air force search and rescue, EMS (medical).   Initial use for the 15th Asian Games all games venues inclusive of transportation routes for "blue light" services, later extended to cover the State of Qatar. Known as Qatar Secure TETRA Radio System (QSTRS).
- Saudi Arabia   Leonardo   Riyadh Metro   Extension of existing TETRA network for Riyadh Metro   Awarded in 2025

Currently in deployment

- Latin America   Mexico   Rohde & Schwarz / Sepura   Mazatlán, Sinaloa Police & Emergency Services   Police, emergency services operational   Operational
- South America   Argentina   HMF Smart Solutions / ACCESSNET®-T IP   Mendoza   Public Safety   In use
- Brazil   Motorola   América Latina Logística   Railroad, communication and licensing.   Operational
- Teltronic / Motorola   Polícia Rodoviária Federal   Road patrol, country-wide   In operation / national roll-out in progress
- Teltronic / Motorola   12 states   Public Safety Agencies   In operation, 600+ stationary stations.
- Chile   HMF Smart Solutions / ACCESSNET®-T IP   Gendarmeria de Chile   Public Safety   Awarded 2025
- Peru   HMF Smart Solutions / ACCESSNET®-T IP   National Police and district units of Pucallpa   Public Safety   In use
- Caribbean   Windward Islands and Leeward Islands   Rohill   Zenitel, C3 since 2005   Police, emergency services, oil and professional communications   Aruba, Bonaire, Curaçao, Sint Maarten, Saint Martin, Saba, Sint Eustatius, and Anguilla operational
- Dominican Republic   Hytera US / HMF Smart Solutions      Public Safety   In use
- Oceania   Australia   DAMM TetraFlex   BHP Billiton   Temco Smeltering Tasmania - mining, commercial, safety, security   Awarded 2011
- DAMM TetraFlex   Rio Tinto   Western Australia Mining   Awarded 2009
- Rohill Tetra   Inpex   Ichthys LNG   Infrastructure
- Rohill Tetra   BHP Billiton   Macedon Gas   Infrastructure
- DAMM TetraFlex   Origin Energy (APLNG)   Kordia Solutions   Australian Pacific Project
- Rohill Tetra   Goldlinq   Goldcoast rail   Goldcoast infrastructure
- DAMM TetraFlex   Fortescue Metals group   Open cut mining   Awarded 2011
- DAMM TetraFlex   Gorgon LNG Project, Chevron, Australia   Gas and pipelines   Awarded 2011
- Motorola   BHP Billiton   Pyrenees FPSO   Awarded 2016
- Motorola   Zeon   Local government   Operational across Brisbane City Council, including the Brisbane State Emergency Service Unit
- DAMM TetraFlex   Australian Submarine Co   Military, defence, comms, safety, security   Awarded 2012
- Motorola   Zeon   Tertiary education   Used by Queensland University of Technology security staff.
- Sepura         Being used by several Mining Operations throughout Western Australia and Queensland - Terminals only - No Infrastructure.
- New Zealand   DAMM TetraFlex   BHP One Steel   Aluminium Smelter - ore production - safety, security, operations   Awarded 2012
- Kordia   KorKor   Airports   Used by Wellington International Airport, Air New Zealand
- Kordia   KorKor   Councils   Used by Hutt City, Auckland Transport
- Teltronic   Widarcom   Commercial network launched 2008   Used by University of Auckland, Westpac

### Amateur radio usage

In the past decade, TETRA has seen an uptick in usage in the amateur radio community. The perceived higher audio quality compared to other digital voice modes, capacity for packet data, SDS, single frequency DMO repeaters, close proximity of the [UHF (430-440MHz) amateur radio band](70-centimeter%20band.md) and full duplex audio in TMO are motivating arguments to experiment contacts with this technology.

Multiple constraints have to be noted when using TETRA for amateur radio service:

- In most countries, encryption cannot be used.
- Most older (pre-2010) terminals don't cover the Region 1 amateur radio frequency range (430–440) natively, and must be modified via software with a possible impact on RF performance.

Multiple amateur DMO and TMO networks are established throughout Europe.

Additionally, an open-source project aims to create a complete SDR-based TETRA stack, with a working DMO repeater proof of concept.

---

*Source: Wikipedia, TETRA (https://en.wikipedia.org/wiki/TETRA), by Wikipedia contributors, CC BY-SA 4.0.*
