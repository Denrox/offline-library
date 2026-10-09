# Does a dipole require a 1.5:1 balun?

*Tags: balun · score 4*

## Question

Dipoles ideally have 72 ohms impedance. I know most of the time this isn't what one gets and it can vary a lot. But let's assume we can build this perfect dipole that exhibits this impedance.

Why do most designs just suggest a 1:1 balun for coax, if coax is usually 50 ohms? Wouldn't it be better to use a 1.5:1 balun? What would be the loss if we connect a 72 ohm antenna to a 50 ohm line without matching it?

## Answer (score 4, by Phil Frost - W8II)

A "1:1 balun" in this application is usually a common-mode choke. Its function is primarily to [reduce common-mode current](Using%20a%20balun%20with%20a%20resonant%20dipole.md), rather than to perform any impedance transformation.

Such baluns are easy and inexpensive to fabricate, work on many bands, can handle a lot of power, and have low loss; all because in the differential mode they just look like a length of transmission line.

If there were a trivial way to achieve a 1.5:1 impedance transformation additionally, that would be great. Unfortunately there is not. One could use a transformer with an appropriate turns ratio, but that would involve transferring power through the core with associated loss and other issues. Or an L matching network could be used, but again this comes with loss and other engineering challenges.

In practice, any SWR under 1.6:1 is acceptable for most applications. The [SWR losses](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md) due to such a mismatch are most likely less than the loss that would be introduced by a matching network.

The SWR loss can be eliminated by using 75 ohm coax. Of course the transmitter will still see a 75 ohm load, but this is within the specifications of most transmitters.

## Answer (score 3, by Aleksander Alekseev - R2AUK)

In you are feeding an antenna which has an impedance 72 Ohm, you will get SWR:

```
72 / 50 == 1.44

```

... which corresponds to ~3% power loss. Considering that the transformer may cause power losses of similar order personally I wouldn't use one.

This being said in reality a dipole can be bent to inverted-V shape. Inverted-V has an impedance about 50 Ohm.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15589/does-a-dipole-require-a-1-5-1-balun, by hjf, Phil Frost - W8II, Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
