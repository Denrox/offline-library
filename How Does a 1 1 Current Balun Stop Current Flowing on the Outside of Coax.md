# How Does a 1:1 Current Balun Stop Current Flowing on the Outside of Coax?

*Tags: transmission-line · score 3*

## Question

Does anyone know how a current balun, when connected between coax and a series center fed half wave dipole, prevents RF current from splitting up at the join between coax braid and balun and traveling down the outside of the coax ?

I have added another picture to further clarify what i am asking - when transmitting, how does the current balun in the drawing below prevent Ishield-outer ? Noting that the current arrows indicate instantaneous direction only, because this is the current of an RF AC waveform flowing through the wires of the coax that i am talking about.

## Accepted answer (score 2, by hobbs - KC2G)

I have added another picture to further clarify what i am asking - when transmitting, how does the current balun in the drawing below prevent Ishield-outer ?

I'm going to ignore the arrows in your picture and adopt a convention of "positive current sign = upwards", to hopefully avoid confusion. I'm also adding two more measurements, I(balun left side) and I(balun right side) for the currents in each of the two coils.

KCL tells us that I(shield inner) + I(shield outer) - I(balun left side) = 0. [eqn 1]

A quick glance tells us that I(center) = I(balun right side). [eqn 2]

The properties of coax tell us that I(center) = -I(shield inner). [eqn 3]

The balun does its best to ensure that I(balun left side) = -I(balun right side). [eqn 4]

Let's assume that the balun is perfect and that the last equation holds exactly. Then by substituting eqn 4 into eqn 2 we can come up with I(center) = -I(balun left side).

Substituting that into eqn 3 we get I(shield inner) = I(balun left side).

Now substitute that into eqn 1 and we have I(shield outer) + I(shield inner) - I(shield inner) = 0. Or, simplifying, I(shield outer) = 0.

Equations 1 through 3 are another way of stating that "only common-mode current flows on the outside of the shield". If upward current on the outside of the shield makes a "U-turn" and becomes a downward current on the inside of the shield, it induces an upward current on the center conductor in doing so! So perhaps another way of answering your question would be: it *does* do that, but contrary to your intuition, that doesn't prevent the balun from working — it's exactly what *makes* the balun work. Any current induced by the outside world on the outside of the shield will be presented to both balun terminals equally, and therefore be subject to the balun's high impedance towards common-mode current.

## Answer (score 4, by user10489)

A balun or unun prevents (or reduces) common mode current by providing a low impedance path for differential current and a high impedance path for common mode current.

The pictured balun does this by pairing the wires that you want equal and opposite current in them, while common mode current has to deal with the impedance of the windings around the core. However, if you have high power common mode current with this, the core can saturate, overheat, and possibly crack.

The paired wires form mutual equal and opposite magnetic fields that cancel, so impedance is low. Common mode current flows in the same direction in both wires, so the fields add instead of cancel, and the resulting field interacts with the core. You can think of the core like a huge magnetic field dampener with a high magnetic inertia and resistance, and thus the result of the wire around the core is a high electrical impedance.

The core does not just interact with the shield, it interacts with common mode current in *both* wires.

Note that balun cores are designed differently than regular transformer cores. Transformer cores typically use laminated plates to have a low magnetic resistance in one direction while having a high resistance in a perpendicular direction to reduce eddy currents. Balun cores use powdered ferrite which has a high magnetic resistance in all directions.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21819/how-does-a-1-1-current-balun-stop-current-flowing-on-the-outside-of-coax, by Andrew, hobbs - KC2G, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
