# Any Matrix Represents a Linear Map

The prior subsection shows that the action of a linear map $$h$$ is described by a matrix $$H$$, with respect to appropriate bases, in this way.

$$
\vec{v}=\begin{pmatrix} v_1 \\ \vdots \\ v_n \end{pmatrix}_B \;\overset{h}{\underset{H}{\longmapsto}}\; \begin{pmatrix} h_{1,1}v_1+\dots+h_{1,n}v_n \\ \vdots \\ h_{m,1}v_1+\dots+h_{m,n}v_n \end{pmatrix}_D =h(\vec{v})
$$

In this subsection, we will show the converse, that each matrix represents a linear map.

Recall that, in the definition of the matrix representation of a linear map, the number of columns of the matrix is the dimension of the map's domain and the number of rows of the matrix is the dimension of the map's codomain. Thus, for instance, a $$2 \! \times \! 3$$ matrix cannot represent a map from $$\mathbb{R}^5$$ to $$\mathbb{R}^4$$. The next result says that, beyond this restriction on the dimensions, there are no other limitations: the $$2 \! \times \! 3$$ matrix represents a map from any three-dimensional space to any two-dimensional space.

**Theorem 2.1**  —

Any matrix represents a homomorphism between vector spaces of appropriate dimensions, with respect to any pair of bases.

**Proof**  —

For the matrix

$$
H=\left( \begin{array}{cccc} h_{1,1} &h_{1,2} &\ldots &h_{1,n}\\ h_{2,1} &h_{2,2} &\ldots &h_{2,n} \\ &\vdots\\ h_{m,1} &h_{m,2} &\ldots &h_{m,n} \end{array} \right)
$$

fix any $$n$$-dimensional domain space $$V$$ and any $$m$$-dimensional codomain space $$W$$. Also fix bases $$B=\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ and $$D=\langle \vec{\delta}_1,\dots,\vec{\delta}_m \rangle$$ for those spaces. Define a function $$h:V\to W$$ by: where $$\vec{v}$$ in the domain is represented as

$$
{\rm Rep}_{B}(\vec{v}) =\begin{pmatrix} v_1 \\ \vdots \\ v_n \end{pmatrix}_B
$$

then its image $$h(\vec{v})$$ is the member the codomain represented by

$$
{\rm Rep}_{D}(\,h(\vec{v})\,) =\begin{pmatrix} h_{1,1}v_1+\dots+h_{1,n}v_n \\ \vdots \\ h_{m,1}v_1+\dots+h_{m,n}v_n \end{pmatrix}_D
$$

that is, $$h(\vec{v})=h(v_1\vec{\beta}_1+\dots+v_n\vec{\beta}_n)$$ is defined to be $$(h_{1,1}v_1+\dots+h_{1,n}v_n)\cdot\vec{\delta}_1 +\dots+ (h_{m,1}v_1+\dots+h_{m,n}v_n)\cdot\vec{\delta}_m$$. (This is well-defined by the uniqueness of the representation $${\rm Rep}_{B}(\vec{v})$$.)

Observe that $$h$$ has simply been defined to make it the map that is represented with respect to $$B,D$$ by the matrix $$H$$. So to finish, we need only check that $$h$$ is linear. If $$\vec{v}, \vec{u}\in V$$ are such that

$$
{\rm Rep}_{B}(\vec{v})=\begin{pmatrix} v_1 \\ \vdots \\ v_n \end{pmatrix} \quad\text{and}\quad {\rm Rep}_{B}(\vec{u})=\begin{pmatrix} u_1 \\ \vdots \\ u_n \end{pmatrix}
$$

and $$c,d\in\mathbb{R}$$ then the calculation

$$
\begin{array}{rl} h(c\vec{v}+d\vec{u}) &=\bigl(h_{1,1}(cv_1+du_1)+\dots+ h_{1,n}(cv_n+du_n)\bigr)\cdot\vec{\delta}_1+ \\ & \quad\cdots+\bigl(h_{m,1}(cv_1+du_1)+\dots +h_{m,n}(cv_n+du_n)\bigr)\cdot\vec{\delta}_m \\ &=c\cdot h(\vec{v})+d\cdot h(\vec{u}) \end{array}
$$

provides this verification.

**Example 2.2**  —

Which map the matrix represents depends on which bases are used. If

$$
H= \begin{pmatrix} 1 &0 \\ 0 &0 \end{pmatrix}, \quad B_1=D_1=\langle \begin{pmatrix} 1 \\ 0 \end{pmatrix},\begin{pmatrix} 0 \\ 1 \end{pmatrix} \rangle , \quad\text{and}\quad B_2=D_2=\langle \begin{pmatrix} 0 \\ 1 \end{pmatrix},\begin{pmatrix} 1 \\ 0 \end{pmatrix} \rangle ,
$$

then $$h_1:\mathbb{R}^2\to \mathbb{R}^2$$ represented by $$H$$ with respect to $$B_1,D_1$$ maps

$$
\begin{pmatrix} c_1 \\ c_2 \end{pmatrix} =\begin{pmatrix} c_1 \\ c_2 \end{pmatrix}_{B_1} \quad \mapsto \quad \begin{pmatrix} c_1 \\ 0 \end{pmatrix}_{D_1} = \begin{pmatrix} c_1 \\ 0 \end{pmatrix}
$$

while $$h_2:\mathbb{R}^2\to \mathbb{R}^2$$ represented by $$H$$ with respect to $$B_2,D_2$$ is this map.

$$
\begin{pmatrix} c_1 \\ c_2 \end{pmatrix} =\begin{pmatrix} c_2 \\ c_1 \end{pmatrix}_{B_2} \quad \mapsto \quad \begin{pmatrix} c_2 \\ 0 \end{pmatrix}_{D_2} = \begin{pmatrix} 0 \\ c_2 \end{pmatrix}
$$

These two are different. The first is projection onto the $$x$$ axis, while the second is projection onto the $$y$$ axis.

So not only is any linear map described by a matrix but any matrix describes a linear map. This means that we can, when convenient, handle linear maps entirely as matrices, simply doing the computations, without have to worry that a matrix of interest does not represent a linear map on some pair of spaces of interest. (In practice, when we are working with a matrix but no spaces or bases have been specified, we will often take the domain and codomain to be $$\mathbb{R}^n$$ and $$\mathbb{R}^m$$ and use the standard bases. In this case, because the representation is transparent— the representation with respect to the standard basis of $$\vec{v}$$ is $$\vec{v}$$— the column space of the matrix equals the range of the map. Consequently, the column space of $$H$$ is often denoted by $$\mathcal{R}(H)$$.)

With the theorem, we have characterized linear maps as those maps that act in this matrix way. Each linear map is described by a matrix and each matrix describes a linear map. We finish this section by illustrating how a matrix can be used to tell things about its maps.

**Theorem 2.3**  —

The rank of a matrix equals the rank of any map that it represents.

**Proof**  —

Suppose that the matrix $$H$$ is $$m \! \times \! n$$. Fix domain and codomain spaces $$V$$ and $$W$$ of dimension $$n$$ and $$m$$, with bases $$B=\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ and $$D$$. Then $$H$$ represents some linear map $$h$$ between those spaces with respect to these bases whose rangespace

$$
\begin{array}{rl} \{h(\vec{v})\,\big|\, \vec{v}\in V\} &=\{h(c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n) \,\big|\, c_1,\dots,c_n\in\mathbb{R}\} \\ &=\{c_1h(\vec{\beta}_1)+\dots+c_nh(\vec{\beta}_n) \,\big|\, c_1,\dots,c_n\in\mathbb{R}\} \end{array}
$$

is the span $$[\{h(\vec{\beta}_1),\dots,h(\vec{\beta}_n)\}]$$. The rank of $$h$$ is the dimension of this rangespace.

The rank of the matrix is its column rank (or its row rank; the two are equal). This is the dimension of the column space of the matrix, which is the span of the set of column vectors $$[\{{\rm Rep}_{D}(h(\vec{\beta}_1)),\dots,{\rm Rep}_{D}(h(\vec{\beta}_n))\}]$$.

To see that the two spans have the same dimension, recall that a representation with respect to a basis gives an isomorphism $$\text{Rep}_D:W\to \mathbb{R}^m$$. Under this isomorphism, there is a linear relationship among members of the rangespace if and only if the same relationship holds in the column space, e.g, $$\vec{0}=c_1h(\vec{\beta}_1)+\dots+c_nh(\vec{\beta}_n)$$ if and only if $$\vec{0}=c_1{\rm Rep}_{D}(h(\vec{\beta}_1))+\dots+c_n{\rm Rep}_{D}(h(\vec{\beta}_n))$$. Hence, a subset of the rangespace is linearly independent if and only if the corresponding subset of the column space is linearly independent. This means that the size of the largest linearly independent subset of the rangespace equals the size of the largest linearly independent subset of the column space, and so the two spaces have the same dimension.

**Example 2.4**  —

Any map represented by

$$
\begin{pmatrix} 1 &2 &2 \\ 1 &2 &1 \\ 0 &0 &3 \\ 0 &0 &2 \end{pmatrix}
$$

must, by definition, be from a three-dimensional domain to a four-dimensional codomain. In addition, because the rank of this matrix is two (we can spot this by eye or get it with Gauss' method), any map represented by this matrix has a two-dimensional rangespace.

**Corollary 2.5**  —

Let $$h$$ be a linear map represented by a matrix $$H$$. Then $$h$$ is onto if and only if the rank of $$H$$ equals the number of its rows, and $$h$$ is one-to-one if and only if the rank of $$H$$ equals the number of its columns.

**Proof**  —

For the first half, the dimension of the rangespace of $$h$$ is the rank of $$h$$, which equals the rank of $$H$$ by the theorem. Since the dimension of the codomain of $$h$$ is the number of rows in $$H$$, if the rank of $$H$$ equals the number of rows, then the dimension of the rangespace equals the dimension of the codomain. But a subspace with the same dimension as its superspace must equal that superspace (a basis for the rangespace is a linearly independent subset of the codomain, whose size is equal to the dimension of the codomain, and so this set is a basis for the codomain).

For the second half, a linear map is one-to-one if and only if it is an isomorphism between its domain and its range, that is, if and only if its domain has the same dimension as its range. But the number of columns in $$H$$ is the dimension of $$h$$'s domain, and by the theorem the rank of $$H$$ equals the dimension of $$h$$'s range.

The above results end any confusion caused by our use of the word "rank" to mean apparently different things when applied to matrices and when applied to maps. We can also justify the dual use of "nonsingular". We've defined a matrix to be nonsingular if it is square and is the matrix of coefficients of a linear system with a unique solution, and we've defined a linear map to be nonsingular if it is one-to-one.

**Corollary 2.6**  —

A square matrix represents nonsingular maps if and only if it is a nonsingular matrix. Thus, a matrix represents an isomorphism if and only if it is square and nonsingular.

**Proof**  —

Immediate from the prior result.

**Example 2.7**  —

Any map from $$\mathbb{R}^2$$ to $$\mathcal{P}_1$$ represented with respect to any pair of bases by

$$
\begin{pmatrix} 1 &2 \\ 0 &3 \end{pmatrix}
$$

is nonsingular because this matrix has rank two.

**Example 2.8**  —

Any map $$g:V\to W$$ represented by

$$
\begin{pmatrix} 1 &2 \\ 3 &6 \end{pmatrix}
$$

is not nonsingular because this matrix is not nonsingular.

We've now seen that the relationship between maps and matrices goes both ways: fixing bases, any linear map is represented by a matrix and any matrix describes a linear map. That is, by fixing spaces and bases we get a correspondence between maps and matrices. In the rest of this chapter we will explore this correspondence. For instance, we've defined for linear maps the operations of addition and scalar multiplication and we shall see what the corresponding matrix operations are. We shall also see the matrix operation that represent the map operation of composition. And, we shall see how to find the matrix that represents a map's inverse.  
### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Decide if the vector is in the column space of the matrix.

1. $$\begin{pmatrix} 2 &1 \\ 2 &5 \end{pmatrix}$$, $$\begin{pmatrix} 1 \\ -3 \end{pmatrix}$$
2. $$\begin{pmatrix} 4 &-8 \\ 2 &-4 \end{pmatrix}$$, $$\begin{pmatrix} 0 \\ 1 \end{pmatrix}$$
3. $$\begin{pmatrix} 1 &-1 &1 \\ 1 &1 &-1 \\ -1 &-1 &1 \end{pmatrix}$$, $$\begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Decide if each vector lies in the range of the map from $$\mathbb{R}^3$$ to $$\mathbb{R}^2$$ represented with respect to the standard bases by the matrix.

1. $$\begin{pmatrix} 1 &1 &3 \\ 0 &1 &4 \end{pmatrix}$$, $$\begin{pmatrix} 1 \\ 3 \end{pmatrix}$$
2. $$\begin{pmatrix} 2 &0 &3 \\ 4 &0 &6 \end{pmatrix}$$, $$\begin{pmatrix} 1 \\ 1 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

Consider this matrix, representing a transformation of $$\mathbb{R}^2$$, and these bases for that space.

$$
\frac{1}{2}\cdot \begin{pmatrix} 1 &1 \\ -1 &1 \end{pmatrix} \qquad B=\langle \begin{pmatrix} 0 \\ 1 \end{pmatrix},\begin{pmatrix} 1 \\ 0 \end{pmatrix} \rangle \quad D=\langle \begin{pmatrix} 1 \\ 1 \end{pmatrix},\begin{pmatrix} 1 \\ -1 \end{pmatrix} \rangle
$$

1. To what vector in the codomain is the first member of $$B$$ mapped?
2. The second member?
3. Where is a general vector from the domain (a vector with components $$x$$ and $$y$$) mapped? That is, what transformation of $$\mathbb{R}^2$$ is represented with respect to $$B,D$$ by this matrix?

**Problem 4**  —

What transformation of $$F=\{a\cos\theta+b\sin\theta\,\big|\, a,b\in\mathbb{R}\}$$ is represented with respect to $$B=\langle \cos\theta-\sin\theta,\sin\theta \rangle$$ and $$D=\langle \cos\theta+\sin\theta,\cos\theta \rangle$$ by this matrix?

$$
\begin{pmatrix} 0 &0 \\ 1 &0 \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 5**  —

Decide if $$1+2x$$ is in the range of the map from $$\mathbb{R}^3$$ to $$\mathcal{P}_2$$ represented with respect to $$\mathcal{E}_3$$ and $$\langle 1,1+x^2,x \rangle$$ by this matrix.

$$
\begin{pmatrix} 1 &3 &0 \\ 0 &1 &0 \\ 1 &0 &1 \end{pmatrix}
$$

**Problem 6**  —

Example 2.8 gives a matrix that is nonsingular, and is therefore associated with maps that are nonsingular.

1. Find the set of column vectors representing the members of the nullspace of any map represented by this matrix.
2. Find the nullity of any such map.
3. Find the set of column vectors representing the members of the rangespace of any map represented by this matrix.
4. Find the rank of any such map.
5. Check that rank plus nullity equals the dimension of the domain.  
*This exercise is recommended for all readers.*

**Problem 7**  —

Because the rank of a matrix equals the rank of any map it represents, if one matrix represents two different maps $$H={\rm Rep}_{B,D}(h)={\rm Rep}_{\hat{B},\hat{D}}(\hat{h})$$ (where $$h,\hat{h}:V\to W$$) then the dimension of the rangespace of $$h$$ equals the dimension of the rangespace of $$\hat{h}$$. Must these equal-dimensioned rangespaces actually be the same?  
*This exercise is recommended for all readers.*

**Problem 8**  —

Let $$V$$ be an $$n$$-dimensional space with bases $$B$$ and $$D$$. Consider a map that sends, for $$\vec{v}\in V$$, the column vector representing $$\vec{v}$$ with respect to $$B$$ to the column vector representing $$\vec{v}$$ with respect to $$D$$. Show that is a linear transformation of $$\mathbb{R}^n$$.

**Problem 9**  —

Example 2.2 shows that changing the pair of bases can change the map that a matrix represents, even though the domain and codomain remain the same. Could the map ever not change? Is there a matrix $$H$$, vector spaces $$V$$ and $$W$$, and associated pairs of bases $$B_1,D_1$$ and $$B_2,D_2$$ (with $$B_1\neq B_2$$ or $$D_1\neq D_2$$ or both) such that the map represented by $$H$$ with respect to $$B_1,D_1$$ equals the map represented by $$H$$ with respect to $$B_2,D_2$$?  
*This exercise is recommended for all readers.*

**Problem 10**  —

A square matrix is a **diagonal** matrix if it is all zeroes except possibly for the entries on its upper-left to lower-right diagonal— its $$1,1$$ entry, its $$2,2$$ entry, etc. Show that a linear map is an isomorphism if there are bases such that, with respect to those bases, the map is represented by a diagonal matrix with no zeroes on the diagonal.

**Problem 11**  —

Describe geometrically the action on $$\mathbb{R}^2$$ of the map represented with respect to the standard bases $$\mathcal{E}_2,\mathcal{E}_2$$ by this matrix.

$$
\begin{pmatrix} 3 &0 \\ 0 &2 \end{pmatrix}
$$

Do the same for these.

$$
\begin{pmatrix} 1 &0 \\ 0 &0 \end{pmatrix} \quad \begin{pmatrix} 0 &1 \\ 1 &0 \end{pmatrix} \quad \begin{pmatrix} 1 &3 \\ 0 &1 \end{pmatrix}
$$

**Problem 12**  —

The fact that for any linear map the rank plus the nullity equals the dimension of the domain shows that a necessary condition for the existence of a homomorphism between two spaces, onto the second space, is that there be no gain in dimension. That is, where $$h:V\to W$$ is onto, the dimension of $$W$$ must be less than or equal to the dimension of $$V$$.

1. Show that this (strong) converse holds: no gain in dimension implies that there is a homomorphism and, further, any matrix with the correct size and correct rank represents such a map.
2. Are there bases for $$\mathbb{R}^3$$ such that this matrix

$$
H=\begin{pmatrix} 1 &0 &0 \\ 2 &0 &0 \\ 0 &1 &0 \end{pmatrix}
$$

represents a map from $$\mathbb{R}^3$$ to $$\mathbb{R}^3$$ whose range is the $$xy$$ plane subspace of $$\mathbb{R}^3$$?

**Problem 13**  —

Let $$V$$ be an $$n$$-dimensional space and suppose that $$\vec{x}\in\mathbb{R}^n$$. Fix a basis $$B$$ for $$V$$ and consider the map $$h_{\vec{x}}:V\to \mathbb{R}$$ given $$\vec{v}\mapsto\vec{x}\cdot{\rm Rep}_{B}(\vec{v})$$ by the dot product.

1. Show that this map is linear.
2. Show that for any linear map $$g:V\to \mathbb{R}$$ there is an $$\vec{x}\in\mathbb{R}^n$$ such that $$g=h_{\vec{x}}$$.
3. In the prior item we fixed the basis and varied the $$\vec{x}$$ to get all possible linear maps. Can we get all possible linear maps by fixing an $$\vec{x}$$ and varying the basis?

**Problem 14**  —

Let $$V,W,X$$ be vector spaces with bases $$B,C,D$$.

1. Suppose that $$h:V\to W$$ is represented with respect to $$B,C$$ by the matrix $$H$$. Give the matrix representing the scalar multiple $$rh$$ (where $$r\in\mathbb{R}$$) with respect to $$B,C$$ by expressing it in terms of $$H$$.
2. Suppose that $$h,g:V\to W$$ are represented with respect to $$B,C$$ by $$H$$ and $$G$$. Give the matrix representing $$h+g$$ with respect to $$B,C$$ by expressing it in terms of $$H$$ and $$G$$.
3. Suppose that $$h:V\to W$$ is represented with respect to $$B,C$$ by $$H$$ and $$g:W\to X$$ is represented with respect to $$C,D$$ by $$G$$. Give the matrix representing $$g\circ h$$ with respect to $$B,D$$ by expressing it in terms of $$H$$ and $$G$$.

Solutions

---

*Source: Wikibooks, Linear Algebra/Any Matrix Represents a Linear Map (https://en.wikibooks.org/wiki/Linear_Algebra/Any_Matrix_Represents_a_Linear_Map), by Wikibooks contributors, CC BY-SA 4.0.*
