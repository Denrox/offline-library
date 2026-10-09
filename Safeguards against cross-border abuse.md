# Safeguards against cross-border abuse?

*Tags: legal · score 3*

## Question

I live in a country that falls under ITU region three and recently joined my national amateur radio association. I learned that the frequencies for the repeaters run by the association were kept secret because they'd been facing cross-border abuse from neighboring countries when regional political relationships became...strained. Since the association runs all the repeaters in the country, that means all the repeaters are operated in secret.

I found this odd because since all regional associations are "member-societies" of the International Amateur Radio Union as per its constitution. Are there no safeguards to cross-border amateur radio abuse?

Note that I do not know the exact nature of the abuse, just that it was serious enough to cause this change.

## Accepted answer (score 4, by Marcus Müller)

There can't be physical "safeguards"; radio waves simply do not care about human borders.

There should be political safeguards, but these would require the regulatory bodies of two countries to cooperate. If cooperation fails, you get a political problem (not a technically solvable one, typically). If cooperation on a regulatory level between countries fails, the least they're probably going to worry about the constitution of some international organization that is occupied with coordinating a hobby internationally.

Personally, how would you even keep active repeater frequencies secret? It would take a person with an SDR transceiver seconds to scan all bands in question and minutes to figure out which frequencies get transposed to others. Keeping frequencies secret sounds more like a military thing to do (where you can actually make it illegal / punishable by localization and potential military counteraction to "probe" these frequencies) than something applicable to civil-access frequencies.

**Extended Answer (from the comments)**

Legally, nothing binds nations but international law (which not all countries feel bound by), only enforcable by action of the UN – and I'd assume it'll take a couple of decades to even reach a decision, and enforcement could typically only happen by means of violence; I doubt a halfway reasonable congregation of states will ever wage war because of IARU violations. So, no, there's no "realistic" legal ways to enforce things between non-cooperating states Things look very different when states still feel bound by contracts they signed. But if tensions are high, like let's say between Pakistan and India, this commitment to contracts breaks down. Again, there's nothing legally binding states if states don't want to commit to that. International law very much is extremely only defined by the notion that it's

1. better for all if states adhere to that; and
2. the relatively abstract assumption that violation of it can have embargoes or war as consequence. Again, states won't wage war because amateur radio rights are broken, realistically.

So, the legal safeguard you can get can only work if the worst case – war with a neighbor – is actually so unlikely that neither side risks that. If, like you say, "tensions are high", then your best bet at getting a legal safeguard for the neighboring country not violating your rights is to make your own government find peace with its neighbors, and reinstantiate the rule of law on a basis of agreement. Sorry. There's no easier alternative.

## Answer (score 2, by Brian K1LI)

I post this response as a brainstorming idea. I don't know the law and I point out the weaknesses of the idea.

I am surprised that keeping the repeater frequencies secret has worked. Static information like this is notoriously difficult to protect. I perceive the goal as being to reduce the frequency of unauthorized access to some tolerable level, with a means to monitor compliance and rapidly respond to breaches, without increasing equipment cost. As your "legal" tag suggests, this must be accomplished by means that pass muster with IARU.

Because an in-band repeater might include a duplexer, changing the PL tones could be a more convenient and cost-effective way to limit access than changing repeater frequencies. For a cross-band repeater, it might be simpler to just change the frequencies inside each band, or even go so far as to implement frequency hopping.

But, even if you change the PL tones or frequencies, the problem is the same: protecting the new values. Perhaps you could use an algorithm that works like a "security dongle," computing the current PL tone or repeater frequencies for use at any given time. When the details of the algorithm and its parameters leak out (which they will), you can change the algorithm and/or its parameters. This logic would have to be implemented in the repeater, authorized members would need to carry the computing means with them and the regulatory authorities would need to be informed.

Because there is a small number of PL tones available, it would not take very long for a determined abuser to identify the new PL tone, so it may be difficult to balance the convenience of authorized operators with security against abuse. Adding external tone-generating hardware could implement multi-tone and poly-tone means that would effectively increase the "mean time to being hacked."

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13067/safeguards-against-cross-border-abuse, by Amin Shah Gilani, Marcus Müller, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
