# What would be the typical received power of an "S9" signal?

*Tags: receiver, rf-power · score 5*

## Question

Obviously, I would expect the amount of power at a receiver would vary greatly based on distance from, and the power/efficiency of, the transmitter. But I don't really have a good sense for what "ballpark" the power would even be in for a "good quality" signal. Is it — milliwatts? picowatts?

## Answer (score 3, by natevw - AF7TB)

The answer for a literal "S9" value is actually pretty simple! According to the table in this helpful article on S-meters, S9 corresponds to **50 picowatts** of input power.

This is actually *by definition*: a standard S9 value was defined as 50 μV in the HF range (but 5 μV for frequencies above 30 MHz) — and at 50 ohms impedance, such voltage is developed by that approximately 50 pW of power. To avoid a dependency on impedance, the standard has apparently been updated directly in terms of power. The Wikipedia S Meter article cites:

IARU Region 1 Technical Recommendation R.1 defines S9 for the HF bands to be a receiver input power of -73 dBm. This is a level of 50 microvolts at the receiver's antenna input assuming the input impedance of the receiver is 50 ohms.

All other *standard* S-values are relative to this S9 definition which I ended up finding in the [IARU Region 1 HF Manager Handbook, chapter 8.2.1 rather than Wikipedia's citation]. Granted, the signal meter on any given receiver may or may not actually give readings according to this full standard, but contrary to rumors, at least there *is* a standard.

Since I had started to work out my own estimate via Free-space path loss equations before I thought to simply search for the S-value definitions, I thought it'd be interesting to see what sort of **distance** S9 would then correspond to given a 100W transmission between two dipoles.

Re-arranging the Friis transmission equation, and neglecting all other factors, this works out to:

$$ R = \lambda / 4 \pi \cdot 10^{\large (G_r + G_t + P_t - P_r)/20} $$

For the following values:

```
Pr = -73 dBm (S9 power at receiver relative to millwatts)
Pt = 50 dBm (100W output power from transmitter)
Gt = Gr = 2.15 dBi (half-wave dipole gain over isotropic)
λ = 40 meters (is a fun band)

```

Works out to:

$$ 40/(4\cdot\pi) \cdot 10^{\large (2.15+2.15+50+73) / 20} = 7,376,496.273 $$

So given an otherwise lossless system, but tempered by fairly low-gain antennas, you would, **on the 40m band, receive an S9 signal from a 100W transmitter when it was 7375 kilometers away**. A longer distance than I imagined! But I guess that's reasonable given complete transmitter system efficiency and no atmospheric attenuation — if calling mere picowatts of energy a "strong signal" is "reasonable" in the first place!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6950/what-would-be-the-typical-received-power-of-an-s9-signal, by natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
