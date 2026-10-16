# Sums and Scalar Products

Recall that for two maps $$f$$ and $$g$$ with the same domain and codomain, the map sum $$f+g$$ has this definition.

$$
\vec{v} \;\stackrel{f+g}{\longmapsto}\; f(\vec{v})+g(\vec{v})
$$

The easiest way to see how the representations of the maps combine to represent the map sum is with an example.

**Example 1.1**  —

Suppose that $$f,g:\mathbb{R}^2\to \mathbb{R}^3$$ are represented with respect to the bases $$B$$ and $$D$$ by these matrices.

$$
F={\rm Rep}_{B,D}(f)= \begin{pmatrix} 1 &3 \\ 2 &0 \\ 1 &0 \end{pmatrix}_{B,D} \qquad G={\rm Rep}_{B,D}(g)= \begin{pmatrix} 0 &0 \\ -1 &-2 \\ 2 &4 \end{pmatrix}_{B,D}
$$

Then, for any $$\vec{v}\in V$$ represented with respect to $$B$$, computation of the representation of $$f(\vec{v})+g(\vec{v})$$

$$
\begin{pmatrix} 1 &3 \\ 2 &0 \\ 1 &0 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} + \begin{pmatrix} 0 &0 \\ -1 &-2 \\ 2 &4 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} =\begin{pmatrix} 1v_1+3v_2 \\ 2v_1+0v_2 \\ 1v_1+0v_2 \end{pmatrix} +\begin{pmatrix} 0v_1+0v_2 \\ -1v_1-2v_2 \\ 2v_1+4v_2 \end{pmatrix}
$$

gives this representation of $$f+g\,(\vec{v})$$.

$$
\begin{pmatrix} (1+0)v_1+(3+0)v_2 \\ (2-1)v_1+(0-2)v_2 \\ (1+2)v_1+(0+4)v_2 \end{pmatrix} =\begin{pmatrix} 1v_1+3v_2 \\ 1v_1-2v_2 \\ 3v_1+4v_2 \end{pmatrix}
$$

Thus, the action of $$f+g$$ is described by this matrix-vector product.

$$
\begin{pmatrix} 1 &3 \\ 1 &-2 \\ 3 &4 \end{pmatrix}_{B,D} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}_B =\begin{pmatrix} 1v_1+3v_2 \\ 1v_1-2v_2 \\ 3v_1+4v_2 \end{pmatrix}_D
$$

This matrix is the entry-by-entry sum of original matrices, e.g., the $$1,1$$ entry of $${\rm Rep}_{B,D}(f+g)$$ is the sum of the $$1,1$$ entry of $$F$$ and the $$1,1$$ entry of $$G$$.

Representing a scalar multiple of a map works the same way.

**Example 1.2**  —

If $$t$$ is a transformation represented by

$$
{\rm Rep}_{B,D}(t) = \begin{pmatrix} 1 &0 \\ 1 &1 \end{pmatrix}_{B,D} \quad\text{so that}\quad \vec{v}=\begin{pmatrix} v_1 \\ v_2 \end{pmatrix}_B\mapsto \begin{pmatrix} v_1 \\ v_1+v_2 \end{pmatrix}_D=t(\vec{v})
$$

then the scalar multiple map $$5t$$ acts in this way.

$$
\vec{v}=\begin{pmatrix} v_1 \\ v_2 \end{pmatrix}_B \;\longmapsto\; \begin{pmatrix} 5v_1 \\ 5v_1+5v_2 \end{pmatrix}_D=5\cdot t(\vec{v})
$$

Therefore, this is the matrix representing $$5t$$.

$$
{\rm Rep}_{B,D}(5t) = \begin{pmatrix} 5 &0 \\ 5 &5 \end{pmatrix}_{B,D}
$$

**Definition 1.3**  —

The **sum** of two same-sized matrices is their entry-by-entry sum. The **scalar multiple** of a matrix is the result of entry-by-entry scalar multiplication.

**Remark 1.4**  —

These extend the vector addition and scalar multiplication operations that we defined in the first chapter.

**Theorem 1.5**  —

Let $$h,g:V\to W$$ be linear maps represented with respect to bases $$B,D$$ by the matrices $$H$$ and $$G$$, and let $$r$$ be a scalar. Then the map $$h+g:V\to W$$ is represented with respect to $$B,D$$ by $$H+G$$, and the map $$r\cdot h:V\to W$$ is represented with respect to $$B,D$$ by $$rH$$.

**Proof**  —

Problem 2; generalize the examples above.

A notable special case of scalar multiplication is multiplication by zero. For any map $$0\cdot h$$ is the zero homomorphism and for any matrix $$0\cdot H$$ is the zero matrix.

**Example 1.6**  —

The zero map from any three-dimensional space to any two-dimensional space is represented by the $$2 \! \times \! 3$$ zero matrix

$$
Z=\begin{pmatrix} 0 &0 &0 \\ 0 &0 &0 \end{pmatrix}
$$

no matter which domain and codomain bases are used.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Perform the indicated operations, if defined.

1. $$\begin{pmatrix} 5 &-1 &2 \\ 6 &1 &1 \end{pmatrix} + \begin{pmatrix} 2 &1 &4 \\ 3 &0 &5 \end{pmatrix}$$
2. $$6\cdot\begin{pmatrix} 2 &-1 &-1 \\ 1 &2 &3 \end{pmatrix}$$
3. $$\begin{pmatrix} 2 &1 \\ 0 &3 \end{pmatrix} + \begin{pmatrix} 2 &1 \\ 0 &3 \end{pmatrix}$$
4. $$4\begin{pmatrix} 1 &2 \\ 3 &-1 \end{pmatrix} + 5\begin{pmatrix} -1 &4 \\ -2 &1 \end{pmatrix}$$
5. $$3\begin{pmatrix} 2 &1 \\ 3 &0 \end{pmatrix} +2 \begin{pmatrix} 1 &1 &4 \\ 3 &0 &5 \end{pmatrix}$$

**Problem 2**  —

Prove Theorem 1.5.

1. Prove that matrix addition represents addition of linear maps.
2. Prove that matrix scalar multiplication represents scalar multiplication of linear maps.  
*This exercise is recommended for all readers.*

**Problem 3**  —

Prove each, where the operations are defined, where $$G$$, $$H$$, and $$J$$ are matrices, where $$Z$$ is the zero matrix, and where $$r$$ and $$s$$ are scalars.

1. Matrix addition is commutative $$G+H=H+G$$.
2. Matrix addition is associative $$G+(H+J)=(G+H)+J$$.
3. The zero matrix is an additive identity $$G+Z=G$$.
4. $$0\cdot G=Z$$
5. $$(r+s)G=rG+sG$$
6. Matrices have an additive inverse $$G+(-1)\cdot G=Z$$.
7. $$r(G+H)=rG+rH$$
8. $$(rs)G=r(sG)$$

**Problem 4**  —

Fix domain and codomain spaces. In general, one matrix can represent many different maps with respect to different bases. However, prove that a zero matrix represents only a zero map. Are there other such matrices?  
*This exercise is recommended for all readers.*

**Problem 5**  —

Let $$V$$ and $$W$$ be vector spaces of dimensions $$n$$ and $$m$$. Show that the space $$\mathop{\mathcal L}(V,W)$$ of linear maps from $$V$$ to $$W$$ is isomorphic to $$\mathcal{M}_{m \! \times \! n}$$.  
*This exercise is recommended for all readers.*

**Problem 6**  —

Show that it follows from the prior questions that for any six transformations $$t_1,\dots,t_6:\mathbb{R}^2\to \mathbb{R}^2$$ there are scalars $$c_1,\dots,c_6\in\mathbb{R}$$ such that $$c_1t_1+\dots+c_6t_6$$ is the zero map. (*Hint:* this is a bit of a misleading question.)

**Problem 7**  —

The **trace** of a square matrix is the sum of the entries on the main diagonal (the $$1,1$$ entry plus the $$2,2$$ entry, etc.; we will see the significance of the trace in Chapter Five). Show that $$\text{trace}(H+G)=\text{trace}(H)+\text{trace}(G)$$. Is there a similar result for scalar multiplication?

**Problem 8**  —

Recall that the **transpose** of a matrix $$M$$ is another matrix, whose $$i,j$$ entry is the $$j,i$$ entry of $$M$$. Verifiy these identities.

1. $${{(G+H)}^{\rm trans}}={{G}^{\rm trans}}+{{H}^{\rm trans}}$$
2. $${{(r\cdot H)}^{\rm trans}}=r\cdot{{H}^{\rm trans}}$$  
*This exercise is recommended for all readers.*

**Problem 9**  —

A square matrix is **symmetric** if each $$i,j$$ entry equals the $$j,i$$ entry, that is, if the matrix equals its transpose.

1. Prove that for any $$H$$, the matrix $$H+{{H}^{\rm trans}}$$ is symmetric. Does every symmetric matrix have this form?
2. Prove that the set of $$n \! \times \! n$$ symmetric matrices is a subspace of $$\mathcal{M}_{n \! \times \! n}$$.  
*This exercise is recommended for all readers.*

**Problem 10**  —

1. How does matrix rank interact with scalar multiplication— can a scalar product of a rank $$n$$ matrix have rank less than $$n$$? Greater?
2. How does matrix rank interact with matrix addition— can a sum of rank $$n$$ matrices have rank less than $$n$$? Greater?

Solutions

---

*Source: Wikibooks, Linear Algebra/Sums and Scalar Products (https://en.wikibooks.org/wiki/Linear_Algebra/Sums_and_Scalar_Products), by Wikibooks contributors, CC BY-SA 4.0.*
