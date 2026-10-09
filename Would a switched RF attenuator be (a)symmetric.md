# Would a switched RF attenuator be (a)symmetric?

*Tags: equipment-design, rf-power, testing, electronics · score 3*

## Question

I picked up this 0-80 dB switched RF attenuator at a flea market, with no part number or other useful markings other than the knob settings. I've tested it and confirmed that it works, but there's one thing I'm uncertain about which I don't have the theory to be certain of and can't test non-destructively:

Is there potentially **a difference between "input" and "output" ports**, or is it symmetric? In particular, would there possibly be better or worse **maximum power handling** capability depending on which way around it's connected? If there is a difference, how can I tell which port is which? (They aren't labeled.)

I'm interested in answers which are either general, for all reasonable designs of attenuators, or specific to this unit if you should happen to recognize it. (I have used Google Image Search to try to find things which look like this specific model and haven't succeeded. According to the seller, it was likely an internal module from equipment made by HP.)

If it's unlikely that there's a significant difference, then I'm happy to go ahead and use it as I intend (testing transmitters hooked up to receivers with no antennas involved, no more than 5 watts, not continuous) but if it matters I'd like to use it properly and have less chance of burning it out. (This was cheap, but apparently comparable new units are in the hundreds of dollars.)

## Accepted answer (score 2, by mtrberzi)

From http://urgentcomm.com/mag/radio_demystifying_rf_attenuators:

...[A]ttenuators are symmetrical, provided the input and output impedances are the same. In applications where attenuators are used as impedance-matching devices, they are not symmetrical.

A typical attenuator circuit will be a purely resistive network - for example, this pi-network for a balanced attenuator:

Since both cables coming out of your attenuator are identical and use the same connector, we expect Z1 and Z2 (the impedance seen "looking into" each cable) to be equal. What makes things interesting in your case is where the variable resistor (controlled by the knob) is connected. In that case, the most likely design for your attenuator is this T-type network:

In this case the most likely location for the variable resistor is at component Rp, so no matter how the attenuator is connected, both Z1 and Z2 are symmetric and Rp performs exactly the same function in the circuit.

To summarize, for this particular case there should be no difference with respect to how your attenuator is connected - either "direction" will be fine. In general, it will depend on the input impedance at each connector.

Edit: The answer so far assumes ideal components, but for a real attenuator the power rating of each resistor is important as well. For a mass-produced attenuator, the most likely case is that the power rating is symmetric as well (although presumably unknown). This is because of the "economy of scale": using two identical resistors in a circuit is cheaper and easier to design (you only have to do power calculations once but you can use the circuit twice) than using two resistors intentionally chosen to have different power ratings. For this specific attenuator, since it may have been manufactured as a bespoke (one-off) system and not sold commercially, this may not necessarily apply, but it is still the most likely case for the same reason (it's easier to design the circuit that way).

(Image credit: http://en.wikipedia.org/wiki/File:Pi_type_balanced_attenuator_circuit.jpg, http://en.wikipedia.org/wiki/File:T_type_balanced_attenuator_circuit.jpg)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2144/would-a-switched-rf-attenuator-be-a-symmetric, by Kevin Reid AG6YO, mtrberzi. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
