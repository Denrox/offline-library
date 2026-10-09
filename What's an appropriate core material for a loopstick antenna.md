# What's an appropriate core material for a loopstick antenna?

*Tags: antenna, antenna-construction, ferrite, magnetic-loop · score 8*

## Question

A loopstick antenna, if you don't know, is a coil of many turns around a high permeability core. They are frequently encountered in AM receivers and look like this:

This particular example is actually two antennas on one core.

What type of material is an appropriate core for these antennas? What material parameters are relevant in the selection of an appropriate core, and how do they affect antenna performance?

## Accepted answer (score 3, by WPrecht)

As it's name implies, a loopstick antenna is a magnetic loop antenna and is one of the best choices for an electrically short antenna; necessary because broadcast AM wavelengths are hundreds of meters long.

Rather than a regular loop, a loopstick utilizes a large amount of (usually Litz) wire wrapped around a ferrite rod. This forms an inductor which is tuned to resonance by a variable capacitor as the radio is tuned to a frequency.

The material for the core of these antennas is ferrite -- a powdered iron based magnetic material with a variety of other metals added. The exact composition of the ferrite material (called it's "mix") governs it's characteristics.

The goal of the ferrite is to produce a very high Q inductor with a high electrical resistance. The efficiency of the inductor is governed by the permeability of the ferrite core and the core's permeability changes with frequency.

This is because the ferrite itself absorbs power. This arises from the energy required to change the magnetic alignment of the magnetic domains inside the granular structure of the ferrite. The higher the frequency, the greater the number of changes and hence the higher the loss, generally dropping off sharply. See the following chart (lifted from the Fair-Rite catalog) for example:

In the chart, μ' is the permeability of the ferrite and μ" is the ferrite induced losses. While the permeability continues to rise until about 11 MHz, the loses begin to rise dramatically starting at about 4.5MHz. This is why Fair-Rite Corp only recommends this mix through about 5MHz.

This is a chart of their "mix 61", which uses Nickel and Zinc in the iron to achieve it's characteristics and is recommended as the proper one for AM broadcast frequency antenna material.

Some ferrite mixes are produced specifically for applications that take advantage of the ferrite's ability to absorb energy. These materials can be used to suppress unwanted signals.

As one example, for suppression of energy occurring at HF frequencies, they recommend "mix 73", a combination of Nickel and Manganese which performs well at absorbing energy, up to about 50MHz as shown here:

It's worth noting in this chart that the losses are much higher than the MF band material, but so is the permeability.

This is probably a good time to underline an important characteristic of ferrite: while it concentrates the magnetic fields, it has a very high electrical resistance. This isn't very important for receiving. But the use of ferrite in a transmitting antenna, or as is more common among hams, as a transformer in baluns or ununs, it can be important.

Ferrite's resistance is inversely related to it's permeability. The less permeable ferrite becomes, the more resistant it becomes. Ferrite's permeability is also affected by temperature. As the ferrite warms up, it's permeability increases until it reaches what's called it's Curie temperature, for this mix, about 160° C. At that point ferrite rapidly loses it's permeability as shown in this graph:

And this is how baluns and ununs fail. Power through the transformer warms the material due to the ferrite related loses. All is OK until the curie temperature it reached and then the permeability falls off a cliff and the resistance **increases** causing more heating in a runaway thermal loop until your coax melts and shorts the inner conductor to the shield.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1156/what-s-an-appropriate-core-material-for-a-loopstick-antenna, by Phil Frost - W8II, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
