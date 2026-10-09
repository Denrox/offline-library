# Development of quartz resonator qualities over the decades

*Tags: frequency, history, components · score 3*

## Question

While writing this answer here, I had to admit I only have "*…, I think*"-level of knowledge what a 1970's quartz resonator for a consumer radio device would have been spec'ed at.

My understanding is that consumer devices in the early 70s, typically used resonators that were speced to be no better than +-50ppm.

But that doesn't say much about amateur radio-used quartzes. While I know that quartz buyer-side "matching" and "binning" of quartzes is a thing for filter application, I don't know what the usual accuracy you would typically buy in the 1960s, 70s and 80s were. Could someone enlighten me?

- When you bought a replacable resonator for a radio device, what was the accuracy that you would buy?
- Was that even something "written on the box" or specified in the catalog, or were there just expectations that you would have for a reputable seller?

(Note: not asking for general availability of higher-accuracy quartzes. If your pricing model is called "Agilent measurement devices" or you have military budgets, and export clearances, you can buy fantastic frequency standards.)

## Accepted answer (score 6, by Ryuji AB1WX)

Crystal resonators (individual resonator packages like HC-18/u or HC-49/u) had widely varying performances, and I bet they still do today. Here, temperature-frequency sensitivity and long-term (aging) drifts are included in the broad term "performance" among other factors like Q drop or spur.

First of all, those parameters are heavily influenced by things like the precision of cutting the slice out of a crystal, smoothness of the surfaces (etching and polishing of the roughness created by sawing/lapping and other chemical stresses), electrode-deposition technology, mounting mechanism, packaging, gas fill and tightness of the seal, overall cleanliness of the manufacturing environment, etc.

There was also a wide range of manufacturing process controls. Imagine 3.579545MHz (or 3.58MHz) or 32.768 kHz crystals manufactured in a massive volume compared to custom-ordered crystals made to exact specs. They both may come in the same form factor, but the process controls are hugely different. Many special-order quartz labs were small labs, taking orders from corporate labs and factories (such as Kenwood), but some of them also took orders from people like me. I could just mail about $20 or so and exact spec (freq, Q, schematic of the oscillator circuit, etc. - of course, must be reasonable re available technology) and they mailed me a crystal in a few weeks, with a few sheets of test results from actual measurements (it was handwritten in ink). Those were of better quality than what I found in mass-produced consumer devices (such as digital logic devices and computer peripherals) of that time in the 1980s and 1990s. Some of those guys were also willing to cut and sell a set of crystals to make a ladder filter. They took the spec and schematics, or they specified the schematics. Those cost more, but user binning was not required that way.

Those quality differences, as far as I was aware back then, were mostly established as the reputation of the lab among RF-minded electrical engineers. When quality mattered, we always bought the crystals from the guy we knew or referred by the guys we trusted. There may be some variations, but I would not be surprised if the ecosystem and user dynamics were analogous in FRG and the USA back then, but only among engineers who cared.

User binning of the resonance frequencies was and is common when making narrow passband IF filters using stock crystals (not special order ones). If you are making a 3 kHz SSB filter, that's not so much of a problem, but if you are making 500 Hz or worse 250/200 Hz filters, the resonance frequencies must be matched to just a couple of Hertz tolerance.

In oscillators, most RF applications of the 1970s-1980s just required a trim cap to fine tune the frequency.

Regarding the temperature coefficient, the story is different. Most crystals were AT-cut by the 1970s. Those have a significant 2nd and 3rd order temperature response (dd freq / dT, ddd freq / dT) within the typical operating temperature window, but kept the worst deviation away from the nominal frequency within a specified limit. That is a good compromise for ambient temperature use. However, those were undesirable compromises for OCXOs and TCXOs. The latter applications require a gradual and predictable first-order response but very small higher-order terms. So SC-cut became common in those applications. But SC-cut was more difficult to make, and it was definitely higher-priced, and not all labs made them.

Obviously, manufacturing process control must have improved drastically in some high-end labs that make quartz oscillators. For example, we have a much higher fundamental frequency limit (i.e., much thinner precision cut that is stable under the mounting mechanical stress) than we had back in the 1980s. Precision, surface smoothness, mounting stress control, cleanliness, etc., all matter and also contribute to lower aging drifts. But I would not be surprised if some of the marginal quality components are still in circulation.

Out of mass-produced products, high-end HF amateur radio equipment, particularly 200-250 Hz CW IF filters, may be among the most demanding due to cost constraints and desired performance. The aging drift was probably a few times better (like 2-3 ppm/yr max, although I'm not sure if that was a typical written spec) than what those guys were saying (10ppm/yr).

Among age-related deterioration of crystals, I would worry more about Q drop (becomes harder to oscillate or amplitude unstable), spur, erratic oscillation behavior, etc., than about the drift being too large (without any of the former symptoms).

Incidentally, there probably was a good technical (not just business or managerial) reason why companies like HP (which was essentially run by an entirely different philosophy before Fiorina) and Kenwood made their own internal component number nomenclature rather than simply adopting their suppliers'.

I have no desire to join that thread or have my information used in a proxy battle there.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23713/development-of-quartz-resonator-qualities-over-the-decades, by Marcus Müller, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
