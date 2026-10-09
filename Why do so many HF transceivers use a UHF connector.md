# Why do so many HF transceivers use a UHF connector?

*Tags: transceiver, connectors, pl259-so239-connector · score 9*

## Question

Just looking around at various rigs online for a fiend. Lots of them look really attractive TS-480, K2, K3, FT-450D, FT-950, IC-78, FT-897 to name just a few...

These rigs are mostly HF, albeit some are also VHF/UHF capable. Yet the antenna connector used is usually either PL259, or SO239. Both mentioned connectors are known UHF.

- What is the rationale behind having a UHF connector attached to an (essentially) HF rig?
- Is it merely a matter of cost/convenience as listed in [Pros/cons of the PL259/SO239 connector (M type)?](Pros%20cons%20of%20the%20PL259%20SO239%20connector%20%28M%20type%29.md)?

## Accepted answer (score 20, by oh7lzb)

The "UHF" PL259/SO239 connector, which was originally designed at World War II times as a *shielded banana plug* is actually **not a very good connector to be used on UHF frequencies**, due to its non-continuous impedance and other properties. The common name is a bit misleading, since it's old - at the time of the design, UHF referred to frequencies above 30 MHz, and by today's standards UHF is 300 MHz to 3 GHz. A measurement found online at the time of writing this answer documented 0.2 db insertion loss at 144 MHz and 1 db insertion loss at 432 MHz, and with low-quality connectors (or higher frequency such as 2.4 GHz) it would be worse. The connector works fine on the frequencies it was designed for: HF and VHF.

Most modern HF rigs come with these connectors mostly because it has become an industry standard for amateur HF transceivers, and it works. It might not be the best connector on the face of the earth, but everyone already has them on their rigs, cables, amplifiers, tuners and antenna switches. When someone produces an HF rig with some other connector, most users will have to use adapters or build adapter cables. **Cost, convenience, standard solution.**

## Answer (score 4, by GerryC)

The "UHF" connector, as stated, is a hold-over from World War II, and has become an industry standard. A lot of hams "know" how to put them on coax, and, since radio is, overall, forgiving, most don't notice the folly of their installation processes (melted dielectric, poor solder wetting, etc). Me? I can install them, but prefer to crimp them on. That, however isn't pertinent to your question.

Your original question has been answered well enough already, but you posed a corollary question. In my opinion, it depends on the target frequency you're working with and the size of the hardware. In general terms, I use a BNC connector for most of my lower frequency work (yeah, because they're easy to crimp, too), and SMA for anything about 1.2GHz. For me, it's often about saving space and still having efficient connectors. Both the BNC and SMA (and even the N) demonstrate a smaller impedence "bump" than most UHF connectors I've looked at.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/501/why-do-so-many-hf-transceivers-use-a-uhf-connector, by VU2NHW, oh7lzb, GerryC. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
