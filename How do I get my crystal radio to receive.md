# How do I get my crystal radio to receive?

*Tags: antenna-construction, grounding, crystal-radio · score 3*

## Question

My 8 year old and I are trying to figure out how to get this crystal radio we made working. It's based off this youtube video. We get clicks when we put the crystal ear piece either side of the resistor but nothing more yet.

My son tried a really long aerial, wire winding all around the house, and for ground he had a wire hooked to a bolt pushed into a pot with dirt. (However I'm not sure whether we actually tried both these at the same time!)

Why does it need a ground, and will it work without one?

How long does the aerial need to be?

Does the covered copper coil need to be thinner wire? Whats the relationship between the wire size and amount of turnings, and the length of arial needed? We have about 200 windings.

Would be great to understand this a little bit more and actually get it working.

Here's some photos:

## Answer (score 5, by Glenn W9IQ)

This design of a crystal radio relies on the capacitance of the antenna and the inter-winding capacitance of the inductor as well as the inductance of the inductor to form the tuned circuit. The length of the antenna can therefore play a role in the ability to tune in AM stations.

I agree with Mike regarding the soldered connections. Go through them all again and reheat and apply solder. Your annealed wire must be scraped or sanded down to bright, bare copper wherever there is a connection unless your annealing is the self melting type.

It appears from your picture that your slider bar on the inductor is not making electrical contact with the coil. That area on the top of the coil must also be sanded to expose the bare copper. The slider bar itself does not appear to be a good conductor - a brass rod would be a better choice.

For longer term reliability, you may wish to use brass screws and washers throughout. You can also solder to these if you wish to make it bullet proof.

The selection of the diode can make a big difference in performance. A 1N34 or a Schottky diode are good choices.

You mentioned that you have connected a ground wire but this is not visible in your pictures. It should be attached to the coil on the end opposite from the antenna.

## Answer (score 3, by Mike Waters)

A bolt pushed into a pot full of dirt will never work! *You need a ground return to planet earth itself* for your crystal radio. :-) This could be as simple as the screw on a plastic cover that holds an electrical outlet in place. That's what I did when I was a kid.

Also, some of those connections look "iffy". Make sure they are all making contact with an ohmmeter set at the lowest resistance scale (unless you have one with an auto-ranging feature).

You can also use a copper-clad steel rod --available from hardware stores, home improvement stores, or electrical supply houses-- driven into the earth. Use an ordinary stainless steel hose clamp or (more expensive) a bronze clamp made for the purpose.

## Answer (score 3, by Andrea Richards)

I am no expert on House Wiring, but when mine was done, all the pipes in the house (central heating and water) were all grounded for safety reasons. I believe these were all connected to the main ground in the electrical cupboard where the meter is and the electrician checked to make sure it was a "good earth". So if you see the Green/Yellow wires attached to your water pipes (copper ones), then attaching an earth to one of those may suffice. I have know amateurs to place a metal spike in the ground and keep it watered in the dry months.

I agree with the others that the winding does need to have the insulation removed to make a good contact with the slider. There has to be a circuit here, not an open circuit.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9930/how-do-i-get-my-crystal-radio-to-receive, by Agent Zebra, Glenn W9IQ, Mike Waters, Andrea Richards. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
