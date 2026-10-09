# How would this RF field strength meter be calibrated?

*Tags: equipment-design, calibration, equipment-operation · score 4*

## Question

I'm interested in an RF field strength meter that doesn't have to be lab quality, but still gives enough information about the RF field to know if an area exposed to RF is above the safety limits suggested by the ARRL and others.

One of the simpler designs available has no information about accuracy or calibration. Can the following design be calibrated, or is the circuit only good for relative measurements? The only circuit description I have follows the schematic:

A radio field signal strength indicator is very usefull for determine radiation patterns of transmitters antennas. An ancillary antenna must be put close to main transmitter antenna. The received signal is applied to L1,L2 and C2, this allows the field indicator circuit to adjust to the same frequency as the transmitter. With the coils values from the radio signal indicator wiring schematic, the frequency band is 6 to 60MHz. A pair of headphones can be connected to hear the transmission. The total impendance of the headphones has to be at least 2.2Kohm.

## Answer (score 2, by Phil Frost - W8II)

In theory, if you can expose this device to a known field, you should be able to calculate some constants which allow you to convert the measured current (in μA) to a power density (in power per area, such as mW per cm). Power is proportional to the square of current. T1 introduces some unknown gain, and the filters have some unknown loss. The antenna has some aperture. The power density is the power received by the antenna, divided by the aperture of the antenna. All the variables you don't know (the circuit's impedance, the antenna aperture, T1's gain, filter losses, etc) can all be lumped into a general quadratic equation of the form:

$$ \text{power density} = aI^2 + bI $$

Where $I$ is the current displayed on the meter, and $a$ and $b$ are some constants you must determine through calibration. You could determine them by exposing the device to a handful of known fields, recording the measured current, then performing a quadratic regression with a spreadsheet program to find the values for $a$ and $b$ which best fit the measurements.

The trouble is coming up with a *known field*. You could transmit into some antenna that is easily modeled (say, a dipole) a known power, then calculate (by the antenna model) what the power density should be at some distance.

For example, modeling with EZNEC suggests that a half-wave dipole a half-wavelength above ground has between 8.6 dBi of gain for "very good ground" to 6.8 dBi for "very poor ground", in the direction of maximum gain. This is broadside to the dipole, at about 20 degrees elevation. We can then calculate the power density at some distance with the inverse square law. For our example:

- we are **100m** away,
- we are putting a **20W** carrier into the antenna, and,
- we estimate the dipole's gain is around **7 dBi**.

It's important to note that we need to be many wavelengths away, for two reasons:

- We must be in the far field for the predictions of our antenna modeling to be accurate.
- The inverse square law only holds for things that are far enough away that they appear to be an infinitely small, single point.

A measurement distance of 100m might be sufficient for a 10m dipole, but for 160m, I'd want to be much farther away. As a rule of thumb, I'd stick to 10 wavelengths or more.

Now, the math. First convert the gain into a multiplicative value:

$$ 7\mathrm{dB} = 10^{7/10} \approx 5 $$

The EIRP is then:

$$ 20\mathrm W \cdot 5 = 100\mathrm W $$

At 100m, that 100W will be spread out over an area equal to the surface area of a sphere with radius 100m (this is the inverse square law). That sphere's area is:

$$ 4\pi (100\mathrm m)^2 \approx 125663 \mathrm m^2$$

The power density is then the EIRP divided by this area:

$$ \frac{100 \mathrm W}{125663 \mathrm m^2} = \frac{0.000796 \mathrm W}{\mathrm m^2} $$

Converting to the more usual unit of mW/cm:

$$ \require{cancel} \frac{0.000796 \cancel{\mathrm W}}{\cancel{\mathrm m^2}} \frac{1000 \mathrm{mW}}{\cancel{\mathrm W}} \frac{1 \cancel{\mathrm{m}}}{100 \mathrm{cm}} \frac{1 \cancel{\mathrm{m}}}{100 \mathrm{cm}} = \frac{0.0796 \mathrm{mW}}{\mathrm{cm^2}} $$

Here's the trouble: this method is only as good as your model, and the model isn't very good. It might get you within an order of magnitude at best.

Further, if this calibration is dependent on a model for its accuracy, you might as well just model the antenna in question, the one which you want to measure for safety. Then you can guess what its fields are directly, and skip the building of the probe, and the calibration, and you won't be any less accurate.

Even so, a probe "calibrated" in this manner can still be useful. Its readings will always be off by some multiplicative constant, so it can be used for comparing one antenna to another, or measuring the radiation pattern of an antenna, or measuring the effect of other station changes (upgrade feedline, install a balun, new transmitter, etc).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1527/how-would-this-rf-field-strength-meter-be-calibrated, by Adam Davis, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
