# Why would you choose a Turnstile vs Crossed Yagi CP antenna?

*Tags: antenna, antenna-theory, satellites, yagi, circular-polarization · score 3*

## Question

## Question

What is the difference between circularly-polarized crossed-Yagi and turnstile antennas used for satellite contacts? From what I can tell, the crossed elements of a Yagi are electrically connected through a phasing network of $\frac{\lambda}{4}$, whereas, in a turnstile the crossed elements are directly connected without phasing network.

- Visually they each are similar to each other, so why would you choose one over the other?
- Are there any electrical or propagation related reasons?
- Other reasons?

## Crossed-Yagi

From DK7ZB:

#### Crossed-Yagi phasing network

## Turnstile

From Neoklis 5B4AZ, *"RHCP turnstile for 137MHz (WX sat band). This design is Russian and its used on the Wx sats!"*:

You can see that in this turnstile, the crossed elements are excited directly without a phasing network:

#### Turnstile NEC2 code

```
CM --- NEC2 Input File created or edited by xnec2c 3.5 ---
CM Turnstile antenna RH elliptical polarization for 137 MHz
CE --- End Comments ---
GW     1    24   0.00000E+00  5.17000E-01  0.00000E+00  0.00000E+00 -5.17000E-01  0.00000E+00  6.00000E-03
GW     2    24  -5.17000E-01  0.00000E+00  0.00000E+00  5.17000E-01  0.00000E+00  0.00000E+00  6.00000E-03
GW     3    12  -5.15000E-01  0.00000E+00  4.00000E-01  0.00000E+00  1.00000E-02  4.00000E-01  6.00000E-03
GW     4    12   0.00000E+00 -1.00000E-02  4.00000E-01  5.15000E-01 -1.00000E-02  4.00000E-01  6.00000E-03
GW     5    11   0.00000E+00 -4.65000E-01  4.00000E-01  0.00000E+00 -1.00000E-02  4.00000E-01  6.00000E-03
GW     6    11   0.00000E+00  1.00000E-02  4.00000E-01  0.00000E+00  4.65000E-01  4.00000E-01  6.00000E-03
GW     7     1   0.00000E+00  1.00000E-02  4.00000E-01  0.00000E+00 -1.00000E-02  4.00000E-01  6.00000E-03
GW     8    24  0.00000E+00  4.50000E-01  7.00000E-01  0.00000E+00 -4.50000E-01  7.00000E-01  6.00000E-03
GW     9    24  4.50000E-01  0.00000E+00  7.00000E-01 -4.50000E-01  0.00000E+00  7.00000E-01  6.00000E-03
GE     0     0   0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00
EX     0     7     1      0  1.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00
FR     0    51     0      0  1.30000E+02  6.00000E-01  1.60000E+02  0.00000E+00  0.00000E+00  0.00000E+00
NH     0     0     0      0  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00
NE     0    16     1     16 -1.50000E+00  0.00000E+00 -9.00000E-01  2.00000E-01  0.00000E+00  2.00000E-01
RP     0    19    37   1000  0.00000E+00  0.00000E+00  1.00000E+01  1.00000E+01  0.00000E+00  0.00000E+00
EN     0     0     0      0  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00

```

## Accepted answer (score 4, by tomnexus)

The picture you show is not really a turnstile antenna, it's a three element crossed yagi.

A turnstile at its simplest is a *horizontally polarised omni-directional antenna*, formed by feeding two orthogonal horizontal dipoles, 90 degrees out of phase. The "turnstile" refers to the way that the pattern "spins" around the mast as the horizontal elements are excited in turn. A turnstile with a single pair of elements radiates up and down too; when they are stacked (for FM or TV transmission etc) then they form a narrower beam to the sides.

A ground plate or resonant reflector element can be added behind a turnstile to direct its radiation pattern upwards... but when you add both a reflector and a director then it really becomes a crossed yagi antenna, with a fairly narrow beam pointing upwards (as shown).

A 90 degree feed network is usually required for any circularly polarised antenna.  
However it is possible to tweak the driven element lengths to achieve nearly 90 degree phasing, by making one element fairly capacitive, and the other fairly inductive.  
This is difficult because: - The phase is never really 90 degrees. - the power split is never equal because the real part also changes with length. - This trick only works for a very narrow bandwidth as the reactances change quickly with frequency. - In a yagi the driven element impedance is affected by the reflector and director so it may not be possible to get the impedance you want.

Apart from the feeding, the only difference between the two yagis is the gain - the longer crossed yagi will have larger gain and smaller beamwidth.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22703/why-would-you-choose-a-turnstile-vs-crossed-yagi-cp-antenna, by KJ7LNW, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
