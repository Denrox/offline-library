# A first homebrew design: Band, antenna, and ground wave propagation

*Tags: hf, diy, frequency, cw, link-budget · score 4*

## Question

I'm working on a very simple homebrew transceiver and request review of our selected band, antenna, and power.

**Background:** A child got very interested in ham radio, as an incentive for to earn his license *and* CW (way to go!), I committed to earn my license and design and build a simple CW transceiver with him. His (and my) interest is on the electronics side, understanding and designing RF rigs, more than the ability to talk with anyone around the world.

**Goals & Non-Goals:** *Simple* is the key word. This is our first RF design (though we've designed and built many analog and digital circuits), and we need to start small. So we've agreed on a well-defined goal:

Design and build two devices that can communicate with each other at small distances (10 km objective, 1 km threshold) through CW on the Technician licensed spectrum.

*Simple* means:

1. Simple to design. This is our first RF design.
2. Simple to debug.
3. Simple to build. Ideally all parts should be commonly available.
4. Simple to deploy. Large or antennas and power supplies are prohibitive. The rig with antenna needs to be transportable (though not necessarily mobile).

Working DX or even random QSOs are non-goals at this stage. That may come later. For now, we have a clear focus: talk to each other over short distances.

**Preliminary Design:** Based on those goals (and non-goals), we selected the following, to which I ask for review, feedback, and suggestions:

**Band & Antenna:** Since we'll need to use our DSO to debug, which has a maximum frequency of 40 MHz, the wavelength must be 10 m or longer (no VHF). 10 m also makes antennas much easier, makes minimal antenna height possible, and may allow mounting the antenna vertically (needed for good ground wave propagation). And although 10 m propagation is tricky, since we're focusing on short distance ground wave propagation, I believe 10 m should work well enough.

That being said, 40 m has a big advantage: At that frequency, we'll be able to test our building blocks on breadboards. (I assume that 28 MHz is too high frequency for breadboards, but 7 MHz is fine). And, the better ground wave propagation of 40 m may make up for a worse antenna. So, the question is:

Given our goals and constraints, is 10 m the right choice? Is there a small, simple 40 m antenna that, while perhaps performing poorly, will be good enough for us to communicate CW QRP over 1-10 km? At these distances, with a small antenna, will 10 m perform better (since the ratio of wavelength to antenna length, and wavelength to distance to ground, are both better) or 40 m (since 40 me generally has better ground wave propagation)?

Closely related is **power:** To keep the power supplies simple, and to minimize any safety concerns, this will be QRP. Ideally, I'd like to power it off a USB supply, 5V @ 500ma. Assuming 40% efficiency, that's 1 W RF transmit power.

Is 1 W of transmit power enough to achieve our goals? If not, what's an appropriate power supply and transmit power?

## Update

I've gotten several upvotes (thank you!) but no answers or even comments as of yet. So, I'll say:

1. If you have a partial response, please post it - even if only a comment.
2. If the question needs more information, please comment what else you'd like to know.
3. If the question is hard to answer, please let me know that, and why -- that itself will be helpful.

## Accepted answer (score 1, by Ryuji AB1WX)

Either 40m or 10m would work. 15m would also work. You probably have the most chance of making contact with strangers if you do 40m, less on 15m, and then the least on 10m, but a lot of magic happens on 10m.

A distance of 10km with 1W should be doable, but that is not a guarantee. You'll have to choose locations and antennas carefully to avoid disappointment. Direct line of sight is not required, but you don't want to have downtown buildings or a hill/mountain in between. The best places to test this is along the ocean. I operate portable on a park in the city of Boston. I operate on the fishing pier on the Atlantic, using a 1/4 wavelength vertical antenna, and I made a number of ground or direct wave contacts with stations in eastern Massachusetts and sometimes beyond. Stations with about 10km distance and also on the beach came in 599++. Subtracting 20dB (100W to 1W) would still get 559 or better. You want to use a good antenna, but 1/4 wavelength vertical with really good radials would be good enough. Also, the ambient noise level and the receiver sensitivity matter a lot. Urban areas are super noisy, so pick a flat and low population-density area for the distance test.

For 15 and 10m, there are 5.5m stainless steel rod antennas you can find on AliExpress for less than 30 USD each. There is also MFJ1979. Those work well. For 40m, I use Spiderbeam 12m HD mast and run a 18AWG wire along it. With 10W or 100W depending on the day, I made contacts with all over the world with those antennas. I also scored top in homebrew transceiver QRP contests (but that was 20m).

If you use a 1/4 wavelength vertical on all bands, you get the most ground wave propagation distance on 40m or, better yet, 80m. However, the ambient noise level increases as you go down the frequency. So, which is better for your criteria is a tricky question. However, as I outlined in the above paragraph, I don't think going down to 40m is necessary just to make a 10km contact.

Don't try to run the whole thing with a 5V supply. The final amp is best run on 9V or higher, because cheaply available transistors suitable for 1W to 10W range don't work very well with low supply voltages. (There are fancier transistors that work well with 7V, though.) If you are going 10m or 15m, I recommend searching for a CB final transistor (bipolar junction transistor). They are easy to use, and you can get 3-5W easily. The problem is that all those are discontinued, and most you find online are counterfeit, mostly junk. There are some alternatives that can substitute them. If you are going 40m, you can use BS170 MOSFET and a common class D amplifier. Logic gates can drive them. It's not too easy to get adequate gain and power using those fast switching MOSFETs on 15m and higher.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22708/a-first-homebrew-design-band-antenna-and-ground-wave-propagation, by SRobertJames, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
