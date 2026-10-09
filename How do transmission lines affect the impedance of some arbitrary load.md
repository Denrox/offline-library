# How do transmission lines affect the impedance of some arbitrary load?

*Tags: transmission-line, impedance · score 3*

## Question

Let's say I have something like a non-resonant dipole, so that impedance changes depending on frequency and could take any number of values.

Whatever that impedance is, how does adding transmission lines or baluns change the impedance seen by the transceiver?

## Accepted answer (score 3, by Phil Frost - W8II)

You are probably familiar with SWR, where 1:1 represents a perfect match. SWR quantifies the magnitude of mismatch between two impedances, such as the antenna and the transmission line. As the two impedances become more unequal, the SWR increases.

The SWR does not change with the length of the transmission line, as long as that transmission line is lossless. Usually transmission losses are low enough to be negligible for impedance calculations.

SWR tells you the magnitude of mismatch, but nothing about the relative impedances. For example, 25Ω and 200Ω are both a 2:1 SWR to 50Ω coax. There are also any number of complex impedances that are also a 2:1 SWR.

There is a more general concept to represent mismatches: reflection coefficient ($\Gamma$). It's a complex number that quantifies not only the magnitude of the mismatch, but also the phase.

I find it easiest to visualize on a Smith Chart. Let's say we have a 300Ω ladder line, and a load (an antenna, say) with an (arbitrarily selected) impedance of (90+150j)Ω. In the Smith Chart, the center represents our target impedance (in this case, 300Ω) and all the impedances are normalized to that value. So we divide (90+150j)Ω by 300 to get (0.3+0.5j)Ω, and plot that on the Smith Chart:

By measuring the distance from the center, and the angle, we get the reflection coefficient in polar coordinates.

That's the impedance of the antenna at the feedpoint, normalized to 300Ω. Now let's add a 300Ω transmission line of increasing length, and consider the impedance at the end of it that would be seen, for example by the transmitter.

As the transmission line gets longer, the equivalent impedance moves in a clockwise circle around the center of the chart. This changes the phase of the reflection coefficient, but not the magnitude. Since the magnitude is constant, so is the SWR.

The distance moved around that circle depends on how long the transmission line is. When its a half-wavelength, it will have gone a full circle. A full circle is just a half-wavelength because the reflection must travel over that half-wavelengh twice: there and back.

We can stop at any time and read our new position on the Smith chart. Then, multiply the values read from the Smith chart by the normalized impedance (300Ω in our example). In this example, we end up at (0.28-0.43j)Ω. Multiplied by 300 makes (84-129j)Ω.

What if now we add a 4:1 balun? Depending on which way we orient the balun, we can step the impedance up or down by 4. Let's step down: simply divide the impedance by 4 to get (21-32.25)Ω.

Now, let's add some 50Ω coax. Divide by 50 to get a normalized impedance of (0.42-0.645)Ω. Plot that:

As before, as the transmission line gets longer, the dot moves about the center in a clockwise circle. Multiply the final location by 50 to get the equivalent impedance seen by the transmitter.

As luck would have it, for this 50Ω coax we've ended up a little closer to the center, so the 50Ω coax will have a lower SWR than the 300Ω ladder line. I've just been picking arbitrary impedances and lengths, but with the careful selection of transmission line impedances and lengths this can actually be used to match loads.

## Answer (score 2, by abcd567)

The answer given by Phil Frost - W8II is comprehensive. Using Smith Chart makes it graphical and very easy to understand and very easy to use.

I am giving below the same answer, but in a mathematical form, in case some one is interested.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7174/how-do-transmission-lines-affect-the-impedance-of-some-arbitrary-load, by Phil Frost - W8II, abcd567. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
