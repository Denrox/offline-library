# What does

*Tags: ft8 · score 4*

## Question

I caught this in FT8, did someone just enter <...> as their call sign or is this code for something?

## Accepted answer (score 5, by Peter Bagyinszki)

From the WSJT-X documentation:

Angle brackets imply that the enclosed callsign is not transmitted in full, but rather as a hash code using a smaller number of bits. Receiving stations will display the full nonstandard callsign if it has been received in full in the recent past. Otherwise it will be displayed as <...>.

https://wsjt.sourceforge.io/wsjtx-doc/wsjtx-main-2.7.0-rc2.html#COMP-CALL

This is an interesting read about FT8 callsign hashes: http://www.dx.nl/?p=1478

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22052/what-does-mean-in-ft8, by Pablo Fernandez, Peter Bagyinszki. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
