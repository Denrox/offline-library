# NanoVNA(v2)... what to capture for future reference when comparing past antennas?

*Tags: nanovna · score 3*

## Question

I'm designing a HF antenna that uses a portion of a downspout (electrically isolated from the gutters above and lower portion) as a bottom-loaded shortened quarter-wave vertical.

I'm about to trim the downspout down to what I'm planning to use as its final length, but want to cut off 2-3 inches at a time & capture a sweep at each length for posterity, just so I can document any "golden" length I encounter along the way & find it again in the future if I end up being dissatisfied with a shorter length. I'm also planning to document the performance of a vertical wire of comparable length hanging in the same location, to see whether I'd be better off replacing the 8-9 foot aluminum segment between the insulators with vinyl and hiding an antenna wire inside (or adhering 1" copper foil tape to the front & painting over it).

To that end... what 4 "format" values should I be capturing at my 4 marker-position frequencies of interest (10.08, 14.07, 18.13, and 21.07MHz)?


**SWR** is probably an obvious one


**SMITH** is probably another

... but that leaves two more available. Are there two other format values that, if captured, will ensure that I have all the information I'll need to derive any other values?


Real and Imaginary?


Resistance and Reactance?


Logmag, Phase, Delay, and/or Polar?

One obvious thing I think I want to have available is **Feedpoint Impedance** (ie, Z = r + jx), because (I *think*) that will allow me to design a coil+capacitor matching network to bring that particular length to 50 ohm feedpoint impedance for the frequency in question, and/or give insight into whether an unun would at least improve matters when used in conjunction with the radio's built-in antenna tuner (and if so, what ratio it ought to have).

I *thought* that was supposed to be what "Smith" conveys... but on MY NanoVNA (v2_2), at least, "Smith" shows the value as {resistance}ohms + {capacitance}(nano|micro)Farads.

So... if the values I really will need in the future are r + jx, can they be derived directly from the Smith value pair, or will I need to capture one or two other values (real, imaginary, resistance, reactance, or ???) to have the information I'll need to do it?

## Answer (score 6, by hobbs - KC2G)

The real+imaginary S11 and the frequency, *or* the resistance and reactance (R+jX) and the frequency, along with a known Z0 (which I think is always going to be 50 ohm for a NanoVNA), are enough to re-derive every other variable of interest for a single-port measurement, whether that's return loss, SWR, phase angle, or equivalent capacitance or inductance. So given those three things, you can get anywhere; anything else you capture (like SWR) is just for your convenience.

## Answer (score 2, by hotpaw2)

A nanoVNA will sweep 101 frequency points. So I would sweep a frequency range that includes the entire band, for each of your radio bands of interest.

You can connect to the nanoVNA via its USB serial port, and send it commands. The “frequencies” command will print out a list of frequencies swept. The “data” command will print out a list of IQ values for the entire swept frequency range. Save these to a file. You can convert your frequency and IQ tables into an either a Smith chart or an SWR plot, using a spreadsheet or etc.

There may be software utilities that automate this, but I’ve downloaded the data manually, and used a Basic program or Python notebook to do the plotting.

Then I compare plots of my antenna changes to see whether I made things better or worse, and where across the entire band.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18447/nanovna-v2-what-to-capture-for-future-reference-when-comparing-past-antennas, by Bitbang3r, hobbs - KC2G, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
