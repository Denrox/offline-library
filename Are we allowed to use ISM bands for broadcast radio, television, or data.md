# Are we allowed to use ISM bands for broadcast radio, television, or data?

*Tags: united-states, legal, fcc · score 3*

## Question

Do you need an FCC license to broadcast television and radio on ISM bands? Does it make sense to transmit this way?

## Accepted answer (score 5, by Ryuji AB1WX)

ISM bands are unlicensed for Part 15 compliant devices, which include some communication devices, but broadcast audio or video programming, intended for the public, for entertainment or information dissemination, is not allowed in Part 15. (Broadcast services and other commercial services are explicitly defined in 47 USC Parts 73 through 79, and those services and usages are not allowed in any of the ISM bands.)

Some of the commenters appear to be confused about the primary users of the ISM bands: ISM (industrial, scientific, and medical) users. Communication is a secondary user, and as such, all communication devices under Part 15 must tolerate unlimited interference.

The output power and emission limits are also set differently for the ISM users versus communication devices. If a transmitter is designed to modulate any informational programming payload, the output power limit goes down to a level unusable for broadcast.

When a broadcast license is granted, the licensee must have a defined primary service contour and meet the minimum field strength obligations. Frequency assignment must also be coordinated to avoid interference (broadcast is very often the primary user). Those standards are incompatible with the ISM bands.

Thus the concepts of ISM and broadcast bands are totally opposite. One demands tolerance of unlimited interference from all other users, and the other requires a well-defined quality of service for many stations in any geographical area, requiring bandwidth and strong coordination. They are totally incompatible from a regulatory viewpoint.

In the case of HF ISM bands, such as 6.765–6.795 MHz, 13.553–13.567 MHz, and 26.957–27.283 MHz, the power limit may be higher, but broadcasting is still prohibited.

The 6.8MHz ISM was the subject of the other thread, but in that case, the whole band is only 30 kHz, not enough for any video other than slow scan TV.

Globally, ISM and broadcast services are equally incompatible. ITU RR 5.138, 5.150, 5.280, etc. define ISM allocation, but the nature and restrictions are parallel to the US regulations.

## Answer (score 3, by David Hoelzer)

This is an interesting and somewhat tricky question, I think. First, any answer to this type of question must include the disclaimer that it depends where you are in the world and who your regulating body is. Of course, it also depends what you are doing. As I read the regulations from the FCC, as long as you are within power limits defined in part 18 and the equipment meets part 15 standards, you should be able to transmit nearly anything as long as the content does not violate some other law or standard.

As I understand things, Part 18 is the primary controlling section for folks covered by the FCC. Likely, the most important part of this for your question would be the frequencies and power restrictions. While Part 18 devices need to be interference tolerant, I believe we are *always* required to avoid unnecessary interference. As the experimenter who is likely using equipment that does not have other FCC approvals, the responsibility to limit interference would rest with you.

The other section you should read closely is Part 15 which deals with devices and experimentation requirements.

If you live in any kind of fairly densely populated area, I would suggest reaching out the the FCC field office for advice or to a local amateur radio club. Local clubs are often made up of folks who previously worked as engineers in broadcasting roles, veteran radio operators, and similar who can assist you in interpreting the regulations in addition to helping you to be safe with experimental transmissions.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23680/are-we-allowed-to-use-ism-bands-for-broadcast-radio-television-or-data, by jimmie bridges, Ryuji AB1WX, David Hoelzer. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
