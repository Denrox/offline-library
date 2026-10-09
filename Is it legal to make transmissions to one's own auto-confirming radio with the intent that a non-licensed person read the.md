# Is it legal to make transmissions to one's own auto-confirming radio with the intent that a non-licensed person read the messages?

*Tags: united-states, legal, fcc, automation, digital · score 3*

## Question

Is this scenario legal?

1. John, K1ABC, sends this message from a portable QTH: K1ABC-1 DE K1ABC-2 On the way home DE K1ABC/P
2. John's home radio automatically responds (controlled by a computer): K1ABC-2 DE K1ABC-1 MESSAGE RECEIVED DE K1ABC
3. John's wife Jane, who is at home and is not licensed, reads the message on his computer. (This was John's goal.)

This "QSO" takes place in a section of an HF band where automatically controlled digital stations are allowed. The modulation and protocol are legal and publicly documented.

This would be similar to John sending an email to Jane through his own Winlink node, except Jane cannot reply (besides the computer's acknowledgment of receiving the message, which Jane does not control).

## Answer (score 2, by natevw - AF7TB)

Perhaps a good lawyer could help you argue for some sort of loophole here, but this this certainly seems to fall within the *intent* of the § 97.113 **Prohibited** transmissions section of Part 97. Both:

(a) No amateur station shall transmit: […] (5) Communications, on a regular basis, which could reasonably be furnished alternatively through other radio services.

and:

(b) An amateur station shall not engage in any form of broadcasting, nor may an amateur station transmit one-way communications except as specifically provided in these rules; […]

Where broadcasting is defined as "Transmissions intended for reception by the general public, either direct or relayed." (I'm basically ignoring the signal report / "ACK" response that you've added since it doesn't really seem to make it any more of the kind of "two-way" transmission that *is* allowed….)

Looking on the flip side of "§ 97.111 Authorized transmissions" you can see that apart from some specific public service roles, the amateur radio service is meant mostly just for hams to talk to hams about ham stuff.

[**UPDATE**: see comment thread for some discussion; whether the FCC condones or simply overlooks it, there has certainly been a long tradition in ham radio of outright non-ham/third-party–oriented personal usage of the bands…]

All that said, I can think of a big counterexample that hinges around one specifically authorized one-way communication: **telemetry**!

If I understand correctly, it's been a long-standing tradition for hams to "broadcast" their mobile location over APRS knowing and indeed in many cases *intending* that their (non-ham) friends/family could follow along.

How different is sending a series of live GPS updates revealing a vehicle en route, than your example of simply saying "on the way home" outright? Is one telemetry ["measurements at a distance from the measuring instrument"] and the other not?

It's natural to want to think of creative ways around the rules, and frankly the FCC is not going to roll a van full of men in black after you for a relatively harmless stunt like what you described. But unless you get philosophical about humans being measuring instruments it seems to me that the APRS stunt ends up technically "in bounds" (telemetry transmission) while the self-QSO stunt feels more "out of bounds" (one-way personal communication).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21396/is-it-legal-to-make-transmissions-to-one-s-own-auto-confirming-radio-with-the-, by Someone, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
