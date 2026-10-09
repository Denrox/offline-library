# How does selecting the opposite sideband when receiving CW on HF reduce interference?

*Tags: hf, cw, filter, ssb · score 16*

## Question

I am studying for my FCC General Class license, and question/answer G4A02 reads as follows:

**Q:** What is one advantage of selecting the opposite or "reverse" sideband when receiving CW signals on a typical HF transceiver?

**A:** It may be possible to reduce or eliminate interference from other signals.

I am studying from the *ARRL General Class License Manual (Seventh Edition)*.

I don't understand how this is possible. If the signal is being transmitted on the upper sideband, how does switching to receive on the lower sideband eliminate interference? As I understand it, that would eliminate everything from the upper sideband, and I would hear nothing from the upper sideband *including* the CW signal I'm trying to listen for.

The referenced page from the Q/A explains this concept thusly:

...  
*Reverse Sideband* controls allow the operator to switch between receiving CW signals above the displayed carrier frequency (USB) and below it (LSB). This can help avoid nearby signals causing interference by placing them on the other side of the carrier frequency where filtering rejects them.  
...

I do not understand. **How does this work?**

## Accepted answer (score 20, by Kevin Reid AG6YO)

CW signals are not “transmitted on the upper sideband”, nor the lower one. A CW signal is approximately *at a single frequency* (with only the additional bandwidth required to allow the key-up and key-down transitions).

However, the standard method of *receiving* a CW signal is identical in structure to a single-sideband receiver. The local oscillator (LO) of the receiver is set to a frequency *not quite equal* to the CW signal, and the difference between the incoming CW and the LO is the audio tone you hear. Let's say for concreteness that the difference is 800 Hz.

If that frequency shifting were all that was going on, then you would hear many CW signals (from both sidebands) at different pitches, so there is a very narrow filter to select just the one signal. That filter will select either the frequency +800 Hz from the LO (upper sideband) or the one −800 Hz from the LO (lower sideband).

For convenience, a modern transceiver does not display the LO frequency (as it does in single-sideband mode) but rather the LO frequency offset by 800 Hz, so that you know the actual frequency of the signal.

If you switch from upper-sideband reception to lower-sideband reception, then you (or your receiver's CPU, more likely) should simultaneously change the LO frequency to be 1600 Hz (double the offset) higher, so that (if you were perfectly tuned to start with) you'll hear the same signal at the same pitch as before.

The difference this makes is that signals *not* exactly at the 800 Hz offset frequency will be flipped around that midpoint: an unwanted signal within the filter passband that was at (relative) 1200 Hz will now be at 400 Hz, and you might find that lower-pitched sound less troublesome. Or, if your receiver's filters are not perfectly symmetrical for this purpose, the unwanted signal could be actually attenuated.

If you have a receiver already, listen to CW and SSB signals using both CW and SSB modes, tune around, and try to get a feel for what's going on. CW mode is just SSB mode with a narrower filter and the offset display.

(Note that when you switch between CW and SSB mode, your receiver might preserve the actual LO frequency (thus changing the displayed frequency), or preserve the displayed frequency (thus changing the LO frequency and the pitch of what you hear).

## Answer (score 5, by hotpaw2)

If you are using (or building) a vintage radio that does not have a narrow CW audio filter, the audio bandwidth above and below a listenable CW audio side-tone frequency can be quite unsymmetric. By flipping the side-band, one might be able to move an interfering signal down close to 0 Hz audio frequency (inaudible), even if the audio is not bandpass filtered to any "reasonable" degree. (e.g. I started out in this hobby by building a tube regenerative SW receiver.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3711/how-does-selecting-the-opposite-sideband-when-receiving-cw-on-hf-reduce-interf, by Bryson, Kevin Reid AG6YO, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
