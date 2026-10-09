# Measuring effectiveness of vehicle bonding

*Tags: hf, mobile, measurement, bonding · score 3*

## Question

Is there any objective way to measure the effectiveness of your bonding in a mobile HF setup? Or determining when you have "adequate" bonding? I have a hard time with just throwing straps on blindly and hoping they help

## Accepted answer (score 2, by tomnexus)

The main goal of bonding the vehicle panels together is to increase the effective size of the ground plane, to improve antenna efficiency.

It also has the benfit of reducing coupling to the vehicle electronics, which could possibly be affected by high power transmissions (though they are tested to quite large field strengths already, so that cars don't stop working near police vehicles or MW transmitter sites). It reduces pickup of noise from the vehicle ignition, alternator and motor brushes, and electronics. Bonding should also reduce the RF exposure of the people inside the vehicle (which probably doesn't matter at 100 W power levels) and to the radio mic lead (these can be surprisingly sensitive to RF, considering they're designed to be connected to a radio transmitter...)

The simplest way of measuring change in ground loss would be *measure the SWR bandwidth* of a simple whip antenna, including its base load, at 3.5 MHz or 7 MHz. Try this before and after connecting the bonding straps. Park the car outside on the bare dirt (or any unreinforced surface).

Tune the antenna for the ham band, and using a VNA or SWR meter, measure the frequency range over which the antenna SWR is less than (say) 3:1. Then re-connect the panel bonding straps and measure it again.

If the antenna goes from 1% to 2% efficient because of the panel bonding reducing the coupling to the ground, then the bandwidth will be about half as wide. The actual bandwidth available will be affected by other things - the base inductor design, the type of ground you have, etc.

Use a whip with a simple fixed inductor base load. An ATU might choose to include some parallel L and C for a better match, which would muddy the results as it's different every time.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21129/measuring-effectiveness-of-vehicle-bonding, by Brad Mace, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
