# WSJT-X V2: How to identify stations already logged?

*Tags: digital-modes, software, ft8 · score 3*

## Question

In V1.9 of WSJT-X, there was a feature that allowed one to change the color of stations already logged. This was necessary in knowing whether or not to respond to a given CQ.

In version 2, I am unable to determine whether or not I have already logged a potential contact that is calling CQ.

Is there a way to have WSJT-X V2 signify whether or not one has logged a given call sign?

## Answer (score 3, by Cecil - W5DXP)

Set your "New Call" to one color and your "CQ in message" to a different color. My new call CQs are green and my "CQ in message" are light red. The light red indicates that I have worked the station before because it is not a "New Call". And as Chris said, JTAlert also works.

The logic is that the combination of "New Call" and "CQ Only" result in New Call CQs and anything left over from that having "CQ in Message" is not a New Call. I'm glad it worked for you.

## Answer (score 2, by Brad Low - K5BDL)

I have version 2.1.0. Under File->Settings, select the General tab. There is a box marked "Show DXCC, grid, and worked before status" that can be check marked. I use that to identify stations I have worked before.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12503/wsjt-x-v2-how-to-identify-stations-already-logged, by MarqTwine, Cecil - W5DXP, Brad Low - K5BDL. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
