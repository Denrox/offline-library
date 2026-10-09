# How to make a ferrite bar antenna for RTL-SDR?

*Tags: antenna, antenna-construction, rtl-sdr, ferrite · score 7*

## Question

I bought a RTL-SDR (blue one with little MCX antenna). I modified its Q branch, and can receive short wave radio with Degen 31MS antenna now. For MW, Degen 31MS antenna has a ferrite bar antenna coupler to work with the internal antenna of the radio. I don't have a ferrite bar antenna. How can I make a ferrite bar antenna for RTL-SDR?

## Accepted answer (score 2, by Avid Coder)

Looking at an Amazon listing, it appears that the Degen 31MS active antenna has three ways to connect to a radio. The first is via a direct ANT jack, the second is via clips to existing wire (likely telescoping) antennas, and the third is some sort of ferrite bar coupler that you're mentioning. A brief search didn't bring up a user manual or anything like that (link?). My guess of what their coupler is, without anything physical in hand to examine, and without any documents to support, is that it's an external ferrite bar with a number of copper wire turns wrapped around it, to be placed over the location of the internal antenna of your radio receiver to couple signal into the receiver. A quasi-transformer, if you will.

To make something like that is fairly simple - all you need is a ferrite bar. Where would you find one? Well... many old AM/FM clock radios or the like used these bar antennas for reception. Take one apart and you'll probably find one. Simply connect up the two ends of the coil to the leads from your Degen, and off you go. Or just buy a bar and a spool of copper wire, and start winding.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12169/how-to-make-a-ferrite-bar-antenna-for-rtl-sdr, by jac123, Avid Coder. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
