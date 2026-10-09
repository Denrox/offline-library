# Resources and guidance regarding APRS

*Tags: aprs, emergency · score 3*

## Question

I know getting my Technician License is the place to start, however, I have in my head a clear path that I want to achieve and am looking for guidance for the most efficient way to achieve that goal.

The goal is to set-up my family and I with APRS so in the event of a disaster as apart of my PACE plan we can set up a laptop (heard this is possible with a radio like the Kenwood D74) and be able to share coordinates and even send text communications to each other.

I am using Online resources now to study and get my Technician. I am not specifically looking for a dissertation in the practice of using APRS just good resources, pitfalls things to look out for as well as a lapse in my reasoning or things I am not understanding with my current thinking.

I appreciate any and all help and in advance, Thank you for sharing your expertise.

## Accepted answer (score 3, by rclocher3)

As you already know, amateur radio is an excellent resource for emergency communications, and APRS is a fine tool for it. However, APRS is not the only tool, and I would caution you to not obsess over this one tool. For instance, I'd advise you to make sure that you and your family also know how to communicate using the simplest technology available, which is generally VHF/UHF FM for local communications, or HF SSB for longer distances. For FM you should know what your active local repeaters are and have practice using them, and also know how to use simplex when the repeaters are down. Having a plan for emergency power would also be a good thing.

Regarding APRS, I don't know of any books that comprehensively describe it, but such a book may be out there. However, the official APRS web site aprs.org does a pretty good job of covering the subject, even if it does ramble a bit. Most APRS packets are received by gateway stations, which copy the packets to an internet network of servers called APRS-IS. The web site aprs.fi receives APRS packets from APRS-IS, filters the packets for a local area, and displays the information on a map. You can use aprs.fi to see APRS activity in your local area, even without a license.

APRS is intended to be a tactical information system that can be used to broadcast all sorts of interesting information. Unfortunately it hardly ever gets used as such, and instead is mostly used by weather stations and people broadcasting the location of their cars. However it is still tremendously useful for some things. In many places the network of APRS digipeaters has better coverage than the mobile phone network, and as you noted, APRS can be used to deliver short text messages. The International Space Station has a digipeater, and it could possibly be used as a last-ditch emergency way to get a message out of a wilderness area, although these days there are [better tools for that job](How%20to%20do%20APRS%20in%20real%20wilderness.md).

Unfortunately I haven't done a review of available APRS software in several years, but if you want to send text messages via APRS then you'll probably want to use software to do it. I've heard that there is interesting APRS software for Android and iOS.

Let me point out some related ham technologies/tools that you might find interesting. First, Winlink allows a station to send text-based messages over HF, VHF or UHF. These messages are in the format of emails, and the Winlink network interoperates with the internet, so emails can be sent by radio and then go through a gateway station to the recipient over the internet, and vice-versa. Second, D-STAR is a digital mode for VHF and UHF that can carry voice and data simultaneously. D-STAR can also be used for location data and text messaging using a tool called D-RATS, and I believe the location data is shared with APRS-IS (I'm not positive about that). The downside of D-STAR for such purposes is that the radios and repeaters tend to be expensive, and there are not nearly as many D-STAR repeaters as APRS digipeaters.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17099/resources-and-guidance-regarding-aprs, by Adam Schneider, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
