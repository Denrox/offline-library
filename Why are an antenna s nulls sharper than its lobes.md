# Why are an antenna’s nulls sharper than its lobes?

*Tags: antenna-theory · score 7*

## Question

Why, for realistic directional antennas, are its nulls sharper (deeper, narrower, etc.), than the radiation pattern’s lobes (local angular maxima)? Is there some physics or mathematical geometry to EM fields that requires this to be true?

Or is there a some way to do the opposite, make an antenna with sharper (narrower) lobes than nulls?

## Answer (score 8, by glen_geek)

Its all in the nature of nulls:  

Two signal sources (same frequency) can possibly **subtract exactly** producing a *very deep* null.


Two signal sources (same frequency) can only **add constructively** to *double* amplitude, at best.

Or, if you wish, imagine a sinusoidal wave whose average value is 1.0, and whose peak is also 1.0. I've chosen a frequency of 1 Hz, but that's not really important.

- The sinusoid **adds** the 1.0 DC to the 1.0 peak to produce a peak of 2.0.
- The 1.0 DC **subtracts** from the other peak to produce exactly 0.0.  
Even though the subtraction goes to zero very smoothly, the approach to zero is very sharp, which can be seen on a log plot of the waveform. The approach to the 2.0 peak is certainly not-so-sharp.

## Answer (score 8, by Phil Frost - W8II)

To increase an antenna's gain, the elements of the antenna must be arranged such that they interfere constructively in the intended direction, and destructively in every other direction. This is possible because varying the distance to an element varies the phase of the wave, so in some positions the phase difference is such that the waves interfere constructively, while in other positions the waves interfere destructively. Most positions experience some interference somewhere between these two extremes.

Now let's consider the math of wave interference a bit with a simple example. Wikipedia has the full derivation, but the tl;dr is the addition of two identical waves differing only in phase by $\varphi$ is:

$$ \underbrace{A\cos(kx-\omega t)}_\text{wave 1} + \underbrace{A\cos(kx-\omega t+\varphi) }_\text{wave 2} = \underbrace{2A\cos \left( \varphi \over 2 \right)}_\text{amplitude} \cos\left(kx-\omega t+{\varphi \over 2}\right) $$

That is, summing two sinusoidal waves identical except in phase together, the result is a sinusoid of amplitude proportional to $\cos(\varphi/2)$.

A quick graph of that:

Keep in mind we aren't looking at the resulting wave as a function of time, we're looking at the amplitude of the resulting wave as a function of phase difference between the two component waves. That they are both sinusoids is coincidental.

Antenna patterns do not usually distinguish polarity, but sometimes you find one that does and you will see each lobe alternates in polarity. What's happening is for the purposes of the radiation pattern we really just care about the absolute value of the amplitude of the resulting wave. So now, a graph of $|\cos(\varphi/2)|$:

Now one sense of "sharp" means an abrupt change in direction. > is sharp. ) is blunt. You could say something is sharp if there is a discontinuity in the derivative. The nulls certainly look like they do, but if you consider the polarity of the lobes, there is not actually a discontinuity. That's just an artifact of taking the absolute value of the amplitude for the purposes of the polar plot.

Another sense of "sharp" is "not wide". The reason it's hard to make very narrow lobes is mathematically similar to the reason a pulse train has infinitely many harmonics. Our simple example considered only 2 waves from 2 antenna elements, but if you want more complex antenna patterns you can create them by adding together spherical harmonics just as you can create any periodic waveform by adding together harmonically related sinusoids. However, the number of antenna elements, and thus the number of spherical harmonics that can be added together, is limited by practicality.

## Answer (score 5)

Well, antenna gain plots are logarithmic, and $\log(\sin^2(x))$ hits negative infinity for every zero transition of the sine's power, so while the power of some directivity pattern may actually touch its minima as gently as its maxima (it depends on just what kind of transition is there, though), in a logarithmic gain plot you get to see a lot more drama.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18694/why-are-an-antennas-nulls-sharper-than-its-lobes, by hotpaw2, glen_geek, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
