# Topic: Geometry of Linear Maps

The pictures below contrast $$f_1(x)=e^x$$ and $$f_2(x)=x^2$$, which are nonlinear, with $$h_1(x)=2x$$ and $$h_2(x)=-x$$, which are linear. Each of the four pictures shows the domain $$\mathbb{R}^1$$ on the left mapped to the codomain $$\mathbb{R}^1$$ on the right. Arrows trace out where each map sends $$x=0$$, $$x=1$$, $$x=2$$, $$x=-1$$, and $$x=-2$$. Note how the nonlinear maps distort the domain in transforming it into the range. For instance, $$f_1(1)$$ is further from $$f_1(2)$$ than it is from $$f_1(0)$$ — the map is spreading the domain out unevenly so that an interval near $$x=2$$ is spread apart more than is an interval near $$x=0$$ when they are carried over to the range.

The linear maps are nicer, more regular, in that for each map all of the domain is spread by the same factor.

The only linear maps from $$\mathbb{R}^1$$ to $$\mathbb{R}^1$$ are multiplications by a scalar. In higher dimensions more can happen. For instance, this linear transformation of $$\mathbb{R}^2$$, rotates vectors counterclockwise, and is not just a scalar multiplication.

The transformation of $$\mathbb{R}^3$$ which projects vectors into the $$xz$$-plane is also not just a rescaling.

Nonetheless, even in higher dimensions the situation isn't too complicated.

Below, we use the standard bases to represent each linear map $$h:\mathbb{R}^n\to \mathbb{R}^m$$ by a matrix $$H$$. Recall that any $$H$$ can be factored $$H=PBQ$$, where $$P$$ and $$Q$$ are nonsingular and $$B$$ is a partial-identity matrix. Further, recall that nonsingular matrices factor into elementary matrices $$PBQ=T_nT_{n-1}\cdots T_jBT_{j-1}\cdots T_1$$, which are matrices that are obtained from the identity $$I$$ with one Gaussian step

$$
I\xrightarrow[]{k\rho_i}M_i(k) \qquad I\xrightarrow[]{\rho_i\leftrightarrow\rho_j}P_{i,j} \qquad I\xrightarrow[]{k\rho_i+\rho_j}C_{i,j}(k)
$$

($$i\neq j$$, $$k\neq 0$$). So if we understand the effect of a linear map described by a partial-identity matrix, and the effect of linear mapss described by the elementary matrices, then we will in some sense understand the effect of any linear map. (The pictures below stick to transformations of $$\mathbb{R}^2$$ for ease of drawing, but the statements hold for maps from any $$\mathbb{R}^n$$ to any $$\mathbb{R}^m$$.)

The geometric effect of the linear transformation represented by a partial-identity matrix is projection.

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} \quad\xrightarrow{\begin{pmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &0 \end{pmatrix}_{\mathcal{E}_3,\mathcal{E}_3}}\quad \begin{pmatrix} x \\ y \\ 0 \end{pmatrix}
$$

For the $$M_i(k)$$ matrices, the geometric action of a transformation represented by such a matrix (with respect to the standard basis) is to stretch vectors by a factor of $$k$$ along the $$i$$-th axis. This map stretches by a factor of $$3$$ along the $$x$$-axis.

Note that if $$0\leq k<1$$ or if $$k<0$$ then the $$i$$-th component goes the other way; here, toward the left.

Either of these is a **dilation**.

The action of a transformation represented by a $$P_{i,j}$$ permutation matrix is to interchange the $$i$$-th and $$j$$-th axes; this is a particular kind of reflection.

In higher dimensions, permutations involving many axes can be decomposed into a combination of swaps of pairs of axes— see Problem 5.

The remaining case is that of matrices of the form $$C_{i,j}(k)$$. Recall that, for instance, that $$C_{1,2}(2)$$ performs $$2\rho_1+\rho_2$$.

$$
\begin{pmatrix} x \\ y \end{pmatrix} \xrightarrow{\begin{pmatrix} 1 &0 \\ 2 &1 \end{pmatrix}_{\mathcal{E}_2,\mathcal{E}_2}} \qquad \begin{pmatrix} x \\ 2x+y \end{pmatrix}
$$

In the picture below, the vector $$\vec{u}$$ with the first component of $$1$$ is affected less than the vector $$\vec{v}$$ with the first component of $$2$$— $$h(\vec{u})$$ is only $$2$$ higher than $$\vec{u}$$ while $$h(\vec{v})$$ is $$4$$ higher than $$\vec{v}$$.

Any vector with a first component of $$1$$ would be affected as is $$\vec{u}$$; it would be slid up by $$2$$. And any vector with a first component of $$2$$ would be slid up $$4$$, as was $$\vec{v}$$. That is, the transformation represented by $$C_{i,j}(k)$$ affects vectors depending on their $$i$$-th component.

Another way to see this same point is to consider the action of this map on the unit square. In the next picture, vectors with a first component of $$0$$, like the origin, are not pushed vertically at all but vectors with a positive first component are slid up. Here, all vectors with a first component of $$1$$— the entire right side of the square— is affected to the same extent. More generally, vectors on the same vertical line are slid up the same amount, namely, they are slid up by twice their first component. The resulting shape, a rhombus, has the same base and height as the square (and thus the same area) but the right angles are gone.

For contrast the next picture shows the effect of the map represented by $$C_{2,1}(1)$$. In this case, vectors are affected according to their second component. The vector $$\binom{x}{y}$$ is slid horozontally by twice $$y$$.

Because of this action, this kind of map is called a **shear**.

With that, we have covered the geometric effect of the four types of components in the expansion $$H=T_nT_{n-1}\cdots T_jBT_{j-1}\cdots T_1$$, the partial-identity projection $$B$$ and the elementary $$T_i$$'s. Since we understand its components, we in some sense understand the action of any $$H$$. As an illustration of this assertion, recall that under a linear map, the image of a subspace is a subspace and thus the linear transformation $$h$$ represented by $$H$$ maps lines through the origin to lines through the origin. (The dimension of the image space cannot be greater than the dimension of the domain space, so a line can't map onto, say, a plane.) We will extend that to show that any line, not just those through the origin, is mapped by $$h$$ to a line. The proof is simply that the partial-identity projection $$B$$ and the elementary $$T_i$$'s each turn a line input into a line output (verifying the four cases is Problem 6), and therefore their composition also preserves lines. Thus, by understanding its components we can understand arbitrary square matrices $$H$$, in the sense that we can prove things about them.

An understanding of the geometric effect of linear transformations on $$\mathbb{R}^n$$ is very important in mathematics. Here is a familiar application from calculus. On the left is a picture of the action of the nonlinear function $$y(x)=x^2+x$$. As at that start of this Topic, overall the geometric effect of this map is irregular in that at different domain points it has different effects (e.g., as the domain point $$x$$ goes from $$2$$ to $$-2$$, the associated range point $$f(x)$$ at first decreases, then pauses instantaneously, and then increases).

But in calculus we don't focus on the map overall, we focus instead on the local effect of the map.

At $$x=1$$ the derivative is $$y^\prime(1)=3$$, so that near $$x=1$$ we have $$\Delta y\approx 3\cdot\Delta x$$.

That is, in a neighborhood of $$x=1$$, in carrying the domain to the codomain this map causes it to grow by a factor of $$3$$ — it is, locally, approximately, a dilation.

The picture below shows a small interval in the domain $$(x-\Delta x\,..\,x+\Delta x)$$ carried over to an interval in the codomain $$(y-\Delta y\,..\,y+\Delta y)$$ that is three times as wide: $$\Delta y \approx 3\cdot \Delta x$$.

(When the above picture is drawn in the traditional cartesian way then the prior sentence about the rate of growth of $$y(x)$$ is usually stated: the derivative $$y^\prime(1)=3$$ gives the slope of the line tangent to the graph at the point $$(1,2)$$.)

In higher dimensions, the idea is the same but the approximation is not just the $$\mathbb{R}^1$$-to-$$\mathbb{R}^1$$ scalar multiplication case. Instead, for a function $$y:\mathbb{R}^n\to \mathbb{R}^m$$ and a point $$\vec{x}\in\mathbb{R}^n$$, the derivative is defined to be the linear map $$h:\mathbb{R}^n\to \mathbb{R}^m$$ best approximating how $$y$$ changes near $$y(\vec{x})$$. So the geometry studied above applies.

We will close this Topic by remarking how this point of view makes clear an often-misunderstood, but very important, result about derivatives: the derivative of the composition of two functions is computed by using the Chain Rule for combining their derivatives. Recall that (with suitable conditions on the two functions)

$$
\frac{d\,(g\circ f)}{dx}(x) = \frac{dg}{dx}(f(x))\cdot\frac{df}{dx}(x)
$$

so that, for instance, the derivative of $$\sin(x^2+3x)$$ is $$\cos(x^2+3x)\cdot(2x+3)$$. How does this combination arise? From this picture of the action of the composition.

The first map $$f$$ dilates the neighborhood of $$x$$ by a factor of

$$
\frac{df}{dx}(x)
$$

and the second map $$g$$ dilates some more, this time dilating a neighborhood of $$f(x)$$ by a factor of

$$
\frac{dg}{dx}(\,f(x)\,)
$$

and as a result, the composition dilates by the product of these two.

In higher dimensions the map expressing how a function changes near a point is a linear map, and is expressed as a matrix. (So we understand the basic geometry of higher-dimensional derivatives; they are compositions of dilations, interchanges of axes, shears, and a projection). And, the Chain Rule just multiplies the matrices.

Thus, the geometry of linear maps $$h:\mathbb{R}^n\to \mathbb{R}^m$$ is appealing both for its simplicity and for its usefulness.

### Exercises

**Problem 1**  —

Let $$h:\mathbb{R}^2\to \mathbb{R}^2$$ be the transformation that rotates vectors clockwise by $$\pi/4$$ radians.

1. Find the matrix $$H$$ representing $$h$$ with respect to the standard bases. Use Gauss' method to reduce $$H$$ to the identity.
2. Translate the row reduction to to a matrix equation $$T_jT_{j-1}\cdots T_1H=I$$ (the prior item shows both that $$H$$ is similar to $$I$$, and that no column operations are needed to derive $$I$$ from $$H$$).
3. Solve this matrix equation for $$H$$.
4. Sketch the geometric effect matrix, that is, sketch how $$H$$ is expressed as a combination of dilations, flips, skews, and projections (the identity is a trivial projection).

**Problem 2**  —

What combination of dilations, flips, skews, and projections produces a rotation counterclockwise by $$2\pi/3$$ radians?

**Problem 3**  —

What combination of dilations, flips, skews, and projections produces the map $$h:\mathbb{R}^3\to \mathbb{R}^3$$ represented with respect to the standard bases by this matrix?

$$
\begin{pmatrix} 1 &2 &1 \\ 3 &6 &0 \\ 1 &2 &2 \end{pmatrix}
$$

**Problem 4**  —

Show that any linear transformation of $$\mathbb{R}^1$$ is the map that multiplies by a scalar $$x\mapsto kx$$.

**Problem 5**  —

Show that for any permutation (that is, reordering) $$p$$ of the numbers $$1$$, ..., $$n$$, the map

$$
\begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} \mapsto \begin{pmatrix} x_{p(1)} \\ x_{p(2)} \\ \vdots \\ x_{p(n)} \end{pmatrix}
$$

can be accomplished with a composition of maps, each of which only swaps a single pair of coordinates. *Hint:* it can be done by induction on $$n$$. (*Remark:* in the fourth chapter we will show this and we will also show that the parity of the number of swaps used is determined by $$p$$. That is, although a particular permutation could be accomplished in two different ways with two different numbers of swaps, either both ways use an even number of swaps, or both use an odd number.)

**Problem 6**  —

Show that linear maps preserve the linear structures of a space.

1. Show that for any linear map from $$\mathbb{R}^n$$ to $$\mathbb{R}^m$$, the image of any line is a line. The image may be a degenerate line, that is, a single point.
2. Show that the image of any linear surface is a linear surface. This generalizes the result that under a linear map the image of a subspace is a subspace.
3. Linear maps preserve other linear ideas. Show that linear maps preserve "betweeness": if the point $$B$$ is between $$A$$ and $$C$$ then the image of $$B$$ is between the image of $$A$$ and the image of $$C$$.

**Problem 7**  —

Use a picture like the one that appears in the discussion of the Chain Rule to answer: if a function $$f:\mathbb{R}\to \mathbb{R}$$ has an inverse, what's the relationship between how the function — locally, approximately — dilates space, and how its inverse dilates space (assuming, of course, that it has an inverse)?

Solutions

---

*Source: Wikibooks, Linear Algebra/Topic: Geometry of Linear Maps (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Geometry_of_Linear_Maps), by Wikibooks contributors, CC BY-SA 4.0.*
