# Parameters needed to calculate inductor value to achieve proper phase delay?

*Tags: antenna-theory, antenna-construction, vertical-antenna · score 6*

## Question

I'm thinking about trying a coil in my collinear 5/8λ antenna, instead of the 3/8λ phasing delay line between the lower and upper elements pictured below.

I figure that a coil with a certain inductance could give me a current delay of nearly 90° and the remaining 45° might be achieved by the overall length of the wire used for the coil turns. (Please correct me if I'm wrong about any aspect of this thought process.)

So if I'm not off base on the previous idea, then my question is, is it crucial to use a specific value of inductance so there is an impedance match between the top of the lower element to the bottom of the upper element, and would the impedances between those two elements be different? Does the coil have to be of a value that helps the impedance mismatch? I'm using MMANA-GAL to model the design, but I can't find any way to see what the impedance values are at any of the given segments.

And since the inductance phase calculator https://www.translatorscafe.com/unit-converter/en-US/calculator/series-rl-impedance/ asks for the series resistance of the circuit, I'm not sure what value to use in this formula?

## Answer (score 2, by rclocher3)

I'd never heard of an inductor being used for phasing in an antenna, and it sounds like an interesting idea. The inductance of your phasing coil would definitely affect the impedance matching between the sections and also the phasing.

I thought about modeling this antenna, and I was wondering how to start. Should the phasing coil be a "lumped" component, i.e. just an inductance, or should it be included in the model as a physical coil? I'd probably start by attempting to calculate the required impedance by modeling the antenna in SPICE, specifically LTspice, as an RLC series circuit with each antenna section modeled as a resistor and a capacitor, with the phasing coil in the middle. The inductance could be adjusted to make the antenna resonant. Then I'd try modeling the antenna in antenna modeling software with the phasing coil as a lumped component.

By the way, to get the impedance of the two radiating sections, I'd model each one with antenna modeling software as an end-fed antenna, located in space where they would be with the complete antenna. In other words, take your existing antenna model, remove everything else, and end-feed it.

But thinking more, I realize that this is not a simple antenna. Not only is the impedance of the phasing coil important, but so is its physical length. A real-world coil won't have the inductance predicted by the formula, because it's not a coil in free space, it's part of a radiating antenna. One might want to adjust the lengths of the radiating sections to work better with the coil. In other words, there are many variables to adjust for a successful design.

So I did some research on the web, and I discovered that the late, great L.B. Cebik, W4RNL, analyzed this antenna in an article titled "The Case of the Curly Collinear". I'd link to the article, but I know that before he died, L.B. sold the publishing rights to his articles to AntenneX, which was an online magazine. (L.B.'s old site cebik.com and Antennex's web site are both gone.) The articles have been republished in several places on the web, but as far as I know, these sites are pirating copyrighted content, so I won't link to the article here. Anyway, L.B. has already gone over this ground, and the article makes fascinating reading. L.B. shared his NEC files along with his articles, so the NEC files he used to develop the article may be available.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20367/parameters-needed-to-calculate-inductor-value-to-achieve-proper-phase-delay, by Louis Seaman, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
