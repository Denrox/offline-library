# Coax braid acting as power supply ground between radio and amplifier connected to the same supply, is this a problem?

*Tags: amplifier, dc-power, battery · score 4*

## Question

I have a Kenwood TH-D72 and I just got an old Radio Shack HTA-20 2m amplifier to use with it. They're both powered from a sizeable 3S2P Li-Ion battery pack and they work great together for the most part, but I recently noticed something odd. I connected a meter to measure the current draw of the amp, and with it turned off it still seemed to be drawing about 100mA. After a bit of head scratching as the amp has a physical power switch and so shouldn't draw anything when off, I concluded that when they're both connected to the same battery the radio must be getting a much lower resistance connection to the power supply ground/negative through the coax braid and the 12 gauge wire I've run to the amp than through its own comparatively dinky power lead; when I unplug the radio from the shared external battery or disconnect the coax from the radio to the amp, the current draw at the powered-off amp goes away.

Using the coax as a power supply lead just doesn't seem like a good thing to me, but is this really a big deal? The amp starts acting up when the battery gets below about 10.7V in this configuration, which is what got me hooking up meters and testing things in the first place, but it does the same thing when the battery gets a bit lower even when the radio is running on its internal battery, so I think this amp just doesn't handle undervoltage well and the extra voltage drop to the amp when its cabling is also partly powering the radio (which itself pulls a couple of amps on TX) causes it to misbehave sooner.

So, do I need to stop the radio from using the coax braid as its primary negative power supply connection and if so, how? Some sort of balun/unun/other transformerish isolator?

Thanks!

## Answer (score 7, by Phil Frost - W8II)

If I understand the description correctly:

If that's all it is, I wouldn't say it's any big deal. Whenever you have multiple paths to ground, current will split between them. It's these currents that keep "ground" approximately the same voltage everywhere: an essential assumption in the design of most electronic equipment.

Some DC on the coax won't cause any issue. In fact putting a DC bias on coax is a common way to power an active antenna.

It could be the power leads for the radio are simply too light. The ground lead may not be a problem since the coax provides a low impedance connection, but the positive lead is equally small. Try eliminating the coax by attaching a dummy load to the radio. Then while transmitting, compare the battery voltage to the voltage at the radio's terminals. It shouldn't drop more than a volt, preferably less. You can also multiply that difference times the supply current and calculate the power wasted in the power leads, which might be of concern if you're trying to maximize the battery life of this station.

Out of an abundance of caution, I should also mention the possibility that this current has some more dangerous origin involving a fault in your mains wiring. You didn't describe anything not powered by the battery, but if you have for example a connection from the radio to a computer, and there's a ground fault in the computer, that ground current you are measuring could be the only thing keeping the chassis of your equipment from being an electrocution hazard. It's unlikely but possible, so be careful.

## Answer (score 4, by Kevin Reid AG6YO)

An anecdote: I had problems with my station which included computer-radio interconnections; some of my devices (RTL-SDRs) would lock up when I powered on my Yaesu FT-897. I eventually tracked this down to the power-on inrush currrent of the radio passing through coax shields and the chassis of the antenna switch that both were connected to.

I solved the problem by replacing the fuse (an element with resistance, after all) in the negative power lead of the FT-897 with a jumper (keeping the fuse in the positive side). This way, the negative power wire's impedance has been reduced compared to the paths not intended for power.

So, the above is an example of one kind of problem that can happen, and a general precaution to take:

- Make sure your power wires are fat and securely connected.
- Make sure there is no way to have a positive connection without a negative.
- Don't use an ammeter or current shunt on the negative lead, except where there is no other negative-side path (e.g. the battery terminals, or an otherwise-isolated load, but not interconnected components). Not only will it cause shield currents, it will read inaccurately since some current is bypassing it.

Adding galvanic isolation by a transformer ("voltage balun" in this context) could work, and will completely eliminate rather than reduce the stray current, but would be an expensive and heavy component (typical baluns are "current baluns", which do not isolate, because that way they can avoid needing a magnetic core sized for the full RF power being carried). I've never heard of someone using one.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16446/coax-braid-acting-as-power-supply-ground-between-radio-and-amplifier-connected, by MoTLD, Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
