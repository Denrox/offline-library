# Can APRS and other AX.25 packet-based systems (ie. a BBS) use the same frequency?

*Tags: aprs, packet · score 4*

## Question

I realize that it is technically possible to multiplex APRS and other AX.25 traffic on a single frequency, but I'm wondering if this is frowned upon or not. My hunch is that it is, but I wanted to see what other folks had to say as well.

My use case is that I have a single TNC and I'd like to use it for both APRS digipeating and a packet-based BBS system if possible. What I'm concerned about most is the connectionless nature of APRS and that BBS traffic would interfere with APRS packets enough to become a nuisance.

Let me know what you think.

## Accepted answer (score 5, by User5754448)

APRS typically uses a fixed frequency (e.g. 144.39MHz in the US), and shared by all APRS users. So yes, it would be frowned upon to also run a BBS on that frequency as it would interfere with everyone else's APRS communication.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22100/can-aprs-and-other-ax-25-packet-based-systems-ie-a-bbs-use-the-same-frequency, by Andrew Young, User5754448. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
