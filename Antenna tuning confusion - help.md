# Antenna tuning confusion - help!

*Tags: antenna, impedance-matching · score 5*

## Question

In a recent discussion with a fellow ham about where to use a RigExpert antenna analyzer for tuning an antenna for minimum SWR, we couldn't decide if "antenna only" or "feedline+antenna with the analyzer at the transmitter end". For example, if I tune my antenna for minimum SWR right at the antenna itself ... that's perfection, right? But if I then analyze the feedline coax PLUS the antenna, the "whole antenna system" ... and realize that I need to tune the antenna again for minimum SWR (as seen by the radio end), then that tune would result in the highest power efficiency 'into the air'. But wouldn't that be a de-tune of the antenna itself? I'm confused on where I should connect the analyzer, and whether or not the "de-tune of the antenna" is real or best or not? Can any of you, smarter than me, explain and explain what I should do? BTW, calling different antenna manufacturer tech support lines gave us different answers ... one said to tune at the antenna, the other said tune from the transmitter end of the coax.

## Answer (score 6, by user10489)

Tuning at the antenna will give you the most accurate antenna characteristics, but a good VNA can cover up some of the inaccuracies from tuning at the end of the coax instead.

However, you have to realize that the coax is also part of the antenna system. You shouldn't have to tune the coax, but you can.

If SWR is lower at the end of the coax, that's normal loss in the coax. If it is higher, the coax is acting like part of the antenna and a choke to stop common mode current will help.

If there is common mode on the coax, that means the coax is radiating and part of the antenna. You can tune the coax by making it a multiple of a quarter wavelength (corrected for velocity factor) long. However, if you do this, you have to realize the coax is radiating like part of the antenna which can be undesirable and possibly dangerous. If the coax is not tuned, this will raise your SWR. A balun will prevent (or at least reduce) common mode current and (hopefully) make the coax length irrelevant.

Some antennas (like the carolina windom) intentionally allow part of the coax to radiate by careful placement of the balun (or unun). However, you don't want the coax in your shack radiating, as that adds extra RF exposure, and the possibility of RF burns.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22127/antenna-tuning-confusion-help, by K4JUL, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
