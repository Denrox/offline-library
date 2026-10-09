# Why is the neper a useful unit for transmission line calculations?

*Tags: math · score 6*

## Question

[SWR Measured at the Transmitter versus SWR at the Antenna](SWR%20Measured%20at%20the%20Transmitter%20versus%20SWR%20at%20the%20Antenna.md) says the neper is "a more convenient unit for transmission line calculations".

Why exactly? What is a neper, and what about it makes it more convenient than the more common decibel? Are there some examples of equations which are more complicated in decibels?

## Accepted answer (score 7, by Glenn W9IQ)

A neper, just like a decibel, is a logarithmic expression of ratios. The decibel uses the base-10, or decadic, logarithm while the neper uses the natural, or Euler constant, logarithm.

The decibel is strictly defined as the ratio of two powers.

$$dB=10\log_{10}\left(\frac{P_1}{P_2}\right) \tag 1$$

While it is common to see a decibel formula based on voltage or current, such a ratio is only valid if the impedance of the two terms is the same.

The neper is simply defined as the ratio of voltage or current (or more generally, 'field' values):

$$Np=\ln\left(\frac{V_1}{V_2}\right) \text{ or } \ln\left(\frac{I_1}{I_2}\right) \tag 2$$

It can be shown that 1 neper is equal to $20\log_{10}(e)$ or about 8.6858 decibels.

One way to think about a natural logarithm is that it can be used to calculate how much time it takes to get a certain growth. The inverse function, e, can be used to calculate growth given a certain amount of time. In fact e is sometimes referred to as the universal rate of growth.

This has many applications in the area of electronics. As an example, the formula for voltage across a capacitor as a function of time (growth/decay) as it discharges through a resistor makes use of this relationship:

$$V_C{(t)}=V_0*e^\left({\frac{-t}{RC}}\right) \tag 3$$

where R is the discharge resistance in ohms, C is the capacitance in Farads, t is the time in seconds, and V0 is the initial voltage across the capacitor.

Similarly transmission line equations have the notion of growth or decay of voltage and current as a function of time or length. Transmission line attenuation is such as example. The attenuation of a transmission line ($\alpha$) is generally given as nepers/meter or nepers/kilometer. Thus for a given length of transmission line, the attenuated voltage at any point along the line is simply given as:

$$V_{(l)}=\frac{V_0}{e^{\alpha l}} \tag 4$$

where V0 is the original voltage, $\alpha$ is the attenuation in nepers/meter, and l is the point in the transmission line in meters from the initial voltage V0.

The same form of the calculation using attenuation expressed in dB/meter results in:

$$V_{(l)}=\frac{V_0}{e^{\left(\frac{\alpha l}{8.6858}\right)}} \tag 5$$

where $\alpha$ is expressed in dBs/meter.

An alternative form to equation 5 would be:

$$V_{(l)}=\frac{V_0}{10^{\left(\frac{\alpha l}{20}\right)}} \tag 6$$

where again $\alpha$ is expressed in dBs/meter.

Thus it can be seen that equation 4 is slightly simpler in form compared to equation 5 or 6. The simplicity of equation 4 also makes the derivation of the "rate of growth" clearer. There is no need to ask, for example, what is the 8.6858 factor doing there?

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9759/why-is-the-neper-a-useful-unit-for-transmission-line-calculations, by Phil Frost - W8II, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
