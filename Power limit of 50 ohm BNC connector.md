# Power limit of 50 ohm BNC connector?

*Tags: rf-power, connectors · score 8*

## Question

Is there a limit to the power a 50 ohm BNC connector can handle?

## Answer (score 7, by Dan KD2EE)

Note that the following may not apply to adapters, which may have lower power limits.

This thread on eham contains a few suggestions. The third poster states that the design rating is 7 amps on the center pin, or 5 amps accounting for skin effect at different frequencies. This corresponds to 1250 watts for a 50 ohm feedline with a matched load.

There is a 500 volt maximum rating, but this is not the best basis. This is based on the dielectric (insulator) effect between the pin and shell, not on the maximum power dissipation. The 1250 watt figure is based on the amount of heat that will be generated if 5 amps is run through the connector. Heat generation is the relevant effect when we're talking about maximum power, because that's what's going to melt the coax and light your shack on fire.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/132/power-limit-of-50-ohm-bnc-connector, by Timtech, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
