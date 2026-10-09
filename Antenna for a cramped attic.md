# Antenna for a cramped attic

*Tags: antenna, vhf, antenna-system · score 8*

## Question

Brand new Ham. I bought a cheapo UV5 right before I got my call sign. I want to set up a decent 2m/70cm station for starters and I realize that a better radio is important but wanted to knock out the antenna situation first.

I live in HOA hell so no outdoor antennas, and to make matters worse, I am working with a 60 foot length / 36-40 inch height attic space. The good thing is my room/ham shack sits below the largest part of the house so I would only be looking at a — at most — 30 foot run to the antenna.

Any recommendations on DIY or for purchase antennas would be much appreciated. Any recommendations on type of cable to run (RG8/RG8x/LMR-400)? I'm looking for really good results to get started without a huge investment — I may be dreaming on this one.

## Accepted answer (score 5, by Kevin Reid AG6YO)

Your attic is pretty low but not quite low enough to be a problem for installing a vertically polarized 144 MHz antenna. There are two common antenna designs that would suit your case:


Ground plane antenna.

This simply consists of a vertical quarter-wavelength element (stiff wire or rod) sticking up from a horizontal ground plane (sheet metal, as big as you can make it). You can either make it entirely from scratch, or get an antenna intended for vehicles (magnet or through-hole mount) and supply your own sheet metal surface (if you don't have metal supply handy, buy a steel cookie sheet).


Vertical dipole antenna.

This consists of two quarter-wavelength elements, one above the other, fed from the center. Your roof is *just* high enough that you'll be able to fit one in in the full height.

The most straightforward way to feed a vertical dipole is to run coax *horizontally* to the center (feed point); the coax must not just dangle next to the lower element. Alternatively, you can [run the feed line inside the antenna, coaxially](Handheld%20Dipoles.md).

A vertical dipole is an uncommon antenna because it's taller than most and because it either requires a sideways bit sticking out or more complex construction. You'll probably have to make it from scratch, but that's easier since (for the horizontal feed) all you need is plain wire and a way to support the ends and join to the coax in the center.

Ideally, your antenna would be cut to exactly the right length to present a 50 Ω impedance (1:1 SWR) to the radio, but HTs are built to deal with compromise antennas (short ‘rubber duckies’), so it'll work fine, just not quite as efficiently. But if you know a friend with an antenna analyzer, have them bring it over to test while you trim the antenna to length.

In either case, if you are planning higher-power operation, or in general for best results, you should install a *choke balun* at the feed-point (except for the coaxial vertical dipole which does not need one). This ensures that the part of your system which actually radiates/receives is the part in the attic, not the rest of the cable.

The simplest possible design is simply taking some extra length of cable in your feed line and coiling it into a tight neat helix (use a piece of plastic pipe as a form) as if you were making an inductor. Don't bend coaxial cable too tightly — check the specifications!

Finally, for your choice of coaxial cable: look up its specifications, find the loss (given in dB per some length at a particular frequency), multiply that by the length you'll be using (check your units!), and decide if that loss is acceptable.

For example, if you paid the price to install some LMR-400 which specifies loss as 1.5 dB/100 ft at 150 MHz, and your run is 30 feet long, then your actual loss is:

$$ \frac{1.5\,\mathrm{dB}}{100\,\mathrm{ft}} \cdot 30\,\mathrm{ft} = 0.45\,\mathrm{dB} $$

And to convert that to a power ratio we calculate $10^{-0.45/10} = 0.902$. So however much power your transmitter puts out, you're losing a tenth of it in the coax. That's quite good. If you use lesser coax, you'll have worse results, but even, say, a 3 dB loss is not really a big deal.

(Note that the actual loss will be worse than this insofar as your SWR is poor, because standing waves mean reflections mean the signal traversing the cable more than once.)

## Answer (score 2, by William Oliver)

I'm using a 5/8 wave 2m mag mount on a 2'x 2' piece of sheet metal in the attic. I live in NW New Jersey on a small hill and reliably hit repeaters 50-60 miles from me.

## Answer (score 2, by rclocher3)

The antennas that Kevin AG6YO describes are single-band antennas. If there aren't many 70cm repeaters in your area, then a single-band 2m antenna should work fine. However, if there are 70cm repeaters where you live, then you might want to think about dual-band antennas. Antennas designed for 2m will often radiate on the 70cm band with an acceptably-low SWR, but with a poor radiation pattern that avoids the horizon, where the repeaters are. If both bands are important to you, then you might consider a dual-band antenna.

I recommend a dual-band J-pole antenna as designed by Ed Fong, WB6IQN, described in a QST article from February 2003. I homebrewed one myself and learned quite a lot about antennas that way.

I must warn you though, it's a fairly advanced project for an antenna homebrewer: I had to accurately measure the velocity factor of a transmission line, completely understand the theory behind a J-pole and how this design was made to work efficiently on both bands (oh so clever!), understand the theory of transmission lines including shunts and stubs using Smith charts, and raise and lower the antenna many times while making measurements during construction. I borrowed an expensive antenna analyzer that works on both bands. The 2m part was fairly simple to build, but the 70cm part required sub-millimeter precision. I probably put 10 hours into the build, but as I said I learned quite a lot about antennas doing so.

But if you just want to get on the air, you can buy one of these antennas from the designer himself on eBay for a very reasonable price: just search for "dual-band J-pole", and click on the listing that mentions Ed Fong. By the way, Ed's design is mounted in a PVC pipe. Of course you could put it in the attic, but also I would think that there are many ways to disguise a PVC pipe outdoors so that neighbors would never suspect that it's an antenna.

If you're curious about the theory, a J-pole antenna is an end-fed vertical dipole. End-fed dipoles have a high impedance, so the J-pole includes a matching network to make the impedance 50 Ω. Being a vertical dipole, it doesn't need radials or a ground plane. It should be used with a choke balun, usually made from eight to ten turns of coax around a suitable form, such as a piece of PVC drain pipe 4 inches / 10 cm in diameter. (Be sure to respect the minimum bending radius specified by the coax manufacturer.) Because this particular vertical dipole is end-fed, instead of being fed in the middle, the coax doesn't need to be connected perpendicularly to the middle of the antenna; the coax conveniently connects to the end.

People often build (single-band) J-poles out of copper pipe; the antenna then looks like a letter J, that is two parallel vertical lines, one short and one tall, connected at the bottom. The tall part of the J is the half-wave vertical dipole plus an approximately quarter-wave matching section, and the short part is the *nearly* quarter-wave matching stub.

A dual-band J-pole makes an excellent 2m and 70cm antenna, but there are lots of other ways you could go. There are several commercially-made dual-band antennas that would serve you well. A dual-band antenna made for a car would need a ground plane such as a large piece of sheet metal, so I'd recommend a dual-band antenna designed for home use instead. If you're determined to homebrew antennas, but you want both bands, but you want a simpler antenna than Ed's design, then you could homebrew two single-band antennas and connect them together with a duplexer.

I think you're taking the right approach to get the antenna right first, and then worry about getting a better radio later. Good luck and have fun!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6611/antenna-for-a-cramped-attic, by ThaKidd KG5ORD, Kevin Reid AG6YO, William Oliver, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
