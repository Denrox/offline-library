# How can quadrature mixing adjust the phase of all frequencies by the same amount? Can it be done in the digital domain?

*Tags: software-defined-radio, mixer, dsp · score 8*

## Question

This came up in some feedback I got when I tried to answer [What is IQ in the context of SDRs?](What%20is%20IQ%20in%20the%20context%20of%20SDRs.md) and revealed some of my own misunderstanding.

Initially, I gave an answer something like (paraphrasing):

You could collect I/Q data by taking a second sample delayed by 1/4th of the sample rate

That is, I had been imagining that the "quadrature" phase was related to a time offset relative to the **sampling** rate. But with some feedback I came to think that instead it was related to a time offset relative to a **local oscillator** and applicable only in the context of a mixer. So I said:

the quadrature component is equivalent to a second sample taken "90º later" in terms of the tuning frequency (i.e. delayed in time by 1/4 of the LO's period).

But even that explanation [was disputed](What%20is%20IQ%20in%20the%20context%20of%20SDRs.md) by someone with a better understanding, who said:

the phase shift is 90 degrees for *all* frequencies, because it's achieved not by adding a delay, but by changing the LO phase

How can that happen? What modulates the LO? How can all sorts of simple mixer circuits — and I've seen some that were just XOR logic chips?? — introduce just the right phase delay across the spectrum of one of its inputs as it multiplies it with the other? Or taken another way, assuming that a mixer is indeed necessary, does a mixer enable something that a scalar sampling process cannot accomplish alone?

Feel free to pick more convenient numbers, but let's say I have a ADC that can capture scalar samples all a generous rate of 1 GSPS. We are interested in receiving signals at 720 kHz and 1040 kHz and can optionally mix that RF input with a 1 MHz LO.

Originally I would have said: let's treat this stream of 1 GSPS scalar samples as a vector of 4 components coming in at a rate of 250 MSPS instead. Then the first component would be the "I" value, the second component would be the "Q" value and we'll just toss the other two. Thus the second component is 90º out of phase with the first. But apparently this is **not** what quadrature sampling means?

Trying again, what if we sample after mixing with the local oscillator (which I'll assume is phase-locked to the ADC)? With the input signals at A1 = 720 kHz and A2 = 1040 kHz and the LO of B = 1 MHz, we'll get the famed sum (A + B) and difference (|A - B|) products out for each and our ADC will see signals at 1720 kHz, 280 kHz, 2040 kHz, 40 kHz. We could now group our 1 GSPS sample stream so that it matches up with our 1 MHz LO, taking the first of every 10 samples as the "I" value and perhaps interpolate the second and third to get the "2.5th" sample for the "Q" value, 90º later relative to the LO.

Would I be able to feed those samples into a DSP unit as if it were I/Q data and get meaningful results out? Is there *any* sort of processing I could do to convert a stream of 1 GSPS scalar samples to "true" I/Q samples at 500 MSPS or even say 50 kSPS?

## Accepted answer (score 4, by Phil Frost - W8II)

An ideal frequency mixer simply multiplies its inputs. One input is the RF signal we wish to shift in frequency, and the other is the local oscillator (LO). For the moment, let's consider just an ideal frequency mixer where the LO is a pure sinusoid.

Since mixers are used to shift frequencies, we can use the Fourier transform to better understand their behavior in the frequency domain. I'm going to define the Fourier transform as:

$$ \hat f(\nu) = \int_{-\infty}^\infty f(x)e^{-i \nu x} dx \tag 1 $$

This is a bit dense, so breaking it down:

- $f(x)$ is the function to transform. In our case this is some function of time where $x$ is seconds,
- $e$ is the base of the natural logarithm (about 2.718), and
- $i$ is the imaginary unit, $\sqrt{-1}$,
- $\hat f(\nu)$ is the transformed function, where $\nu$ is frequency in radians per second.

The $e^{-i \nu x}$ term is a bit magic, but we can connect it to something more relatable with Euler's formula:

$$ e^{ix} = \cos x + i \sin x \tag 2 $$

So whenever you see $e$ raised to some imaginary power, think of this as simultaneously two sinusoids, one 90 degrees apart from the other. So, this:

$$ f(x)e^{-i \nu x} $$

takes our signal at time $x$ and multiplies it with both a sine and a cosine of frequency $\nu$, also at time $x$.

Then we throw this integrator operator around it all, which says that to find the value of the transformed function at one frequency $\nu$, sum the product of the function and those two sinusoids over all points in time. That is, convolve the function with a sine and a cosine for the frequency you want to know about.

Why a sine *and* a cosine? With the Fourier transform we are "probing" (with convolution) for something in the signal at every possible frequency. If we probe with just one sinusoid and the signal is 90 degrees out of phase with that, the result of the convolution is 0. Probing with both a sine and a cosine is sure to catch a signal of any phase, with the result being some complex number simultaneously representing sine and cosine parts. The argument of that complex number tells us the phase, and the modulus tells us the magnitude.

Now with a mixer, we are multiplying the signal with a cosine. So the mixer calculates:

$$ f(x) \times \cos(2\pi f_\text{lo} x) \tag 3 $$

and we want to know what the mixer does in the frequency domain, so we can do that by calculating the Fourier transform of this expression. And by calculate I mean we can look it up in a table and just take for granted that someone else has done the mathematical proof. The Fourier transform of two functions like this:

$$ f(x) g(x) $$

is

$$ {1 \over 2 \pi} \left(\hat f * \hat g\right)(\nu) \tag 4 $$

$*$ denotes convolution, and the hat denotes the Fourier transform. So to find the Fourier transform of two functions multiplied together, you can take the Fourier transform of each function and then convolve them. And then divide by $2\pi$.

One of the functions is just a cosine, so we can look that up in the table too, and see that the Fourier transform of $\cos(ax)$ is

$$ \pi (\delta(\nu - a) + \delta(\nu + a)) \tag 5 $$

$\delta$ is the Dirac delta function, which is 1 at 0 and 0 everywhere else. So this expression is a fancy way of saying $\pi$ at $\pm a$ and 0 everywhere else.

Convolution of a function with an impulse is simple: it shifts the function left or right. That there are two impulses explains image frequencies. So there you go, that's the mathematical basis for a common RF mixer that produces sum and difference outputs.

We can then look up $\sin(ax)$ in the table to see how things are different if we change the phase of the LO by 90 degrees:

$$ -i\pi (\delta(\nu - a) + \delta(\nu + a)) \tag 6 $$

It's the same thing, but multiplied by $-i$. The $i$ term comes from the $i \sin x$ term in equation 2 above. In other words, the result is rotated 90 degrees around the complex plane.

Note that the rotation is 90 degrees for all frequencies. This isn't something that can be accomplished by adding a time delay, because a 90 degree delay is a different time for every frequency. Mixers can do this "magic" because they are nonlinear components. Linear components can't multiply two functions.

Hopefully from here it's intuitively obvious that if changing the phase of the LO by 90 degrees changes the output of the mixer by 90 degrees, then this works for really any phase change as a superposition of these two cases.

It's a bit funny but it really does work. To demonstrate, try graphing these equations:

$$ y = \cos(50x) \cos(51x) \\ y = \cos(50x) \sin(51x) $$

We know the results will contain a high frequency component and a low frequency component, and they will both be in quadrature. Zooming in on a small part of the graph we can see the high frequency component, and indeed they are in quadrature:

Zooming out we can see the low frequency component, and that too is in quadrature:

It doesn't matter at all what the function on the left is: multiplying it by a sine and a cosine will always yield two functions with the same frequency spectra, but with the phases 90 degrees apart.

Bringing this theory to implementation, it's pretty difficult to make an analog component that exactly multiplies an arbitrary signal by a sinusoid. However it's not so hard to multiply a signal by a square wave: that's just an XOR gate or a switch. Analog implementations of switches can be pretty close to ideal especially when we're talking about relatively low frequencies. Changing the LO from a sinusoid to a square wave the function is much the same, except adding the odd harmonics to the LO means odd harmonics in the input will also be mixed down to baseband. In practice this is addressed by passing the signal through a low-pass filter to remove all those harmonics before the mixer.

## Answer (score 8, by Phil Frost - W8II)

Let's first start by developing some intuition of what a complex signal looks like. We can use GNU Radio to generate a signal that's just an unmodulated carrier, and then put that into a UI that will display the real and imaginary components over time:

The result for 80 Hz is this:

Notice how the real part is 90 degrees behind the imaginary part. If you were to plot this on the complex plane, it would trace a circle.

If we change the frequency to -80 Hz:

Now the phase difference is still 90 degrees, but it's the imaginary part that's lagging. Plotted on the complex plane it still traces a circle, but it spins in the opposite direction.

It's this property that allows complex signals to represent positive and negative frequencies.

Now importantly, this 90 degree phase shift holds for any frequency. If we change the frequency to 160 Hz but keep the sample rate the same:

The oscillation speed has doubled, as expected, but the phase difference between the real and imaginary parts is *still* 90 degrees.

This is why IQ data isn't equivalent to sampling twice as fast: the 90 degree phase relationship between real and imaginary components must exist for *every* frequency. By sampling the signal twice with some delay between samples, you can indeed introduce a 90 degree phase shift for *some* frequencies. But 90 degrees is a different amount of time for each frequency, so generating the imaginary component with just a delay will generate the correct results for only one frequency.

Since the imaginary component is just the real component +/- 90 degrees, if we had some kind of filter that could introduce a 90 degree phase shift for every frequency we could use that to convert from a real signal to a complex one.

Mathematically, that "filter" is called the Hilbert transform. It can be realized as an analog filter or a digital filter.

GNU Radio provides a "Hilbert" block which has a real input and complex output. It uses the Hilbert transform to create the imaginary part, where the real part is just the input passed through, with appropriate delay to match the delay added by the filter. We can use this block to take a real-valued signal and produce the equivalent complex-valued signal. The complex signal has (ideally) no negative frequencies present: it is an analytic signal.

It is interesting then to see what happens if we present this block with an input that contains more than one frequency, like a square wave:

Note how the real component is the square wave we expect, but the imaginary part certainly isn't just a delayed square wave. Once the real component is not a single frequency the 90 degree relationship between real and imaginary parts is no longer visually obvious from the time domain plot.

We can see however that the frequency domain is just what we'd expect for a square wave: a fundamental at 640 Hz and then a series of odd harmonics of that. Ideally there would be no negative frequencies present, but the ideal Hilbert filter has an infinite impulse response: truncating it introduces some imaging.

Finally we can take the complex value and split it into real and imaginary parts. We've already seen them in the time domain, but looking at them in the frequency domain we can see that really all the same frequency components are in both real and imaginary parts, just 90 degrees apart:

This visualization shows only the frequency magnitude but not phase, so the real and imaginary parts are drawn right on top of each other. We can also see that the discrete Fourier transform inherently produces complex results, but since we gave it real inputs the negative frequencies are exactly a mirror of the positive ones.

Perhaps now with a better intuition of what we're trying to accomplish with IQ sampling, how might we go about generating the digital stream of complex numbers from an analog signal which can have only real values?

One way would be implement an analog Hilbert filter, and feed that into the 2nd channel of an ADC. We can then treat one channel as the real part, and the other channel as the imaginary part.

However there would be little point in that: to realize an analog Hilbert filter that provides an accurate 90 degree phase shift over a wide range of frequencies requires a large number of components, and the filter can't add any information. This approach is used in some analog SSB transceivers for sideband cancellation, but if you're going to be digitizing the signal then a digital implementation would be cheaper and perform better.

Instead, we can feed the RF signal to not one but *two* frequency mixers:

You've probably read about how frequency mixers produce outputs with the sum and difference of the frequency components at the inputs. That's true, but what's the phase of the outputs? Turns out if you change the phase of the LO, then the phase of all the outputs is changed by the same amount. And unlike a delay, modulating the phase in this way makes the same phase shift for *all* frequencies, just what we need to generate both real and imaginary parts for a complex signal.

It is simple (in terms of component complexity) to create this phase shift with a mixer because the mixer is a nonlinear device. That means it has access to mathematical operators that linear devices (capacitors, inductors, resistors, transmission lines) don't, namely the multiplication of two functions.

Furthermore, since both real and imaginary parts are available digitally, we don't need analog filters to deal with image cancellation. What would be considered "images frequencies" in an analog design are instead just negative frequencies in the digital domain, and since the signal can be manipulated as a complex number these negative frequencies don't present any ambiguity.

This is also why you can find direct-sampling SDRs that work up to a few hundred MHz, but they get pricey because an ADC operating at 1 Gsps isn't cheap, nor is the FPGA you'll need to process that data rate. Once the frequency becomes high enough that a mixer is required, SDRs are almost exclusively use an IQ architecture since it's simpler to implement.

## Answer (score 2, by Brian K1LI)

...it looks like a "quadrature mixer" is really just two separate mixers, with one fed by an LO to which a [constant] phase delay has been applied relative to the other's LO.

Yes ... and. Quadrature versions of the *modulating* signal may comprise the "baseband" inputs to the quadrature mixers:

Here's where "the phase shift is 90 degrees for all frequencies" becomes more challenging, because the baseband input may simultaneously include any number of frequencies superimposed on each other; think of how the strings of a musical instrument produce harmonics and extend that concept to the human voicebox to get an idea of the spectral complexity of the modulating signal.

Quadrature versions of the modulating signal can be produced by analog circuits, but the accuracy is limited by component tolerances. Jim Tonne's *QuadNet* applet gives an idea of the complexity and limitations of these circuits. Conversely, a digital computer can be used to apply a Hilbert transform to the input, producing a much more accurate and reproducible result with modern A/D and DSP technologies.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16495/how-can-quadrature-mixing-adjust-the-phase-of-all-frequencies-by-the-same-amou, by natevw - AF7TB, Phil Frost - W8II, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
