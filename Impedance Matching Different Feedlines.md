# Impedance Matching Different Feedlines

*Tags: impedance, balun · score 6*

## Question

(I promise there will be a question in this wall of text. I'm just giving context.)

I've been wanting to try my hand at building my own antenna system for the last few weeks and in doing research, a number of questions came up. In particular, matching transmitters, feed lines and antennas in order to create a fully balanced system.

This site, run by W5ALT, gives a great overview on why different systems need to be impedance matched in order to function properly, as well as consequences of improper impedance matching. I therefore understand why a balun would be used for coax feeding a balanced dipole, both for balance and impedance purposes.

I also went about researching different antennas for portable use. Stackexchange led me to the October 1984 QST article on a full-wave delta loop. One of these setups (see following image, part B) describes a 450-ohm ladderline going into a 100-ohm feed point on the loop.

On this site, the author says to NOT use a balun between the 50- or 75-ohm coax feedline and the 100-ohm feed point:

Don't use a Balun on this Antenna! On a horizontally oriented loop you can feed a corner, center of a side or anywhere it is unimportant.

I also have a folded dipole fed directly by ladderline (Cobra Ultralite Sr.) that functions quite well (I busted through a pileup for a Portuguese contest; it can't be that bad). It is fed by 50-ohm coax from a tuner into a 1:4 balun to the ladderline. From various sources on the internet, the typical impedance of a resonant dipole is roughly 73 ohms. A folded dipole will increase this impedance to the square of the number of parallel elements (for the ultralite sr. with 3 parallel elements, I calculate 9 * 73 = 657 ohms impedance). The feedline could very well be 600-ohm ladderline (I am not sure; the line is not marked with impedance).

**So my question is this:** in particular, why does the W1FB full-wave loop design *not* require some form of a transformer between the 450-ohm ladderline and the 100-ohm antenna? My research tells me it's obvious that having matched impedance would allow more efficient power transfer from the feedline to the antenna. Is it because ladderline is balanced? Is that kind of impedance mismatch allowable? Is it a rule that you don't need a balun for ladderline? Is it purely a choice by the designer? I'm familiar with the subject of electronics, but I'm certainly no electrical engineer, so the theory behind this just seems to contradict practical examples.

Thanks for any and all help. I've been trying to find a reason for this for days and nothing seems logical to me.

## Accepted answer (score 1, by Phil Frost - W8II)

It doesn't make sense because people on the internet are wrong or misinformed, present conflicting information, or just plain don't know what they are talking about.

Impedance mismatches aren't the end of the world. An impedance mismatch does not, in itself, cause power loss. It causes power to be *reflected*, at which point it will go in the other direction until it's either absorbed or encounters another impedance mismatch which reflects it back at the antenna. When it gets back to the antenna, some of that power is radiated, and the rest of it reflects back and forth again until its all radiated.

In fact, if you had a lossless transmission line, impedance mismatches wouldn't matter at all. Each parcel of power would just reflect back and forth until it's radiated.

We can't have lossless transmission line, but we can keep losses very low. One way is to buy good coax. Good coax is expensive. Another way is to use ladder line. For the cost, ladder line has lower loss than coax.

Interestingly, a piece of transmission line can be used as a transformer. If that transmission line is 1/4 wave long, it's called a quarter-wave transformer, and it makes whatever's at the end of it look like the conjugate impedance. That's part of what's going on in some of these antennas, but there's a problem...

Whenever you hear someone say "don't use a balun", you should be thinking:

1. they may not have a good understanding of RF engineering, and
2. the feedline is actually part of the antenna

See [Using a balun with a resonant dipole](Using%20a%20balun%20with%20a%20resonant%20dipole.md). You absolutely can feed a dipole without a balun, but you have to understand that if you do it, the coax is as much of the antenna as the balun. This means anything you read about dipoles (like, their radiation pattern, feedpoint impedance, etc) does not apply. It doesn't necessarily mean it's a bad antenna, it's just some other kind of antenna which might be good or bad. Since the geometry of the feedline is different at each station, it doesn't mean anything. It just means you don't know.

Be especially dubious when you hear "don't use a balun" in combination with "multi-band antenna". One way to make a multi-band antenna is to design the antenna such that there are a lot of common-mode currents on the feedline, thus making the feedline in effect a long-wire antenna. The "antenna" is really just a distraction: the feedline does most of the radiating. There are quite a few antennas that dubiously work this way.

I hope that addresses your concerns enough. I can't really explain every question you have (that would be an entire book on antenna design), but regardless there are some good lessons to be learned here:

- the internet can be wrong,
- especially when hams are writing about antennas,
- your intuition about things not making sense is well-founded, and
- the best way to learn how things really work involves a good deal of skepticism.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2469/impedance-matching-different-feedlines, by Italic_, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
