# What is a fixed digital message forwarding system?

*Tags: digital-modes, jargon, band-plan · score 10*

## Question

What is a fixed digital message forwarding system? I noticed this on the lower end of the 222MHz allocation in the US but it's not explained on the band chart:

## Answer (score 8, by Phil Frost - W8II)

That's a lot of words for digipeater. These are stations that listen for digital messages, record them in temporary storage, then re-transmit them. This particular allocation is on a secondary basis, with the primary allocation going to AMTS.

"message forwarding system" is defined in §97.3:

(32) Message forwarding system. A group of amateur stations participating in a voluntary, cooperative, interactive arrangement where communications are sent from the control operator of an originating station to the control operator of one or more destination stations by one or more forwarding stations.

A "fixed station" isn't defined in §97 anywhere that I can find, but Merriam-Webster provides a definition:

a permanently located radio transmitting station used for communicating with similar stations

"Digital" in practice probably means 1200 baud AFSK AX.25. However, there's no clear definition I can find, so if you wanted to stray outside this (for example, what about digital voice?) you probably end up in a grey area. Definitions might include various mentions of "digital" in the emissions designators in Title 47 §2.201. Or, "digital" might mean the definition of "data" again from §97.3:

(2) Data. Telemetry, telecommand and computer communications emissions having (i) designators with A, C, D, F, G, H, J or R as the first symbol, 1 as the second symbol, and D as the third symbol; (ii) emission J2D; and (iii) emissions A1C, F1C, F2C, J2C, and J3C having an occupied bandwidth of 500 Hz or less when transmitted on an amateur service frequency below 30 MHz. Only a digital code of a type specifically authorized in this part may be transmitted.

The specific FCC regulations for 219-220 MHz are §97.303 (l):

(l) In the 219-220 MHz segment:

(1) Use is restricted to amateur stations participating as forwarding stations in fixed point-to-point digital message forwarding systems, including intercity packet backbone networks. It is not available for other purposes.

(2) Amateur stations must not cause harmful interference to, and must accept interference from, stations authorized by:

(i) The FCC in the Automated Maritime Telecommunications System (AMTS), the 218-219 MHz Service, and the 220 MHz Service, and television stations broadcasting on channels 11 and 13; and

(ii) Other nations in the fixed and maritime mobile services.

(3) No amateur station may transmit unless the licensee has given written notification of the station's specific geographic location for such transmissions in order to be incorporated into a database that has been made available to the public. The notification must be given at least 30 days prior to making such transmissions. The notification must be given to: The American Radio Relay League, Inc., 225 Main Street, Newington, CT 06111-1494.

(4) No amateur station may transmit from a location that is within 640 km of an AMTS coast station that operates in the 217-218 MHz and 219-220 MHz bands unless the amateur station licensee has given written notification of the station's specific geographic location for such transmissions to the AMTS licensee. The notification must be given at least 30 days prior to making such transmissions. The location of AMTS coast stations using the 217-218/219-220 MHz channels may be obtained as noted in paragraph (l)(3) of this section.

(5) No amateur station may transmit from a location that is within 80 km of an AMTS coast station that uses frequencies in the 217-218 MHz and 219-220 MHz bands unless that amateur station licensee holds written approval from that AMTS licensee. The location of AMTS coast stations using the 217-218/219-220 MHz channels may be obtained as noted in paragraph (l)(3) of this section.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2051/what-is-a-fixed-digital-message-forwarding-system, by Adam Davis, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
