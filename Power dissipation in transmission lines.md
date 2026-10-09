# Power dissipation in transmission lines?

*Tags: rf-power, feed-line · score 7*

## Question

I was wondering, does the impedance of a transmission line have any effect on the power it dissipates? I'm familiar with the fact that an impedance equal to the load will provide maximum power transfer (and dissipate just as much power as the load) but guess that's of no bearing when talking about transmission lines? If a line is rated as 50 Ohm, does it have any impact on power dissipation?

## Accepted answer (score 6, by Dan KD2EE)

No. The cause of power loss in a feed line is not due to the characteristic impedance, it actually varies among transmission lines of the same impedance. Otherwise all 50 ohm coax would be the same - but there are many different types and qualities of cable. The actual loss is measured not in ohms but in decibels per foot, and varies with both the type of cable and the frequency in use (with higher frequencies having greater loss, due to skin effect). If you need to get the loss of a particular cable, or compare two cables, you should get a chart or table from the manufacturer. This table lists some common types of coax at a variety of frequencies.

The 50 ohm value being described is not the impedance of a circuit element, which is a word for the complex form of resistance. It has a 50 ohm characteristic impedance. It's still the ratio of the voltage to the current, but in this case of a wave travelling down the core and back along the shield. It's a property of how the line behaves in response to a wave travelling through it, and it's important because if it doesn't match at any given connection, since current coming in must equal current coming out and that means the two sides would have different voltages, part of the wave is reflected to allow everything to even out. However even though it's measured in ohms, it is not related to resistive loss.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/469/power-dissipation-in-transmission-lines, by s3c, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
