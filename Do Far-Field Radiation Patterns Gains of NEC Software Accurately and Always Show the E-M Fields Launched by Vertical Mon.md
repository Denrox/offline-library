# Do Far-Field Radiation Patterns/Gains of NEC Software Accurately and Always Show the E-M Fields "Launched" by Vertical Monopoles?

*Tags: antenna, vertical-antenna, radiation-pattern, antenna-modeling · score 3*

## Question

Judging from posts on the Internet, this belief commonly is considered to be valid. But what is the correct answer?

## Answer (score 2, by Richard Fry)

The NEC4.2 analysis below compares the intrinsic fields/gains of the same monopole for the definitions and conditions shown in that graphic.

Note that the monopole having a 10 Ω path connecting it to the ground plane does not display zero gain in the horizontal plane, then gradually rising to more positive values for greater elevation angles above the horizontal — as is shown by a NEC "far-field" analysis. The analysis below shows that the greatest field/gain reduction actually "launched" by that monopole using the 10 Ω path to r-f ground is about 1 dB (in the horizontal plane), relative to using a perfect ground.

Propagation losses beyond a few wavelengths away from these monopoles affect their intrinsic radiation patterns. However when an imperfect ground plane is present, the losses existing beyond that radius distance produce more attenuation for low-angle, radiated fields.

It is this phenomenon that produces the zero and relatively low-amplitude, low elevation angle fields/gains shown by a far-field analysis using NEC (MoM software), from vertical monopoles using imperfect ground planes.

However that doesn't mean that those fields/gains first launched by a vertical monopole using imperfect ground planes did not have much higher values closer to the antenna site.

In response to the comments of tomnexus, this edit to my answer adds a new graphic (below), which better illustrates these issues and observations.

Amateur radio operators tend to use the NEC-calculated far-field analysis almost exclusively. However the far field as defined in antenna engineering textbooks begins at a distance of about 2L²/λ meters [L = Radiator Length(Height), in meters; λ = wavelength, in meters].

Note that at the distance of 1 kilometer specified for the e-fields of these NEC calculations, both the far-field *and* the surface wave values lie in far-field of that radiator.

Using only the NEC far-field pattern to analyze the performance of a vertical monopole antenna system driven against a lossy ground plane can lead to a belief that it has zero radiation in the horizontal plane, and not much more than zero at very low elevation angles.

However that is not always the case, when NEC analyzes the surface wave at ranges within distances of 30 miles or even more from the antenna site (depending on radiated power, frequency, ground plane conductivity etc).

**Added November 29, 2019**

Below is an expansion of my answer to address the concept that the radiation pattern of a vertical monopole requires a circular ground plane having a radius of some 10 to 100 wavelengths in order to reach its final form.

The graphic below shows the radiated fields of a vertical monopole for the conditions shown in the graphic, calculated using NEC4.2. Elevation AGL is shown on the left Y axis; field intensity 0.1 km from the radiator vs. elevation angle are shown by the X axis and the right Y axis.

Observations, for these conditions:

» The fields for Earth conductivities ranging from sea water (5,000 mS/m) to very poor (1 mS/m) all have nearly the same relative values (E/Emax)

» All of these radiated fields are maximum in the horizontal plane

» These radiation patterns did not require "10 to 100 wavelengths" to form; the 0.1 km horizontal distance used in this analysis is only 0.617 wavelengths away from the radiator

» Low values of Earth conductivity do not produce zero v-pol radiation in the horizontal plane, as shown by a NEC far-field (only) analysis

For reference, the field at 0.1 km radiated by this transmit/antenna system using a perfect ground plane is 0.992 V/m, an improvement of only 0.19 dB when compared to sea water.

]3

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15611/do-far-field-radiation-patterns-gains-of-nec-software-accurately-and-always-sh, by Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
