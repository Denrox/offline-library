# Determinants as Size Functions

This parallelogram picture

is familiar from the construction of the sum of the two vectors. One way to compute the area that it encloses is to draw this rectangle and subtract the area of each subregion.

$$
\begin{array}{l} \text{area of parallelogram} \\ \quad =\text{area of rectangle} -\text{area of }A-\text{area of }B \\ \qquad -\cdots-\text{area of }F \\ \quad =(x_1+x_2)(y_1+y_2)-x_2y_1-x_1y_1/2 \\ \qquad -x_2y_2/2-x_2y_2/2-x_1y_1/2-x_2y_1 \\ \quad =x_1y_2-x_2y_1 \end{array}
$$

The fact that the area equals the value of the determinant

$$
\begin{vmatrix} x_1 &x_2 \\ y_1 &y_2 \end{vmatrix} =x_1y_2-x_2y_1
$$

is no coincidence. The properties in the definition of determinants make reasonable postulates for a function that measures the size of the region enclosed by the vectors in the matrix.

For instance, this shows the effect of multiplying one of the box-defining vectors by a scalar (the scalar used is $$k=1.4$$).

The region formed by $$k\vec{v}$$ and $$\vec{w}$$ is bigger, by a factor of $$k$$, than the shaded region enclosed by $$\vec{v}$$ and $$\vec{w}$$. That is, $$\text{size}\, (k\vec{v},\vec{w})=k\cdot\text{size}\, (\vec{v},\vec{w})$$ and in general we expect of the size measure that $$\text{size}\, (\dots,k\vec{v},\dots)=k\cdot\text{size}\, (\dots,\vec{v},\dots)$$. Of course, this postulate is already familiar as one of the properties in the definition of determinants.

Another property of determinants is that they are unaffected by pivoting. Here are before-pivoting and after-pivoting boxes (the scalar used is $$k=0.35$$).

Although the region on the right, the box formed by $$v$$ and $$k\vec{v}+\vec{w}$$, is more slanted than the shaded region, the two have the same base and the same height and hence the same area. This illustrates that $$\text{size}\, (\vec{v},k\vec{v}+\vec{w})=\text{size}\, (\vec{v},\vec{w})$$. Generalized, $$\text{size}\, (\dots,\vec{v},\dots,\vec{w},\dots) =\text{size}\, (\dots,\vec{v},\dots,k\vec{v}+\vec{w},\dots)$$, which is a restatement of the determinant postulate.

Of course, this picture

shows that $$\text{size}\, (\vec{e}_1,\vec{e}_2)=1$$, and we naturally extend that to any number of dimensions $$\text{size}\,(\vec{e}_1,\dots,\vec{e}_n)=1$$, which is a restatement of the property that the determinant of the identity matrix is one.

With that, because property (2) of determinants is redundant (as remarked right after the definition), we have that all of the properties of determinants are reasonable to expect of a function that gives the size of boxes. We can now cite the work done in the prior section to show that the determinant exists and is unique to be assured that these postulates are consistent and sufficient (we do not need any more postulates). That is, we've got an intuitive justification to interpret $$\det(\vec{v}_1,\dots,\vec{v}_n)$$ as the size of the box formed by the vectors. (*Comment.* An even more basic approach, which also leads to the definition below, is in (Weston 1959).

**Example 1.1**  —

The volume of this parallelepiped, which can be found by the usual formula from high school geometry, is $$12$$.

$$
\begin{vmatrix} 2 &0 &-1\\ 0 &3 &0 \\ 2 &1 &1 \end{vmatrix}=12
$$

**Remark 1.2**  —

Although property (2) of the definition of determinants is redundant, it raises an important point. Consider these two.

- $$\begin{vmatrix} 4 &1 \\ 2 &3 \end{vmatrix}=10$$  $$\begin{vmatrix} 1 &4 \\ 3 &2 \end{vmatrix}=-10$$

The only difference between them is in the order in which the vectors are taken. If we take $$\vec{u}$$ first and then go to $$\vec{v}$$, follow the counterclockwise arc shown, then the sign is positive. Following a clockwise arc gives a negative sign. The sign returned by the size function reflects the "orientation" or "sense" of the box. (We see the same thing if we picture the effect of scalar multiplication by a negative scalar.)

Although it is both interesting and important, the idea of orientation turns out to be tricky. It is not needed for the development below, and so we will pass it by. (See Problem 20.)

**Definition 1.3**  —

The **box** (or **parallelepiped**) formed by $$\langle \vec{v}_1,\dots,\vec{v}_n \rangle$$ (where each vector is from $$\mathbb{R}^n$$) includes all of the set $$\{t_1\vec{v}_1+\dots+t_n\vec{v}_n \,\big|\, t_1,\ldots,t_n\in [0..1]\}$$. The **volume** of a box is the absolute value of the determinant of the matrix with those vectors as columns.

**Example 1.4**  —

Volume, because it is an absolute value, does not depend on the order in which the vectors are given. The volume of the parallelepiped in Example 1.1, can also be computed as the absolute value of this determinant.

$$
\begin{vmatrix} 0 &2 &-1 \\ 3 &0 &0 \\ 1 &2 &1 \end{vmatrix}=-12
$$

The definition of volume gives a geometric interpretation to something in the space, boxes made from vectors. The next result relates the geometry to the functions that operate on spaces.

**Theorem 1.5**  —

A transformation $$t:\mathbb{R}^n\to \mathbb{R}^n$$ changes the size of all boxes by the same factor, namely the size of the image of a box $$\left|t(S)\right|$$ is $$\left|T\right|$$ times the size of the box $$\left|S\right|$$, where $$T$$ is the matrix representing $$t$$ with respect to the standard basis. That is, for all $$n \! \times \! n$$ matrices, the determinant of a product is the product of the determinants $$\left|TS\right|=\left|T\right|\cdot\left|S\right|$$.

The two sentences state the same idea, first in map terms and then in matrix terms. Although we tend to prefer a map point of view, the second sentence, the matrix version, is more convienent for the proof and is also the way that we shall use this result later. (Alternate proofs are given as Problem 16 and Problem 21].)

**Proof**  —

The two statements are equivalent because $$\left|t(S)\right|=\left|TS\right|$$, as both give the size of the box that is the image of the unit box $$\mathcal{E}_n$$ under the composition $$t\circ s$$ (where $$s$$ is the map represented by $$S$$ with respect to the standard basis).

First consider the case that $$\left|T\right|=0$$. A matrix has a zero determinant if and only if it is not invertible. Observe that if $$TS$$ is invertible, so that there is an $$M$$ such that $$(TS)M=I$$, then the associative property of matrix multiplication $$T(SM)=I$$ shows that $$T$$ is also invertible (with inverse $$SM$$). Therefore, if $$T$$ is not invertible then neither is $$TS$$ — if $$\left|T\right|=0$$ then $$\left|TS\right|=0$$, and the result holds in this case.

Now consider the case that $$\left|T\right|\neq 0$$, that $$T$$ is nonsingular. Recall that any nonsingular matrix can be factored into a product of elementary matrices, so that $$TS=E_1E_2\cdots E_rS$$. In the rest of this argument, we will verify that if $$E$$ is an elementary matrix then $$\left|ES\right|=\left|E\right|\cdot\left|S\right|$$. The result will follow because then $$\left|TS\right|=\left|E_1\cdots E_rS\right|=\left|E_1\right|\cdots\left|E_r\right|\cdot\left|S\right| =\left|E_1\cdots E_r\right|\cdot\left|S\right|=\left|T\right|\cdot\left|S\right|$$.

If the elementary matrix $$E$$ is $$M_i(k)$$ then $$M_i(k)S$$ equals $$S$$ except that row $$i$$ has been multiplied by $$k$$. The third property of determinant functions then gives that $$\left|M_i(k)S\right|=k\cdot\left|S\right|$$. But $$\left|M_i(k)\right|=k$$, again by the third property because $$M_i(k)$$ is derived from the identity by multiplication of row $$i$$ by $$k$$, and so $$\left|ES\right|=\left|E\right|\cdot\left|S\right|$$ holds for $$E=M_i(k)$$. The $$E=P_{i,j}=-1$$ and $$E=C_{i,j}(k)$$ checks are similar.

**Example 1.6**  —

Application of the map $$t$$ represented with respect to the standard bases by

$$
\begin{pmatrix} 1 &1 \\ -2 &0 \end{pmatrix}
$$

will double sizes of boxes, e.g., from this

$$
\begin{vmatrix} 2 &1 \\ 1 &2 \end{vmatrix}=3
$$

to this

$$
\begin{vmatrix} 3 &3 \\ -4 &-2 \end{vmatrix}=6
$$

**Corollary 1.7**  —

If a matrix is invertible then the determinant of its inverse is the inverse of its determinant $$\left|T^{-1}\right|=1/\left|T\right|$$.

**Proof**  —

$$
1=\left|I\right|=\left|TT^{-1}\right|=\left|T\right|\cdot\left|T^{-1}\right|
$$

Recall that determinants are not additive homomorphisms, $$\det(A+B)$$ need not equal $$\det(A)+\det(B)$$. The above theorem says, in contrast, that determinants are multiplicative homomorphisms: $$\det(AB)$$ does equal $$\det(A)\cdot \det(B)$$.

### Exercises

**Problem 1**  —

Find the volume of the region formed.

1. $$\langle \begin{pmatrix} 1 \\ 3 \end{pmatrix},\begin{pmatrix} -1 \\ 4 \end{pmatrix} \rangle$$
2. $$\langle \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix},\begin{pmatrix} 3 \\ -2 \\ 4 \end{pmatrix}, \begin{pmatrix} 8 \\ -3 \\ 8 \end{pmatrix} \rangle$$
3. $$\langle \begin{pmatrix} 1 \\ 2 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 2 \\ 2 \\ 2 \\ 2 \end{pmatrix}, \begin{pmatrix} -1 \\ 3 \\ 0 \\ 5 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \\ 7 \end{pmatrix} \rangle$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Is

$$
\begin{pmatrix} 4 \\ 1 \\ 2 \end{pmatrix}
$$

inside of the box formed by these three?

$$
\begin{pmatrix} 3 \\ 3 \\ 1 \end{pmatrix} \quad \begin{pmatrix} 2 \\ 6 \\ 1 \end{pmatrix} \quad \begin{pmatrix} 1 \\ 0 \\ 5 \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 3**  —

Find the volume of this region.  
*This exercise is recommended for all readers.*

**Problem 4**  —

Suppose that $$\left|A\right|=3$$. By what factor do these change volumes?

1. $$A$$
2. $$A^2$$
3. $$A^{-2}$$  
*This exercise is recommended for all readers.*

**Problem 5**  —

By what factor does each transformation change the size of boxes?

1. $$\begin{pmatrix} x \\ y \end{pmatrix}\mapsto\begin{pmatrix} 2x \\ 3y \end{pmatrix}$$
2. $$\begin{pmatrix} x \\ y \end{pmatrix}\mapsto\begin{pmatrix} 3x-y \\ -2x+y \end{pmatrix}$$
3. $$\begin{pmatrix} x \\ y \\ z \end{pmatrix}\mapsto\begin{pmatrix} x-y \\ x+y+z \\ y-2z \end{pmatrix}$$

**Problem 6**  —

What is the area of the image of the rectangle $$[2..4]\times [2..5]$$ under the action of this matrix?

$$
\begin{pmatrix} 2 &3 \\ 4 &-1 \end{pmatrix}
$$

**Problem 7**  —

If $$t:\mathbb{R}^3\to \mathbb{R}^3$$ changes volumes by a factor of $$7$$ and $$s:\mathbb{R}^3\to \mathbb{R}^3$$ changes volumes by a factor of $$3/2$$ then by what factor will their composition changes volumes?

**Problem 8**  —

In what way does the definition of a box differ from the definition of a span?  
*This exercise is recommended for all readers.*

**Problem 9**  —

Why doesn't this picture contradict Theorem 1.5?

$$
\xrightarrow[]{\scriptstyle \begin{pmatrix} 2 &1 \\ 0 &1 \end{pmatrix}}
$$

- area is $$2$$  determinant is $$2$$  area is $$5$$  
*This exercise is recommended for all readers.*

**Problem 10**  —

Does $$\left|TS\right|=\left|ST\right|$$? $$\left|T(SP)\right|=\left|(TS)P\right|$$?

**Problem 11**  —

1. Suppose that $$\left|A\right|=3$$ and that $$\left|B\right|=2$$. Find $$\left|A^2\cdot {{B}^{\rm trans}}\cdot B^{-2}\cdot {{A}^{\rm trans}} \right|$$.
2. Assume that $$\left|A\right|=0$$. Prove that $$\left|6A^3+5A^2+2A\right|=0$$.  
*This exercise is recommended for all readers.*

**Problem 12**  —

Let $$T$$ be the matrix representing (with respect to the standard bases) the map that rotates plane vectors counterclockwise thru $$\theta$$ radians. By what factor does $$T$$ change sizes?  
*This exercise is recommended for all readers.*

**Problem 13**  —

Must a transformation $$t:\mathbb{R}^2\to \mathbb{R}^2$$ that preserves areas also preserve lengths?  
*This exercise is recommended for all readers.*

**Problem 14**  —

What is the volume of a parallelepiped in $$\mathbb{R}^3$$ bounded by a linearly dependent set?  
*This exercise is recommended for all readers.*

**Problem 15**  —

Find the area of the triangle in $$\mathbb{R}^3$$ with endpoints $$(1,2,1)$$, $$(3,-1,4)$$, and $$(2,2,2)$$. (Area, not volume. The triangle defines a plane— what is the area of the triangle in that plane?)  
*This exercise is recommended for all readers.*

**Problem 16**  —

An alternate proof of Theorem 1.5 uses the definition of determinant functions.

1. Note that the vectors forming $$S$$ make a linearly dependent set if and only if $$\left|S\right|=0$$, and check that the result holds in this case.
2. For the $$\left|S\right|\neq 0$$ case, to show that $$\left|TS\right|/\left|S\right|=\left|T\right|$$ for all transformations, consider the function $$d:\mathcal{M}_{n \! \times \! n}\to \mathbb{R}$$ given by $$T\mapsto \left|TS\right|/\left|S\right|$$. Show that $$d$$ has the first property of a determinant.
3. Show that $$d$$ has the remaining three properties of a determinant function.
4. Conclude that $$\left|TS\right|=\left|T\right|\cdot\left|S\right|$$.

**Problem 17**  —

Give a non-identity matrix with the property that $${{A}^{\rm trans}}=A^{-1}$$. Show that if $${{A}^{\rm trans}}=A^{-1}$$ then $$\left|A\right|=\pm 1$$. Does the converse hold?

**Problem 18**  —

The algebraic property of determinants that factoring a scalar out of a single row will multiply the determinant by that scalar shows that where $$H$$ is $$3 \! \times \! 3$$, the determinant of $$cH$$ is $$c^3$$ times the determinant of $$H$$. Explain this geometrically, that is, using Theorem 1.5,  
*This exercise is recommended for all readers.*

**Problem 19**  —

Matrices $$H$$ and $$G$$ are said to be **similar** if there is a nonsingular matrix $$P$$ such that $$H=P^{-1}GP$$ (we will study this relation in Chapter Five). Show that similar matrices have the same determinant.

**Problem 20**  —

We usually represent vectors in $$\mathbb{R}^2$$ with respect to the standard basis so vectors in the first quadrant have both coordinates positive.

$$
{\rm Rep}_{\mathcal{E}_2}(\vec{v})=\begin{pmatrix} +3 \\ +2 \end{pmatrix}
$$

Moving counterclockwise around the origin, we cycle thru four regions:

$$
\cdots \;\longrightarrow\begin{pmatrix} + \\ + \end{pmatrix} \;\longrightarrow\begin{pmatrix} - \\ + \end{pmatrix} \;\longrightarrow\begin{pmatrix} - \\ - \end{pmatrix} \;\longrightarrow\begin{pmatrix} + \\ - \end{pmatrix} \;\longrightarrow\cdots\,.
$$

Using this basis

$$
B=\langle \begin{pmatrix} 0 \\ 1 \end{pmatrix},\begin{pmatrix} -1 \\ 0 \end{pmatrix} \rangle
$$

gives the same counterclockwise cycle. We say these two bases have the same *orientation*.

1. Why do they give the same cycle?
2. What other configurations of unit vectors on the axes give the same cycle?
3. Find the determinants of the matrices formed from those (ordered) bases.
4. What other counterclockwise cycles are possible, and what are the associated determinants?
5. What happens in $$\mathbb{R}^1$$?
6. What happens in $$\mathbb{R}^3$$?

A fascinating general-audience discussion of orientations is in (Gardner 1990).

**Problem 21**  —

*This question uses material from the optional Determinant Functions Exist subsection.* Prove Theorem 1.5 by using the permutation expansion formula for the determinant.  
*This exercise is recommended for all readers.*

**Problem 22**  —

1. Show that this gives the equation of a line in $$\mathbb{R}^2$$ thru $$(x_2,y_2)$$ and $$(x_3,y_3)$$.

$$
\begin{vmatrix} x &x_2 &x_3 \\ y &y_2 &y_3 \\ 1 &1 &1 \end{vmatrix}=0
$$

2. (Peterson 1955) Prove that the area of a triangle with vertices $$(x_1,y_1)$$, $$(x_2,y_2)$$, and $$(x_3,y_3)$$ is

$$
\frac{1}{2} \begin{vmatrix} x_1 &x_2 &x_3 \\ y_1 &y_2 &y_3 \\ 1 &1 &1 \end{vmatrix}.
$$

3. (Bittinger 1973) Prove that the area of a triangle with vertices at $$(x_1,y_1)$$, $$(x_2,y_2)$$, and $$(x_3,y_3)$$ whose coordinates are integers has an area of $$N$$ or $$N/2$$ for some positive integer $$N$$.

Solutions

### References

- Bittinger, Marvin (proposer) (1973), "Quickie 578", *Mathematics Magazine*, **46** (5), American Mathematical Society: 286, 296 {{citation}}: Unknown parameter |month= ignored (help).
- Gardner, Martin (1990), *The New Ambidextrous Univers*, W. H. Freeman and Company {{citation}}: Unknown parameter |editition= ignored (help).
- Peterson, G. M. (1955), "Area of a triangle", *American Mathematical Monthly*, **62** (4), American Mathematical Society: 249 {{citation}}: Unknown parameter |month= ignored (help).
- Weston, J. D. (1959), "Volume in Vector Spaces", *American Mathematical Monthly*, **66** (7), American Mathematical Society: 575–577 {{citation}}: Unknown parameter |month= ignored (help).

---

*Source: Wikibooks, Linear Algebra/Determinants as Size Functions (https://en.wikibooks.org/wiki/Linear_Algebra/Determinants_as_Size_Functions), by Wikibooks contributors, CC BY-SA 4.0.*
