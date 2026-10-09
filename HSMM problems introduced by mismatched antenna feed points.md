# HSMM problems introduced by mismatched antenna feed points

*Tags: hsmm, yagi · score 4*

## Question

I have been trying to understand the finer points of HSMM, and I ran across this statement about antenna feed points (emphasis mine):

802.11 signals produce very broadband signals, typically 20-22 MHz. There is evidence to date that indicates the use of a same polarized antenna with one type of feed point at one end of the link and the use of a same polarized antenna with a different type of feed point at the other end of the link, *may introduce a problem with HS digital signals*. A common example of this potential mixed-antenna issue would be if one HSMM radio station uses a horizontally polarized linear Yagi, while the other HSMM radio station at the opposite end of the link uses a horizontally polarized loop Yagi.

- Can someone cite references that detail the specific evidence for these kind of problems?
- If it's known, what are the technical reasons that HSMM transmissions through a horizontally polarized linear Yagi would introduce HSMM signal problems when they are received by a horizontally polarized loop Yagi?

## Accepted answer (score 1, by WPrecht)

At a guess, the problem is probably a timing issue with the way the antennas receive signals. At the speed you are using here, 2.4GHz or 5GHz, small things matter. Early tests with repurposed Part 15 hardware had problems initiating a link at 34 miles as the firmware designed for WiFi house networks (<100') had already given up waiting and was retrying before the ACK came back (IEEE 802.11 Experiments in Virginia’s Shenandoah Valley, QST July 2005).

John Champa, KBOCL (SK), did a lot of writing popularizing HSMM in CQ VHF magazine. The heyday of this seems to have been 2003-2008. While otherwise hard to get, scans of some of his articles are to be found at http://hsmm.wikispaces.com. In his Spring 2004 article called "The Frontllnee: HSMM Part 2 - Developments in Amateur Radio", he mentions:

Mixed Antenna Design Problem: This is the possibility of a unique situation when using HSMM radio with certain antennas which requires more amateur radio study. It is often thought that as long as both antennas at the ends of an HSMM radio link are of broad-bandwidth design (the HSMM signal is 22 MHz wide) and of the same polarization (usually horizontal) then this is acceptable and all is okay. While this may be true for other wide signals, such as analog ATV VSB (vestigial sideband) signals or analog ATV-FM signals, it may not be true with even more broad-bandwidth high-speed digital signals. Some evidence seems to indicate that, for example, the use of a horizontally polarized dish antenna with a dipole feedpoint at one end ofthe link and the use of a horizontally polarized long loop Yagi at the other end (again both broad-bandwidth antennas and both horizontally polarized) may nonetheless introduce a problem (higher BER, or bit error rate) because of symbol errors caused by the manner in which each antenna manipulates the radio-signal wave front. Again, further radio amateur experimentation with HSMM radio signals is warranted to determine the impact of using mixed antenna types on the radio link .

Unfortunately, he gives no specific references to his source on that an almost all the links mention in the acknowledge section are out of date.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/186/hsmm-problems-introduced-by-mismatched-antenna-feed-points, by Mike Pennington, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
