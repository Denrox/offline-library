# What is the point of high gain antenna with respect to the maximum EIRP

*Tags: antenna, legal, antenna-system, gain · score 4*

## Question

OFCOM states that the maximum EIRP within the UK for 2.4 GHz is 100mW. Simply put, what is the point in being able to buy 2.4 GHz high gain antennas which can say do 24dBi, which already puts the output power at 256mW?

Is this a case of OFCOM turning a blind eye to things, considering the USA for example has limits which far exceed the UK?

**Source sites:**

WiFi Transmit Power Calculations  
Max EIRP (1)  
Max EIRP (2)  
24 dBi antenna

## Answer (score 5, by Phil Frost - W8II)

Not everyone is subject to that EIRP limit. For example, part of the 13 centimeter amateur band overlaps the 2.4 GHz ISM band, and a licensed amateur has a very much higher power limit. Commercial licenses also exist. Regional regulations vary but it's a safe bet there are licensed services available in most jurisdictions with a higher limit.

A higher gain antenna is also more directional, and thus has better receive performance by virtue of receiving less noise from other directions. Even if power is reduced to keep the EIRP at 100 mW, a more directional antenna will have better link quality.

And yes, people install these illegally. I imagine enforcement is very difficult unless there's a specific complaint.

## Answer (score 3, by ON5MF Jurgen)

A higher gain antenna means you can use lower power for the same EIRP. Or you can use a longer cable between the transmitter and the antenna.

Moreover a higher gain antenna helps you to receive weaker signals.

## Answer (score 2, by Glenn W9IQ)

Power output limits stated in terms of EIRP can be quite helpful in the case of very low frequencies, where it is difficult to build an efficient antenna and at very high frequencies where feedline and dielectric losses become significant. In these cases, a higher transmitter power than may otherwise be allowed can be deployed to make up for these systemic losses.

A 24 dBi antenna provides a gain of >251 times that of an isotropic antenna. This means that if you put in 100 mW into this antenna, your EIRP will be >25 watts - well over the 100 mW EIRP legal level. To use this antenna legally, the power going into the antenna can be no more than ~0.4 mW. This is probably rarely followed in practice. Do take care as 25 watts at this frequency can be harmful to body tissues at close range.

Assuming the directivity of the antenna favors the application, a high gain antenna offers the following advantages:

- Increases the received signal by the same gain
- Reduces receive interference from other (low gain) directions
- Makes up for feedline loss on transmit and receive
- Focuses the transmit power in the desired direction reducing interference to other receivers
- May reduce the odds of reception of transmitted signals for nefarious purposes

The potential disadvantages are:

- Mechanically more complex
- A larger antenna profile
- May not be applicable for a wide area system if gain direction is not favorable to the required coverage area
- Potentially higher cost

If you require coverage of a larger area and you wish to use high gain antennas you could consider multiple transceivers and multiple antennas aimed in different directions.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7558/what-is-the-point-of-high-gain-antenna-with-respect-to-the-maximum-eirp, by R4D4, Phil Frost - W8II, ON5MF Jurgen, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
