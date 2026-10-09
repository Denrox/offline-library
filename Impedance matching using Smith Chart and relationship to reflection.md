# Impedance matching using Smith Chart and relationship to reflection

*Tags: impedance-matching, smith-chart · score 5*

## Question

I've been reading the impedance matching chapter of Bowick's excellent RF Circuit Design book and I have a question.

For those who haven't read this book (or have but can't remember!), the chapter discusses L and 3 element matching networks (very intuitively, I might add) with some helpful examples before moving to an introduction to the Smith Chart.

He uses some of the earlier matching examples (solved using equations) and shows how the same result can be obtained using the Smith Chart. The text points out that adding reactive elements in series with a resistor is a simple matter of adding the appropriate imaginary quantity, thus moving you along the constant resistance circle. Likewise, adding reactive elements in shunt can be achieved with the conductance form of the Smith Chart again using a simple addition or subtraction. If you use a combined impedance and conductance chart you can easily model ladder networks, which of course is exactly what you need for an L, Pi or T matching network. If you need to match one impedance to another (one would be a conjugate), you simply identify the two impedances on the chart (normalized if necessary) and track a path between the two using the rules above.

**What I don't understand is, where is the reflection coefficient in any of this?** If I understand the chart correctly, it basically maps the reflection coefficient for a normalized characteristic impedance to every possible (within reason) impedance (or conductance). In other words, the charts "meaning" is related to reflection. But, it seems to me that the kind of impedance matching operation described above is simply using the impedance(conductance) map and its ability to express complex addition and subtraction to move from one point to another and each points relationship to reflection isn't really relevant. I worry I've missed an important point here. I hope this question isn't too confusing.

## Answer (score 4, by Glenn W9IQ)

You are correct that there is a clear correlation. Perhaps your Smith chart does not have the following scales along the bottom?:

The technique is to use your compass to measure from the center of the chart to the normalized load impedance (zL). Then relocated the compass pin to the point marked "CENTER" in the above scales and read the reflection coefficient from the scale at the mark of the compass.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10558/impedance-matching-using-smith-chart-and-relationship-to-reflection, by Buck8pe, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
