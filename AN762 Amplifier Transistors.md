# AN762 Amplifier Transistors

*Tags: hf, diy, amplifier, impedance · score 3*

## Question

According to the MRF421 or MRF454 transistor datasheets, used in the AN762 HF amplifiers say that the transistors are "100% tested for load mismatch at all phase angles with 30:1 VSWR".

Further, in the application note (page 9), they describe testing the amplifier with varying SWR and noted stable performance up to a 5:1 or 9:1 depending on the model.

Is it safe to operate an amplifier based on this design with an SWR measured between the amp and antenna of say 3:1, or are there other factors involved?

## Accepted answer (score 5, by Hamsterdave)

The tests they are referring to are for amplification characteristics like linearity and stability, not continuous thermal dissipation.

That said, unless you've constructed the thing in such a way that the transistor's thermal dissipation capacity is severely derated, it is very rarely heat that kills finals, at least in the short term. While severe and repeated thermal cycles caused by poor design or execution of the cooling system can cause mechanical stress that eventually cause the amp to fail, it takes exceptionally high temperatures to get the silicon itself to fail while it is operating within normal design parameters. Like, "burn your finger when touching it" high temperatures. When radios do fail from heat, it is quite often not the finals transistors themselves that fail, at least at first. Peripheral components such as capacitors and resistors are much more likely to go severely out of tolerance when temperatures really start to climb, though as those fail, they may take the finals with them as the circuit fails in a less than graceful manner.

High voltage is far and away the most likely killer of PA transistors in the short term. The 'cooking the transistors' scenario that everybody fears is a misconception that likely stems from the fact that high voltage and high temperatures generally occur under similar conditions, poor impedance matching, and high temperatures are usually far easier to spot than a brief arc.

Arcing can occur for a couple of reasons. Most often it is a failure in a high Q L/C tank somewhere in the antenna or feed system. Such tank circuits are present in filters, tuners, antenna loading systems, and band traps. If the antenna itself presents a very high impedance, or is simply absent due to an operator error, these high Q, resonant tank circuits can "ring", inducing *very* high voltage within the tank, often on the order of 1kV or more. The result is most often directly observed as a "burned" plate in a variable capacitor inside an antenna tuner, as the plate spacing of air variable capacitors is often the weakest link in the circuit. Many times this arcing is not fatal to the radio when it happens in some component along the transmission line/antenna chain, but it can be under the right circumstances. If this arcing occurs within the radio, or the circumstances of the arc in the feed/antenna chain allow the high voltage to travel directly back to the radio, the finals may be destroyed almost instantly as the high voltage literally burns through delicate internal structures in the transistor.

For a good example of high voltage appearing in high Q resonant circuits in ham radio applications, a magnetic loop antenna is a very good example. Voltage at the tuning capacitor can often exceed 2kV with just 100 watts input, nearly 10 times the typical peak voltage observed within a 50 ohm antenna system.

All of that said: Is 3:1 safe for your amp?

In all likelihood, yes, but be generous with the selection of your heat sink, use best practices for construction of filters and matching networks, and include a solid safety margin in voltage and temperature ratings when selecting all components

The reflected power will only be a few watts, and the maximum peak to peak (ignoring potential for ringing) voltage will only be about 100V higher than a 50 ohm load would generate.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6044/an762-amplifier-transistors, by user5418, Hamsterdave. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
