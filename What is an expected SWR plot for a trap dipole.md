# What is an expected SWR plot for a trap dipole?

*Tags: antenna, dipole, inverted-vee, trap · score 3*

## Question

I've build a trap dipole for 20/40m bands. Traps are made of a coil wound on an insulator of RG213 coax and 3 kV NP0 capacitors. The impedance measured with EU1KY antenna analyzer is following:

This is a single trap, before and after putting a heatshrink. The final version of this one is for 14.080 MHz. The second one turned out a bit different, the resonant frequency is 14.150 MHz.

Here is an SWR plot of a final antenna:

The mast is non-conductive, 10 meter high. The balun is 7 turns of RG58 on FT140-43 core. The active impedance is > 1000 Ohm from 80 to 15 meters. The antenna is used in **inverted-V** configuration.

The antenna was tested using 100W CW. It works OK. However I was surprised to get such a narrow band and SWR >= 1.5 on 20 meters. What brings a question - is it an expected result for trap dipoles? I always thought that it supposed to be more narrowband on lowest band, because traps work as loading coils there. Can it indicate that something is wrong with the antenna?

## Accepted answer (score 0, by Aleksander Alekseev - R2AUK)

OK, I've checked 5 or 6 types of traps made of different materials, tuned to the same or slightly different frequencies, tuned right on the band, below the band and above the band. Most of them were not better than the first pair. Tuning above the band doesn't work. Traps made of RG58 coax work best. You get SWR 1:1 on both bands, 320 kHz bandwidth on 20m and 225 kHz bandwidth on 40m with SWR <= 2. According to WSPR report the antenna is no less effective than my previous fan dipole was. The article An Attic Coaxial-Cable Trap Dipole for 10, 15, 20, 30, 40, and 80 Meters by John DeGood, NU3E explains how to make such traps in great detail. Turned out these traps are tuned to the slightly different frequencies below the band.

Answering my own question: **NO**, this is not an expected result. Although such antenna kind of works, you can make a much better one.

## Answer (score 3, by Phil Frost - W8II)

I don't know how much of an impact it might make, but you might try moving the trap resonance to be outside the 20m band.

Trap losses are highest at the trap's resonant frequency because at this frequency the current circulating between the inductance and capacitance is at a maximum. Thus, ohmic losses within the trap are maximized.

At resonance is also where the rate of change of impedance with respect to frequency is highest. Designing the trap to be resonant within the 20m band means the trap impedance will vary rapidly over the band, which could explain the narrow SWR bandwidth.

To work as a trap you don't need the impedance to be infinite: only high enough to sufficiently isolate the following length of the antenna. Moving the resonant frequency of the trap may lower its impedance, but you can compensate for that by adjusting the length of the antenna. On the up side, losses may be lower and SWR bandwidth may be improved.

Further reading:

- https://www.falstad.com/circuit/e-res-par.html
- https://www.w8ji.com/traps.htm

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16937/what-is-an-expected-swr-plot-for-a-trap-dipole, by Aleksander Alekseev - R2AUK, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
