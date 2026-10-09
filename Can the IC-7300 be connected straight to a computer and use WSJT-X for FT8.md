# Can the IC-7300 be connected straight to a computer and use WSJT-X for FT8?

*Tags: icom, ft8 · score 4*

## Question

Do I need a separate device to use digital modes with the IC-7300 or do I just need to connect the 7300 to my computer via USB in order to use WSJT-X for FT8?

Thank you.

## Answer (score 7, by AndrejaKo)

Yes, you only need a USB2 A to B cable.

The IC-7300 already has an integrated sound card, for audio signal transmission, and an integrated serial port for remote control, both of which are connected to computer using the USB2 B port at the back of the radio.

In some rare cases, you might also want a Icom CT-17 compatible interface cable. Namely, the radio also has a CT-17 compatible serial input.

If you want to control the frequency and key the radio in RTTY mode and at the same time, switch between the mark and space using the serial port, but without using DTS/RTS pins, then you need the capability to have two serial ports on the radio, for which a CT-17 compatible cable is needed.  
Otherwise, the USB cable is enough.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11780/can-the-ic-7300-be-connected-straight-to-a-computer-and-use-wsjt-x-for-ft8, by MarqTwine, AndrejaKo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
