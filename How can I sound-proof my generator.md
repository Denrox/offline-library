# How can I sound-proof my generator?

*Tags: power-supply · score 5*

## Question

Looking for advice to semi-soundproof my extremely noisy gas generator, which kept everybody edgy on Field Day. It's a real powerhouse, but the cost of that power is my hearing. I'm looking to buy or homebrew something lightweight that I can use to enclose the generator, but leave easy access to refilling the tank, exhaust, etc. Thoughts? Links?

It's a Champion 100155 : https://www.championpowerequipment.com/product/100155-7000-watt-dual-fuel-generator/

## Accepted answer (score 4, by Marcus Müller)

I'd argue that power law is your friend: It's probably cheapest and most reliable and least of a hazard to get a long cable and place the generator as far away as feasible, possibly behind a car, rock, very large dog, small elephant, large elephant…

Downside of long cables of course is voltage drop due to resistance in the cable. Rule of thumb: The longer the cable, the more copper crosssection would be sensible. Before you spend lots of money on oversized cables: You can find the AWG table on every corner on the internet, and they list resistance per length for any common conductor diameter.

Calculate your maximum current drawn (if using many inductive / bad-PFC devices, 1.4× that number), approach with "I can live with a voltage drop of $x\in[2\ldots20]\,\text V$ for that current", calculate maximum resistance that would allow that ($U=R\cdot I$), and then just pick a cable diameter that doesn't have more over the length of cable you want to use.

Other than that, speaking from experience with a small car with a holey muffler: Probably, the exhaust end of the engine is where most noise happens. If you have a garage of your trust, maybe ask them whether it's realistic to add a muffler without losing too much power?

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9500/how-can-i-sound-proof-my-generator, by Noji, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
