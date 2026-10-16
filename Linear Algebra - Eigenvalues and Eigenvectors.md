# Eigenvalues and Eigenvectors

In this subsection we will focus on the property of [Corollary 2.4](Linear%20Algebra%20-%20Diagonalizability.md).

**Definition 3.1**  —

A transformation $$t:V\to V$$ has a scalar **eigenvalue** $$\lambda$$ if there is a nonzero **eigenvector** $$\vec{\zeta}\in V$$ such that $$t(\vec{\zeta})=\lambda\cdot\vec{\zeta}$$.

("Eigen" is German for "characteristic of" or "peculiar to"; some authors call these **characteristic** values and vectors. No authors call them "peculiar".)

**Example 3.2**  —

The projection map

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} \stackrel{\pi}{\longmapsto} \begin{pmatrix} x \\ y \\ 0 \end{pmatrix} \qquad x,y,z\in\mathbb{C}
$$

has an eigenvalue of $$1$$ associated with any eigenvector of the form

$$
\begin{pmatrix} x \\ y \\ 0 \end{pmatrix}
$$

where $$x$$ and $$y$$ are scalars at least one of which is non-$$0$$. On the other hand, $$2$$ is not an eigenvalue of $$\pi$$ since no non-$$\vec{0}$$ vector is doubled.

That example shows why the "non-$$\vec{0}$$" appears in the definition. Disallowing $$\vec{0}$$ as an eigenvector eliminates trivial eigenvalues.

**Example 3.3**  —

The only transformation on the trivial space $$\{\vec{0}\,\}$$ is

$$
\vec{0}\mapsto\vec{0}
$$

This map has no eigenvalues because there are no non-$$\vec{0}$$ vectors $$\vec{v}$$ mapped to a scalar multiple $$\lambda\cdot\vec{v}$$ of themselves.

**Example 3.4**  —

Consider the homomorphism $$t:\mathcal{P}_1\to \mathcal{P}_1$$ given by $$c_0+c_1x\mapsto(c_0+c_1)+(c_0+c_1)x$$. The range of $$t$$ is one-dimensional. Thus an application of $$t$$ to a vector in the range will simply rescale that vector: $$c+cx\mapsto (2c)+(2c)x$$. That is, $$t$$ has an eigenvalue of $$2$$ associated with eigenvectors of the form $$c+cx$$ where $$c\neq 0$$.

This map also has an eigenvalue of $$0$$ associated with eigenvectors of the form $$c-cx$$ where $$c\neq 0$$.

**Definition 3.5**  —

A square matrix $$T$$ has a scalar **eigenvalue** $$\lambda$$ associated with the non-$$\vec{0}$$ **eigenvector** $$\vec{\zeta}$$ if $$T\vec{\zeta}=\lambda\cdot\vec{\zeta}$$.

**Remark 3.6**  —

Although this extension from maps to matrices is obvious, there is a point that must be made. Eigenvalues of a map are also the eigenvalues of matrices representing that map, and so similar matrices have the same eigenvalues. But the eigenvectors are different— similar matrices need not have the same eigenvectors.

For instance, consider again the transformation $$t:\mathcal{P}_1\to \mathcal{P}_1$$ given by $$c_0+c_1x\mapsto (c_0+c_1)+(c_0+c_1)x$$. It has an eigenvalue of $$2$$ associated with eigenvectors of the form $$c+cx$$ where $$c\neq 0$$. If we represent $$t$$ with respect to $$B=\langle 1+1x,1-1x \rangle$$

$$
T={\rm Rep}_{B,B}(t)= \begin{pmatrix} 2 &0 \\ 0 &0 \end{pmatrix}
$$

then $$2$$ is an eigenvalue of $$T$$, associated with these eigenvectors.

$$
\{\begin{pmatrix} c_0 \\ c_1 \end{pmatrix}\,\big|\, \begin{pmatrix} 2 &0 \\ 0 &0 \end{pmatrix}\begin{pmatrix} c_0 \\ c_1 \end{pmatrix} =\begin{pmatrix} 2c_0 \\ 2c_1 \end{pmatrix} \} =\{\begin{pmatrix} c_0 \\ 0 \end{pmatrix}\,\big|\, c_0\in\mathbb{C},\, c_0\neq 0 \}
$$

On the other hand, representing $$t$$ with respect to $$D=\langle 2+1x,1+0x \rangle$$ gives

$$
S={\rm Rep}_{D,D}(t)= \begin{pmatrix} 3 &1 \\ -3 &-1 \end{pmatrix}
$$

and the eigenvectors of $$S$$ associated with the eigenvalue $$2$$ are these.

$$
\{\begin{pmatrix} c_0 \\ c_1 \end{pmatrix}\,\big|\, \begin{pmatrix} 3 &1 \\ -3 &-1 \end{pmatrix}\begin{pmatrix} c_0 \\ c_1 \end{pmatrix} =\begin{pmatrix} 2c_0 \\ 2c_1 \end{pmatrix} \} =\{\begin{pmatrix} 0 \\ c_1 \end{pmatrix}\,\big|\, c_1\in\mathbb{C},\, c_1\neq 0 \}
$$

Thus similar matrices can have different eigenvectors.

Here is an informal description of what's happening. The underlying transformation doubles the eigenvectors $$\vec{v}\mapsto 2\cdot\vec{v}$$. But when the matrix representing the transformation is $$T={\rm Rep}_{B,B}(t)$$ then it "assumes" that column vectors are representations with respect to $$B$$. In contrast, $$S={\rm Rep}_{D,D}(t)$$ "assumes" that column vectors are representations with respect to $$D$$. So the vectors that get doubled by each matrix look different.

The next example illustrates the basic tool for finding eigenvectors and eigenvalues.

**Example 3.7**  —

What are the eigenvalues and eigenvectors of this matrix?

$$
T= \begin{pmatrix} 1 &2 &1 \\ 2 &0 &-2 \\ -1 &2 &3 \end{pmatrix}
$$

To find the scalars $$x$$ such that $$T\vec{\zeta}=x\vec{\zeta}$$ for non-$$\vec{0}$$ eigenvectors $$\vec{\zeta}$$, bring everything to the left-hand side

$$
\begin{pmatrix} 1 &2 &1 \\ 2 &0 &-2 \\ -1 &2 &3 \end{pmatrix} \begin{pmatrix} z_1 \\ z_2 \\ z_3 \end{pmatrix} -x\begin{pmatrix} z_1 \\ z_2 \\ z_3 \end{pmatrix} =\vec{0}
$$

and factor $$(T-x I)\vec{\zeta}=\vec{0}$$. (Note that it says $$T-xI$$; the expression $$T-x$$ doesn't make sense because $$T$$ is a matrix while $$x$$ is a scalar.) This homogeneous linear system

$$
\begin{pmatrix} 1-x &2 &1 \\ 2 &0-x &-2 \\ -1 &2 &3-x \end{pmatrix} \begin{pmatrix} z_1 \\ z_2 \\ z_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$

has a non-$$\vec{0}$$ solution if and only if the matrix is singular. We can determine when that happens.

$$
\begin{array}{rl} 0 &=\left|T-x I\right| \\ &=\begin{vmatrix} 1-x &2 &1 \\ 2 &0-x &-2 \\ -1 &2 &3-x \end{vmatrix} \\ &=x^3-4x^2+4x \\ &=x(x-2)^2 \end{array}
$$

The eigenvalues are $$\lambda_1=0$$ and $$\lambda_2=2$$. To find the associated eigenvectors, plug in each eigenvalue. Plugging in $$\lambda_1=0$$ gives

$$
\begin{pmatrix} 1-0 &2 &1 \\ 2 &0-0 &-2 \\ -1 &2 &3-0 \end{pmatrix} \begin{pmatrix} z_1 \\ z_2 \\ z_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \qquad\Longrightarrow\qquad \begin{pmatrix} z_1 \\ z_2 \\ z_3 \end{pmatrix} = \begin{pmatrix} a \\ -a \\ a \end{pmatrix}
$$

for a scalar parameter $$a\neq 0$$ ($$a$$ is non-$$0$$ because eigenvectors must be non-$$\vec{0}$$). In the same way, plugging in $$\lambda_2=2$$ gives

$$
\begin{pmatrix} 1-2 &2 &1 \\ 2 &0-2 &-2 \\ -1 &2 &3-2 \end{pmatrix} \begin{pmatrix} z_1 \\ z_2 \\ z_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \qquad\Longrightarrow\qquad \begin{pmatrix} z_1 \\ z_2 \\ z_3 \end{pmatrix} = \begin{pmatrix} b \\ 0 \\ b \end{pmatrix}
$$

with $$b\neq 0$$.

**Example 3.8**  —

If

$$
S= \begin{pmatrix} \pi &1 \\ 0 &3 \end{pmatrix}
$$

(here $$\pi$$ is not a projection map, it is the number $$3.14\ldots$$) then

$$
\left| \begin{pmatrix} \pi-x &1 \\ 0 &3-x \end{pmatrix} \right| = (x-\pi)(x-3)
$$

so $$S$$ has eigenvalues of $$\lambda_1=\pi$$ and $$\lambda_2=3$$. To find associated eigenvectors, first plug in $$\lambda_1$$ for $$x$$:

$$
\begin{pmatrix} \pi-\pi &1 \\ 0 &3-\pi \end{pmatrix} \begin{pmatrix} z_1 \\ z_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \qquad\Longrightarrow\qquad \begin{pmatrix} z_1 \\ z_2 \end{pmatrix} = \begin{pmatrix} a \\ 0 \end{pmatrix}
$$

for a scalar $$a\neq 0$$, and then plug in $$\lambda_2$$:

$$
\begin{pmatrix} \pi-3 &1 \\ 0 &3-3 \end{pmatrix} \begin{pmatrix} z_1 \\ z_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \qquad\Longrightarrow\qquad \begin{pmatrix} z_1 \\ z_2 \end{pmatrix} = \begin{pmatrix} -b/(\pi-3) \\ b \end{pmatrix}
$$

where $$b\neq 0$$.

**Definition 3.9**  —

The **characteristic polynomial** of a square matrix $$T$$ is the determinant of the matrix $$T-x I$$, where $$x$$ is a variable. The **characteristic equation** is $$\left|T-xI\right|=0$$. The characteristic polynomial of a transformation $$t$$ is the polynomial of any $${\rm Rep}_{B,B}(t)$$.

Problem 11 checks that the characteristic polynomial of a transformation is well-defined, that is, any choice of basis yields the same polynomial.

**Lemma 3.10**  —

A linear transformation on a nontrivial vector space has at least one eigenvalue.

**Proof**  —

Any root of the characteristic polynomial is an eigenvalue. Over the complex numbers, any polynomial of degree one or greater has a root. (This is the reason that in this chapter we've gone to scalars that are complex.)

Notice the familiar form of the sets of eigenvectors in the above examples.

**Definition 3.11**  —

The **eigenspace** of a transformation $$t$$ associated with the eigenvalue $$\lambda$$ is $$V_\lambda=\{\vec{\zeta}\,\big|\, t(\vec{\zeta}\,)=\lambda\vec{\zeta}\,\} \cup\{\vec{0}\,\}$$. The eigenspace of a matrix is defined analogously.

**Lemma 3.12**  —

An eigenspace is a subspace.

**Proof**  —

An eigenspace must be nonempty— for one thing it contains the zero vector— and so we need only check closure. Take vectors $$\vec{\zeta}_1,\ldots,\vec{\zeta}_n$$ from $$V_\lambda$$, to show that any linear combination is in $$V_\lambda$$

$$
\begin{array}{rl} t(c_1\vec{\zeta}_1+c_2\vec{\zeta}_2+\cdots +c_n\vec{\zeta}_n) &=c_1t(\vec{\zeta}_1)+\dots+c_nt(\vec{\zeta}_n) \\ &=c_1\lambda\vec{\zeta}_1+\dots+c_n\lambda\vec{\zeta}_n \\ &=\lambda(c_1\vec{\zeta}_1+\dots+c_n\vec{\zeta}_n) \end{array}
$$

(the second equality holds even if any $$\vec{\zeta}_i$$ is $$\vec{0}$$ since $$t(\vec{0})=\lambda\cdot\vec{0}=\vec{0}$$).

**Example 3.13**  —

In Example 3.8 the eigenspace associated with the eigenvalue $$\pi$$ and the eigenspace associated with the eigenvalue $$3$$ are these.

$$
V_{\pi}=\{\begin{pmatrix} a \\ 0 \end{pmatrix}\,\big|\, a\in\mathbb{R}\} \qquad V_3=\{\begin{pmatrix} -b/\pi-3 \\ b \end{pmatrix}\,\big|\, b\in\mathbb{R}\}
$$

**Example 3.14**  —

In Example 3.7, these are the eigenspaces associated with the eigenvalues $$0$$ and $$2$$.

$$
V_0=\{\begin{pmatrix} a \\ -a \\ a \end{pmatrix}\,\big|\, a\in\mathbb{R}\}, \qquad V_2=\{\begin{pmatrix} b \\ 0 \\ b \end{pmatrix}\,\big|\, b\in\mathbb{R}\}.
$$

**Remark 3.15**  —

The characteristic equation is $$0=x(x-2)^2$$ so in some sense $$2$$ is an eigenvalue "twice". However there are not "twice" as many eigenvectors, in that the dimension of the eigenspace is one, not two. The next example shows a case where a number, $$1$$, is a double root of the characteristic equation and the dimension of the associated eigenspace is two.

**Example 3.16**  —

With respect to the standard bases, this matrix

$$
\begin{pmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &0 \end{pmatrix}
$$

represents projection.

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} \stackrel{\pi}{\longmapsto} \begin{pmatrix} x \\ y \\ 0 \end{pmatrix} \qquad x,y,z\in\mathbb{C}
$$

Its eigenspace associated with the eigenvalue $$0$$ and its eigenspace associated with the eigenvalue $$1$$ are easy to find.

$$
V_0=\{\begin{pmatrix} 0 \\ 0 \\ c_3 \end{pmatrix}\,\big|\, c_3\in\mathbb{C}\} \qquad V_1=\{\begin{pmatrix} c_1 \\ c_2 \\ 0 \end{pmatrix}\,\big|\, c_1,c_2\in\mathbb{C}\}
$$

By the lemma, if two eigenvectors $$\vec{v}_1$$ and $$\vec{v}_2$$ are associated with the same eigenvalue then any linear combination of those two is also an eigenvector associated with that same eigenvalue. But, if two eigenvectors $$\vec{v}_1$$ and $$\vec{v}_2$$ are associated with different eigenvalues then the sum $$\vec{v}_1+\vec{v}_2$$ need not be related to the eigenvalue of either one. In fact, just the opposite. If the eigenvalues are different then the eigenvectors are not linearly related.

**Theorem 3.17**  —

For any set of distinct eigenvalues of a map or matrix, a set of associated eigenvectors, one per eigenvalue, is linearly independent.

**Proof**  —

We will use induction on the number of eigenvalues. If there is no eigenvalue or only one eigenvalue then the set of associated eigenvectors is empty or is a singleton set with a non-$$\vec{0}$$ member, and in either case is linearly independent.

For induction, assume that the theorem is true for any set of $$k$$ distinct eigenvalues, suppose that $$\lambda_1,\dots,\lambda_{k+1}$$ are distinct eigenvalues, and let $$\vec{v}_1,\dots,\vec{v}_{k+1}$$ be associated eigenvectors. If $$c_1\vec{v}_1+\dots+c_k\vec{v}_k+c_{k+1}\vec{v}_{k+1}=\vec{0}$$ then after multiplying both sides of the displayed equation by $$\lambda_{k+1}$$, applying the map or matrix to both sides of the displayed equation, and subtracting the first result from the second, we have this.

$$
c_1(\lambda_{k+1}-\lambda_1)\vec{v}_1+\dots +c_k(\lambda_{k+1}-\lambda_k)\vec{v}_k +c_{k+1}(\lambda_{k+1}-\lambda_{k+1})\vec{v}_{k+1}=\vec{0}
$$

The induction hypothesis now applies: $$c_1(\lambda_{k+1}-\lambda_1)=0,\dots,c_k(\lambda_{k+1}-\lambda_k)=0$$. Thus, as all the eigenvalues are distinct, $$c_1,\,\dots,\,c_k$$ are all $$0$$. Finally, now $$c_{k+1}$$ must be $$0$$ because we are left with the equation $$\vec{v}_{k+1}\neq\vec{0}$$.

**Example 3.18**  —

The eigenvalues of

$$
\begin{pmatrix} 2 &-2 &2 \\ 0 &1 &1 \\ -4 &8 &3 \end{pmatrix}
$$

are distinct: $$\lambda_1=1$$, $$\lambda_2=2$$, and $$\lambda_3=3$$. A set of associated eigenvectors like

$$
\{ \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 9 \\ 4 \\ 4 \end{pmatrix}, \begin{pmatrix} 2 \\ 1 \\ 2 \end{pmatrix} \}
$$

is linearly independent.

**Corollary 3.19**  —

An $$n \! \times \! n$$ matrix with $$n$$ distinct eigenvalues is diagonalizable.

**Proof**  —

Form a basis of eigenvectors. Apply [Corollary 2.4](Linear%20Algebra%20-%20Diagonalizability.md).

### Exercises

**Problem 1**  —

For each, find the characteristic polynomial and the eigenvalues.

1. $$\begin{pmatrix} 10 &-9 \\ 4 &-2 \end{pmatrix}$$
2. $$\begin{pmatrix} 1 &2 \\ 4 &3 \end{pmatrix}$$
3. $$\begin{pmatrix} 0 &3 \\ 7 &0 \end{pmatrix}$$
4. $$\begin{pmatrix} 0 &0 \\ 0 &0 \end{pmatrix}$$
5. $$\begin{pmatrix} 1 &0 \\ 0 &1 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

For each matrix, find the characteristic equation, and the eigenvalues and associated eigenvectors.

1. $$\begin{pmatrix} 3 &0 \\ 8 &-1 \end{pmatrix}$$
2. $$\begin{pmatrix} 3 &2 \\ -1 &0 \end{pmatrix}$$

**Problem 3**  —

Find the characteristic equation, and the eigenvalues and associated eigenvectors for this matrix. *Hint.* The eigenvalues are complex.

$$
\begin{pmatrix} -2 &-1 \\ 5 &2 \end{pmatrix}
$$

**Problem 4**  —

Find the characteristic polynomial, the eigenvalues, and the associated eigenvectors of this matrix.

$$
\begin{pmatrix} 1 &1 &1 \\ 0 &0 &1 \\ 0 &0 &1 \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 5**  —

For each matrix, find the characteristic equation, and the eigenvalues and associated eigenvectors.

1. $$\begin{pmatrix} 3 &-2 &0 \\ -2 &3 &0 \\ 0 &0 &5 \end{pmatrix}$$
2. $$\begin{pmatrix} 0 &1 &0 \\ 0 &0 &1 \\ 4 &-17 &8 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 6**  —

Let $$t:\mathcal{P}_2\to \mathcal{P}_2$$ be

$$
a_0+a_1x+a_2x^2\mapsto (5a_0+6a_1+2a_2)-(a_1+8a_2)x+(a_0-2a_2)x^2.
$$

Find its eigenvalues and the associated eigenvectors.

**Problem 7**  —

Find the eigenvalues and eigenvectors of this map $$t:\mathcal{M}_2\to \mathcal{M}_2$$.

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \mapsto \begin{pmatrix} 2c &a+c \\ b-2c &d \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 8**  —

Find the eigenvalues and associated eigenvectors of the differentiation operator $$d/dx:\mathcal{P}_3\to \mathcal{P}_3$$.

**Problem 9**  — Prove that

the eigenvalues of a triangular matrix (upper or lower triangular) are the entries on the diagonal.  
*This exercise is recommended for all readers.*

**Problem 10**  —

Find the formula for the characteristic polynomial of a $$2 \! \times \! 2$$ matrix.

**Problem 11**  —

Prove that the characteristic polynomial of a transformation is well-defined.  
*This exercise is recommended for all readers.*

**Problem 12**  —

1. Can any non-$$\vec{0}$$ vector in any nontrivial vector space be a eigenvector? That is, given a $$\vec{v}\neq\vec{0}$$ from a nontrivial $$V$$, is there a transformation $$t:V\to V$$ and a scalar $$\lambda\in\mathbb{R}$$ such that $$t(\vec{v})=\lambda\vec{v}$$?
2. Given a scalar $$\lambda$$, can any non-$$\vec{0}$$ vector in any nontrivial vector space be an eigenvector associated with the eigenvalue $$\lambda$$?  
*This exercise is recommended for all readers.*

**Problem 13**  —

Suppose that $$t:V\to V$$ and $$T={\rm Rep}_{B,B}(t)$$. Prove that the eigenvectors of $$T$$ associated with $$\lambda$$ are the non-$$\vec{0}$$ vectors in the kernel of the map represented (with respect to the same bases) by $$T-\lambda I$$.

**Problem 14**  —

Prove that if $$a,\ldots,\,d$$ are all integers and $$a+b=c+d$$ then

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix}
$$

has integral eigenvalues, namely $$a+b$$ and $$a-c$$.  
*This exercise is recommended for all readers.*

**Problem 15**  —

Prove that if $$T$$ is nonsingular and has eigenvalues $$\lambda_1,\dots,\lambda_n$$ then $$T^{-1}$$ has eigenvalues $$1/\lambda_1,\dots,1/\lambda_n$$. Is the converse true?  
*This exercise is recommended for all readers.*

**Problem 16**  —

Suppose that $$T$$ is $$n \! \times \! n$$ and $$c,d$$ are scalars.

1. Prove that if $$T$$ has the eigenvalue $$\lambda$$ with an associated eigenvector $$\vec{v}$$ then $$\vec{v}$$ is an eigenvector of $$cT+dI$$ associated with eigenvalue $$c\lambda+d$$.
2. Prove that if $$T$$ is diagonalizable then so is $$cT+dI$$.  
*This exercise is recommended for all readers.*

**Problem 17**  —

Show that $$\lambda$$ is an eigenvalue of $$T$$ if and only if the map represented by $$T-\lambda I$$ is not an isomorphism.

**Problem 18**  —

1. Show that if $$\lambda$$ is an eigenvalue of $$A$$ then $$\lambda^k$$ is an eigenvalue of $$A^k$$.
2. What is wrong with this proof generalizing that? "If $$\lambda$$ is an eigenvalue of $$A$$ and $$\mu$$ is an eigenvalue for $$B$$, then $$\lambda\mu$$ is an eigenvalue for $$AB$$, for, if $$A\vec{x}=\lambda\vec{x}$$ and $$B\vec{x}=\mu\vec{x}$$ then $$AB\vec{x}=A\mu\vec{x}=\mu A\vec{x}=\mu\lambda\vec{x}$$"?

(Strang 1980)

**Problem 19**  —

Do matrix-equivalent matrices have the same eigenvalues?

**Problem 20**  —

Show that a square matrix with real entries and an odd number of rows has at least one real eigenvalue.

**Problem 21**  —

Diagonalize.

$$
\begin{pmatrix} -1 &2 &2 \\ 2 &2 &2 \\ -3 &-6 &-6 \end{pmatrix}
$$

**Problem 22**  —

Suppose that $$P$$ is a nonsingular $$n \! \times \! n$$ matrix. Show that the **similarity transformation** map $$t_P:\mathcal{M}_{n \! \times \! n}\to \mathcal{M}_{n \! \times \! n}$$ sending $$T\mapsto PTP^{-1}$$ is an isomorphism.

**? Problem 23**  —

Show that if $$A$$ is an $$n$$ square matrix and each row (column) sums to $$c$$ then $$c$$ is a characteristic root of $$A$$. (Morrison 1967)

Solutions

### References

- Morrison, Clarence C. (proposer) (1967), "Quickie", *Mathematics Magazine*, **40** (4): 232.
- Strang, Gilbert (1980), *Linear Algebra and its Applications* (Second ed.), Harcourt Brace Jovanovich.

---

*Source: Wikibooks, Linear Algebra/Eigenvalues and Eigenvectors (https://en.wikibooks.org/wiki/Linear_Algebra/Eigenvalues_and_Eigenvectors), by Wikibooks contributors, CC BY-SA 4.0.*
