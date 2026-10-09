# Why is SNR for FT8 defined using the noise power in the 2500 Hz channel containing the FT8 signal?

*Tags: ft8, wsjt-x · score 4*

## Question

I see the term "SNR_2500" is often use to make it clear. Is it useful to use this SNR definition in some contexts? Is this kind of convention used in other digital modes or communication systems?

Edit to add: I should have made it clear that my expectation is that the noise power used for SNR would be that in the range of frequencies occupied by the FT8 signal (or perhaps the range of frequencies seen by the FT8 detector).

## Answer (score 6, by hobbs - KC2G)

Matter of opinion, but it's kind of a "level playing field" thing. Say you want to compare the SNR required to have a successful QSO across SSB, conversational-speed CW, QRS(S) CW, and various different digital modes. Each of those will have a different occupied bandwidth.

If you compute SNR for each mode using its *own* occupied bandwidth, that's an "honest SNR", and the narrower modes will naturally have higher SNR since you're including a narrower noise bandwidth.

On the other hand, if you use the *same* noise bandwidth for each mode, then the SNR at the receiver, under the same conditions, with the same transmitter power, can be expected to be pretty much the same. Naturally you want to pick the *widest* bandwidth of any of the modes you care about, which is going to be 2500Hz for typical SSB. Now instead of saying "mode X is copyable down to 3dBSNR, mode Y is copyable down to 0dBSNR, but mode Y is half as wide so they're effectively the same", you can just make a statement like "SSB is good above +10dB, RTTY down to -5dB, PSK31 and CW down to -10dB, FT8 and QRSS down to -25dB" *all using dB(SNR-in-2500Hz)*, and it becomes easy to rank them. If you come up with a new mode, you can measure it on that same scale and see where it stacks up, without too many caveats.

Here is an article that explains pretty much the same thing, taking it a step further and arguing in favor of Eb/N0. But SNR-in-2500 is something that's pretty accessible to hams (in many cases you can read it almost directly off of the S-meter by setting your passband to 2500Hz), while Eb/N0 requires intimate knowledge of the protocol to calculate Eb from a received power level, and at least a bit of math to calculate N0 from the noise power in any realistic passband.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22477/why-is-snr-for-ft8-defined-using-the-noise-power-in-the-2500-hz-channel-contai, by gschro, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
