# Using NanoVNA to tune antenna

*Tags: wire-antenna, coaxial-cable, antenna-tuner, portable, nanovna · score 4*

## Question

I'm extremely new to this, so I'm mostly asking for tutorials and so on.

I have tried configuring the device according to one tutorial I found. When I hook up the cheap antennas that came with a couple of my radios. I could see the attenuation dips at the 2M band, and 70cm Band, but would like to check the SWR as well.

I am going to be building a "mantenna" (when I was deployed we used lengths of stripped coax woven into our gear as antennas, hence the name).

Since my body will attenuate the signal, I plan to thread extra long wire through my gear, and use the NanoVNA to trim the cable bit by bit to tune it to my needed frequencies in realtime.

I would love any pointers to tutorials, or walkthrus anyone could recommend.

73 KG7PLF

## Accepted answer (score 4, by Lou-in-USA)

Jesse Knott, I am not sure by what you mean when you say you "see attenuation dips" on your Nano-VNA, unless you are talking about the LogMag function. For your purposes I'd do your evaluation using the Smith Chart and SWR functions. I can say that I'm not a fan of having an antenna near your body, but if that's the case, you will probably be capacitively loading the antenna, which means you'll need to add inductive reactance, which can likely be achieved by keeping your radiator and counterpoise a little longer than what a conventional formula would calculate Online dipole calculator for you. If you are doing a stripped coax antenna, you should put a choke at the appropriate distance from the feed-point, either coil the coax, or use a ferrite, otherwise you will have a significant amount of RF current returning to your radio via the shield side of the coax. This is less of a problem if you strip back the coax and seperate the shield and center conductor and make a "dipole" (without a BalUn, this is really a counterpoised 1/4 wave antenna, but people call it a dipole), and again if you don't use a BalUn, place a choke at the feed-point (where the shield and center conductor seperate). Whatever you do, you will likely have to wear the clothing while testing to get a proper handle on the SWR and resistance-reactance of your setup.

Remember that with the "dipole" setup, you have more control of your feed-point resistance since resistance is adjustable by the angle of seperation between the two elements. Your best mode to carry out testing is the Smith Chart function. Online Smith Chart Tool Setup the Nano VNA to do a sweep of the frequencies you want your antenna to be used on, and see the results. The first thing to do is get the antenna to resonance in the middle of the range of frequencies you will want it to work on. "Perfect" resonance is when your sweep spiral crosses the impedance and admittance line (center line) of the Smith Chart. Once resonance is established on your "center frequency", you can go about getting your resistance to the impedance you need, presumably 50 Ohms. If your impedance at your "center frequency" is greater than 50 Ohms, you can narrow the angle between the dipole elements, if your resistance is too low (less than 50 Ohms), and you're already at 180 degrees of element seperation, you can increase the length of the radiating element and shorten the length of the counterpoise, making in essence, an off-center-fed dipole. I'd guess this will be a tedious process considering you're wearing the antenna, so you may have to settle on something close. Another thing to keep in mind is that your maximum current will be at the antenna's feed-point, this is where most of the RF radiation will occur, conversely, at the ends of the antenna elements will be where your voltage maximas will be, so make sure you cap the wire end (of at least the center conductor, or both if you're using a BalUn) so you don't get tingled when transmitting.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21888/using-nanovna-to-tune-antenna, by Jesse Knott, Lou-in-USA. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
