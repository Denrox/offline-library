# How can I safely transmit without an antenna tuner or SWR meter?

*Tags: antenna, impedance, antenna-tuner · score 16*

## Question

Just what the title says.

An Antenna Tuner, henceforth AT, is almost a de facto piece of equipment in a shack; working the bands without one is tantamount to leaping off the diving board into a swimming pool with tarantula nests in it ... or worse.

The reason for the AT is primarily to match the antenna to the transmitter for the Standing Wave Ratio. The greater the SWR, the more the risk to the transmitter. But before one uses an AT, one either designs the antenna (balanced/unbalanced, array-type, length, impedance ... and constructs it), or purchases the antenna.

**Keeping it simple**

- Say, A simple mono-band centre-fed dipole is constructed after calculating the length for that band
- Say further, neither an AT nor an SWR meter is available

**Given the above assumptions, what I would like to know**

- How can I transmit without an antenna tuner?
- Are there any rule-of-thumb tests/calculations I may do to determine whether an antenna is a decent fit for a given band?

*As a corollary*

- What if the antenna is **not** a simple centre-fed mono-band antenna?
- How did they tune antennas back when the hobby was still new? I guess [Does a tube based HF transmitter need an antenna tuner?](Does%20a%20tube%20based%20HF%20transmitter%20need%20an%20antenna%20tuner.md) may be relevant to this part of the question

## Accepted answer (score 8, by Adam Davis)

The SWR meter helps you match the impedance of the radio to the antenna. If the impedance is mismatched, you lose power. If the impedance mismatch is large, you risk damaging your radio, particularly on the lower frequencies.

Tube based transmitters and amplifiers have more leeway for mismatch than semiconductor based amplifiers.

Lower power transmitters also have more leeway for mismatch before damage occurs.

The *ideal is to borrow an SWR meter and tune your antenna for the intended frequency, or send the antenna to someone who can do that for you.*

**If you don't have any of these tools and can't get help from others easily, you can get as close to the right frequency by building the antenna according to the design, then start transmitting on low power and make contacts. Find someone willing to work with you, and ask for signal quality reports. Then make a small adjustment to the antenna and ask for another report.**

It's a long process, but they will receive more signal the better your radio is matched to your antenna, so it's an easy check.

Do this at low power though, so you reduce the risk of damaging your transmitter.

## Answer (score 11, by Phil Frost - W8II)

How can I transmit without an antenna tuner?

Simple. You use an antenna that's already tuned. There are *plenty* of radios that operate without any tuner. For example, basically every VHF radio. One reason for this is that most VHF antennas are purchased rather than manufactured by the amateur, and the antenna manufacturer has already tested and tuned the antenna design.

It's also relevant to mention that an antenna tuner doesn't actually make the antenna tuned. With a perfectly matched antenna (SWR 1:1), all the power sent down the feedline by the transmitter will be accepted by the antenna and radiated away. When the antenna isn't perfectly matched, some of the power is accepted by the antenna, and some is reflected back at the transmitter. When it reaches the transmitter, the transmitter's RF amplifier sees an impedance other than the 50 ohms for which it designed, which can mean currents or voltages high enough to cause damage. Some radios sense this condition and reduce output power to prevent damage.

By inserting a tuner between the transmitter and the feedline, the power reflected back from the feedpoint is then reflected again back at the antenna. The transmitter now sees no reflected power: it sees a well-matched load. However, the power is *still* being reflected back-and-forth between the feedpoint and the tuner, encountering [losses in the feedline](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md) each time. So, the tuner doesn't make the antenna work any better: it just takes some load off your transmitter.

## Answer (score 4, by Paul)

**Reduce Power**

One of the bad effects of SWR is heating of the power amplifier inside the radio. This heating occurs because of reflected power. The higher the SWR, the less power is transmitted out the antenna and more of the power is reflected back to the radio to become heat.

You can reduce reflected power by reducing output power. For instance, operate a 100W radio into an unknown antenna with the power set to only 5W.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/615/how-can-i-safely-transmit-without-an-antenna-tuner-or-swr-meter, by VU2NHW, Adam Davis, Phil Frost - W8II, Paul. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
