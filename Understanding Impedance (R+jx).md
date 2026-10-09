# Understanding Impedance (R+jx)

*Tags: antenna · score 5*

## Question

In a typical antenna (lets say dipole for this discussion), the pattern below is observed in the impedance (R+jx) graph:

I'm trying to wrap my head around this graph.

Why does the resistance spike, and what is the significance of the interval it re-occurs?

Most R+jx graphs i've seen have similar curves, a near vertical reactive drop slightly before the resistive spike.

I understand the points along the reactance line where X=0 (or near), and resistance is a useful value to match the feed-line, but i'm trying to better understand the phenomenon above.

Thanks.

## Accepted answer (score 7, by tomnexus)

The graph is correct and shows the impedance of a thin dipole. As the frequency increases, its length relative to wavelength increases too. The impedance results from the physics of the current in the wire interacting with the electromagnetic fields it generates.

You can see the first resonance is at 40 MHz, where the imaginary part crosses zero) but the real impedance is quite low, 70 ohms, and not visible at this scale. This is where the antenna is about half a wavelength long. The second resonance occurs at 80 MHz, when the antenna is about a full wavelength, and at this resonance the real part of the antenna impedance is quite high, thousands of ohms.

The unfortunate thing about plotting impedance on a linear scale cartesian graph is you don't see the beautiful structure and the graph is dominated by the high-impedance peaks, which are regions we don't use often. The impedance change near full-wave resonance is faster than half wave, but this plot exaggerates it a lot.

If you have the raw data, try plotting it as a parametric curve with log-real on X and lin-imag on Y and see the shape it makes. I can't easily find one online but here is a photo from Kraus. It shows a *monopole* over a wide range of $L/\lambda$. (monopoles are much easier to measure, the length and impedance is half that of the dipole).

See the two (three) resonances as the length increases, Note also how the thick antenna has a smaller spiral than the thin one.

Antennas are useful at many lengths, but there are reasons we like to use them at certain specific ones - mainly because of the impedance and the radiation pattern. Some examples from shortest to longest:

1. Very short (monopoles usually) - (impedance of 3-j1000 ohms. Only used when we can't make the antenna any longer (think of a 40 metre wavelength and a vehicle whip antenna). The short antenna has a low real part and a high capacitive impedance, so a series inductor is used, followed by a matching network to raise the real part to 50 ohms
2. Half wave dipoles (73+j0) or monopoles (36+j0) are quite useful. Not so much because they're resonant but because the *VSWR to 50 ohms* is lowest around resonance. They can thus be used in a 50 ohm system without any impedance transformation
3. full-wave dipoles (2500+j0) or their monopole equivalent, the end-fed half-wave are useful because of their high impedance, so can be fed with a high ratio transformer (say 49:1 impedance). Because of this high impedance, very little current is required on the counterpoise, so these are good on fibreglass boats where there is no metal ground plane available
4. 5/8 wavelength monopoles (50-j150) are useful because the *real* impedance is 50 ohms (not the 36 of a resonant monopole) and the ~150 ohms of capacitance can be cancelled with a modest inductor at the base. It's also the longest you can make a monopole without *pattern break-up*. The 5/8 has a few dB of gain over the 1/4 wave monopole, but any longer and the gain on the horizon starts to fall as the main lobe splits into two.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20964/understanding-impedance-r-jx, by t252, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
