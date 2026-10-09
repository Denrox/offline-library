# Can IMAP email be used for packet radio?

*Tags: packet, internet · score 4*

## Question

I just barely learned that IMAP is a protocol that allows you to read and respond to emails without using the internet. Would it be possible to use this application for packet radio and if so, how? I am using the Ubuntu 14.10 operating system.

## Accepted answer (score 2, by David KF4MDV)

IMAP is a protocol for transferring email, nothing more, nothing less. It typically uses TCP/IP as the underlying protocol, but it *could* be routed over something else (like packet radio). If you wanted to, you could configure TCP/IP over AX.25 but I don't know if anyone else is doing it, so you'd probably need to run your own mailserver on the other end as well. (You could even configure that mailserver to bridge to the internet, but keep in mind that you'd be responsible for any incoming traffic that made it onto amateur frequencies!)

What you can't do is use Thunderbird to interact with any typical packet BBS or mailbox systems, they work with different protocols. So essentially, what you ask is possible, I'm just not sure if it's useful.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3663/can-imap-email-be-used-for-packet-radio, by BJsgoodlife, David KF4MDV. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
