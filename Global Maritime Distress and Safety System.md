# Global Maritime Distress and Safety System

The **Global Maritime Distress and Safety System** (**GMDSS**) is a worldwide system for automated emergency signal communication for ships at sea developed by the United Nations' International Maritime Organization (IMO) as part of the SOLAS Convention.

It is a set of safety procedures, types of equipment, and communication protocols used for safety and rescue operations of the distressed ships, boats, and aircraft. It is supplemental to the International Convention on Maritime Search and Rescue (ICMSaR) adopted in 1979 and provides basis for the communication.

GMDSS consists of several systems which are intended to perform the following functions: alerting (including position determination of the ship in distress) ships in the vicinity and ashore authorities, search and rescue coordination, locating (homing), maritime safety information broadcasts, general communications, and bridge-to-bridge communications. Specific radio carriage requirements depend upon the ship's area of operation, rather than its tonnage. The system also provides redundant means of distress alerting, and emergency sources of power.

Recreational vessels do not need to comply with GMDSS radio carriage requirements. Offshore vessels may elect to equip themselves further. Vessels under 300 gross tonnage (GT) are not subject to GMDSS requirements.

### Components of GMDSS

The main types of equipment used in GMDSS are:

#### Emergency position-indicating radio beacon (EPIRB)

Cospas-Sarsat is an international satellite-based search and rescue system, established by Canada, France, the United States, and Russia. These four countries jointly helped develop the 406 MHz Emergency Position-Indicating Radio Beacon (EPIRB), an element of the GMDSS designed to operate with Cospas-Sarsat system. These automatic-activating EPIRBs, now required on SOLAS ships, commercial fishing vessels, and all passenger ships, are designed to transmit to alert rescue coordination centers via the satellite system from anywhere in the world. The original COSPAS/SARSAT system used polar orbiting satellites, but in recent years the system has been expanded to also include 4 geostationary satellites and 50 medium orbiting navigation satellites. Newest designs incorporate GPS receivers to transmit highly accurate positions (within about 20 metres) of the distress position. EPIRB manufacturers offer AIS (Automatic Identification System) enabled beacons. 406 MHz EPIRBs transmit an ID which is linked to a database of information about the vessel. Typically a vessel has a unique ID: MMSI. The serviceability of these items is checked monthly and annually and they have limited battery shelf life, between two and five years using mostly lithium-type batteries.

#### NAVTEX

Navtex is an international, automated system for instantly distributing maritime safety information (MSI) which includes navigational warnings, weather forecasts and weather warnings, search and rescue notices and similar information to ships. A small, low-cost and self-contained "smart" printing [radio receiver](Radio%20receiver.md) is installed on the bridge, or the place from where the ship is navigated, and checks each incoming message to see if it has been received during an earlier transmission, or if it is of a category of no interest to the ship's master. The frequency of transmission of these messages is 518 kHz in English, while 490 kHz is sometime used to broadcast in a local language. The messages are coded with a header code identified by the using single letters of the alphabet to represent broadcasting stations, type of messages, and followed by two figures indicating the serial number of the message. For example: **FA56** where **F** is the ID of the transmitting station, **A** indicates the message category *navigational warning*, and **56** is the consecutive message number.

#### Satellite

As of January 2020, there are two certified providers of GMDSS satellite services: [Inmarsat](Inmarsat.md), with several of their commsats in equatorial geosynchronous orbit, and Iridium Communications, with their [66-satellite constellation](Iridium%20satellite%20constellation.md) in low Earth orbit (LEO) that can cover higher latitudes and operate with lower communications latency. The certification of Iridium in 2020 ended a monopoly on the provision of the satellite-based portion of maritime distress services that had previously been held by Inmarsat since the system became operational in 1999.

Satellite systems operated by the [Inmarsat](Inmarsat.md) company, overseen by the International Mobile Satellite Organization (IMSO) are important elements of the GMDSS. The types of Inmarsat ship earth station terminals recognized by the GMDSS are: Inmarsat C and F77. Inmarsat F77, an updated version of the now redundant Inmarsat A and B, provide ship-to-shore, ship-to-ship and shore-to-ship telephone, telex and high-speed data services, including a distress priority telephone and telex service to and from rescue coordination centers. Fleet 77 fully supports the Global Maritime Distress and Safety System (GMDSS) and includes advanced features such as emergency call prioritisation. Unfortunately Fleet 77 has an end of life scheduled for 1 December 2020.  No definite alternatives are currently defined. The Inmarsat C provides ship/shore, shore/ship and ship/ship store-and-forward data and email messaging, the capability for sending preformatted distress messages to a rescue coordination center, and the Inmarsat C SafetyNET service. The Inmarsat C SafetyNET service is a satellite-based worldwide maritime safety information broadcast service of high seas weather warnings, NAVAREA navigational warnings, radionavigation warnings, ice reports and warnings generated by the USCG-conducted International Ice Patrol, and other similar information not provided by NAVTEX. SafetyNET works similarly to NAVTEX in areas outside NAVTEX coverage.

Inmarsat C equipment is relatively small and lightweight, and costs much less than a F77 station. A F77 ship earth station requires a relatively large gyro-stabilized unidirectional antennas; the antenna size of the Inmarsat C is much smaller and is omnidirectional. Inmarsat C being a low power system allows for its operation from the vessels emergency 24volt battery supply under emergency conditions. This coupled to the omni [directional antenna](Directional%20antenna.md) arrangements allow for a guaranteed response to a distress alert between 76 degrees North and 76 degrees South (Sea area A3).

Under a cooperative agreement with the National Oceanic and Atmospheric Administration (NOAA), combined meteorological observations and AMVER reports can now be sent to both the USCG AMVER Center, and NOAA, using an Inmarsat C ship earth station, at no charge.

SOLAS now requires that Inmarsat C equipment have an integral satellite navigation receiver, or be externally connected to a satellite navigation receiver. That connection will ensure accurate location information to be sent to a rescue coordination center if a distress alert is ever transmitted.

Also, the new LRIT long-range tracking systems are upgraded via GMDSS Inmarsat C, which are also compliant, along with inbuilt SSAS, or ship security alert system. SSAS provides a means to covertly transmit a security alert distress message to local authorities in the event of a mutiny, pirate attack, or other hostile action towards the vessel or its crew.

#### High frequency

A GMDSS system may include high-frequency (HF) radiotelephone and [radiotelex](Radioteletype.md) (narrow-band direct printing) equipment, with calls initiated by digital selective calling (DSC). Worldwide broadcasts of maritime safety information can also be made on HF narrow-band direct printing channels. All ships trading in Sea area A4 must carry HF DSC and NBDP equipment which can also operate from the ships reserve energy supply (typically a 24 Volt battery supply). This HF provision is necessary as the Inmarsat coverage does not extend to the polar regions.

#### Search and rescue transponder (SART)

The GMDSS installation on ships include one (two on vessels over 500 GT) search-and-rescue locating device called Search and Rescue Radar Transponders (SART) which are used to locate survival craft or distressed vessels by creating a series of twelve dots on a rescuing ship's 3 cm radar display. The detection range between these devices and ships, dependent upon the height of the ship's radar mast and the height of the Search and Rescue Locating device, is normally about 15 km (8 nautical miles). Once detected by radar, the Search and Rescue Locating device will produce a visual and aural indication to the persons in distress.

#### Digital selective calling

The IMO also introduced digital selective calling (DSC) on MF, HF and VHF maritime radios as part of the GMDSS system. DSC is primarily intended to initiate ship-to-ship, ship-to-shore and shore-to-ship radiotelephone and MF/HF radiotelex calls. DSC calls can also be made to individual stations, groups of stations, or "all stations" in one's radio range. Each DSC-equipped ship, shore station and group is assigned a unique 9-digit Maritime Mobile Service Identity.

DSC distress alerts, which consist of a preformatted distress message, are used to initiate emergency communications with ships and rescue coordination centers. DSC was intended to eliminate the need for persons on a ship's bridge or on shore to continuously guard radio receivers on voice radio channels, including VHF channel 16 (156.8 MHz) and [2182 kHz](2182%20kHz.md) now used for distress, safety and calling. A listening watch aboard GMDSS-equipped ships on 2182 kHz ended on February 1, 1999. In May 2002, IMO decided to postpone cessation of a VHF listening watch aboard ships. That watchkeeping requirement had been scheduled to end on February 1, 2005.

IMO and ITU both require that the DSC-equipped MF/HF and VHF radios be externally connected to a satellite navigation receiver (GPS). That connection will ensure accurate location information is sent to a rescue coordination center if a distress alert is transmitted. The FCC requires that all new VHF and MF/HF maritime radiotelephones type accepted after June 1999 have at least a basic DSC capability.

VHF digital selective calling also has other capabilities beyond those required for the GMDSS. The US Coast Guard uses this system to track vessels in Prince William Sound, Alaska, Vessel Traffic Service. IMO and the USCG also plan to require ships carry a Universal Shipborne automatic identification system, which will be DSC-compatible. Countries having a GMDSS A1 Area should be able to identify and track AIS-equipped vessels in its waters without any additional radio equipment. A DSC-equipped radio cannot be interrogated and tracked unless that option was included by the manufacturer, and unless the user configures it to allow tracking.

GMDSS telecommunications equipment should not be reserved for emergency use only. The International Maritime Organization encourages mariners to use GMDSS equipment for routine as well as safety telecommunications.

#### Power supply requirements

GMDSS equipment is required to be powered from three sources of supply:

- ship's normal alternators/generators;
- ship's emergency alternator/generator (if fitted); and
- a dedicated radio battery supply.

The batteries are required to have a capacity to power the equipment for 1 hour on ships with an emergency generator or built prior to February 1995, and 6 hours on ships not fitted with an emergency generator or built after February 1995 in order to comply with SOLAS. The batteries must be charged by an automatic charger, which is also required to be powered from the main and emergency generators. Changeover from AC to battery supply must be automatic, and effected in such a way that any data held by the equipment is not corrupted ("no break").

During Coast Guard inspections, the batteries must be able to go from 100% discharge to fully charged in no longer than 10 hours in order to pass certification. The charger too must be obtainable at all times during vessel operation and should be inspected to make sure it functions properly. When the reserve source of energy consists of batteries, the battery capacity must be checked at intervals not exceeding 12 months. If not completed within past 12 months, this must be done during inspection.

Storage batteries provided as a reserve source of energy must be installed in accordance with applicable electrical codes and good engineering practice. They must be protected from adverse weather and physical damage. They must be readily accessible for maintenance and replacement.

### GMDSS sea areas

GMDSS sea areas serve two purposes: to describe areas where GMDSS services are available, and to define what radio equipment GMDSS ships must carry (carriage requirements). Prior to the GMDSS, the number and type of radio safety equipment ships had to carry depended upon its tonnage. With GMDSS, the number and type of radio safety equipment ships have to carry depends upon the GMDSS areas in which they travel. GMDSS sea areas are classified into the following four areas: A1, A2, A3 and A4. In 2024 the definitions of A3 and A4 were updated to account for the global coverage now provided by Iridium.

- Sea Area A1—An area within the radiotelephone coverage of at least one VHF coast station in which continuous digital selective calling (Ch.70/156.525 MHz) alerting and radiotelephony services are available. Such an area could extend typically 30 to 40 nautical miles (56 to 74 km) from the Coast Station.
- Sea area A2—An area within a coverage of at least one coast station continuous listening on MF (2187.5 kHz) other than Area A1
- Sea Area A3—An area, excluding sea areas A1 and A2, within the coverage of an RMSS (Recognised Mobile Satellite System). For ships fitted with Inmarsat geostationary satellite, this area lies between about latitude 76 Degrees North and South, but excludes A1 and/or A2 designated areas. Inmarsat guarantees their system will work between 70 South and 70 North though it will often work to 76 degrees South or North. For vessels fitted with Iridium A3, it also includes the polar regions.
- Sea Area A4—An area outside Sea Areas A1, A2 and A3 is called Sea Area A4. For ships fitted with Inmarsat as their RMSS this is essentially the polar regions, north and south of about 76 degrees of latitude, excluding any A1, A2 and A3 areas. For ships that carry Iridium as their RMSS, there is no Area A4.

In addition to the equipment listed, all GMDSS-regulated ships must carry a satellite EPIRB, a NAVTEX receiver (if they travel in any areas served by NAVTEX), an Inmarsat-C SafetyNET receiver (if they travel in any areas not served by NAVTEX), a DSC-equipped VHF radiotelephone, two (if between 300 and less than 500 GRT) or three VHF handhelds (if 500 GRT or more), and two 9 GHz search and rescue radar transponders (SART).

#### GMDSS radio equipment required for U.S. coastal voyages

At present, until an A1 or A2 Sea Area is established, GMDSS-mandated ships operating off the U.S. coast must fit to Sea Areas A3 (or A4) regardless of where they operate. U.S. ships whose voyage allows them to always remain within VHF channel 16 coverage of U.S. Coast Guard stations may apply to the Federal Communications Commission for an individual waiver to fit to Sea Area A1 requirements. Similarly, those who remain within 2182 kHz coverage of U.S. Coast Guard stations may apply for a waiver to fit to Sea Area A2 requirements.

As of August 2013, the U.S. Coast Guard provides a Sea Area A1 service through its Rescue 21 system.

### Licensing of operators (USA)

National maritime authorities may issue various classes of licenses. The General Operator’s Certificate is required on SOLAS vessels operating also outside GMDSS Sea Area A1, while a Restricted Operator’s Certificate is needed on SOLAS vessels operated solely within GMDSS Sea Area A1,

Long Range Certificate may be issued, and is required on non-SOLAS vessels operating outside GMDSS Sea Area A1, while a Short Range Certificate is issued for non-SOLAS vessels operating only inside GMDSS Sea Area A1.

Finally there is a restricted radiotelephone operator's certificate, which is similar to the Short Range Certificate but limited VHF DSC radio operation. Some countries do not consider this adequate for GMDSS qualification.

In the United States four different GMDSS certificates are issued:

- A GMDSS Radio Maintainer's License allows a person to maintain, install, and repair GMDSS equipment at sea.
- A GMDSS Radio Operator's License is necessary for a person to use required GMDSS equipment.
- The holder of both certificates can be issued one GMDSS Radio Operator/Maintainer License.
- Finally, the **GMDSS Restricted License** is available for VHF operations only within 20 nautical miles (37 km) of the coast.

To obtain any of these licenses a person must be a U.S. citizen or otherwise eligible for work in the country, be able to communicate in English, and take written examinations approved by the Federal Communications Commission. Like the [amateur radio](Amateur%20radio.md) examinations, these are given by private, FCC-approved groups. These are generally not the same agencies who administer the ham tests. Written test elements 1 and 7 are required for the Operator license, and elements 1 and 7R for the Restricted Operator. (Passing element 1 also automatically qualifies the applicant for the Marine Radiotelephone Operator Permit, the MROP.)

For the Maintainer license, written exam element 9 must be passed. However, to obtain this certificate an applicant must also hold a General radiotelephone operator license (GROL), which requires passing commercial written exam elements 1 and 3 (and thus supersedes the MROP). Upon the further passing of optional written exam element 8 the ship radar endorsement will be added to both the GROL and Maintainer licenses. This allows the holder to adjust, maintain, and repair shipboard radar equipment.

Until March 25, 2008 GMDSS operator and maintainer licenses expired after five years but could be renewed upon payment of a fee. On that date all new certificates were issued valid for the lifetimes of their holders. For those still valid but previously issued with expiration dates, the FCC states:

Any GMDSS Radio Operator's License, Restricted GMDSS Radio Operator's License, GMDSS Radio Maintainer's License, GMDSS Radio Operator/Maintainer License, or Marine Radio Operator Permit that was active, i.e., had not expired, as of March 25, 2008, does not have to be renewed.

Since an older certificate does show an expiration date, for crewmembers sailing internationally it may be worth paying the fee (as of 2010 it was $60) to avoid any confusion with local authorities.

Finally, to actually serve as a GMDSS operator on most commercial vessels the United States Coast Guard requires additional classroom training and practical experience beyond just holding a license.

### Licensing of operators (UK and Europe)

In the United Kingdom and Europe four different GMDSS certificates of Competence are issued:

- Short Range Certificate (SRC)
- Long Range Certificate (LRC)
- Restricted Operator Certificate (ROC)
- General Operator Certificate (GOC)

Each certificate is issued on the successful completion of a course and exam and each certificate is recognised internationally.

Which Certificate of Competence a seafarer requires will depend on two factors. Firstly, officers on board SOLAS vessels (GMDSS compulsory fit vessels) require the ROC or GOC. Operators onboard non SOLAS vessels (which includes leisure craft) may take the shorter Short Range Certificate or Long Range Certificate Courses.

The second deciding factor is the intended operating area of the vessel. Craft operating exclusively in Sea Area A1 can use the SRC or ROC certificates, where as vessels venturing further offshore into Sea Areas A2, A3 and/or A4 require the LRC or GOC.

---

*Source: Wikipedia, Global Maritime Distress and Safety System (https://en.wikipedia.org/wiki/Global_Maritime_Distress_and_Safety_System), by Wikipedia contributors, CC BY-SA 4.0.*
