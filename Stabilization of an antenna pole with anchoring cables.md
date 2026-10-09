# Stabilization of an antenna pole with anchoring cables

*Tags: antenna, antenna-construction, vertical-antenna · score 3*

## Question

I am mounting my first antenna. It is a TRAM 1481 (about 16' height), which will be placed on a 20' pole, on my home's flat roof (about 25' height).

To properly stabilize the pole/antenna: - How far up the pole should I tie the cables? - How far away from the pole should I place the cables' anchors? - Any minimum amount of cables I should use?

I was planning to tie the cables up 16' and place the anchors around 3' away. I will then need around 16.3' of cable per anchor to tie to the pole.

But is there a formula to determine all this?

## Accepted answer (score 6, by Phil Frost - W8II)

What you have is a basic civil engineering problem. You might calculate a sheer and moment diagram, look up all the material properties, and calculate the failure points of all the components. In the case of an antenna, the most significant force is usually wind, and the objective is to make it strong enough that the structure doesn't blow over. It gets quite complex however.

Instead you may opt to employ "That Looks About Right" (TLAR) engineering principles, where you look at other things that have worked, combine some experience and intuition, and come up with something about right. You might look at the ROHN H20 push-up mast guy plan. The H20 has a maximum height of 19.25 feet, so not unlike your pole.

Here you can see the top set of wires is up about 19 feet, and is 18 feet away from the base. The drawing is not to scale. ROHN also has a 2nd set of wires at the midpoint. Since this is a push-up mast it's in two sections, so this is unavoidable. If you have a single 20 foot pole you might do without, depending on the rigidity of your pole and maximum wind load.

Generally you would not want to bring the anchor point closer to the base than this. You propose having the anchor point only 3 feet away from the base, and I think that's only marginally better than no guying at all.

Consider, the wind wants to blow the pole over (blue). That force is countered by two others: tension on the guy wire (green), and compression on the mast (red). There is potentially also a bending moment if the mast is connected rigidly to the ground, through for simplicity I've omitted it here. All the forces must be balanced if the mast is to remain stationary.

As you can see, in the left example with a steep angle there is significantly more force on the guy wire and the mast for the same wind load.

As a rule of thumb, anchor points about as far away from the base as the pole is high is a good compromise between strength and minimizing wire length and footprint.

## Answer (score 2, by Pedja YT9TP)

As general rule, anchoring point at the ground should not be closer than half of the height where guying line is attached to the pole (guying line slope would be 30 degrees).

Optimal is to have ground anchoring point at the distance which is the same as height where guying line is attached to pole (guying line slope would be 45 degrees).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10117/stabilization-of-an-antenna-pole-with-anchoring-cables, by KP4MCG, Phil Frost - W8II, Pedja YT9TP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
