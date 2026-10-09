# Efficient BPSK31 amplification

*Tags: digital-modes, amplifier · score 7*

## Question

I'm looking at making a portable system that can transmit BPSK31. I have a limited power budget, so I'm looking at trying to make my final power amplifier as efficient as possible. From my understanding, you can't use a plain non-linear amplifier (e.g. Class C or E) because BPSK31 isn't a constant envelope signal. The amplitude drops to zero on bit changes, and that behavior prevents splatter on bit changes.

Is there a way to efficiently amplify BPSK31, or am I stuck with an inefficient final amplifier?

## Accepted answer (score 2, by Phil Frost - W8II)

There is a way, but you don't end up with an amplifier that you can connect to an ordinary rig. The trick is to express the signal as phase and amplitude.

Consider: with an ordinary non-linear amplifier (such as typical for FM use, for example) you can manipulate phase (and thus, also frequency), but the amplitude is fixed by the amplifier's supply voltage.

What if you vary the supply voltage? You then have a way to also manipulate amplitude. If you can manipulate phase and amplitude, then you can express anything that can be expressed in I/Q representation -- the only difference is that you are doing it in polar coordinates instead of Cartesian coordinates.

Now you have the problem of making an efficient "amplifier", the output of which is the power supply for the class C amplifier. However, since the amplitude variations are much slower in this polar domain (for PSK31, only 31.25 Hz), this is a substantially easier problem. A switch-mode power supply can do the task.

This seems pretty simple, so you might wonder why everyone doesn't use amplifiers like this. The trouble lies in implementation details. However, if you are designing for the specific case of PSK31, then you can take specific knowledge of the modulation into account for your design. Also, PSK31 is such a simple and slow scheme, the challenges are much less than they would be if we were trying to make an amplifier for a cellular phone or Wi-Fi radio.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1971/efficient-bpsk31-amplification, by W5VO, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
