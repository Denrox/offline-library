# Gram-Schmidt Orthogonalization

*This subsection is optional. It requires material from the prior, also optional, subsection. The work done here will only be needed in the final two sections of Chapter Five.*

The prior subsection suggests that projecting onto the line spanned by $$\vec{s}$$ decomposes a vector $$\vec{v}$$ into two parts

- $$\displaystyle \vec{v}=\text{proj}_{[\vec{s}\,]}({\vec{v}}) \,+\,\left(\vec{v}-\text{proj}_{[\vec{s}\,]}({\vec{v}})\right)$$

that are orthogonal and so are "not interacting". We will now develop that suggestion.

**Definition 2.1**  —

Vectors $$\vec{v}_1,\dots,\vec{v}_k\in\mathbb{R}^n$$ are **mutually orthogonal** when any two are orthogonal: if $$i\neq j$$ then the dot product $$\vec{v}_i\cdot\vec{v}_j$$ is zero.

**Theorem 2.2**  —

If the vectors in a set $$\{\vec{v}_1,\dots,\vec{v}_k\}\subset\mathbb{R}^n$$ are mutually orthogonal and nonzero then that set is linearly independent.

**Proof**  —

Consider a linear relationship $$c_1\vec{v}_1+c_2\vec{v}_2+\dots+c_k\vec{v}_k=\vec{0}$$. If $$i\in [1..k]$$ then taking the dot product of $$\vec{v}_i$$ with both sides of the equation

$$
\begin{array}{rl} \vec{v}_i\cdot (c_1\vec{v}_1+c_2\vec{v}_2+\dots+c_k\vec{v}_k) &=\vec{v}_i\cdot\vec{0} \\ c_i\cdot(\vec{v}_i\cdot\vec{v}_i) &=0 \end{array}
$$

shows, since $$\vec{v}_i$$ is nonzero, that $$c_i$$ is zero.

**Corollary 2.3**  —

If the vectors in a size $$k$$ subset of a $$k$$ dimensional space are mutually orthogonal and nonzero then that set is a basis for the space.

**Proof**  —

Any linearly independent size $$k$$ subset of a $$k$$ dimensional space is a basis.

Of course, the converse of Corollary 2.3 does not hold— not every basis of every subspace of $$\mathbb{R}^n$$ is made of mutually orthogonal vectors. However, we can get the partial converse that for every subspace of $$\mathbb{R}^n$$ there is at least one basis consisting of mutually orthogonal vectors.

**Example 2.4**  —

The members $$\vec{\beta}_1$$ and $$\vec{\beta}_2$$ of this basis for $$\mathbb{R}^2$$ are not orthogonal.

- $$\displaystyle B=\left\langle \begin{pmatrix} 4 \\ 2 \end{pmatrix}, \begin{pmatrix} 1 \\ 3 \end{pmatrix} \right\rangle$$

However, we can derive from $$B$$ a new basis for the same space that does have mutually orthogonal members. For the first member of the new basis we simply use $$\vec{\beta}_1$$.

$$
\vec{\kappa}_1=\begin{pmatrix} 4 \\ 2 \end{pmatrix}
$$

For the second member of the new basis, we take away from $$\vec{\beta}_2$$ its part in the direction of $$\vec{\kappa}_1$$,

- $$\displaystyle \vec{\kappa}_2=\begin{pmatrix} 1 \\ 3 \end{pmatrix} -\text{proj}_{\scriptstyle[\vec{\kappa}_1]}({\begin{pmatrix} 1 \\ 3 \end{pmatrix}}) =\begin{pmatrix} 1 \\ 3 \end{pmatrix}-\begin{pmatrix} 2 \\ 1 \end{pmatrix}=\begin{pmatrix} -1 \\ 2 \end{pmatrix}$$

which leaves the part, $$\vec{\kappa}_2$$ pictured above, of $$\vec{\beta}_2$$ that is orthogonal to $$\vec{\kappa}_1$$ (it is orthogonal by the definition of the projection onto the span of $$\vec{\kappa}_1$$). Note that, by the corollary, $$\{\vec{\kappa}_1,\vec{\kappa}_2\}$$ is a basis for $$\mathbb{R}^2$$.

**Definition 2.5**  —

An **orthogonal basis** for a vector space is a basis of mutually orthogonal vectors.

**Example 2.6**  —

To turn this basis for $$\mathbb{R}^3$$

$$
\left\langle \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ 3 \end{pmatrix} \right\rangle
$$

into an orthogonal basis, we take the first vector as it is given.

$$
\vec{\kappa}_1=\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}
$$

We get $$\vec{\kappa}_2$$ by starting with the given second vector $$\vec{\beta}_2$$ and subtracting away the part of it in the direction of $$\vec{\kappa}_1$$.

$$
\vec{\kappa}_2=\begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix} -\text{proj}_{[\vec{\kappa}_1]}({\begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix}}) =\begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix}-\begin{pmatrix} 2/3 \\ 2/3 \\ 2/3 \end{pmatrix} =\begin{pmatrix} -2/3 \\ 4/3 \\ -2/3 \end{pmatrix}
$$

Finally, we get $$\vec{\kappa}_3$$ by taking the third given vector and subtracting the part of it in the direction of $$\vec{\kappa}_1$$, and also the part of it in the direction of $$\vec{\kappa}_2$$.

$$
\vec{\kappa}_3=\begin{pmatrix} 1 \\ 0 \\ 3 \end{pmatrix} -\text{proj}_{[\vec{\kappa}_1]}({\begin{pmatrix} 1 \\ 0 \\ 3 \end{pmatrix}}) -\text{proj}_{[\vec{\kappa}_2]}({\begin{pmatrix} 1 \\ 0 \\ 3 \end{pmatrix}}) =\begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}
$$

Again the corollary gives that

$$
\left\langle \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \begin{pmatrix} -2/3 \\ 4/3 \\ -2/3 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} \right\rangle
$$

is a basis for the space.

The next result verifies that the process used in those examples works with any basis for any subspace of an $$\mathbb{R}^n$$ (we are restricted to $$\mathbb{R}^n$$ only because we have not given a definition of orthogonality for other vector spaces).

**Theorem 2.7 (Gram-Schmidt orthogonalization)**  —

If $$\left\langle \vec{\beta}_1,\ldots\vec{\beta}_k \right\rangle$$ is a basis for a subspace of $$\mathbb{R}^n$$ then, where

$$
\begin{array}{rl} \vec{\kappa}_1 &=\vec{\beta}_1 \\ \vec{\kappa}_2 &=\vec{\beta}_2-\text{proj}_{[\vec{\kappa}_1]}({\vec{\beta}_2}) \\ \vec{\kappa}_3 &=\vec{\beta}_3 -\text{proj}_{[\vec{\kappa}_1]}({\vec{\beta}_3}) -\text{proj}_{[\vec{\kappa}_2]}({\vec{\beta}_3}) \\ &\vdots \\ \vec{\kappa}_k &=\vec{\beta}_k -\text{proj}_{[\vec{\kappa}_1]}({\vec{\beta}_k})-\cdots -\text{proj}_{[\vec{\kappa}_{k-1}]}({\vec{\beta}_k}) \end{array}
$$

the $$\vec{\kappa}\,$$'s form an orthogonal basis for the same subspace.

**Proof**  —

We will use induction to check that each $$\vec{\kappa}_i$$ is nonzero, is in the span of $$\left\langle \vec{\beta}_1,\ldots\vec{\beta}_i \right\rangle$$ and is orthogonal to all preceding vectors: $$\vec{\kappa}_1\cdot\vec{\kappa}_i= \cdots =\vec{\kappa}_{i-1}\cdot\vec{\kappa}_{i}=0$$. With those, and with Corollary 2.3, we will have that $$\left\langle \vec{\kappa}_1,\ldots\vec{\kappa}_k \right\rangle$$ is a basis for the same space as $$\left\langle \vec{\beta}_1,\ldots\vec{\beta}_k \right\rangle$$.

We shall cover the cases up to $$i=3$$, which give the sense of the argument. Completing the details is Problem 15.

The $$i=1$$ case is trivial— setting $$\vec{\kappa}_1$$ equal to $$\vec{\beta}_1$$ makes it a nonzero vector since $$\vec{\beta}_1$$ is a member of a basis, it is obviously in the desired span, and the "orthogonal to all preceding vectors" condition is vacuously met.

For the $$i=2$$ case, expand the definition of $$\vec{\kappa}_2$$.

$$
\vec{\kappa}_2=\vec{\beta}_2 -\text{proj}_{[\vec{\kappa}_1]}({\vec{\beta}_2})= \vec{\beta}_2 -\frac{\vec{\beta}_2\cdot\vec{\kappa}_1}{ \vec{\kappa}_1\cdot\vec{\kappa}_1} \cdot\vec{\kappa}_1 = \vec{\beta}_2 -\frac{\vec{\beta}_2\cdot\vec{\kappa}_1}{ \vec{\kappa}_1\cdot\vec{\kappa}_1} \cdot\vec{\beta}_1
$$

This expansion shows that $$\vec{\kappa}_2$$ is nonzero or else this would be a non-trivial linear dependence among the $$\vec{\beta}$$'s (it is nontrivial because the coefficient of $$\vec{\beta}_2$$ is $$1$$) and also shows that $$\vec{\kappa}_2$$ is in the desired span. Finally, $$\vec{\kappa}_2$$ is orthogonal to the only preceding vector

$$
\vec{\kappa}_1\cdot\vec{\kappa}_2= \vec{\kappa}_1\cdot(\vec{\beta}_2 -\text{proj}_{[\vec{\kappa}_1]}({\vec{\beta}_2}))=0
$$

because this projection is orthogonal.

The $$i=3$$ case is the same as the $$i=2$$ case except for one detail. As in the $$i=2$$ case, expanding the definition

$$
\begin{array}{rl} \vec{\kappa}_3 &=\vec{\beta}_3 -\frac{\vec{\beta}_3\cdot\vec{\kappa}_1}{ \vec{\kappa}_1\cdot\vec{\kappa}_1} \cdot\vec{\kappa}_1 -\frac{\vec{\beta}_3\cdot\vec{\kappa}_2}{ \vec{\kappa}_2\cdot\vec{\kappa}_2} \cdot\vec{\kappa}_2 \\ &=\vec{\beta}_3 -\frac{\vec{\beta}_3\cdot\vec{\kappa}_1}{ \vec{\kappa}_1\cdot\vec{\kappa}_1} \cdot\vec{\beta}_1 -\frac{\vec{\beta}_3\cdot\vec{\kappa}_2}{ \vec{\kappa}_2\cdot\vec{\kappa}_2} \cdot\bigl(\vec{\beta}_2 -\frac{\vec{\beta}_2\cdot\vec{\kappa}_1}{ \vec{\kappa}_1\cdot\vec{\kappa}_1} \cdot\vec{\beta}_1\bigr) \end{array}
$$

shows that $$\vec{\kappa}_3$$ is nonzero and is in the span. A calculation shows that $$\vec{\kappa}_3$$ is orthogonal to the preceding vector $$\vec{\kappa}_1$$.

$$
\begin{array}{rl} \vec{\kappa}_1\cdot\vec{\kappa}_3 &=\vec{\kappa}_1\cdot\bigl(\vec{\beta}_3 -\text{proj}_{[\vec{\kappa}_1]}({\vec{\beta}_3}) -\text{proj}_{[\vec{\kappa}_2]}({\vec{\beta}_3})\bigr) \\ &=\vec{\kappa}_1\cdot\bigl(\vec{\beta}_3 -\text{proj}_{[\vec{\kappa}_1]}({\vec{\beta}_3})\bigr) -\vec{\kappa}_1\cdot\text{proj}_{[\vec{\kappa}_2]}({\vec{\beta}_3}) \\ &=0 \end{array}
$$

(Here's the difference from the $$i=2$$ case— the second line has two kinds of terms. The first term is zero because this projection is orthogonal, as in the $$i=2$$ case. The second term is zero because $$\vec{\kappa}_1$$ is orthogonal to $$\vec{\kappa}_2$$ and so is orthogonal to any vector in the line spanned by $$\vec{\kappa}_2$$.) The check that $$\vec{\kappa}_3$$ is also orthogonal to the other preceding vector $$\vec{\kappa}_2$$ is similar.

Beyond having the vectors in the basis be orthogonal, we can do more; we can arrange for each vector to have length one by dividing each by its own length (we can **normalize** the lengths).

**Example 2.8**  —

Normalizing the length of each vector in the orthogonal basis of Example 2.6 produces this **orthonormal basis**.

$$
\left\langle \begin{pmatrix} 1/\sqrt{3} \\ 1/\sqrt{3} \\ 1/\sqrt{3} \end{pmatrix}, \begin{pmatrix} -1/\sqrt{6} \\ 2/\sqrt{6} \\ -1/\sqrt{6} \end{pmatrix}, \begin{pmatrix} -1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{pmatrix} \right\rangle
$$

Besides its intuitive appeal, and its analogy with the standard basis $$\mathcal{E}_n$$ for $$\mathbb{R}^n$$, an orthonormal basis also simplifies some computations. See Exercise 9, for example.

### Exercises

**Problem 1**  —

Perform the Gram-Schmidt process on each of these bases for $$\mathbb{R}^2$$.

1. $$\left\langle \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 2 \\ 1 \end{pmatrix} \right\rangle$$
2. $$\left\langle \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \begin{pmatrix} -1 \\ 3 \end{pmatrix} \right\rangle$$
3. $$\left\langle \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \end{pmatrix} \right\rangle$$

Then turn those orthogonal bases into orthonormal bases.  
*This exercise is recommended for all readers.*

**Problem 2**  —

Perform the Gram-Schmidt process on each of these bases for $$\mathbb{R}^3$$.

1. $$\left\langle \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}, \begin{pmatrix} 0 \\ 3 \\ 1 \end{pmatrix} \right\rangle$$
2. $$\left\langle \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix} \right\rangle$$

Then turn those orthogonal bases into orthonormal bases.  
*This exercise is recommended for all readers.*

**Problem 3**  —

Find an orthonormal basis for this subspace of $$\mathbb{R}^3$$: the plane $$x-y+z=0$$.

**Problem 4**  —

Find an orthonormal basis for this subspace of $$\mathbb{R}^4$$.

$$
\{\begin{pmatrix} x \\ y \\ z \\ w \end{pmatrix}\,\big|\, x-y-z+w=0\text{ and }x+z=0\}
$$

**Problem 5**  —

Show that any linearly independent subset of $$\mathbb{R}^n$$ can be orthogonalized without changing its span.  
*This exercise is recommended for all readers.*

**Problem 6**  —

What happens if we apply the Gram-Schmidt process to a basis that is already orthogonal?

**Problem 7**  —

Let $$\left\langle \vec{\kappa}_1,\dots,\vec{\kappa}_k \right\rangle$$ be a set of mutually orthogonal vectors in $$\mathbb{R}^n$$.

1. Prove that for any $$\vec{v}$$ in the space, the vector $$\vec{v}-(\text{proj}_{[\vec{\kappa}_1]}({\vec{v}\,}) +\dots+\text{proj}_{[\vec{v}_k]}({\vec{v}\,}))$$ is orthogonal to each of $$\vec{\kappa}_1$$, ..., $$\vec{\kappa}_k$$.
2. Illustrate the prior item in $$\mathbb{R}^3$$ by using $$\vec{e}_1$$ as $$\vec{\kappa}_1$$, using $$\vec{e}_2$$ as $$\vec{\kappa}_2$$, and taking $$\vec{v}$$ to have components $$1$$, $$2$$, and $$3$$.
3. Show that $$\text{proj}_{[\vec{\kappa}_1]}({\vec{v}\,}) +\dots+\text{proj}_{[\vec{v}_k]}({\vec{v}\,})$$ is the vector in the span of the set of $$\vec{\kappa}$$'s that is closest to $$\vec{v}$$. *Hint*. To the illustration done for the prior part, add a vector $$d_1\vec{\kappa}_1+d_2\vec{\kappa}_2$$ and apply the Pythagorean Theorem to the resulting triangle.

**Problem 8**  —

Find a vector in $$\mathbb{R}^3$$ that is orthogonal to both of these.

$$
\begin{pmatrix} 1 \\ 5 \\ -1 \end{pmatrix} \qquad \begin{pmatrix} 2 \\ 2 \\ 0 \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 9**  —

One advantage of orthogonal bases is that they simplify finding the representation of a vector with respect to that basis.

1. For this vector and this non-orthogonal basis for $$\mathbb{R}^2$$

$$
\vec{v}=\begin{pmatrix} 2 \\ 3 \end{pmatrix} \qquad B=\left\langle \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \end{pmatrix} \right\rangle
$$

first represent the vector with respect to the basis. Then project the vector onto the span of each basis vector $$[{\vec{\beta}_1}]$$ and $$[{\vec{\beta}_2}]$$.
2. With this orthogonal basis for $$\mathbb{R}^2$$

$$
K=\left\langle \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \end{pmatrix} \right\rangle
$$

represent the same vector $$\vec{v}$$ with respect to the basis. Then project the vector onto the span of each basis vector. Note that the coefficients in the representation and the projection are the same.
3. Let $$K=\left\langle \vec{\kappa}_1,\ldots,\vec{\kappa}_k \right\rangle$$ be an orthogonal basis for some subspace of $$\mathbb{R}^n$$. Prove that for any $$\vec{v}$$ in the subspace, the $$i$$-th component of the representation $${\rm Rep}_{K}(\vec{v}\,)$$ is the scalar coefficient $$(\vec{v}\cdot\vec{\kappa}_i)/ (\vec{\kappa}_i\cdot\vec{\kappa}_i)$$ from $$\text{proj}_{[\vec{\kappa}_i]}({\vec{v}\,})$$.
4. Prove that $$\vec{v}=\text{proj}_{[\vec{\kappa}_1]}({\vec{v}\,}) +\dots+\text{proj}_{[\vec{\kappa}_k]}({\vec{v}\,})$$.

**Problem 10**  —

*Bessel's Inequality*. Consider these orthonormal sets

$$
B_1=\{\vec{e}_1\} \quad B_2=\{\vec{e}_1,\vec{e}_2\} \quad B_3=\{\vec{e}_1,\vec{e}_2,\vec{e}_3\} \quad B_4=\{\vec{e}_1,\vec{e}_2,\vec{e}_3,\vec{e}_4\}
$$

along with the vector $$\vec{v}\in\mathbb{R}^4$$ whose components are $$4$$, $$3$$, $$2$$, and $$1$$.

1. Find the coefficient $$c_1$$ for the projection of $$\vec{v}$$ onto the span of the vector in $$B_1$$. Check that $$|\vec{v}\,|^2\geq |c_1|^2$$.
2. Find the coefficients $$c_1$$ and $$c_2$$ for the projection of $$\vec{v}$$ onto the spans of the two vectors in $$B_2$$. Check that $$|\vec{v}\,|^2\geq |c_1|^2+|c_2|^2$$.
3. Find $$c_1$$, $$c_2$$, and $$c_3$$ associated with the vectors in $$B_3$$, and $$c_1$$, $$c_2$$, $$c_3$$, and $$c_4$$ for the vectors in $$B_4$$. Check that $$|\vec{v}\,|^2\geq |c_1|^2+\dots+|c_3|^2$$ and that $$|\vec{v}\,|^2\geq |c_1|^2+\dots+|c_4|^2$$.

Show that this holds in general: where $$\{\vec{\kappa}_1,\ldots,\vec{\kappa}_k\}$$ is an orthonormal set and $$c_i$$ is coefficient of the projection of a vector $$\vec{v}$$ from the space then $$|\vec{v}\,|^2\geq |c_1|^2+\dots+|c_k|^2$$. *Hint*. One way is to look at the inequality $$0\leq|\vec{v}-(c_1\vec{\kappa}_1+\dots+c_k\vec{\kappa}_k)|^2$$ and expand the $$c$$'s.

**Problem 11**  —

Prove or disprove: every vector in $$\mathbb{R}^n$$ is in some orthogonal basis.

**Problem 12**  —

Show that the columns of an $$n \! \times \! n$$ matrix form an orthonormal set if and only if the inverse of the matrix is its transpose. Produce such a matrix.

**Problem 13**  —

Does the proof of Theorem 2.2 fail to consider the possibility that the set of vectors is empty (i.e., that $$k=0$$)?

**Problem 14**  —

Theorem 2.7 describes a change of basis from any basis $$B=\left\langle \vec{\beta}_1,\ldots,\vec{\beta}_k \right\rangle$$ to one that is orthogonal $$K=\left\langle \vec{\kappa}_1,\ldots,\vec{\kappa}_k \right\rangle$$. Consider the change of basis matrix $${\rm Rep}_{B,K}(\text{id})$$.

1. Prove that the matrix $${\rm Rep}_{K,B}(\text{id})$$ changing bases in the direction opposite to that of the theorem has an upper triangular shape— all of its entries below the main diagonal are zeros.
2. Prove that the inverse of an upper triangular matrix is also upper triangular (if the matrix is invertible, that is). This shows that the matrix $${\rm Rep}_{B,K}(\text{id})$$ changing bases in the direction described in the theorem is upper triangular.

**Problem 15**  —

Complete the induction argument in the proof of Theorem 2.7.

Solutions

---

*Source: Wikibooks, Linear Algebra/Gram-Schmidt Orthogonalization (https://en.wikibooks.org/wiki/Linear_Algebra/Gram-Schmidt_Orthogonalization), by Wikibooks contributors, CC BY-SA 4.0.*
