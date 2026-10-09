# How do I select a programmed memory scan on the Yaesu FT-897D?

*Tags: transceiver, yaesu, equipment-operation · score 3*

## Question

The Yaesu FT-897D has a so-called “Programmable Memory Scan (PMS)” feature, which allows limiting scanning to a user-defined band by creating special paired memory entries which set the upper and lower frequency bounds.

I've used it successfully on the first programmed band (M-P1L to M-P1U), but I can't figure out how to select a different programmed band to scan. I've tried selecting M-P1L before entering PMS mode and it just goes to PMS-1 instead of PMS-2, and none of the controls *in* PMS mode change bands that I've noticed.

The manual on page 50 discusses how to enable PMS but not how to change bands. Searching for advice on the web only turned up this rather annoyed person's workaround of SKIPping the memories other than the one to use, which can't possibly be how it's supposed to work.

## Accepted answer (score 2, by Kevin Reid AG6YO)

The PMS pairs interact with tuning similarly to the built-in band limits. Use the usual tuning controls (MEM/VFO CH or DIAL) to go past an end — higher than M-PxU or lower than M-PxL — and the transceiver will switch to the next or previous PMS pair.

As far as I've found, this is the *only* way to change between PMS pairs. Pressing the BAND buttons will *not* do so, and will merely disable PMS and change bands normally.

If you leave and re-enter PMS mode the last used PMS pair will be remembered, but the VFO will be reset to the M-PxL frequency.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1461/how-do-i-select-a-programmed-memory-scan-on-the-yaesu-ft-897d, by Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
