# What is the difference between MFSK64 and MFSK64L?

*Tags: digital-modes, fldigi · score 8*

## Question

I noticed this after updating fldigi to decode a Voice of America Radiogram.

The only thing I could find in the fldigi changelog was this:

```
MFSK HF Long Modes
* Added MFSK64L and MFSL128L new modes
* 6.25 Second interleaver for very-robust HF reception
* Assigned new RSIDs
* Mode MFSK-64L : 1026
* Mode MFSK-128L : 1029

```

Is the 6.25s interleaver all that has changed? What does this mean explicitly?

## Answer (score 5, by Phil Frost - W8II)

Yes, that's all that's changed. MFSK uses forward error correction, a technique of adding redundant information to the transmitted data so that if some of it is lost, it can be reconstructed from the redundant data. Because errors tend to happen in bursts (static crashes, fast fading, etc), it's common for FEC schemes to also use interleaving, which takes the bits to be transmitted and spreads them out over time. This way, if a burst of noise causes a string of bits to be mangled, after de-interleaving they won't be consecutive bits, thus the FEC will have a better chance of correcting the error.

On HF, long interleaving can be especially useful. The ever-changing ionosphere can make phase cancellations that come and go with a period of seconds. If the interleaving is done over long periods (in this instance, 6.25s), then this doesn't matter so much. To the decoder, it looks not as if the signal is fading and recovering, but just that the bit error rate is increased uniformly everywhere. As long as the FEC encodes enough redundancy, the message is still successfully decoded. The cost is increased latency: the transmission can't possibly be complete until 6.25s after the entire message is available. Rather annoying for conversations. Contrast with PSK31, which has no FEC, and no interleaving, so each character is transmitted as soon as it is typed.

If you want to dive into the *really specific* details, ARRL specifies the interleaving for MFSK as "self-synchronizing, based on 10 concatenated 4 × 4 bit IZ8BLY diagonal interleavers." You can also consult the Fldigi source code, or browse the particular commit responsible on Berlios. Comparing two modes in mfsk.cxx:

```
case MODE_MFSK64:
samplerate = 8000;
symlen =  128;
symbits =    4;
depth = 10;
basetone = 16;
numtones = 16;
preamble = 180;
cap |= CAP_IMG;
break;

```

[...]

```
case MODE_MFSK64L:
samplerate = 8000;
symlen =  128;
symbits =    4;
depth = 400;
preamble = 2500;
basetone = 16;
numtones = 16;
break;

```

we can see the two differ in just a few parameters.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/784/what-is-the-difference-between-mfsk64-and-mfsk64l, by Sterling N0SSC, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
