# Is Morse code allowed on FM in the USA

*Tags: united-states, legal, cw · score 9*

## Question

Let's say I get my little 2 meter FM handheld out and make a little sine-wave generator with which I pulse a morse code and if I connect it to headphones a speaker, I hear the dits and dahs of a nice sine wave tone. Now let's say I connect this to the microphone port on my transceiver with the VOX setting turned to detect when I am entering the morse.

Is this allowed, or is it illegal because of the wasted bandwidth when I could just use carrier?

My country is the USA.

## Accepted answer (score 17, by Dan KD2EE)

Completely legal. In fact, it's common practice to identify repeaters (both in the amateur service and in public safety/commercial) with exactly this method.

That said, you likely won't make many QSOs with it. There aren't many people who would be prepared to immediately respond if they started hearing FM morse on 146.52 (the typical hailing frequency for simplex operators on the 2m band), compared to people down in the CW section of the band.

## Answer (score 10, by James NF8I)

tl;dr: It's legal on any VHF or above frequency where phone modes are permitted. It is not allowed on HF or below, nor where phone modes are not allowed.

What you have described is called "Modulated Continuous Wave" (MCW), as defined in the US amateur radio rules under 47 CFR §97.3(c)(4), and would have the emission designator F2A. (The usual CW used on HF has emission designator A1A.) In areas regulated by the FCC, it is *not* legal on frequencies below 50.1 MHz, between 144.0 and 144.1 MHz, or between 219 and 220 MHz. It is legal on any other amateur frequency.

MCW is commonly used for automated identification of FM voice repeaters.

It is worth noting that some software capable of transmitting the many HF digital modes via an SSB transceiver can also generate CW in the same fashion. When transmitted this way through an SSB transceiver, it is technically emission designator J2A, which is still within the definition of proper CW. In areas regulated by the FCC, proper CW is legal on any frequency allocated to the amateur service (subject to certain limitations on the 60m band).

Sources:

- 47 CFR §97.3(c)(1), 47 CFR §97.3(c)(4), 47 CFR §97.3(c)(5), and 47 CFR §97.305(c)
- Wikipedia: Modulated Continuous Wave
- Wikipedia: Types of Radio Emissions

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/357/is-morse-code-allowed-on-fm-in-the-usa, by Skyler 440, Dan KD2EE, James NF8I. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
