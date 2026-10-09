# Why do homebrew designs wrap toroids instead of using off the shelf inductors?

*Tags: diy, equipment-design, inductor, components · score 6*

## Question

Why do homebrew designs wrap toroids instead of using off the shelf inductors?

Off the shelf inductors are easily available in a range of values, including uH and even some mH. And hand wrapping toroids is laborious and in some cases difficult. There must be an advantage to using them, otherwise why bother. What is it?

## Accepted answer (score 7, by Kevin Reid AG6YO)

Broadly, the thing about about inductors (and transformers) is that

- it is very easy to make them by hand, *compared to most other components*, and
- they are relatively rarely used in mass-produced electronic circuits *other* than filters, matching networks, and power supplies, so there is less economy-of-scale in manufacturing them.

The inductor's closest relative, the capacitor, requires very thin layers of metal and dielectric (which are hard to assemble using readily available materials and tools) to get a useful capacitance in a reasonable volume (except for very small values), and is much more widely used, so there are a lot more capacitors available with all sorts of properties.

Thus, it makes sense to buy exactly the capacitor you need for your circuit, but a similarly specific inductor, with the right inductance value *and* the right sort of core, might be much more expensive or even entirely unavailable.

## Answer (score 2)

you can choose different cores with different permeability ratings. they generally have higher inductance and you can get very good Q values with a carefully wound torrid.

You also can easily change the inductance by adding or removing wraps or changing the spacing between the wraps.

You can also use them to make simple RF transformers.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22709/why-do-homebrew-designs-wrap-toroids-instead-of-using-off-the-shelf-inductors, by SRobertJames, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
