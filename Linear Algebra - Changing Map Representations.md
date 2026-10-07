# Changing Map Representations

The first subsection shows how to convert the representation of a vector with respect to one basis to the representation of that same vector with respect to another basis. Here we will see how to convert the representation of a map with respect to one pair of bases to the representation of that map with respect to a different pair. That is, we want the relationship between the matrices in this arrow diagram.  
To move from the lower-left of this diagram to the lower-right we can either go straight over, or else up to $$V_B$$ then over to $$W_D$$ and then down. Restated in terms of the matrices, we can calculate $$\hat{H}={\rm Rep}_{\hat{B},\hat{D}}(h)$$ either by simply using $$\hat{B}$$ and $$\hat{D}$$, or else by first changing bases with $${\rm Rep}_{\hat{B},B}(\text{id})$$ then multiplying by $$H={\rm Rep}_{B,D}(h)$$ and then changing bases with $${\rm Rep}_{D,\hat{D}}(\text{id})$$. This equation summarizes.

$$
\hat{H}= {\rm Rep}_{D,\hat{D}}(\text{id})\cdot H\cdot {\rm Rep}_{\hat{B},B}(\text{id}) \qquad\qquad(*)
$$

(To compare this equation with the sentence before it, remember that the equation is read from right to left because function composition is read right to left and matrix multiplication represent the composition.)

**Example 2.1**  —

The matrix

$$
T=\begin{pmatrix} \cos(\pi/6) &-\sin(\pi/6) \\ \sin(\pi/6) &\cos(\pi/6) \end{pmatrix} = \begin{pmatrix} \sqrt{3}/2 &-1/2 \\ 1/2 &\sqrt{3}/2 \end{pmatrix}
$$

represents, with respect to $$\mathcal{E}_2,\mathcal{E}_2$$, the transformation $$t:\mathbb{R}^2\to \mathbb{R}^2$$ that rotates vectors $$\pi/6$$ radians counterclockwise.

We can translate that representation with respect to $$\mathcal{E}_2,\mathcal{E}_2$$ to one with respect to

$$
\hat{B}=\langle \begin{pmatrix} 1 \\ 1 \end{pmatrix} \begin{pmatrix} 0 \\ 2 \end{pmatrix} \rangle \qquad \hat{D}=\langle \begin{pmatrix} -1 \\ 0 \end{pmatrix} \begin{pmatrix} 2 \\ 3 \end{pmatrix} \rangle
$$

by using the arrow diagram and formula ($$*$$) above.  
From this, we can use the formula:

$$
\hat{T}= {\rm Rep}_{\mathcal{E}_2,\hat{D}}(\text{id})\cdot T\cdot {\rm Rep}_{\hat{B},\mathcal{E}_2}(\text{id})
$$

Note that $${\rm Rep}_{\mathcal{E}_2,\hat{D}}(\text{id})$$ can be calculated as the matrix inverse of $${\rm Rep}_{\hat{D},\mathcal{E}_2}(\text{id})$$.

$$
\begin{array}{rl} {\rm Rep}_{\hat{B},\hat{D}}(t) &=\begin{pmatrix} -1 &2 \\ 0 &3 \end{pmatrix}^{-1} \begin{pmatrix} \sqrt{3}/2 &-1/2 \\ 1/2 &\sqrt{3}/2 \end{pmatrix} \begin{pmatrix} 1 &0 \\ 1 &2 \end{pmatrix} \\ &=\begin{pmatrix} (5-\sqrt{3})/6 &(3+2\sqrt{3})/3 \\ (1+\sqrt{3})/6 &\sqrt{3}/3 \end{pmatrix} \end{array}
$$

Although the new matrix is messier-appearing, the map that it represents is the same. For instance, to replicate the effect of $$t$$ in the picture, start with $$\hat{B}$$,

$$
{\rm Rep}_{\hat{B}}(\begin{pmatrix} 1 \\ 3 \end{pmatrix})=\begin{pmatrix} 1 \\ 1 \end{pmatrix}_{\hat{B}}
$$

apply $$\hat{T}$$,

$$
\begin{pmatrix} (5-\sqrt{3})/6 &(3+2\sqrt{3})/3 \\ (1+\sqrt{3})/6 &\sqrt{3}/3 \end{pmatrix}_{\hat{B},\hat{D}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}_{\hat{B}} = \begin{pmatrix} (11+3\sqrt{3})/6 \\ (1+3\sqrt{3})/6 \end{pmatrix}_{\hat{D}}
$$

and check it against $$\hat{D}$$

$$
\frac{11+3\sqrt{3}}{6}\cdot\begin{pmatrix} -1 \\ 0 \end{pmatrix} +\frac{1+3\sqrt{3}}{6}\cdot\begin{pmatrix} 2 \\ 3 \end{pmatrix} =\begin{pmatrix} (-3+\sqrt{3})/2 \\ (1+3\sqrt{3})/2 \end{pmatrix}
$$

to see that it is the same result as above.

**Example 2.2**  —

On $$\mathbb{R}^3$$ the map

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix}\stackrel{t}{\longmapsto}\begin{pmatrix} y+z \\ x+z \\ x+y \end{pmatrix}
$$

that is represented with respect to the standard basis in this way

$$
{\rm Rep}_{\mathcal{E}_3,\mathcal{E}_3}(t)= \begin{pmatrix} 0 &1 &1 \\ 1 &0 &1 \\ 1 &1 &0 \end{pmatrix}
$$

can also be represented with respect to another basis

if $$B=\langle \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ -2 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \rangle$$ then $${\rm Rep}_{B,B}(t)= \begin{pmatrix} -1 &0 &0 \\ 0 &-1 &0 \\ 0 &0 &2 \end{pmatrix}$$

in a way that is simpler, in that the action of a diagonal matrix is easy to understand.

Naturally, we usually prefer basis changes that make the representation easier to understand. When the representation with respect to equal starting and ending bases is a diagonal matrix we say the map or matrix has been **diagonalized**. In Chaper Five we shall see which maps and matrices are diagonalizable, and where one is not, we shall see how to get a representation that is nearly diagonal.

We finish this subsection by considering the easier case where representations are with respect to possibly different starting and ending bases. Recall that the prior subsection shows that a matrix changes bases if and only if it is nonsingular. That gives us another version of the above arrow diagram and equation ($$*$$).

**Definition 2.3**  —

Same-sized matrices $$H$$ and $$\hat{H}$$ are **matrix equivalent** if there are nonsingular matrices $$P$$ and $$Q$$ such that $$\hat{H}=PHQ$$.

**Corollary 2.4**  —

Matrix equivalent matrices represent the same map, with respect to appropriate pairs of bases.

Problem 10 checks that matrix equivalence is an equivalence relation. Thus it partitions the set of matrices into matrix equivalence classes.

- All matrices:     $$H$$ matrix equivalent  
to $$\hat{H}$$

We can get some insight into the classes by comparing matrix equivalence with row equivalence (recall that matrices are row equivalent when they can be reduced to each other by row operations). In $$\hat{H}=PHQ$$, the matrices $$P$$ and $$Q$$ are nonsingular and thus each can be written as a product of elementary reduction matrices (see Lemma 4.8 in the previous subsection). Left-multiplication by the reduction matrices making up $$P$$ has the effect of performing row operations. Right-multiplication by the reduction matrices making up $$Q$$ performs column operations. Therefore, matrix equivalence is a generalization of row equivalence— two matrices are row equivalent if one can be converted to the other by a sequence of row reduction steps, while two matrices are matrix equivalent if one can be converted to the other by a sequence of row reduction steps followed by a sequence of column reduction steps.

Thus, if matrices are row equivalent then they are also matrix equivalent (since we can take $$Q$$ to be the identity matrix and so perform no column operations). The converse, however, does not hold.

**Example 2.5**  —

These two

$$
\begin{pmatrix} 1 &0 \\ 0 &0 \end{pmatrix} \qquad \begin{pmatrix} 1 &1 \\ 0 &0 \end{pmatrix}
$$

are matrix equivalent because the second can be reduced to the first by the column operation of taking $$-1$$ times the first column and adding to the second. They are not row equivalent because they have different reduced echelon forms (in fact, both are already in reduced form).

We will close this section by finding a set of representatives for the matrix equivalence classes.

**Theorem 2.6**  —

Any $$m \! \times \! n$$ matrix of rank $$k$$ is matrix equivalent to the $$m \! \times \! n$$ matrix that is all zeros except that the first $$k$$ diagonal entries are ones.

$$
\begin{pmatrix} 1 &0 &\ldots &0 &0 &\ldots &0 \\ 0 &1 &\ldots &0 &0 &\ldots &0 \\ &\vdots \\ 0 &0 &\ldots &1 &0 &\ldots &0 \\ 0 &0 &\ldots &0 &0 &\ldots &0 \\ &\vdots \\ 0 &0 &\ldots &0 &0 &\ldots &0 \end{pmatrix}
$$

Sometimes this is described as a **block partial-identity** form.

$$
\left(\begin{array}{c|c} I &Z \\ \hline Z &Z \end{array}\right)
$$

**Proof**  —

As discussed above, Gauss-Jordan reduce the given matrix and combine all the reduction matrices used there to make $$P$$. Then use the leading entries to do column reduction and finish by swapping columns to put the leading ones on the diagonal. Combine the reduction matrices used for those column operations into $$Q$$.

**Example 2.7**  —

We illustrate the proof by finding the $$P$$ and $$Q$$ for this matrix.

$$
\begin{pmatrix} 1 &2 &1 &-1 \\ 0 &0 &1 &-1 \\ 2 &4 &2 &-2 \end{pmatrix}
$$

First Gauss-Jordan row-reduce.

$$
\begin{pmatrix} 1 &-1 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{pmatrix} \begin{pmatrix} 1 &0 &0 \\ 0 &1 &0 \\ -2 &0 &1 \end{pmatrix} \begin{pmatrix} 1 &2 &1 &-1 \\ 0 &0 &1 &-1 \\ 2 &4 &2 &-2 \end{pmatrix} = \begin{pmatrix} 1 &2 &0 &0 \\ 0 &0 &1 &-1 \\ 0 &0 &0 &0 \end{pmatrix}
$$

Then column-reduce, which involves right-multiplication.

$$
\begin{pmatrix} 1 &2 &0 &0 \\ 0 &0 &1 &-1 \\ 0 &0 &0 &0 \end{pmatrix} \begin{pmatrix} 1 &-2 &0 &0 \\ 0 &1 &0 &0 \\ 0 &0 &1 &0 \\ 0 &0 &0 &1 \end{pmatrix} \begin{pmatrix} 1 &0 &0 &0 \\ 0 &1 &0 &0 \\ 0 &0 &1 &1 \\ 0 &0 &0 &1 \end{pmatrix} = \begin{pmatrix} 1 &0 &0 &0 \\ 0 &0 &1 &0 \\ 0 &0 &0 &0 \end{pmatrix}
$$

Finish by swapping columns.

$$
\begin{pmatrix} 1 &0 &0 &0 \\ 0 &0 &1 &0 \\ 0 &0 &0 &0 \end{pmatrix} \begin{pmatrix} 1 &0 &0 &0 \\ 0 &0 &1 &0 \\ 0 &1 &0 &0 \\ 0 &0 &0 &1 \end{pmatrix} = \begin{pmatrix} 1 &0 &0 &0 \\ 0 &1 &0 &0 \\ 0 &0 &0 &0 \end{pmatrix}
$$

Finally, combine the left-multipliers together as $$P$$ and the right-multipliers together as $$Q$$ to get the $$PHQ$$ equation.

$$
\begin{pmatrix} 1 &-1 &0 \\ 0 &1 &0 \\ -2 &0 &1 \end{pmatrix} \begin{pmatrix} 1 &2 &1 &-1 \\ 0 &0 &1 &-1 \\ 2 &4 &2 &-2 \end{pmatrix} \begin{pmatrix} 1 &0 &-2 &0 \\ 0 &0 &1 &0 \\ 0 &1 &0 &1 \\ 0 &0 &0 &1 \end{pmatrix} = \begin{pmatrix} 1 &0 &0 &0 \\ 0 &1 &0 &0 \\ 0 &0 &0 &0 \end{pmatrix}
$$

**Corollary 2.8**  —

Two same-sized matrices are matrix equivalent if and only if they have the same rank. That is, the matrix equivalence classes are characterized by rank.

**Proof**  —

Two same-sized matrices with the same rank are equivalent to the same block partial-identity matrix.

**Example 2.9**  —

The $$2 \! \times \! 2$$ matrices have only three possible ranks: zero, one, or two. Thus there are three matrix-equivalence classes.  
All $$2 \! \times \! 2$$ matrices:  Three equivalence  
classes

Each class consists of all of the $$2 \! \times \! 2$$ matrices with the same rank. There is only one rank zero matrix, so that class has only one member, but the other two classes each have infinitely many members.

In this subsection we have seen how to change the representation of a map with respect to a first pair of bases to one with respect to a second pair. That led to a definition describing when matrices are equivalent in this way. Finally we noted that, with the proper choice of (possibly different) starting and ending bases, any map can be represented in block partial-identity form.

One of the nice things about this representation is that, in some sense, we can completely understand the map when it is expressed in this way: if the bases are $$B=\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ and $$D=\langle \vec{\delta}_1,\dots,\vec{\delta}_m \rangle$$ then the map sends

$$
c_1\vec{\beta}_1+\dots+c_k\vec{\beta}_k+c_{k+1}\vec{\beta}_{k+1}+\dots +c_n\vec{\beta}_n \;\longmapsto\; c_1\vec{\delta}_1+\dots+c_k\vec{\delta}_k+\vec{0}+\dots+\vec{0}
$$

where $$k$$ is the map's rank. Thus, we can understand any linear map as a kind of projection.

$$
\begin{pmatrix} c_1 \\ \vdots \\ c_k \\ c_{k+1} \\ \vdots \\ c_n \end{pmatrix}_B \;\mapsto\; \begin{pmatrix} c_1 \\ \vdots \\ c_k \\ 0 \\ \vdots \\ 0 \end{pmatrix}_D
$$

Of course, "understanding" a map expressed in this way requires that we understand the relationship between $$B$$ and $$D$$. However, despite that difficulty, this is a good classification of linear maps. }}

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Decide if these matrices are matrix equivalent.

1. $$\begin{pmatrix} 1 &3 &0 \\ 2 &3 &0 \end{pmatrix}$$, $$\begin{pmatrix} 2 &2 &1 \\ 0 &5 &-1 \end{pmatrix}$$
2. $$\begin{pmatrix} 0 &3 \\ 1 &1 \end{pmatrix}$$, $$\begin{pmatrix} 4 &0 \\ 0 &5 \end{pmatrix}$$
3. $$\begin{pmatrix} 1 &3 \\ 2 &6 \end{pmatrix}$$, $$\begin{pmatrix} 1 &3 \\ 2 &-6 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Find the canonical representative of the matrix-equivalence class of each matrix.

1. $$\begin{pmatrix} 2 &1 &0 \\ 4 &2 &0 \end{pmatrix}$$
2. $$\begin{pmatrix} 0 &1 &0 &2 \\ 1 &1 &0 &4 \\ 3 &3 &3 &-1 \end{pmatrix}$$

**Problem 3**  —

Suppose that, with respect to

$$
B=\mathcal{E}_2 \qquad D=\langle \begin{pmatrix} 1 \\ 1 \end{pmatrix},\begin{pmatrix} 1 \\ -1 \end{pmatrix} \rangle
$$

the transformation $$t:\mathbb{R}^2\to \mathbb{R}^2$$ is represented by this matrix.

$$
\begin{pmatrix} 1 &2 \\ 3 &4 \end{pmatrix}
$$

Use change of basis matrices to represent $$t$$ with respect to each pair.

1. $$\hat{B}=\langle \begin{pmatrix} 0 \\ 1 \end{pmatrix},\begin{pmatrix} 1 \\ 1 \end{pmatrix} \rangle$$, $$\hat{D}=\langle \begin{pmatrix} -1 \\ 0 \end{pmatrix},\begin{pmatrix} 2 \\ 1 \end{pmatrix} \rangle$$
2. $$\hat{B}=\langle \begin{pmatrix} 1 \\ 2 \end{pmatrix},\begin{pmatrix} 1 \\ 0 \end{pmatrix} \rangle$$, $$\hat{D}=\langle \begin{pmatrix} 1 \\ 2 \end{pmatrix},\begin{pmatrix} 2 \\ 1 \end{pmatrix} \rangle$$  
*This exercise is recommended for all readers.*

**Problem 4**  —

What sizes are $$P$$ and $$Q$$ in the equation $$\hat{H}=PHQ$$?  
*This exercise is recommended for all readers.*

**Problem 5**  —

Use Theorem 2.6 to show that a square matrix is nonsingular if and only if it is equivalent to an identity matrix.  
*This exercise is recommended for all readers.*

**Problem 6**  —

Show that, where $$A$$ is a nonsingular square matrix, if $$P$$ and $$Q$$ are nonsingular square matrices such that $$PAQ=I$$ then $$QP=A^{-1}$$.  
*This exercise is recommended for all readers.*

**Problem 7**  —

Why does Theorem 2.6 not show that every matrix is diagonalizable (see Example 2.2)?

**Problem 8**  —

Must matrix equivalent matrices have matrix equivalent transposes?

**Problem 9**  —

What happens in Theorem 2.6 if $$k=0$$?  
*This exercise is recommended for all readers.*

**Problem 10**  —

Show that matrix-equivalence is an equivalence relation.  
*This exercise is recommended for all readers.*

**Problem 11**  —

Show that a zero matrix is alone in its matrix equivalence class. Are there other matrices like that?

**Problem 12**  —

What are the matrix equivalence classes of matrices of transformations on $$\mathbb{R}^1$$? $$\mathbb{R}^3$$?

**Problem 13**  —

How many matrix equivalence classes are there?

**Problem 14**  —

Are matrix equivalence classes closed under scalar multiplication? Addition?

**Problem 15**  —

Let $$t:\mathbb{R}^n\to \mathbb{R}^n$$ represented by $$T$$ with respect to $$\mathcal{E}_n,\mathcal{E}_n$$.

1. Find $${\rm Rep}_{B,B}(t)$$ in this specific case.

$$
T=\begin{pmatrix} 1 &1 \\ 3 &-1 \end{pmatrix} \qquad B=\langle \begin{pmatrix} 1 \\ 2 \end{pmatrix}, \begin{pmatrix} -1 \\ -1 \end{pmatrix} \rangle
$$

2. Describe $${\rm Rep}_{B,B}(t)$$ in the general case where $$B=\langle\vec{\beta}_1,\ldots,\vec{\beta}_n\rangle$$.

**Problem 16**  —

1. Let $$V$$ have bases $$B_1$$ and $$B_2$$ and suppose that $$W$$ has the basis $$D$$. Where $$h:V\to W$$, find the formula that computes $${\rm Rep}_{B_2,D}(h)$$ from $${\rm Rep}_{B_1,D}(h)$$.
2. Repeat the prior question with one basis for $$V$$ and two bases for $$W$$.

**Problem 17**  —

1. If two matrices are matrix-equivalent and invertible, must their inverses be matrix-equivalent?
2. If two matrices have matrix-equivalent inverses, must the two be matrix-equivalent?
3. If two matrices are square and matrix-equivalent, must their squares be matrix-equivalent?
4. If two matrices are square and have matrix-equivalent squares, must they be matrix-equivalent?  
*This exercise is recommended for all readers.*

**Problem 18**  —

Square matrices are **similar** if they represent the same transformation, but each with respect to the same ending as starting basis. That is, $${\rm Rep}_{B_1,B_1}(t)$$ is similar to $${\rm Rep}_{B_2,B_2}(t)$$.

1. Give a definition of matrix similarity like that of Definition 2.3.
2. Prove that similar matrices are matrix equivalent.
3. Show that similarity is an equivalence relation.
4. Show that if $$T$$ is similar to $$\hat{T}$$ then $$T^2$$ is similar to $$\hat{T}^2$$, the cubes are similar, etc. *Contrast with the prior exercise.*
5. Prove that there are matrix equivalent matrices that are not similar.

Solutions

### Footnotes

---

*Source: Wikibooks, Linear Algebra/Changing Map Representations (https://en.wikibooks.org/wiki/Linear_Algebra/Changing_Map_Representations), by Wikibooks contributors, CC BY-SA 4.0.*
