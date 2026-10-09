# Using 75 Ω instead of 50 Ω coax feed

*Tags: coaxial-cable, antenna-system, impedance-matching · score 7*

## Question

Can I replace my old 50 Ω coax with RG6? It's cheaper and less loss at VHF/UHF. I would match by L/2 multiples of coax to repeat input and output impedance or L/C matching networks at each end.

Is this a viable alternative to expensive 50 Ω coax and what problems could I have?

So far I have used this on UHF and found a 6dB improvement in received signal.

## Answer (score 9, by Phil Frost - W8II)

Sure, you can use 75 ohm coax instead of 50 ohm. In some cases (such as feeding a dipole), 75 ohm coax may be a better match to the load than 50 ohm. In other cases (such as feeding a vertical), it may be a worse match.

You may not even need to do additional matching. A 75 ohm load on a transmitter designed for a 50 ohm load is only a 1.5:1 SWR, which isn't that bad.

Do however keep in mind that in many cases 75 ohm coax is cheap not because 75 ohm coax is inherently cheaper, but because it's just plain *cheap coax*. The common application of CATV means big-box stores are quick to carry cheap 75 ohm coax because their customers care primarily about cost, and for a short CATV run, the high loss and poor isolation of a cheap cable may not be especially critical or noticed by a typical consumer.

For a transmitting radio application, the consequences may not be so benign. It is usually cheaper to buy better coax than it is to buy a bigger amplifier. And a directional antenna in a receive application fed with coax with poor isolation may pick up enough external noise to negate the benefits of the antenna directivity.

75 ohm coax will work, and you may be able to find good quality 75 ohm coax at a favorable price. But do try to make an informed decision.

## Answer (score 5, by Mike Waters)

Many, many hams use 75Ω coax. I have for decades. All of my outdoor coax is RG-6 or RG-11. In the past I have used larger 75Ω CATV hardline, which has even lower loss.

Many hams just accept the 1.5:1 VSWR caused by the small impedance difference. I fed a 50Ω 2m array with 75Ω coax using a very simple matching arrangement, using two short pieces of coax at the feedpoint; one 50Ω and one 75Ω. (I can't think what it is called right now).

In fact, the feedpoint impedance of a center-fed dipole is 75Ω! It is only 50Ω at one low height. Feed a resonant dipole with 50Ω coax, and you actually have a small mismatch!

The power handing capability of RG-6 is almost identical to RG-213. And even at the legal limit, the voltage is still low enough that flashover will not occur between the center conductor and the shield even with a mismatch.

The thin copper plating on the RG6 cable centre conductor may be a problem at HF but for UHF it should be ok

K4KYV, myself, and others on the Topband reflector measured it. The consensus was that at 80 meters it made no difference, and at 160m it made a little difference but it was still insignificant.

This *may* be a duplicate question. In any case check out this search and see if you can find more answers there.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14760/using-75-o-instead-of-50-o-coax-feed, by R Johnson, Phil Frost - W8II, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
