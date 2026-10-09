# Yaesu FT-991A: FM and C4FM modes don't work on HF bands

*Tags: transceiver, fm, equipment-operation, yaesu, equipment-troubleshooting · score 4*

## Question

I bought a second-hand Yaesu FT-991A. It works pretty well and by the look of it's internals I don't believe it was ever repaired.

However I noticed one weird thing. When I try to use FM or C4FM on HF bands (including 28 MHz and 50 Mhz), FT-991A transmits for about half a second, then the green speaker icon blinks 3 times and the transceiver returns to receive mode. There is no such problem on 2m and 70cm bands.

The question is - is this a well-known behavior and maybe I just need to check some settings, or this unit is defective? All settings related to VOX and operation using a repeater I could find are disabled.

UPD1: It worth noticing that the manual of this transceiver is in Japanese, and maybe it's behavior differs from EU/US versions. As I understood using Google Translate, the manual implicitly says that FM and C4FM can be used only on 28 Mhz, 50 Mhz, 2m and 70cm bands. The manual in English doesn't seem to say that. I tried to take into account IARU Region 3 band plan and possible power limitations, but it didn't help. Also it seems that the unit was subjected to MARS/CAP mod, because it's possible to transmit outside of amateur bands, e.g. on 6 MHz.

UPD2: I've checked that the latest available firmware is used (MAIN v02-01, TFT v02-00, DSP v01-11). Also I thought maybe PTT wires could catch an RFI, but using MOX has the same effect. Resetting the transceiver to factory defaults didn't help.

## Accepted answer (score 2, by Aleksander Alekseev - R2AUK)

After reverting MARS/CAP mod everything works as expected. I don't know whether the problem was caused by the mod per se or maybe just one of FCC cables was a little bit misplaced when the mod was made.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16116/yaesu-ft-991a-fm-and-c4fm-modes-don-t-work-on-hf-bands, by Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
