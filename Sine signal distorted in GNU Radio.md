# Sine signal distorted in GNU Radio

*Tags: gnuradio · score 6*

## Question

I am starting off with the Ettus Research lab-1 - lab-5 tutorial to learn GNU Radio. I have set up the following super simple flow graph. I am using WX GUI as it is what used in the tutorial.

This flow-graph works well for low frequencies. As indicated in the output. However my problem starts when I increase the frequency. As per my knowledge, a sampling rate of 32k is sufficient to sample a signal of maximum frequency of 16k. Hence, I am confused as to why my output is distorted.

## Accepted answer (score 10, by Marcus Müller)

Your confusion stems from the fact that your mind (and the WX GUI scope sink) uses linear interpolation between the samples.

That's not right – in your case, where the signal period isn't an integer number of samples, this becomes obvious by the fact that things don't look very sinusoidal. They still are (I promise ;) ).

Think about it like this: at exactly 16 kHz sampled with 32 kHz, you'd get 2 samples per period, right? So, if these samples happen to lie on the extrema of the cosine, you'd get $[+1\, -1\, +1\, -1\, \ldots]$.

With 13.7 kHz not that far away from that, you "mostly" get alternating signs, too, but every so and so many samples, you still "hit" the same upper or lower half of a cosine twice. That's why things **look** irregular.

Things are in perfect, nice shape! I've made a quick Jupyter Notebook to illustrate. If you don't have the time to read it, here's the takeaway:

What you need to do, mentally, is interpolate using a $\mathrm{sinc}$ function as interpolator. (I did that in the improved version of the notebook with the bigger pictures in the last part.)

The whole point is that although it might not look like it, these "jagged" samples of a 13.7 kHz oscillation still **are** 100% that oscillation, and contain all the info the continuous signal had. Neat!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9471/sine-signal-distorted-in-gnu-radio, by Denis, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
