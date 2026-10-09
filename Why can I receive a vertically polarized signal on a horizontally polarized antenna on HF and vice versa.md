# Why can I receive a vertically polarized signal on a horizontally polarized antenna on HF and vice versa?

*Tags: polarization · score 6*

## Question

One explanation I found is that a signal reflected from ionosphere is always circularly polarized. Thus it can be received by both vertically and horizontally polarized antennas (naturally, with 3 dB attenuation). However I don't trust the source very much and thus decided to ask for a second opinion.

Is this explanation accurate or is the truth a little more complicated?

## Answer (score 5, by Phil Frost - W8II)

Why can I receive a vertically polarized signal on a horizontally polarized antenna on HF and vice versa?

Who says you can?

Cross-polarization is a common source of path loss even on HF. LZ1AQ has some experiments which show as much as a 25 dB difference between horizontal and vertical polarization. [25 dB is quite a lot](How%20big%20is%20a%20decibel.md), enough to make the difference between 100% copy and unintelligible.

In practice, ionospheric propagation changes rapidly and unpredictably, and the polarization might be rotated 90 degrees one instant, and 30 seconds later, not rotated at all. As such, trying to match the other station's polarization is a futile game of chance. So it's not so much that the problems with opposite polarization don't exist on HF, but rather they are just unavoidable.

Unless of course you have both horizontally and vertically polarized antennas to choose from, and some mechanism to combine them dynamically in the best way in the moment. This is called *diversity reception*, and it can greatly increase the robustness of a receiver. It could be as simple as a switch between two antennas, or two separate receivers and antennas driving different ears on headphones, or a pair of phase-coherent receivers and a dynamic algorithm that finds the best combination for each moment.

Why is the fading only 25 dB, and not much more? Theoretically, the coupling between cross-polarized antennas should be zero, but in practice there's always a bit of overlap. Polarization is not a binary choice between "horizontal" or "vertical", but can be any angle. The coupling between antennas is proportional to the cosine of the difference between the angles, so there's infinite loss only when the polarization is exactly 90 degrees apart.

Furthermore, most paths, and especially ionospheric paths, are not truly just one path: they are the combination of many paths. It is very unlikely all possible paths at any given time will be cross-polarized.

Finally, all real antennas are somewhat sensitive to the opposite polarization though imperfections in their design. For example, a horizontal dipole often has a vertical feedline. Although not an ideal behavior, the antenna will be somewhat sensitive to common-mode currents on this feedline which will be vertically polarized.

## Answer (score 4, by Cecil - W5DXP)

Reflections from the ionosphere are randomly distorted from the original polarization - but not circular. Polarization matters for ground waves but not for most sky waves.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12667/why-can-i-receive-a-vertically-polarized-signal-on-a-horizontally-polarized-an, by Aleksander Alekseev - R2AUK, Phil Frost - W8II, Cecil - W5DXP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
