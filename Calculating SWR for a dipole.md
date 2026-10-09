# Calculating SWR for a dipole

*Tags: antenna, dipole, impedance-matching, bandwidth, math · score 3*

## Question

I have a dipole wire antenna that is tuned to 14.0 MHz so that it has an SWR there of nearly 1:1. Is there a mathematical formula by which I can compute the expected SWR for other frequencies? I would, for example, like to calculate the expected SWR if I transmit a frequency of 14.3 MHz into that same antenna.

## Accepted answer (score 2, by webmarc)

here is a [great answer](Calculating%20bandwidth%20of%20antenna.md) to a similar question, "how do I calculate the bandwidth of an antenna".

Assuming the antenna is in free space, you only need to know the length and diameter of the wire used to construct the dipole. The math is hairy but I wrote a program to do the calculations. Here is the SWR (assuming a 50 ohm source) and feedpoint impedance for a dipole 10 meters long, with a diameter of 2.053mm

And Phil shared the source of a Python program that will help calculate in the above linked answer.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19984/calculating-swr-for-a-dipole, by Bill KG5RMJ, webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
