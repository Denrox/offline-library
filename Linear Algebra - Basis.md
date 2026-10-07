# Basis

**Definition 1.1**  —

A **basis** for a vector space is a sequence of vectors that form a set that is linearly independent and that spans the space.

We denote a basis with angle brackets $$\langle\vec{\beta_1},\vec{\beta_2},\dots\rangle$$ to signify that this collection is a sequence — the order of the elements is significant. (The requirement that a basis be ordered will be needed, for instance, in Definition 1.13.)

**Example 1.2**  —

This is a basis for $$\R^2$$ .

$$
\langle\begin{pmatrix}2\\4\end{pmatrix},\begin{pmatrix}1\\1\end{pmatrix}\rangle
$$

It is linearly independent

$$
c_1\begin{pmatrix}2\\4\end{pmatrix}+c_2\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix} \quad\implies\quad \begin{array}{rcrcr} 2c_1 &+ &1c_2 &= &0 \\ 4c_1 &+ &1c_2 &= &0 \end{array} \quad\implies\quad c_1=c_2=0
$$

and it spans $$\R^2$$ .

$$
\begin{array}{rcrcr} 2c_1 &+ &1c_2 &= &x \\ 4c_1 &+ &1c_2 &= &y \end{array} \quad\implies\quad c_2=2x-y\text{ and } c_1=\frac{y-x}{2}
$$

**Example 1.3**  —

This basis for $$\R^2$$

$$
\langle\begin{pmatrix}1\\1\end{pmatrix},\begin{pmatrix}2\\4\end{pmatrix}\rangle
$$

differs from the prior one because the vectors are in a different order. The verification that it is a basis is just as in the prior example.

**Example 1.4**  —

The space $$\R^2$$ has many bases. Another one is this.

$$
\langle\begin{pmatrix}1\\0\end{pmatrix},\begin{pmatrix}0\\1\end{pmatrix}\rangle
$$

The verification is easy.

**Definition 1.5**  —

For any $$\R^n$$ ,

$$
\mathcal{E}_n=\langle \begin{pmatrix}1\\0\\ \vdots\\0\end{pmatrix}, \begin{pmatrix}0\\1\\ \vdots\\0\end{pmatrix}, \dots,\, \begin{pmatrix}0\\0\\ \vdots\\1\end{pmatrix} \rangle
$$

is the **standard** (or **natural**) basis. We denote these vectors by $$\vec{e_1},\dots,\vec{e_n}$$ .  
(Calculus books refer to $$\mathbb{R}^2$$'s standard basis vectors $$\vec{\imath}$$ and $$\vec{\jmath}$$ instead of $$\vec{e}_1$$ and $$\vec{e}_2$$, and they refer to $$\mathbb{R}^3$$'s standard basis vectors $$\vec{\imath}$$, $$\vec{\jmath}$$, and $$\vec{k}$$ instead of $$\vec{e}_1$$, $$\vec{e}_2$$, and $$\vec{e}_3$$.) Note that the symbol "$$\vec{e}_1$$" means something different in a discussion of $$\mathbb{R}^3$$ than it means in a discussion of $$\mathbb{R}^2$$.

**Example 1.6**  —

Consider the space $$\{a\cdot\cos\theta+b\cdot\sin\theta\,\big|\, a,b\in\mathbb{R}\}$$ of functions of the real variable $$\theta$$.

$$
\langle 1\cdot\cos\theta+0\cdot\sin\theta, 0\cdot\cos\theta+1\cdot\sin\theta \rangle =\langle \cos\theta, \sin\theta \rangle
$$

Another basis is $$\langle \cos\theta-\sin\theta, 2\cos\theta+3\sin\theta \rangle$$. Verification that these two are bases is Problem 7.

**Example 1.7**  —

A natural for the vector space of cubic polynomials $$\mathcal{P}_3$$ is $$\langle 1,x,x^2,x^3 \rangle$$. Two other bases for this space are $$\langle x^3,3x^2,6x,6 \rangle$$ and $$\langle 1,1+x,1+x+x^2,1+x+x^2+x^3 \rangle$$. Checking that these are linearly independent and span the space is easy.

**Example 1.8**  —

The trivial space $$\{\vec{0}\}$$ has only one basis, the empty one $$\langle \rangle$$.

**Example 1.9**  —

The space of finite-degree polynomials has a basis with infinitely many elements $$\langle 1,x,x^2,\ldots \rangle$$.

**Example 1.10**  —

We have seen bases before. In the first chapter we described the solution set of homogeneous systems such as this one

$$
\begin{array}{rcrcrcrcr} x &+ &y & & &- &w &= &0 \\ & & & &z &+ &w &= &0 \end{array}
$$

by parametrizing.

$$
\{\begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \end{pmatrix}y +\begin{pmatrix} 1 \\ 0 \\ -1 \\ 1 \end{pmatrix}w \,\big|\, y,w\in\mathbb{R} \}
$$

That is, we described the vector space of solutions as the span of a two-element set. We can easily check that this two-vector set is also linearly independent. Thus the solution set is a subspace of $$\mathbb{R}^4$$ with a two-element basis.

**Example 1.11**  —

Parameterization helps find bases for other vector spaces, not just for solution sets of homogeneous systems. To find a basis for this subspace of $$\mathcal{M}_{2 \! \times \! 2}$$

$$
\{\begin{pmatrix} a &b \\ c &0 \end{pmatrix} \,\big|\, a+b-2c=0\}
$$

we rewrite the condition as $$a=-b+2c$$.

$$
\{\begin{pmatrix} -b+2c &b \\ c &0 \end{pmatrix} \,\big|\, b,c \in \mathbb{R}\} =\{b\begin{pmatrix} -1 &1 \\ 0 &0 \end{pmatrix}+ c\begin{pmatrix} 2 &0 \\ 1 &0 \end{pmatrix} \,\big|\, b,c \in \mathbb{R}\}
$$

Thus, this is a good candidate for a basis.

$$
\langle \begin{pmatrix} -1 &1 \\ 0 &0 \end{pmatrix}, \begin{pmatrix} 2 &0 \\ 1 &0 \end{pmatrix} \rangle
$$

The above work shows that it spans the space. To show that it is linearly independent is routine.

Consider again Example 1.2. It involves two verifications.

In the first, to check that the set is linearly independent we looked at linear combinations of the set's members that total to the zero vector $$c_1\vec{\beta}_1+c_2\vec{\beta}_2=\binom{0}{0}$$. The resulting calculation shows that such a combination is unique, that $$c_1$$ must be $$0$$ and $$c_2$$ must be $$0$$.

The second verification, that the set spans the space, looks at linear combinations that total to any member of the space $$c_1\vec{\beta}_1+c_2\vec{\beta}_2=\binom{x}{y}$$. In Example 1.2 we noted only that the resulting calculation shows that such a combination exists, that for each $$x,y$$ there is a $$c_1,c_2$$. However, in fact the calculation also shows that the combination is unique: $$c_1$$ must be $$(y-x)/2$$ and $$c_2$$ must be $$2x-y$$.

That is, the first calculation is a special case of the second. The next result says that this holds in general for a spanning set: the combination totaling to the zero vector is unique if and only if the combination totaling to any vector is unique.

**Theorem 1.12**  —

In any vector space, a subset is a basis if and only if each vector in the space can be expressed as a linear combination of elements of the subset in a unique way.

We consider combinations to be the same if they differ only in the order of summands or in the addition or deletion of terms of the form "$$0\cdot\vec{\beta}$$".

**Proof**  —

By definition, a sequence is a basis if and only if its vectors form both a spanning set and a linearly independent set. A subset is a spanning set if and only if each vector in the space is a linear combination of elements of that subset in at least one way.

Thus, to finish we need only show that a subset is linearly independent if and only if every vector in the space is a linear combination of elements from the subset in at most one way. Consider two expressions of a vector as a linear combination of the members of the basis. We can rearrange the two sums, and if necessary add some $$0\vec{\beta}_i$$ terms, so that the two sums combine the same $$\vec{\beta}$$'s in the same order: $$\vec{v}=c_1\vec{\beta}_1+c_2\vec{\beta}_2+\cdots +c_n\vec{\beta}_n$$ and $$\vec{v}=d_1\vec{\beta}_1+d_2\vec{\beta}_2+\cdots +d_n\vec{\beta}_n$$. Now

$$
c_1\vec{\beta}_1+c_2\vec{\beta}_2+\cdots +c_n\vec{\beta}_n=d_1\vec{\beta}_1+d_2\vec{\beta}_2+\cdots +d_n\vec{\beta}_n
$$

holds if and only if

$$
(c_1-d_1)\vec{\beta}_1+\dots+(c_n-d_n)\vec{\beta}_n=\vec{0}
$$

holds, and so asserting that each coefficient in the lower equation is zero is the same thing as asserting that $$c_i=d_i$$ for each $$i$$.

**Definition 1.13**  —

In a vector space with basis $$B$$ the **representation of $$\vec{v}$$ with respect to $$B$$** is the column vector of the coefficients used to express $$\vec{v}$$ as a linear combination of the basis vectors:

$$
{\rm Rep}_{B}(\vec{v})= \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix}
$$

where $$B=\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ and $$\vec{v}=c_1\vec{\beta}_1+c_2\vec{\beta}_2+\cdots +c_n\vec{\beta}_n$$. The $$c$$'s are the **coordinates of $$\vec{v}$$ with respect to $$B$$**

We will later do representations in contexts that involve more than one basis. To help with the bookkeeping, we shall often attach a subscript $$B$$ to the column vector.

**Example 1.14**  —

In $$\mathcal{P}_3$$, with respect to the basis $$B=\langle 1,2x,2x^2,2x^3 \rangle$$, the representation of $$x+x^2$$ is

$$
{\rm Rep}_{B}(x+x^2)=\begin{pmatrix} 0 \\ 1/2 \\ 1/2 \\ 0 \end{pmatrix}_B
$$

(note that the coordinates are scalars, not vectors). With respect to a different basis $$D=\langle 1+x,1-x,x+x^2,x+x^3 \rangle$$, the representation

$$
{\rm Rep}_{D}(x+x^2)=\begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}_D
$$

is different.

**Remark 1.15**  —

This use of column notation and the term "coordinates" has both a down side and an up side.

The down side is that representations look like vectors from $$\mathbb{R}^n$$, which can be confusing when the vector space we are working with is $$\mathbb{R}^n$$, especially since we sometimes omit the subscript base. We must then infer the intent from the context. For example, the phrase "in $$\mathbb{R}^2$$, where $$\vec{v}=\binom{3}{2}$$" refers to the plane vector that, when in canonical position, ends at $$(3,2)$$. To find the coordinates of that vector with respect to the basis

$$
B=\langle \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 2 \end{pmatrix} \rangle
$$

we solve

$$
c_1\begin{pmatrix} 1 \\ 1 \end{pmatrix} +c_2\begin{pmatrix} 0 \\ 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}
$$

to get that $$c_1=3$$ and $$c_2=-1/2$$. Then we have this.

$$
{\rm Rep}_{B}(\vec{v})=\begin{pmatrix} 3 \\ -1/2 \end{pmatrix}
$$

Here, although we've ommited the subscript $$B$$ from the column, the fact that the right side is a representation is clear from the context.

The up side of the notation and the term "coordinates" is that they generalize the use that we are familiar with:~in $$\mathbb{R}^n$$ and with respect to the standard basis $$\mathcal{E}_n$$, the vector starting at the origin and ending at $$(v_1,\dots,v_n)$$ has this representation.  

$$
{\rm Rep}_{\mathcal{E}_n}(\begin{pmatrix} v_1 \\ \vdots \\ v_n \end{pmatrix}) = \begin{pmatrix} v_1 \\ \vdots \\ v_n \end{pmatrix}_{\mathcal{E}_n}
$$

Our main use of representations will come in the third chapter. The definition appears here because the fact that every vector is a linear combination of basis vectors in a unique way is a crucial property of bases, and also to help make two points. First, we fix an order for the elements of a basis so that coordinates can be stated in that order. Second, for calculation of coordinates, among other things, we shall restrict our attention to spaces with bases having only finitely many elements. We will see that in the next subsection.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Decide if each is a basis for $$\mathbb{R}^3$$.

1. $$\langle \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}, \begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \rangle$$
2. $$\langle \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}, \begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix} \rangle$$
3. $$\langle \begin{pmatrix} 0 \\ 2 \\ -1 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 2 \\ 5 \\ 0 \end{pmatrix} \rangle$$
4. $$\langle \begin{pmatrix} 0 \\ 2 \\ -1 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix} \rangle$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Represent the vector with respect to the basis.

1. $$\begin{pmatrix} 1 \\ 2 \end{pmatrix}$$, $$B=\langle \begin{pmatrix} 1 \\ 1 \end{pmatrix},\begin{pmatrix} -1 \\ 1 \end{pmatrix} \rangle \subseteq\mathbb{R}^2$$
2. $$x^2+x^3$$, $$D=\langle 1,1+x,1+x+x^2,1+x+x^2+x^3 \rangle \subseteq\mathcal{P}_3$$
3. $$\begin{pmatrix} 0 \\ -1 \\ 0 \\ 1 \end{pmatrix}$$, $$\mathcal{E}_4\subseteq\mathbb{R}^4$$

**Problem 3**  —

Find a basis for $$\mathcal{P}_2$$, the space of all quadratic polynomials. Must any such basis contain a polynomial of each degree:~degree zero, degree one, and degree two?

**Problem 4**  —

Find a basis for the solution set of this system.

$$
\begin{array}{rcrcrcrcr} x_1 &- &4x_2 &+ &3x_3 &- &x_4 &= &0 \\ 2x_1 &- &8x_2 &+ &6x_3 &- &2x_4 &= &0 \end{array}
$$

*This exercise is recommended for all readers.*

**Problem 5**  —

Find a basis for $$\mathcal{M}_{2 \! \times \! 2}$$, the space of $$2 \! \times \! 2$$ matrices.  
*This exercise is recommended for all readers.*

**Problem 6**  —

Find a basis for each.

1. The subspace $$\{a_2x^2+a_1x+a_0\,\big|\, a_2-2a_1=a_0\}$$ of $$\mathcal{P}_2$$
2. The space of three-wide row vectors whose first and second components add to zero
3. This subspace of the $$2 \! \times \! 2$$ matrices

$$
\{\begin{pmatrix} a &b \\ 0 &c \end{pmatrix} \,\big|\, c-2b=0\}
$$

**Problem 7**  —

Check Example 1.6.  
*This exercise is recommended for all readers.*

**Problem 8**  —

Find the span of each set and then find a basis for that span.

1. $$\{1+x,1+2x\}$$ in $$\mathcal{P}_2$$
2. $$\{2-2x,3+4x^2\}$$ in $$\mathcal{P}_2$$  
*This exercise is recommended for all readers.*

**Problem 9**  —

Find a basis for each of these subspaces of the space $$\mathcal{P}_3$$ of cubic polynomials.

1. The subspace of cubic polynomials $$p(x)$$ such that $$p(7)=0$$
2. The subspace of polynomials $$p(x)$$ such that $$p(7)=0$$ and $$p(5)=0$$
3. The subspace of polynomials $$p(x)$$ such that $$p(7)=0$$, $$p(5)=0$$, and~$$p(3)=0$$
4. The space of polynomials $$p(x)$$ such that $$p(7)=0$$, $$p(5)=0$$, $$p(3)=0$$, and~$$p(1)=0$$

**Problem 10**  —

We've seen that it is possible for a basis to remain a basis when it is reordered. Must it *always* remain a basis?

**Problem 11**  —

Can a basis contain a zero vector?  
*This exercise is recommended for all readers.*

**Problem 12**  —

Let $$\langle \vec{\beta}_1,\vec{\beta}_2,\vec{\beta}_3 \rangle$$ be a basis for a vector space.

1. Show that $$\langle c_1\vec{\beta}_1,c_2\vec{\beta}_2,c_3\vec{\beta}_3 \rangle$$ is a basis when $$c_1, c_2, c_3\neq 0$$. What happens when at least one $$c_i$$ is $$0$$?
2. Prove that $$\langle \vec{\alpha}_1,\vec{\alpha}_2,\vec{\alpha}_3 \rangle$$ is a basis where $$\vec{\alpha}_i=\vec{\beta}_1+\vec{\beta}_i$$.

**Problem 13**  —

Find one vector $$\vec{v}$$ that will make each into a basis for the space.

1. $$\langle \begin{pmatrix} 1 \\ 1 \end{pmatrix},\vec{v} \rangle$$ in $$\mathbb{R}^2$$
2. $$\langle \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix},\vec{v} \rangle$$ in $$\mathbb{R}^3$$
3. $$\langle x,1+x^2,\vec{v} \rangle$$ in $$\mathcal{P}_2$$  
*This exercise is recommended for all readers.*

**Problem 14**  —

Where $$\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ is a basis, show that in this equation

$$
c_1\vec{\beta}_1+\dots+c_k\vec{\beta}_k = c_{k+1}\vec{\beta}_{k+1}+\dots+c_n\vec{\beta}_n
$$

each of the $$c_i$$'s is zero. Generalize.

**Problem 15**  —

A basis contains some of the vectors from a vector space; can it contain them all?

**Problem 16**  —

Theorem 1.12 shows that, with respect to a basis, every linear combination is unique. If a subset is not a basis, can linear combinations be not unique? If so, must they be?  
*This exercise is recommended for all readers.*

**Problem 17**  —

A square matrix is **symmetric** if for all indices $$i$$ and $$j$$, entry $$i,j$$ equals entry $$j,i$$.

1. Find a basis for the vector space of symmetric $$2 \! \times \! 2$$ matrices.
2. Find a basis for the space of symmetric $$3 \! \times \! 3$$ matrices.
3. Find a basis for the space of symmetric $$n \! \times \! n$$ matrices.  
*This exercise is recommended for all readers.*

**Problem 18**  —

We can show that every basis for $$\mathbb{R}^3$$ contains the same number of vectors.

1. Show that no linearly independent subset of $$\mathbb{R}^3$$ contains more than three vectors.
2. Show that no spanning subset of $$\mathbb{R}^3$$ contains fewer than three vectors. (*Hint.* Recall how to calculate the span of a set and show that this method, when applied to two vectors, cannot yield all of $$\mathbb{R}^3$$.)

**Problem 19**  —

One of the exercises in the Subspaces subsection shows that the set

$$
\{\begin{pmatrix} x \\ y \\ z \end{pmatrix}\,\big|\, x+y+z=1\}
$$

is a vector space under these operations.

$$
\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}+\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} =\begin{pmatrix} x_1+x_2-1 \\ y_1+y_2 \\ z_1+z_2 \end{pmatrix} \qquad r\begin{pmatrix} x \\ y \\ z \end{pmatrix}=\begin{pmatrix} rx-r+1 \\ ry \\ rz \end{pmatrix}
$$

Find a basis.

Solutions

### Footnotes

---

*Source: Wikibooks, Linear Algebra/Basis (https://en.wikibooks.org/wiki/Linear_Algebra/Basis), by Wikibooks contributors, CC BY-SA 4.0.*
