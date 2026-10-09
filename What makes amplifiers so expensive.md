# What makes amplifiers so expensive?

*Tags: amplifier · score 7*

## Question

Why are amplifiers so expensive? What is in it that makes them so expensive? My research suggests that the cheapest amplifier is >$2,000. The most expensive one is the new ICOM 1kW amplifier, and it costs

$5,500. It's just 400 more watts, why is it so much more expensive? It's more expensive than a new HF/VHF/UHF 100 watt radio! Wikipedia says it has vacuum tubes in it, but they don't even come close to triple digits. Is there something else that makes it more expensive? It says modern amplifiers have MOSFETs in it, but MOSFETs are even more cheaper. On Ebay, there are

$20 amplifiers. It outputs 70 watts, so if it could output 1kW, it should be 250 dollars. So what is going on here?

## Accepted answer (score 11, by hobbs - KC2G)

Wikipedia says it has vacuum tubes in it, but they don't even come close to triple digits.

Actually, they do. The sort of tubes that go into a new-make HF amplifier typically cost $400+ (vacuum tubes are a rare commodity these days), and it's common for an amplifier to use two.

It says modern amplifiers have MOSFETs in it, but MOSFETs are even more cheaper.

Not by as much as you think. Again, there's MOSFETs and then there's the sort of MOSFETs that you want to use for high-power RF. The ones you'd find in a modern HF amp are typically $200-400 per transistor, and again most designs use two.

Of course an amplifying element (tube or transistor) isn't enough to make an amplifier: you also need a power supply (an amp that makes 1000W of output power needs close to 2000W of well-regulated input), cooling (fans, plus a lot of heatsink), impedance matching, output filters, and typically you want some means of measuring the temperature, output power, SWR, and plate/drain current, and some means of detecting if those values go out of range and shutting the amplifier down before it does permanent damage to one of the $400 doodads inside. Plus a bunch more if you want ALC, automatic band switching, a built-in ATU, an antenna switcher, or any other bells and whistles. Everything needs to be built to handle the power (which means bigger, more expensive components), and everything needs to be designed and shielded to keep noise out of the output and to avoid catastrophic oscillation (if you've got a 30dB FET at the heart of your design, and 0.01% of its output manages to creep back into its input, you've got a big problem!)

All of that adds up to a significant parts cost, but that's still not the whole story, because selling an amplifier commercially means designing it (not a trivial job, I assure you), prototyping it, writing the firmware, getting it certified, tooling up a production line, writing the manual, manufacturing it, marketing it, warehousing and distributing it, all of which is likely to cost millions of dollars on top of the actual BOM cost.

And then, once you've done all that, you're going to sell... a thousand amplifiers, maybe, over the lifetime of the product. Ten thousand, if you're really lucky. Because there aren't that many customers out there, and not all of them are going to choose your product. Which means you need to sell every single unit for *much* more than the cost of parts to have any chance of making the whole project worthwhile. That's why the retail cost is so high.

You can get boards in kit form and build your own amplifier, and save some money. Or do it all from scratch and save even more. But it's a demanding project.

## Answer (score 10, by Marcus Müller)

As hobbs says, economies of scale are dominant here – you design, prototype and distribute a high-quality amplifier for a couple hundred to thousand people. Your risk and investments are very high, so you can't sell them for their part and production costs, but need to factor in your engineering time and the financial risk (what if you *don't* sell so many?) into every single one that you sell.

Also, hobbs is 100% on with "it's powerful, so it's got large and expensive components": The moment you need to do anything to a high power, every component necessarily becomes either very large or very well-cooled, and usually both.

Then, you write something very surprising:

On Ebay, there are $20 amplifiers. It outputs 70 watts, so if it could output 1kW, it should be 250 dollars.

Your math seems to be extremely broken here. Cost scales *worse* than linearly with power, not better: A \$ 20 amplifier off ebay probably does around 5 W to 10 W, realistically, at acceptable signal quality. (Ebay sellers lie. Unless you have the measurement electronics to guarantee you're not exceeding your amateur radio allocation's bands with the harmonics of bad amplifiers, hands off cheap amplifiers; you have taken an amateur exam where you have answered questions on these things. You can't even *claim* you didn't know that out-of-band emissions are illegal!)

So, a 1 kW transmitter would be 100 times as powerful as your ebay device. I don't see anyone building that with a \$ 250 budget.

So what is going on here?

Mostly, you ignoring three things:

1.

Basics of economical modelling. the number of people who can operate a 1 kW amplifier is very limited, but the number of companies that can build and sell something that is easy enough to operate for a ham is even smaller. And the ham equipment market is one where the buyers are chronically at an informational disadvantage: They don't understand (on average) the technology well enough to assess what they need or what the qualities of the products they might be buying are. Your question is a good example of that! Your comparison with an ebay device is a good illustration of that. No electrical engineer would buy that – the spec sheet that even defines the very basic properties of an amplifier is simply missing. Hams are hence at a economic disadvantage, because they can't tell a good deal from a really bad one. So, the only sensible path forward is to stick to established brands, because e.g. ICOM wouldn't risking their reputation by selling you a bad device. Of course, that makes the demand for ICOM devices higher compared to comparable amplifiers of other manufacturers, and they incorporate that into their pricing.

2.

Economics of scale: Makes a huge difference if you can split your development and capital costs over a million amplifiers, or a few hundred. Do a thought experiment: To a US, German or Japanese company, an average engineer hour might be worth around 200 \$. (Don't forget they are paying taxes, need an administration to make sure their salary gets paid on time etc, work in buildings that someone has to pay for, have to go to workshops regularly to become better etc… It's not only their salary!) Now imagine a team of 5 engineers working on a product for a month (1 development engineer, 1 production process engineer, 1 test engineer, 1 acquisition / component availability engineer, 1 project manager). That's 5 × 40 hr × 200 \$/hr, before the first of that device gets produced. Divide that by the number of devices you sell within the first few years, and add 4% accumulating capital interest per year. Then you get the base price for that product, on top of which someone has to actually *produce* the thing and actually *buy* the components and actually *ship* it to the customer and *support* the customer.

3.

You totally base your pricing ideas on gut feelings, not on actual technical properties: cost scales typically more like quadratically with output power. And: where you can get away with much laxer filtering and still don't emit illegally much power in other bands due to harmonics, and when you do 100× the power, you need 100× better filters – and that's the "best case", because typically the harmonics get worse with more power. So, you probably need a much-better-than-100×-better filter!

Finally, I'd like to say that it's honestly very surprising to me that people *want* 1 kW amplifiers. Not only do these things get hot and use a lot of power, they're also heavy and *dangerous*! I understand the very ham desire to make contacts as far away as possible, but I think the time is ripe for realizing that that means going *better* signal design, not *stronger* signal power.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22980/what-makes-amplifiers-so-expensive, by John Doe, hobbs - KC2G, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
