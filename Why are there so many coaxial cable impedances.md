# Why are there so many coaxial cable impedances?

*Tags: coaxial-cable, impedance · score 10*

## Question

Why do we have 50, 75, 62 and 92 Ω coaxial cable, to name a few? Why not just one standardised cable? Is there some technical reason or did Mr. Coax and Mr. Cable have a disagreement, like Mr. Tesla and Mr. Edison?

## Answer (score 5, by Brian K1LI)

RF Cafe cites quotes Harmon Banning of W.L. Gore & Associates, Inc.:

In the early days of microwaves, around World War II, impedances were chosen depending on the application. For maximum power handling, somewhere between 30 and 44 Ω was used. On the other hand, lowest attenuation for an air filled line was around 93 Ω. In those days, there were no flexible cables, at least for higher frequencies, only rigid tubes with air dielectric. Semi-rigid cable came about in the early 50s, while real microwave flex cable was approximately 10 years later.

Somewhere along the way it was decided to standardize on a given impedance so that economy and convenience could be brought into the equation. In the US, 50 Ω was chosen as a compromise. There was a group known as JAN, which stood for Joint Army and Navy who took on these matters. They later became DESC, for Defense Electronic Supply Center, where the MIL specs evolved. Europe chose 60 Ω. In reality, in the U.S., since most of the "tubes" were actually existing materials consisting of standard rods and water pipes, 51.5 Ω was quite common. It was amazing to see and use adapter/converters to go from 50 to 51.5 Ω. Eventually, 50 won out, and special tubing was created (or maybe the plumbers allowed their pipes to change dimension slightly).

Further along, the Europeans were forced to change because of the influence of companies such as Hewlett-Packard which dominated the world scene. 75 Ω is the telecommunications standard, because in a dielectric filled line, somewhere around 77 Ω gives the lowest loss. (Cable TV) 93 Ω is still used for short runs such as the connection between computers and their monitors because of low capacitance per foot which would reduce the loading on circuits and allow longer cable runs.

## Answer (score 5, by Kevin Reid AG6YO)

Glad to see this question posted! This has a really interesting answer which I'm not qualified to write a comprehensive answer to, so here's a rather unsupported answer to help you along until someone writes a better one.

There are several reasons why coaxial cable is used in several different impedances.


On basic principles: if a device on one end of the cable inherently has a specific impedance, then using a cable matched to that impedance means you don't need a matching network at least at that end.


Different choices of impedance result in different characteristics of the cable, given the available choices of material and construction techniques.

It is said (I don't have a citation) that 50 Ω was chosen as a compromise between power handling capability (lower impedance would be better) and attenuation per length (higher impedance would be better). In high-power applications, 50 Ω is used to allow use of the smallest cable possible for the power (minimizing cost and bulk).

On the other hand, if you are not intending to transfer significant power, i.e. your application is very low-power or receive-only, then you only care about attenuation and so you choose the higher 75 Ω to optimize for least attenuation.


Even if there was one best line impedance to use, you would still want to have available cables of other impedances. This is because RF circuits that use transmission lines as impedance transformers don't need any *specific* impedance, but they do need to have an impedance that is *different than the impedance of the incoming/outgoing lines*. For example, in this Wilkinson power divider implemented using coax:

*(Image credit: SpinningSpark on Wikimedia Commons)*

If your lines are 50 Ω then you need 71 Ω in the divider. If your lines are $x$ Ω then you need $\sqrt{2}x$ Ω in the divider. No single type of coax can do this.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14765/why-are-there-so-many-coaxial-cable-impedances, by R Johnson, Brian K1LI, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
