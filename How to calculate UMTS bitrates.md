# How to calculate UMTS bitrates?

*Tags: digital-modes · score 6*

## Question

Assuming:

**Radio frame**

1. Subdivided in 15 slots
2. Number of chips: 38.400
3. Duration: 10 ms; each slots = 666.6 μs and has 2.560 chips

**Example of channelsDPDCH (Dedicated Physical Data Channel) (UL)**

- Spreading factor varies between 4 and 256
- Data rates 960, 480, 240, 120, 60, 30 and 15 kbit/s
- Spreading factor 4, 640 bits/slot, 15 slots/frame, 100 frames/s -> 960 kbit/s
- Spreading factor 256, 640 bits/slot, 15 slots/frame, 100 frames/s ->15 kbit/s
- A connection can have at most 6 DPDCH -> 5, 74 Mbit/s

**Question**

I don't really understand how the bitrate for DPDCH is determined like "960kbit/s" for example. Which formula is used to derive these values?

Here is a picture of the frame structure.

## Accepted answer (score 6, by Phil Frost - W8II)

Spreading factor 4, 640 bits/slot, 15 slots/frame, 100 frames/s = 960 kbit/s

I don't really understand how the bandwidth for DPDCH is determined like "960kbit/s" for example.

There's no equation. It's just another way of stating the information that's already there. By dimensional analysis:

$$ \require{cancel} \frac{640\, \text{b}}{\cancel{\text{slot}}} \frac{15 \cancel{\text{ slot}}}{\cancel{\text{frame}}} \frac{100 \cancel{\text{frame}}}{s} \frac{1\,\text{k}}{1000} = \frac{960\,\text{kb}}{\text{s}} $$

I also would not call "960 kbit/s" a *bandwidth*. That may be acceptable in the context of say, a PCI bus, but in the context of a radio protocol, *bandwidth* also means the width of the signal in the frequency domain. I'd call it a *bitrate* to avoid that confusion.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1254/how-to-calculate-umts-bitrates, by beginningperl, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
