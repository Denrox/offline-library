# Are used PolyPhaser IS-50 RF surge protectors likely to work?

*Tags: lightning · score 3*

## Question

I'm looking at buying a used IS-50NX-C0:

The listings usually say something like "Used, pulled from working equipment." While I'd believe they still work as far as normal operation is concerned, I doubt the sellers have tested their surge suppression capabilities.

I can't find much information on what's inside these things. Does it wear out over time? Can it withstand multiple strikes? Or is it likely what I'd be buying is a unit that's already toasted?

## Accepted answer (score 4, by Glenn W9IQ)

The Polyphaser consists of a DC blocking capacitor in series with the radio and a gas discharge element in parallel with the antenna.

The Polyphaser can normally withstand multiple <20 kA strikes without failing. Unfortunately, in the far majority of the cases, the gas discharge element fails in an open state. There is therefore no practical, absolute test of the the functionality of the device. Polyphaser advises that a change in SWR would be an indicator of failure.

## Answer (score 2, by Phil Frost - W8II)

Polyphaser sent me a document on request. Salient points:

The only way to test the IS-50 or IS-B50 without expensive test equipment is by seeing if the VSWR (return loss) has increased or remove it from the line and see if the radio performance is better. Because the product is a DC block device, there is no way to test adequately with a multi-meter. A properly running product will test the same as a bad one. Normal operation, with an ohm meter you will get a short between pins and short between any pin and the housing (ground). The same results if the gas tube has failed. 95% of the time a gas tube will fail open which is also its normal state.

[...]

Since lightning is a natural event with varying current waveforms and return strokes there is no way to predict the gas tube lifetime. The current IS-50 series has been in production since 1993. It is a very reliable product. The first indication of impending failure will be increased insertion loss and SWR. The protector should be replaced immediately if insertion loss and SWR are greater than a straight through coax barrel connector (female to female) as full failure may or may not pass RF.

[...]

The MTBF (Mean Time Between Failures) is also effected by where and how the protector is installed and the natural variation in the intensity and number of return strokes per lightning event. The tower size, placement, ground conductivity, and number of storms per year can also affect MTBF. The gas tube manufacturer can provide raw data on gas tube failures, but in the real world, it’s relatively meaningless. The good news is the gas tubes will probably withstand 5 hits of 20KA each, but the N connector center pin will be damaged with the first 20KA hit. Good news? Yes, since it is obvious that the protector has done its job and should be replaced. How often could this happen? Probably never. That much current could only ride on the shield, and indicates a failure to properly ground the coax cable shield or a poor tower ground connection.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9042/are-used-polyphaser-is-50-rf-surge-protectors-likely-to-work, by Phil Frost - W8II, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
