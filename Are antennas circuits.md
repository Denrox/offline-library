# Are antennas circuits?

*Tags: antenna, theory, antenna-theory · score 12*

## Question

For an antenna to work, doesn’t charge have to flow through it? A current must be present. To me it indicates it must be a circuit, but how is a dipole a circuit?

If they are not circuits, then how does charge flow in them?

## Accepted answer (score 16, by Phil Frost - W8II)

What do you mean by "circuit"? Do you mean there's a loop of conductor from one side of a battery to the other, possibly with some other conducting components along the way? How about this circuit?

Is there a circuit here? There certainly isn't any way to follow a line from one side of the battery to the other. Each half connects to opposite plates of the capacitor, and those plates are separated by an insulator. Yet, if you flip that switch repeatedly, the LED will blink. Clearly there's some current flowing.

If we pull the plates of the capacitor apart, it's still a capacitor. It capacitance will decrease, but it's still a capacitor. Just a smaller one.

If we squish the plates into long, thin tubes or wires, it's still a capacitor. Capacitance may decrease still more due to the smaller area of the plates, but it's still a capacitor. The circuit now is looking something like this:

What if we now pull the ends of the capacitor apart?

Yep, it's a dipole antenna. Lose the LED and the resistor, and flip the switch a few million times per second, and you have a transmitter.

Not illustrated here is also the inductance of the antenna. All circuits have inductance, which you can realize if you follow a similar argument but with an inductor instead of a capacitor, and start straightening the coil into a straight line. The inductance decreases, but it never goes away. Usually we don't draw the inductance because it's small enough to be negligible in a simple circuit that blinks an LED.

Thus, antennas have capacitance and inductance. They also have resistive losses (unless they are made of superconductors) and radiation resistance. Putting all these together, antennas can be modeled as an RLC circuit.

## Answer (score 3, by Kevin Reid AG6YO)

**The idea that a closed circuit — a loop — must be present for current to flow is a simplified description, which is only true for simple DC circuits.** It's a simplification that works because in the DC case, if there is no complete circuit and yet current is flowing, then charge is accumulating somewhere, and the electric field from that excess of charge will oppose the current, increasing to the exact point at which the current stops.

However, in the AC case — and RF is AC, or perhaps “beyond AC” depending on how you classify things — the current is expected to reverse, and therefore those accumulations of charge can go away again, so the system can pass through repeating cycles of charging and discharging. The common circuit component in which this happens is a **capacitor**.

The movement of charge in a dipole antenna is *somewhat* like that in a capacitor, with “the rest of the universe” substituting for the space between the capacitor plates.

Like in a capacitor, no charges actually move from one half of the antenna to the other (except indirectly through the rest of the circuit). Instead, the charges *bunch up* in the antenna, forming a positive excess on one half and a negative excess on the other. In a receiving antenna, the energy to push the charges together comes from the incoming wave. In a transmitting antenna, it comes from the transmitter.

As the wave continues through the rest of its cycle, the antenna discharges and charges in the opposite polarity.

Thus, the rest of the circuit connected to a receiving antenna “sees” an oscillating voltage corresponding to the original wave.

Actually, it'll increase a little bit further and reverse — sloshing back and forth a bit until it settles down. This is due to *inductance*. But that doesn't matter for the rest of this answer.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3502/are-antennas-circuits, by mikew, Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
