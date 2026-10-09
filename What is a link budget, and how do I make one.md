# What is a link budget, and how do I make one?

*Tags: jargon, range, path-loss · score 28*

## Question

Like the question title says, what is a radio link budget? For what is it useful, and how do I make one?

## Accepted answer (score 36, by user)

A link budget is a summary of a communications link that tries to take into account all factors which have an impact on the received signal strength. It is often used to determine the minimum amount of output power required at the transmitter for a given signal strength at the receiver, and takes into consideration power output, antenna gains, propagation losses, acceptable signal fading, and other factors (for example, for long cable runs, cable attenuation may be a factor, and at microwave frequencies, losses due to absorption in atmospheric gases become a significant factor for Earth-bound links).

A few elementary values are required to make up a link budget. For unobstructed line of sight communications, which is the primary propagation mode on VHF and up, propagation losses can be estimated using the formula

$$L_{p} = -22 - 20\log{\frac{r}{λ}}$$

Where *r* is the distance covered and *λ* is the wavelength of the operating frequency. When the two use the same units (for example, meters), *Lp* comes out in dB and expresses the propagation attenuation (loss) between two isotropic antennas. For example, the propagation loss for a distance of 100 meters at 450 MHz is approximately 65.5 dB. Note that the determining factor is actually the distance in terms of wavelengths between the two antennas, so the loss goes up by 6 dB for every doubling of either the physical distance or the frequency (halving of the wavelength).

No antenna is perfectly isotropic, and the common dipole has a gain of approximately 2.15 dBi (dB over isotropic) broadside to the antenna. Directional antennas generally have their gain specified as either dBi or dBd (dB over dipole, which is dBi - 2.15 dB, so 3 dBd = 5.15 dBi).

To ease calculations, convert the power output of the transmitter to dBm. Using dB throughout turns many a multiplication and division into addition and subtraction, greatly simplifying calculations. For example, a 100 W transmitter puts out +50 dBm, and a 5 W transmitter puts out +37 dBm.

**To make the link budget, at a minimum add the transmitter output power, transmitter antenna gain in the desired direction, propagation loss and receiver antenna gain in the desired direction.** By making the calculations in dB relative to some known reference (generally dBm or dBW) this comes down to addition and subtraction.

**As a very simple example,** for a 100 W transmitter with dipoles at both ends broadside to each other (+2.15 dBi × 2), over an unobstructed 20 km path using a frequency of 150 MHz (2.00 meters wavelength), we get:

```
+50    dBm   power output
+  2.15 dBi   transmitter antenna gain
 -102    dB    propagation loss, 20 km at 150 MHz
+  2.15 dBi   receiver antenna gain
===========
 -47.7  dBm   signal strength at receiver

```

If the minimum usable signal at the receiver for the modulation and bandwidth in use, taking into account natural and receiver noise, is -90 dBm, this gives us a margin of about 42 dB, which is huge. This of course means that in theory, we can reduce our output power by a corresponding amount, maintaining communications with only +8 dBm output, as seen below:

```
+8    dBm   power output
+  2.15 dBi   transmitter antenna gain
 -102    dB    propagation loss, 20 km at 150 MHz
+  2.15 dBi   receiver antenna gain
===========
 -89.7  dBm   signal strength at receiver

```

Admittedly, the above link budget gives us for all intents and purposes no margin: to maintain communications over this path using this equipment and mode of transmission, everything must work out absolutely perfectly. To have a 10 dB margin for issues such as fading, we'd need to use +18 dBm (slightly less than 100 mW = +20 dBm) power output, which is trivially achievable with practically *any* handheld radio.

A link budget for a HF link, or an obstructed VHF link, is much more complex because the propagation losses are harder to calculate than for a pure line-of-sight link, but the general principle remains exactly the same. A complete link budget for a line-of-sight link will at least include the following factors:

- ＋ Transmitter output power
- － Attenuation in the transmitter's antenna cabling, including any impedance matching network
- ＋ Transmitter antenna gain in the direction of the receiver
- － Propagation loss in free space
- － Attenuation due to absorption in atmospheric gases
- － Margin for attenuation due to rain
- － Margin for attenuation in tree foilage
- － Margin for attenuation due to reflection against walls etc.
- － Margin for signal fading
- ＋ Receiver antenna gain in the direction of the transmitter
- － Attenuation in the receiver's antenna cabling, including any impedance matching network
- ＝ Signal strength at the receiver input terminals, to be compared with the minimum necessary signal strength

It is important to note that several of these factors (propagation loss, atmospheric absorption, foilage losses, and so on) are heavily dependent on the operating frequency. This means that a link budget for one frequency is unlikely to be applicable at another frequency, even if nothing else changes.

## Answer (score 15, by Phil Karn)

That's a pretty good answer but I can add some more details.

The exact formula for path loss is $$ 20 \times \log_{10}\left( 4 \times \pi \times \frac{d}{\lambda{}} \right) $$ $ 20 \times \log_{10}\left(4\times\pi{}\right) \approx 21.98$, and that's where the '22' comes from.

If your receiver specs give a minimum signal strength, then the analysis above is pretty much all you need. But in a more general link budget you have to compute the required receive power yourself from the data rate, the type of modulation and coding, and the receiver system noise temperature.

The most power-efficient modulation/coding method in use is rate 1/6 turbo coding over BPSK (binary phase shift keying). This is a very popular deep space signal; it's being used by New Horizons at Pluto, for example. This particular signal requires a minimum $E_b/N_0$ of about 0 dB.

What is $E_b/N_0$? It's the received energy per bit divided by the received noise power spectral density in watts/Hz. This also has units of energy, so the ratio is dimensionless. It's usually expressed in decibels. The famous Shannon Limit says it's impossible to make a system operate error-free at an $E_b/N_0$ below -1.6 dB even if you can use infinite bandwidth. So you can see that we're pretty close to the theoretical limit.

Then you add the data rate, also expressed in decibels (with respect to 1 bps). For example, 1000 b/s would be 30 dB(bps), so your New Horizons signal would require a $P/N_0$ of at least 0 + 30 = +30 dB, where P is received power.

That just leaves us with $N_0$. In space communications, noise is usually expressed as a temperature T since everything above absolute zero generates thermal noise. The big 70m dish at the NASA Deep Space Network sites has a noise temperature of 17.5 kelvins (I looked it up). To get N0, you multiply T by Boltzmann's constant, 1.38e-23 J/K or -228.6 dBW/Hz-K. So 17.5K is an $N_0$ of -216.2 dBW/Hz (or dBJ, same units).

Now you have what you need to compute P, the required receive power. It is simply -216.2 dBW/Hz + 30 dB-Hz = -186.2 dBW or -156.2 dBm. That's not much, but it's still hard to generate all the way from Pluto!

## Answer (score 2, by Edwin van Mierlo)

Let me take the later question out of the title.

how do I make one?

By using a tool, such as

- Radio Mobile Online
- Help is here, you don't need a free account to read it

This is a free tool, and will work for Amateur Radio frequencies.

Once you get started, in order to display a "Link", you do the following

- Use "New Site" from the main menu to setup both TX location and RX location
- Use "New Link" from the main menu to setup a new link.

This will get you a nice graphical representation of your link, and accompaning data which was used for its calculation.

YMMV.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/352/what-is-a-link-budget-and-how-do-i-make-one, by user, Phil Karn, Edwin van Mierlo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
