# Determinants Exist

*This subsection is optional. It consists of proofs of two results from the prior subsection. These proofs involve the properties of permutations, which will not be used later, except in the optional Jordan Canonical Form subsection.*

The prior subsection attacks the problem of showing that for any size there is a determinant function on the set of square matrices of that size by using multilinearity to develop the permutation expansion.

$$
\begin{array}{rl} \begin{vmatrix} t_{1,1} &t_{1,2} &\ldots &t_{1,n} \\ t_{2,1} &t_{2,2} &\ldots &t_{2,n} \\ &\vdots \\ t_{n,1} &t_{n,2} &\ldots &t_{n,n} \end{vmatrix} &= \begin{array}{l} t_{1,\phi_1(1)}t_{2,\phi_1(2)}\cdots t_{n,\phi_1(n)}\left|P_{\phi_1}\right| \\ \quad+t_{1,\phi_2(1)}t_{2,\phi_2(2)}\cdots t_{n,\phi_2(n)}\left|P_{\phi_2}\right| \\ \quad\vdots \\ \quad+t_{1,\phi_k(1)}t_{2,\phi_k(2)}\cdots t_{n,\phi_k(n)}\left|P_{\phi_k}\right| \end{array} \\ &=\displaystyle\sum_{\text{permutations }\phi} t_{1,\phi(1)}t_{2,\phi(2)}\cdots t_{n,\phi(n)} \left|P_{\phi}\right| \end{array}
$$

This reduces the problem to showing that there is a determinant function on the set of permutation matrices of that size.

Of course, a permutation matrix can be row-swapped to the identity matrix and to calculate its determinant we can keep track of the number of row swaps. However, the problem is still not solved. We still have not shown that the result is well-defined. For instance, the determinant of

$$
P_{\phi}= \begin{pmatrix} 0 &1 &0 &0 \\ 1 &0 &0 &0 \\ 0 &0 &1 &0 \\ 0 &0 &0 &1 \end{pmatrix}
$$

could be computed with one swap

$$
P_{\phi} \xrightarrow[]{\rho_1\leftrightarrow\rho_2} \begin{pmatrix} 1 &0 &0 &0 \\ 0 &1 &0 &0 \\ 0 &0 &1 &0 \\ 0 &0 &0 &1 \end{pmatrix}
$$

or with three.

$$
P_{\phi} \xrightarrow[]{\rho_3\leftrightarrow\rho_1} \begin{pmatrix} 0 &0 &1 &0 \\ 1 &0 &0 &0 \\ 0 &1 &0 &0 \\ 0 &0 &0 &1 \end{pmatrix} \xrightarrow[]{\rho_2\leftrightarrow\rho_3} \begin{pmatrix} 0 &0 &1 &0 \\ 0 &1 &0 &0 \\ 1 &0 &0 &0 \\ 0 &0 &0 &1 \end{pmatrix} \xrightarrow[]{\rho_1\leftrightarrow\rho_3} \begin{pmatrix} 1 &0 &0 &0 \\ 0 &1 &0 &0 \\ 0 &0 &1 &0 \\ 0 &0 &0 &1 \end{pmatrix}
$$

Both reductions have an odd number of swaps so we figure that $$\left|P_{\phi}\right|=-1$$ but how do we know that there isn't some way to do it with an even number of swaps? Corollary 4.6 below proves that there is no permutation matrix that can be row-swapped to an identity matrix in two ways, one with an even number of swaps and the other with an odd number of swaps.

**Definition 4.1**  —

Two rows of a permutation matrix

$$
\begin{pmatrix} \vdots \\ \iota_{k} \\ \vdots \\ \iota_{j} \\ \vdots \end{pmatrix}
$$

such that $$k>j$$ are in an **inversion** of their natural order.

**Example 4.2**  —

This permutation matrix

$$
\begin{pmatrix} \iota_3 \\ \iota_2 \\ \iota_1 \end{pmatrix} = \begin{pmatrix} 0 &0 &1 \\ 0 &1 &0 \\ 1 &0 &0 \end{pmatrix}
$$

has three inversions: $$\iota_3$$ precedes $$\iota_1$$, $$\iota_3$$ precedes $$\iota_2$$, and $$\iota_2$$ precedes $$\iota_1$$.

**Lemma 4.3**  —

A row-swap in a permutation matrix changes the number of inversions from even to odd, or from odd to even.

**Proof**  —

Consider a swap of rows $$j$$ and $$k$$, where $$k>j$$. If the two rows are adjacent

$$
P_{\phi}= \begin{pmatrix} \vdots \\ \iota_{\phi(j)} \\ \iota_{\phi(k)} \\ \vdots \end{pmatrix} \xrightarrow[]{\rho_k\leftrightarrow\rho_j} \begin{pmatrix} \vdots \\ \iota_{\phi(k)} \\ \iota_{\phi(j)} \\ \vdots \end{pmatrix}
$$

then the swap changes the total number of inversions by one — either removing or producing one inversion, depending on whether $$\phi(j)>\phi(k)$$ or not, since inversions involving rows not in this pair are not affected. Consequently, the total number of inversions changes from odd to even or from even to odd.

If the rows are not adjacent then they can be swapped via a sequence of adjacent swaps, first bringing row $$k$$ up

$$
\begin{pmatrix} \vdots \\ \iota_{\phi(j)} \\ \iota_{\phi(j+1)} \\ \iota_{\phi(j+2)} \\ \vdots \\ \iota_{\phi(k)} \\ \vdots \end{pmatrix} \xrightarrow[]{\rho_k\leftrightarrow\rho_{k-1}}\;\; \xrightarrow[]{\rho_{k-1}\leftrightarrow\rho_{k-2}} \dots \xrightarrow[]{\rho_{j+1}\leftrightarrow\rho_j} \begin{pmatrix} \vdots \\ \iota_{\phi(k)} \\ \iota_{\phi(j)} \\ \iota_{\phi(j+1)} \\ \vdots \\ \iota_{\phi(k-1)} \\ \vdots \end{pmatrix}
$$

and then bringing row $$j$$ down.

$$
\xrightarrow[]{\rho_{j+1}\leftrightarrow\rho_{j+2}}\;\; \xrightarrow[]{\rho_{j+2}\leftrightarrow\rho_{j+3}} \dots \xrightarrow[]{\rho_{k-1}\leftrightarrow\rho_k} \begin{pmatrix} \vdots \\ \iota_{\phi(k)} \\ \iota_{\phi(j+1)} \\ \iota_{\phi(j+2)} \\ \vdots \\ \iota_{\phi(j)} \\ \vdots \end{pmatrix}
$$

Each of these adjacent swaps changes the number of inversions from odd to even or from even to odd. There are an odd number $$(k-j)+(k-j-1)$$ of them. The total change in the number of inversions is from even to odd or from odd to even.

**Definition 4.4**  —

The **signum** of a permutation $$\operatorname{sgn}(\phi)$$ is $$+1$$ if the number of inversions in $$P_\phi$$ is even, and is $$-1$$ if the number of inversions is odd.

**Example 4.5**  —

With the subscripts from [Example 3.8](Linear%20Algebra%20-%20The%20Permutation%20Expansion.md) for the $$3$$-permutations, $$\operatorname{sgn}(\phi_1)=1$$ while $$\operatorname{sgn}(\phi_2)=-1$$.

**Corollary 4.6**  —

If a permutation matrix has an odd number of inversions then swapping it to the identity takes an odd number of swaps. If it has an even number of inversions then swapping to the identity takes an even number of swaps.

**Proof**  —

The identity matrix has zero inversions. To change an odd number to zero requires an odd number of swaps, and to change an even number to zero requires an even number of swaps.

We still have not shown that the permutation expansion is well-defined because we have not considered row operations on permutation matrices other than row swaps. We will finesse this problem: we will define a function $$d:\mathcal{M}_{n \! \times \! n}\to \mathbb{R}$$ by altering the permutation expansion formula, replacing $$\left|P_\phi\right|$$ with $$\operatorname{sgn}(\phi)$$

$$
d(T)= \sum_{\text{permutations }\phi}t_{1,\phi(1)}t_{2,\phi(2)}\dots t_{n,\phi(n)} \operatorname{sgn}(\phi)
$$

(this gives the same value as the permutation expansion because the prior result shows that $$\det(P_\phi)=\operatorname{sgn}(\phi)$$). This formula's advantage is that the number of inversions is clearly well-defined — just count them. Therefore, we will show that a determinant function exists for all sizes by showing that $$d$$ is it, that is, that $$d$$ satisfies the four conditions.

**Lemma 4.7**  —

The function $$d$$ is a determinant. Hence determinants exist for every $$n$$.

**Proof**  —

We'll must check that it has the four properties from the definition.

Property (4) is easy; in

$$
d(I)= \sum_{\text{perms }\phi} \iota_{1,\phi(1)}\iota_{2,\phi(2)}\cdots \iota_{n,\phi(n)} \operatorname{sgn}(\phi)
$$

all of the summands are zero except for the product down the diagonal, which is one.

For property (3) consider $$d(\hat{T})$$ where $$T[b]{\xrightarrow[]{k\rho_i}}\hat{T}$$.

$$
\sum_{\text{perms }\phi}\!\! \hat{t}_{1,\phi(1)} \cdots\hat{t}_{i,\phi(i)}\cdots\hat{t}_{n,\phi(n)} \operatorname{sgn}(\phi) =\sum_{\phi} t_{1,\phi(1)}\cdots kt_{i,\phi(i)}\cdots t_{n,\phi(n)} \operatorname{sgn}(\phi)
$$

Factor the $$k$$ out of each term to get the desired equality.

$$
=k\cdot\sum_{\phi} t_{1,\phi(1)}\cdots t_{i,\phi(i)}\cdots t_{n,\phi(n)} \operatorname{sgn}(\phi) =k\cdot d(T)
$$

For (2), let $$T[b]{\xrightarrow[]{\rho_i\leftrightarrow\rho_j}}\hat{T}$$.

$$
d(\hat{T})= \sum_{\text{perms }\phi}\!\! \hat{t}_{1,\phi(1)} \cdots\hat{t}_{i,\phi(i)} \cdots\hat{t}_{j,\phi(j)} \cdots \hat{t}_{n,\phi(n)} \operatorname{sgn}(\phi)
$$

To convert to unhatted $$t$$'s, for each $$\phi$$ consider the permutation $$\sigma$$ that equals $$\phi$$ except that the $$i$$-th and $$j$$-th numbers are interchanged, $$\sigma(i)=\phi(j)$$ and $$\sigma(j)=\phi(i)$$. Replacing the $$\phi$$ in $$\hat{t}_{1,\phi(1)} \cdots\hat{t}_{i,\phi(i)} \cdots\hat{t}_{j,\phi(j)} \cdots \hat{t}_{n,\phi(n)}$$ with this $$\sigma$$ gives $$t_{1,\sigma(1)} \cdots t_{j,\sigma(j)} \cdots t_{i,\sigma(i)} \cdots t_{n,\sigma(n)}$$. Now $$\operatorname{sgn}(\phi)=-\operatorname{sgn}(\sigma)$$ (by Lemma 4.3) and so we get

$$
\begin{array}{rl} &=\sum_\sigma t_{1,\sigma(1)} \cdots t_{j,\sigma(j)} \cdots t_{i,\sigma(i)} \cdots t_{n,\sigma(n)} \cdot\bigl(-\operatorname{sgn}(\sigma)\bigr) \\ &=-\sum_{\sigma} t_{1,\sigma(1)}\cdots t_{j,\sigma(j)} \cdots t_{i,\sigma(i)}\cdots t_{n,\sigma(n)}\cdot\operatorname{sgn}(\sigma) \end{array}
$$

where the sum is over all permutations $$\sigma$$ derived from another permutation $$\phi$$ by a swap of the $$i$$-th and $$j$$-th numbers. But any permutation can be derived from some other permutation by such a swap, in one and only one way, so this summation is in fact a sum over all permutations, taken once and only once. Thus $$d(\hat{T})=-d(T)$$.

To do property (1) let $$T[b]{\xrightarrow[]{k\rho_i+\rho_j}}\hat{T}$$ and consider

$$
\begin{array}{rl} d(\hat{T}) &=\sum_{\text{perms }\phi} \hat{t}_{1,\phi(1)}\cdots\hat{t}_{i,\phi(i)} \cdots\hat{t}_{j,\phi(j)}\cdots\hat{t}_{n,\phi(n)} \operatorname{sgn}(\phi) \\ &=\sum_{\phi} t_{1,\phi(1)}\cdots t_{i,\phi(i)} \cdots (kt_{i,\phi(j)}+t_{j,\phi(j)})\cdots t_{n,\phi(n)} \operatorname{sgn}(\phi) \end{array}
$$

(notice: that's $$kt_{i,\phi(j)}$$, not $$kt_{j,\phi(j)}$$). Distribute, commute, and factor.

$$
\begin{array}{rl} =&\displaystyle\sum_{\phi} \big[t_{1,\phi(1)}\cdots t_{i,\phi(i)} \cdots kt_{i,\phi(j)}\cdots t_{n,\phi(n)} \operatorname{sgn}(\phi)\\ &\displaystyle\qquad+t_{1,\phi(1)}\cdots t_{i,\phi(i)} \cdots t_{j,\phi(j)}\cdots t_{n,\phi(n)} \operatorname{sgn}(\phi)\big] \\ \\ =&\displaystyle \sum_{{\phi}} t_{1,\phi(1)}\cdots t_{i,\phi(i)} \cdots kt_{i,\phi(j)}\cdots t_{n,\phi(n)} \operatorname{sgn}(\phi) \\ &\displaystyle\qquad +\sum_{\phi} t_{1,\phi(1)}\cdots t_{i,\phi(i)} \cdots t_{j,\phi(j)}\cdots t_{n,\phi(n)} \operatorname{sgn}(\phi) \\ \\ =&\displaystyle k\cdot \sum_{{\phi}} t_{1,\phi(1)}\cdots t_{i,\phi(i)} \cdots t_{i,\phi(j)}\cdots t_{n,\phi(n)} \operatorname{sgn}(\phi)+d(T) \end{array}
$$

We finish by showing that the terms $$t_{1,\phi(1)}\cdots t_{i,\phi(i)} \cdots t_{i,\phi(j)}\dots t_{n,\phi(n)} \operatorname{sgn}(\phi)$$ add to zero. This sum represents $$d(S)$$ where $$S$$ is a matrix equal to $$T$$ except that row $$j$$ of $$S$$ is a copy of row $$i$$ of $$T$$ (because the factor is $$t_{i,\phi(j)}$$, not $$t_{j,\phi(j)}$$). Thus, $$S$$ has two equal rows, rows $$i$$ and $$j$$. Since we have already shown that $$d$$ changes sign on row swaps, as in [Lemma 2.3](Linear%20Algebra%20-%20Properties%20of%20Determinants.md) we conclude that $$d(S)=0$$.

We have now shown that determinant functions exist for each size. We already know that for each size there is at most one determinant. Therefore, the permutation expansion computes the one and only determinant value of a square matrix.

We end this subsection by proving the other result remaining from the prior subsection, that the determinant of a matrix equals the determinant of its transpose.

**Example 4.8**  —

Writing out the permutation expansion of the general $$3 \! \times \! 3$$ matrix and of its transpose, and comparing corresponding terms

$$
\begin{vmatrix} a &b &c \\ d &e &f \\ g &h &i \end{vmatrix} = \cdots\,+ cdh\cdot\begin{vmatrix} 0 &0 &1 \\ 1 &0 &0 \\ 0 &1 &0 \end{vmatrix} +\,\cdots
$$

(terms with the same letters)

$$
\begin{vmatrix} a &d &g \\ b &e &h \\ c &f &i \end{vmatrix} = \cdots\,+ dhc\cdot\begin{vmatrix} 0 &1 &0 \\ 0 &0 &1 \\ 1 &0 &0 \end{vmatrix} +\,\cdots
$$

shows that the corresponding permutation matrices are transposes. That is, there is a relationship between these corresponding permutations. Problem 6 shows that they are inverses.

**Theorem 4.9**  —

The determinant of a matrix equals the determinant of its transpose.

**Proof**  —

Call the matrix $$T$$ and denote the entries of $${{T}^{\rm trans}}$$ with $$s$$'s so that $$t_{i,j}=s_{j,i}$$. Substitution gives this

$$
\left|T\right| =\sum_{\text{perms }\phi} t_{1,\phi(1)}\dots t_{n,\phi(n)} \operatorname{sgn}(\phi) =\sum_{\phi} s_{\phi(1),1}\dots s_{\phi(n),n} \operatorname{sgn}(\phi)
$$

and we can finish the argument by manipulating the expression on the right to be recognizable as the determinant of the transpose. We have written all permutation expansions (as in the middle expression above) with the row indices ascending. To rewrite the expression on the right in this way, note that because $$\phi$$ is a permutation, the row indices in the term on the right $$\phi(1)$$, ..., $$\phi(n)$$ are just the numbers $$1$$, ..., $$n$$, rearranged. We can thus commute to have these ascend, giving $$s_{1,\phi^{-1}(1)}\cdots s_{n,\phi^{-1}(n)}$$ (if the column index is $$j$$ and the row index is $$\phi(j)$$ then, where the row index is $$i$$, the column index is $$\phi^{-1}(i)$$). Substituting on the right gives

$$
=\sum_{\phi^{-1}} s_{1,\phi^{-1}(1)}\cdots s_{n,\phi^{-1}(n)} \operatorname{sgn}(\phi^{-1})
$$

(Problem 5 shows that $$\operatorname{sgn}(\phi^{-1})=\operatorname{sgn}(\phi)$$). Since every permutation is the inverse of another, a sum over all $$\phi^{-1}$$ is a sum over all permutations $$\phi$$

$$
=\sum_{\text{perms }\sigma} s_{1,\sigma^(1)}\dots s_{n,\sigma(n)} \operatorname{sgn}(\sigma) =\left|{{T}^{\rm trans}}\right|
$$

as required.

### Exercises

*These summarize the notation used in this book for the $$2$$- and $$3$$- permutations.*

$$
\begin{array}{c|cc} i &1 &2 \\ \hline \phi_1(i) &1 &2 \\ \phi_2(i) &2 &1 \end{array} \qquad \begin{array}{c|ccc} i &1 &2 &3 \\ \hline \phi_1(i) &1 &2 &3 \\ \phi_2(i) &1 &3 &2 \\ \phi_3(i) &2 &1 &3 \\ \phi_4(i) &2 &3 &1 \\ \phi_5(i) &3 &1 &2 \\ \phi_6(i) &3 &2 &1 \end{array}
$$

**Problem 1**  —

Give the permutation expansion of a general $$2 \! \times \! 2$$ matrix and its transpose.  
*This exercise is recommended for all readers.*

**Problem 2**  —

*This problem appears also in the prior subsection.*

1. Find the inverse of each $$2$$-permutation.
2. Find the inverse of each $$3$$-permutation.  
*This exercise is recommended for all readers.*

**Problem 3**  —

1. Find the signum of each $$2$$-permutation.
2. Find the signum of each $$3$$-permutation.

**Problem 4**  —

What is the signum of the $$n$$-permutation $$\phi=\langle n,n-1,\dots,2,1 \rangle$$? (Strang 1980)

**Problem 5**  —

Prove these.

1. Every permutation has an inverse.
2. $$\operatorname{sgn}(\phi^{-1})=\operatorname{sgn}(\phi)$$
3. Every permutation is the inverse of another.

**Problem 6**  —

Prove that the matrix of the permutation inverse is the transpose of the matrix of the permutation $$P_{\phi^{-1}}={{P_{\phi}}^{\rm trans}}$$, for any permutation $$\phi$$.  
*This exercise is recommended for all readers.*

**Problem 7**  —

Show that a permutation matrix with $$m$$ inversions can be row swapped to the identity in $$m$$ steps. Contrast this with Corollary 4.6.  
*This exercise is recommended for all readers.*

**Problem 8**  —

For any permutation $$\phi$$ let $$g(\phi)$$ be the integer defined in this way.

$$
g(\phi)=\prod_{i<j} [\phi(j)-\phi(i)]
$$

(This is the product, over all indices $$i$$ and $$j$$ with $$i<j$$, of terms of the given form.)

1. Compute the value of $$g$$ on all $$2$$-permutations.
2. Compute the value of $$g$$ on all $$3$$-permutations.
3. Prove this.

$$
\operatorname{sgn}(\phi)=\frac{g(\phi)}{|g(\phi)|}
$$

Many authors give this formula as the definition of the signum function.

Solutions

### References

- Strang, Gilbert (1980), *Linear Algebra and its Applications* (2nd ed.), Hartcourt Brace Javanovich

---

*Source: Wikibooks, Linear Algebra/Determinants Exist (https://en.wikibooks.org/wiki/Linear_Algebra/Determinants_Exist), by Wikibooks contributors, CC BY-SA 4.0.*
