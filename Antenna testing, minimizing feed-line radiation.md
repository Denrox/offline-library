# Antenna testing, minimizing feed-line radiation?

*Tags: antenna, feed-line, testing · score 3*

## Question

Assume that one does not have access to a multi-million-dollar RF anechoic chamber.

When testing an amateur radio HF or VHF antenna, how would one absolutely minimize the amount of any RF radiation from the feedline, tower, and/or any other parasitic elements, such as power supply cords, AC wiring, computer cables, gutters, or any other nearby antennas?

Assume the antenna is (claimed to be) an imperfect dummy load, and you want to make sure the vast majority of any RF radiation is convincingly coming from the dummy load antenna, and not elsewhere.

## Answer (score 2, by Mike Waters)

The proper mix of ferrite for your frequency of interest in a properly-designed common-mode current choke is your friend.

Look no further than Jim Brown's latest PDF on this subject at k9yc.com There is no better source of information anywhere else.

**RFI, Ferrites, and Common Mode Chokes For HamsMost recent update April 2019.** This tutorial is directed specifically to RFI in ham radio applications. It includes an extended discussion of the use of common mode chokes in antenna systems and for suppression of RFI. A chapter on audio and computer interconnections in ham stations shows how to make bulletproof connections between a computer sound card and ham rigs for SSB, RTTY, PSK31, and SO2R contesting without expensive interface boxes, using nothing more than simple cables with the right connectors on each end. There's also a chapter on grounding and bonding.

Of course, the unun or balun would be mounted right at the antenna feedpoint; right where the power cord meets the power supply, etc.

http://k9yc.com/RFI-Ham.pdf

Also see http://www.karinya.net/g3txq/chokes. Although he recently passed away, his expertise lives on.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15137/antenna-testing-minimizing-feed-line-radiation, by hotpaw2, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
