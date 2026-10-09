# Pi Matching circut for tube PA - what values?

*Tags: impedance, transmitter, amplifier, antenna-tuner, vacuum-tubes · score 4*

## Question

I am working on my 80m and 40m CW transmitter and ran into a problem:

I need to match the high impedance of PL504 to 50ohm coax, a Pi match seems to be the best, but I don't know how to calculate the inductor - the calculators online give capacitor values of several nF, too big for tuning caps and sometimes they just say NaN.

Operation class is C and I'd like to get 20W of power at least.

- What is the best value for plate RF choke?
- Can it be made with a SMPS power core rated for 200kHz?
- Are there any general errors?

## Accepted answer (score 3, by Brian K1LI)

Inspection of figures 17.17 through 17.19 in the ARRL *Handbook* suggest that the components in your Pi network might need to be adjusted:

Jim Tonne, W4ENE, wrote a utility called PIEL to calculate output tank values. A Pi-L network - a Pi network with an L-network extension - is frequently used to match a wider range of impedances than a Pi network alone can handle.

To use the program, you must know the load represented by the plate of the tube. PIEL includes a "Plate load help" button to perform this calculation using your intended voltage swing, RMS output power and class of operation.

Assuming you want the plate to swing over half the 100V supply to produce 20W in class C, PIEL calculates the plate impedance to be 62.5$\Omega$. Entering this value in PIEL's main screen with an intermediate impedance of 50$\Omega$ to drop the L-section yields this Pi network:

Increasing the plate voltage swing and reducing the network Q reduces the capacitor values. You can experiment with these values until you find a network you can build with available components. For example, increasing the swing to 90V and reducing the Q to 3 produces this network:

But, you need to keep in mind that the network may no longer provide the harmonic rejection required to comply with FCC rules.

## Answer (score 3, by Brian K1LI)

DISCLAIMER: I offer these results only as a *possible* solution. Completing this design may depend on many other factors, thermal and electrical, steady state and transient, component- and layout-dependent parasitics. This is the subject of, at least, sizeable chapters if not entire text books, which I will not reproduce here. Your mileage may vary.

I entered the following values into the PiEl program:

Plate load help:

```
- Plate voltage swing: 190 volts
- RF power: 12 watts, RMS
- Class C (k=2)

```

- Plate load result: 1.504k ohms

Main page

```
- Frequency: 3.5MHz
- Plate load: 1.504k
- Intermediate impedance: 1.504k
- Load impedance: 50 ohms
- Pi-section Q: 10

```

Resulting output network:

Resulting harmonic output:

You can do this yourself to settle on a set of parameters that best meets your particular constraints and requirements.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14593/pi-matching-circut-for-tube-pa-what-values, by thegamebusterpl, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
