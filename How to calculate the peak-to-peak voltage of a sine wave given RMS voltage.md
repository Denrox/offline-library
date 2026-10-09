# How to calculate the peak-to-peak voltage of a sine wave given RMS voltage

*Tags: rf-power, math, voltage · score 3*

## Question

How do I calculate the peak-to-peak voltage of a sine wave given RMS voltage?

## Accepted answer (score 7, by Amber)

#### The short answer:

\begin{equation} \frac{V_{p-p}}{V_{rms}} = 2\sqrt{2} \end{equation}

#### The long answer, or how to derive the above:

As noted on the Wikipedia page for root mean square, the RMS of a sine wave is equal to its amplitude divided by the square root of two. (You can also derive this by doing the integral over a sine wave yourself.)

\begin{equation} V_{rms} = \frac{a}{\sqrt{2}} \end{equation}

The peak-to-peak voltage is twice the amplitude of the wave, since it's measuring from the tip of a peak to the tip of a trough.

\begin{equation} V_{p-p} = 2a \end{equation}

We can rearrange these two equations:

\begin{equation} V_{rms} \cdot \sqrt{2} = a \end{equation} \begin{equation} V_{p-p} = 2 \cdot (V_{rms} \cdot \sqrt{2}) \end{equation} \begin{equation} V_{p-p} = V_{rms} \cdot 2\sqrt{2} \end{equation}

Thus, we multiply the RMS voltage by twice the square root of two - a factor of about 2.828 or so:

\begin{equation} 2\sqrt{2} = 2.8284271247.... \end{equation}

Of course, the process also works in reverse - if you can measure the peak-to-peak voltage, dividing that by the same factor will give you the RMS voltage assuming a perfect sine wave.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/278/how-to-calculate-the-peak-to-peak-voltage-of-a-sine-wave-given-rms-voltage, by Dan, Amber. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
