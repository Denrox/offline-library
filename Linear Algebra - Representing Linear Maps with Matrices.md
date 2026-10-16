# Representing Linear Maps with Matrices

**Example 1.1**  —

Consider a map $$h$$ with domain $$\mathbb{R}^2$$ and codomain $$\mathbb{R}^3$$ (fixing

$$
B=\langle \begin{pmatrix} 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 4 \end{pmatrix} \rangle \quad\text{and}\quad D=\langle \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ -2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \rangle
$$

as the bases for these spaces) that is determined by this action on the vectors in the domain's basis.

$$
\begin{pmatrix} 2 \\ 0 \end{pmatrix} \stackrel{h}{\longmapsto} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \qquad \begin{pmatrix} 1 \\ 4 \end{pmatrix} \stackrel{h}{\longmapsto} \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}
$$

To compute the action of this map on any vector at all from the domain, we first express $$h(\vec{\beta}_1)$$ and $$h(\vec{\beta}_2)$$ with respect to the codomain's basis:

$$
\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}= 0\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} -\frac{1}{2}\begin{pmatrix} 0 \\ -2 \\ 0 \end{pmatrix} +1\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \quad\text{so}\quad {\rm Rep}_{D}( h(\vec{\beta}_1) )=\begin{pmatrix} 0 \\ -1/2 \\ 1 \end{pmatrix}_D
$$

and

$$
\begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}= 1\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} -1\begin{pmatrix} 0 \\ -2 \\ 0 \end{pmatrix} +0\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \quad\text{so}\quad {\rm Rep}_{D}( h(\vec{\beta}_2) )=\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}_D
$$

(these are easy to check). Then, as described in the preamble, for any member $$\vec{v}$$ of the domain, we can express the image $$h(\vec{v})$$ in terms of the $$h(\vec{\beta})$$'s.

$$
\begin{array}{rl} h(\vec{v}) &=h(c_1\cdot \begin{pmatrix} 2 \\ 0 \end{pmatrix}+c_2\cdot \begin{pmatrix} 1 \\ 4 \end{pmatrix}) \\ &=c_1\cdot h(\begin{pmatrix} 2 \\ 0 \end{pmatrix})+c_2\cdot h(\begin{pmatrix} 1 \\ 4 \end{pmatrix}) \\ &=c_1\cdot ( 0\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \!-\frac{1}{2}\begin{pmatrix} 0 \\ -2 \\ 0 \end{pmatrix} \!+1\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}\! ) +c_2\cdot ( 1\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \!-1\begin{pmatrix} 0 \\ -2 \\ 0 \end{pmatrix} \!+0\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}\! ) \\ &=(0c_1+1c_2)\cdot \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} +(-\frac{1}{2}c_1-1c_2)\cdot \begin{pmatrix} 0 \\ -2 \\ 0 \end{pmatrix} +(1c_1+0c_2)\cdot \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \end{array}
$$

Thus,

with $${\rm Rep}_{B}(\vec{v})=\begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$$ then $${\rm Rep}_{D}(\,h(\vec{v})\,) =\begin{pmatrix} 0c_1+1c_2 \\ -(1/2)c_1-1c_2 \\ 1c_1+0c_2 \end{pmatrix}$$.

For instance,

with $${\rm Rep}_{B}(\begin{pmatrix} 4 \\ 8 \end{pmatrix})=\begin{pmatrix} 1 \\ 2 \end{pmatrix}_B$$ then $${\rm Rep}_{D}(\,h(\begin{pmatrix} 4 \\ 8 \end{pmatrix})\,) =\begin{pmatrix} 2 \\ -5/2 \\ 1 \end{pmatrix}$$.

We will express computations like the one above with a matrix notation.

$$
\begin{pmatrix} 0 &1 \\ -1/2 &-1 \\ 1 &0 \end{pmatrix}_{B,D} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}_B = \begin{pmatrix} 0c_1+1c_2 \\ (-1/2)c_1-1c_2 \\ 1c_1+0c_2 \end{pmatrix}_D
$$

In the middle is the argument $$\vec{v}$$ to the map, represented with respect to the domain's basis $$B$$ by a column vector with components $$c_1$$ and $$c_2$$. On the right is the value $$h(\vec{v})$$ of the map on that argument, represented with respect to the codomain's basis $$D$$ by a column vector with components $$0c_1+1c_2$$, etc. The matrix on the left is the new thing. It consists of the coefficients from the vector on the right, $$0$$ and $$1$$ from the first row, $$-1/2$$ and $$-1$$ from the second row, and $$1$$ and $$0$$ from the third row.

This notation simply breaks the parts from the right, the coefficients and the $$c$$'s, out separately on the left, into a vector that represents the map's argument and a matrix that we will take to represent the map itself.

**Definition 1.2**  —

Suppose that $$V$$ and $$W$$ are vector spaces of dimensions $$n$$ and $$m$$ with bases $$B$$ and $$D$$, and that $$h:V\to W$$ is a linear map. If

$$
{\rm Rep}_{D}(h( \vec{\beta}_1 ))= \begin{pmatrix} h_{1,1} \\ h_{2,1} \\ \vdots \\ h_{m,1} \end{pmatrix}_D \;\ldots\; {\rm Rep}_{D}(h( \vec{\beta}_n ))= \begin{pmatrix} h_{1,n} \\ h_{2,n} \\ \vdots \\ h_{m,n} \end{pmatrix}_D
$$

then

$$
{\rm Rep}_{B,D}(h)=\left( \begin{array}{cccc} h_{1,1} &h_{1,2} &\ldots &h_{1,n}\\ h_{2,1} &h_{2,2} &\ldots &h_{2,n} \\ &\vdots\\ h_{m,1} &h_{m,2} &\ldots &h_{m,n} \end{array} \right)_{B,D}
$$

is the **matrix representation of $$h$$ with respect to $$B, D$$**.

Briefly, the vectors representing the $$h(\vec{\beta})$$'s are adjoined to make the matrix representing the map.

$$
{\rm Rep}_{B,D}(h)= \left(\begin{array}{c|c|c} \vdots & &\vdots \\ {\rm Rep}_{D}(\,h(\vec{\beta}_1)\,) &\cdots &{\rm Rep}_{D}(\,h(\vec{\beta}_n)\,) \\ \vdots & &\vdots \end{array}\right)
$$

Observe that the number of columns $$n$$ of the matrix is the dimension of the domain of the map, and the number of rows $$m$$ is the dimension of the codomain.

**Example 1.3**  —

If $$h:\mathbb{R}^3\to \mathcal{P}_1$$ is given by

$$
\begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} \stackrel{h}{\longmapsto} (2a_1+a_2)+(-a_3)x
$$

then where

$$
B= \langle \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix} \rangle \quad\text{and}\quad D= \langle 1+x,-1+x \rangle
$$

the action of $$h$$ on $$B$$ is given by

$$
\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}\stackrel{h}{\longmapsto}-x \qquad \begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix}\stackrel{h}{\longmapsto}2 \qquad \begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix}\stackrel{h}{\longmapsto}4
$$

and a simple calculation gives

$$
{\rm Rep}_{D}(-x)=\begin{pmatrix} -1/2 \\ -1/2 \end{pmatrix}_D \quad {\rm Rep}_{D}(2)=\begin{pmatrix} 1 \\ -1 \end{pmatrix}_D \quad {\rm Rep}_{D}(4)=\begin{pmatrix} 2 \\ -2 \end{pmatrix}_D
$$

showing that this is the matrix representing $$h$$ with respect to the bases.

$$
{\rm Rep}_{B,D}(h) = \begin{pmatrix} -1/2 &1 &2 \\ -1/2 &-1 &-2 \end{pmatrix}_{B,D}
$$

We will use lower case letters for a map, upper case for the matrix, and lower case again for the entries of the matrix. Thus for the map $$h$$, the matrix representing it is $$H$$, with entries $$h_{i,j}$$.

**Theorem 1.4**  —

Assume that $$V$$ and $$W$$ are vector spaces of dimensions $$m$$ and $$n$$ with bases $$B$$ and $$D$$, and that $$h:V\to W$$ is a linear map. If $$h$$ is represented by

$$
{\rm Rep}_{B,D}(h)=\left( \begin{array}{cccc} h_{1,1} &h_{1,2} &\ldots &h_{1,n}\\ h_{2,1} &h_{2,2} &\ldots &h_{2,n} \\ &\vdots\\ h_{m,1} &h_{m,2} &\ldots &h_{m,n} \end{array} \right)_{B,D}
$$

and $$\vec{v}\in V$$ is represented by

$$
{\rm Rep}_{B}(\vec{v})=\begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix}_B
$$

then the representation of the image of $$\vec{v}$$ is this.

$$
{\rm Rep}_{D}(\, h(\vec{v}) \,) = \begin{pmatrix} h_{1,1}c_1+h_{1,2}c_2+\dots+h_{1,n}c_n \\ h_{2,1}c_1+h_{2,2}c_2+\dots+h_{2,n}c_n \\ \vdots \\ h_{m,1}c_1+h_{m,2}c_2+\dots+h_{m,n}c_n \end{pmatrix}_D
$$

**Proof**  —

Problem 18.

We will think of the matrix $${\rm Rep}_{B,D}(h)$$ and the vector $${\rm Rep}_{B}(\vec{v})$$ as combining to make the vector $${\rm Rep}_{D}(h(\vec{v}))$$.

**Definition 1.5**  —

The **matrix-vector product** of a $$m \! \times \! n$$ matrix and a $$n \! \times \! 1$$ vector is this.

$$
\left( \begin{array}{cccc} a_{1,1} &a_{1,2} &\ldots &a_{1,n}\\ a_{2,1} &a_{2,2} &\ldots &a_{2,n} \\ &\vdots\\ a_{m,1} &a_{m,2} &\ldots &a_{m,n} \end{array} \right) \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix} = \begin{pmatrix} a_{1,1}c_1+a_{1,2}c_2+\dots+a_{1,n}c_n \\ a_{2,1}c_1+a_{2,2}c_2+\dots+a_{2,n}c_n \\ \vdots \\ a_{m,1}c_1+a_{m,2}c_2+\dots+a_{m,n}c_n \end{pmatrix}
$$

The point of Definition 1.2 is to generalize Example 1.1, that is, the point of the definition is Theorem 1.4, that the matrix describes how to get from the representation of a domain vector with respect to the domain's basis to the representation of its image in the codomain with respect to the codomain's basis. With Definition 1.5, we can restate this as: application of a linear map is represented by the matrix-vector product of the map's representative and the vector's representative.

**Example 1.6**  —

With the matrix from Example 1.3 we can calculate where that map sends this vector.

$$
\vec{v}=\begin{pmatrix} 4 \\ 1 \\ 0 \end{pmatrix}
$$

This vector is represented, with respect to the domain basis $$B$$, by

$$
{\rm Rep}_{B}(\vec{v})=\begin{pmatrix} 0 \\ 1/2 \\ 2 \end{pmatrix}_B
$$

and so this is the representation of the value $$h(\vec{v})$$ with respect to the codomain basis $$D$$.

$$
\begin{array}{rl} {\rm Rep}_{D}(h(\vec{v})) &=\begin{pmatrix} -1/2 &1 &2 \\ -1/2 &-1 &-2 \end{pmatrix}_{B,D} \begin{pmatrix} 0 \\ 1/2 \\ 2 \end{pmatrix}_B \\ &=\begin{pmatrix} (-1/2)\cdot 0+1\cdot (1/2) + 2\cdot 2 \\ (-1/2)\cdot 0-1\cdot (1/2) - 2\cdot 2 \end{pmatrix}_D =\begin{pmatrix} 9/2 \\ -9/2 \end{pmatrix}_D \end{array}
$$

To find $$h(\vec{v})$$ itself, not its representation, take $$(9/2)(1+x)-(9/2)(-1+x)=9$$.

**Example 1.7**  —

Let $$\pi:\mathbb{R}^3\to \mathbb{R}^2$$ be projection onto the $$xy$$-plane. To give a matrix representing this map, we first fix bases.

$$
B=\langle \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} \rangle \qquad D=\langle \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \end{pmatrix} \rangle
$$

For each vector in the domain's basis, we find its image under the map.

$$
\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}\stackrel{\pi}{\longmapsto}\begin{pmatrix} 1 \\ 0 \end{pmatrix} \quad \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}\stackrel{\pi}{\longmapsto}\begin{pmatrix} 1 \\ 1 \end{pmatrix} \quad \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}\stackrel{\pi}{\longmapsto}\begin{pmatrix} -1 \\ 0 \end{pmatrix}
$$

Then we find the representation of each image with respect to the codomain's basis

$$
{\rm Rep}_{D}(\begin{pmatrix} 1 \\ 0 \end{pmatrix})=\begin{pmatrix} 1 \\ -1 \end{pmatrix} \quad {\rm Rep}_{D}(\begin{pmatrix} 1 \\ 1 \end{pmatrix})=\begin{pmatrix} 0 \\ 1 \end{pmatrix} \quad {\rm Rep}_{D}(\begin{pmatrix} -1 \\ 0 \end{pmatrix})=\begin{pmatrix} -1 \\ 1 \end{pmatrix}
$$

(these are easily checked). Finally, adjoining these representations gives the matrix representing $$\pi$$ with respect to $$B,D$$.

$$
{\rm Rep}_{B,D}(\pi) =\begin{pmatrix} 1 &0 &-1 \\ -1 &1 &1 \end{pmatrix}_{B,D}
$$

We can illustrate Theorem 1.4 by computing the matrix-vector product representing the following statement about the projection map.

$$
\pi( \begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix} )=\begin{pmatrix} 2 \\ 2 \end{pmatrix}
$$

Representing this vector from the domain with respect to the domain's basis

$$
{\rm Rep}_{B}(\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix})= \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}_B
$$

gives this matrix-vector product.

$$
{\rm Rep}_{D}( \,\pi(\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix})\,)= \begin{pmatrix} 1 &0 &-1 \\ -1 &1 &1 \end{pmatrix}_{B,D} \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}_B = \begin{pmatrix} 0 \\ 2 \end{pmatrix}_D
$$

Expanding this representation into a linear combination of vectors from $$D$$

$$
0\cdot\begin{pmatrix} 2 \\ 1 \end{pmatrix} +2\cdot\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 2 \end{pmatrix}
$$

checks that the map's action is indeed reflected in the operation of the matrix. (We will sometimes compress these three displayed equations into one

$$
\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}=\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}_B \;\overset{h}{\underset{H}{\longmapsto}}\; \begin{pmatrix} 0 \\ 2 \end{pmatrix}_D=\begin{pmatrix} 2 \\ 2 \end{pmatrix}
$$

in the course of a calculation.)

We now have two ways to compute the effect of projection, the straightforward formula that drops each three-tall vector's third component to make a two-tall vector, and the above formula that uses representations and matrix-vector multiplication. Compared to the first way, the second way might seem complicated. However, it has advantages. The next example shows that giving a formula for some maps is simplified by this new scheme.

**Example 1.8**  —

To represent a **rotation** map $$t_{\theta}:\mathbb{R}^2\to \mathbb{R}^2$$ that turns all vectors in the plane counterclockwise through an angle $$\theta$$

we start by fixing bases. Using $$\mathcal{E}_2$$ both as a domain basis and as a codomain basis is natural, Now, we find the image under the map of each vector in the domain's basis.

$$
\begin{pmatrix} 1 \\ 0 \end{pmatrix}\stackrel{t_\theta}{\longmapsto}\begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix} \qquad \begin{pmatrix} 0 \\ 1 \end{pmatrix}\stackrel{t_\theta}{\longmapsto}\begin{pmatrix} -\sin\theta \\ \cos\theta \end{pmatrix}
$$

Then we represent these images with respect to the codomain's basis. Because this basis is $$\mathcal{E}_2$$, vectors are represented by themselves. Finally, adjoining the representations gives the matrix representing the map.

$$
{\rm Rep}_{\mathcal{E}_2,\mathcal{E}_2}(t_\theta) = \begin{pmatrix} \cos\theta &-\sin\theta \\ \sin\theta &\cos\theta \end{pmatrix}
$$

The advantage of this scheme is that just by knowing how to represent the image of the two basis vectors, we get a formula that tells us the image of any vector at all; here a vector rotated by $$\theta=\pi/6$$.

$$
\begin{pmatrix} 3 \\ -2 \end{pmatrix}\;\stackrel{t_{\pi/6}}{\longmapsto}\; \begin{pmatrix} \sqrt{3}/2 &-1/2 \\ 1/2 &\sqrt{3}/2 \end{pmatrix} \begin{pmatrix} 3 \\ -2 \end{pmatrix} \approx \begin{pmatrix} 3.598 \\ -0.232 \end{pmatrix}
$$

(Again, we are using the fact that, with respect to $$\mathcal{E}_2$$, vectors represent themselves.)

We have already seen the addition and scalar multiplication operations of matrices and the dot product operation of vectors. Matrix-vector multiplication is a new operation in the arithmetic of vectors and matrices. Nothing in Definition 1.5 requires us to view it in terms of representations. We can get some insight into this operation by turning away from what is being represented, and instead focusing on how the entries combine.

**Example 1.9**  —

In the definition the width of the matrix equals the height of the vector. Hence, the first product below is defined while the second is not.

$$
\begin{pmatrix} 1 &0 &0 \\ 4 &3 &1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 \\ 6 \end{pmatrix} \qquad \begin{pmatrix} 1 &0 &0 \\ 4 &3 &1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix}
$$

One reason that this product is not defined is purely formal: the definition requires that the sizes match, and these sizes don't match. Behind the formality, though, is a reason why we will leave it undefined— the matrix represents a map with a three-dimensional domain while the vector represents a member of a two-dimensional space.

A good way to view a matrix-vector product is as the dot products of the rows of the matrix with the column vector.

$$
\begin{pmatrix} &\vdots \\ a_{i,1} &a_{i,2} &\ldots &a_{i,n} \\ &\vdots \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix} = \begin{pmatrix} \vdots \\ a_{i,1}c_1+a_{i,2}c_2+\ldots+a_{i,n}c_n \\ \vdots \end{pmatrix}
$$

Looked at in this row-by-row way, this new operation generalizes dot product.

Matrix-vector product can also be viewed column-by-column.

$$
\begin{array}{rl} \left( \begin{array}{cccc} h_{1,1} &h_{1,2} &\ldots &h_{1,n}\\ h_{2,1} &h_{2,2} &\ldots &h_{2,n} \\ &\vdots\\ h_{m,1} &h_{m,2} &\ldots &h_{m,n} \end{array} \right) \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix} &=\begin{pmatrix} h_{1,1}c_1+h_{1,2}c_2+\dots+h_{1,n}c_n \\ h_{2,1}c_1+h_{2,2}c_2+\dots+h_{2,n}c_n \\ \vdots \\ h_{m,1}c_1+h_{m,2}c_2+\dots+h_{m,n}c_n \end{pmatrix} \\ &=c_1\begin{pmatrix} h_{1,1} \\ h_{2,1} \\ \vdots \\ h_{m,1} \end{pmatrix} +\dots +c_n\begin{pmatrix} h_{1,n} \\ h_{2,n} \\ \vdots \\ h_{m,n} \end{pmatrix} \end{array}
$$

**Example 1.10**  —

$$
\begin{pmatrix} 1 &0 &-1 \\ 2 &0 &3 \end{pmatrix} \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} = 2\begin{pmatrix} 1 \\ 2 \end{pmatrix} -1\begin{pmatrix} 0 \\ 0 \end{pmatrix} +1\begin{pmatrix} -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 1 \\ 7 \end{pmatrix}
$$

The result has the columns of the matrix weighted by the entries of the vector. This way of looking at it brings us back to the objective stated at the start of this section, to compute $$h(c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n)$$ as $$c_1h(\vec{\beta}_1)+\dots+c_nh(\vec{\beta}_n)$$.

We began this section by noting that the equality of these two enables us to compute the action of $$h$$ on any argument knowing only $$h(\vec{\beta}_1)$$, ..., $$h(\vec{\beta}_n)$$. We have developed this into a scheme to compute the action of the map by taking the matrix-vector product of the matrix representing the map and the vector representing the argument. In this way, any linear map is represented with respect to some bases by a matrix. In the next subsection, we will show the converse, that any matrix represents a linear map.  
### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Multiply the matrix

$$
\begin{pmatrix} 1 &3 &1 \\ 0 &-1 &2 \\ 1 &1 &0 \end{pmatrix}
$$

by each vector (or state "not defined").

1. $$\begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}$$
2. $$\begin{pmatrix} -2 \\ -2 \end{pmatrix}$$
3. $$\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$

**Problem 2**  —

Perform, if possible, each matrix-vector multiplication.

1. $$\begin{pmatrix} 2 &1 \\ 3 &-1/2 \end{pmatrix} \begin{pmatrix} 4 \\ 2 \end{pmatrix}$$
2. $$\begin{pmatrix} 1 &1 &0 \\ -2 &1 &0 \end{pmatrix} \begin{pmatrix} 1 \\ 3 \\ 1 \end{pmatrix}$$
3. $$\begin{pmatrix} 1 &1 \\ -2 &1 \end{pmatrix} \begin{pmatrix} 1 \\ 3 \\ 1 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

Solve this matrix equation.

$$
\begin{pmatrix} 2 &1 &1 \\ 0 &1 &3 \\ 1 &-1 &2 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} =\begin{pmatrix} 8 \\ 4 \\ 4 \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 4**  —

For a homomorphism from $$\mathcal{P}_2$$ to $$\mathcal{P}_3$$ that sends

$$
1\mapsto 1+x, \quad x\mapsto 1+2x, \quad\text{and}\quad x^2\mapsto x-x^3
$$

where does $$1-3x+2x^2$$ go?  
*This exercise is recommended for all readers.*

**Problem 5**  —

Assume that $$h:\mathbb{R}^2\to \mathbb{R}^3$$ is determined by this action.

$$
\begin{pmatrix} 1 \\ 0 \end{pmatrix}\mapsto\begin{pmatrix} 2 \\ 2 \\ 0 \end{pmatrix} \qquad \begin{pmatrix} 0 \\ 1 \end{pmatrix}\mapsto\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}
$$

Using the standard bases, find

1. the matrix representing this map;
2. a general formula for $$h(\vec{v})$$.  
*This exercise is recommended for all readers.*

**Problem 6**  —

Let $$d/dx:\mathcal{P}_3\to \mathcal{P}_3$$ be the derivative transformation.

1. Represent $$d/dx$$ with respect to $$B,B$$ where $$B=\langle 1,x,x^2,x^3 \rangle$$.
2. Represent $$d/dx$$ with respect to $$B,D$$ where $$D=\langle 1,2x,3x^2,4x^3 \rangle$$.  
*This exercise is recommended for all readers.*

**Problem 7**  —

Represent each linear map with respect to each pair of bases.

1. $$d/dx:\mathcal{P}_n\to \mathcal{P}_n$$ with respect to $$B,B$$ where $$B=\langle 1,x,\dots,x^n \rangle$$, given by

$$
a_0+a_1x+a_2x^2+\dots+a_nx^n \mapsto a_1+2a_2x+\dots+na_nx^{n-1}
$$

2. $$\int:\mathcal{P}_n\to \mathcal{P}_{n+1}$$ with respect to $$B_n,B_{n+1}$$ where $$B_i=\langle 1,x,\dots,x^i \rangle$$, given by

$$
a_0+a_1x+a_2x^2+\dots+a_nx^n \mapsto a_0x+\frac{a_1}{2}x^2+\dots+\frac{a_n}{n+1}x^{n+1}
$$

3. $$\int^1_0:\mathcal{P}_n\to \mathbb{R}$$ with respect to $$B,\mathcal{E}_1$$ where $$B=\langle 1,x,\dots,x^n \rangle$$ and $$\mathcal{E}_1=\langle 1 \rangle$$, given by

$$
a_0+a_1x+a_2x^2+\dots+a_nx^n \mapsto a_0+\frac{a_1}{2}+\dots+\frac{a_n}{n+1}
$$

4. $$\text{eval}_3:\mathcal{P}_n\to \mathbb{R}$$ with respect to $$B,\mathcal{E}_1$$ where $$B=\langle 1,x,\dots,x^n \rangle$$ and $$\mathcal{E}_1=\langle 1 \rangle$$, given by

$$
a_0+a_1x+a_2x^2+\dots+a_nx^n \mapsto a_0+a_1\cdot 3+a_2\cdot 3^2+\dots+a_n\cdot 3^n
$$

5. $$\text{slide}_{-1}:\mathcal{P}_n\to \mathcal{P}_n$$ with respect to $$B,B$$ where $$B=\langle 1,x,\ldots,x^n \rangle$$, given by

$$
a_0+a_1x+a_2x^2+\dots+a_nx^n \mapsto a_0+a_1\cdot (x+1)+\dots+a_n\cdot (x+1)^n
$$

**Problem 8**  —

Represent the identity map on any nontrivial space with respect to $$B,B$$, where $$B$$ is any basis.

**Problem 9**  —

Represent, with respect to the natural basis, the transpose transformation on the space $$\mathcal{M}_{2 \! \times \! 2}$$ of $$2 \! \times \! 2$$ matrices.

**Problem 10**  —

Assume that $$B=\langle \vec{\beta}_1,\vec{\beta}_2,\vec{\beta}_3,\vec{\beta}_4 \rangle$$ is a basis for a vector space. Represent with respect to $$B,B$$ the transformation that is determined by each.

1. $$\vec{\beta}_1\mapsto\vec{\beta}_2$$, $$\vec{\beta}_2\mapsto\vec{\beta}_3$$, $$\vec{\beta}_3\mapsto\vec{\beta}_4$$, $$\vec{\beta}_4\mapsto\vec{0}$$
2. $$\vec{\beta}_1\mapsto\vec{\beta}_2$$, $$\vec{\beta}_2\mapsto\vec{0}$$, $$\vec{\beta}_3\mapsto\vec{\beta}_4$$, $$\vec{\beta}_4\mapsto\vec{0}$$
3. $$\vec{\beta}_1\mapsto\vec{\beta}_2$$, $$\vec{\beta}_2\mapsto\vec{\beta}_3$$, $$\vec{\beta}_3\mapsto\vec{0}$$, $$\vec{\beta}_4\mapsto\vec{0}$$

**Problem 11**  —

Example 1.8 shows how to represent the rotation transformation of the plane with respect to the standard basis. Express these other transformations also with respect to the standard basis.

1. the **dilation** map $$d_s$$, which multiplies all vectors by the same scalar $$s$$
2. the **reflection** map $$f_\ell$$, which reflects all all vectors across a line $$\ell$$ through the origin  
*This exercise is recommended for all readers.*

**Problem 12**  —

Consider a linear transformation of $$\mathbb{R}^2$$ determined by these two.

$$
\begin{pmatrix} 1 \\ 1 \end{pmatrix}\mapsto\begin{pmatrix} 2 \\ 0 \end{pmatrix} \qquad \begin{pmatrix} 1 \\ 0 \end{pmatrix}\mapsto\begin{pmatrix} -1 \\ 0 \end{pmatrix}
$$

1. Represent this transformation with respect to the standard bases.
2. Where does the transformation send this vector?

$$
\begin{pmatrix} 0 \\ 5 \end{pmatrix}
$$

3. Represent this transformation with respect to these bases.

$$
B=\langle \begin{pmatrix} 1 \\ -1 \end{pmatrix},\begin{pmatrix} 1 \\ 1 \end{pmatrix} \rangle \qquad D=\langle \begin{pmatrix} 2 \\ 2 \end{pmatrix},\begin{pmatrix} -1 \\ 1 \end{pmatrix} \rangle
$$

4. Using $$B$$ from the prior item, represent the transformation with respect to $$B,B$$.

**Problem 13**  —

Suppose that $$h:V\to W$$ is nonsingular so that by [Theorem II.2.21](Linear%20Algebra%20-%20Rangespace%20and%20Nullspace.md), for any basis $$B=\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle \subset V$$ the image $$h(B)=\langle h(\vec{\beta}_1),\dots,h(\vec{\beta}_n) \rangle$$ is a basis for $$W$$.

1. Represent the map $$h$$ with respect to $$B,h(B)$$.
2. For a member $$\vec{v}$$ of the domain, where the representation of $$\vec{v}$$ has components $$c_1$$, ..., $$c_n$$, represent the image vector $$h(\vec{v})$$ with respect to the image basis $$h(B)$$.

**Problem 14**  —

Give a formula for the product of a matrix and $$\vec{e}_i$$, the column vector that is all zeroes except for a single one in the $$i$$-th position.  
*This exercise is recommended for all readers.*

**Problem 15**  —

For each vector space of functions of one real variable, represent the derivative transformation with respect to $$B,B$$.

1. $$\{a\cos x+b\sin x \,\big|\, a,b\in\mathbb{R}\}$$, $$B=\langle \cos x,\sin x \rangle$$
2. $$\{ae^x+be^{2x} \,\big|\, a,b\in\mathbb{R}\}$$, $$B=\langle e^x,e^{2x} \rangle$$
3. $$\{a+bx+ce^x+dxe^{x} \,\big|\, a,b,c,d\in\mathbb{R}\}$$, $$B=\langle 1,x,e^x,xe^{x} \rangle$$

**Problem 16**  —

Find the range of the linear transformation of $$\mathbb{R}^2$$ represented with respect to the standard bases by each matrix.

1. $$\begin{pmatrix} 1 &0 \\ 0 &0 \end{pmatrix}$$
2. $$\begin{pmatrix} 0 &0 \\ 3 &2 \end{pmatrix}$$
3. a matrix of the form $$\begin{pmatrix} a &b \\ 2a &2b \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 17**  —

Can one matrix represent two different linear maps? That is, can $${\rm Rep}_{B,D}(h)={\rm Rep}_{\hat{B},\hat{D}}(\hat{h})$$?

**Problem 18**  —

Prove Theorem 1.4.  
*This exercise is recommended for all readers.*

**Problem 19**  —

Example 1.8 shows how to represent rotation of all vectors in the plane through an angle $$\theta$$ about the origin, with respect to the standard bases.

1. Rotation of all vectors in three-space through an angle $$\theta$$ about the $$x$$-axis is a transformation of $$\mathbb{R}^3$$. Represent it with respect to the standard bases. Arrange the rotation so that to someone whose feet are at the origin and whose head is at $$(1,0,0)$$, the movement appears clockwise.
2. Repeat the prior item, only rotate about the $$y$$-axis instead. (Put the person's head at $$\vec{e}_2$$.)
3. Repeat, about the $$z$$-axis.
4. Extend the prior item to $$\mathbb{R}^4$$. (*Hint:* "rotate about the $$z$$-axis" can be restated as "rotate parallel to the $$xy$$-plane".)

**Problem 20 (Schur's Triangularization Lemma)**  —

1. Let $$U$$ be a subspace of $$V$$ and fix bases $$B_U\subseteq B_V$$. What is the relationship between the representation of a vector from $$U$$ with respect to $$B_U$$ and the representation of that vector (viewed as a member of $$V$$) with respect to $$B_V$$?
2. What about maps?
3. Fix a basis $$B=\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ for $$V$$ and observe that the spans

$$
[\{\vec{0}\}]=\{\vec{0}\}\subset[\{\vec{\beta}_1\}] \subset[\{\vec{\beta}_1,\vec{\beta}_2\}] \subset \quad\cdots\quad \subset[B]=V
$$

form a strictly increasing chain of subspaces. Show that for any linear map $$h:V\to W$$ there is a chain $$W_0=\{\vec{0}\}\subseteq W_1\subseteq \dots \subseteq W_m =W$$ of subspaces of $$W$$ such that

$$
h([\{\vec{\beta}_1,\dots,\vec{\beta}_i\}])\subset W_i
$$

for each $$i$$.
4. Conclude that for every linear map $$h:V\to W$$ there are bases $$B,D$$ so the matrix representing $$h$$ with respect to $$B,D$$ is upper-triangular (that is, each entry $$h_{i,j}$$ with $$i>j$$ is zero).
5. Is an upper-triangular representation unique?

Solutions

---

*Source: Wikibooks, Linear Algebra/Representing Linear Maps with Matrices (https://en.wikibooks.org/wiki/Linear_Algebra/Representing_Linear_Maps_with_Matrices), by Wikibooks contributors, CC BY-SA 4.0.*
