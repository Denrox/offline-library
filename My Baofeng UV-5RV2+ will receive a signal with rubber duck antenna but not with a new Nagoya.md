# My Baofeng UV-5RV2+ will receive a signal with rubber duck antenna but not with a new Nagoya

*Tags: antenna, baofeng, squelch · score 5*

## Question

I bought my self a Baofeng UV-5RV2+ as an inexpensive way to introduce myself to the world of ham radio. With all of the stock components everything has been working fine. I wanted to try to increase the radios performance so I purchased a Nagoya NA-320A antenna. When this antenna is attached I have to turn the squelch to 0 or hold the moni button to receive any sort of transmission. When the transmission comes in (squelch-0 or moni pressed) it is very clear with little static. my question(s) is; Did I get the wrong antenna, Did I get a bad antenna, is my radio broken, or is it something else entirely?

## Answer (score 6, by Glenn W9IQ)

The fact that you have a static free signal when you press the monitor button or open the squelch sounds like you may have CTCSS or DCS decode (receive squelch) turned on. This feature is normally used to ensure that the squelch does not open on your radio unless the repeater or station you are monitoring transmits its sub audible tone or digitally coded squelch code.

The Boefang brand refers to this feature as Select Calling and more specifically Group Calling. You can turn it on for CTCSS or DCS. Consult your manual or programming software. If you are setting this from the radio keypad, you need to enter a CTCSS or DCS code of 0 for the R-CTCSS and R-DCS values when prompted on the screen.

The following is excerpted from the manual and applies if you are not using memories:

**CTCSS**

1. Press the [MENU] button to enter the menu.
2. Enter [1] [1] on the numeric keypad to get to Receiver CTCSS (R-CTCS).
3. Press the [MENU] button to select.
4. Enter the desired CTCSS sub-tone frequency in hertz on the numeric keypad.
5. Press the [MENU] button to confirm and save.
6. Enter [1] [3] on the numeric keypad to get to Transmitter CTCSS (T-CTCS).
7. Press the [MENU] button to select.
8. Enter the desired CTCSS sub-tone frequency in hertz on the numeric keypad.
9. Press the [MENU] button to confirm and save.
10. Press the [EXIT] button to exit the menu.

**DCS**

1. Press the [MENU] button to enter the menu.
2. Enter [1] [0] on the numeric keypad to get to Receiver DCS (R-DCS).
3. Press the [MENU] button to select.
4. Enter the desired DCS sub-tone frequency in hertz on the numeric keypad.
5. Press the [MENU] button to confirm and save.
6. Enter [1] [2] on the numeric keypad to get to Transmitter DCS (T-DCS).
7. Press the [MENU] button to select.
8. Enter the desired DCS sub-tone frequency in hertz on the numeric keypad.
9. Press the [MENU] button to confirm and save.
10. Press the [EXIT] button to exit the menu.

Note that you may need the transmit T-CTCSS or T-DCS to be enabled in order to talk through repeaters in your area. Check your repeater guide.

Each memory can have its own CTCSS and DCS settings. If you are using memories, consult your manual or software to disable R-CTCSS and R-DCS for the appropriate memory channels.

## Answer (score 2, by rclocher3)

According to the web, your Nagoya NA-320A works on both the 2m and 70cm bands, matches the reverse-SMA antenna connector on your Baofeng, and works reasonably well. So you probably chose a reasonably-good model of antenna. Your new antenna might be broken, or there could be something wrong with your radio, or your radio might be set up incorrectly. (Do you have it programmed for the local repeaters? Does a repeater reply when you key it up with either antenna? Don't expect to hear much on the factory default frequencies.)

A good strategy might be to find someone else with a similar Baofeng HT, and have him or her test the antenna for you, and also look at your Baofeng. A knowledgeable operator could probably sort out your problem quickly. A good place to meet such people would be at the meeting of your local radio club. (Personally, I often bring my laptop and a programming cable to club meetings so I can help newbies program their HTs on the spot.) If you're in the US, you can use the ARRL's club search tool to find a nearby ARRL-affiliated club.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9177/my-baofeng-uv-5rv2-will-receive-a-signal-with-rubber-duck-antenna-but-not-with, by T12mack, Glenn W9IQ, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
