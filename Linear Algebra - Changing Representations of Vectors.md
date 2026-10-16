# Changing Representations of Vectors

In converting $${\rm Rep}_{B}(\vec{v})$$ to $${\rm Rep}_{D}(\vec{v})$$ the underlying vector $$\vec{v}$$ doesn't change. Thus, this translation is accomplished by the identity map on the space, described so that the domain space vectors are represented with respect to $$B$$ and the codomain space vectors are represented with respect to $$D$$.  
(The diagram is vertical to fit with the ones in the next subsection.)

**Definition 1.1**  —

The **change of basis matrix**for bases $$B,D\subset V$$ is the representation of the identity map $$\text{id}:V\to V$$ with respect to those bases.

$$
{\rm Rep}_{B,D}(\text{id})= \left(\begin{array}{c|c|c} \vdots & &\vdots \\ {\rm Rep}_{D}(\vec{\beta}_1) &\;\cdots\; &{\rm Rep}_{D}(\vec{\beta}_n) \\ \vdots & &\vdots \end{array}\right)
$$

**Lemma 1.2**  —

Left-multiplication by the change of basis matrix for $$B,D$$ converts a representation with respect to $$B$$ to one with respect to $$D$$. Conversly, if left-multiplication by a matrix changes bases $$M\cdot{\rm Rep}_{B}(\vec{v})={\rm Rep}_{D}(\vec{v})$$ then $$M$$ is a change of basis matrix.

**Proof**  —

For the first sentence, for each $$\vec{v}$$, as matrix-vector multiplication represents a map application, $${\rm Rep}_{B,D}(\text{id})\cdot{\rm Rep}_{B}(\vec{v})={\rm Rep}_{D}(\,\text{id}(\vec{v})\,) ={\rm Rep}_{D}(\vec{v})$$. For the second sentence, with respect to $$B,D$$ the matrix $$M$$ represents some linear map, whose action is $$\vec{v}\mapsto\vec{v}$$, and is therefore the identity map.

**Example 1.3**  —

With these bases for $$\mathbb{R}^2$$,

$$
B= \langle \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \end{pmatrix} \rangle \qquad D= \langle \begin{pmatrix} -1 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \end{pmatrix} \rangle
$$

because

$$
{\rm Rep}_{D}(\,\text{id}(\begin{pmatrix} 2 \\ 1 \end{pmatrix})) =\begin{pmatrix} -1/2 \\ 3/2 \end{pmatrix}_D \qquad {\rm Rep}_{D}(\,\text{id}(\begin{pmatrix} 1 \\ 0 \end{pmatrix})) =\begin{pmatrix} -1/2 \\ 1/2 \end{pmatrix}_D
$$

the change of basis matrix is this.

$$
{\rm Rep}_{B,D}(\rm id) = \begin{pmatrix} -1/2 &-1/2 \\ 3/2 &1/2 \end{pmatrix}
$$

We can see this matrix at work by finding the two representations of $$\vec{e}_2$$

$$
{\rm Rep}_{B}(\begin{pmatrix} 0 \\ 1 \end{pmatrix} ) =\begin{pmatrix} 1 \\ -2 \end{pmatrix} \qquad {\rm Rep}_{D}(\begin{pmatrix} 0 \\ 1 \end{pmatrix} ) =\begin{pmatrix} 1/2 \\ 1/2 \end{pmatrix}
$$

and checking that the conversion goes as expected.

$$
\begin{pmatrix} -1/2 &-1/2 \\ 3/2 &1/2 \end{pmatrix} \begin{pmatrix} 1 \\ -2 \end{pmatrix} = \begin{pmatrix} 1/2 \\ 1/2 \end{pmatrix}
$$

We finish this subsection by recognizing that the change of basis matrices are familiar.

**Lemma 1.4**  —

A matrix changes bases if and only if it is nonsingular.

**Proof**  —

For one direction, if left-multiplication by a matrix changes bases then the matrix represents an invertible function, simply because the function is inverted by changing the bases back. Such a matrix is itself invertible, and so nonsingular.

To finish, we will show that any nonsingular matrix $$M$$ performs a change of basis operation from any given starting basis $$B$$ to some ending basis. Because the matrix is nonsingular, it will Gauss-Jordan reduce to the identity, so there are elementatry reduction matrices such that $$R_r\cdots R_1\cdot M=I$$. Elementary matrices are invertible and their inverses are also elementary, so multiplying from the left first by $${R_r}^{-1}$$, then by $${R_{r-1}}^{-1}$$, etc., gives $$M$$ as a product of elementary matrices $$M={R_1}^{-1}\cdots {R_r}^{-1}$$. Thus, we will be done if we show that elementary matrices change a given basis to another basis, for then $${R_r}^{-1}$$ changes $$B$$ to some other basis $$B_r$$, and $${R_{r-1}}^{-1}$$ changes $$B_r$$ to some $$B_{r-1}$$, ..., and the net effect is that $$M$$ changes $$B$$ to $$B_1$$. We will prove this about elementary matrices by covering the three types as separate cases.

Applying a row-multiplication matrix

$$
M_{i}(k) \begin{pmatrix} c_1 \\ \vdots \\ c_i \\ \vdots \\ c_n \end{pmatrix} = \begin{pmatrix} c_1 \\ \vdots \\ kc_i \\ \vdots \\ c_n \end{pmatrix}
$$

changes a representation with respect to $$\langle \vec{\beta}_1,\dots,\vec{\beta}_i,\dots,\vec{\beta}_n \rangle$$ to one with respect to $$\langle \vec{\beta}_1,\dots,(1/k)\vec{\beta}_i,\dots,\vec{\beta}_n \rangle$$ in this way.

$$
\vec{v}= c_1\cdot\vec{\beta}_1+\dots+c_i\cdot\vec{\beta}_i +\dots+c_n\cdot\vec{\beta}_n
$$

$$
\mapsto\; c_1\cdot\vec{\beta}_1+\dots+kc_i\cdot(1/k)\vec{\beta}_i+\dots +c_n\cdot\vec{\beta}_n=\vec{v}
$$

Similarly, left-multiplication by a row-swap matrix $$P_{i,j}$$ changes a representation with respect to the basis $$\langle \vec{\beta}_1,\dots,\vec{\beta}_i,\dots,\vec{\beta}_j, \dots,\vec{\beta}_n \rangle$$ into one with respect to the basis $$\langle \vec{\beta}_1,\dots,\vec{\beta}_j,\dots,\vec{\beta}_i, \dots,\vec{\beta}_n \rangle$$ in this way.

$$
\vec{v}= c_1\cdot\vec{\beta}_1+\dots+c_i\cdot\vec{\beta}_i +\dots+c_j\vec{\beta}_j+\dots+c_n\cdot\vec{\beta}_n
$$

$$
\mapsto\; c_1\cdot\vec{\beta}_1+\dots+c_j\cdot\vec{\beta}_j+\dots +c_i\cdot\vec{\beta}_i+\dots+c_n\cdot\vec{\beta}_n=\vec{v}
$$

And, a representation with respect to $$\langle \vec{\beta}_1,\dots,\vec{\beta}_i,\dots,\vec{\beta}_j, \dots,\vec{\beta}_n \rangle$$ changes via left-multiplication by a row-combination matrix $$C_{i,j}(k)$$ into a representation with respect to $$\langle \vec{\beta}_1,\dots,\vec{\beta}_i-k\vec{\beta}_j, \dots,\vec{\beta}_j,\dots,\vec{\beta}_n \rangle$$

$$
\vec{v}= c_1\cdot\vec{\beta}_1+\dots+c_i\cdot\vec{\beta}_i +c_j\vec{\beta}_j+\dots+c_n\cdot\vec{\beta}_n
$$

$$
\mapsto\; c_1\cdot\vec{\beta}_1+\dots+c_i\cdot(\vec{\beta}_i-k\vec{\beta}_j)+\dots +(kc_i+c_j)\cdot\vec{\beta}_j+\dots+c_n\cdot\vec{\beta}_n=\vec{v}
$$

(the definition of reduction matrices specifies that $$i\neq k$$ and $$k\neq 0$$ and so this last one is a basis).

**Corollary 1.5**  —

A matrix is nonsingular if and only if it represents the identity map with respect to some pair of bases.

In the next subsection we will see how to translate among representations of maps, that is, how to change $${\rm Rep}_{B,D}(h)$$ to $${\rm Rep}_{\hat{B},\hat{D}}(h)$$. The above corollary is a special case of this, where the domain and range are the same space, and where the map is the identity map.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

In $$\mathbb{R}^2$$, where

$$
D=\langle \begin{pmatrix} 2 \\ 1 \end{pmatrix},\begin{pmatrix} -2 \\ 4 \end{pmatrix} \rangle
$$

find the change of basis matrices from $$D$$ to $$\mathcal{E}_2$$ and from $$\mathcal{E}_2$$ to $$D$$. Multiply the two.  
*This exercise is recommended for all readers.*

**Problem 2**  —

Find the change of basis matrix for $$B,D\subseteq\mathbb{R}^2$$.

1. $$B=\mathcal{E}_2$$, $$D=\langle \vec{e}_2,\vec{e}_1 \rangle$$
2. $$B=\mathcal{E}_2$$, $$D=\langle \begin{pmatrix} 1 \\ 2 \end{pmatrix},\begin{pmatrix} 1 \\ 4 \end{pmatrix} \rangle$$
3. $$B=\langle \begin{pmatrix} 1 \\ 2 \end{pmatrix},\begin{pmatrix} 1 \\ 4 \end{pmatrix} \rangle$$, $$D=\mathcal{E}_2$$
4. $$B=\langle \begin{pmatrix} -1 \\ 1 \end{pmatrix},\begin{pmatrix} 2 \\ 2 \end{pmatrix} \rangle$$, $$D=\langle \begin{pmatrix} 0 \\ 4 \end{pmatrix},\begin{pmatrix} 1 \\ 3 \end{pmatrix} \rangle$$

**Problem 3**  —

For the bases in Problem 2, find the change of basis matrix in the other direction, from $$D$$ to $$B$$.  
*This exercise is recommended for all readers.*

**Problem 4**  —

Find the change of basis matrix for each $$B,D\subseteq\mathcal{P}_2$$.

1. $$B=\langle 1,x,x^2 \rangle , D=\langle x^2,1,x \rangle$$
2. $$B=\langle 1,x,x^2 \rangle , D=\langle 1,1+x,1+x+x^2 \rangle$$
3. $$B=\langle 2,2x,x^2 \rangle , D=\langle 1+x^2,1-x^2,x+x^2 \rangle$$  
*This exercise is recommended for all readers.*

**Problem 5**  —

Decide if each changes bases on $$\mathbb{R}^2$$. To what basis is $$\mathcal{E}_2$$ changed?

1. $$\begin{pmatrix} 5 &0 \\ 0 &4 \end{pmatrix}$$
2. $$\begin{pmatrix} 2 &1 \\ 3 &1 \end{pmatrix}$$
3. $$\begin{pmatrix} -1 &4 \\ 2 &-8 \end{pmatrix}$$
4. $$\begin{pmatrix} 1 &-1 \\ 1 &1 \end{pmatrix}$$

**Problem 6**  —

Find bases such that this matrix represents the identity map with respect to those bases.

$$
\begin{pmatrix} 3 &1 &4 \\ 2 &-1 &1 \\ 0 &0 &4 \end{pmatrix}
$$

**Problem 7**  —

Conside the vector space of real-valued functions with basis $$\langle \sin(x),\cos(x) \rangle$$. Show that $$\langle 2\sin(x)+\cos(x),3\cos(x) \rangle$$ is also a basis for this space. Find the change of basis matrix in each direction.

**Problem 8**  —

Where does this matrix

$$
\begin{pmatrix} \cos(2\theta) &\sin(2\theta) \\ \sin(2\theta) &-\cos(2\theta) \end{pmatrix}
$$

send the standard basis for $$\mathbb{R}^2$$? Any other bases? *Hint.* Consider the inverse.  
*This exercise is recommended for all readers.*

**Problem 9**  —

What is the change of basis matrix with respect to $$B,B$$?

**Problem 10**  —

Prove that a matrix changes bases if and only if it is invertible.

**Problem 11**  —

Finish the proof of Lemma 1.4.  
*This exercise is recommended for all readers.*

**Problem 12**  —

Let $$H$$ be a $$n \! \times \! n$$ nonsingular matrix. What basis of $$\mathbb{R}^n$$ does $$H$$ change to the standard basis?  
*This exercise is recommended for all readers.*

**Problem 13**  —

1. In $$\mathcal{P}_3$$ with basis $$B=\langle 1+x,1-x,x^2+x^3,x^2-x^3 \rangle$$ we have this represenatation.

$$
{\rm Rep}_{B}(1-x+3x^2-x^3)= \begin{pmatrix} 0 \\ 1 \\ 1 \\ 2 \end{pmatrix}_B
$$

Find a basis $$D$$ giving this different representation for the same polynomial.

$$
{\rm Rep}_{D}(1-x+3x^2-x^3)= \begin{pmatrix} 1 \\ 0 \\ 2 \\ 0 \end{pmatrix}_D
$$

2. State and prove that any nonzero vector representation can be changed to any other.

*Hint.* The proof of Lemma 1.4 is constructive— it not only says the bases change, it shows how they change.

**Problem 14**  —

Let $$V,W$$ be vector spaces, and let $$B,\hat{B}$$ be bases for $$V$$ and $$D,\hat{D}$$ be bases for $$W$$. Where $$h:V\to W$$ is linear, find a formula relating $${\rm Rep}_{B,D}(h)$$ to $${\rm Rep}_{\hat{B},\hat{D}}(h)$$.  
*This exercise is recommended for all readers.*

**Problem 15**  —

Show that the columns of an $$n \! \times \! n$$ change of basis matrix form a basis for $$\mathbb{R}^n$$. Do all bases appear in that way: can the vectors from any $$\mathbb{R}^n$$ basis make the columns of a change of basis matrix?  
*This exercise is recommended for all readers.*

**Problem 16**  —

Find a matrix having this effect.

$$
\begin{pmatrix} 1 \\ 3 \end{pmatrix} \;\mapsto\; \begin{pmatrix} 4 \\ -1 \end{pmatrix}
$$

That is, find a $$M$$ that left-multiplies the starting vector to yield the ending vector. Is there a matrix having these two effects?

1. $$\begin{pmatrix} 1 \\ 3 \end{pmatrix}\mapsto\begin{pmatrix} 1 \\ 1 \end{pmatrix} \quad \begin{pmatrix} 2 \\ -1 \end{pmatrix}\mapsto\begin{pmatrix} -1 \\ -1 \end{pmatrix}$$
2. $$\begin{pmatrix} 1 \\ 3 \end{pmatrix}\mapsto\begin{pmatrix} 1 \\ 1 \end{pmatrix} \quad \begin{pmatrix} 2 \\ 6 \end{pmatrix}\mapsto\begin{pmatrix} -1 \\ -1 \end{pmatrix}$$

Give a necessary and sufficient condition for there to be a matrix such that $$\vec{v}_1\mapsto\vec{w}_1$$ and $$\vec{v}_2\mapsto\vec{w}_2$$.

Solutions

For more exercises see Abstract Algebra/3x3 real matrices.

---

*Source: Wikibooks, Linear Algebra/Changing Representations of Vectors (https://en.wikibooks.org/wiki/Linear_Algebra/Changing_Representations_of_Vectors), by Wikibooks contributors, CC BY-SA 4.0.*
