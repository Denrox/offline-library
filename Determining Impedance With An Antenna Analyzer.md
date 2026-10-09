# Determining Impedance With An Antenna Analyzer

*Tags: antenna-theory, balun, impedance-matching, measurement · score 5*

## Question

I need some help interpreting some information from my antenna analyzer (RigExpert AA-35). I want to use the information to impedance match my AM receiving antenna system to AM radios. No transmitting, just receiving. The data was captured at the point just before the feed-line enters the radio. 75Ω coax is used & was programmed into the analyzer. Here is the data that the analyzer provided:

1. Freq in kHz = 511.2
2. SWR = 2.62
3. RL dB = 6.98
4. Z (Ω) = 167.19 - j63.91
5. |Z| (Ω) = 178.99
6. |rho| = .045, phase = 19.95 (Degrees)
7. C (pF) = 4871.47
8. Zpar (Ω) = 191.62 - j501.28
9. Cpar (pF) = 621.08
10. 1/4 Cable Length = 317.47'

***Q1:*** *How do I convert the above data to provide the impedance of my antenna, at this point, for this tested frequency?*

***Q2:*** *Then, how many ohms, increase or decrease, would be required to “transform” from the antenna impedance, so it becomes the 75Ω expected for input to the radio?*

How these two answers are arrived at using the figures provided by the analyzer and the known requirements of the radio would be most helpful, so I understand the process.

I was under the mistaken impression that this impedance number would be provided in ohms by the analyzer in the same simple manner in which say the SWR is given. Trying to learn this process and hoping that being provided “how” this answer is achieved will help me understand how to use the analyzer for this purpose.

Just for reference, the antenna is an “IP33 MIni Whip Antenna”. Connected to 75 Ω coax. Connected to the systems small power amp for the whip (Unplugged). Connected to another short length of the 75 coax. The analyzer was at this point connected to the system. The same point where the antenna lead is converted to enter the back of the radio. I have measured at other points in the system. Just used this point as the example.

This question is not really about location placement of any actual transformer or Balun or Unun that might be installed. I am just using the above example to understand the impedance data acquisition and conversion for use in impedance matching. Thanks!

## Answer (score 5, by Kevin Reid AG6YO)

How do I convert the above data to provide the impedance of my antenna, at this point, for this tested frequency?

"Z (Ω) = 167.19 - j63.91" *is* telling you the impedance. The impedance of your antenna is $(167.19 - j63.91)$ ohms.

Then, how many ohms, increase or decrease, would be required to “transform” from the antenna impedance, so it becomes the 75Ω expected for input to the radio?

That's not how impedance transformation works. You need a matching network, which may contain inductors, capacitors, transformers, chokes, transmission lines, or all of those. Impedance matching is a two-dimensional problem, just as we measure impedance as a complex number with two components.

Furthermore, we don't want to add ohms in the form of a resistor, because while that *would*, technically, be able to help match the impedance (e.g. in the simple case where the antenna's impedance is too small), it would not improve the signal to the receiver, but merely throw away some of it (dissipated in the antenna).

There's many different ways to design matching networks; I should really link to an introduction to the topic here but I haven't found a good one at the moment.

## Answer (score 4, by Phil Frost - W8II)

Firstly, an SWR of 2.62 is probably acceptable for a receiver, and no additional matching is necessary. See [What is the relationship between SWR and receive performance?](What%20is%20the%20relationship%20between%20SWR%20and%20receive%20performance.md)

Also, the IP33 Mini Whip Antenna is an active antenna, meaning it has a preamplifier built-in. Antenna analyzers are good for looking at passive antennas, but looking into a preamplifier may not tell you anything about the preamplifier's output impedance. For that it would be best simply to consult the manual. In any case, that you're using an active antenna only reinforces the notion that matching isn't required here.

But let's say you did want to match this impedance, if only as an exercise. You don't need to calculate the impedance, because the analyzer shows it directly:

Z (Ω) = 167.19 - j63.91

That's the impedance seen by the analyzer, which will also be the impedance seen by receiver. This is looking at the antenna, through the feedline. Your objective is to add some matching network to change that to some target impedance, probably 75+j0 or 50+j0.

There are many ways to design such a matching network, but perhaps the most intuitive is using a Smith chart. I suggest trying an interactive tutorial to get some intuition for how it works.

## Answer (score 4, by Brian K1LI)

Thanks for following up on your [earlier question](RigExpert%20AA-35%20-%20Interpreting%20The%20Information.md).

All of the data you provide in your question represents the impedance the analyzer "sees" at the point you measured it. There is no need to convert anything, it's all there, the challenge is how to use it.

Because the impedance you measured at the transmitter end of the feedline to your antenna includes both resistance (167.19$\Omega$) and reactance (-63.91$\Omega$), "how many ohms, increase or decrease" doesn't fully describe the process by which you transform it to the 75$\Omega$ (resistive) output impedance of your rig. Instead, a network of inductors and capacitors must be designed to perform the required transformation.

A two-element "L" network is a simple circuit to accomplish the transformation. The easiest way to obtain the L-network values may be to use one of several calculators available on the internet.

For example, let's use this calculator. From the data in your question, we enter the following information:

which produces the following results:

Your matching network looks like this:

Using SimSmith to plot this transformation on a Smith chart:

shows that the L-network provides a nearly perfect match to your transmitter.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13181/determining-impedance-with-an-antenna-analyzer, by B. Varner, Kevin Reid AG6YO, Phil Frost - W8II, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
