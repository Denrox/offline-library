# In SSB how do receivers calculate the frequency offset without a carrier?

*Tags: receiver, ssb · score 3*

## Question

On page 2-9 of the ARRL Ham Radio License Manual, it discusses how in SSB one of the side bands and the carrier are suppressed to conserve power and bandwidth. Given the explanation of how AM works, however, it seems like a receiver would need the carrier in order to determine the various frequencies in the SSB; it would need the offset distance from the carrier to understand what frequency the rightmost or leftmost sidebands represent. Are SSB receivers just guessing, looking for the cluster of sidebands and assuming the leftmost is some low phone frequency?

## Answer (score 7, by Kevin Reid AG6YO)

No, the receiver does not try to determine a carrier frequency, *you* do. When receiving SSB, you must adjust the VFO (main frequency control), not just until you hear a signal, but also to adjust to match the suppressed carrier frequency by ear.

Slightly-off SSB signals have a distinct sound, which is not just being too low or high in pitch, because the human voice contains harmonics. For some fundamental audio frequency $f$ you have $f, 2f, 3f, …$ in some proportions, but if the VFO is offset by some amount $\delta$, the demodulated audio will have $f + \delta, 2f + \delta, 3f + \delta, …$ which do not make up the same wave shape and therefore sound funny.

In principle a receiver could attempt to automatically tune in the way you describe, but this would only work at high signal-to-noise ratios (strong signals). Doing it manually takes advantage of your human skill at recognizing human speech.

You'll quickly understand this for yourself once you have a receiver in your hands — and learn why people care about the feel of the VFO knob.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5646/in-ssb-how-do-receivers-calculate-the-frequency-offset-without-a-carrier, by rcampbell, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
