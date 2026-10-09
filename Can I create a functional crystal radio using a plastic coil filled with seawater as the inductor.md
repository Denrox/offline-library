# Can I create a functional crystal radio using a plastic coil filled with seawater as the inductor?

*Tags: receiver, crystal-radio · score 4*

## Question

Pex is cheap and comes pre-coiled,

3/8" pex is 0.360" ID.

1/2" is 0.485" ID

Fill with "sea water" using distilled water and sea salt to proper concentration.

Use for AM and/or Shortwave coil.

Sea water is HIGHLY conductive and interacts with radio waves.

I need some suggestions for the size of the coil and how many turns, I intend to test it.

I'm within 2 miles of a couple radio stations, @ ~1100 and ~1400 so sensitivity issues will be minimal.

## Answer (score 5, by Phil Frost - W8II)

Sea water is not that conductive: about 5 S/m. By comparison, the conductivity of copper is about 60000000 S/m, so seven orders of magnitude more conductive.

The low conductivity of sea water will effectively appear as a resistance in series with the coil. This will increase losses in the coil, reducing sensitivity.

But worse, it will decrease the Q factor of the LC filter, reducing selectivity. The resulting "radio" would be incapable of tuning to an individual station. Perhaps this isn't too much of a concern, since given the sensitivity issues you will have to be very close to a transmitter to hear anything, at which point that single transmitter is probably the strongest source of RF around.

I guess technically we could call this a "radio", though by this definition you could attach just about anything conductive to a diode and call it a radio. For any practical application, copper (or really, most metals) is a better choice: it's smaller, cheaper, electrically superior, non-corrosive, and solid at room temperature.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12432/can-i-create-a-functional-crystal-radio-using-a-plastic-coil-filled-with-seawa, by Aerothorn, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
