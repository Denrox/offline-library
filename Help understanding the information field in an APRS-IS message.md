# Help understanding the information field in an APRS-IS message

*Tags: aprs · score 5*

## Question

I'm looking at the raw packet data from http://aprs.fi. I see packets such as these:

```
ROSLDG>APN390,HEBOWX,OR2*,qAR,MKSRDG:@015805z4501.34NF12351.41W_000/000g000t053r000p000P000h92b......U2k
W7KKE-9>TTRSUT,NEWPRT*,OR2-1,qAR,W7GC-3:'4]. {nv/]"3z}
KG7HEL-3>AAAPPP,WIDE1-1,WIDE2-1,qAR,BEAVRT:'vX<0x1c><0x1c> <0x1c>#/>TEMP1-1 digi running on battery= [Latitude and longitude are both 0]

```

Where is the specification for the information that comes after the : at the end of the path information? I can find a specification for APRS data as it is packeted into an AX.25 packet, but not for the messages that come from an APRS-IS server. Can I assume that anything after the : is in the same format as the Information Field in the APRS AX.25 specification? What happens to non-printables?

I've surmised that the ' and @ after the : are APRS Data Type Identifiers, but I have no idea what the <0x1c> stuff is in the last packet.

## Answer (score 3, by Duston)

Everything after the : is the payload that the station is sending out. While there are conventions so that the data is meaningful, I don't believe there are any standards. For example, the first line is a weather report, Wind calm (0 mph at 0 degrees, 0 mph gust), temp 54, no rain, RH 92% etc). The second line is probably a compressed location packet (compressed so that it takes less time to send.) In the last line, the <0x1c> probably represents a non-printable character (CTRL+Z or EOF). Since non-printable characters are, well, not printable the software either on the sending or receiving end likely converted the 0x1C (binary) to the string <0x1C> so that it would be printable (and if needed human readable.) Beyond that, without knowing the software sending the telemetry, there's not much more you can learn from it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10336/help-understanding-the-information-field-in-an-aprs-is-message, by watkipet, Duston. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
