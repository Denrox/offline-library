# GNU Radio sinusoid multiplication does not produce perfect results

*Tags: software-defined-radio, gnuradio · score 8*

## Question

I created a simple sketch in GNU Radio that multiples two signals. One is a sine and the other is cosine. I paste a screenshot of it and its results below.

I have heard that in DSP, we can do almost perfect signal processing. Hence, I assume phenomena such as LO leakage and doubly balanced mixers are not applicable when already digitized signals are multiplied such as in the presented case.

However, after multiplying the following two consine signals in GNU Radio, I expect to see the sum & difference frequencies; nothing else.

To my surprise, I am seeing a big peak at the sum frequency followed by a series of multiple peaks on the FFT. I'm curious to know what I am missing here.

## Accepted answer (score 14, by Marcus Müller)

I expect to see the sum & difference frequencies.

You're multiplying two *complex sinusoids*, not a $\sin$ and a $\cos$, but

$$e^{j2\pi f_1t}\cdot e^{j\left(2\pi f_2t-\frac\pi2\right)}= e^{j2\pi(f_1+f_2)-j\frac\pi2}$$

So, only the sum frequency, as it should.

I am seeing a big peak at sum frequency followed by a series of multiple peaks on the FFT. I'm curious to know what I am missing here.

First of all, don't forget that unless your signal's period perfectly fits in the FFT length, you'll see *leakage*, i.e. the effect of convolution with a sinc. Your signal has a period of $\frac4{15}$. You'll find that you can't divide 1024 by that and get an integer. So, from a pure mathematical point of view, you *must* see leakage here.

Then, look at the scale of things: your theoretic peak is more than 120 dB above all your other side peaks. That's OK. That's a factor of $10^{12}$, and around the numerical accuracy of the floating point numbers used in this software. I can't think of a case where that becomes a problem

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10419/gnu-radio-sinusoid-multiplication-does-not-produce-perfect-results, by Denis, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
