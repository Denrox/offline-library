# How to increase antenna aperture?

*Tags: antenna, antenna-theory · score 6*

## Question

I know that in the short wavelength region, where parabolic antennas are used, the aperture can be increased simply by making the dish larger, as is the case with the radio telescopes. But how to do this in the RF? If I make a half wave dipole larger, its resonant frequency decreases. The other way I can imagine is to make an array of antennas working in phase, but in this case it gets more directional with larger number of elements. Is there a way to increase antenna aperture without making it directional?

## Accepted answer (score 4, by Phil Frost - W8II)

Is there a way to increase antenna aperture without making it directional?

Not really. You can make the antenna more efficient by reducing losses, but since antennas are usually designed for minimum loss already, there is probably no significant gain to be made in this direction unless you are starting with an electrically small or poorly designed antenna.

Radio telescopes do operate "in the RF", so what applies to them also applies to any other antenna. Increasing the dish size does increase the effective aperture. It also increases directionality.

If you didn't know it already, effective antenna aperture ($A_\text{eff}$) and gain ($G$) are essentially two ways of specifying the same thing. They are related by the equation:

$$ G = \frac {4 \pi A_\text{eff} } { \lambda^2 } $$

Assuming our antennas are already as efficient as we can make them, then we can't increase the aperture, or equivalently, gain, without also increasing directionality.

Here's why. Consider you have a 1W transmitter. If you send that power equally in all directions, then you have an isotropic radiator which has by definition a gain of 1.

Let's just say you found a way to increase the gain of this isotropic radiator without also increasing its directionality. That is, it has a gain greater than unity, but still sends energy equally in all directions. Were you to construct such a device, I would surround it with a Dyson sphere, which would capture all of the energy it transmitted. If your device had a gain of 2, then the 1W transmitter would be emitting 2W of power for my Dyson sphere to capture. I could then use the output of that Dyson sphere to power another instance of your device, giving me 4W. I could go on cascading instances of this device and obtain limitless power. It's a perpetual motion machine, so probably is impossible.

By reciprocity, it can be seen that the same thing is true when receiving. I can make an antenna array which has some greater gain in some direction, but it must necessarily have less gain in some other direction for some given phasing configuration.

If you provide a way to vary the phasing of the antenna, such as combining the signals from each element independently and dynamically in software, rather than in hardware, then you can pick the best phasing for a particular signal which might come from any direction. However, this requires that "best" is defined and measured dynamically. Modern radio communication systems do this, for example MIMO in 802.11n. However, it adds complexity to the system, and I guess might be considered as "cheating" as far as your question is concerned.

Alternately, you can provide an additional source of energy as an amplifier. This adds gain to all directions, so you could say it increases antenna aperture. Because you must supply the amplifier with additional energy, it is not a perpetual motion machine. While we use amplifiers all the time, we don't usually consider this as increasing gain or aperture because that way of thinking isn't very useful. If the antenna directionality is not increased, than the amplifier increases noise as well as signal. That is, the signal to noise ratio remains the same.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1836/how-to-increase-antenna-aperture, by Tr00rle, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
