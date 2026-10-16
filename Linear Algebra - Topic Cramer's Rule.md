# Topic: Cramer's Rule

We have introduced determinant functions algebraically by looking for a formula to decide whether a matrix is nonsingular. After that introduction we saw a geometric interpretation, that the determinant function gives the size of the box with sides formed by the columns of the matrix. This Topic makes a connection between the two views.

First, a linear system

$$
\begin{array}{rcrcr} x_1 &+ &2x_2 &= &6 \\ 3x_1 &+ &x_2 &= &8 \end{array}
$$

is equivalent to a linear relationship among vectors.

$$
x_1\cdot\begin{pmatrix} 1 \\ 3 \end{pmatrix}+x_2\cdot\begin{pmatrix} 2 \\ 1 \end{pmatrix}=\begin{pmatrix} 6 \\ 8 \end{pmatrix}
$$

The picture below shows a parallelogram with sides formed from $$\binom{1}{3}$$ and $$\binom{2}{1}$$ nested inside a parallelogram with sides formed from $$x_1\binom{1}{3}$$ and $$x_2\binom{2}{1}$$.

So even without determinants we can state the algebraic issue that opened this book, finding the solution of a linear system, in geometric terms: by what factors $$x_1$$ and $$x_2$$ must we dilate the vectors to expand the small parallegram to fill the larger one?

However, by employing the geometric significance of determinants we can get something that is not just a restatement, but also gives us a new insight and sometimes allows us to compute answers quickly. Compare the sizes of these shaded boxes.

The second is formed from $$x_1\binom{1}{3}$$ and $$\binom{2}{1}$$, and one of the properties of the size function— the determinant— is that its size is therefore $$x_1$$ times the size of the first box. Since the third box is formed from $$x_1\binom{1}{3}+x_2\binom{2}{1}=\binom{6}{8}$$ and $$\binom{2}{1}$$, and the determinant is unchanged by adding $$x_2$$ times the second column to the first column, the size of the third box equals that of the second. We have this.

$$
\begin{vmatrix} 6 &2 \\ 8 &1 \end{vmatrix} = \begin{vmatrix} x_1\cdot 1 &2 \\ x_1\cdot 3 &1 \end{vmatrix} = x_1\cdot \begin{vmatrix} 1 &2 \\ 3 &1 \end{vmatrix}
$$

Solving gives the value of one of the variables.

$$
x_1= \frac{\begin{vmatrix} 6 &2 \\ 8 &1 \end{vmatrix} }{ \begin{vmatrix} 1 &2 \\ 3 &1 \end{vmatrix} } =\frac{-10}{-5}=2
$$

The theorem that generalizes this example, **Cramer's Rule**, is: if $$\left|A\right|\neq 0$$ then the system $$A\vec{x}=\vec{b}$$ has the unique solution $$x_i=\left|B_i\right|/\left|A\right|$$ where the matrix $$B_i$$ is formed from $$A$$ by replacing column $$i$$ with the vector $$\vec{b}$$. Problem 3 asks for a proof.

For instance, to solve this system for $$x_2$$

$$
\begin{pmatrix} 1 &0 &4 \\ 2 &1 &-1 \\ 1 &0 &1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} =\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}
$$

we do this computation.

$$
x_2= \frac{ \begin{vmatrix} 1 &2 &4 \\ 2 &1 &-1 \\ 1 &-1 &1 \end{vmatrix} }{ \begin{vmatrix} 1 &0 &4 \\ 2 &1 &-1 \\ 1 &0 &1 \end{vmatrix} } =\frac{-18}{-3}
$$

Cramer's Rule allows us to solve many two equations/two unknowns systems by eye. It is also sometimes used for three equations/three unknowns systems. But computing large determinants takes a long time, so solving large systems by Cramer's Rule is not practical.

### Exercises

**Problem 1**  —

Use Cramer's Rule to solve each for each of the variables.

1. $$\begin{array}{rcrcr} x &- &y &= &4 \\ -x &+ &2y &= &-7 \end{array}$$
2. $$\begin{array}{rcrcr} -2x &+ &y &= &-2 \\ x &- &2y &= &-2 \end{array}$$

**Problem 2**  —

Use Cramer's Rule to solve this system for $$z$$.

$$
\begin{array}{rcrcrcrcr} 2x &+ &y &+ &z &= &1 \\ 3x & & &+ &z &= &4 \\ x &- &y &- &z &= &2 \end{array}
$$

**Problem 3**  —

Prove Cramer's Rule.

**Problem 4**  —

Suppose that a linear system has as many equations as unknowns, that all of its coefficients and constants are integers, and that its matrix of coefficients has determinant $$1$$. Prove that the entries in the solution are all integers. (*Remark.* This is often used to invent linear systems for exercises. If an instructor makes the linear system with this property then the solution is not some disagreeable fraction.)

**Problem 5**  —

Use Cramer's Rule to give a formula for the solution of a two equations/two unknowns linear system.

**Problem 6**  —

Can Cramer's Rule tell the difference between a system with no solutions and one with infinitely many?

**Problem 7**  —

The first picture in this Topic (the one that doesn't use determinants) shows a unique solution case. Produce a similar picture for the case of infintely many solutions, and the case of no solutions.

Solutions

---

*Source: Wikibooks, Linear Algebra/Topic: Cramer's Rule (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Cramer%27s_Rule), by Wikibooks contributors, CC BY-SA 4.0.*
