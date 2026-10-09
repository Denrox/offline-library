# How can the impedance of a half wave dipole at its resonant frequency be purely resistive when the voltage and current are seemingly not in phase?

*Tags: antenna-theory, dipole, impedance · score 4*

## Question

A half wave center-fed dipole has a resonant frequency where the input impedance appears to be purely resistive. How can this be, when the voltage and current distribution along the length of a half wave dipole when fed with an AC waveform of the resonant frequency are seemingly not in phase and in fact appear to be 90 degrees out of phase?

## Accepted answer (score 0, by Andrew)

Thanks to everyone who provided answers to this question, but none are completely correct, so after all this time I have answered the question myself.

This image appears in the Wikipedia article for Half Wave Dipole.

The voltage and current shown in the image is the actual voltage and current of the standing wave which exists along the elements of a resonant half wave dipole antenna. The standing wave on the antenna is circulating reactive energy present due to the fact that the antenna is a resonant system.

The voltage and current of the standing wave are always about 90 degrees out of phase with each other. The voltage of the standing wave always lags the current by a bit less than 90 deg, and for a given antenna and frequency of operation this phase difference is constant at each point along the length of the dipole elements.

The departure of phase difference away from 90 deg between the voltage and current of the standing wave is the non-reactive energy of the standing wave which results in radiation. Reactive energy stays in the antenna as circulating resonant energy and non-reactive energy leaves the antenna as radiation. For a high Q antenna the source tops up the much larger in amplitude energy of the standing wave as energy is radiated away.

The phase difference between voltage and current of the standing wave does not determine the reactance present in the center feed point impedance. Rather, it is the phase difference between that of standing wave and of the source which determines what the reactance in the impedance will be.

The voltage and current of the source at the center feed point are in phase. At resonance, the current of the standing wave is exactly in phase with that the voltage of the source, and the voltage of the standing wave, which is out of phase by almost 90 deg, is at the zero crossing point and so is zero all the time at the feed points and so contributes no reactance to the feed point impedance.

At resonance the current of the standing wave is in phase with the source because the ends of the dipole elements are an electrical 1/4 wavelength away from the feed points.

This presents a low impedance with no reactance between the two center feed points.

Hope that helps to clear up some of the confusion !

## Answer (score 5, by user15838)

Andrew, the typical graphics showing standing waves are showing voltage and current *distribution* along the wire, not phase shift from each other. Voltage and current are always in-phase at every point, they are syncronized in time, so there are no reactive components in the impedance. The instant of time when voltage is at its max peak also current is at the same value. The same is true at the zero crossing instant or at any other time. This happens at the center of the antenna, at its extremes, and at all the points in between. This fact is useful in the off-center feed dipole (aka OCF dipole), which is feed at a point where it has about 200 ohms with a 4:1 balun. This points have about the same impedance at several bands, making it a multi-band antenna.

## Answer (score 4, by Cecil - W5DXP)

Andrew, a dipole is a standing wave antenna. That means that the energy existing on the dipole that hasn't been radiated is in standing waves which do not change phase. The equation for a standing current wave is $I(x,t) = I_{\max} \sin(kx) \cos(\omega t)$. The distance $x$ determines the magnitude of the standing wave, not the phase. Only time determines the phase. At any instant in time, the phase of the standing wave is the same all up and down the length of the antenna. At resonance, the standing wave voltage and standing wave current are everywhere in phase. The forward current and reflected current are coherent phasors of close to equal magnitudes rotating in opposite directions. It's obvious that their sum would have constant phase. Same is true for the forward and reflected voltage phasors.

Phase has two different meanings for this context. The amplitudes of the voltage standing wave and current standing wave are out of phase in time but the phase of the voltage standing wave and current standing wave are in phase, i.e. equal in time.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12110/how-can-the-impedance-of-a-half-wave-dipole-at-its-resonant-frequency-be-purel, by Andrew, user15838, Cecil - W5DXP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
