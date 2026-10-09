# Is this an unintended short circuit in my Moonraker GPA-80F vertical HF antenna?

*Tags: antenna, toroid, wiring · score 3*

## Question

I'm a newly licensed ham and purchased this Moonraker antenna from DX Engineering as my first HF antenna.

I noticed that there is continuity between the inside and outside of the SO-239 connector at the base of the antenna so I opened up the box and it looks like the blue wire wrapped around the toroid inside is soldered to the inner pin at one end and the outer shell of the connector at the other end.

Does that seem right? Should I disconnect the blue wire from the inner pin and connect it just to the outer shell so that both ends are attached at the same spot?

## Accepted answer (score 3, by Marcus Müller)

Ryuji's answer is 100% on point, but I thought it might be nice for you to understand *why*.

Ignore the yellow cable for a moment (or don't, and assume it's unplugged).

What you see being attached to the coax is a wire wound around a magnetic material core. That's a coil: an inductor!

You might remember inductors from your ham exam: they don't really influence DC, but they get more and more "resistive" the higher you go in frequency.

We can actually think about what happens here when you apply a DC current (e.g. to measure the resistance): The current through the blue cable causes a magnetic field. Maybe you're familiar with the right hand rule (or *Lenz's Law*), which tells you which direction the magnetic field lines "circle" around a conductor through which current flows.  
(mentally) Follow the blue cable around that ring core with your thumb and see how your fingers always point in the same direction inside the core (clockwise along the ring, or counterclockwise).  
So, your DC current causes a closed loop of magnetic field lines along the ring. Neat!

These field lines *magnetize* the material of that ring, and it effectively becomes an electromagnet, but one that you can't use for lifiting things, because its end is its beginning – it's a ring. But all that energy of an electromagnet is now stored as magnetic energy in the core material. That happens once when you turn on the DC – and in fact, putting that energy into the material will look to your multimeter as if the resistance was very high first, and only drops as you can't put more energy into the material, where it remains stored.

Well, that's fine than. After we've "charged up" the core with magnetic energy from the power of our DC, the inductor doesn't exert any power any more - it's simply reached a stable state. OK, that explains why the transformer you're measuring looks like a short to DC!

Now think about AC: You have just successfully put energy into the core, with the field lines running in one direction (say, counterclockwise). Now you switch the direction of the current. Hm, now the field lines are supposed to run against that direction? That's no good, this is like trying to spin a wheel that's already spinning, in the opposite direction. You will need to spend extra power to stop the spinning magnetic field and point it in the other direction!

That means that from the point of view of the coax when excited with an alternating voltage, you always get the back the energy you put into the core, but with a lag, at the moment you are trying to do the opposite.

Huh! So, now we qualitatively have a feeling for why it's OK that this seems to be a short to a multimeter. And why it won't look like a short to RF!

Now, but why is that useful, and why is there the yellow cable, and what does it do?

Can't explain that by the right-hand rule and static fields alone. Physics has it such that a *time-changing* magnetic field causes a voltage difference in conductors lying perpendicularly to these field lines. That's basically just the inversion of "AC through blue wire causes changing magnetic field lines in core" to "changing magnetic field lines in core cause AC through blue wire", just for that current to flow, you actually need to attach something to the yellow wire. Without connecting both ends of the yellow wire, it's pretty much as if it wasn't there. But you attach a load to that yellow wire, and suddenly, the yellow wire drains the energy the blue wire puts in from the magnetic field in the core. That in turn means the blue wire doesn't "see" such an opposing force.

That's a transformer, right there!

And that's why you have that: through choice of how you connect the yellow wire, and how many windings you give it, you can effect things just as building a *balun*, or (or and!) an impedance transformer.

That's exactly what you have here: This piece of engineering transforms the load that an RF signal experiences when you apply it at the antenna feedpoint to something that's what your cabling expects (50 Ω, probably).

So, no, don't change it. It's crucial!

## Answer (score 4, by Ryuji AB1WX)

That is a 4:1 Ruthroff voltage transformer, wired correctly. Don't alter the circuit unless there is a reason to (e.g. you want different impedance ratio).

DC continuity does not mean good or bad. What matters is how it operates (or not) at the operating frequency.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23499/is-this-an-unintended-short-circuit-in-my-moonraker-gpa-80f-vertical-hf-antenn, by Adam Soltys, Marcus Müller, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
