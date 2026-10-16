# Iridium satellite constellation

Iridium

Replica of a first-generation Iridium satellite

- Manufacturer Motorola (original constellation), Thales Alenia Space (NEXT constellation)
- Country of origin United States
- Operator Iridium Communications
- Applications communications
- Specifications
- Bus LM-700 (original), EliteBus1000 (NEXT)
- Launch mass 689 kilograms (1,519 lb)
- Power 2 deployable solar panels + batteries
- Regime Low Earth orbit
- Production
- Status In service
- Built 98 (original), 81 (NEXT)
- Launched 95 (original), 80 (NEXT)
- Operational 82 (76 in active service, 6 spares)
- Maiden launch Iridium 4, 5, 6, 7, 8 on 5 May 1997

The **Iridium satellite constellation** provides L band voice and data information coverage to [satellite phones](Satellite%20phone.md), satellite messenger communication devices and integrated transceivers. Iridium Communications owns and operates the constellation, additionally selling equipment and access to its services. It was conceived by Bary Bertiger, Raymond J. Leopold and Ken Peterson in late 1987 (in 1988 protected by patents Motorola filed in their names) and then developed by Motorola on a fixed-price contract from July 29, 1993, to November 1, 1998, when the system became operational and commercially available.

The constellation consists of 66 active satellites in orbit, required for global coverage, and additional spare satellites to serve in case of failure. Satellites are placed in low Earth orbit at a height of approximately 781 kilometres (485 mi) and inclination of 86.4°. The nearly polar orbit and communication between satellites via Ka band inter-satellite links provide global service availability (including both poles, oceans and airways), regardless of the position of ground stations and gateways.

In 1999, *The New York Times* quoted a wireless market analyst, regarding people having "one number that they could carry with them anywhere" as "expensive... There never was a viable market."

Due to the shape of the original Iridium satellites' reflective antennas, the first generation satellites focused sunlight on a small area of the Earth surface in an incidental manner. This resulted in a phenomenon called Iridium flares, whereby the satellite momentarily appeared as one of the brightest objects in the night sky and could be seen even during daylight. Newer Iridium satellites do not produce flares.

### Overview

The Iridium system was designed to be accessed by small handheld phones, the size of a cell phone. While "the weight of a typical cell phone in the early 1990s was 10.5 ounces" (300 grams) *Advertising Age* wrote in mid 1999 that "when its phone debuted, weighing 1 pound (454 g) and costing $3,000, it was viewed as both unwieldly and expensive."

An [omnidirectional antenna](Omnidirectional%20antenna.md) was intended to be small enough to be mounted on the planned phone, but the low handset battery power was insufficient for contact with a satellite in geostationary orbit, 35,785 km (22,236 mi) above the Earth; the normal orbit of communications satellites, in which the satellite appears stationary in the sky. In order for a handheld phone to communicate with them, the Iridium satellites are closer to the Earth, in low Earth orbit, about 781 km (485 mi) above the surface. With an orbital period of about 100 minutes a satellite can only be in view of a phone for about 7 minutes, so the call is automatically "handed off" to another satellite when one passes beyond the local horizon. This requires multiple satellites, carefully spaced out in polar orbits (see animated image of coverage) to ensure that at least one satellite is continually in view from every point on the Earth's surface. At least 66 satellites are required, in 6 polar orbits containing 11 satellites each, for seamless coverage.

#### Orbit

Orbital velocity of the satellites is approximately 27,000 km/h (17,000 mph). Satellites communicate with neighboring satellites via Ka band inter-satellite links. Each satellite can have four inter-satellite links: one each to neighbors fore and aft in the same orbital plane, and one each to satellites in neighboring planes to either side. The satellites orbit from pole to same pole with an orbital period of roughly 100 minutes. This design means that there is excellent satellite visibility and service coverage especially at the North and South poles. The over-the-pole orbital design produces "seams" where satellites in counter-rotating planes next to one another are traveling in opposite directions. Cross-seam inter-satellite link hand-offs would have to happen very rapidly and cope with large Doppler shifts; therefore, Iridium supports inter-satellite links only between satellites orbiting in the same direction. The constellation of 66 active satellites has six orbital planes spaced 30° apart, with 11 satellites in each plane (not counting spares). The original concept was to have 77 satellites, which is where the name *Iridium* came from; the element iridium has the atomic number 77, and the satellites evoked the Bohr model image of electrons orbiting around the Earth as its nucleus. This reduced set of six planes is sufficient to cover the entire Earth surface at every moment.

### Original Iridium constellation

The satellites each contained seven Motorola/Freescale PowerPC 603E processors running at roughly 200 MHz, connected by a custom backplane network. One processor was dedicated to each cross-link antenna ("HVARC"), and two processors ("SVARC"s) were dedicated to satellite control, one being a spare. Late in the project an extra processor ("SAC") was added to perform resource management and phone call processing.

The cellular look down antenna had 48 spot beams arranged as 16 beams in three sectors. The four inter-satellite cross links on each satellite operated at 10 Mbit/s. Optical links could have supported a much greater bandwidth and a more aggressive growth path, but microwave cross links were chosen because their bandwidth was more than sufficient for the desired system. Nevertheless, a parallel optical cross link option was carried through a critical design review, and ended when the microwave cross links were shown to support the size, weight and power requirements allocated within the individual satellite's budget. Iridium Satellite LLC stated that their second generation satellites would also use microwave, not optical, inter-satellite communications links. Iridium's cross-links are unique in the satellite telephone industry as other providers do not relay data between satellites; Globalstar and [Inmarsat](Inmarsat.md) both use a transponder without cross-links.

The original design as envisioned in the 1960s was that of a completely static "dumb satellite" with a set of control messages and time-triggers for an entire orbit that would be uploaded as the satellite passed over the poles. It was found that this design did not have enough bandwidth in the space-based backhaul to upload each satellite quickly and reliably over the poles. Moreover, fixed, static scheduling would have left more than 90% of the satellite links idle at all times. Therefore, the design was scrapped in favour of a design that performed dynamic control of routing and channel selection late in the project, resulting in a one-year delay in system delivery.

Each satellite can support up to 1,100 concurrent phone calls at 2,400 bit/s and weighs about 680 kilograms (1,500 lb). The Iridium System presently operates within a dedicated band segment from 1,618.725 to 1,626.5 MHz and shares with Globalstar a band segment from 1,617.775 to 1,618.725 MHz. These segments are part of the wider L band, adjacent to the Radio Astronomy Service (RAS) band segment from 1,610.6 to 1,613.8 MHz.

The configuration of the Satellite concept was designated as Triangular Fixed, 80 Inch Main Mission Antenna, Light-weight (TF80L). The packaging design of the spacecraft was managed by Lockheed Bus Spacecraft team; it was the first commercial satellite bus designed at the Sunnyvale Space Systems Division in California. The TF80L configuration was considered a non-conventional, innovative approach to developing a satellite design that could be assembled and tested in five days. The TF80L design configuration was also instrumental in simultaneously solving fundamental design problems involving optimization of the communications payload thermal environment and RF main mission antenna performance, while achieving the highest payload fairing packaging for each of the three main launch vehicle providers.

The first spacecraft mock-up of this design was built in the garage workshop in Santa Clara, California for the Bus PDR/CDR as a proof-of-concept model. This first prototype paved the way for the design and construction of the first engineering models. This design was the basis of the largest constellation of satellites deployed in low Earth orbit. After ten years of successful on-orbit performance, the Iridium team celebrated the equivalent of 1,000 cumulative years of on-orbit performance in 2008. One of the engineering Iridium satellite models was placed on permanent exhibit in the National Air and Space Museum in Washington, D.C.

#### Launch campaign

95 of the 99 built satellites were launched between 1997 and 2002. Four satellites were kept on the ground as spares.

The 95 satellites were launched over twenty-two missions (nine missions in 1997, ten in 1998, one in 1999 and two in 2002). One extra mission on Chang Zheng was a payload test and did not carry any actual satellites.

- Launch date   Launch site   Launch vehicle   Satellite number (at launch)
- 1997-05-05   Vandenberg   Delta II 7920-10C   4, 5, 6, 7, 8
- 1997-06-18   Baikonur   Proton-K/17S40   9, 10, 11, 12, 13, 14, 16
- 1997-07-09   Vandenberg   Delta II 7920-10C   15, 17, 18, 20, 21
- 1997-08-21   Vandenberg   Delta II 7920-10C   22, 23, 24, 25, 26
- 1997-09-01   Taiyuan   Chang Zheng 2C-III/SD   *Iridium payload test / no satellite*
- 1997-09-14   Baikonur   Proton-K/17S40   27, 28, 29, 30, 31, 32, 33
- 1997-09-27   Vandenberg   Delta II 7920-10C   19, 34, 35, 36, 37
- 1997-11-09   Vandenberg   Delta II 7920-10C   38, 39, 40, 41, 43
- 1997-12-08   Taiyuan   Chang Zheng 2C-III/SD   42, 44
- 1997-12-20   Vandenberg   Delta II 7920-10C   45, 46, 47, 48, 49
- 1998-02-18   Vandenberg   Delta II 7920-10C   50, 52, 53, 54, 56
- 1998-03-25   Taiyuan   Chang Zheng 2C-III/SD   51, 61
- 1998-03-30   Vandenberg   Delta II 7920-10C   55, 57, 58, 59, 60
- 1998-04-07   Baikonur   Proton-K/17S40   62, 63, 64, 65, 66, 67, 68
- 1998-05-02   Taiyuan   Chang Zheng 2C-III/SD   69, 71
- 1998-05-17   Vandenberg   Delta II 7920-10C   70, 72, 73, 74, 75
- 1998-08-19   Taiyuan   Chang Zheng 2C-III/SD   3, 76
- 1998-09-08   Vandenberg   Delta II 7920-10C   77, 79, 80, 81, 82
- 1998-11-06   Vandenberg   Delta II 7920-10C   2, 83, 84, 85, 86
- 1998-12-19   Taiyuan   Chang Zheng 2C-III/SD   11a, 20a
- 1999-06-11   Taiyuan   Chang Zheng 2C-III/SD   14a, 21a
- 2002-02-11   Vandenberg   Delta II 7920-10C   90, 91, 94, 95, 96
- 2002-06-20   Plesetsk   Rokot/Briz-KM   97, 98

**^** Iridium satellite number changed over time following failure and replacement.

#### In-orbit spares

Spare satellites are usually held in a 666 kilometres (414 mi) storage orbit. These can be boosted to the correct altitude and put into service in case of a satellite failure. After the Iridium company emerged from bankruptcy the new owners decided to launch seven new spares, which would have ensured two spare satellites were available in each plane. As of 2009, not every plane had a spare satellite; however, the satellites can be moved to a different plane if required. A move can take several weeks and consumes fuel which will shorten the satellite's expected service life.

Significant orbital inclination changes are normally very fuel-intensive, but orbital perturbation analysis aids the process. The Earth's equatorial bulge causes the orbital right ascension of the ascending node (RAAN) to precess at a rate that depends mainly on the period and inclination.

A spare Iridium satellite in the lower storage orbit has a shorter period so its RAAN moves westward more quickly than the satellites in the standard orbit. Iridium simply waits until the desired RAAN (i.e., the desired orbital plane) is reached and then raises the spare satellite to the standard altitude, fixing its orbital plane with respect to the constellation. Although this saves substantial amounts of fuel, it can be a time-consuming process.

During 2016, Iridium experienced in-orbit failures which could not be corrected with in-orbit spare satellites, thus only 64 of the 66 satellites required for seamless global coverage were in operation. This caused some service interruptions until the next-generation constellation was put into service.

### Next-generation constellation

In 2017, Iridium began launching Iridium NEXT, a second-generation worldwide network of telecommunications satellites, consisting of 66 active satellites, with another nine in-orbit spares and six on-ground spares. These satellites incorporate features such as data transmission that were not emphasized in the original design. The next-generation terminals and service became commercially available in 2018. One of the Iridium NEXT services is Iridium Certus, a globally available satellite broadband, which is capable of up to 704 kbit/s of bandwidth across maritime, aviation, land mobile, government, and IoT applications.

The NEXT satellites incorporate a secondary payload for Aireon, a space-qualified ADS-B receiver for use by air traffic control and, via FlightAware, by airlines. A tertiary payload on 58 satellites is a marine AIS ship-tracker receiver for Canadian company ExactEarth Ltd.

In January 2020, the Iridium constellation was certified for use in the [Global Maritime Distress and Safety System](Global%20Maritime%20Distress%20and%20Safety%20System.md) (GMDSS). The certification ended a monopoly on the provision of maritime distress services that had previously been held by [Inmarsat](Inmarsat.md) since the system became operational in 1999.

Iridium NEXT also provides data link to other satellites in space, enabling command and control of other space assets regardless of the position of ground stations and gateways.

#### Launch campaign

In June 2010, Iridium signed the largest commercial rocket-launch deal ever at that time, a US$492 million contract with SpaceX to launch 70 Iridium NEXT satellites on seven Falcon 9 rockets from 2015 to 2017 via a SpaceX leased launch facility at Vandenberg Space Force Base. The final two satellites were originally slated to be orbited by a single launch of an ISC Kosmotras Dnepr. Technical issues and consequential demands from Iridium's insurance delayed the launch of the first pair of Iridium NEXT satellites until April 2016.

Iridium NEXT launch plans originally included launch of satellites on both Ukrainian Dnepr launch vehicles and SpaceX Falcon 9 launch vehicles, with the initial satellites launching on Dnepr in April 2016; however, in February 2016, Iridium announced a change. Due to an extended slowdown in obtaining the requisite launch licenses from Russian authorities, Iridium revamped the entire launch sequence for the 75-satellite constellation. It launched and successfully deployed 10 satellites with SpaceX on January 14, 2017, delayed due to weather from January 9, 2017, and the first of those new satellites took over the duties of an old satellite on March 11, 2017.

At the time of the launch of the first batch, the second flight of ten satellites was planned to launch only three months later in April 2017. However, in a February 15 statement, Iridium said that SpaceX pushed back the launch of its second batch of Iridium NEXT satellites from mid-April to mid-June 2017. This second launch, which occurred on June 25, 2017, delivered another ten Iridium NEXT satellites to low Earth orbit (LEO) on a SpaceX Falcon 9 rocket. A third launch, which occurred on October 9, 2017, delivered another ten satellites to LEO, as planned. The Iridium NEXT IV mission launched with ten satellites on December 23, 2017. The fifth mission, Iridium NEXT V, launched with ten satellites on March 30, 2018. The sixth launch on May 22, 2018, sent another 5 satellites into LEO. The penultimate Iridium NEXT launch occurred on July 25, 2018, launching another 10 Iridium NEXT satellites. The final ten NEXT satellites launched on January 11, 2019. Of the six additional spare satellites five have been launched on 20 May 2023 while the last one, Iridium 101, is still on the ground.

- Launch date   Launch site   Launch vehicle   Satellite numbers (at launch)
- 2017-01-14   Vandenberg   Falcon 9 FT   102, 103, 104, 105, 106, 108, 109, 111, 112, 114
- 2017-06-25   Vandenberg   Falcon 9 FT   113, 115, 117, 118, 120, 121, 123, 124, 126, 128
- 2017-10-09   Vandenberg   Falcon 9 B4   100, 107, 119, 122, 125, 129, 132, 133, 136, 139
- 2017-12-23   Vandenberg   Falcon 9 FT   116, 130, 131, 134, 135, 137, 138, 141, 151, 153
- 2018-03-30   Vandenberg   Falcon 9 B4   140, 142, 143, 144, 145, 146, 148, 149, 150, 157
- 2018-05-22   Vandenberg   Falcon 9 B4   110, 147, 152, 161, 162
- 2018-07-25   Vandenberg   Falcon 9 B5   154, 155, 156, 158, 159, 160, 163, 164, 165, 166
- 2019-01-11   Vandenberg   Falcon 9 B5   167, 168, 169, 170, 171, 172, 173, 175, 176, 180
- 2023-05-20   Vandenberg   Falcon 9 B5   174, 177, 178, 179, 181

**^** Iridium satellite number could change over time following failure and replacement.

Iridium 127 had to be re-designated as Iridium 100 before launch due to a ground software issue.

### Defunct satellites

Over the years a number of Iridium satellites have ceased to work and are no longer in active service, some are partially functional and have remained in orbit whereas others have tumbled out of control or have reentered the atmosphere.

Iridium 21, 27, 20, 11, 46, 71, 44, 14, 79, 69 and 85 all suffered from issues before entering operational service soon after their launch. By 2018, of these eleven, Iridium 27, 79 and 85 have decayed out of orbit; Iridium 11, 14, 20 and 21 were renamed to Iridium 911, 914, 920 and 921 respectively since replacements of the same name were launched.

From 2017, several first-generation Iridium satellites have been deliberately de-orbited after being replaced by operational Iridium NEXT satellites.

As of January 2023, a total of 80 previously operating satellites are now defunct or no longer exist.

- List of defunct Iridium satellites previously in operating service
- Satellite   Date   Replacement   Status
- **Iridium 73**   Nov/Dec 1998   Iridium 75   Uncontrolled orbit
- **Iridium 48**   Nov/Dec 1998   Iridium 20a   Decayed 5 May 2001
- **Iridium 2**   Nov/Dec 1998   ?   Decayed 30 June 2024
- **Iridium 9**   October 2000   Iridium 84   Decayed 11 March 2003
- **Iridium 38**   September 2003   Iridium 82   Uncontrolled orbit
- **Iridium 16**   April 2005   Iridium 86   Uncontrolled orbit
- **Iridium 17**   August 2005   Iridium 77   Uncontrolled orbit
- **Iridium 74**   January 2006   Iridium 21a   Deorbited 11 June 2017
- **Iridium 36**   January 2007   Iridium 97   Uncontrolled orbit
- **Iridium 28**   July 2008   Iridium 95   In orbit
- **Iridium 33**   10 February 2009   Iridium 91   Destroyed in collision with Kosmos 2251. Some fragments remain in orbit, while some have decayed.
- **Iridium 26**   August 2011   Iridium 11a   In orbit
- **Iridium 4**   2012   Iridium 96   In orbit
- **Iridium 29**   Early 2014   Iridium 45   In orbit
- **Iridium 42**   August 2014   Iridium 98   Uncontrolled orbit
- **Iridium 63**   August 2014   Iridium 14a   In orbit
- **Iridium 6**   October 2014   Iridium 51   Decayed 23 December 2017
- **Iridium 57**   May 2016   Iridium 121   Observed drifting from nominal position
- **Iridium 39**   June 2016   Iridium 15   In orbit
- **Iridium 7**   2017   Iridium 51   Failed in orbit
- **Iridium 22**   2017   ?   Failed in orbit
- **Iridium 77**   August 2017   Iridium 109   Decayed 22 September 2017
- **Iridium 30**   August 2017   Iridium 126   Decayed 28 September 2017
- **Iridium 8**   November 2017   Iridium 133   Decayed 24 November 2017
- **Iridium 34**   December 2017   Iridium 122   Decayed 8 January 2018
- **Iridium 3**   ?   Iridium 131   Decayed 8 February 2018
- **Iridium 43**   ?   Iridium 111   Decayed 11 February 2018
- **Iridium 49**   ?   ?   Decayed 13 February 2018
- **Iridium 23**   ?   ?   Decayed 28 March 2018
- **Iridium 94**   ?   ?   Decayed 18 April 2018
- **Iridium 19**   ?   ?   Decayed 19 April 2018
- **Iridium 13**   ?   ?   Decayed 29 April 2018
- **Iridium 25**   ?   ?   Decayed 14 May 2018
- **Iridium 72**   ?   ?   Decayed 14 May 2018
- **Iridium 21a**   ?   ?   Decayed 24 May 2018
- **Iridium 37**   ?   ?   Decayed 26 May 2018
- **Iridium 68**   ?   ?   Decayed 6 June 2018
- **Iridium 67**   ?   ?   Decayed 2 July 2018
- **Iridium 75**   ?   ?   Decayed 10 July 2018
- **Iridium 81**   ?   ?   Decayed 17 July 2018
- **Iridium 65**   ?   ?   Decayed 19 July 2018
- **Iridium 41**   ?   ?   Decayed 28 July 2018
- **Iridium 80**   ?   ?   Decayed 12 August 2018
- **Iridium 18**   ?   ?   Decayed 19 August 2018
- **Iridium 66**   ?   ?   Decayed 23 August 2018
- **Iridium 98**   ?   ?   Decayed 24 August 2018
- **Iridium 76**   ?   ?   Decayed 28 August 2018
- **Iridium 47**   ?   ?   Decayed 1 September 2018
- **Iridium 12**   ?   ?   Decayed 2 September 2018
- **Iridium 50**   ?   ?   Decayed 23 September 2018
- **Iridium 40**   ?   ?   Decayed 23 September 2018
- **Iridium 53**   ?   ?   Decayed 30 September 2018
- **Iridium 86**   ?   ?   Decayed 5 October 2018
- **Iridium 10**   ?   ?   Decayed 6 October 2018
- **Iridium 70**   ?   ?   Decayed 11 October 2018
- **Iridium 56**   ?   ?   Decayed 11 October 2018
- **Iridium 15**   ?   ?   Decayed 14 October 2018 (Over No. Pacific)
- **Iridium 20a**   ?   ?   Decayed 22 October 2018
- **Iridium 11a**   ?   ?   Decayed 22 October 2018
- **Iridium 84**   ?   ?   Decayed 4 November 2018
- **Iridium 83**   ?   ?   Decayed 5 November 2018
- **Iridium 52**   ?   ?   Decayed 5 November 2018
- **Iridium 62**   ?   ?   Decayed 7 November 2018
- **Iridium 31**   ?   ?   Decayed 20 December 2018
- **Iridium 35**   ?   ?   Decayed 26 December 2018
- **Iridium 90**   ?   ?   Decayed 23 January 2019
- **Iridium 32**   ?   ?   Decayed 10 March 2019
- **Iridium 59**   ?   ?   Decayed 11 March 2019
- **Iridium 91**   ?   ?   Decayed 13 March 2019
- **Iridium 14a**   ?   ?   Decayed 15 March 2019
- **Iridium 60**   ?   ?   Decayed 17 March 2019
- **Iridium 95**   ?   ?   Decayed 25 March 2019
- **Iridium 55**   ?   ?   Decayed 31 March 2019
- **Iridium 64**   ?   ?   Decayed 1 April 2019
- **Iridium 58**   ?   ?   Decayed 7 April 2019
- **Iridium 24**   ?   ?   In orbit
- **Iridium 54**   ?   ?   Decayed 11 May 2019
- **Iridium 61**   ?   ?   Decayed 23 July 2019
- **Iridium 97**   ?   ?   Decayed 27 December 2019
- **Iridium 96**   ?   ?   Decayed 30 May 2020
- Total: 80

#### Iridium 33 collision

At 16:56 UTC on February 10, 2009, Iridium 33 collided with the defunct Russian satellite Kosmos 2251. This accidental collision was the first hypervelocity collision between two artificial satellites in low Earth orbit. Iridium 33 was in active service when the accident took place. It was one of the oldest satellites in the constellation, having been launched in 1997. The satellites collided at a relative speed of roughly 35,000 km/h (22,000 miles per hour) This collision created over 2000 large space debris fragments that could be hazardous to other satellites.

Iridium moved one of its in-orbit spares, Iridium 91 (formerly known as Iridium 90), to replace the destroyed satellite, completing the move on March 4, 2009.

### Technical details

#### Air interface

Communication between satellites and handsets is done using a TDMA and FDMA based system using L-band spectrum between 1,616 and 1,626.5 MHz. Iridium exclusively controls 7.775 MHz of this and shares a further 0.95 MHz. In 1999, Iridium agreed to timeshare a portion of spectrum, allowing radio astronomers to observe hydroxyl emissions. in 2010, the amount of shared spectrum was reduced from 2.625 MHz.

External "hockey puck" type antennas used with Iridium handheld phones, data modems and SBD terminals are usually defined as 3 [dB](Decibel.md) gain, 50 ohms impedance with RHCP (right hand circular polarization) and 1.5:1 VSWR. As Iridium antennas function at frequencies very close to those of GPS, a single antenna may be utilized through a pass-through for both Iridium and GPS reception.

The type of modulation used is normally DE-QPSK, although DE-BPSK is used on the uplink (mobile to satellite) for acquisition and synchronization. Each time slot is 8.28 milliseconds long and sits in a 90 milliseconds frame. Within each FDMA channel there are four TDMA time slots in each direction. The TDMA frame starts off with a 20.32 milliseconds period used for simplex messaging to devices such as pagers and to alert Iridium phones of an incoming call, followed by the four upstream slots and four downstream slots. This technique is known as time-division multiplexing. Small guard periods are used between time slots. Regardless of the modulation method being used, communication between mobile units and satellites is performed at 25 kilobaud.

Channels are spaced at 41.666 kHz and each channel occupies a bandwidth of 31.5 kHz; this allows space for Doppler shifts.

#### Handoff

The Iridium system uses three different handoff types. As a satellite travels over the ground location, calls are handed to adjacent spot-beams; this occurs approximately every fifty seconds. A satellite only stays in view for seven minutes at the equator. When the satellite disappears from view, an attempt is made to hand the call to another satellite. If no other satellite is in view, the connection is dropped. This may occur when the signal from either satellite is blocked by an obstacle. When successful, the inter-satellite handoff may be noticeable by a quarter-second interruption.

The satellites are also able to transfer mobile units to different channels and time slots within the same spot beam.

#### Ground stations

Iridium routes phone calls through space. In addition to communicating with the satellite phones in its footprint, each satellite in the constellation also maintains contact with two to four adjacent satellites, and routes data between them, to effectively create a large mesh network. There are several ground stations which link to the network through the satellites visible to them. The space-based backhaul routes outgoing phone call packets through space to one of the ground station downlinks ("feeder links"). Iridium ground stations interconnect the satellite network with land-based fixed or wireless infrastructures worldwide to improve availability. Station-to-station calls from one satellite phone to another can be routed directly through space without going through a ground station. As satellites leave the area of a ground station, the routing tables are updated and packets headed for the ground station are forwarded to the next satellite just coming into view of the ground station. Communication between satellites and ground stations is at 20 and 30 GHz.

Gateways are located in

- Tempe, Arizona (USA)
- Fairbanks, Alaska (USA)
- Svalbard, Norway (Europe)
- Izhevsk, Russia
- Punta Arenas, Chile (South America)

The pre-bankruptcy corporate incarnation of Iridium built eleven gateways, most of which have since been closed.

#### Adoption of standard-based solutions for cellphones

In 2024, Iridium introduced Project Stardust, a 3GPP standard-based satellite-to-cellphone service focusing on messaging, emergency communications and IoT for devices like cars, smartphones, tablets and related consumer applications. The solution will be supported using a version of the NB-IoT standard for 5G non-terrestrial networks (NTN). Scheduled for launch in 2026, it won't replace the company's proprietary solution for voice and high-speed data; instead it will co-exist with that offering on the Iridium's existing global low-earth orbit satellite network.

---

*Source: Wikipedia, Iridium satellite constellation (https://en.wikipedia.org/wiki/Iridium_satellite_constellation), by Wikipedia contributors, CC BY-SA 4.0.*
