# How much attenuation (dB) from a balun is expected?

*Tags: antenna, balun, choke-balun · score 6*

## Question

I'm building a dipole antenna for 433 MHz, first one ever. I will have to use a ferrite bead to balance the feed. How many decibels of attenuation should I expect from the ferrite bead?

## Answer (score 6, by tomnexus)

If you do it right, the bead(s) shouldn't get hot at all, and shouldn't add much loss.

The impedance of the bead(s) should be about 10 x the impedance of the dipole. The current on the feedline with no balun might be about half the antenna current. With the beads on it it'll be less than 1/10 of the curent, or 1/100 of the power. Small beads (3.5 mm inside, 6 mm outside, 12 mm long) can dissipate about 5 W, but in this case they'd dissipate 50 mW if you transmit 50 W, so they'll stay cool.

Remember to run the feed line perpendicular to the antenna for some distance.

## Answer (score 2, by Jack0220)

Different beats have different attenuation at different frequencies. My gut tells me you want at least 6 dB, preferably more. Guys seem to wind their own inductors as RF chokes but not sure how much attenuation at the desired frequencies.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20082/how-much-attenuation-db-from-a-balun-is-expected, by AllYourBaseAreBelongToUs, tomnexus, Jack0220. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
