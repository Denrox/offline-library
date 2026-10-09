# Are the voltage ratings on Vacuum Variable Capacitors RMS or Peak

*Tags: capacitance, magnetic-loop · score 3*

## Question

I'm building a magnetic loop antenna and was wondering if the voltage ratings on the vaccuum variable capacitors I have are:

- RMS
- Peak to Peak
- Peak
- other?

I have been looking at this wonderful magnetic loop calculator to help choose a capacitor and it gives the required cap voltage in RMS.

## Accepted answer (score 1, by Marcus Müller)

You raise an interesting point; intuitively, what I'd have thought is that the peak voltage matters – because discharge through the dielectric doesn't happen for any reason but an electrical field strength (at least for vacuum as dielectric, which can have no electric polarization of any kind, being not a material) above the Schwinger limit which you will never reach even remotely.

Now, necessarily, your cap doesn't hang in *perfect* vaccuum, but let's assume it happens in a quality of vacuum (gas pressure) that guarantees a breakdown value at least equivalent to that of air (see Paschen's Law), but with negligible polarization losses; then you'd still have around 2.5 MV/m breakdown voltage (probably more).

Notice how I precluded polarization effects – this is my guess why these caps use vacuum instead of just being filled with some inert gas: Without any material to be subject to changing electrical field strength, you can't have molecules/atoms align their electric momentum with the field, which can, when quickly enough changing that field, reduce the breakdown voltage of a capacitor, and lead to energy losses and thus, heating of the dielectric.

For considerations of how much energy will get lost in a material, the RMS voltage is a good measure – same goes for the breakdown voltage reduction.

However, as a vacuum cap sees neither of these effects under "earthly" conditions, RMS is not what you need to know – you really just want to know how much voltage you might *ever* see, because, as soon as that voltage crosses breakdown voltage, there will be an arc within your cap – and that might become a self-sustaining arc, considering that its heat will possibly vaporize and splutter some of the conductor plates into the vacuum, making it a box of conductive plasma.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6400/are-the-voltage-ratings-on-vacuum-variable-capacitors-rms-or-peak, by Arthur, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
