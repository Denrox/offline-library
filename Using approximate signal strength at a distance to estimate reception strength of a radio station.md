# Using approximate signal strength at a distance to estimate reception strength of a radio station

*Tags: propagation, rf-power, history, physics · score 3*

## Question

I have some historical data on radio stations, but unfortunately, the dataset only has these variables:


the power of the transmitter, in watts


the coordinates of the radio tower

Unfortunately, I don't have **any** data on the characteristics of the antenna(s) or the radio towers themselves, e.g. their height. Anecdotally, the frequencies of these stations are from 500 to 1500 kilocycles, which I believe are AM frequencies.

I asked a similar question on the physics.SE and was told that, with an example of a 500 W transmitter, I can *very* roughly estimate the strength at a distance of, say, 10 km, as

At a distance of $10km$, that power is uniformly distributed over a sphere of radius $10km$. In other words, the power per $m^2$ will be

$\frac{500}{4 \pi r^2}$ in units of $\frac{watt}{m^2}$.

In this example, this gives me approximately $4 \times 10^{-7} \frac{\text{watts}}{m^2}$, or -33.98 dBm per square meter.

With that number in hand, is there anything I can say about a receiver's ability to pick up that signal? As in, a standard household radio receiver in the 1920s could, on average, audibly receive signals down to strength -25 dbm, so it probably wouldn't be able to pick up this signal?

Or is the more appropriate way to convert this power into $V/m$ and use an approximation of the audible area like in this article?

**(Yes, I know this is an overly simplistic approximation; I'm trying to do the best I can with the extremely limited data that I have. It was recommended that I ask here, so any information is most welcome!)**

## Accepted answer (score 3, by Glenn W9IQ)

We have some clues from a historical perspective. In the January 1917 edition of *The Radio Experimentor*, author H. Winfield Secor noted that approximately 50 kW (kilo-watts) of transmitter power was required to reach a 3,000 to 4,000 mile range with CW. He then went on to note that 10 μA (micro-amperes) is considered a weak receive signal while 20 μA is a strong signal. He also recorded an important fact that 10 μA is equivalent to 0.01 μW (micro-watts). From this we can calculate the input impedance:

$$Z_{in}=\frac{P}{I^2} \tag 1$$

where P is the power in watts and I is the current in amperes.

So we see that the apparent input impedance that supports Secors statistics is 100 ohms. We can then re-arrange equation 1 to return watts based on amps:

$$P=Z_{in}*I^2=100*I^2 \tag 2$$

Using equation 2, we can then translate the 10 μA field signal level to 0.01 uW or -50 dBm and the 20 uA signal to 0.04 uW or -44 dBm since:

$$dBm=10 \log \left(\frac{P}{0.001 watts}\right) \tag 3$$

where dBm is the decibels compared to 1 mW (0.001 watts).

Just as a basis for comparison, modern radios easily achieve 0.25 μV (micro-volt) MDS (minimum discernible signal) sensitivity across a 50 ohm input impedance. We compute power in this case as:

$$P=\frac{E^2}{R} \tag 4$$

where E is the voltage in volts.

This is equivalent to 0.00125 pW (pico-watts or 10 watts) or -119 dBm.

Secor does not make it clear if his references are the input currents to the receiver or if this is the field strength (the square root of irradiance) in the field of the receiver antenna. But the basis of the article was to assemble a compendium of competing methods of detection so I believe it would be safe to say that this was the required current at the input to the receiver terminals. Supporting this notion is the clarifying note from the author: '*Technically speaking, radio detectors are usually rated by the amount of electrical energy in ergs necessary to actuate them.*' when he was referencing the earlier listed micro amperes.

To compare your tabular data with this historical reference, you would need to presume that the equivalent receive and transmit antenna gains for the path in question are used in the comparison. You would also need to presume that the path loss is equal. Then, as you noted in your question, you can compare potential distances simply as a function of power and the inverse of distance squared.

Do note that Secor's article is based upon CW transmissions so AM detection may have different statistics. Also note that during the 1915 to 1930 period, there were significant advances in detector technology and receiver architectures. As a result, there could be a significant error range in your estimates depending upon the exact period of comparison.

## Answer (score 3, by Richard Fry)

The methodology needed to accurately calculate the radiated r-f power needed to generate a given field intensity at some distance along a terrestrial path is highly complex — probably beyond the practical possibility of posting in an answer here, even in outline form.

However, the U.S. FCC has developed a set of propagation charts relating to this topic, which provide a fairly straightforward way of answering this question for frequencies in the AM broadcast band.

Below is a link to a paper based on those propagation charts. It includes some background information along with several plots showing the distance to a groundwave field intensity of 0.5 mV/m, which is about the minimum field needed by a consumer-level AM broadcast receiver with a built-in antenna, given sufficiently low co- and adjacent-channel interference from other AM stations, and a receive site having sufficiently low ambient r-f noise levels.

Factors in MW Signal Coverage

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11945/using-approximate-signal-strength-at-a-distance-to-estimate-reception-strength, by Michael A, Glenn W9IQ, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
