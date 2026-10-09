# Dummy load construction and heat dissipation

*Tags: diy, equipment-design, dummy-load · score 6*

## Question

I'm building my own dummy load, consisting of resistors submerged in liquid paraffin (or something similar, not 100% decided).

I had some questions around heat dissipation and how I can calculate and avoid the thing over-heating.

1. Is there a particular fluid that is better than other in both performance and cost?
2. What sort of volume of fluid should I use assuming I would be using up to 100W, such that it won't start heating up quickly? Is there even a way to accurately calculate this?
3. Are there any non-obvious safety concerns I need to think about when constructing and using this? I don't want to miss anything simple but obscure.
4. In a sealed system like this, is there any risk of explosion due to pressure from the liquid heating?

## Accepted answer (score 4, by Phil Frost - W8II)

Is there a particular fluid that is better than other in both performance and cost?

Water is hard to beat in both respects. The trouble is it has this tendency to become a conductor as it dissolves salts, so it must be insulated, or somehow kept very pure. Sometimes the trouble of this is too much, so some sort of oil is easier.

What sort of volume of fluid should I use assuming I would be using up to 100W, such that it won't start heating up quickly? Is there even a way to accurately calculate this?

Heat capacity is perhaps the relevant physical property here. The specific heat capacity of liquid water is about $4.8J/(gK)$, and since 1mL of water weighs about 1g, we can also say the volumetric heat capacity of liquid water is about $4.8J/(mLK)$. We know that $W=1J/s$, and from these two things, given a power, and some volume of water, we can calculate at what rate the temperature will rise, if the temperature is uniform throughout, and no heat energy is being lost elsewhere. Let's use 100W and 1L as an example:

$$ \require{cancel} \frac{100\cancel{J}}{s} \cdot \frac{\cancel{mL}K}{4.8\cancel{J}} \cdot \frac{1}{1000\cancel{mL}} = 0.21\frac{K}{s}\\ $$

Since we are talking about a rate of change, you might as well consider $K=^\circ C$.

Of course, this involves two assumptions we know to not be true, the first being that the temperature of the water (or whatever coolant) is uniform everywhere. If the coolant is actively stirred, then it might be close enough to true. Otherwise, you are dependent on conductive currents and conduction to distribute the heat energy throughout the coolant, some parts are hotter and some are cooler, but the average temperature increases at this rate.

But this is somewhat moot, given the second assumption: that no heat energy is otherwise being lost. Probably you won't wrap the dummy load in blankets then operate it until it overheats, but rather construct it with a surface designed to radiate heat into the ambient environment well enough that it can be operated indefinitely without overheating. The job of the coolant is really just to provide a good thermal coupling between the heat sink and the heat sources, and to average out any transient thermal loads.

The relevant physical property for the heatsink is absolute thermal resistance. This quantity has units $K/W$ and tells you, for a given constant power, what the temperature increase above ambient will be. It will be specified by the manufacturer's datasheet. You also need to add to this the thermal resistance of everything between the heat sources and the heat sink. Unfortunately calculating the absolute thermal resistance of your tank of coolant is hard, because it has a complex geometry, and the things likely to be used in the tank (water, oil) are actually not especially good thermal conductors: they move the heat around mostly by convection.

So, the general approach is this: figure out, for your design power and allowable temperature rise, how big the heatsink would need to be assuming the best case, then make it bigger to account for other factors. TLAR is probably the most economical method, and if you need something more precise, then pump a known power into a prototype, and if it gets too hot, make it bigger.

Are there any non-obvious safety concerns I need to think about when constructing and using this? I don't want to miss anything simple but obscure.

Besides the obvious ones of having a potentially large quantity of possibly flammable, probably very hot fluid, potentially heated beyond its boiling point, connected to an electrical energy source that might be capable of generating sparks or heating (especially under fault conditions) materials above said fluid's flash point? No, I can't really think of any. I don't think it's the non-obvious safety concerns that are going to kill you.

In a sealed system like this, is there any risk of explosion due to pressure from the liquid heating?

Very yes, see last question. I wouldn't seal it if I could help it, and if I did, I'd be sure it wasn't sealed very well, so an overpressure fault would just dribble rather than explode. Also couldn't hurt to make sure the pressure release mechanism indeed *dribbles* and not *shoots a hot jet of oil*.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/939/dummy-load-construction-and-heat-dissipation, by David VK2VXK, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
