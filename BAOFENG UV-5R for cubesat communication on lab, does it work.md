# BAOFENG UV-5R for cubesat communication on lab, does it work?

*Tags: vhf, uhf, baofeng, icom · score 5*

## Question

Here we have a cubesat which operates in VHF/UHF. Communication with it (from a ground station perspective) is done with an Icom Radio. Would it be possible to replace it with a cheaper BAOFENG?

## Answer (score 4, by sessyargc.jp)

The usability of the Baofeng (or any radio with > 1Hz frequency step) will depend on the frequency and mode that you are using. If you use a 12.5kHz frequency step size you will never be able to tune to 435.345 MHz (FM mode) frequency, for example. You have to change your frequency step size to 5 kHz or 2.5 kHz to tune it.  
  
Notice though that the Baofeng has a tunable step size as documented in the specification you linked (Page 11). 2.5/5/6.25/10/12.5/25kHz frequency step sizes are sufficient for FM mode communications with a satellite.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3720/baofeng-uv-5r-for-cubesat-communication-on-lab-does-it-work, by oqrxke, sessyargc.jp. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
