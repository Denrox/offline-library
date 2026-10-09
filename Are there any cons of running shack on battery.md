# Are there any cons of running shack on battery?

*Tags: power-supply, dc-power, battery · score 5*

## Question

I'm building a low-power shack to operate on non-licensed bands (UHF PMR 0.5W + HF CB 4W). I don't have any "RF-grade" sources of 12(-ish) volts and don't want to buy a specialised power unit.

I'm thinking of running the whole setup from a 12V battery (VRLA / NiCd / LiPoFe4).

**Here're my thoughts; am I missing something?**

### Pros

- Cheaper than a dedicated RF-grade power supply (USD30 for 40 Ah car battery)
- No interference from AC mains and/or cheap power supply
- Safer: no risks of electric shock (no AC mains on my table)
- Lightning safety: the equipment is not connected to the house AC, so potential bolt would only damage the radios
- No need to re-wire mains / use lengthening cable if I decide to move table
- Blackout proof :)

### Cons (with my refutal ;)

- Runtime *[not a problem, I do not expect avg drain to be much more than 1A, so even a small car battery would give me over 20 hours, more than enough]*
- Need to charge *[I'm not operating the rig 24/7 so not an issue]*
- Voltage drop when battery is not fully charged *[might be small, depending on chemistry... and actually, cheap power supply that I'm using now drops from 12V when idle to 10V when Tx'ing, and the radio is still working]*
- Safety issues with large batteries sitting alone and unsupervised *[I will disconnect it every time and can stove it in shed when I'm away]*
- Limited lifespan of batteries *[before the battery would die of old age/overuse, I'd either lose interest or decide to build something bigger anyway :)]*

## Answer (score 7, by Phil Frost - W8II)

I don't mean to talk you out of the idea, but I suspect the advantages are not nearly so great as you imagine.

Cheaper than a dedicated RF-grade power supply (USD30 for 40 Ah car battery)

I don't know about that. While there are certainly people selling "RF-grade" supplies at high prices because there are people that will pay, we're not talking about a power supply for the first manned interplanetary mission here. Power supply requirements for RF are not especially stringent and any generic supply will do. The only requirement is it isn't terribly noisy.

Any linear supply will have nearly no noise. A quick search for "12V linear supply" turns up plenty of candidates for about $30 USD.

Most switching supplies are also fine. The very cheapest kind may not have sufficient filtering. Otherwise, the noise remaining after the built-in filtering in the supply and your radio is unlikely to be noticeable among the thousands of other switching supplies in a typical environment, and it's cheap to add a little more filtering, if required.

Also keep in mind also car batteries are designed for short, high-current loads to start the car. They will not last long if they are repeatedly discharged. You will want a "deep cycle" battery or some other chemistry which is designed to be charged and discharged.

Safer: no risks of electric shock (no AC mains on my table)

Dubious. You probably use AC appliances all day (including to type this question) and don't give it a thought. Between device testing, electric codes, and inspections, AC is pretty safe.

A 12V battery might not pose much of an electrocution hazard, but it can start fires if shorted, rupture and spew corrosive chemicals, or emit hydrogen gas which can accumulate in a building and explode. Will you have your installation inspected? Will you submit your designs to a testing facility?

Lightning safety: the equipment is not connected to the house AC, so potential bolt would only damage the radios

A battery-powered shack certainly avoids some of the more [blatant problems](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md), but don't assume because your house isn't connected it's now immune. It's still connected, through the soil.

And besides, now you have the additional hazard of a battery fire if you forget to disconnect the battery.

No need to re-wire mains / use lengthening cable if I decide to move table

Indeed, or even if you decide to put the entire station in the car.

Blackout proof :)

Absolutely. Furthermore, you'll be surprised how much lower the noise floor is when all your neighborhood's RFI sources are switched off. A blackout can be a great time to get on the radio.

## Answer (score 5, by tomnexus)

Possibly an issue with your HF CB rig is that the output power will be lower at 12.1 than at 13.8 or 14.0 volts.

I've seen on 100 watt ham rigs that the final amplifier runs directly from the DC supply, so the output power is quite sensitive to the supply voltage. So you might lose out on a few watts running from battery.

This probably won't apply to the UHF CB.

Make sure you have the correct fuses everywhere. Lead acid batteries can generate hundreds of amps. The fuse is there to protect the cable, not the radio, so you need a fuse at the battery itself, and then if that fuse is too large, another smaller fuse each time the cable gets thinner. The test is that at all points in the circuit, a short circuit should blow the fuse and not melt the cable. This is how it's done in your car:  
Large battery (500 Amps) --> 100 A fuse --> 100 A cable --> Fuse box  
Fuse box --> 15 A fuse --> 15 A cable --> headlight.  
You could also just have several 5 A fuses right at the battery and run the thin cables to the rigs from there.

## Answer (score 4, by rclocher3)

In addition to the points raised in the other fine answers, I'd like to add a few:

- A good three-stage battery charger for lead-acid batteries may cost more than a power supply.
- Many chargers make horrific RF noise, so you may not want to operate while the batteries are charging, or you may want to pay more for an RF-quiet charger.
- The actual capacity, as measured in amp-hours or watt-hours, of a lead-acid battery is about half the advertised capacity, assuming that you don't want to damage the battery by draining it down too far.
- The Lithium-chemistry batteries that I've seen specifications for can be fully discharged without damage.

I'm not trying to talk you out of powering your station by battery; I'm thinking of investing in a solar and battery backup power system myself.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18421/are-there-any-cons-of-running-shack-on-battery, by Alexander, Phil Frost - W8II, tomnexus, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
