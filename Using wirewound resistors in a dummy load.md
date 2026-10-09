# Using wirewound resistors in a dummy load

*Tags: equipment-design, impedance, dummy-load · score 3*

## Question

I have a bunch of high-wattage 50 ohm resistors lying around, but they are wirewound.

If I use them as a dummy load for transmitters 144 MHz and down, how bad would that be? Since they probably will be an inductive load, could I use capacitors to cancel out the inductance?

Probably better that I get some non-wirewound resistors, but I'm just wondering how bad it would be for the radio.

## Answer (score 6, by Kevin Reid AG6YO)

If I use them as a dummy load for transmitters 144mhz and down, how bad would that be?

It's just a mismatched load, and the consequences are the same as for a mismatched antenna. Check your transmitter's manual for the degree of mismatch it can handle and any applicable warnings. Modern transmitters typically have self-protection circuits and will not be harmed, but may automatically reduce power or shut off.

Since they probably will seem like an inductive load, could I use capacitors to cancel out the inductance?

Yes, but it would be canceled out at a specific frequency only (and nearly canceled in a region around it) and would have some capacitive or inductive reactance elsewhere. That is, you now have a dummy load with a small bandwidth. If you want to use it on a particular band, or if the transmitter is capable of handling the SWR resulting from the mismatch, then this isn't a problem.

For comparison, if you instead construct your dummy load from non-inductive resistors, then you can use it at any frequency whatsoever equally well, at least ideally. In practice, there's always some stray inductance and/or capacitance and there will be limits — this is why manufactured dummy loads have specified frequency ranges.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1625/using-wirewound-resistors-in-a-dummy-load, by Skyler 440, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
