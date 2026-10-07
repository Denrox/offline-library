# Complex Representations

Recall the definitions of the complex number addition

$$
(a+bi)\,+\,(c+di)=(a+c)+(b+d)i
$$

and multiplication.

$$
\begin{array}{rl} (a+bi)(c+di) &=ac+adi+bci+bd(-1) \\ &=(ac-bd)+(ad+bc)i \end{array}
$$

**Example 2.1**  —

For instance, $$(1-2i)\,+\,(5+4i)=6+2i$$ and $$(2-3i)(4-0.5i)=6.5-13i$$.

Handling scalar operations with those rules, all of the operations that we've covered for real vector spaces carry over unchanged.

**Example 2.2**  —

Matrix multiplication is the same, although the scalar arithmetic involves more bookkeeping.

$$
\begin{pmatrix} 1+1i &2-0i \\ i &-2+3i \end{pmatrix} \begin{pmatrix} 1+0i &1-0i \\ 3i &-i \end{pmatrix}
$$

$$
\begin{align} &=\begin{pmatrix} (1+1i)\cdot(1+0i)+(2-0i)\cdot(3i) &(1+1i)\cdot(1-0i)+(2-0i)\cdot(-i) \\ (i)\cdot(1+0i)+(-2+3i)\cdot(3i) &(i)\cdot(1-0i)+(-2+3i)\cdot(-i) \end{pmatrix} \\ &=\begin{pmatrix} 1+7i &1-1i \\ -9-5i &3+3i \end{pmatrix} \end{align}
$$

Everything else from prior chapters that we can, we shall also carry over unchanged. For instance, we shall call the ordered set of vectors

$$
\left\langle \begin{pmatrix} 1+0i \\ 0+0i \\ \vdots \\ 0+0i \end{pmatrix}, \begin{pmatrix} 0+0i \\ 1+0i \\ \vdots \\ 0+0i \end{pmatrix}, \dots, \begin{pmatrix} 0+0i \\ 0+0i \\ \vdots \\ 1+0i \end{pmatrix} \right\rangle
$$

the **standard basis** for $$\mathbb{C}^n$$ as a vector space over $$\mathbb{C}$$ and again denote it $$\mathcal{E}_n$$.

---

*Source: Wikibooks, Linear Algebra/Complex Representations (https://en.wikibooks.org/wiki/Linear_Algebra/Complex_Representations), by Wikibooks contributors, CC BY-SA 4.0.*
