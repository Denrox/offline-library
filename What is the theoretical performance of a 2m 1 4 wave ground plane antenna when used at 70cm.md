# What is the theoretical performance of a 2m 1/4 wave ground plane antenna when used at 70cm?

*Tags: antenna, wire-antenna, vertical-antenna, 70cm-band, 2m-band · score 3*

## Question

If I have a 2-meter 1/4 wave ground plane antenna with 1/4 wave radials bent down at approximately 45 degrees, what kind of performance in terms of SWR and gain pattern can I expect when using it on the 70cm band, relative to its performance on the 2 meter band?

## Accepted answer (score 3, by Phil Frost - W8II)

Let's assume that this antenna you describe, when operated at 145 MHz, has an SWR of 1:1, and behaves like an ideal antenna. At 145 MHz, the 1/4 wave vertical, plus the image antenna formed by the ground plane, make it effectively like a 1/2 wave dipole. It will have a free-space radiation pattern like this, for an antenna oriented vertically along the Z-axis:

At three times this frequency (435 MHz), the antenna will be resonant again. That means its impedance is unchanged, so if you had a 1:1 SWR at 145 MHz, you will have a 1:1 SWR again at 435 MHz.

However, the radiation pattern is different, because now it's not a 1/2 wavelength dipole, but a 1 1/2 wavelength dipole. The radiation pattern looks like this:

In the latter case, at 435 MHz, the maximum gain is the same as it was at 145 MHz. However, the lobes are narrower, and higher elevation. There's a secondary lobe around the horizon, but it's even narrower, and about 4 dB below the main lobes.

These images are from antenna-theory.com, which has a good deal more to say on the issue. Everything there about dipoles is also relevant to verticals, which are just dipoles where half of the dipole is formed by an image antenna through the ground plane.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1532/what-is-the-theoretical-performance-of-a-2m-1-4-wave-ground-plane-antenna-when, by Andrew N5ITM, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
