# Coax in the wall, or around the house?

*Tags: coaxial-cable, rfi, antenna-system, feed-line · score 4*

## Question

I am mounting a hex-beam antenna to the peak of my house (assuming that I can find someone with a cherry-picker or a scissor-lift that can help me get it up there). Right at that end of the house is an open vent into my attic, which is easily accessible. In addition to reinforcing the mounting location with 2x4s, I am wondering if I should run the coax from the antenna into the vent, and from there through the wall down into my basement. Back about 6 years ago, my first antenna was fed that way, but this was a G5RV with ladder line; this caused a lot of RF interference in other devices in the house, and I got a lot on receive also (for those who don't know, the feed-line for a G5RV antenna is ladder-line - window-line? - and is a radiating part of the antenna).

In the current case, routing coax inside the walls would be about half the coax length required if I were to route it around the house outside and then through the bulkhead fitting I have in my basement door. But can I expect inferior performance due to send/receive interference? Assuming no common-mode on the coax, is this a reasonable solution?

## Answer (score 5, by tomnexus)

Three things that matter here:

1. **Lightning!** You need to ground the coax *as it enters the house*.  
This is difficult if it comes in via a vent.

You should probably ground the antenna anyway, but you definitely want to take the coax outside, down to the ground, and **ground the outer of the coax** ususally with a flanged barrel connector, or a lightning arrestor. The primary thing here is to protect your house, and for that you don't want an ungrounded cable from high above the roof, coming indoors without being properly grounded first.

If you're in the US you probably have a coax cable for TV/internet, coming from the street, overhead. When it arrives at your house, it goes through a special grounding block, with a heavy gauge connection to ground, before entering the house. You want to do the same with the radio coax.

If the coax is not thick enough for the full lightning current, (RG58 and RG213 are too thin) then you should ideally run an appropriate earth wire in parallel with it (1 AWG Copper or 0 AWG Aluminium). This prevents it from becoming an incandescent fire starter when it's struck.

1.

**Cable losses** - at HF, with a low SWR antenna, the loss in the cable will be insignificant.

2.

**Balun** - To reduce RF in the house, caused by the coax (or ground lead) radiating, your beam should be fed with a balun. If not an actual transformer, then at least make an RF choke, winding the coax through an appropriate ferrite core. You could do this twice, once at the feedpoint and once a quarter-wave down the cable.

3.

**Lightning arrestor**  
Finally, if most of the lightning current has been diverted to earth,aA lighting arrestor may help protect your radio from large differential voltages on the cable. It needs to be properly grounded - install it at the entry point, where you connect the coax to ground.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22180/coax-in-the-wall-or-around-the-house, by Don Levey, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
