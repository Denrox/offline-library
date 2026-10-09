# Winlink

**Winlink**, or formally, **Winlink Global Radio Email** (registered US Service Mark), also known as the **Winlink 2000 Network**, is a worldwide radio messaging system that uses amateur-band radio frequencies and government frequencies to provide radio interconnection services that include email with attachments, position reporting, weather bulletins, emergency and relief communications, and message relay. The system is built and administered by volunteers and is financially supported by the Amateur Radio Safety Foundation.

### Network

Winlink networking started by providing interconnection services for [amateur radio](Amateur%20radio.md) (also known as *ham radio*). It is well known for its central role in emergency and contingency communications worldwide. The system used to employ multiple central message servers around the world for redundancy, but in 2017–2018 upgraded to Amazon Web Services that provides a geographically-redundant cluster of virtual servers with dynamic load balancers and global content-distribution. Gateway stations have operated on sub-bands of [HF](High%20frequency.md) since 2013 as the *Winlink Hybrid Network*, offering message forwarding and delivery through a mesh-like smart network whenever Internet connections are damaged or inoperable. During the late 2000s, it increasingly became what is now the standard network system for radio email, worldwide. Additionally, in response to the need for better disaster response communications in the mid to later part of the 2000s, the network was expanded to provide separate parallel radio email networking systems for the US Department of Homeland Security SHARES Winlink Radio Email System, along with other governments (non-amateur radio) services, also to include Non-government Organizations such as the US American Red Cross, the Austrian International Red Cross, and other such critical infrastructure Non-Government Organizations. Although these services are separate, and for reasons of security may be unknown to each other, the capability to cross services with complete Interoperability is available. For example, a US ham using Winlink on the amateur radio spectrum may email a Winlink user on the DHS SHARES Winlink system (non-amateur) radio service, which may then be picked up on the DHS SHARES Winlink network system. Of course, the originator of any service must be familiar with the regulatory environment of the recipient's service should it be another Winlink service.

### Amateur radio HF e-mail

E-mail via [HF](High%20frequency.md) can be used nearly everywhere on the planet, and is made possible by connecting an HF single sideband (SSB) transceiver system to a computer, modem interface, and appropriate software. The HF modem technologies include PACTOR, Winmor (deprecated), ARDOP, Vara HF, and Automatic Link Establishment (ALE). VHF/UHF protocols include AX.25 Packet and Vara FM.

#### Guidelines

Operators in each country must, as a baseline, follow the appropriate regulatory guidelines for their license. Some countries may limit or regulate types of amateur messaging (such as e-mail) by content, origination location, end destination, or license class of the operator. Origination of *third party messages* (messages sent on behalf of, or sent to, an end destination who is not an amateur operator) may also be regulated in some countries; those that limit such *third party messages* normally have exceptions for emergency communications. In accordance with long standing amateur radio tradition, international guidelines and FCC rules section 97.113, hams using the Winlink system are advised that it is not appropriate to use it for business communications.

### Users

The Winlink system is open to properly licensed amateur radio operators, worldwide. The system primarily serves radio users without normal access to the internet, government and non-government public service organizations, medical and humanitarian non-profits, and emergency communications organizations. As of July 2008, there were approximately 12,000 radio users and approximately 100,000 Internet correspondents. Monthly traffic volume averages over 100,000 messages.

For offshore cruising yachts, Winlink is widely used as an alternative, or alongside, Sailmail, which is an HF PACTOR based-email system using marine HF frequencies rather than amateur, and unlike the amateur radio use of Winlink, allows business to be conducted over radio. In addition to email, Winlink uses a system called "Saildocs," and other file delivery methods, which allows properly licensed amateur radio cruisers to retrieve meteorological, maritime safety and other crucial files over Winlink email. As example, Winlink was found to be more useful in and around South Africa where best weather was provided by SAMNet (South African Mobile Maritime Net).

### Supported radio technologies

- 802.11 WiFi
- ALE (Automatic Link Establishment)
- [APRS](Automatic%20Packet%20Reporting%20System.md) ([Automatic Packet Reporting System](Automatic%20Packet%20Reporting%20System.md))
- [AX.25](AX.25.md) Packet Radio
- D-Star
- PACTOR
- PACTOR-II
- PACTOR-III
- PACTOR-IV
- Winmor (deprecated)
- ARDOP
- Vara HF
- Vara FM
- TCP/IP (Telnet and other wireless technologies)

### Technical protocols

PACTOR-I, Winmor(deprecated), ARDOP, HSMM (WiFi), AX.25 packet, D-Star, TCP/IP, and ALE are non-proprietary protocols used in various RF applications to access the Winlink network systems. Later versions of PACTOR are proprietary and supported only by commercially available modems from Special Communications Systems GmbH. In amateur radio service, *AirMail*, *Winlink Express*, and other email client programs used by the Winlink system, disable the proprietary compression technology for PACTOR-II, PACTOR-III, and PACTOR-IV modems and instead relies on the open FBB protocol, also widely used worldwide by [packet radio](Packet%20radio.md) BBS forwarding systems.

### US regulatory issues

In May 1995, the American Radio Relay League (ARRL) privately asked the FCC to change Part 97.309(a) to allow fully documented G-TOR, Clover, and original open source PacTOR (Pactor I) modes. The FCC granted this request in DA-95-2106 based on the ARRL's representation that it had worked with developers to ensure complete technical documentation of these codes were available to all amateur radio operators. However, subsequent versions of Pactor contained proprietary compression algorithms that prevent over-the-air interception. As of July 9, 2024, the Winlink Development Team has stated that their software only uses an open compressed binary format called Open B2F, which is publicly listed on the Winlink website, and replaces proprietary compression used by some manufacturers of protocols used.

In 2007, a US amateur radio operator filed a formal petition with the Federal Communications Commission (FCC) aimed at reducing the signal bandwidth in automatic operation subbands; but, in May 2008 FCC ruled against the petition. In the Official Order, FCC said, "Additionally, we believe that amending the amateur service rules to limit the ability of amateur stations to experiment with various communications technologies or otherwise impeding their ability to advance the radio art would be inconsistent with the definition and purpose of the amateur service. Moreover, we do not believe that changing the rules to prohibit a communications technology currently in use is in the public interest."

In 2013, the FCC ruled in Report and Order 13-1918 against the use of encryption in the US amateur radio bands for any purpose, including emergency communications. The FCC cited the need for all amateur radio communications to be open and unobscured, to uphold the Commission's long-standing requirement that the service be able to police itself.

Winlink itself uses point-to-point protocols that may be copied by a third party through methods provided by the authors of these protocols as well as from independent sources. Because the content of data is not obstructed on the amateur spectrum, those government agencies who do use Winlink for Continuity of Government and public safety emergency communications requested (or in some cases, mandated) that they be allowed to encrypt their messages.

On non-amateur radio frequencies worldwide, Winlink provides for encryption via AES-256 for its most used protocols, Pactor and VARA. Such transmission encryption, once set up properly, is seamless to the end-user and requires no additional effort, but is left up to the individual operator or government agency to setup.

In addition to "readers" being made available for protocols used by the Winlink system, in the US, all messages passing through licensed US amateur radio stations by radio are freely accessible by other licensed amateurs via the WinLink Open Message Viewer on the Winlink WebSite. Amateurs concerned about encryption are encouraged to help the US amateur radio community police itself by search and viewing such messages, and reporting messages if they spot a violation.

#### Deletion of the Symbol Rate Rule RM-11708

This change was requested in 2013 by ARRL, and the FCC released notice of proposed rulemaking in 2016. In November 2023, the FCC finally removed the symbol rate limit of 300 baud in favor of an occupied bandwidth limit of 2.8 kHz (WT Docket No. 16-239). In the Report and Order, the FCC stated, "The amateur radio community can and does play a vital role in emergency response communications, but is often unnecessarily hindered by the baud rate limitations in the rules."

Supporting this change were a host of federal, state and local emergency management agencies, who continually wrote *ex parte* comments to the FCC regarding their concerns with the impact such a limitation had on emergency email communications via Winlink. In addition, American Radio Relay League (ARRL) continued to push its efforts toward this change through Congressional pathways.

---

*Source: Wikipedia, Winlink (https://en.wikipedia.org/wiki/Winlink), by Wikipedia contributors, CC BY-SA 4.0.*
