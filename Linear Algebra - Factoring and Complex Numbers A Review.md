# Factoring and Complex Numbers: A Review

*This subsection is a review only and we take the main results as known. For proofs, see (Birkhoff & MacLane 1965) or (Ebbinghaus 1990).*

Just as integers have a division operation— e.g., "$$4$$ goes $$5$$ times into $$21$$ with remainder $$1$$"— so do polynomials.

**Theorem 1.1 (Division Theorem for Polynomials)**  —

Let $$c(x)$$ be a polynomial. If $$m(x)$$ is a non-zero polynomial then there are **quotient** and **remainder** polynomials $$q(x)$$ and $$r(x)$$ such that

$$
c(x)=m(x)\cdot q(x)+r(x)
$$

where the degree of $$r(x)$$ is strictly less than the degree of $$m(x)$$.

In this book constant polynomials, including the zero polynomial, are said to have degree $$0$$. (This is not the standard definition, but it is convienent here.)

The point of the integer division statement "$$4$$ goes $$5$$ times into $$21$$ with remainder $$1$$" is that the remainder is less than $$4$$— while $$4$$ goes $$5$$ times, it does not go $$6$$ times. In the same way, the point of the polynomial division statement is its final clause.

**Example 1.2**  —

If $$c(x)=2x^3-3x^2+4x$$ and $$m(x)=x^2+1$$ then $$q(x)=2x-3$$ and $$r(x)=2x+3$$. Note that $$r(x)$$ has a lower degree than $$m(x)$$.

**Corollary 1.3**  —

The remainder when $$c(x)$$ is divided by $$x-\lambda$$ is the constant polynomial $$r(x)=c(\lambda)$$.

**Proof**  —

The remainder must be a constant polynomial because it is of degree less than the divisor $$x-\lambda$$, To determine the constant, take $$m(x)$$ from the theorem to be $$x-\lambda$$ and substitute $$\lambda$$ for $$x$$ to get $$c(\lambda)=(\lambda-\lambda)\cdot q(\lambda)+r(x)$$.

If a divisor $$m(x)$$ goes into a dividend $$c(x)$$ evenly, meaning that $$r(x)$$ is the zero polynomial, then $$m(x)$$ is a **factor** of $$c(x)$$. Any **root** of the factor (any $$\lambda\in\mathbb{R}$$ such that $$m(\lambda)=0$$) is a root of $$c(x)$$ since $$c(\lambda)=m(\lambda)\cdot q(\lambda)=0$$. The prior corollary immediately yields the following converse.

**Corollary 1.4**  —

If $$\lambda$$ is a root of the polynomial $$c(x)$$ then $$x-\lambda$$ divides $$c(x)$$ evenly, that is, $$x-\lambda$$ is a factor of $$c(x)$$.

Finding the roots and factors of a high-degree polynomial can be hard. But for second-degree polynomials we have the quadratic formula: the roots of $$ax^2+bx+c$$ are

$$
\lambda_1=\frac{-b+\sqrt{b^2-4ac}}{2a} \qquad \lambda_2=\frac{-b-\sqrt{b^2-4ac}}{2a}
$$

(if the discriminant $$b^2-4ac$$ is negative then the polynomial has no real number roots). A polynomial that cannot be factored into two lower-degree polynomials with real number coefficients is **irreducible over the reals**.

**Theorem 1.5**  —

Any constant or linear polynomial is irreducible over the reals. A quadratic polynomial is irreducible over the reals if and only if its discriminant is negative. No cubic or higher-degree polynomial is irreducible over the reals.

**Corollary 1.6**  —

Any polynomial with real coefficients can be factored into linear and irreducible quadratic polynomials. That factorization is unique; any two factorizations have the same powers of the same factors.

Note the analogy with the prime factorization of integers. In both cases, the uniqueness clause is very useful.

**Example 1.7**  —

Because of uniqueness we know, without multiplying them out, that $$(x+3)^2(x^2+1)^3$$ does not equal $$(x+3)^4(x^2+x+1)^2$$.

**Example 1.8**  —

By uniqueness, if $$c(x)=m(x)\cdot q(x)$$ then where $$c(x)=(x-3)^2(x+2)^3$$ and $$m(x)=(x-3)(x+2)^2$$, we know that $$q(x)=(x-3)(x+2)$$.

While $$x^2+1$$ has no real roots and so doesn't factor over the real numbers, if we imagine a root— traditionally denoted $$i$$ so that $$i^2+1=0$$— then $$x^2+1$$ factors into a product of linears $$(x-i)(x+i)$$.

So we adjoin this root $$i$$ to the reals and close the new system with respect to addition, multiplication, etc. (i.e., we also add $$3+i$$, and $$2i$$, and $$3+2i$$, etc., putting in all linear combinations of $$1$$ and $$i$$). We then get a new structure, the **complex numbers**, denoted $$\mathbb{C}$$.

In $$\mathbb{C}$$ we can factor (obviously, at least some) quadratics that would be irreducible if we were to stick to the real numbers. Surprisingly, in $$\mathbb{C}$$ we can not only factor $$x^2+1$$ and its close relatives, we can factor any quadratic.

$$
ax^2+bx+c= a\cdot \big(x-\frac{-b+\sqrt{b^2-4ac}}{2a}\big) \cdot \big(x-\frac{-b-\sqrt{b^2-4ac}}{2a}\big)
$$

**Example 1.9**  —

The second degree polynomial $$x^2+x+1$$ factors over the complex numbers into the product of two first degree polynomials.

$$
\big(x-\frac{-1+\sqrt{-3}}{2}\big) \big(x-\frac{-1-\sqrt{-3}}{2}\big) = \big(x-(-\frac{1}{2}+\frac{\sqrt{3}}{2}i)\big) \big(x-(-\frac{1}{2}-\frac{\sqrt{3}}{2}i)\big)
$$

**Corollary 1.10 (Fundamental Theorem of Algebra)**  —

Polynomials with complex coefficients factor into linear polynomials with complex coefficients. The factorization is unique.

### References

- Ebbinghaus, H. D. (1990), *Numbers*, Springer-Verlag.
- Birkhoff, Garrett; MacLane, Saunders (1965), *Survey of Modern Algebra* (Third ed.), Macmillian.

---

*Source: Wikibooks, Linear Algebra/Factoring and Complex Numbers: A Review (https://en.wikibooks.org/wiki/Linear_Algebra/Factoring_and_Complex_Numbers%3A_A_Review), by Wikibooks contributors, CC BY-SA 4.0.*
