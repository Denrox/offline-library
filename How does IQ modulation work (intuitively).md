# How does IQ modulation work (intuitively)?

*Tags: software-defined-radio, theory, math, mixer, modem · score 10*

## Question

I'm trying to get my head around IQ modulation. What I understand so far is that each of the I and Q branches of the mixer produce two sidebands with the same frequency components, but in the Q branch, these sidebands have opposite phase to each other. So when we add the I and Q components together, we get an upper sideband consisting of I+Q and a lower sideband consisting of I-Q.

Then, on the receiver side, the I mixer causes the two sidebands to be imaged onto each other (giving I + Q + I - Q), while the Q mixer does the same thing, but shifts the phase of the lower sideband again, giving I + Q. And the point of all this is that we don't waste any bandwidth with redundant sidebands.

Assuming that this "signal cancellation" view is correct, is there an intuitive way to understand why the lower sideband of the Q output gets phase shifted relative to the upper sideband? This article seems to say that it can be understood simply in terms of the basic trigonometric identities

$$\cos A \cos B = {\cos(A+B) + \cos(A-B) \over 2}\\ \cos A \sin B = {\sin(A+B) - \sin(A+B) \over 2}$$

It's easy to see why this has the desired effect when both baseband signals are represented simply as $\cos A$: the second term in the second identity is negative. But does that explain it completely? Other sources suggest (eg. here) that this phenomenon involves the Hilbert Transform (which I don't really understand). Although, strangely, they're only saying that Hilbert is needed to understand the demodulation side, whereas with my view of things I was expecting the process to work the same way for both modulation an demodulation.

So does the trigonometry above explain it, or is that just a special case when both I and Q are cosines? Or am I on the wrong track completely?

## Answer (score 15, by Phil Frost - W8II)

I think it's more intuitive if you unlearn some things first.

Oscillation is *not*:

$$ \cos(\omega t) $$

where $\omega$ is the angular frequency in radians per second, and $t$ is time.

Rather, oscillation is:

$$ e^{i \omega t} $$

By Euler's formula this can be expanded to:

$$ \cos(\omega t) + i \sin(\omega t) $$

If you plot this function on the complex plane, you get a circle:

Why bother with this circle thing? Well, the circle can spin counterclockwise with a positive frequency as shown in the animation. Or it can spin clockwise, and that's a negative frequency. You can't unambiguously represent negative frequencies with just a line wave because $\cos -x = \cos x$ and $\sin -x = -\sin x$. Thus you can't tell with just a sine wave if a frequency is positive or negative, but you can tell with a circle by which way its spinning.

This is useful because it's simple. Frequency mixers multiply things; what happens when you multiply two of these circle-oscillations together?

$$ e^{i\omega_1 t} \times e^{i\omega_2 t} = e^{i(\omega_1 + \omega_2)t} $$

So, this circle-mixer doesn't make sum and difference terms at its output: there's just a sum term. There are not two sidebands: there's just one. There is no image frequency. And since frequency can be negative, this circle-mixer can convert frequencies up or down. Much simpler than the old kind of mixer.

The only trouble is this: to implement this in analog electronics, where the signal is represented as a voltage, and where voltage can have only real values, how to we represent the complex numbers in this math?

You'll have to build two analog circuits, where the voltage of one represents the real part, the other the imaginary part. You are trying to understand an IQ demodulator as two mixers. But you've got it backwards: an IQ demodulator is just one mixer. And what you previously thought of as a mixer is actually two mixers.

Why? Well, consider what happens if you add two circle-oscillations together, one with the negative frequency of the other:

$$ e^{i\omega t} + e^{i (-\omega) t} $$

Expand with Euler's formula:

$$ \cos(\omega t) + i \sin(\omega t) + \cos(-\omega t) + i \sin(-\omega t) $$

Using the identities $\cos -x = \cos x$ and $\sin -x = -\sin x$:

$$ \cos(\omega t) + i \sin(\omega t) + \cos(\omega t) - i \sin(\omega t) \\ = 2 \cos(\omega t) $$

So when you have a sinusoidal function which is purely real, *you can think of that as the superposition of a positive and negative frequency*.

So you might have thought mixers multiply some input $x(t)$ by a sinusoid to compute their output, like this:

$$ x(t) \times \cos(\omega t) $$

But really that one physical device is simultaneously computing *two* multiplications, because $\cos(\omega t)$ is a superposition of positive and negative circle-oscillations:

$$ x(t) \times e^{i \omega t} + x(t) \times e^{i (-\omega) t} $$

Now you see where the sum and difference frequencies come from.

## Answer (score 5, by carloc)

I believe a good point of view is the concept of orthogonality.

This is clear under everybody's eyes when seen in physical space, take for instance a 2-dimension space, a plane.

In the example above any point on the plane can bear two *indipendent* informations, its x and y. The keyword here is indipendent, I can freely change one, let's say go from x1 to x2 while leaving the other unchanged.

This indipendence is given by the orthogonality of the two axes choosen, in the plane depicted we may say that $\alpha=90^\circ$

In more general way we might say that orthogonality/indipendance is given by the dot-product of any vector laying on the two axis being zero, for instance $$\bar x_1 \cdot \bar y_1=|x_1|\,|y_1| \cos \alpha=0$$

This same concept of orthogonality can be extended to any space where such a dot-product can be defined.

Electrical signals are (surprisingly) such a space, and a good dot-product suitable for periodic signals is the average over one period of their product. $$\bar{ x(t)} \cdot \bar{y(t)}=\frac{1}{T}\int_T x(t)y(t)\mathrm{d}t$$

It can be easily proved that any $\cos(\omega t)$ and $\sin(\omega t)$ are orthogonal

$$\frac{1}{T}\int_T \sin\left(\frac{2\pi}{T}t\right)\cos\left(\frac{2\pi}{T}t\right)\mathrm{d}t=0$$

and can hence be used as carriers to bear two indipendent information, namely I and Q channels.

A lot of details has been left over but I believe that's the core.

## Answer (score 3, by Phil Frost - W8II)

First let's look at what happens in the case of a single mixer:

We know that mixers produce sum and difference frequencies. That is to say, the Fourier transform will contain impulses at $f_1 + f_2$ and also $f_2 - f_1$. Or is it $f_1 - f_2$?

It doesn't actually matter, and it's important to understand why. The Fourier transform is defined in terms of complex exponentials:

$$ \hat f(\xi) = \int_{-\infty}^\infty f(x)e^{-2 \pi i x \xi} dx \tag 1 $$

By Euler's formula:

$$ e^{ix} = \cos x + i \sin x \tag 2 $$

To by taking the Fourier transform we are convolving $f(x)$ with a complex exponential at every possible frequency to answer the question "how much does this function look like this frequency?"

But the inputs and outputs to this mixer are single voltages and thus must be real functions, so how can real functions look like complex exponentials which have a non-zero imaginary part?

To resolve this, it's important to understand that a real function can be represented by adding together complex exponentials of positive and negative frequencies. Brian K1LI has provided a nice graphical animation of this. You can also convince yourself that $e^{-ix} + e^{ix} = 2 \cos x$.

With that in mind, what's the mixer above do? Multiplication of two functions is equivalent to convolving their Fourier transforms. So considering that real functions have Fourier transforms which are symmetrical about frequency 0, what the mixer above calculates is:

Notice that the assumption is made that $f_2<f_1$, which makes $f_2-f_1$ positive. But if it was the other way around it wouldn't matter, since a negative answer is *also* correct. Because the output of this mixer is a real voltage, the Fourier transform of the output must contain both positive and negative frequencies.

Because real functions have Fourier transforms that are symmetrical about zero, talking about their negative frequencies doesn't add any insight. But it is critical to grasp that they are there anyway, because that leads to a much simpler mathematical explanation, and thus better intuition about how things like mixers work.

Now what about an IQ mixer, like this:

While your first instinct may be to think of this as two mixers, I find it more insightful to view it as a single mixer which can operate on complex numbers by representing the real part as one voltage, and the imaginary part as another voltage. Viewed this way, this mixer is simply multiplying by a complex exponential:

$$ \begin{align} y(t) &= \cos(2\pi f_1 t) \cdot e^{2\pi f_2 t} \\ &= \cos(2\pi f_1 t) \cdot \cos(2\pi f_2 t) + \cos(2\pi f_1 t) \cdot i \sin(2\pi f_2 t) \end{align} $$

Recall from equation 2 that the $e^{2\pi f_2 t}$ is comprised of real cosine and imaginary sine terms, which are the inputs to each branch of the mixer.

Now the complex exponential, unlike a sinusoid, has a Fourier transform which doesn't need to be symmetrical about zero. So in the frequency domain, this mixer calculates:

Now the output isn't symmetrical about zero in the frequency domain, and so negative frequencies have some utility.

Notice that there are now half as many impulses in the Fourier transform. The mixer no longer calculates sum and difference frequencies, but just sum frequencies. Pretty handy, if we can figure out a to separate negative and positive frequencies! But...

## What's a negative frequency?

### Explanation 1: spinning backwards

A sinusoid is a real function. It can move only in one dimension: the real number line. Sinusoids oscillate only "left to right". So only positive frequencies make sense.

But a complex exponential is a complex function. It can move in two dimensions, the imaginary and real axes on the complex plane. Complex exponentials oscillate in circles, like a spinning top or wheel. Things can spin in two directions. Frequency is how fast phase changes over time, and phase can increase (move counter-clockwise around the circle) or decrease (clockwise).

So think of frequency as a one-dimensional vector with both a magnitude (how many times per second it spins) and direction (counter-clockwise or clockwise). Just as a negative current doesn't mean less than zero charge is moving, but rather just means charge is moving is the opposite the conventionally positive direction, a negative frequency doesn't mean the top is spinning less than zero times per second, it just means it's spinning the other way.

### Explanation 2: math

This is a positive frequency:

$$ e^{ix} = \cos x + i \sin x $$

This the negative of that frequency is just the negation of $x$:

$$ \begin{align} e^{-ix} &= \cos -x + i \sin -x \\ &= \cos x - i \sin x \end{align} $$

Notice that positive and negative frequencies are identical in the real part (blue), but have opposite phase in the imaginary part (red). For a positive frequency, the imaginary part leads by 90 degrees. For a negative frequency, the imaginary part lags 90 degrees.

### Explanation 3: mixers

This is not a complete explanation, but maybe insightful regardless. Consider the multiplication of a sine and a cosine, of different frequencies. In one case the sine is 1.6 the frequency of the cosine, and in the other case the cosine is 1.6 times the frequency of the sine:

You can see in either both the upper and lower sideband. But notice that the phase of the upper sideband is equal in either case, while for the lower sideband the phase is opposite in each case.

Notice also this doesn't work when both functions are $\cos$, because obviously

$$ \cos(x) \cos(1.6x) = \cos(1.6x) \cos(x) $$

So clearly there is some way to distinguish between signals that are above the LO versus those that are below, but it only works when the inputs are in quadrature, which is why if you don't know the phase of the signal you're looking for, you need two mixers to do this trick.

Now back to our problem. We're looking at the output of the IQ mixer, which has a Fourier transform like:

If you were to casually look at either the real or imaginary parts of this mixer output, you might not notice that it's different than the single mixer case. Given the above explanations about negative frequency, you can tell from this Fourier transform that the impulse at $-f_1+f_2$ still means something is happening $|-f_1+f_2| = f_1-f_2$ times per second, just as before. You can't tell that it's a negative frequency because what makes it negative or positive is not how many times per second it happens, but rather the relative phase of when it happens between the imaginary and real parts. You can't tell that by looking at just the real or just the imaginary.

But if you were to look closely at the thing happening $f_1-f_2$ times per second, you'd notice that it happens first on the real part, with the imaginary part lagging behind 90 degrees. That is what makes it a negative frequency.

You would also notice something happening $f_1+f_2$ times per second. But there you would notice that it is the imaginary part leading with the real part lagging. That is what makes it a positive frequency.

## Converting back to a real function

You could digitize the I and Q parts in an ADC, then process them digitally as complex numbers. But regardless, if this is something like an SSB signal, at some point you'll want to convert it to a real function because obviously complex numbers aren't compatible with headphones and microphones.

To do that, you require something that can introduce a phase shift of 90 degrees for all frequencies. Mathematically, that is the Hilbert Transform. The Hilbert transform can be approximated with discrete components, such as in the QRP Labs polyphase network. One of the articles you linked calls it a "90 degree hybrid".

Given such a device, separating positive and negative frequencies is possible. If you shift the imaginary part forward 90 degrees, then for positive signals the imaginary and real parts have equal phase and reinforce, but negative frequencies have real and imaginary parts in opposite phase and cancel. If you swap the phase shift or do it to the real part instead of the imaginary, you can just as easily keep the negative frequencies and discard the positive ones, which is what you might want to do for LSB demodulation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18093/how-does-iq-modulation-work-intuitively, by John B, Phil Frost - W8II, carloc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
