# What do you call antenna that combines multiple Hustler resonators (using a VP-1) above a shared mast?

*Tags: antenna-theory, vertical-antenna, theory · score 5*

## Question

I know that a Hustler MO-3 54" mast with something like a RM-20S resonator on top is officially an example of a center-loaded quarter-wave vertical...

... but Hustler also allows you to mount *multiple* resonators (say, a RM20 or RM20S + RM30 + RM40 or RM40S) by using their VP-1 bracket, which basically looks like a metal triangle whose ends are bent at an angle & have a hole centered within the bent ends for mounting up to 3 such resonators, and a hole in the middle to mount the whole assembly to the top of a mast (like the MO-3).

I'm scratching my head trying to figure out what you'd actually *call* that type of antenna, though.

On one hand, the coils might act kind of like traps... but *then*, that logically implies that it only acts like a single-band antenna for frequencies at or above the frequency of the highest band's resonator mounted to it. In other words, if you had resonators for 20m, 30m, and 40m mounted, 28MHz would see it as a single center-loaded quarter-wave vertical (because it would be blocked by the 30m and 40m resonators' coils), but wtf happens when you're transmitting on 7-10MHz?It seems like at 7mhz, you'd have RF dividing itself up among *all three* of the resonators (and their whips at the top) & end up with an antenna type that probably has a different name than merely "center-loaded quarter-wave vertical".

If it's not obvious, I'm seriously intrigued by the idea of combining multiple Hustler resonators on a mast via something like their VP-1 bracket. Given that these products have been around since before most of us were even born, *someone* has to have written about them, their design, and their theory of operation by now. If not a dissertation, maybe an article in QST or 73 magazine sometime in the 1970s or 1980s. But without knowing the proper name for an antenna that results from mounting two or more resonators above a shared mast, I'm searching for a needle in a haystack.

Some photos & a description of an antenna like this are at https://ab4bj.com/wordpress/2017/01/ab4bj-portable-antenna-system/

## Accepted answer (score 3, by Brian K1LI)

It appears that Hustler simply calls it a multiband vertical. I would call it a "center loaded fan vertical." It's definitely a vertical, being operated against some conductor that represents "ground" (e.g., auto body). And, the coil-loaded elements fan out in an arrangement similar to a fan dipole. Searching the internet turns up a coining of the term "fan dipole" by VK6FLAB in a QRZ forum post from 2019, but he appears to be referring to a monopole adaptation of the fan dipole.

Each "resonator" - a loading coil plus whip - allows current to pass only on its design band of operation, but not on other bands. On bands *below* the resonator's design frequency, the resonator presents a large *capacitive* reactance, while on bands *above* the resonator's design frequency, the resonator presents a large *inductive* reactance, both of which impede the flow of RF current to render that resonator electrically open.

As you point out, this product has been around since long before the allocation of the WARC bands to amateur operation. Individual resonators are available for bands from 80m through 10m, so it may be necessary to evaluate possible interactions between resonators on closely-spaced bands, e.g., 20-17-15 as a trio. I can't find any documentation on the response of combined resonators.

## Answer (score 3, by hobbs - KC2G)

It's analogous to a fan dipole, where you feed multiple dipoles, with different resonant frequencies, in parallel, under the assumption that if one of them corresponds to the band you're transmitting on, then it will have the lowest |Z| and therefore take most of the current, while the other elements remain more-or-less inactive. Except that:

1. It's not a dipole, it's a monopole.
2. The elements are coil-loaded rather than depending on their length for resonance.
3. There's a shared segment (the mast) before the different elements split off, so it's not quite a proper "fan".

I would just call it a multiband loaded vertical and call it a day. The theory behind it is going to be that of a loaded short vertical, combined with that of a fan dipole (for how the bands interact).

The coils don't act as traps; instead, the wrong-band coil+whip combinations have (presumably) a large reactance, therefore a large overall impedance, which limits the share of current it will take compared to the right-band coil+whip combination. And when you add one small impedance in parallel with two much larger ones, the result will be pretty close to the small one, so the overall contraption is still a decent SWR match to your transmitter, provided that one of the elements alone would have been.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18066/what-do-you-call-antenna-that-combines-multiple-hustler-resonators-using-a-vp-, by Bitbang3r, Brian K1LI, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
