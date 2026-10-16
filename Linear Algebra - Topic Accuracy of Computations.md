# Topic: Accuracy of Computations

Gauss' method lends itself nicely to computerization. The code below illustrates. It operates on an $$n \! \times \! n$$ matrix a, pivoting with the first row, then with the second row, etc.

```
for (pivot_row = 1; pivot_row <= n - 1; pivot_row++) {
for (row_below = pivot_row + 1; row_below <= n; row_below++) {
multiplier = a[row_below, pivot_row] / a[pivot_row, pivot_row];
for (col = pivot_row; col <= n; col++) {
a[row_below, col] -= multiplier * a[pivot_row, col];
}
}
}

```

(This code is in the C language. Here is a brief translation. The loop construct for (pivot_row = 1; pivot_row <= n - 1; pivot_row++) { ... } sets pivot_row to 1 and then iterates while pivot_row is less than or equal to $$n-1$$, each time through incrementing pivot_row by one with the "++" operation. The other non-obvious construct is that the "-=" in the innermost loop amounts to the a[row_below, col] =- multiplier * a[pivot_row, col] + a[row_below, col]} operation.)

While this code provides a quick take on how Gauss' method can be mechanized, it is not ready to use. It is naive in many ways. The most glaring way is that it assumes that a nonzero number is always found in the pivot_row, pivot_row position for use as the pivot entry. To make it practical, one way in which this code needs to be reworked is to cover the case where finding a zero in that location leads to a row swap, or to the conclusion that the matrix is singular.

Adding some if$$\cdots$$ statements to cover those cases is not hard, but we will instead consider some more subtle ways in which the code is naive. There are pitfalls arising from the computer's reliance on finite-precision floating point arithmetic.

For example, we have seen above that we must handle as a separate case a system that is singular. But systems that are nearly singular also require care. Consider this one.

$$
\begin{array}{rcrcr} x &+ &2y &= &3 \\ 1.000\,000\,01x &+ &2y &= &3.000\,000\,01 \end{array}
$$

By eye we get the solution $$x=1$$ and $$y=1$$. But a computer has more trouble. A computer that represents real numbers to eight significant places (as is common, usually called **single precision**) will represent the second equation internally as $$1.000\,000\,0x+2y=3.000\,000\,0$$, losing the digits in the ninth place. Instead of reporting the correct solution, this computer will report something that is not even close— this computer thinks that the system is singular because the two equations are represented internally as equal.

For some intuition about how the computer could come up with something that far off, we can graph the system.

At the scale of this graph, the two lines cannot be resolved apart. This system is nearly singular in the sense that the two lines are nearly the same line. Near-singularity gives this system the property that a small change in the system can cause a large change in its solution; for instance, changing the $$3.000\,000\,01$$ to $$3.000\,000\,03$$ changes the intersection point from $$(1,1)$$ to $$(3,0)$$. This system changes radically depending on a ninth digit, which explains why the eight-place computer has trouble. A problem that is very sensitive to inaccuracy or uncertainties in the input values is **ill-conditioned**.

The above example gives one way in which a system can be difficult to solve on a computer. It has the advantage that the picture of nearly-equal lines gives a memorable insight into one way that numerical difficulties can arise. Unfortunately this insight isn't very useful when we wish to solve some large system. We cannot, typically, hope to understand the geometry of an arbitrary large system. In addition, there are ways that a computer's results may be unreliable other than that the angle between some of the linear surfaces is quite small.

For an example, consider the system below, from (Hamming 1971).

$$
\begin{array}{rcrcr} 0.001x &+ &y &= &1 \\ x &- &y &= &0 \end{array} \qquad(*)
$$

The second equation gives $$x=y$$, so $$x=y=1/1.001$$ and thus both variables have values that are just less than $$1$$. A computer using two digits represents the system internally in this way (we will do this example in two-digit floating point arithmetic, but a similar one with eight digits is easy to invent).

$$
\begin{array}{rcrcr} (1.0\times 10^{-3})x &+ &(1.0\times 10^{0})y &= &1.0\times 10^{0} \\ (1.0\times 10^{0})x &- &(1.0\times 10^{0})y &= &0.0\times 10^{0} \end{array}
$$

The computer's row reduction step $$-1000\rho_1+\rho_2$$ produces a second equation $$-1001y=-999$$, which the computer rounds to two places as $$(-1.0\times 10^{3})y=-1.0\times 10^{3}$$. Then the computer decides from the second equation that $$y=1$$ and from the first equation that $$x=0$$. This $$y$$ value is fairly good, but the $$x$$ is quite bad. Thus, another cause of unreliable output is a mixture of floating point arithmetic and a reliance on pivots that are small.

An experienced programmer may respond that we should go to **double precision** where sixteen significant digits are retained. This will indeed solve many problems. However, there are some difficulties with it as a general approach. For one thing, double precision takes longer than single precision (on a '486 chip, multiplication takes eleven ticks in single precision but fourteen in double precision (Microsoft 1993)) and has twice the memory requirements. So attempting to do all calculations in double precision is just not practical. And besides, the above systems can obviously be tweaked to give the same trouble in the seventeenth digit, so double precision won't fix all problems. What we need is a strategy to minimize the numerical trouble arising from solving systems on a computer, and some guidance as to how far the reported solutions can be trusted.

Mathematicians have made a careful study of how to get the most reliable results. A basic improvement on the naive code above is to not simply take the entry in the *pivot_row*, *pivot_row* position for the pivot, but rather to look at all of the entries in the *pivot_row* column below the *pivot_row* row, and take the one that is most likely to give reliable results (e.g., take one that is not too small). This strategy is **partial pivoting**. For example, to solve the troublesome system ($$*$$) above, we start by looking at both equations for a best first pivot, and taking the $$1$$ in the second equation as more likely to give good results. Then, the pivot step of $$-.001\rho_2+\rho_1$$ gives a first equation of $$1.001y=1$$, which the computer will represent as $$(1.0\times 10^{0})y=1.0\times 10^{0}$$, leading to the conclusion that $$y=1$$ and, after back-substitution, $$x=1$$, both of which are close to right. The code from above can be adapted to this purpose.

```
for (pivot_row = 1; pivot_row <= n - 1; pivot_row++) {
/* Find the largest pivot in this column (in row max). */
max = pivot_row;
for (row_below = pivot_row + 1; pivot_row <= n; row_below++) {
if (abs(a[row_below, pivot_row]) > abs(a[max, row_below]))
max = row_below;
}

/* Swap rows to move that pivot entry up. */
for (col = pivot_row; col <= n; col++) {
temp = a[pivot_row, col];
a[pivot_row, col] = a[max, col];
a[max, col] = temp;
}

/* Proceed as before. */
for (row_below = pivot_row + 1; row_below <= n; row_below++) {
multiplier = a[row_below, pivot_row] / a[pivot_row, pivot_row];
for (col = pivot_row; col <= n; col++) {
a[row_below, col] -= multiplier * a[pivot_row, col];
}
}
}

```

A full analysis of the best way to implement Gauss' method is outside the scope of the book (see (Wilkinson 1965)), but the method recommended by most experts is a variation on the code above that first finds the best pivot among the candidates, and then scales it to a number that is less likely to give trouble. This is **scaled partial pivoting**.

In addition to returning a result that is likely to be reliable, most well-done code will return a number, called the **condition number** that describes the factor by which uncertainties in the input numbers could be magnified to become inaccuracies in the results returned (see (Rice 1993)).

The lesson of this discussion is that just because Gauss' method always works in theory, and just because computer code correctly implements that method, and just because the answer appears on green-bar paper, doesn't mean that the answer is reliable. In practice, always use a package where experts have worked hard to counter what can go wrong.

### Exercises

**Problem 1**  —

Using two decimal places, add $$253$$ and $$2/3$$.

**Problem 2**  —

This intersect-the-lines problem contrasts with the example discussed above.

$$
\displaystyle \begin{array}{rcrcr} x &+ &2y &= &3 \\ 3x &- &2y &= &1 \end{array}
$$

Illustrate that in this system some small change in the numbers will produce only a small change in the solution by changing the constant in the bottom equation to $$1.008$$ and solving. Compare it to the solution of the unchanged system.

**Problem 3**  —

Solve this system by hand (Rice 1993).

$$
\begin{array}{rcrcr} 0.000\,3x &+ &1.556y &= &1.569 \\ 0.345\,4x &- &2.346y &= &1.018 \end{array}
$$

1. Solve it accurately, by hand.
2. Solve it by rounding at each step to four significant digits.

**Problem 4**  —

Rounding inside the computer often has an effect on the result. Assume that your machine has eight significant digits.

1. Show that the machine will compute $$(2/3)+((2/3)-(1/3))$$ as unequal to $$((2/3)+(2/3))-(1/3)$$. Thus, computer arithmetic is not associative.
2. Compare the computer's version of $$(1/3)x+y=0$$ and $$(2/3)x+2y=0$$. Is twice the first equation the same as the second?

**Problem 5**  —

Ill-conditioning is not only dependent on the matrix of coefficients. This example (Hamming 1971) shows that it can arise from an interaction between the left and right sides of the system. Let $$\varepsilon$$ be a small real.

$$
\begin{array}{rcrcrcr} 3x &+ &2y &+ &z &= &6 \\ 2x &+ &2\varepsilon y &+ &2\varepsilon z &= &2+4\varepsilon \\ x &+ &2\varepsilon y &- &\varepsilon z &= &1+\varepsilon \end{array}
$$

1. Solve the system by hand. Notice that the $$\varepsilon$$'s divide out only because there is an exact cancelation of the integer parts on the right side as well as on the left.
2. Solve the system by hand, rounding to two decimal places, and with $$\varepsilon=0.001$$.

Solutions

### References

- Hamming, Richard W. (1971), *Introduction to Applied Numerical Analysis*, Hemisphere Publishing.
- Rice, John R. (1993), *Numerical Methods, Software, and Analysis*, Academic Press.
- Wilkinson, J. H. (1965), *The Algebraic Eigenvalue Problem*, Oxford University Press.
- Microsoft (1993), *Microsoft Programmers Reference*, Microsoft Press.

---

*Source: Wikibooks, Linear Algebra/Topic: Accuracy of Computations (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Accuracy_of_Computations), by Wikibooks contributors, CC BY-SA 4.0.*
