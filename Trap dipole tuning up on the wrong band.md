# Trap dipole tuning up on the wrong band

*Tags: hf, antenna-construction · score 3*

## Question

I'm building a trap dipole for the high HF bands, 10 / 12 / 15 / 17.  
So far what I've got in the air is:

- The 10 meter section (4.92 meters, 16.14 feet, resonant at 29Mhz)
- The 10 meter traps (8pF cap in parallel with a 4µH inductor, resonant at ≈28Mhz)
- The 12 meter section (80 cm, 31.5 inch)

```
 8pF/4µH                             8pF/4µH
 ----{10M}------------{Balun}------------{10M}----
 0.4M        2.46M        ║       2.46M          0.4M
║
║ 30.4M coax

```

Now take a look at the output from my antenna analyzer:

Whhaaaat... Well, I'm happy with the 10 meter resonant point (given by M1) but what the heck happened next? I read somewhere that traps would electrically shorten all subsequent dipole sections, but i'm not sure what to make of this. Why would the 12 meter section be so far out of tune. Any ideas?

## Accepted answer (score 2, by Phil Frost - W8II)

Traps require that the sections that follow them to be shortened because they look like loading coils. We can demonstrate this by calculating the impedance of your trap at 28MHz and 24.9MHz.

The impedance of a parallel LC circuit is given by:

$$ Z(\omega) = -j \left( 1 \over C \right) \left( \omega \over \omega^2 - \omega_0^2 \right )$$

Where

- $\omega = 2 \pi f$
- $\omega_0 = 1 / \sqrt{LC}$

So for your trap:

$$ \omega_0 = {1 \over \sqrt{4\:\mathrm{\mu H} \cdot 8\:\mathrm{pF}}} = 176776695 $$

This is the resonant frequency in radians per second; if we divide by 2π we see that it's 28.13MHz as expected. We can then calculate the impedance at the relevant frequencies:

$$ Z(28\:\mathrm{MHz}\cdot 2 \pi) = j73.6\:\mathrm k\Omega \\ Z(24.9\:\mathrm{MHz}\cdot 2 \pi) = j2.89\:\mathrm k\Omega $$

In the case of 28MHz, the trap is a high impedance, and this serves to reduce the current on the section past the trap to some negligible level.

At 24.9MHz the impedance is much lower, but it's not nothing. Additionally, it is no longer a quarter-wave down the antenna, but something less. Because this impedance is purely imaginary and positive, it's an inductive impedance. We can divide the reactance (the imaginary part of impedance) by ω to get an effective inductance:

$$ {2.89\:\mathrm k\Omega \over 2 \pi \cdot 24.9\:\mathrm{MHz}} = 18.5\:\mathrm{\mu H} $$

Thus, at 24.9MHz (and just that one frequency), the trap looks just like a 18.5μH inductor. Just like a loading coil.

Because the coil is not at the base of the antenna but closer to the tip, its effect on the feedpoint impedance somewhat diminished. [I don't know the exact math](How%20does%20an%20antenna%20transform%20impedances%20along%20its%20length.md), although you can find loading coil calculators around the net. Normally we use a loading coil when we don't have room for a full-sized antenna, but here we are reasoning in the opposite order: because you have a loading coil, your antenna can't be full-size.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3605/trap-dipole-tuning-up-on-the-wrong-band, by Turingrad, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
