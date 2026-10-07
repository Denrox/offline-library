# Topic: Fields

Linear combinations involving only fractions or only integers are much easier for computations than combinations involving real numbers, because computing with irrational numbers is awkward. Could other number systems, like the rationals or the integers, work in the place of $$\mathbb{R}$$ in the definition of a vector space?

Yes and no. If we take "work" to mean that the results of this chapter remain true then an analysis of which properties of the reals we have used in this chapter gives the following list of conditions an algebraic system needs in order to "work" in the place of $$\mathbb{R}$$.

**Definition 1.1**  —

A **field** is a set $$\mathcal{F}$$ with two operations"$$+$$" and "$$\cdot$$" such that

1. for any $$a,b\in\mathcal{F}$$ the result of $$a+b$$ is in $$\mathcal{F}$$ and

 - $$a+b=b+a$$
 - if $$c\in\mathcal{F}$$ then $$a+(b+c)=(a+b)+c$$
2. for any $$a,b\in\mathcal{F}$$ the result of $$a\cdot b$$ is in $$\mathcal{F}$$ and

 - $$a\cdot b=b\cdot a$$
 - if $$c\in\mathcal{F}$$ then $$a\cdot (b\cdot c)=(a\cdot b)\cdot c$$
3. if $$a,b,c\in\mathcal{F}$$ then $$a\cdot (b+c)=a\cdot b+a\cdot c$$
4. there is an element $$0\in\mathcal{F}$$ such that

 - if $$a\in\mathcal{F}$$ then $$a+0=a$$
 - for each $$a\in\mathcal{F}$$ there is an element $$-a\in\mathcal{F}$$ such that $$(-a)+a=0$$
5. there is an element $$1\in\mathcal{F}$$ such that

 - if $$a\in\mathcal{F}$$ then $$a\cdot 1=a$$
 - for each element $$a\neq 0$$ of $$\mathcal{F}$$ there is an element $$a^{-1}\in\mathcal{F}$$ such that $$a^{-1}\cdot a=1$$.

The number system consisting of the set of real numbers along with the usual addition and multiplication operation is a field, naturally. Another field is the set of rational numbers with its usual addition and multiplication operations. An example of an algebraic structure that is not a field is the integer number system — it fails the final condition.

Some examples are surprising. The set $$\{0,1\}$$ under these operations:

$$
\begin{array}{c|cc} + & 0 & 1 \\ \hline 0 & 0 & 1 \\ 1 & 1 & 0 \end{array} \qquad \begin{array}{c|cc} \cdot & 0 & 1 \\ \hline 0 & 0 & 0 \\ 1 & 0 & 1 \end{array}
$$

is a field (see Problem 4).

We could develop Linear Algebra as the theory of vector spaces with scalars from an arbitrary field, instead of sticking to taking the scalars only from $$\mathbb{R}$$. In that case, almost all of the statements in this book would carry over by replacing "$$\mathbb{R}$$" with "$$\mathcal{F}$$", and thus by taking coefficients, vector entries, and matrix entries to be elements of $$\mathcal{F}$$ ("almost" because statements involving distances or angles are exceptions). Here are some examples; each applies to a vector space $$V$$ over a field $$\mathcal{F}$$.

- For any $$\vec{v}\in V$$ and $$a\in\mathcal{F}$$,

 1. $$0\cdot\vec{v}=\vec{0}$$, and
 2. $$-1\cdot\vec{v}+\vec{v}=\vec{0}$$, and
 3. $$a\cdot\vec{0}=\vec{0}$$.
- The span (the set of linear combinations) of a subset of $$V$$ is a subspace of $$V$$.
- Any subset of a linearly independent set is also linearly independent.
- In a finite-dimensional vector space, any two bases have the same number of elements.

(Even statements that don't explicitly mention $$\mathcal{F}$$ use field properties in their proof.)

We won't develop vector spaces in this more general setting because the additional abstraction can be a distraction. The ideas we want to bring out already appear when we stick to the reals.

The only exception is in Chapter Five. In that chapter we must factor polynomials, so we will switch to considering vector spaces over the field of complex numbers. We will discuss this more, including a brief review of complex arithmetic, when we get there.

### Exercises

**Problem 1**  —

Show that the real numbers form a field.

**Problem 2**  —

Prove that these are fields.

1. The rational numbers $$\mathbb{Q}$$
2. The complex numbers $$\mathbb{C}$$

**Problem 3**  —

Give an example that shows that the integer number system is not a field.

**Problem 4**  —

Consider the set $$\{0,1\}$$ subject to the operations given above. Show that it is a field.

**Problem 5**  —

Give suitable operations to make the set $$\{0,1,2\}$$ a field.

Solutions

---

*Source: Wikibooks, Linear Algebra/Topic: Fields (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Fields), by Wikibooks contributors, CC BY-SA 4.0.*
