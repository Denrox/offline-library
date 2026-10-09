# UK "Remote Operation" defination

*Tags: legal, united-kingdom, remote-control, encryption · score 3*

## Question

I am a UK licensed Amateur Radio operator with an Intermediate License.

I have a question surrounding the UK's (Ofcom's) definition of "Remote Operation".

My understanding is that for any Remote Operation you must not use any form of encryption on the links, and if you hold an Intermediate License, you must only use wireless links to communicate with your rig (which I think is limited to 500mW).

I am considering building my own little rig using a Raspberry Pi. However, I would most likely be manipulating the Pi (within my house) using SSH, connected to wired Ethernet.

Given Ofcom's restrictions, does this mean I can't do that, as I would be violating both the encryption (using SSH) and wireless-only (by using wired Ethernet)?

Or, have I interpreted the term "Remote Operation" too broadly, and as long as I was at my house, it would be fine as it wouldn't be considered "Remote"?

## Accepted answer (score 1, by Brian K1LI)

According to clause 17(ff) in Ofcom publication, *UK AMATEUR RADIO LICENCE, Section2: Terms,conditions and limitations*, "Remote Control Operation" applies, "...where the Licensee has the ability to control the Radio Equipment from a different location to that where the Radio Equipment is located;" Since your control means and your radio will both be located within your house, they are *not* in different locations and none of the remote control regulations would seem to apply.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13179/uk-remote-operation-defination, by user14615, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
