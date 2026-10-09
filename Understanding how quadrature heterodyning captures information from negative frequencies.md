# Understanding how quadrature heterodyning captures information from negative frequencies

*Tags: software-defined-radio, dsp · score 5*

## Question

The way I understand how SDR works, there is a receiver input, generally connected to an antenna pulling in signals from the ether. That input is connected to two mixers (linear multipliers), being mixed with the same LO frequency in both mixers, however, the two LO signals are 90º out of phase. This results in two output signals, commonly referred to as I and Q, I for the "in phase" signal, and Q for the "quadrature", or 90º out of phase signal.

Then, if there is a modulated (say AM modulated with voice) frequency of interest, we can tune the LO to the carrier frequency, and because of heterodyning principles we are now only having to deal with the baseband frequencies, which is much easier/cheaper to digitize.

Now if we would have only heterodyned with a single mixer, we would get the difference between the carrier frequency and the baseband frequencies, thus the upper sideband would now appear as frequencies from zero to the upper limit of the baseband frequencies, and the lower sideband would appear as a mirror image to that, thus, would be negative frequencies.

How do we deal with negative frequencies? FWIU, this is where the quadrature (Q) heterodyning comes in. Somehow by shifting the LO frequency 90º, the output from the Q mixer contains the information which was present in the lower sideband.

This is what I am having difficulty understanding/visualizing. I am sure Euler's formula comes into this, and could probably follow the math if presented to me (and by all means don't get me wrong, I am interested in seeing the math as well,) but I am having difficulty *visualizing* how this can be so.

For one thing, we talk about 2 LO signals 90º apart. But what determines which one is which? Ie, if I were to mix the incoming signal with only one LO output or the other, the incoming signal would not know the difference and in either case would give me difference frequency between the carrier and the baseband. It would look the same whether I heterodyned it with a sine wave of a cosine wave, because who knows what phase angle either of those waveforms would be to the carrier? It could be anything. At least in traditional superhet radios, it didn't matter.

So then why is I the "in phase" signal? In phase to what? The carrier? But then, following the reasoning of the previous paragraph, why would this matter?

## Answer (score 6, by hobbs - KC2G)

A negative frequency is just a positive frequency "in the opposite direction".

Imagine I have a transparent wheel, which has a black disc inside of it at one point near the edge. Now imagine I shine a light through the wheel's diameter from the side, so that the shadow of the disc appears on the wall. If I spin the wheel, you can watch the shadow going up and down on the wall in a sinusoidal pattern. If you graphed the height of the shadow on the wall vs. time, you could tell the frequency of the sine wave, and therefore the frequency of the wheel's rotation. But nothing you recorded from that shadow could tell you whether the wheel was spinning clockwise or counterclockwise!

Now imagine I added a second light, above the wheel (at a 90° angle from the first in the plane of the wheel), casting a shadow on the table below. This shadow will also move in a sinusoidal pattern, at the same rate as the other one, but with a 90° phase shift, and you could recover exactly the same frequency information by watching this shadow alone.

But if you recorded *both* shadows at the same time, you might notice that in some cases the "positive peak" of one shadow is 90° *ahead* of the other, and sometimes it's 90° *behind* instead. And in fact, the one case is when the wheel is turning clockwise, and the other is when the wheel is turning counterclockwise. (It doesn't matter which axis you define as the "first" axis, which direction you define as positive, or which direction you define as clockwise... as long as you make a choice and stick to it. Any change to one of them will swap the sign of your result).

So, sine and cosine are both 1-D projections of something happening in 2-D. With only one of them, we can't distinguish a "positive" frequency from a negative one, but with both of them, positive and negative frequencies behave differently, and we can use this property to recover information from frequencies that were downmixed "below zero" without running into the aliasing problems that we would have if we only used one.

## Answer (score 5, by Phil Frost - W8II)

Some quick definitions: a sinusoid with angular frequency $\omega$ and phase $\varphi$ at time $t$ is:

$$ \cos(\omega t + \varphi ) $$

Now let's consider a scenario: we have an ideal mixer with an LO with $\omega = 1$ and variable phase, and we want to produce an output at $\omega = 0.3$. We know we can do that with an input to the mixer with either:

1. $\omega = 0.7$ (because $1 - 0.7 = 0.3$), or
2. $\omega = 1.3$ (because $1.3 - 1 = 0.3$).

Now if I might reframe your question a bit, you've been told in the first case, somehow we get a negative frequency, because the input is below the LO; and in the second case we get a positive frequency because the input is above the LO. The question is, how can the mixer "know" if a frequency is positive or negative?

We are going to consider four ways we might mix:

1. Input below the LO, LO phase = 0
2. Input above the LO, LO phase = 0
3. Input below the LO, LO phase = $-\pi/2$
4. Input above the LO, LO phase = $-\pi/2$

### First case: Input below the LO, LO phase = 0

Mathematically, this is

$$ \cos(t) \times \cos(0.7 t) $$

Plot it:

It's plain enough to see this does indeed produce an output that's a low frequency sinusoid superimposed on a higher frequency one. Now, we are really only interested in the lower frequency term (1 - 0.7). We know that lower frequency term has $\omega = 0.3$, what's it's phase? Just eyeballing it, it looks like 0. So let's plot that again, with the low frequency term $\cos(0.3 t + 0)$ included:

So we can say:

$$ \cos(t) \times \cos(0.7 t) = {\cos(0.3t + 0) \over 2} + \dots $$

Here, $\dots$ denotes the higher frequency term that we don't really care about for this example.

### Second case: Input above the LO, LO phase = 0

$$ \cos(t) \times \cos(1.3 t) = {\cos(0.3t + 0) \over 2} + \dots $$

OK, the higher frequency term has changed of course, but the $\omega=0.3$ term we are interested in is exactly the same. It doesn't seem like there's any way to differentiate negative from positive frequencies from this.

### Third case: Input below the LO, LO phase = $-\pi/2$

$$ \cos(t-\pi/2) \times \cos(0.7 t) = { \cos(0.3t - \pi/2) \over 2 } + \dots $$

OK, there's still an $\omega = 0.3$ output, but the phase has changed. That would make sense, because the phase of the LO also changed. Moving on...

### Fourth case: Input above the LO, LO phase = $-\pi/2$

$$ \cos(t-\pi/2) \times \cos(1.3 t) = { \cos(0.3t + \pi/2) \over 2 } + \dots $$

Similar to the last case, but the phase has flipped by 180 degrees. It seems the phase of the mixer's output *changes* depending on whether the input was above or below the LO!

### Conclusion

When multiplying two sinusoids of the same phase, the output does not depend on whether the input to the mixer is above or below the LO.

But when the LO and the mixer input are 90 degrees out of phase, the output will be *inverted*, or not, depending on whether the input was above or below the LO.

It's this difference that allows an IQ mixer to "know" if a frequency is positive or negative. And it's also this difference that explains why complex multiplication can shift frequencies without dealing with image frequencies.

When an IQ mixer multiplies the same signal by two LOs each 90 degrees out of phase, it is effectively converting the input signal (which is a real function) into a complex function. Multiplying by $\cos(\omega_\text{LO}t)$ produces the real part, and multiplying by $\sin(\omega_\text{LO}t)$ produces the imaginary part.

If you think about this as plotted on the complex plane, two sinusoids 90 degrees apart will will trace a circle:  
*image source, which is unfortunately no longer online*

If you invert one of those functions but not the other by moving the signal to the other side of the LO, the result is tracing the same circle but spinning in the other direction.

If you want a purely real function, then what you need are two circles spinning in opposite directions. Added together, and in the right phase, their imaginary parts will cancel and you're left with only the real part.

And the same logic in the other direction, if you start with a purely real function, "under the hood" that's two circles spinning in opposite directions, a positive and negative frequency counterpart.

## Answer (score 2, by hotpaw2)

Negative frequencies in the real (single DOF measurement) world are just what we call positive frequencies that happen to below some other frequency.

Above baseband, that LSB signal isn't really negative, just lower than some reference frequency (the carrier).

The in phase signal alone isn't in phase to anything. It just has a related phase to a second (quadrature) signal. If the other signal (2) matches 90 degrees later (e.g. is less than half a period delayed), then the earlier signal (1) is the in phase signal. If the other signal (2) is delayed by more than half a period, that the same as that other signal (2) being earlier by less than half a period, making that other signal (2) the in phase signal.

When an RF signal is singly modulated down to baseband, its LSB will alias with its USB and thus both sidebands will get mixed together into a single signal. And if you FFT any strictly real signal (non-DC), you will see a complex conjugate mirror image. And can't tell original (before mixing) USB from LSB data.

When quadrature modulated down to baseband, you get two resulting signals.

When mixing (by multiplication) two sinusoids different in frequency, a beat note at the difference between the two input frequencies will appear. The zero crossings of the beat note will appear when the 2 sinusoids are temporarily 90 degrees apart, e.g a peak of one sinusoid near the same time as a zero crossing of the other. The peaks of the beat note will occur when the peaks of the two sinusoids either align or go in opposite directions. Which (same or opposite peak alignment) happens next will depend on whether the difference between in frequency between in input signal and the modulating signal is positive (higher) or negative (lower).

When quadrature modulated down to baseband, you get two "beat note" results; one for I, and one for Q. The phase difference of the two "beat note" results from an LSB signal will be opposite to that of phase difference between the two "beat note" results from an USB signal (of the same offset).

Thus a complex FFT of the IQ baseband signal can differentiate between the two different sidebands, as they won't be strict conjugate mirror images, due to this phase difference in the two different "beat notes".

And you can thus "get" one or the other sideband by looking at the FFT result, or any similar process.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17705/understanding-how-quadrature-heterodyning-captures-information-from-negative-f, by KevinHJ, hobbs - KC2G, Phil Frost - W8II, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
