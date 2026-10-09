# How thick should counterpoise wires be?

*Tags: antenna, antenna-theory, counterpoise, earth · score 4*

## Question

I would like to use a shortened whip antenna with a coil in it's base, e.g. OPEK HVT-400B. My transceiver maximum power is 100 W (and antenna's - 120 W). To make the antenna work I need counterpoise wires. As I understand using three 1/4 wavelength wires just laying on the ground in all directions with 120° between them is considered a good practice, or a starting point at least.

What I don't know is whether counterpoise can conduct a large current and thus I don't know how thick these wires should be. For instance, can I use thin wires from an Ethernet cable or a long USB cable? If not, what gauge is recommended?

## Accepted answer (score 3, by Phil Frost - W8II)

With only three radials, the wire you use is probably not very relevant. Although a smaller wire has a higher resistance and thus loss, with only three radials directly on the ground your losses will still be dominated by the resistive loss of the soil.

As a rule of thumb, a good ground requires at least 16 radials. It's not critical that they be exactly a 1/4 wavelength long, though as a rule of thumb they should be at least that long. Using a shortened whip makes the requirement for a good ground even more important, as the shortening increases the current and the resistive losses with it.

By the time you have 16 radials, the wire does not need to be especially thick since the current is distributed among each of them. Losses are proportional to the square of current, so each doubling of the number of radials reduces the copper losses by a factor of 1/4. But more significantly, more radials puts more of the current in the copper and less in the soil, which is a bigger win. I'd choose 32 radials of 30 AWG over 3 radials of 8 AWG for sure.

So use whatever enables you to put down a lot of radials. I would recommend nothing thinner than 14 AWG just for mechanical robustness, but if you want to keep things really cheap and salvage wires out of cat 5 or whatever, go for it.

## Answer (score 5, by Glenn W9IQ)

The purpose of the counterpoise is to provide an efficient means of conducting the return RF current of the antenna. In the absence of an efficient counterpoise, the current will return through the lossy earth or poorly quantified paths such as coaxial cable shields.

An efficient counterpoise will carry the same current as the primary radiating element. A quarter wave vertical antenna with an efficient counterpoise has a feedpoint impedance of ~34 ohms. We can use Ohm's law to calculate the current:

$$I=\sqrt{\frac{P}{R}} \tag1$$

where I is the current in amps, P is the power in watts and R is the resistance in ohms.

So a 100 watt transmitter fed into a 34 ohm antenna will result in ~1.4 RMS amps. When you have three counterpoise radials, the maximum current in each radial is 1/3 of the antenna current or ~0.47 RMS amps in this example. And generally this current density is dominant near the base of the antenna and becomes less as you move away from the base.

Before selecting a wire gauge, the construction of the wire must be considered. A pure copper wire is easier to analyze than a copper clad wire. In recent years, doorbell type wire, for example, has largely become copper clad. Because the specifications of the copper cladding is rarely published, you should shy away from cladded wires if you have other options since the steel core of the wire is quite lossy if the copper plating cannot carry the majority of the RF current.

Then finally, the gauge of the wire and the frequency of operation determines its losses. As the frequency rises, the current becomes more crowded on the surface of the wire due to skin effect. As an example, a 24 gauge copper wire that is 2.5 meters long (about 1/4 wavelength at 28 MHz) has a DC resistance of ~0.2 ohms but at 28 MHz it has an AC (RF) resistance of ~ 2.2 ohms. You can calculate the AC resistance for any wire size with various online calculators such as this one.

Since you are attempting to increase the efficiency of your antenna, a good goal is to keep the total AC resistance of your counterpoise to less than 1% of the ideal feed point impedance. From the earlier example, 1% of 34 ohms is 0.34 ohms. Since you are using 3 wires, each wire should be 1 ohm or less (0.34 * 3). So the 24 ga wire for 28 MHz would not meet this goal while an 18 gauge, or larger, wire would.

In general, more than 3 radials are desirable for a ground mounted counterpoise. You can see from the example, that as you install more radials, it is possible to also effectively reduce the gauge of the wire.

It has also been empirically determined that ground mounted radials do not need to be tuned to a 1/4 wavelength to be effective. Generally more shorter radials are better than a few 1/4 wave radials.

With all of this being said, don't suffer from analysis paralysis. Any radials of any gauge wire of any construction is generally better than no radials at all.

## Answer (score 2, by Mike Waters)

**Can you elevate the radials?** Two or three *properly installed* elevated radials can be just as effective as 120 on the ground!

By *properly installed*, I mean that they should be roughly 10 feet high **and** have an effective common-mode choke on the coax right at the junction of the radials and coax shield. **This junction MUST NOT BE GROUNDED**. Try and make the radials as symmetrical as you can in relation to the vertical antenna.

See this page about ground radials in general and this one with descriptions and photos of mine about 1/3 of the way down the first page.

Also, be sure and click on the relevant links on the first page.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12309/how-thick-should-counterpoise-wires-be, by Aleksander Alekseev - R2AUK, Phil Frost - W8II, Glenn W9IQ, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
