# Why don't baluns require precise conductor spacing as in twin-lead?

*Tags: balun, toroid · score 3*

## Question

This is a follow up to another recent question of mine: [Does a balun need to be made with coax?](Does%20a%20balun%20need%20to%20be%20made%20with%20coax.md) In that question, we establish that a choke balun doesn't actually work by protecting the "third conductor" on the outside of the coax shield, so there's no need for the coax itself to be part of the balun.

The design in question was the sort pictured below, where a pair of regular wires are wrapped around a toroid core. I've seen this kind of design in many places, including in other balun questions on this site, so the idea must be sound.

Given that there is no sort of precise spacing between the two wires, there must not be any sort of precise characteristic impedance, either. The question is, why doesn't this cause problems? Or does it, and you're expected to be using an antenna tuner to compensate?  
(From http://www.m0pzt.com/baluns/)

## Accepted answer (score 2, by Phil Frost - W8II)

It more or less doesn't matter because it's so small, relative to wavelength. As such, a lumped element model is valid.

You can make a conjecture to that effect by looking inside your antenna tuner (or really, a lot of HF equipment). Unless it's a fancy kind, there will be wires running whatever way between the components, with no attention paid to the characteristic impedance of those connections.

Think about it this way: imagine a change in voltage propagating down the line. When it encounters the balun, it will encounter some mismatched impedance, and some amount of the energy is reflected back. A very short time later (due to the very small size, relative to the balun) the same change, but reversed, which will send another reflection except opposite in phase back down the line.

If these two reflected waves occurred at exactly the same time, they would entirely cancel. In practice they aren't *exactly* at the same time, but since the change in phase between the two is so small (remember, tiny relative to wavelength), they *almost completely* cancel, and the effect is negligible.

The spacing of the wires does matter in a different way: there's some capacitance between them. We can incorporate that into the lumped model like this:

The inductor and the capacitor each have some impedance, with the inductor's impedance increasing with frequency, and the capacitor's inductance decreasing with frequency. The two form a parallel LC circuit, and at the frequency where the impedances are equal, the impedance of the balun as a whole is at a maximum.

It's easy to add more turns to a balun, so achieving a sufficiently high inductance isn't too hard. But each turn also increases the area where the wires are close together, introducing additional capacitance. At some point there's so much capacitance that the associated impedance is so low it effectively makes the balun a short, making it ineffective as a balun.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7033/why-don-t-baluns-require-precise-conductor-spacing-as-in-twin-lead, by Dominick Pastore, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
