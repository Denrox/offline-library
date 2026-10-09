# How to find the front-to-back ratio given an antenna radiation pattern diagram?

*Tags: antenna, math · score 6*

## Question

I know that the front-to-back ratio is 18dB in the below antenna radiation pattern diagram, but I don't know how to read the diagram to obtain this result. How does one read and understand such diagrams?

## Accepted answer (score 10, by Amber)

The diagram is a polar plot where 0 degrees (the 0 on the right-hand edge) corresponds to the front of the antenna and 180 degrees corresponds to the back.

Within the diagram, a logarithmic scale is utilized to represent radiation strength. This is in addition to the fact that the Decibel is a logarithmic unit. (The diagram really should explicitly list its units, but for the application of antenna radition, the unit is typically dB.) You can tell that a logarithmic scale is in use by observing that the distance between the $-6$ and $-12$ lines is the same as that between the $-12$ and $-24$ lines, so it's obviously not a linear scaling.

For the front-back ratio, we look at the values indicated on the plot for 0 and 180 degrees. In this particular instance, the value at 0 degrees is $0$, and the value at 180 degrees is approximately $-18$.

Since logarithmic scales transform division into subtraction, we calculate the ratio front to back by subtracting the logarithmic back value from that of the front.

Since $0 - (-18) = 18$, the answer is 18dB.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/267/how-to-find-the-front-to-back-ratio-given-an-antenna-radiation-pattern-diagram, by Dan, Amber. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
