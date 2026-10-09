# Antenna tuner at the transceiver output confusion

*Tags: antenna-theory, impedance-matching, impedance, antenna-tuner, resonance · score 5*

## Question

I am a bit confused. Let's take a HF transceiver for example.

My understanding is that the output impedance of the transmitter is 50 ohms. The impedance of the coaxial cable feedline is 50 ohms, and if we have a resonant antenna at the operating frequency, the antenna will have an impedance of 50 ohms, so all good, a maximum transfer of power, and no need for an antenna tuner. Great.

Now if we have a non-resonant antenna, the transmitter output impedance will still be 50 ohms, the feedline still 50 ohms, but there is now an impedance mismatch between the end of the coax and the antenna. Shouldn't the antenna tuner be placed there to solve the mismatch?

How is it that an antenna tuner (internal inside a transceiver, or placed at the output of the transceiver) will solve this issue?

Will this not change the output impedance of the transmitter so that now we have an impedance mismatch between the transmitter output an the coaxial cable feedline which is fixed at 50 ohms? Thanks in advance for any clarity on this.

## Answer (score 5, by rclocher3)

Having a transmatch (antenna tuner) at the feed point of the antenna can be an excellent way to solve the problem of a mismatched antenna; an antenna system with the transmatch at the feed point of the antenna will almost always have less loss than an antenna system with the transmatch at the output of the transmitter, because the feedline operates the most efficiently. Remote transmatches have many disadvantages also:

- Usually more expensive than a transmatch in the shack
- Only work for a single antenna
- Must be weatherproofed
- Can be difficult to mount
- Can be difficult to access for service
- Harder to protect from lightning
- Usually don't support more power than 100 or 200 W
- Power must be provided, either from a separate power line or by using devices that send power through the coax
- Must be remotely controlled somehow; if they sense the frequency of the transmitted RF, then the transmatch may be mis-tuned for a second or two after changing frequencies or bands, possibly forcing the transmitter to reduce power or be damaged

For an antenna tuner in the shack, the transmitter sees an antenna system with a nice 50 Ω input impedance (ideally), so the transmitter is happy. Things are not quite as optimal in the feed line, because standing waves form, which raises voltages at every point in the feed line, causing higher losses. The impedance mismatch between the feed line and the antenna causes reflections (which is what creates the standing waves), but reflections are generally not the problem; we are usually more concerned with losses in the feed line. Often, the losses are negligible or low.

Suppose that a transmitter transmits 100 W, the coax has a loss of 10 W, and a remote transmatch has an insertion loss of 10 W. The power to the antenna is 80 W. Suppose that the transmatch is moved to the shack, and the power line losses increase by 20 W; the power to the antenna is now 60 W. Another 20 W may seem like a lot, but that's only another 1.2 dB of loss, a small fraction of an S-unit. On HF, only dedicated contesters, DXers, and other weak-signal aficionados [would notice](How%20big%20is%20a%20decibel.md) a loss of 1.2 dB.

To sum up, remote transmatches are a fine solution to some mismatch problems, but not all mismatch problems. A transmatch in the shack keeps the transmitter just as happy. Transmatches in the shack cause more loss, but the loss is often negligible in practical terms. Transmatches in the shack are less expensive, and often quite a bit more practical, than remote transmatches.

## Answer (score 2, by hobbs - KC2G)

It's important to remember that a feedline having a 50-ohm characteristic impedance doesn't "force" any signal appearing at its terminal to be 50 ohms; it just means that if you give it a signal where V/I = 50 ohm, then it will make it to the other end without reflection or transformation, while other impedances will be reflected at its boundaries and transformed along its length.

Will this not change the output impedance of the transmitter so that now we have an impedance mismatch between the transmitter output an the coaxial cable feedline which is fixed at 50 ohms?

Yes, and this is exactly what you want to happen. As you probably know, an impedance mismatch causes a reflection. A well-matched tuner causes just the right mismatch at the transceiver end of the feedline to *re-reflect the reflection* caused by the mismatch at the antenna end of the feedline.

The feedline itself sees mismatches at both ends, but the antenna impedance, as transformed by the feedline and the tuner, looks like 50 ohms to the transmitter; and the transmitter impedance, as transformed by the tuner and the feedline, looks like a conjugate match to the antenna, so both of them are happy and transferring optimum amounts of power to/from the feedline.

Since the feedline is operating at an SWR > 1:1, the standing-wave current causes additional losses compared to the case where the antenna is perfectly matched (or the case where the tuner is at the antenna end), but the magnitude of those additional losses depends not only on the SWR, but on *how much loss the feedline has at the operating frequency to begin with*. If the SWR is moderate, the cable run is short, the frequency is low, and/or the cable is low-loss, then the mismatch loss will be manageable.

The fact that the reflections have to travel down and back the feedline (potentially multiple times) before getting absorbed by the antenna *does* cause some amount of distortion in the form of inter-symbol interference, but [for reasonably narrowband signals, and reasonable SWRs, this effect is absolutely negligible](Why%20aren%27t%20ghosts%20and%20intersymbol%20interference%20due%20to%20unmatched%20impedance%20%28high%20SWR%29%20a%20concern%20for%20HF%20receivers.md).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20165/antenna-tuner-at-the-transceiver-output-confusion, by Engineer999, rclocher3, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
