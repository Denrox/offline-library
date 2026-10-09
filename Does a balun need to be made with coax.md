# Does a balun need to be made with coax?

*Tags: coaxial-cable, balun, toroid · score 9*

## Question

## The short version

My understanding is that one of the main reasons to use a balun with coax is to prevent the outside of the shield from becoming part of your antenna system. If that's the case, won't a design like the one pictured below be ineffective? Can't current flow to the outside of the shield at the coax connector, before the windings?

## The long version

I'm new to the HF bands. My understanding is that baluns are good practice when feeding a dipole from coax (or any balanced system from an unbalanced one)--the idea being to ensure the currents on the two conductors are equal and opposite. With coax in particular, due to skin effect, the inside and outside of the shield act as different conductors. The inside is balanced with the center conductor, but the outside of the shield is not balanced with anything, so any current there causes undesired radiation. A balun ensures all the power goes to the antenna, not to the outside of the coax (and also works the other way, preventing undesired signals from being picked up by the outer shield).

At least that's my understanding.

I've seen a few designs for baluns, and I'll describe a couple here. The first two make sense to me, but the third doesn't, and I'm wondering why (or if) it really works.

**Design 1: A section of coax with one or more ferrite beads**  
The effectiveness would obviously depend on the beads used, but this would act as an inductor and impede RF on the outer shield, while the currents inside the shield would remain unaffected and balanced.

**Design 2: A coil of coax**  
This can be air-wound or on a core. Either way, similar to #1, inductance blocks RF on the outside of the shield while currents inside the shield pass through.

**Design 3: Parallel wires wrapped around a core (see picture below)**  
This is the one that doesn't make sense to me. The windings would block common-mode currents, sure. So I suppose your antenna would be fed a balanced signal. But the coax ends before the windings. Wouldn't that mean RF can still flow to the outside of the shield?  
(From http://www.m0pzt.com/baluns/)

### Some sources:

- ARRL The Doctor Is In podcast - All About Baluns
- Baluns: What They Do and How They Do It (ARRL)

## Accepted answer (score 8, by Phil Frost - W8II)

I'll explain the operation of that balun very briefly: for the differential mode (which by definition has equal but opposite currents on each conductor), each conductor induces an equal but opposite magnetic flux in the core. These magnetic fluxes cancel, and so the differential mode sees no inductance: it's as if the core and the windings aren't there.

Meanwhile the common mode interacts with the core like an ordinary, single wire, and sees a large inductance. This high inductance makes the common mode on the coax a high impedance (hopefully) relative to a lower impedance path like radials, the other arm of a dipole, or some other deliberate counterpoise.

But I think your question isn't really about how it works. Rather, it's a mental hangup right here:

With coax in particular, due to skin effect, the inside and outside of the shield act as different conductors.

So, I bet you are thinking that with the balun pictured in your question, the end of the coax is "exposed", and that means common mode current can "get in", causing problems. You may be thinking once the common-mode current is inside it's stuck there, isolated from the outside by skin effect. With coiled coax or coax through beads the integrity of the coax is maintained, so nothing can "get in".

I remember reading statements like that many times when I was trying to wrap my head around these same concepts, and I found them very misleading.

As a matter of fact, the shield is one conductor. So if someone says it's acting like two different conductors, what are they trying to say? Is it *really* like two conductors? If we can make one conductor behave like two, couldn't we exploit that to reduce the number of conductors required for all kinds of cable assemblies? And having established one conductor can behave as two conductors, are those two resulting "conductors" subject to the same rule? By repeated division, could we make one conductor behave as any number of conductors? If the shield is already like two conductors, why do we need a third inner conductor?

This seems highly suspect to me. I think it's a terrible phrasing of a property that does more to cultivate incorrect ideas than anything else. Here's how I'd put it:

*The current on any transmission line can be considered the superposition of a differential mode and a common mode.*

The neat thing is you can analyze each separately and independently, then add the two together and get the same result. I think that's what the statement about skin effect is trying to say. And the fact that the common mode ends up on the outside of the shield, and the differential mode on the inside is just a bit of physics trivia.

It isn't that the balanced mode current is flowing on the inside that prevents it from radiating: it's that it's cancelled by an equal and opposite current (and voltage) on the inner conductor. Look to balanced twin-lead transmission lines for a counter example: the current isn't "concealed from our view" by any kind of shield. And yet, they don't radiate because the [equal but opposite fields in each conductor cancel](Why%20must%20twin-lead%20conductor%20spacing%20be%20small%20to%20avoid%20radiation.md).

The advantage of coax over twin-lead is that outside the shield, the cancellation of balanced mode fields is complete, whereas for twin-lead we need to go away some multiple of the conductor spacing before that happens.

Let's consider a cross-section of coax with equal but opposite charges on the center and shield, and the associated electric fields:

Added together, there's no field at points outside the shield. That the charges are on the inside of the shield is really not the primary thing to be thinking about, because if the charges on the inner conductor went away, the charges on the shield would migrate to the outside.

And so getting back to your question about the balun, you don't need to be concerned so much with the distinction between the inside and the outside of the shield. Rather, think about maintaining equal and opposite currents and charges on the shield and center. If you do that, the fields will cancel like this, and the coax won't radiate.

## Answer (score 5, by Hamsterdave)

Short answer: No, and in fact you'll often get more bang for your buck by *avoiding* coaxial baluns.

The description of the balun's purpose in an antenna system you quote is an oft repeated bit of "common wisdom" in ham radio, but it is such an over-simplification that it is at best drastically misleading and at worst, just plain wrong.

The purpose of a balun in an antenna system is to suppress common mode current. That's it. You can (and should) use them on balanced line, even when feeding it with a balanced tuner. You can (and should) use them on balanced, resonant antennas like dipoles that are fed with unbalanced feedline, even if the SWR is perfect. You can (and should) use them between an unbalanced vertical antenna and a coaxial feedline. (A side note: Virtually every ham radio antenna system *should* have some form of common mode suppression mechanism installed, regardless of antenna or feedline type).

The coax shield behaves as two (mostly) independent conductors. The center conductor of the coax is "driven" by the radio, while the shield is held at ground potential. Because the coax shield has a non-zero impedance (there's some amount of resistance and reactance present, because thermodynamics), and because the inner layer of the shield is strongly coupled both inductively and capacitively to the center conductor, a current is induced on the inside of the coax shield that is, in theory, equal in magnitude and opposite in phase to the current on the center conductor.

These two fields exist in close proximity and we hope they are precise opposites of each other, so the two fields effectively cancel each other out, preventing the feedline from radiating. **This pervasive idea that the coax shield behaves as a grounded Faraday cage is just flat out wrong**. Faraday cages do not work in the near field, and the shield is most DEFINITELY in the near field of the center conductor. Also, there has to be a return path, so the shield **must** carry some amount of current.

Notice that when I mentioned the cancellation of the two opposite fields, I specifically stated that the current was flowing on the *inside* of the coax shield. This is because skin effect causes the inside and the outside surfaces of the shield to behave as two separate conductors, connected to each other through a relatively high impedance resistor. Exactly how high the impedance of said virtual resistor is depends on the electrical and physical characteristics of the feedline, such as characteristic impedance, capacitance, length relative to frequency, and many other variables.

In an ideal world, the outside of the coax shield would have a nearly infinite impedance between it and the inner coax shield. This is because any current flowing on the outside of the coax shield cannot interact very efficiently with the current flowing on the center conductor of the coax, meaning that the field generated by the current flowing on the outside of the coax shield is not cancelled out by any other fields. *Any current flowing on the outside of the shield is free to radiate*.

This also means that any current induced on the outside of the coax shield from external sources, such as a noisy appliance power supply in your home, will be free to travel back to your radio, where it will induce current on the chassis of the radio. A significant fraction of complaints about RF noise received from within the ham's own home can be tracked back to common mode currents entering the receiver via the coax shield.

Now that we know that a coax cable behaves more like 3 conductors, not 2, let's look at how that works with a coaxial balun.

If we take a few feet of coax and wrap it around a ferrite toroid, the fields generated by the center conductor and the inside of the coax shield are still cancelling out, nothing much has changed inside the coax. They're still in very close proximity, and Ohm's Law says that if the current is going out through the center conductor, some of it has to be coming back in via the coax shield. However, we *have* suddenly put the outside of the coax shield in very close proximity to the ferrite toroid, and there is no opposing field to cancel the field generated by the current on the outside of the coax. Any current flowing there will couple to the toroid, primarily inductively, and a magnetic field (and current) will then be induced **on the toroid**. It becomes an electromagnet. If the toroid happens to be very good at turning energy at the frequency that's passing through the coax in to heat, then much of the current flowing on the outside of the coax will turn to heat rather than making it back to the radio, or out to the antenna, while anything flowing on the inside of the coax shield or the center conductor continues on mostly unaffected.

There are some problems with using coax for toroid baluns. The two biggest are:


Coax doesn't like to make sharp bends, so larger loops have to be made, resulting in less inductive coupling. This usually means you have to use several toroids stacked together, and a significant length of coax.


Coax isn't very good at dissipating heat. This means that if the toroid is turning lots of common mode current in to heat to get rid of it, and you've covered up most of the toroid's surface area with coax, things could get quite hot, potentially hot enough to damage the coax.


Coax baluns that don't use toroids or iron cores cannot provide sufficient common mode suppression on multiple bands, particularly if the antenna has a high impedance or poor match on one or more bands. You should be aiming for a bare minimum of 1,000 ohms of common mode impedance (>2,000 is best), but air core "ugly baluns" typically struggle to achieve more than 500 ohms even on their designed band. On other bands, it can be even lower. The characteristic capacitance of the coax causes an ugly balun to behave like a resonant band reject filter from the common mode current's perspective, not like a broadband choke.

So the problem is not that there is current on the outside of the coax shield, the problem is that the current on the outside of the coax shield is unopposed. If we were to solder two wires to a bit of coax, one to the shield and one to the center conductor, then wrap those two wires around a ferrite toroid as your image shows, the current on the two wires interact with the toroid about equally. If the two wires were carrying unequal currents, they wouldn't cancel exactly, and a magnetic field would be induced in the toroid. By selecting materials that are very lossy at the frequency of interest, the balun can be used to dissipate **only the portion of the current that is unopposed**. If 10 watts were flowing on the center conductor, but only 8 watts were flowing on the shield in total, a field equivalent to 2 watts would be induced on the toroid and turned in to heat. At that point the current on the two wires is once again balanced, and no current will appear on the coax shield, because there is no unopposed component remaining.

Imbalance in antenna systems is virtually universal. They are *designed* to radiate, which means they must, by their nature, couple heavily to their nearby environment. This inevitably means that the antenna system will be prone to picking up local common mode noise, as well as generating common mode current due to asymmetry in the antenna system. A balun is a way to ensure that the current on the two conductors is equal and opposite, nothing more or less.

Wire baluns have their own set of challenges, mostly heat related:

- Toroids are even worse than coax at dissipating heat. If you want good choking in a coaxial balun, you'll need multiple toroids, meaning more surface area and more mass to handle waste heat. With a wire balun, it is quite possible to get excellent choking impedance from a single large toroid, but the same amount of power is dissipated, meaning that the toroids can become *very* hot. A single core, wire balun should not be used for more than 250 watts unless you can see with a fairly good degree of certainty that your system is not generating excessive common mode currents.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6983/does-a-balun-need-to-be-made-with-coax, by Dominick Pastore, Phil Frost - W8II, Hamsterdave. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
