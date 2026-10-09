# RG-174 to pull signal from 1st IF?

*Tags: coaxial-cable, modification · score 3*

## Question

I've built a high impedance buffer out of an op amp on a small piece of perf board. I'm going to attach the input to the first IF on an Icom IC-718 and the output will be pulled out to a jack that I've drilled into the case.

I know that I want to keep stuff as short as possible... but at the same time, there's no super good place to mount the board that I've created. How bad an idea is it to tap into the IF with a piece of RG-174 that's about 6 inches long between the IF and the board? I would tie the shield to ground as close to where I tap the IF as possible.

This is my first major modification to an expensive radio beyond repairs and I'm trying really hard to get it right the first time. :)

## Accepted answer (score 5, by Marcus Müller)

So, you say:

I don't care if the signals are delayed. I'm just tapping the line out to a pan adapter. I am most concerned about influencing the existing function of the receiver

And that's *exactly* what you're going to do with this.

Your Opamp circuit has a high impedance, which translates into "looks like an open end". That means that your tapping coax has a very distinct feature: A *reflection coefficient* of 1.

This can easily be seen by the "mismatch" equation: The ratio of electric field (voltage!) going through the interface between two transmission lines with different impedances and getting reflect is defined as:

$\Gamma = \frac{E^-}{E^+} = \frac{Z_2 - Z_1}{Z_1 + Z_2} $

with $Z_1$ being the impedance of the transmission line from which the wave comes, and $Z_2$ being the impedance of the second transmission line or the sinking device.

In your case, $Z_2\rightarrow \infty$, and hence

$$\begin{align} \lim_{Z_2\rightarrow \infty} \Gamma &=\lim_{Z_2\rightarrow \infty} \frac{Z_2 - Z_1}{Z_1 + Z_2}\\ &= \lim_{Z_2\rightarrow \infty} \frac{\frac{Z_2}{Z_2} - \frac{Z_1}{Z_2}}{\frac{Z_1}{Z_2} + \frac{Z_2}{Z_2}}\\ &= \lim_{Z_2\rightarrow \infty} \frac{1 - \frac{Z_1}{Z_2}}{\frac{Z_1}{Z_2} + 1}\\ &=\frac{1-0}{0+1}\\ &=1 \end{align}$$

That means that *all* energy put into that tap line returns to the line you've tapped – which is pretty logical! Where should the energy you "steal" from the original coax go if you don't sink it somewhere? It's pretty clear you'll have a bad SWR in this situation.

So let's look at the wave from your IF line:

It meets the point where you've tapped the original line. Let's assume that you've build a reflection-free splitter here – that's highly unlikely, but it makes things both better for your use case, and easier to understand.

So, the wave enters your 6 inch (really, inches are a terrible unit for RF design – with meters, and hertz, everything can be calculated without converting) line. That's about $d=0.15\text{ m}$.

Now, RG-174 has a *velocity factor* of 0.66 – meaning that a wave travels with $\frac 23$ of the speed of light in vacuum, which is accurately enough $v_{RG-174}=\frac 23 \, 3\cdot 10^8\frac{\text m}{\text s} = 2\cdot 10^8\frac{\text m}{\text s}$.

So, for the distance between your tapping point, and the end of your RG174, and back, the wave needs

$\Delta t = \frac{2d}{v_{RG-174}} = \frac{0.3\text{ m}}{2\cdot 10^8\frac{\text m}{\text s}}$.

After that time, the wave will hit the tapping point – and **interfere** with the original IF!

By adding up a wave and a delayed version, you have built a frequency-selective device – a *filter*.

Now, what's relevant here is to know the *phase* with which the interference will happen. Let's have a look at that.

The phase $\varphi$ of a signal is the delay, measured in full periods $T$ of the signal (and period is related to frequency by $T=\frac1f$; from your comment, $f=70\text{ MHz}$); in other words:

$$\begin{align} \Delta \varphi &= 2\pi \frac{\Delta t}{T}\\ &= 2\pi \frac{\Delta t}{\frac1f}\\ &= 2\pi \frac{\frac{2d}{v_{RG-174}}}{\frac1f}\\ &= 2\pi \frac{2df}{v_{RG-174}} &\approx 2\pi \cdot 0.1 \end{align}$$

In other words, you're overlaying your original IF signal with a 0.1 waveperiods delayed version of itself. That **will** cancel out specific frequencies, while others will be amplified.

Now, we could derive the frequency response of the **tapped delay line** filter you've built – but since that will in practice depend a lot on things that are hard to know beforehand, like reflection coefficient of your tap (since that massively changes impedance of the line, depending on a lot of things), exact length, etc, this would be pretty much in vain.

The essence is: don't tap analog coax lines. Simple as that.

Get a proper splitter with the correct input impedance, and make sure your opamp circuit is impedance-matched to your transmission line. Everything else will end in significant reflections, interference and frequency-dependent cancelation of signal that is hard to predict and to measure.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6328/rg-174-to-pull-signal-from-1st-if, by David Hoelzer, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
