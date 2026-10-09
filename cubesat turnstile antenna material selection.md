# cubesat turnstile antenna material selection

*Tags: antenna, antenna-construction, satellites · score 8*

## Question

My cubesat team is working on our design for rolled whip antennas to deploy in a UHF turnstile configuration based on this design:

What I would like advice on is the material for the antennas themselves. Spring steel has ideal mechanical properties, but isn't an optimal antenna metal. The material of the one shown is apparently Nitinol shape memory alloy, that will unroll itself when heated. What other metals would you suggest looking into further?

The system characteristics are

- 435 MHz
- Under 50kHz BW
- 4W max power

## Accepted answer (score 5, by Marcus Müller)

As usual, for antennas, the better your material conducts, the higher your antenna efficiency. Hence, go for copper. It has an excellent conductivity per volume (which might or might not be critical in your application), and there's not many metals that will beat its conductivity at all. Steel really isn't good for that.

If you're using suitable frequencies, steel wire with a copper coating might work for a dipole. The frequency will define your skin depth and the losses that a non-perfectly conducting antenna will incur. Definitely sounds like you'd have to just copper-coat some spring steel and try.

Another thing: I don't know how stiff the deployed antenna will be, but you *are* in the earth's magnetic field, with long ferromagnetic rods; that will excert a torque on your satellite... I can't calculate how much, though, since I know nothing about your antenna sizes, your orbit, your height or anything about the satellite.

Generally, when asking about "what's the perfect material for my antenna", you should include a lot of factors:

- frequency (which I find kind of obvious)
- bandwidth
- acceptable loss
- power
- mechanical forces

## Answer (score 3, by Dave Tweed N3AOA)

I think the mechanical properties for proper deployment are much more important than the electrical properties.

The picture appears to show elements that are flat tapes rather than round wires, which is probably a good idea. I'm thinking that if the tape can be given a slightly U-shaped cross-section (like a steel measuring tape), it will be better able to fully straighten itself after deployment, and may allow you to use thinner (lighter) steel stock.

And as Marcus says, plating the steel with copper and/or silver will improve its electrical characteristics without compromising its mechanical characteristics.

I'm trying to figure out the deployment mechanism, but the picture is a bit fuzzy. There are little plastic doors holding the coiled elements in place, with spring-loaded threads holding the doors closed. Are those pairs of SMD resistors designed to heat up and cut the thread for deployment?

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6750/cubesat-turnstile-antenna-material-selection, by Kontakt, Marcus Müller, Dave Tweed N3AOA. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
