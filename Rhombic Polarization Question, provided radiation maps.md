# Rhombic Polarization Question, provided radiation maps

*Tags: antenna-construction, wire-antenna, 2m-band, polarization, radiation-pattern · score 3*

## Question

I am trying to engineer my first antenna to get on the air. I need to hit a repeater 50 miles away at a lower elevation than me so that I can use its IRLP nodes. Would this mean I am looking for low angle radiation?

25 feet up with an HT in the clear and a rubber duck antenna and I can hear just the faintest crackle. I believe that a rhombic would be a cheap, interesting, and clear way of getting my signal to the repeater.

Will it need to be vertically polarized, considering everyone else will be? I started working on the design, here are some preliminary radiation maps before optimization. I just wanted to confirm that I had the correct polarization for the job. ANY tips regarding rhombics would be appreciated as I am new to the hobby and will probably learn a few things the hard way on this project :D

*** Note that the scale on the perimeter of the chart is shifted 90 degrees for some reason, I didn't see this at first. ***

## Accepted answer (score 1, by tomnexus)

Some information, since you asked for comments:

1) your rhombic isn't working properly. It shouldn't have a double beam like that, it should have a single forward beam. Something about the proportions is wrong.

You can and should design a rhombic from formulas, and only simulate at the end. It's a well understood antenna, there is good design data for it.

It needs a termination resistor at the end away from your feed. It's not showing in your model. This needs to be non-inductive, which is tricky for 2m, possibly made of a hundred quarter-watt resistors in series and parallel.

2) as they are usually built, rhombics are horizontally polarised. The repeater is almost certainly vertical. You need to tilt it up on edge to make it vertical. The masts that support it, both the the middle and at the front, must be non-conductive.

3) You're simulating over a ground plane, which is appropriate for HF because it's so intimately involved in the antenna fields. For a VHF antenna 25' up, the ground doesn't matter. You should remove the ground and simulate the antenna in free space. The ground will get involved later, a hundred metres away, but it affects all antennas equally.

4) consider a yagi instead. The main features of rhombics are their simple construction, limited number of supports, and wide bandwidth to cover many bands. This makes them attractive for HF when you have a lot of space. They have reasonably good gain, but nothing like a yagi. Do some digging for information about the gain of a yagi and compare. For example, you can easily make a yagi for 2m from an old broomstick and some fencing wire / welding rods, that will give you about 10 dBi, which is at least 13 to 16 dB more than your handheld antenna yields. If you want a lot of gain, look up the Rope Yagi, which can be made very long.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5064/rhombic-polarization-question-provided-radiation-maps, by Zeke Legge, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
