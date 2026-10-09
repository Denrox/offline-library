# Is Army surplus steel wire suitable for an antenna?

*Tags: antenna-construction, wire-antenna · score 4*

## Question

I have a whole spool of military communications steel wire that I've been thinking about using to string up a doublet. We used this stuff when I was in the 138th Signal Btn and let me tell you, it's the meanest wire for it's size and weight that you'll ever lay your hands on. Some of it's attributes are:


It's so stiff that the set coils are hard to straighten out - and it's really tough to wrap around a bolt. Must be spring-steel?


It doesn't like to 'take' solder. It doesn't tarnish or rust. (???)


The black insulation resists scuffing, abrasion or even stripping.


It's so tough that it's very hard to break - or even to cut with wire dykes.

If anything could withstand being stretched 136 feet between trees and coated with ice to last a dozen winters, this should be it. It's 16 guage and hard to see from 50 feet away.

It's surely not nearly as well suited as copper for conductive properties but we used it in the Army for comm wire between field telephones and it's been used as such through World War II. It's really mean to work with - but it's hard to hurt it. Even in the worst conditions it lasts almost forever!

https://www.omahas.com/shop/communications-wire-spool/

Has anybody tried using this wire for an antenna? What'd you think after you got done? Was it worth the grief?

## Answer (score 3, by tomnexus)

Skin depth resistance on steel wire does bite a bit at low frequencies. Here is my calculation:

This handy calculator says that 60 feet of 16 AWG wire, at 3.5 MHz will have a resistance of about 2.5 ohms if it's copper, and 17 ohms if it's stainless steel. This is about 1/3 of the feedpoint impedance of the dipole, so it will have a neglegible effect on efficiency, less than 1 dB. That's before considering ground losses if the dipole is close to the ground. (I used 60 feet because the current is largest in the centre, and low at the ends, so using the full length wouldn't be appropriate).

Antennas are mechanical beasts first and foremost, and this wire sounds strong, corrosion resistant and hard to see. Most important, you already have a roll of it. If you can handle the challenge of making the connections, this wire sounds great for a dipole.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21094/is-army-surplus-steel-wire-suitable-for-an-antenna, by Dax, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
