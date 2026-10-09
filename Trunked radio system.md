# Trunked radio system

A **trunked radio system** (**TRS**) is a [two-way radio](Two-way%20radio.md) system that uses a control channel to automatically assign frequency channels to groups of user radios. In a traditional half-duplex [land mobile radio system](Land%20mobile%20radio%20system.md) a group of users (a *talkgroup*) with mobile and portable two-way radios communicate over a single shared radio channel, with one user at a time talking. These systems typically have access to multiple channels, up to 40-60, so multiple groups in the same area can communicate simultaneously. In a conventional (non-trunked) system, channel selection is done manually; before use, the group must decide which channel to use, and manually switch all the radios to that channel. This is an inefficient use of scarce radio channel resources because the user group must have exclusive use of their channel regardless of how much or how little they are transmitting. There is also nothing to prevent multiple groups in the same area from choosing the same channel, causing conflicts and 'cross-talk'. A trunked radio system is an advanced alternative in which the channel selection process is done automatically, so as to avoid channel conflicts and maintain frequency efficiency across multiple talkgroups. This process is handled by what is essentially a central * radio traffic controller*, a function automatically handled by a computer system.

Trunking is a more automated and complex radio system, but provides the benefits of less user intervention to operate the radio and greater spectral efficiency with large numbers of users. Instead of assigning a radio channel to one particular user group at a time, users are instead assigned to a logical grouping, a *talkgroup*. When any user in that group wishes to communicate with another user in the talkgroup, an idle radio channel is found automatically by the system and the conversation takes place on that channel. Many unrelated conversations can occur on a channel, making use of the otherwise idle time between conversations. Each radio transceiver contains a microprocessor that handles the channel selection process. A control channel coordinates all the activity of the radios in the system. The control channel computer sends packets of data to enable one *talkgroup* to talk together, regardless of frequency.

The primary purpose of this type of system is efficiency; many people can carry many conversations over only a few distinct frequencies. Trunking is used by many government entities to provide two-way communication for fire departments, police and other municipal services, who all share spectrum allocated to a city, county, or other entity. A secondary benefit of a trunking radio system is the ease with which it can accommodate radio interoperability and with proper planning, add authorized user agencies to the system post-implementation.

### Principles of operation

#### Control channels

In essence, a trunked radio system is a packet switching computer network. Users' radios send data packets to a computer, operating on a dedicated frequency — called a control channel — to request communication on a specific talkgroup. The controller sends a signal to all radios monitoring that talkgroup, instructing the radios to automatically switch to the frequency indicated by the system to monitor the transmission. After the user is finished speaking, the users' radios return to monitoring the control channel for additional transmissions.

This arrangement allows multiple groups of users to share a small set of radio frequencies without hearing each other's conversations. Trunked systems primarily conserve limited radio frequencies and also provide other advanced features to users.

#### Talkgroups

A 'talkgroup' is an assigned logical group of users on a trunked radio system. Unlike a [conventional radio](Two-way%20radio.md) which assigns users a certain frequency, a trunk system uses a number of frequencies allocated to the entire system. Then the control channel coordinates the system so talkgroups can share these frequencies seamlessly. The purpose is to dramatically increase system capacity with optimal use of frequencies. Many radios treat talkgroups as if they were frequencies, since they behave that way. For example, on a [radio scanner](Radio%20scanner.md) it is common to assign talkgroups into banks or lock them out, exactly like conventional frequencies.

#### Fleet maps and IDs

Each system is built with a number of system talkgroups identified as required by the planned user agencies, to which new talkgroups can easily be added as the system matures and new agencies or new requirements are identified. For each user agency, talkgroups are assigned in an agency 'fleetmap'. The fleetmap lays out the various talkgroups that the agency requires to successfully undertake its business. For example, in an ambulance service fleetmap there will be a talkgroup created for each of the hospital ER's that the ambulances interact with; talkgroups for communications with dispatch(s), talkgroups for special events or disasters, a talkgroup for air medical transport, and a number of talkgroups that are shared (with appropriate controls) with other first response agencies such as police and fire services. Each talkgroup is assigned a unique digital ID on the system so that the controller can direct transmissions to the radios which are intended to receive them. Within the same shared system there can be a fleet of ambulances, a fleet of police users, and a fleet of firefighters. In most shared public safety/public service systems, whether city-wide, or state/province-wide, there are often additional users sharing the system at a pre-determined lower priority for service such as animal control, public works, highways maintenance, correctional services, natural resources, etc. The system may also include talkgroups for federal agencies operating within the jurisdiction and in some cases commercial users which provide assistance to general public safety. These fleetmaps are considered subfleets of the actual talkgroups. The subfleets are intuitively programmed into the users' radios so that the users can easily find a talkgroup when s/he is required to switch for a particular situation. Alternatively, a trunking system dispatch console operator can actually 'patch' two talkgroups together making a new 'virtual' talkgroup to allow users from different agencies to communicate without having to switch channels.

Generally in planning a multi-agency trunking radio system, each agency is assigned a 'block' of talkgroup ID numbers based on the number of talkgroups they anticipate requiring, plus some excess for future expansion. Thus a police service block of talkgroup ID's might begin with 102100 up to 102199, and a fire service block on the same system might begin with 102200 up to 102299. This identifies the system as 102XXX and provides one hundred talkgroup ID's for each agency. Agency-shared talkgroups (sometimes referred to as Mutual Aid or Inter-agency) may be assigned a block starting at 102500 up to 102520, allowing for twenty shared talkgroups that can be offered for use by any authorized agency. In many province-wide systems, it is mandatory for participation in the system for user agencies to include all of the authorized shared talkgroups and/or shared simplex frequencies.

#### Scanning

Most scanners that can listen to trunked radio systems (called trunk tracking) are able to scan and store individual talkgroups just as if they were frequencies. The difference in this case is that the groups are assigned to a certain bank in which the trunked system is programmed. In other words, the talkgroups are stored on the trunked bank.

#### Comparison with telephone trunking

The concept of trunking (resource sharing) is actually quite old, and is taken from telephone company technology and practice. Consider two telco central office exchanges, one in town "A" and the other in adjacent town "B". Each of these central offices has the theoretical capacity to handle ten thousand individual telephone numbers. (Central office "A", with prefix "123", has available 10,000 numbers from 123-0000 to 123-9999; central office "B", with prefix "124", the same.)

If all 10,000 subscribers in "A" were to simultaneously call 10,000 subscribers in "B", then it would be necessary to have 10,000 lines to connect the two towns. However, the odds of that happening are remote, as the number of simultaneous phone calls is usually much lower. Erlang-B is a common formula that predicts the optimal number of trunk lines actually needed under normal conditions.

This concept has been simply applied to radio user groups, to determine the optimal number of channels needed, under normal conditions, to accommodate a given number of users. In the event of a widespread emergency such as a major earthquake, many more users than normal will attempt to access both the telephone and radio systems. In both cases once the trunking capacity of the systems is fully used, all subsequent users will receive a busy signal. In such a case management of communications becomes critical with only very local communications sharing simplex (non-system) frequencies, and longer distance communications sharing pre-planned trunking talkgroups and governing use of the resources to essential communications.

In our example of police dispatch, different talkgroups are assigned different system priority levels, sometimes with 'preemption' capability, attempting to ensure that communication between critical units is maintained.

### Differences from conventional two-way radio

'Trunked' radio systems differ from 'conventional' radio systems in that a conventional radio system uses a dedicated channel (frequency) for each individual group of users, while 'trunking' radio systems use a pool of channels which are available for a great many different groups of users.

For example, if police communications are configured in such a way that twelve conventional channels are required to permit citywide dispatch based upon geographical patrol areas, during periods of slow dispatch activity, much of that channel capacity is idle. In a trunked system, the police units in a given geographical area are not assigned a dedicated channel, but instead are members of a talk-group entitled to draw upon the common resources of a smaller pool of channels.

#### Advantages of Trunking

Trunked radio takes advantage of the probability that with any given number of users, not everyone will need channel access at the same time, therefore fewer discrete radio channels are required. From another perspective, with a given number of radio channels, a much greater number of user groups can be accommodated. In the example of the police department, this additional capacity could then be used to assign individual talkgroups to specialized investigative, traffic control, or special-events groups which might otherwise not have the benefit of individual private communications.

To the user, a trunking radio looks just like an 'ordinary' radio: there is a 'channel select switch' for the user to select the 'channel' that they want to use. In reality though, the 'channel switch' is not switching frequencies as in a conventional radio but when changed, it refers to an internal software program which causes a new talkgroup affiliation to be transmitted on the control channel. This identifies the specific radio to the system controller as a member of a specific talkgroup, and that radio will then be included in any conversations involving that talkgroup.

This also allows great flexibility in radio usage – the same radio model can be used for many different types of system users (i.e. Police, Fire, Public Works, Animal Control, etc.) simply by changing the software programming in the radio itself.

Since the talkgroups are constantly transmitting on different frequencies, trunked radio systems makes it more difficult for a scanner listener without a programmed trunk tracking scanner to keep up with the conversation.

In 1997, [radio scanners](Radio%20scanner.md) compatible with trunked systems appeared on the market. One of the first companies to bring these devices to market, Uniden, trademarked the term 'trunk tracking' on December 5, 1997.

### Types of trunked radio systems

This is not a list of manufacturers' equipment types, it is intended as a list of air protocol types unless significant vendor specific modifications have been made which violate the published standard.

Trunked radio technologies have diverged into three distinct types or 'tiers'. These are not 'official', but are clearly defined within protocol types:-

#### Specialized Mobile Radio

**Specialized Mobile Radio** (**SMR**) may be an analog or digital trunked [two-way radio](Two-way%20radio.md) system, operated by a service in the VHF, 220, UHF, 700, 800 or 900 MHz bands. Some systems with advanced features are referred to as an **Enhanced Specialized Mobile Radio** (**ESMR**). Specialized Mobile Radio is a term defined in US Federal Communications Commission (FCC) regulations. The term is of US regulatory origin but may be used in other regions to describe similar commercial systems which offer a radio communications service to businesses.

SMRs were created when the Federal Communications Commission began to license business and commercial 800 MHz two-way radio systems in the late 1970s.

##### Quality of service

In SMR systems, many factors affect the quality of service. This may include the capacity of the radio system versus the number of radio units using the system. A talkative user community may cause busy signals while a disciplined, professional group of SMR users may keep channels idle.

Some systems experience seasonal peaks. For example, a trunked system in an agricultural area used by crop harvesting crews may overload and experience busy signals during peaks in harvesting. A system used by a ski resort may overload on a holiday weekend. Disaster planning experts like to say that trunked system users are likely to hear busy signals for the first time when a disaster occurs. A major flood or earthquake is likely to generate a level of call traffic that loads the system to capacity.

Siting of the system affects coverage: the system [antennas](Antenna%20%28radio%29.md) should overlook the desired coverage area. Federal Communications Commission regulations require systems using the same radio frequency to be spaced 70 miles from one another or do an engineering study to confirm there will be no interference from closer spacing.

Maintenance practices also can affect quality. In some systems, the operator may remove one channel of a trunked system from service to perform repairs. In a heavily used system, this could cause busy signals.

Engineering documentation for these systems suggests another evaluation would be *delivered audio quality*. This is a measurement of the sound quality over all of the involved pieces of communications equipment from end to end. The first clue this may be an issue is that radio users with normal hearing have trouble understanding others when speaking over the radio.

#### Entry-level

These systems are relatively simple in their operation and only meet the minimum requirements to be defined as a 'trunked' radio system. They generally do not have enhanced features such as data communications or registration awareness. They will provide simple trunking facilities for voice calls only.

- SmarTrunk
- Ericsson GE
- EDACS Provoice
- EDACS
- GE Mark V
- Logic Trunked Radio
- LTR Standard
- LTR Passport
- LTR Standard and Passport
- LTR MultiNet
- LTR-Net
- Motorola
- Type I
- Type II
- Type IIi Hybrid
- Type II SmartZone
- Type II SmartZone OmniLink

#### Standard

These systems exhibit some of the characteristics of a high tier trunked radio system but not all features. Therefore, they are suitable for small deployments where users are expected to use the entire network available (such as a private system covering a campus or town). Because of their lack of advanced features they generally are not suited to mission critical deployments, public access mobile radio (PAMR) type operation or uncoordinated shared user types.

DMR/dPMR true Tier 3/Mode 3 protocols are intended eventually to migrate into the "Advanced Mature high end" list below but as of 2015 cannot be classified as such due to major interoperability issues, lack of mature protocol and lack of clearly defined user interface protocol.

- OpenSky System
- APCO Project 16
- [dPMR](Digital%20private%20mobile%20radio.md) Mode 3
- DMR Tier III
- Kenwood NEXEDGE Digital trunked radio
- Icom IDAS Digital trunked Land Mobile Radio
- [Hytera](Hytera.md)
- Motorola, Motorola Capacity Plus, Motorola Connect Plus
- iDEN (integrated Digital Enhanced Network)

#### Advanced systems

Some trunked radio protocols provide additional reliability and security.

[NXDN](NXDN.md) Common Air Interface (CAI) was accepted at the meeting of the ITU-R (International Telecommunication Union Radiocommunications Sector) held in November 2016 and it has been added to Report M.2014-3, published in February 2017. It is an open, multi-vendor protocol widely adopted in mission-critical applications in Japan, USA and mainland Europe.

Other protocols include:

- MPT-1327
- [TETRA](TETRA.md)
- APCO Project 25
- TETRAPOL

---

*Source: Wikipedia, Trunked radio system (https://en.wikipedia.org/wiki/Trunked_radio_system), by Wikipedia contributors, CC BY-SA 4.0.*
