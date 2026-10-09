# Supershield or Superscreen coax: Does it exist? What is its common name?

*Tags: coaxial-cable, testing, mf · score 3*

## Question

I'm sure this seems like a Google question, but I've BTDT and come up empty.

The problem I'm trying to solve is to obtain cables that are as "leak proof" as possible. Tried Pasternak "100% shield" and they leak like a sieve. Tried Andrew FSJ1-50 (F1B-PNMBM-1M) which is pretty good, but leaks at both ends, apparently due to the joining to the connectors.

Given that a commercially made cable isn't good enough here, I'm tempted to make my own, and if I'm going to that much trouble I want the best. I keep seeing references to "Superscreened" or "double Superscreened" coax, which has braid and mu-metal, but I can't find anywhere that sells such cable.

I'm hoping someone here knows where I can find it, and the appropriate BNC ends so I can fab some quality cables. I'm not too concerned about cost.

Premade 1m cables, BNC male to BNC male would be best, but only if the connectors are put on so that they don't leak.

I am working inside a faraday cage sending test signals to multiple antennas, and I don't want the coax radiating anything significant. The ferrite bar antennas have a gain on the order of -80db so leakage from the cables can dominate the signal at the receiver, and I can't use any other type of antenna here.

If there's another way to solve this, that would be great.

Frequency of interest is <1MHz.

## Answer (score 5, by user103218)

It turns out that these cables were made by TE Connectivity. Some time back, they sold that business to Commscope. After talking to Commscope, it looks like those cables no longer are made. :(

Their recommendation is to use FSJ1-50, even though RG-214 has a lower transfer impedance at this frequency, because the shield coverage is better. So I will have to fight the leakage at the joints of the connectors and cables.

Anyway, if someone else can benefit from this info, here it is.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15784/supershield-or-superscreen-coax-does-it-exist-what-is-its-common-name, by user103218. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
