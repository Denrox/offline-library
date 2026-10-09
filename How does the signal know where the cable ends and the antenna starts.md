# How does the signal know where the cable ends and the antenna starts?

*Tags: antenna, antenna-theory, antenna-system · score 23*

## Question

I know very little about antennas. I know, that for a certain frequency the antenna needs a certain lengths for good sending/receiving conditions. Often the antenna is at the end of a cable. Why doesn't the length of the cable count in addition to the length of the antenna?

## Answer (score 32, by Glenn W9IQ)

An excellent question! Without diving too deep into the theory, let's start with a few basic terms.

The "signal" that an antenna is receiving or transmitting is called an electromagnetic wave. This is exactly the same type of wave as light. It is just that our eyes are sensitive to a narrow range of frequencies that we call light. Electromagnetic waves that are lower in frequency behave exactly the same but we cannot see them. These lower frequencies are generally called RF (radio frequencies). Antennas are used to radiate (transmit) and receive electromagnetic RF signals.

The cable or wire that goes between the antenna and a receiver or transmitter is called a transmission line. We use this term even if the cable is simply used for receiving purposes. A transmission line is specifically designed to not radiate an electromagnetic wave but only transport it from one end of the transmission line to the other. There are several types of construction that can meet this requirement but you are probably most familiar with coaxial cable - the same type of cable that is used for "cable TV".

In the case of the coaxial cable, the outer shield keeps the electromagnetic wave contained between the outer shield and the inner conductor. And as it does so, the electromagnetic wave moves from one end of the cable to the other.

The device that generates the electromagnetic wave is called the source. This could be a transmitter or, when receiving a signal, it is the antenna. At the other end of the transmission line is the load. When transmitting, the antenna is considered the load and when receiving it is the receiver that is the load. By convention, the electromagnetic wave travels from the source end to the load end.

So now armed with these few terms, we can restate your question as: Why isn't the transmission line included as part of the antenna when accounting for the length of the antenna?

The simple answer is to realize that an antenna is specifically designed to receive or radiate electromagnetic waves. And you are correct that the dimensions of the antenna play a key role in its overall performance. But now contrast this to the transmission line that is specifically designed to *not* radiate electromagnetic waves.

We can draw a comparison here to a garden hose and a sprinkler. The garden hose is specifically designed to transport the water from one end to the other without leaking any of it along the way (although I have a few hoses that seem not to have gotten that memo). The sprinkler, on the other hand, is specifically designed to "leak" water in a very specific pattern and volume.

I hope that is the level of answer you were expecting. Feel free to use the comments to ask for any clarifications or additional depth.

## Answer (score 10, by Phil Frost - W8II)

Antennas are often resonant. Their physical dimensions are adjusted so standing waves develop at a particular frequency, like a bell rings at a particular tone.

Feedlines are not usually resonant. Usually an engineer ensures the end of the feedline is terminated (by the antenna or the radio) with an impedance that matches the characteristic impedance of the feedline. This ensures that as a wavefront reaches the end of the feedline it's fully absorbed and none of it is reflected back. Since there are ideally no reflections of energy in this configuration, resonance can't happen.

There are of course counterexamples. Non-resonant antennas exist in some applications, especially when the antenna must be physically small, or in receive-only applications where efficiency isn't as important. And transmission lines can be used to introduce controlled phase shifts into the signal, for example to make phased arrays or matching networks, and for this they must be cut to specific lengths that depend on frequency.

## Answer (score 4, by Cecil - W5DXP)

RF signals have no consciousness so they really don't know anything. All they can do is follow the laws of physics. When a signal is traveling in a transmission line conductor there is another signal of equal amplitude and opposite direction (phase) traveling in the other conductor close by. The RF fields from those two signals (almost) cancel so no (or very little) energy is lost to radiation from a transmission line. But suddenly those two signals split up and go off at right angles to each other at the dipole feedpoint so there is no other field close by to cancel the antenna's fields. Both signals are now free to radiate their fields as RF signals propagating through the air - and they do just that. When in the transmission line, the RF signals in each wire are traveling in opposite directions, i.e. are differential. But when one wire takes a 90 degree left hand turn and the other takes a 90 degree right hand turn, it results in the two currents flowing in the same direction, i.e. changes them to radiating antenna currents.

So when does the feedline have an effect on the system and when does it not have an effect? If the feedline SWR is 1:1, it is called "flat" and the feedpoint impedance of the antenna equals the Z0 characteristic impedance of the feedline. This is called the "matched line" case and if there are no common mode signals present, the feedline has very little effect on the conditions surrounding the antenna.

However, if the SWR on the feedline is not 1:1, the feedline becomes a "tuned feeder" and is an active part of the antenna system the length of which determines such things as resonant frequency and the impedance seen by the source transmitter. Some of this effect is explained on my web page at:

http://www.w5dxp.com/notuner/notuner.HTM

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12198/how-does-the-signal-know-where-the-cable-ends-and-the-antenna-starts, by flux, Glenn W9IQ, Phil Frost - W8II, Cecil - W5DXP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
