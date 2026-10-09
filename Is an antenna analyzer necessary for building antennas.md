# Is an antenna analyzer necessary for building antennas?

*Tags: antenna-construction, swr-meter, antenna-analyzer · score 13*

## Question

I'd like to try my hand at building a few antennas for VHF/UHF use. I'm going to be going approximately from established designs, but obviously the final result will require some tuning. I don't currently own either an SWR meter or antenna analyzer. Is an SWR meter good enough for what I want to do, or will an antenna analyzer be necessary for this? What are the benefits of an antenna analyzer in such situations?

## Accepted answer (score 12, by Kevin Reid AG6YO)

I've not personally built antennas from scratch, but I appreciate my antenna analyzer just for being a good instrument — making the invisible aspects of my antenna system visible.

Compared to using a SWR meter for the purpose, an antenna analyzer:


Displays more information.

A SWR meter still gives you *enough* information, in the sense that you can try things until they move towards 1:1 SWR, but it's a one-dimensional measurement: if you tried to adjust an antenna using it you're doing a “hotter colder” search, trying things until it improves.

An antenna analyzer will tell you resistance and reactance independently, which allows you to more directly understand the problem. For example, you can have an exactly resonant antenna, which simply has the wrong magnitude of impedance (you need an impedance transformer). On a SWR meter this can show up as the SWR having a minimum point but remaining well above 1:1. (That minimum point [is not necessarily the resonant point](What%27s%20the%20difference%20between%20minimum%20SWR%20and%20resonance.md).) On an antenna analyzer, you can immediately see that you've got R = 34 Ω instead of 50 Ω (or whatever), and build that correction into your balun.

High-end antenna analyzers can also give you measurements at multiple frequencies — either as a graph or individual readings at selected frequencies. A graph allows you to easily obtain measurements in the opposite direction — not “how suitable is this antenna at this frequency?”, but “what frequencies is this antenna good for?”, as well as other RF-electronics measurements like finding the resonant frequency of a circuit or the upper frequency limit of a ferrite choke.

In the above picture: my RigExpert AA-600 antenna analyzer displaying an impedance graph (it can also compute SWR from the same data). You can see directly from this graph that whatever it's connected to is resonant at the frequency at the middle of the graph (reactance crosses zero) and at that point has a resistance (and also magnitude of impedance) of 100 Ω.


Lets you use less transmitted power.

To measure the impedance of your antenna, no matter what instrument you use, you need a signal generator — a transmitter — somewhere. An antenna analyzer has a low-power signal generator built in.

If you use a SWR meter, you have to use a separate one; if you use your regular transceiver for the purpose, you're limited to its lowest power setting, which might be a few watts! Even if you have a lower power transmitter, it might not be sufficient to show a reading on the SWR meter, which has scales for much higher power levels.

By comparison, my antenna analyzer's output falls within FCC Part 15 emissions limits, so I'm much less likely to interfere with anyone else (and don't have to stop to identify myself, either).

## Answer (score 5, by Phil Frost - W8II)

An antenna analyzer is not necessary. Sure, it's handy. A VNA is even handier. For this equipment you're looking at something like $50 USD for a NanoVNA, up to many thousands of dollars for a lab grade VNA. If you just want to know if you need to trim a bit off a wire dipole or not, and simply get on the air without toasting your transmitter, none of these things are *necessary*. While there's a certain joy in being able to measure and quantify exactly how things are operating and make it all "just so", radios are in fact quite forgiving. An AC current *wants* to radiate. In fact, there's an entire industry around making things *not* radiate.

If you wonder how to make an antenna without these tools, you need only look to the recent past. It wasn't that long ago that we did not have solid state electronics, and test equipment like we have today was either very expensive, or nonexistent. Most of the methods used in those days to measure antenna impedance involve putting an antenna in some kind of bridge and comparing it against a known impedance.

Here's one example of a dead-simple approach:

You can read [the full question](Adapting%20an%20antenna%20coupler.md) for an explanation of how it works. It's not particularly sophisticated, but if you just need to trim your antenna until it's not a horrible match to 50 ohms, it will work just fine. If you have an SWR meter, you can also just adjust for minimum SWR and accomplish the same thing. Note you don't need the matching section (L1, L2, and C3) if you just want to measure impedance.

If you want to take the sophistication up a notch, you can use a grid dip meter. You can find them at any hamfest, or used on eBay or whatnot for some tens of dollars. Just a few decades ago, these were state of the art antenna test equipment. The physical laws that govern their operation have not changed, and they work as just well today.

As another step up, you can consider any number of used impedance bridges which are similar in concept to the schematic above, but have adjustable and calibrated inductors and capacitors so you can measure the complex impedance of the antenna. This is in effect what an antenna analyzer does, the only difference being that the antenna analyzer will automatically adjust the knobs for you, and maybe measure impedance at a range of frequencies at a push of button.

## Answer (score 4, by K7PEH)

I couldn't live without my two antenna analyzers -- I may even get a VNA (vector network analyzer) although that is not necessary for simple antenna analysis.

I own both the MFJ 259B and the Autek Research RX Vector Analyst VA1. Although both do roughly the same thing, they have a few different features and I will touch on a few of those.

Besides digital readout, the MFJ 259B also has an analog SWR meter which greatly helps in finding resonant spots on an antenna using a frequency sweep. You can watch if you are getting close or drifting away much easier than with digital readout.

You can measure capacitance and inductance with both but the MFJ259B does not give you the sign of the reactance. That is, negative for capacitance and positive for inductance. You can determine the sign merely by doing a small shift in frequency and seeing which direction the reactance swings (lower for capacitance if frequency shifts upward for example).

The Autek VA1 though includes the arithmetic sign of reactance so it is just slightly easier if you want a capacitance versus inductance readout.

So, whether you are building antennas for resonance or cutting transmission line to be a transformer, the use of either of these two analyzers makes it gut simple.

Postscript: I forgot to mention whether an SWR meter is any good? Well, it can tell you when you are really bad but it does not really help enough in my opinion. After all, a 50-ohm resistant dummy load gives an SWR of 1:1 but that does not say it is a good antenna. Also, by knowing the R and X values of the reactance, you are able to determine where problems might lie with an antenna. Remember that resonance is where it is purely resistive so $X=0$ or close to zero.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2477/is-an-antenna-analyzer-necessary-for-building-antennas, by David KF4MDV, Kevin Reid AG6YO, Phil Frost - W8II, K7PEH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
