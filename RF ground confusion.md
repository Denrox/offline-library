# RF ground confusion

*Tags: hf, coaxial-cable, vertical-antenna, grounding · score 4*

## Question

I'm a bit confused by RF grounding. Let's take a HF 1/4 wave vertical antenna for example.

When current flows through the centre of the coax to the antenna, my understanding is that the current then needs a return path, which is back through the outer shield of the coax back to ground.

The antenna is what converts the electrical current into RF radiation.

Therefore, what travels back through the outer coax (or should)? Is this the actual electrical current or the RF signal? Feel free to criticize this question if it doesn't make much sense. I'm still trying to grasp some things. Thanks.

## Answer (score 2, by Phil Frost - W8II)

If the coax is operating without common-mode current (a typically desirable property of a properly designed antenna system), then it's the case that at any point, at any time, the current in the shield is equal in magnitude but opposite in direction to the current in the center conductor.

When someone says "the coax shield is ground" what they mean is the electric potential of the shield is zero. Or in other words, the electric potential difference between the shield and a point infinitely away from any charged particle in the universe is zero. Since the Earth is pretty big, fairly conductive, and mostly not charged, its electric potential is also mostly zero. So zero electric potential also means the electric potential difference between the shield and a copper rod driven in the ground is zero. This is desirable because it means the coax doesn't radiate.

The reason the electric potential of the shield is zero is that when the electric and magnetic fields associated with the voltage and current of the shield and the center conductor are equal in magnitude but opposite in direction, the sum of these fields is zero for all points outside the shield. So, the wave is contained entirely inside the coax.

However, no common-mode current isn't a given: it's the result of properly designing the antenna system. This is why [feeding a dipole with coax requires a balun](Using%20a%20balun%20with%20a%20resonant%20dipole.md), for example.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18761/rf-ground-confusion, by Engineer999, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
