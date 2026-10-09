# Marine VHF whip antennae - what are they?

*Tags: antenna, vhf, vertical-antenna · score 9*

## Question

For marine VHF (156~162 MHz), the most commonly used antenna is a 1/2-wave dipole or a collinear array in the form of a fibreglass rod. Collinear arrays are used to increase gain in some antennas. Dipoles/collinear arrays by their nature do not need a groundplane. This much I gather.

However, another popular type - especially with the sailing crowd - is the stainless steel whip antenna. Also supposedly a 1/2-wave antenna, it is roughly 1 m long.

The following page has examples of both types of antennas - AV7M is a fibreglass rod dipole, and AV53BIS3 is a stainless steel whip: http://www.comrod.com/category.php?categoryID=129

Further examples of stainless steel whips specifically:

- http://www.scan-antenna.com/product/vhf23
- http://www.glomex.it/shop/prodotti/diporto-antenne-marine/antenne-vhf/ra106slspb.html
- http://www.pacificaerials.co.nz/Marine/P6001VHF10mStainlessSteelAntenna.aspx
- http://shakespeare-ce.com/marine/wp-content/uploads/sites/4/2015/04/5240-r_5241-r_0.pdf

According to the datasheet and other information available on this type of antenna, the stainless steel whip is an end-fed dipole, and does not need any external ground plane.

The following page describes the concept of an end-fed dipole: http://www.aa5tb.com/efha.html The cylindrical base of the VHF whip then, it can be assumed, contains the LC matching circuit/balun(?) described.

We learn that the antenna doesn't work without a "counterpoise" - and it seems reasonable to assume that the VHF whip is in fact constructed similarly to Figure 15.

Further reading-up on counterpoises brings much confusion about their nature: http://www.antennex.com/shack/Dec06/cps.html

With this in mind:

- While several of the whip antennas referenced above are described as DC-open, whereas "Figure 15" is DC-shorted, is it possible that they are of a "Figure 15"-similar design? If not, then what are they?
- What is the nature of the (probably misnamed) "counterpoise" in "Figure 15" et al (which then, presumably, consists of the antenna's cylindrical brass base, feedline, and the radio equipment)? What is its role in allowing the standing wave/electrons-on-the-move in the radiating element to excite the E-field and, well, radiate?

Would also much appreciate references to literature that explains the physics of antennas in general and these types in particular, with sound scientific base without going deeply into the maths. Have had a hard time finding quality literature among the seemingly vast quantities of "black magic" antenna cookbooks.

## Answer (score 7, by Phil Frost - W8II)

Without having one of these antennas to disassemble (perhaps destructively), I can't tell you exactly how they are constructed. But maybe I can address some of your underlying concerns.

Firstly, *counterpoise*. In one sense, this is an elevated screen of wires designed to take the place of Earth. This sense developed with the Marconi antenna (what we'd probably call a "vertical") in the late 19th century.

In the other sense, *counterpoise* is the "other half" of the antenna. If charge is being removed from the antenna, then it is being added to the counterpoise, and vice versa. This must be so, due to the law of charge conservation. In this sense, the counterpoise may be the Earth, or radials, or the other half of the dipole, or the feedline, mast, tower, or whatever else may be connected or capacitively coupled to the antenna system.

Some people will tell you that one of these senses is wrong, but the fact is that "counterpoise" has no rigorous definition: you have to figure it out by context.

Now the trouble with end-fed dipoles is this: if you are putting charge into the antenna from the end, where are you getting the charge from? In a vertical we can take it from the ground and put it into the antenna, and in a center-fed dipole we take it from one half and put it into the other. But with an end-fed dipole, there's no "other" thing: there is no *counterpoise*.

In practice, the feedline or mast will become the counterpoise. Since you probably didn't intend for the feedline to have RF current all over it, you might want to do something about that. W8JI has a pretty good article on the subject. In summary, you may want to isolate the feedline with a transformer, but if you don't, it's not the end of the world. 25W transmit power probably isn't enough to cause arcing or RF burns no matter what you do. Without disassembling an antenna it's hard to say exactly what the feed and matching arrangement is.

However, it is pretty safe to assume that in all cases, the feedpoint impedance is high, and we need some way to make it lower to match 50 ohms. If the impedance is already purely resistive, then a transformer with the right turns ratio will do the trick.

But we can also accomplish a step-down in impedance with either:

- a parallel inductor + a series capacitor, or
- a series inductor + a parallel capacitor.

It's easy to see how this works on a Smith chart: if we start at 1000 ohms (the green dot) then there are two ways we can get to 50 ohms (the center):

Additionally, making the antenna a little too long, or a little too short, will introduce a reactive component to the feedpoint impedance. So it very well may be that a clever antenna designer can use this to take place of one of the components, and then achieve an acceptable match with just one other component.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5305/marine-vhf-whip-antennae-what-are-they, by user5314, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
