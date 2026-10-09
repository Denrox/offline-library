# What is meant by "poles" when discussing filters?

*Tags: receiver, filter · score 10*

## Question

I was looking over the product page for the K3 (dreaming I know) and noticed that they offer a variety of crystal filters. Some are 5-pole and some are 8-pole, other than price, what is the difference and what is meant by "pole" in this context?

## Answer (score 8, by Phil Frost - W8II)

"Pole" comes from the Laplace transform, or it's discrete (for digital filters) equivalent, the Z-transform. Without delving into the mathematics of it, these transforms enable a filter designer to express the response of a filter in terms of some number of *poles* and *zeros* on the complex plane.

Using these transforms simplifies many tasks of the filter designer, such as guaranteeing stability, or designing a filter to optimize some aspect such as minimum group delay, minimal overshoot, steepest roll-off, etc. There are many common filter designs, such as Butterworth or elliptic, which cover common goals, and these are usually described in terms of poles and zeros.

The practical application for the ham is this: the more poles or zeros a filter has, or the higher the filter's *order*, the steeper the roll-off can be. An an example, here's the frequency response for a number of Butterworth low-pass filters with different numbers of poles:

The numbers by the lines, 1 through 5, denote the order of the filter. For a Butterworth filter, the order is also equal to the number of poles. As we add more poles, the roll-off becomes steeper. Again just for Butterworth filters, the roll-off is 6dB/octave for each pole, so a 6-pole filter would have a roll-off of 36dB/octave, and an 8-pole filter would be 48dB/octave. Other filter designs can achieve a steeper roll-off at the expense of some other property, such as ripple.

The number of poles and zeros is also the minimum number of reactive components (capacitors, inductors) that would be required to implement the filter. So, more poles and zeros means more components, and more cost.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1504/what-is-meant-by-poles-when-discussing-filters, by WPrecht, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
