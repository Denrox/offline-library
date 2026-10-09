# What is the relationship between SWR and receive performance?

*Tags: antenna, impedance, antenna-theory · score 27*

## Question

If an antenna analyzer shows 1:1, does that mean it's an ideal receiver as well? And what about the converse, will a well performing receive antenna show a 1:1 SWR?

I've wondered this for a while, sometimes I want a wide band antenna just for listening, and I am not clear about this relationship.

## Accepted answer (score 21, by user)

If an antenna analyzer shows 1:1, does that mean it's an ideal receiver as well?

**No.**

Assuming we're talking about a characteristic impedance of 50 ohms, a 50 ohm resistor (otherwise known as a dummy load) will show a SWR of 1:1, although it will almost certainly perform very poorly as either a receive or transmit antenna.

The low SWR simply tells you that there are no impedance mismatches along the path from the transmitter (antenna analyzer in the case of your question) to the antenna feedpoint, at the current operating frequency.

And what about the converse, will a well performing receive antenna show a 1:1 SWR?

**Yes and no.**

*Yes,* a SWR of 1:1 means that [you aren't losing signal to impedance mismatch reflections](Why%20do%20I%20need%20to%20tune%20an%20antenna.md).

*No,* another issue is how efficient the antenna is at picking up the (desired) signal, preferably (especially in the case of directional antennas) while rejecting undesired signals as well. An antenna that is 5% of a full half-length dipole isn't going to pick up as much RF as the full-length dipole, let alone a full-sized directional antenna pointed in the proper direction, simply due to the much smaller physical (antenna aperture) size.

**Generally speaking,** if an antenna analyzer or (other) transmitter shows that the antenna output presents a SWR of 1:1, then *what you have* is probably about as good as it gets. *That does not necessarily mean that what you have is a good antenna setup* as exemplified by the extreme example of a dummy load.

## Answer (score 16, by Phil Frost - W8II)

Simplified answer:

*There is no relationship between SWR and receive performance.*

There is one condition for this simplification to be true: the received RF noise floor must be above your receiver's noise floor. Beyond this, anything you might do to increase the output from the antenna does nothing to increase the signal to noise ratio, which is a better measure of receive performance.

SWR is a measure of the impedance mismatch between your antenna and transceiver. Whether transmitting or receiving, a higher SWR correlates with a less efficient coupling of energy between the transceiver and antenna.

This inefficiency is problematic when transmitting because it can make a lot of heat, and it limits one's ability to overcome noise at the intended receiver. We could compensate with an amplifier, but high-power amplifiers are expensive, and big, and hot, etc. However when receiving, losses are easy to overcome. The heat generated is insignificant, and at the extremely low power levels involved in receiving, amplifiers are not large or expensive or difficult to design.

Remember also that losses attenuate the signal, *and also the noise equally*. Improving the SWR will increase the power received, but this is signal and noise, and thus does nothing to make the signal more intelligible, unless both are attenuated so much that most of the noise is no longer coming from the antenna, but instead from the electronics of the receiver. At HF, low-noise amplifiers are easy to design, and the ambient [RF noise floor is relatively high](How%20can%20I%20calculate%20the%20effects%20of%20an%20LNA%2C%20antenna%20gain%2C%20etc.%20on%20noise%20performance.md), so antenna efficiency (including SWR-related losses) is not usually the limiting factor in receive performance.

If you want a wide-band antenna for receiving, then you may do well with a non-resonant antenna. Such an antenna will be very inefficient, but this easily compensated with a low-noise amplifier. Because it is not operated at resonant frequencies, bandwidth is hardly a concern. A small loop or its electrical dual, the Hertzian dipole could work. Or, consider a Beverage antenna if you want directionality, which *does* increase signal-to-noise ratio, provided it's pointing in the right direction.

## Answer (score 3, by KE3FL)

"If an antenna analyzer shows 1:1, does that mean it's an ideal receiver as well?" - It means for this antenna for the frequency you've tested on the antenna is as good as it gets.

"And what about the converse, will a well performing receive antenna show a 1:1 SWR?" - Perhaps not. I have a loop antenna tacked to the ceiling in a bedroom. It is fed with 300 Ohm twin-lead and works very well for all the HF frequencies. I would NOT use it to transmit with a tuner. I have no idea what the SWR is, that is ONLY important to a transmitter.

Most receivers can handle all sorts of mismatch it's the transmitter than needs the "protection" in order to push out full power. However, that said I will also say that one can work well enough with a tuner and receiver and tune for the most noise. Pick an unused frequency and use the tuner to increase the noise level. One you've maxed it out you'll have better reception for frequencies close to this one.

I hope that helps.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/382/what-is-the-relationship-between-swr-and-receive-performance, by K9KRB, user, Phil Frost - W8II, KE3FL. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
