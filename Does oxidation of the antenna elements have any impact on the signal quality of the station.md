# Does oxidation of the antenna elements have any impact on the signal quality of the station?

*Tags: antenna, antenna-construction, wire-antenna, maintenance · score 6*

## Question

So I'm still QRT; apart from a brown-out on the rig, the support on the inverted-vee toppled over in high winds.

Thanks to the topple-over I discovered the conductors (SWG 16 bare copper) had started to turn greenish-black; a sure sign of oxidation. This *may* be because I was QRT for a while before the mast came down. It could probably happen of it's own accord eventually even if the station were on the band with any regularity.

My antenna was an inverted-vee with exposed conductors. It may possibly happen on other wire antennas (sp. antennae??) as well.

Which brings me to my questions

- Does oxidation of the antenna elements have any impact on the signal quality of the station?
- Is there a simple mechanism to avoid/mitigate such oxidation on the antenna elements?

 - E.g. Use a laminated conductor instead of bare
- Is any *regular* maintenance activity necessary on an antenna?

 - E.g. In **my** case, how much should the conductors be allowed to darken before replacing/abrading/scoring the conductors?

## Answer (score 3, by Phil Frost - W8II)

If the oxidation is superficial, that is it hasn't penetrated to a significant depth, it will not affect the antenna. Most metal oxides are good insulators. The antenna is already surrounded by a good insulator: air. Adding a thin layer of another insulator (metal oxides) doesn't change the electrical picture in any significant way.

You should look for corrosion on any connectors or mechanical contacts. The corrosion might work its way into a connection, and since the corrosion is not a good conductor, the contact resistance will be increased.

Antennas can be made to be nearly maintenance-free if you design the connections to avoid corrosion. Protect any connectors from the elements with self-amalgamating tape, or pot them in epoxy, or somehow avoid environmental exposure. Welded connections are great, where they are practical. Be mindful of galvanic corrosion.

## Answer (score 2, by WPrecht)

I don't know if a little oxidation affects the radiation of the elements. I guess it could, but I suspect, not enough to matter in the big picture.

I have an 80m inverted-vee that I soldered up out of spare parts and it's exposed, but hasn't been in the air all that long.

If there is still good, solid electrical contact on the connectors, then it's probably fine. If you wanted to be sure though, clean them off and then coat them with spray paint or lacquer. As long as it's non-metallic paint, it will be fine and keep the connectors from oxidizing. Seems like cheap insurance since the antenna is down already.

## Answer (score 2, by Adam Davis)

Similar to [anodizing and powder coating antenna elements](Will%20anodizing%20or%20powder%20coating%20or%20wetcoating%20%28painting%29%20antenna%20elements%20affect%20performance.md), oxidation will affect the velocity factor of the antenna element, which in turn will affect the tuning of the antenna. The change will be very slight, though for the typically very long antennas in the HF band it might be noticeable and measurable. But that also means it's correctable. You can use an antenna tuner to mitigate the effects, but you'll probably want to retune your antenna yearly. Even with the oxidation, the antenna is perfectly fine as long as it's treated like any other bare antenna, and is well insulated from nearby conductors.

The green is typical copper oxidation, the black may indicate Copper(II) oxide, which typically requires higher temperatures to form, so it might be something else. It can be a skin irritant, though, so wear gloves when handling it.

As mentioned in WPrecht's answer, the oxidation will get in the way of transferring power to the antenna at any point where you want conductors to contact. Make sure they are clean, consider using a good anti-oxidation conductive joint compound, and sealing the joint to make it airtight so you don't have to perform maintenance frequently. You'll want to check it yearly as well.

I wouldn't recommend spending much time replacing the wire with something different. The few problems of oxidation aren't significant enough to warrant replacement, or the effort removing the oxidation and coating it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/989/does-oxidation-of-the-antenna-elements-have-any-impact-on-the-signal-quality-o, by VU2NHW, Phil Frost - W8II, WPrecht, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
