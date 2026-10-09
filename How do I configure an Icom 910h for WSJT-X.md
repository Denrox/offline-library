# How do I configure an Icom 910h for WSJT-X?

*Tags: icom, wsjt-x · score 3*

## Question

Does anyone have the WSJT-X and radio settings for an Icom 910h? I am using a Digi-Rig interface. I do know the radio is 19,200 baud. I have ci-v trn turned off and the ic address is 60. Am I missing anything on the radio side? What about in the WSJT-X settings?

## Answer (score 3, by user10489)

The Icom 910h doesn't know anything about WSJT-X, there are no specific settings for that. The baudrate is mostly irrelevant.

What you really want is settings for all digital modes including wsjt-x. You want at least 2.8KHz bandwidth. All filters turned off. ALC off or set to slow.

Set mic gain to match your computer's audio output levels, or use the line in on the radio. Adjust computer audio output to not overload the radio and trigger ALC. (Audio level too low, you don't put out enough power. Too high, you splatter and distort (especially if ALC messes with the audio), which is worse.)

You need to match the CI-V settings to the radio control settings in the library that WSJT-X is using and make sure that is working. Test both frequency control and PTT in the wsjt-x settings panel.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22922/how-do-i-configure-an-icom-910h-for-wsjt-x, by Kc3ndu, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
