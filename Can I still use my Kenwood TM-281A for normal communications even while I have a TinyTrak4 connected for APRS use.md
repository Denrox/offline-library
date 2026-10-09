# Can I still use my Kenwood TM-281A for normal communications even while I have a TinyTrak4 connected for APRS use?

*Tags: aprs, kenwood · score 6*

## Question

I am considering buying a Byonics TinyTraK4 to connect to my Kenwood TM-281a to do APRS.

However, I am wondering if I should instead buy a separate radio (I am considering a Baofeng UV-5R) as well and connect the TT4 to it instead of the TM-281A.

My fear is that with the TT4 connected to the TM-281, I will no longer be able to use the it for other communications unless I disconnect the TT4.

Is it possible to use the Kenwood for normal communications even while the TT4 is connected to it?

## Accepted answer (score 0, by W8AWT)

No, this would not be possible unless you were to program a PIC chip to switch the radio to the call channel, which would be set to the 144.930 MHZ APRS frquency when it heard an APRS brap from the TT. It would then have to switch the radio back when the APRS had been sent. Still, It would be VERY tricky because the PIC would only be switching the radio when it heard the APRS, not before. So, unless you could have the TT start transmitting but wait one second to send the APRS so the PIC could switch the TT, it would not work.

Additionally, how could the TT know when you were keying the mike?

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2343/can-i-still-use-my-kenwood-tm-281a-for-normal-communications-even-while-i-have, by W8AWT. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
