# What is this (dangerous) connector type that looks like SMA?

*Tags: connectors · score 5*

## Question

At a hamfest, I recently bought a few RF adapters that I *thought* were BNC to SMA:

However, when I tried to use one, it ended up destroying the SMA male plug on the cable I attached to it. It pushed the pin out of the housing!

When I looked more closely, I saw that the socket on this adapter is designed for a much smaller pin - more like 0.4 or 0.5 mm instead of SMA's 0.9 mm. In all other respects it looks exactly like SMA female, and the threads fit an SMA M barrel just fine.

This isn't an RP-SMA issue - it's definitely a socket. I know about the difference between 75 and 50 ohm BNC connectors, but (until today) didn't think a similar situation existed for SMA.

I have a handful of these and they all appear to have the same dimensions. That makes me believe it wasn't a manufacturing defect. That would mean there's some connector that looks a lot like SMA that's not SMA.

What sort of adapter do I have?

## Answer (score 5, by tomnexus)

It would be interesting to see a closer photo of the centre conductor hole.

Is it possibly an adapter with the (partly hollow) centre pin of another SMA connector broken off inside it? Or do the fingers look OK and the hole go all the way down? In this case I suspect it's just a junk adapter, out of tolerance, sold anyway.

In BNC and N type connectors there are 75-ohm variants, which have smaller centre conductors while keeping the outer dimensions the same. The 75 ohm female side can be damaged by the 50 ohm male connector pin; the other way around they just make poor contact.

I'm not aware of a 75 ohm SMA, and I can't find one on the internet. SMA is sometimes sold on 75 ohm cable, which is probably fine up to a few GHz, because the 50-ohm section is only 10 mm long.

There are other connectors that use the same outer thread as the SMA, and can sometimes even be interconnected, but they look quite different and the smaller ones would just be destroyed, not push back the SMA pin. Wikipedia has a nice picture of some of the variants.

## Answer (score 2, by user10489)

It wouldn't be my first guess, but this might just be a bad part. (The other answer covers my first guess.)

This might be an actual SMA connector, but manufactured with bad tolerances. I've seen a lot of those. There's a company making PL259/SO239 connectors but with wrong dimensions that break real ones. Wouldn't surprise me if you found an SMA with the same issue.

The supply chains these days are contaminated with lots of cheap fraudulent and poorly manufactured parts that look almost like real ones.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22470/what-is-this-dangerous-connector-type-that-looks-like-sma, by user3486184, tomnexus, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
