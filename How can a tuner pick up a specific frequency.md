# How can a tuner pick up a specific frequency?

*Tags: antenna, frequency, antenna-tuner · score 6*

## Question

The point I'm confused about is the antenna. Depending on the environment, there are tons of different frequencies passing through you (FM, AM, 4G, SAT, etc). The electrons in the wire will move as the radio frequencies pass by. One wave will move the electrons at a certain rate. Another wave will move the same electrons at a different rate. All these waves will interfere with each other. You get some weird movement or none at all on the wire depending on the different frequencies hitting the antenna.

I kind of understand a tuning circuit (LC). How is the tuner picking up anything when the antenna is giving the LC circuit a complex wave? It's like you mixed up paint and the LC tuner somehow unmixes it. For some reason, it's not clicking for me. So what if it resonates at a certain frequency. The wave it's feeding is complete gibberish. Two different frequencies hitting the antenna could cancel out each other so electrons don't move.

I do not understand how a tuner (LC) can pick up a certain frequency.

Once I understand that this only makes sense for a specific frequency. FM radio works on a range of frequencies. How does a tuner "catch" a range of them?

https://physics.stackexchange.com/questions/326727/how-can-an-antenna-pick-up-thousands-of-frequencies-at-the-same-time

https://physics.stackexchange.com/questions/223469/how-does-the-tuner-really-work-in-a-crystal-set

https://physics.stackexchange.com/questions/8310/how-does-a-digital-radio-tuner-work

Edit: I'd like to give everybody a green checkmark. :) I still have a long way to go to be satisfied with my understanding but this is a great start. I've always been interested in radios. I'm going to start by creating my own AM then FM radio. I just needed the theory because anybody can put a kit together. I want to know the WHY in detail. I have so many more questions but I think this is enough to satisfy this post. You guys are the best!

## Accepted answer (score 3, by hobbs - KC2G)

There's something called the "principle of superposition" — in a linear system (which we can consider an antenna and the "front end" of a receiver to be), if the current resulting from signal A is $C_A$, and the current resulting from signal B is $C_B$, then the current resulting from both signals at once is simply $C_{A}+C_{B}$. Even if you have a million signals, they all just add to one another linearly, without being "modified". And as long as each one has its own frequency, we can use things like LC filters to pick out the one we want. In a time-domain graph it might look like "complete gibberish", but all of the original structure is still there (and much more easily seen in a frequency-domain plot).

It *is* a little bit like mixing paint and separating it out again, but imagine that every different color of paint was made of different-sized particles. When you mix the paints together, it looks like a muddy mess, but all the individual particles are still in there. If you had some very good, very fine mesh filters that could filter particles precisely by their size, you *could* separate one color back out of the mix! With real paints, that's not practical, but with real radio waves, it is.

## Answer (score 3, by Phil Frost - W8II)

Consider a swing, like the kind found at a playground. If you sit on it and shift your weight forward and backward at just the right rhythm, you can get the swing to go very high.

It goes high because the combination of the swing and the mass of your body is *resonant* at a particular frequency. When you shift your weight to "pump" the swing, you add just a little more energy to the swing. And when you pump at the right time, this extra energy is added to the stored energy from all the previous pumps, so with each swing you go a little higher than the last one. But this only works if you pump at the *resonant frequency*.

If you pump at some other frequency, you just jiggle around a little bit. You don't go higher and higher, because the actions of each pump don't reinforce each other.

Imagine you are swinging along happily, and simultaneously you receive a phone call, and your phone in your pocket is on vibrate. The vibration from your phone is also a shifting of weight, just as you are doing to pump the swing. But it is at a much higher frequency. Does it alter your motion on the swing? Technically yes, but the effect is very small because the vibration is not at the swing's resonant frequency. Imagine any perturbation you like: perhaps another person on the swing with you, but pumping at some other frequency. These actions might alter the swinging motion a *little bit*, but the swing responds most significantly to its resonant frequency, even if there are other oscillations going on at the same time.

An LC filter is a resonant system, like a swing. The difference is a swing involves an oscillation between gravitational potential energy (at the top of the swing) and kinetic energy (at the bottom of the swing), whereas an LC filter oscillates between energy stored in the electric and magnetic field of the capacitor and inductor respectively. The LC filter will respond strongly to oscillations at its resonant frequency, while other oscillations at other frequencies have only a negligible effect.

All modulations, not just FM, can be considered a "range" of frequencies. The only signal which is *exactly* just one frequency is an unmodulated carrier, which contains no information and so isn't used for communication. Some modulations use a wider range of frequencies than others, but no practical modulation uses a range of zero width.

That said, how can a filter work when the signal consists of a range of frequencies?

Real filters, even swings, have a resonant frequency where they are most sensitive. As the frequency deviates above or below that resonant frequency, the filter response diminishes, but it does not immediately drop to zero. The objective in designing a filter for a radio is to design a filter which passes the range of frequencies allocated to the signal, but no more. A very simple filter, like one made of a single inductor and capacitor, is "good enough" for some applications. But a radio designed for performance rather than simplicity will have more complicated filters, with more than one inductor and capacitor, to make the filter perform better. There are often multiple stages of filtering. Filtering, whether analog or digital, is a significant part of designing a radio, and a complex topic in itself.

## Answer (score 3, by hotpaw2)

It's not like mixing paint. That's because it's a just a simple sum or linear mix, rather than a chaotic or non-linear mix with intermodulation products.

It's like a duet with a soprano and a bass singer. You can easily transcribe the low frequency bass voice and semi-ignore the soprano, or vice versa, because the frequency ranges are so different, and your ear's cochlea has a filter mechanism that is a mechanical analog to electronic LC filters.

And tuners have a bandwidth. A filter can be either narrow or wide, depending on the design spec.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17512/how-can-a-tuner-pick-up-a-specific-frequency, by Derpy, hobbs - KC2G, Phil Frost - W8II, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
