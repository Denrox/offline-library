# How do I determine antenna spacing?

*Tags: antenna · score 5*

## Question

How do I determine antenna spacing so that I don't end up overdriving the front end of a receiver when transmitting?

## Answer (score 5, by Dan KD2EE)

If the antennas are at least one wavelength apart, you could use the Friis transmission equation. This would allow you to determine, based on the power of the transmitter and the antenna gains, the power at the receive antenna. Subtract out any loss due to cables or duplexers.

Now you need to check two parameters of the reciever: the sensitivity and the specificity (may also be called adjacent channel selectivity). The sensitivity will be given in microvolts and is the weakest signal the reciever can understand. The specificity will be given in decibels and is the maximum ratio between a strong nearby signal and the desired signal that will allow the radio's filters to filter out the nearby signal on a different channel. Convert the receiver power from watts to volts using $$ V=\sqrt{P\times{}R} $$ and $R=50\Omega{}$. This is the voltage at the receiver caused by your nearby transmitter. Finally calculate the ratio between the two voltages - the one you just calculated and the sensitivity. Use the equation $$ 10 \times \log{\frac{V_1}{V_2}} $$ to calculate the ratio in decibels. If this ratio is less than the specificity (ideally by a good margin of error), then you're good. If the ratio is greater than the specificity, or they're within about 10dB from each other, then you may not be able to receive signals over the noise from the other nearby transmitter.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/141/how-do-i-determine-antenna-spacing, by Timtech, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
