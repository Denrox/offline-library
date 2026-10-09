# Why do repeaters use cavity filters?

*Tags: repeater, filter · score 17*

## Question

Repeaters apparently often use large, expensive cavity filters to connect the receiver and transmitter to the same antenna.

Why aren't typical electrical circuits, such as inductors and capacitors used instead? Wouldn't they be cheaper and smaller?

## Accepted answer (score 19, by Phil Frost - W8II)

A cavity filter is inductors and capacitors. Something like this:

(from amateur-radio-wiki.net)

There are several reasons these are not constructed from more common discrete inductors and capacitors. Firstly, these filters must handle a bit of power. Not that you can't get high-power discrete capacitors and inductors, but they aren't cheap, or small.

But perhaps more importantly, the cavity filter is a notch filter. Since we want to pass some frequencies while deeply attenuating some other frequencies that are not very far apart, we need a deep, narrow, steep notch. The notchiness comes from the resonance of the capacitors and inductors, and with ideal components, at resonance, the stopband attenuation is infinite.

Sadly, we can't have ideal components. Any real inductor or capacitor will have some resistance and other non-ideal behaviors (self-resonance, etc) which serve to dampen the resonance of the filter. As this resonance is dampened, you get less of a notch, and more of a shallow trough. Too much damping and now the notch isn't deep or steep enough to accomplish the objective.

Q factor is one way to quantify the damping in an RLC circuit such as this. The cavity filter is a way of constructing an RLC circuit with a very low R, and thus, very high Q.

A good cavity filter will also account for other practical considerations. Its tuning must be stable over temperature changes. It shouldn't leak a lot of RF, since it's probably collocated with other RF equipment. It should be able to handle high power without damage. It should be durable, since it's probably at a difficult to access location. It should come from the factory tested, and perhaps already tuned to the desired frequency. All these things add to the cost.

## Answer (score 2, by Brahm Bothma)

Very good answer @phil (Phil Frost - W8II).

@Adam (Adam Davis) - Another reason is that repeaters are usually located on high-sites where there are a lot of repeaters installed. On these high-sites it would also have line of site to the other high-sites in the area.

There are Inter-modulation involved one these sites where phantom transmissions could occur. A lot of these sites has hi-low pass filters (ie. cavity filters) which filter out these and other frequency so that the repeater only re-transmits the communications that it should, and nothing else.

Hope that this answers you the "use-case". P

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/971/why-do-repeaters-use-cavity-filters, by Adam Davis, Phil Frost - W8II, Brahm Bothma. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
