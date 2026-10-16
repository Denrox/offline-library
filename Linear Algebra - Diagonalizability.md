# Diagonalizability

The prior subsection defines the relation of similarity and shows that, although similar matrices are necessarily matrix equivalent, the converse does not hold. Some matrix-equivalence classes break into two or more similarity classes (the nonsingular $$n \! \times \! n$$ matrices, for instance). This means that the canonical form for matrix equivalence, a block partial-identity, cannot be used as a canonical form for matrix similarity because the partial-identities cannot be in more than one similarity class, so there are similarity classes without one. This picture illustrates. As earlier in this book, class representatives are shown with stars.

We are developing a canonical form for representatives of the similarity classes. We naturally try to build on our previous work, meaning first that the partial identity matrices should represent the similarity classes into which they fall, and beyond that, that the representatives should be as simple as possible. The simplest extension of the partial-identity form is a diagonal form.

**Definition 2.1**  —

A transformation is **diagonalizable** if it has a diagonal representation with respect to the same basis for the codomain as for the domain. A **diagonalizable matrix** is one that is similar to a diagonal matrix: $$T$$ is diagonalizable if there is a nonsingular $$P$$ such that $$PTP^{-1}$$ is diagonal.

**Example 2.2**  —

The matrix

$$
\begin{pmatrix} 4 &-2 \\ 1 &1 \end{pmatrix}
$$

is diagonalizable.

$$
\begin{pmatrix} 2 &0 \\ 0 &3 \end{pmatrix} = \begin{pmatrix} -1 &2 \\ 1 &-1 \end{pmatrix} \begin{pmatrix} 4 &-2 \\ 1 &1 \end{pmatrix} \begin{pmatrix} -1 &2 \\ 1 &-1 \end{pmatrix}^{-1}
$$

**Example 2.3**  —

Not every matrix is diagonalizable. The square of

$$
N=\begin{pmatrix} 0 &0 \\ 1 &0 \end{pmatrix}
$$

is the zero matrix. Thus, for any map $$n$$ that $$N$$ represents (with respect to the same basis for the domain as for the codomain), the composition $$n\circ n$$ is the zero map. This implies that no such map $$n$$ can be diagonally represented (with respect to any $$B,B$$) because no power of a nonzero diagonal matrix is zero. That is, there is no diagonal matrix in $$N$$'s similarity class.

That example shows that a diagonal form will not do for a canonical form— we cannot find a diagonal matrix in each matrix similarity class. However, the canonical form that we are developing has the property that if a matrix can be diagonalized then the diagonal matrix is the canonical representative of the similarity class. The next result characterizes which maps can be diagonalized.

**Corollary 2.4**  —

A transformation $$t$$ is diagonalizable if and only if there is a basis $$B=\langle \vec{\beta}_1,\ldots,\vec{\beta}_n \rangle$$ and scalars $$\lambda_1,\ldots,\lambda_n$$ such that $$t(\vec{\beta}_i)=\lambda_i\vec{\beta}_i$$ for each $$i$$.

**Proof**  —

This follows from the definition by considering a diagonal representation matrix.

$$
{\rm Rep}_{B,B}(t)= \left(\begin{array}{c|c|c} \vdots & &\vdots \\ {\rm Rep}_{B}(t(\vec{\beta}_1)) &\cdots &{\rm Rep}_{B}(t(\vec{\beta}_n)) \\ \vdots & &\vdots \end{array}\right) = \left(\begin{array}{c|c|c} \lambda_1 & &0 \\ \vdots &\ddots &\vdots \\ 0 & &\lambda_n \end{array}\right)
$$

This representation is equivalent to the existence of a basis satisfying the stated conditions simply by the definition of matrix representation.

**Example 2.5**  —

To diagonalize

$$
T=\begin{pmatrix} 3 &2 \\ 0 &1 \end{pmatrix}
$$

we take it as the representation of a transformation with respect to the standard basis $$T={\rm Rep}_{\mathcal{E}_2,\mathcal{E}_2}(t)$$ and we look for a basis $$B=\langle \vec{\beta}_1,\vec{\beta}_2 \rangle$$ such that

$$
{\rm Rep}_{B,B}(t) = \begin{pmatrix} \lambda_1 &0 \\ 0 &\lambda_2 \end{pmatrix}
$$

that is, such that $$t(\vec{\beta}_1)=\lambda_1\vec{\beta}_1$$ and $$t(\vec{\beta}_2)=\lambda_2\vec{\beta}_2$$.

$$
\begin{pmatrix} 3 &2 \\ 0 &1 \end{pmatrix} \vec{\beta}_1=\lambda_1\cdot\vec{\beta}_1 \qquad \begin{pmatrix} 3 &2 \\ 0 &1 \end{pmatrix} \vec{\beta}_2=\lambda_2\cdot\vec{\beta}_2
$$

We are looking for scalars $$x$$ such that this equation

$$
\begin{pmatrix} 3 &2 \\ 0 &1 \end{pmatrix} \begin{pmatrix} b_1 \\ b_2 \end{pmatrix}=x\cdot\begin{pmatrix} b_1 \\ b_2 \end{pmatrix}
$$

has solutions $$b_1$$ and $$b_2$$, which are not both zero. Rewrite that as a linear system.

$$
\begin{array}{rcrcr} (3-x)\cdot b_1 &+ &2\cdot b_2 &= &0 \\ & &(1-x)\cdot b_2 &= &0 \end{array} \qquad (*)
$$

In the bottom equation the two numbers multiply to give zero only if at least one of them is zero so there are two possibilities, $$b_2=0$$ and $$x=1$$. In the $$b_2=0$$ possibility, the first equation gives that either $$b_1=0$$ or $$x=3$$. Since the case of both $$b_1=0$$ and $$b_2=0$$ is disallowed, we are left looking at the possibility of $$x=3$$. With it, the first equation in ($$*$$) is $$0\cdot b_1+2\cdot b_2=0$$ and so associated with $$3$$ are vectors with a second component of zero and a first component that is free.

$$
\begin{pmatrix} 3 &2 \\ 0 &1 \end{pmatrix} \begin{pmatrix} b_1 \\ 0 \end{pmatrix}=3\cdot\begin{pmatrix} b_1 \\ 0 \end{pmatrix}
$$

That is, one solution to ($$*$$) is $$\lambda_1=3$$, and we have a first basis vector.

$$
\vec{\beta}_1=\begin{pmatrix} 1 \\ 0 \end{pmatrix}
$$

In the $$x=1$$ possibility, the first equation in ($$*$$) is $$2\cdot b_1+2\cdot b_2=0$$, and so associated with $$1$$ are vectors whose second component is the negative of their first component.

$$
\begin{pmatrix} 3 &2 \\ 0 &1 \end{pmatrix} \begin{pmatrix} b_1 \\ -b_1 \end{pmatrix}=1\cdot\begin{pmatrix} b_1 \\ -b_1 \end{pmatrix}
$$

Thus, another solution is $$\lambda_2=1$$ and a second basis vector is this.

$$
\vec{\beta}_2=\begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

To finish, drawing the similarity diagram  
and noting that the matrix $${\rm Rep}_{B,\mathcal{E}_2}(\text{id})$$ is easy leads to this diagonalization.

$$
\begin{pmatrix} 3 &0 \\ 0 &1 \end{pmatrix} = \begin{pmatrix} 1 &1 \\ 0 &-1 \end{pmatrix}^{-1} \begin{pmatrix} 3 &2 \\ 0 &1 \end{pmatrix} \begin{pmatrix} 1 &1 \\ 0 &-1 \end{pmatrix}
$$

In the next subsection, we will expand on that example by considering more closely the property of Corollary 2.4. This includes seeing another way, the way that we will routinely use, to find the $$\lambda$$'s.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Repeat Example 2.5 for the matrix from Example 2.2.

**Problem 2**  —

Diagonalize these upper triangular matrices.

1. $$\begin{pmatrix} -2 &1 \\ 0 &2 \end{pmatrix}$$
2. $$\begin{pmatrix} 5 &4 \\ 0 &1 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

What form do the powers of a diagonal matrix have?

**Problem 4**  —

Give two same-sized diagonal matrices that are not similar. Must any two different diagonal matrices come from different similarity classes?

**Problem 5**  —

Give a nonsingular diagonal matrix. Can a diagonal matrix ever be singular?  
*This exercise is recommended for all readers.*

**Problem 6**  —

Show that the inverse of a diagonal matrix is the diagonal of the inverses, if no element on that diagonal is zero. What happens when a diagonal entry is zero?

**Problem 7**  —

The equation ending Example 2.5

$$
\begin{pmatrix} 1 &1 \\ 0 &-1 \end{pmatrix}^{-1} \begin{pmatrix} 3 &2 \\ 0 &1 \end{pmatrix} \begin{pmatrix} 1 &1 \\ 0 &-1 \end{pmatrix} = \begin{pmatrix} 3 &0 \\ 0 &1 \end{pmatrix}
$$

is a bit jarring because for $$P$$ we must take the first matrix, which is shown as an inverse, and for $$P^{-1}$$ we take the inverse of the first matrix, so that the two $$-1$$ powers cancel and this matrix is shown without a superscript $$-1$$.

1. Check that this nicer-appearing equation holds.

$$
\begin{pmatrix} 3 &0 \\ 0 &1 \end{pmatrix} = \begin{pmatrix} 1 &1 \\ 0 &-1 \end{pmatrix} \begin{pmatrix} 3 &2 \\ 0 &1 \end{pmatrix} \begin{pmatrix} 1 &1 \\ 0 &-1 \end{pmatrix}^{-1}
$$

2. Is the previous item a coincidence? Or can we always switch the $$P$$ and the $$P^{-1}$$?

**Problem 8**  —

Show that the $$P$$ used to diagonalize in Example 2.5 is not unique.

**Problem 9**  —

Find a formula for the powers of this matrix *Hint*: see Problem 3.

$$
\begin{pmatrix} -3 &1 \\ -4 &2 \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 10**  —

Diagonalize these.

1. $$\begin{pmatrix} 1 &1 \\ 0 &0 \end{pmatrix}$$
2. $$\begin{pmatrix} 0 &1 \\ 1 &0 \end{pmatrix}$$

**Problem 11**  —

We can ask how diagonalization interacts with the matrix operations. Assume that $$t,s:V\to V$$ are each diagonalizable. Is $$ct$$ diagonalizable for all scalars $$c$$? What about $$t+s$$? $$t\circ s$$?  
*This exercise is recommended for all readers.*

**Problem 12**  —

Show that matrices of this form are not diagonalizable.

$$
\begin{pmatrix} 1 &c \\ 0 &1 \end{pmatrix} \qquad c\neq 0
$$

**Problem 13**  —

Show that each of these is diagonalizable.

1. $$\begin{pmatrix} 1 &2 \\ 2 &1 \end{pmatrix}$$
2. $$\begin{pmatrix} x &y \\ y &z \end{pmatrix} \qquad x,y,z\text{ scalars}$$

Solutions

---

*Source: Wikibooks, Linear Algebra/Diagonalizability (https://en.wikibooks.org/wiki/Linear_Algebra/Diagonalizability), by Wikibooks contributors, CC BY-SA 4.0.*
