# Rangespace and Nullspace

Isomorphisms and homomorphisms both preserve structure. The difference is that homomorphisms needn't be onto and needn't be one-to-one. This means that homomorphisms are a more general kind of map, subject to fewer restrictions than isomorphisms. We will examine what can happen with homomorphisms that is prevented by the extra restrictions satisfied by isomorphisms.

We first consider the effect of dropping the onto requirement, of not requiring as part of the definition that a homomorphism be onto its codomain. For instance, the injection map $$\iota:\mathbb{R}^2\to \mathbb{R}^3$$

$$
\begin{pmatrix} x \\ y \end{pmatrix} \mapsto \begin{pmatrix} x \\ y \\ 0 \end{pmatrix}
$$

is not an isomorphism because it is not onto. Of course, being a function, a homomorphism is onto some set, namely its range; the map $$\iota$$ is onto the $$xy$$-plane subset of $$\mathbb{R}^3$$.

**Lemma 2.1**  —

Under a homomorphism, the image of any subspace of the domain is a subspace of the codomain. In particular, the image of the entire space, the range of the homomorphism, is a subspace of the codomain.

**Proof**  —

Let $$h:V\to W$$ be linear and let $$S$$ be a subspace of the domain $$V$$. The image $$h(S)$$ is a subset of the codomain $$W$$. It is nonempty because $$S$$ is nonempty and thus to show that $$h(S)$$ is a subspace of $$W$$ we need only show that it is closed under linear combinations of two vectors. If $$h(\vec{s}_1)$$ and $$h(\vec{s}_2)$$ are members of $$h(S)$$ then $$c_1\cdot h(\vec{s}_1)+c_2\cdot h(\vec{s}_2) = h(c_1\cdot \vec{s}_1)+h(c_2\cdot \vec{s}_2) = h(c_1\cdot \vec{s}_1+c_2\cdot \vec{s}_2)$$ is also a member of $$h(S)$$ because it is the image of $$c_1\cdot \vec{s}_1+c_2\cdot \vec{s}_2$$ from $$S$$.

**Definition 2.2**  —

The **rangespace** of a homomorphism $$h:V\to W$$ is

$$
\mathcal{R}(h)=\{h(\vec{v})\,\big|\, \vec{v}\in V\}
$$

sometimes denoted $$h(V)$$. The dimension of the rangespace is the map's **rank**.

(We shall soon see the connection between the rank of a map and the rank of a matrix.)

**Example 2.3**  —

Recall that the derivative map $$d/dx:\mathcal{P}_3\to \mathcal{P}_3$$ given by $$a_0+a_1x+a_2x^2+a_3x^3 \mapsto a_1+2a_2x+3a_3x^2$$ is linear. The rangespace $$\mathcal{R}(d/dx)$$ is the set of quadratic polynomials $$\{r+sx+tx^2\,\big|\, r,s,t\in\mathbb{R} \}$$. Thus, the rank of this map is three.

**Example 2.4**  —

With this homomorphism $$h:M_{2 \! \times \! 2}\to \mathcal{P}_3$$

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \mapsto (a+b+2d)+0x+cx^2+cx^3
$$

an image vector in the range can have any constant term, must have an $$x$$ coefficient of zero, and must have the same coefficient of $$x^2$$ as of $$x^3$$. That is, the rangespace is $$\mathcal{R}(h)=\{r+0x+sx^2+sx^3\,\big|\, r,s\in\mathbb{R}\}$$ and so the rank is two.

The prior result shows that, in passing from the definition of isomorphism to the more general definition of homomorphism, omitting the "onto" requirement doesn't make an essential difference. Any homomorphism is onto its rangespace.

However, omitting the "one-to-one" condition does make a difference. A homomorphism may have many elements of the domain that map to one element of the codomain. Below is a "bean " sketch of a many-to-one map between sets. It shows three elements of the codomain that are each the image of many members of the domain.

Recall that for any function $$h:V\to W$$, the set of elements of $$V$$ that are mapped to $$\vec{w}\in W$$ is the **inverse image** $$h^{-1}(\vec{w})=\{\vec{v}\in V\,\big|\, h(\vec{v})=\vec{w}\}$$. Above, the three sets of many elements on the left are inverse images.

**Example 2.5**  —

Consider the projection $$\pi:\mathbb{R}^3\to \mathbb{R}^2$$

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} \stackrel{\pi}{\longmapsto} \begin{pmatrix} x \\ y \end{pmatrix}
$$

which is a homomorphism that is many-to-one. In this instance, an inverse image set is a vertical line of vectors in the domain.

**Example 2.6**  —

This homomorphism $$h:\mathbb{R}^2\to \mathbb{R}^1$$

$$
\begin{pmatrix} x \\ y \end{pmatrix} \stackrel{h}{\longmapsto} x+y
$$

is also many-to-one; for a fixed $$w\in\mathbb{R}^1$$, the inverse image $$h^{-1}(w)$$

is the set of plane vectors whose components add to $$w$$.

The above examples have only to do with the fact that we are considering functions, specifically, many-to-one functions. They show the inverse images as sets of vectors that are related to the image vector $$\vec{w}$$. But these are more than just arbitrary functions, they are homomorphisms; what do the two preservation conditions say about the relationships?

In generalizing from isomorphisms to homomorphisms by dropping the one-to-one condition, we lose the property that we've stated intuitively as: the domain is "the same as" the range. That is, we lose that the domain corresponds perfectly to the range in a one-vector-by-one-vector way.

What we shall keep, as the examples below illustrate, is that a homomorphism describes a way in which the domain is "like", or "analogous to", the range.

**Example 2.7**  —

We think of $$\mathbb{R}^3$$ as being like $$\mathbb{R}^2$$, except that vectors have an extra component. That is, we think of the vector with components $$x$$, $$y$$, and $$z$$ as like the vector with components $$x$$ and $$y$$. In defining the projection map $$\pi$$, we make precise which members of the domain we are thinking of as related to which members of the codomain.

Understanding in what way the preservation conditions in the definition of homomorphism show that the domain elements are like the codomain elements is easiest if we draw $$\mathbb{R}^2$$ as the $$xy$$-plane inside of $$\mathbb{R}^3$$. (Of course, $$\mathbb{R}^2$$ is a set of two-tall vectors while the $$xy$$-plane is a set of three-tall vectors with a third component of zero, but there is an obvious correspondence.) Then, $$\pi(\vec{v})$$ is the "shadow" of $$\vec{v}$$ in the plane and the preservation of addition property says that

- $$\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}$$ above $$\begin{pmatrix} x_1 \\ y_1 \end{pmatrix}$$  plus  $$\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}$$ above $$\begin{pmatrix} x_2 \\ y_2 \end{pmatrix}$$  equals   $$\begin{pmatrix} x_1+y_1 \\ y_1+y_2 \\ z_1+z_2 \end{pmatrix}$$ above $$\begin{pmatrix} x_1+x_2 \\ y_1+y_2 \end{pmatrix}$$

Briefly, the shadow of a sum $$\pi(\vec{v}_1+\vec{v}_2)$$ equals the sum of the shadows $$\pi(\vec{v}_1)+\pi(\vec{v}_2)$$. (Preservation of scalar multiplication has a similar interpretation.)

Redrawing by separating the two spaces, moving the codomain $$\mathbb{R}^2$$ to the right, gives an uglier picture but one that is more faithful to the "bean" sketch.

Again in this drawing, the vectors that map to $$\vec{w}_1$$ lie in the domain in a vertical line (only one such vector is shown, in gray). Call any such member of this inverse image a "$$\vec{w}_1$$ vector". Similarly, there is a vertical line of "$$\vec{w}_2$$ vectors" and a vertical line of "$$\vec{w}_1+\vec{w}_2$$ vectors". Now, $$\pi$$ has the property that if $$\pi(\vec{v}_1)=\vec{w}_1$$ and $$\pi(\vec{v}_2)=\vec{w}_2$$ then $$\pi(\vec{v}_1+\vec{v}_2)=\pi(\vec{v}_1)+\pi(\vec{v}_2) =\vec{w}_1+\vec{w}_2$$. This says that the vector classes add, in the sense that any $$\vec{w}_1$$ vector plus any $$\vec{w}_2$$ vector equals a $$\vec{w}_1+\vec{w}_2$$ vector, (A similar statement holds about the classes under scalar multiplication.)

Thus, although the two spaces $$\mathbb{R}^3$$ and $$\mathbb{R}^2$$ are not isomorphic, $$\pi$$ describes a way in which they are alike: vectors in $$\mathbb{R}^3$$ add as do the associated vectors in $$\mathbb{R}^2$$— vectors add as their shadows add.

**Example 2.8**  —

A homomorphism can be used to express an analogy between spaces that is more subtle than the prior one. For the map

$$
\begin{pmatrix} x \\ y \end{pmatrix} \stackrel{h}{\longmapsto} x+y
$$

from Example 2.6 fix two numbers $$w_1, w_2$$ in the range $$\mathbb{R}$$. A $$\vec{v}_1$$ that maps to $$w_1$$ has components that add to $$w_1$$, that is, the inverse image $$h^{-1}(w_1)$$ is the set of vectors with endpoint on the diagonal line $$x+y=w_1$$. Call these the "$$w_1$$ vectors". Similarly, we have the "$$w_2$$ vectors" and the "$$w_1+w_2$$ vectors". Then the addition preservation property says that

- a "$$w_1$$ vector"  plus  a "$$w_2$$ vector"  equals  a "$$w_1+w_2$$ vector".

Restated, if a $$w_1$$ vector is added to a $$w_2$$ vector then the result is mapped by $$h$$ to a $$w_1+w_2$$ vector. Briefly, the image of a sum is the sum of the images. Even more briefly, $$h(\vec{v}_1+\vec{v}_2)=h(\vec{v}_1)+h(\vec{v}_2)$$. (The preservation of scalar multiplication condition has a similar restatement.)

**Example 2.9**  —

The inverse images can be structures other than lines. For the linear map $$h:\mathbb{R}^3\to \mathbb{R}^2$$

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} \mapsto \begin{pmatrix} x \\ x \end{pmatrix}
$$

the inverse image sets are planes $$x=0$$, $$x=1$$, etc., perpendicular to the $$x$$-axis.

We won't describe how every homomorphism that we will use is an analogy because the formal sense that we make of "alike in that ..." is "a homomorphism exists such that ...". Nonetheless, the idea that a homomorphism between two spaces expresses how the domain's vectors fall into classes that act like the range's vectors is a good way to view homomorphisms.

Another reason that we won't treat all of the homomorphisms that we see as above is that many vector spaces are hard to draw (e.g., a space of polynomials). However, there is nothing bad about gaining insights from those spaces that we are able to draw, especially when those insights extend to all vector spaces. We derive two such insights from the three examples 2.7 , 2.8, and 2.9.

First, in all three examples, the inverse images are lines or planes, that is, linear surfaces. In particular, the inverse image of the range's zero vector is a line or plane through the origin— a subspace of the domain.

**Lemma 2.10**  —

For any homomorphism, the inverse image of a subspace of the range is a subspace of the domain. In particular, the inverse image of the trivial subspace of the range is a subspace of the domain.

**Proof**  —

Let $$h:V\to W$$ be a homomorphism and let $$S$$ be a subspace of the rangespace $$h$$. Consider $$h^{-1}(S)=\{\vec{v}\in V\,\big|\, h(\vec{v})\in S\}$$, the inverse image of the set $$S$$. It is nonempty because it contains $$\vec{0}_V$$, since $$h(\vec{0}_V)=\vec{0}_W$$, which is an element $$S$$, as $$S$$ is a subspace. To show that $$h^{-1}(S)$$ is closed under linear combinations, let $$\vec{v}_1$$ and $$\vec{v}_2$$ be elements, so that $$h(\vec{v}_1)$$ and $$h(\vec{v}_2)$$ are elements of $$S$$, and then $$c_1\vec{v}_1+c_2\vec{v}_2$$ is also in the inverse image because $$h(c_1\vec{v}_1+c_2\vec{v}_2) =c_1h(\vec{v}_1)+c_2h(\vec{v}_2)$$ is a member of the subspace $$S$$.

**Definition 2.11**  —

The **nullspace** or **kernel** of a linear map $$h:V\to W$$ is the inverse image of $$0_W$$

$$
\mathcal{N}(h)=h^{-1}(\vec{0}_W)=\{\vec{v}\in V\,\big|\, h(\vec{v})=\vec{0}_W\}.
$$

The dimension of the nullspace is the map's *nullity*.

**Example 2.12**  —

The map from Example 2.3 has this nullspace $$\mathcal{N}(d/dx)=\{a_0+0x+0x^2+0x^3\,\big|\, a_0\in\mathbb{R}\}$$.

**Example 2.13**  —

The map from Example 2.4 has this nullspace.

$$
\mathcal{N}(h)=\{\begin{pmatrix} a &b \\ 0 &-(a+b)/2 \end{pmatrix}\,\big|\, a,b\in\mathbb{R}\}
$$

Now for the second insight from the above pictures. In Example 2.7, each of the vertical lines is squashed down to a single point— $$\pi$$, in passing from the domain to the range, takes all of these one-dimensional vertical lines and "zeroes them out", leaving the range one dimension smaller than the domain. Similarly, in Example 2.8, the two-dimensional domain is mapped to a one-dimensional range by breaking the domain into lines (here, they are diagonal lines), and compressing each of those lines to a single member of the range. Finally, in Example 2.9, the domain breaks into planes which get "zeroed out", and so the map starts with a three-dimensional domain but ends with a one-dimensional range— this map "subtracts" two from the dimension. (Notice that, in this third example, the codomain is two-dimensional but the range of the map is only one-dimensional, and it is the dimension of the range that is of interest.)

**Theorem 2.14**  —

A linear map's rank plus its nullity equals the dimension of its domain.

**Proof**  —

Let $$h:V\to W$$ be linear and let $$B_N=\langle \vec{\beta}_1,\ldots,\vec{\beta}_k \rangle$$ be a basis for the nullspace. Extend that to a basis $$B_V=\langle \vec{\beta}_1,\dots,\vec{\beta}_k, \vec{\beta}_{k+1},\dots,\vec{\beta}_n \rangle$$ for the entire domain. We shall show that $$B_R=\langle h(\vec{\beta}_{k+1}),\dots,h(\vec{\beta}_n) \rangle$$ is a basis for the rangespace. Then counting the size of these bases gives the result.

To see that $$B_R$$ is linearly independent, consider the equation $$c_{k+1}h(\vec{\beta}_{k+1})+\dots+c_nh(\vec{\beta}_n)=\vec{0}_W$$. This gives that $$h(c_{k+1}\vec{\beta}_{k+1}+\dots+c_n\vec{\beta}_n)=\vec{0}_W$$ and so $$c_{k+1}\vec{\beta}_{k+1}+\dots+c_n\vec{\beta}_n$$ is in the nullspace of $$h$$. As $$B_N$$ is a basis for this nullspace, there are scalars $$c_1,\dots,c_k\in\mathbb{R}$$ satisfying this relationship.

$$
c_1\vec{\beta}_1+\dots+c_k\vec{\beta}_k = c_{k+1}\vec{\beta}_{k+1}+\dots+c_n\vec{\beta}_n
$$

But $$B_V$$ is a basis for $$V$$ so each scalar equals zero. Therefore $$B_R$$ is linearly independent.

To show that $$B_R$$ spans the rangespace, consider $$h(\vec{v})\in \mathcal{R}(h)$$ and write $$\vec{v}$$ as a linear combination $$\vec{v}=c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n$$ of members of $$B_V$$. This gives $$h(\vec{v})=h(c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n) =c_1h(\vec{\beta}_1)+\dots+c_kh(\vec{\beta}_k) +c_{k+1}h(\vec{\beta}_{k+1})+\dots+c_nh(\vec{\beta}_n)$$ and since $$\vec{\beta}_1$$, ..., $$\vec{\beta}_k$$ are in the nullspace, we have that $$h(\vec{v})=\vec{0}+\dots+\vec{0} +c_{k+1}h(\vec{\beta}_{k+1})+\dots+c_nh(\vec{\beta}_n)$$. Thus, $$h(\vec{v})$$ is a linear combination of members of $$B_R$$, and so $$B_R$$ spans the space.

**Example 2.15**  —

Where $$h:\mathbb{R}^3\to \mathbb{R}^4$$ is

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} \stackrel{h}{\longmapsto} \begin{pmatrix} x \\ 0 \\ y \\ 0 \end{pmatrix}
$$

the rangespace and nullspace are

$$
\mathcal{R}(h)= \{\begin{pmatrix} a \\ 0 \\ b \\ 0 \end{pmatrix}\,\big|\, a,b\in\mathbb{R} \} \quad\text{and}\quad \mathcal{N}(h)= \{\begin{pmatrix} 0 \\ 0 \\ z \end{pmatrix}\,\big|\, z\in\mathbb{R} \}
$$

and so the rank of $$h$$ is two while the nullity is one.

**Example 2.16**  —

If $$t:\mathbb{R}\to \mathbb{R}$$ is the linear transformation $$x\mapsto -4x,$$ then the range is $$\mathcal{R}(t)=\mathbb{R}^1$$, and so the rank of $$t$$ is one and the nullity is zero.

**Corollary 2.17**  —

The rank of a linear map is less than or equal to the dimension of the domain. Equality holds if and only if the nullity of the map is zero.

We know that an isomorphism exists between two spaces if and only if their dimensions are equal. Here we see that for a homomorphism to exist, the dimension of the range must be less than or equal to the dimension of the domain. For instance, there is no homomorphism from $$\mathbb{R}^2$$ onto $$\mathbb{R}^3$$. There are many homomorphisms from $$\mathbb{R}^2$$ into $$\mathbb{R}^3$$, but none is onto all of three-space.

The rangespace of a linear map can be of dimension strictly less than the dimension of the domain (Example 2.3's derivative transformation on $$\mathcal{P}_3$$ has a domain of dimension four but a range of dimension three). Thus, under a homomorphism, linearly independent sets in the domain may map to linearly dependent sets in the range (for instance, the derivative sends $$\{1,x,x^2,x^3\}$$ to $$\{0,1,2x,3x^2\}$$). That is, under a homomorphism, independence may be lost. In contrast, dependence stays.

**Lemma 2.18**  —

Under a linear map, the image of a linearly dependent set is linearly dependent.

**Proof**  —

Suppose that $$c_1\vec{v}_1+\dots+c_n\vec{v}_n=\vec{0}_V$$, with some $$c_i$$ nonzero. Then, because $$h(c_1\vec{v}_1+\dots+c_n\vec{v}_n)=c_1h(\vec{v}_1)+\dots+c_nh(\vec{v}_n)$$ and because $$h(\vec{0}_V)=\vec{0}_W$$, we have that $$c_1h(\vec{v}_1)+\dots+c_nh(\vec{v}_n)=\vec{0}_W$$ with some nonzero $$c_i$$.

When is independence not lost? One obvious sufficient condition is when the homomorphism is an isomorphism. This condition is also necessary; see Problem 14. We will finish this subsection comparing homomorphisms with isomorphisms by observing that a one-to-one homomorphism is an isomorphism from its domain onto its range.

**Definition 2.19**  —

A linear map that is one-to-one is *nonsingular*.

(In the next section we will see the connection between this use of "nonsingular" for maps and its familiar use for matrices.)

**Example 2.20**  —

This nonsingular homomorphism $$\iota:\mathbb{R}^2\to \mathbb{R}^3$$

$$
\begin{pmatrix} x \\ y \end{pmatrix} \stackrel{\iota}{\longmapsto} \begin{pmatrix} x \\ y \\ 0 \end{pmatrix}
$$

gives the obvious correspondence between $$\mathbb{R}^2$$ and the $$xy$$-plane inside of $$\mathbb{R}^3$$.

The prior observation allows us to adapt some results about isomorphisms to this setting.

**Theorem 2.21**  —

In an $$n$$-dimensional vector space $$V$$, these:

1. $$h$$ is nonsingular, that is, one-to-one
2. $$h$$ has a linear inverse
3. $$\mathcal{N}(h)=\{\vec{0}\,\}$$, that is, $$\text{nullity}\,(h)=0$$
4. $$\mathop{\text{rank}} (h)=n$$
5. if $$\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ is a basis for $$V$$ then $$\langle h(\vec{\beta}_1),\dots,h(\vec{\beta}_n) \rangle$$is a basis for $$\mathcal{R}(h)$$

are equivalent statements about a linear map $$h:V\to W$$.

**Proof**  —

We will first show that $$1 \Longleftrightarrow 2$$. We will then show that $$1\implies 3\implies 4\implies 5 \implies 2$$.

For $$1 \Longrightarrow 2$$, suppose that the linear map $$h$$ is one-to-one, and so has an inverse. The domain of that inverse is the range of $$h$$ and so a linear combination of two members of that domain has the form $$c_1h(\vec{v}_1)+c_2h(\vec{v}_2)$$. On that combination, the inverse $$h^{-1}$$ gives this.

$$
\begin{array}{rl} h^{-1}(c_1h(\vec{v}_1)+c_2h(\vec{v}_2)) &=h^{-1}(h(c_1\vec{v}_1+c_2\vec{v}_2)) \\ &=h^{-1}\circ h\,(c_1\vec{v}_1+c_2\vec{v}_2) \\ &=c_1\vec{v}_1+c_2\vec{v}_2 \\ &=c_1h^{-1}\circ h\,(\vec{v}_1) +c_2h^{-1}\circ h\,(\vec{v}_2) \\ &=c_1\cdot h^{-1}(h(\vec{v}_1))+c_2\cdot h^{-1}(h(\vec{v}_2)) \end{array}
$$

Thus the inverse of a one-to-one linear map is automatically linear. But this also gives the $$1 \Longrightarrow 2$$ implication, because the inverse itself must be one-to-one.

Of the remaining implications, $$1\implies 3$$ holds because any homomorphism maps $$\vec{0}_V$$ to $$\vec{0}_W$$, but a one-to-one map sends at most one member of $$V$$ to $$\vec{0}_W$$.

Next, $$3 \implies 4$$ is true since rank plus nullity equals the dimension of the domain.

For $$4\implies 5$$, to show that $$\langle h(\vec{\beta}_1),\dots,h(\vec{\beta}_n) \rangle$$ is a basis for the rangespace we need only show that it is a spanning set, because by assumption the range has dimension $$n$$. Consider $$h(\vec{v})\in\mathcal{R}(h)$$. Expressing $$\vec{v}$$ as a linear combination of basis elements produces $$h(\vec{v})=h(c_1\vec{\beta}_1+c_2\vec{\beta}_2+\cdots +c_n\vec{\beta}_n)$$, which gives that $$h(\vec{v})=c_1h(\vec{\beta}_1)+\dots+c_nh(\vec{\beta}_n)$$, as desired.

Finally, for the $$5\implies 2$$ implication, assume that $$\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ is a basis for $$V$$ so that $$\langle h(\vec{\beta}_1),\dots,h(\vec{\beta}_n) \rangle$$ is a basis for $$\mathcal{R}(h)$$. Then every $$\vec{w}\in\mathcal{R}(h)$$ a the unique representation $$\vec{w}=c_1h(\vec{\beta}_1)+\dots+c_nh(\vec{\beta}_n)$$. Define a map from $$\mathcal{R}(h)$$ to $$V$$ by

$$
\vec{w} \;\mapsto\; c_1\vec{\beta}_1+c_2\vec{\beta}_2+\cdots +c_n\vec{\beta}_n
$$

(uniqueness of the representation makes this well-defined). Checking that it is linear and that it is the inverse of $$h$$ are easy.

We've now seen that a linear map shows how the structure of the domain is like that of the range. Such a map can be thought to organize the domain space into inverse images of points in the range. In the special case that the map is one-to-one, each inverse image is a single point and the map is an isomorphism between the domain and the range.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Let $$h:\mathcal{P}_3\to \mathcal{P}_4$$ be given by $$p(x)\mapsto x\cdot p(x)$$. Which of these are in the nullspace? Which are in the rangespace?

1. $$x^3$$
2. $$0$$
3. $$7$$
4. $$12x-0.5x^3$$
5. $$1+3x^2-x^3$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Find the nullspace, nullity, rangespace, and rank of each map.

1. $$h:\mathbb{R}^2\to \mathcal{P}_3$$ given by

$$
\begin{pmatrix} a \\ b \end{pmatrix}\mapsto a+ax+ax^2
$$

2. $$h:\mathcal{M}_{2 \! \times \! 2}\to \mathbb{R}$$ given by

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \mapsto a+d
$$

3. $$h:\mathcal{M}_{2 \! \times \! 2}\to \mathcal{P}_2$$ given by

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \mapsto a+b+c+dx^2
$$

4. the zero map $$Z:\mathbb{R}^3\to \mathbb{R}^4$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

Find the nullity of each map.

1. $$h:\mathbb{R}^5\to \mathbb{R}^8$$ of rank five
2. $$h:\mathcal{P}_3\to \mathcal{P}_3$$ of rank one
3. $$h:\mathbb{R}^6\to \mathbb{R}^3$$, an onto map
4. $$h:\mathcal{M}_{3 \! \times \! 3}\to \mathcal{M}_{3 \! \times \! 3}$$, onto  
*This exercise is recommended for all readers.*

**Problem 4**  —

What is the nullspace of the differentiation transformation $$d/dx:\mathcal{P}_n\to \mathcal{P}_n$$? What is the nullspace of the second derivative, as a transformation of $$\mathcal{P}_n$$? The $$k$$-th derivative?

**Problem 5**  —

Example 2.7 restates the first condition in the definition of homomorphism as "the shadow of a sum is the sum of the shadows". Restate the second condition in the same style.

**Problem 6**  —

For the homomorphism $$h:\mathcal{P}_3\to \mathcal{P}_3$$ given by $$h(a_0+a_1x+a_2x^2+a_3x^3)=a_0+(a_0+a_1)x+(a_2+a_3)x^3$$ find these.

1. $$\mathcal{N}(h)$$
2. $$h^{-1}(2-x^3)$$
3. $$h^{-1}(1+x^2)$$  
*This exercise is recommended for all readers.*

**Problem 7**  —

For the map $$f:\mathbb{R}^2\to \mathbb{R}$$ given by

$$
f(\begin{pmatrix} x \\ y \end{pmatrix})=2x+y
$$

sketch these inverse image sets: $$f^{-1}(-3)$$, $$f^{-1}(0)$$, and $$f^{-1}(1)$$.  
*This exercise is recommended for all readers.*

**Problem 8**  —

Each of these transformations of $$\mathcal{P}_3$$ is nonsingular. Find the inverse function of each.

1. $$a_0+a_1x+a_2x^2+a_3x^3\mapsto a_0+a_1x+2a_2x^2+3a_3x^3$$
2. $$a_0+a_1x+a_2x^2+a_3x^3\mapsto a_0+a_2x+a_1x^2+a_3x^3$$
3. $$a_0+a_1x+a_2x^2+a_3x^3\mapsto a_1+a_2x+a_3x^2+a_0x^3$$
4. $$a_0+a_1x+a_2x^2+a_3x^3\mapsto a_0+(a_0+a_1)x+(a_0+a_1+a_2)x^2+(a_0+a_1+a_2+a_3)x^3$$

**Problem 9**  —

Describe the nullspace and rangespace of a transformation given by $$\vec{v}\mapsto 2\vec{v}$$.

**Problem 10**  —

List all pairs $$(\text{rank}(h),\text{nullity}(h))$$ that are possible for linear maps from $$\mathbb{R}^5$$ to $$\mathbb{R}^3$$.

**Problem 11**  —

Does the differentiation map $$d/dx:\mathcal{P}_n\to \mathcal{P}_n$$ have an inverse?  
*This exercise is recommended for all readers.*

**Problem 12**  —

Find the nullity of the map $$h:\mathcal{P}_n\to \mathbb{R}$$ given by

$$
a_0+a_1x+\dots+a_nx^n\mapsto\int_{x=0}^{x=1}a_0+a_1x+\dots+a_nx^n\,dx.
$$

**Problem 13**  —

1. Prove that a homomorphism is onto if and only if its rank equals the dimension of its codomain.
2. Conclude that a homomorphism between vector spaces with the same dimension is one-to-one if and only if it is onto.

**Problem 14**  —

Show that a linear map is nonsingular if and only if it preserves linear independence.

**Problem 15**  —

Corollary 2.17 says that for there to be an onto homomorphism from a vector space $$V$$ to a vector space $$W$$, it is necessary that the dimension of $$W$$ be less than or equal to the dimension of $$V$$. Prove that this condition is also sufficient; use Theorem 1.9 to show that if the dimension of $$W$$ is less than or equal to the dimension of $$V$$, then there is a homomorphism from $$V$$ to $$W$$ that is onto.

**Problem 16**  —

Let $$h:V\to \mathbb{R}$$ be a homomorphism, but not the zero homomorphism. Prove that if $$\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ is a basis for the nullspace and if $$\vec{v}\in V$$ is not in the nullspace then $$\langle \vec{v},\vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ is a basis for the entire domain $$V$$.  
*This exercise is recommended for all readers.*

**Problem 17**  —

Recall that the nullspace is a subset of the domain and the rangespace is a subset of the codomain. Are they necessarily distinct? Is there a homomorphism that has a nontrivial intersection of its nullspace and its rangespace?

**Problem 18**  —

Prove that the image of a span equals the span of the images. That is, where $$h:V\to W$$ is linear, prove that if $$S$$ is a subset of $$V$$ then $$h([S])$$ equals $$[h(S)]$$. This generalizes Lemma 2.1 since it shows that if $$U$$ is any subspace of $$V$$ then its image $$\{h(\vec{u})\,\big|\, \vec{u}\in U\}$$ is a subspace of $$W$$, because the span of the set $$U$$ is $$U$$.  
*This exercise is recommended for all readers.*

**Problem 19**  —

1. Prove that for any linear map $$h:V\to W$$ and any $$\vec{w}\in W$$, the set $$h^{-1}(\vec{w})$$ has the form

$$
\{\vec{v}+\vec{n}\,\big|\, \vec{n}\in\mathcal{N}(h) \}
$$

for $$\vec{v}\in V$$ with $$h(\vec{v})=\vec{w}$$ (if $$h$$ is not onto then this set may be empty). Such a set is a **coset** of $$\mathcal{N}(h)$$ and is denoted $$\vec{v}+\mathcal{N}(h)$$.
2. Consider the map $$t:\mathbb{R}^2\to \mathbb{R}^2$$ given by

$$
\begin{pmatrix} x \\ y \end{pmatrix} \stackrel{t}{\longmapsto} \begin{pmatrix} ax+by \\ cx+dy \end{pmatrix}
$$

for some scalars $$a$$, $$b$$, $$c$$, and $$d$$. Prove that $$t$$ is linear.
3. Conclude from the prior two items that for any linear system of the form

$$
\begin{array}{rcrcr} ax &+ &by &= &e \\ cx &+ &dy &= &f \end{array}
$$

the solution set can be written (the vectors are members of $$\mathbb{R}^2$$)

$$
\{\vec{p}+\vec{h}\,\big|\, \vec{h}\text{ satisfies the associated homogeneous system} \}
$$

where $$\vec{p}$$ is a particular solution of that linear system (if there is no particular solution then the above set is empty).
4. Show that this map $$h:\mathbb{R}^n\to \mathbb{R}^m$$ is linear

$$
\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} \mapsto \begin{pmatrix} a_{1,1}x_1+\dots+a_{1,n}x_n \\ \vdots \\ a_{m,1}x_1+\dots+a_{m,n}x_n \end{pmatrix}
$$

for any scalars $$a_{1,1}$$, ..., $$a_{m,n}$$. Extend the conclusion made in the prior item.
5. Show that the $$k$$-th derivative map is a linear transformation of $$\mathcal{P}_n$$ for each $$k$$. Prove that this map is a linear transformation of that space

$$
f\mapsto \frac{d^k}{dx^k}f+c_{k-1}\frac{d^{k-1}}{dx^{k-1}}f +\dots+ c_1\frac{d}{dx}f+c_0f
$$

for any scalars $$c_k$$, ..., $$c_0$$. Draw a conclusion as above.

**Problem 20**  —

Prove that for any transformation $$t:V\to V$$ that is rank one, the map given by composing the operator with itself $$t\circ t:V\to V$$ satisfies $$t\circ t=r\cdot t$$ for some real number $$r$$.

**Problem 21**  —

Show that for any space $$V$$ of dimension $$n$$, the **dual space**

$$
\mathop{\mathcal L}(V,\mathbb{R})=\{h:V\to \mathbb{R}\,\big|\, h\text{ is linear}\}
$$

is isomorphic to $$\mathbb{R}^n$$. It is often denoted $$V^\ast$$. Conclude that $$V^\ast\cong V$$.

**Problem 22**  —

Show that any linear map is the sum of maps of rank one.

**Problem 23**  —

Is "is homomorphic to" an equivalence relation? (*Hint:* the difficulty is to decide on an appropriate meaning for the quoted phrase.)

**Problem 24**  —

Show that the rangespaces and nullspaces of powers of linear maps $$t:V\to V$$ form descending

$$
V\supseteq \mathcal{R}(t)\supseteq\mathcal{R}(t^2)\supseteq\ldots
$$

and ascending

$$
\{\vec{0}\}\subseteq\mathcal{N}(t)\subseteq\mathcal{N}(t^2)\subseteq\ldots
$$

chains. Also show that if $$k$$ is such that $$\mathcal{R}(t^k)=\mathcal{R}(t^{k+1})$$ then all following rangespaces are equal: $$\mathcal{R}(t^k)=\mathcal{R}(t^{k+1})=\mathcal{R}(t^{k+2})\ldots\,$$. Similarly, if $$\mathcal{N}(t^k)=\mathcal{N}(t^{k+1})$$ then $$\mathcal{N}(t^k)=\mathcal{N}(t^{k+1})=\mathcal{N}(t^{k+2})=\ldots\,$$.

Solutions

### Footnotes

---

*Source: Wikibooks, Linear Algebra/Rangespace and Nullspace (https://en.wikibooks.org/wiki/Linear_Algebra/Rangespace_and_Nullspace), by Wikibooks contributors, CC BY-SA 4.0.*
