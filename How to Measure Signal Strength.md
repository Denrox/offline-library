# How to Measure Signal Strength

*Tags: antenna, rssi · score 3*

## Question

I am building several types of radio antennas, and I would like to test which is the most effective. I am wondering: What is the best way to measure the strength of the received signal?

It is at ~151 MHz and 2 watt transmission power, and I will be testing over a distance of at least a couple of hundred feet. The results don't have to be calibrated, only correct relative to one another. Any ideas?

Thanks in advance

## Accepted answer (score 2, by Marcus Müller)

For antennas, it's often interesting to know at which frequencies they work best and how far that is from the frequency you designed them for.

So, if you have a broadband or adjustable tone transmitter, you can just plug your antenna into an RTL-SDR dongle (cheap!!) and observe the received spectrum.

That'll not only give you relative reception strength at a given design frequency, but also an understanding for which bandwidths the antenna works well.

Note that passive antennas are reciprocal - i.e. what works good as receiver works just as well as a transmitter; this means you can swap the roles of transmitter and receiver, if that makes the measurement system easier.

## Answer (score 3, by Cecil - W5DXP)

You could use a receiver with an S-meter or if you are not too close to commercial RF signals you could use a field strength meter.

## Answer (score 2, by Richard Fry)

Considerations when comparing the field intensities from different transmit antennas over a given terrestrial path, and assuming use of the same receive+antenna system and its siting/adjustment for all measurements:

- Path distance from transmit antenna to receive antenna
- Height above the reflecting plane (Earth) of the radiation center of each transmit antenna
- Free-space radiation pattern of each transmit antenna toward the receive antenna, in the vertical plane

The graphic below shows the variations in received field vs. elevation above a level ground plane, for the configuration and conditions stated in the graphic.

The vertical axis (Z) = Height above Earth of the calculated field.

The horizontal axis (E) = Field intensity in mV/m.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12896/how-to-measure-signal-strength, by Danny, Marcus Müller, Cecil - W5DXP, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
