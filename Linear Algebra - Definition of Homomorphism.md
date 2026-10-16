# Definition of Homomorphism

**Definition 1.1**  —

A function between vector spaces $$h:V\to W$$ that preserves the operations of addition

if $$\vec{v}_1,\vec{v}_2\in V$$ then $$h(\vec{v}_1+\vec{v}_2)=h(\vec{v}_1)+h(\vec{v}_2)$$

and scalar multiplication

if $$\vec{v}\in V$$ and $$r\in\mathbb{R}$$ then $$h(r\cdot\vec{v})=r\cdot h(\vec{v})$$

is a **homomorphism** or **linear map**.

**Example 1.2**  —

The projection map $$\pi:\mathbb{R}^3\to \mathbb{R}^2$$

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} \stackrel{\pi}{\longmapsto} \begin{pmatrix} x \\ y \end{pmatrix}
$$

is a homomorphism.

It preserves addition

$$
\pi(\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}\!+\!\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}) = \pi(\begin{pmatrix} x_1+x_2 \\ y_1+y_2 \\ z_1+z_2 \end{pmatrix}) = \begin{pmatrix} x_1+x_2 \\ y_1+y_2 \end{pmatrix} = \pi(\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}) + \pi(\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix})
$$

and scalar multiplication.

$$
\pi(r\cdot\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}) = \pi(\begin{pmatrix} rx_1 \\ ry_1 \\ rz_1 \end{pmatrix}) = \begin{pmatrix} rx_1 \\ ry_1 \end{pmatrix} = r\cdot\pi(\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix})
$$

This map is not an isomorphism since it is not one-to-one. For instance, both $$\vec{0}$$ and $$\vec{e}_3$$ in $$\mathbb{R}^3$$ are mapped to the zero vector in $$\mathbb{R}^2$$.

**Example 1.3**  —

Of course, the domain and codomain might be other than spaces of column vectors. Both of these are homomorphisms; the verifications are straightforward.

1. $$f_1:\mathcal{P}_2\to \mathcal{P}_3$$ given by

$$
a_0+a_1x+a_2x^2 \;\mapsto\; a_0x+(a_1/2)x^2+(a_2/3)x^3
$$

2. $$f_2:M_{2 \! \times \! 2}\to \mathbb{R}$$ given by

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \mapsto a+d
$$

**Example 1.4**  —

Between any two spaces there is a **zero homomorphism**, mapping every vector in the domain to the zero vector in the codomain.

**Example 1.5**  —

These two suggest why we use the term "linear map".

1. The map $$g:\mathbb{R}^3\to \mathbb{R}$$ given by

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} \stackrel{g}{\longmapsto} 3x+2y-4.5z
$$

is linear (i.e., is a homomorphism). In contrast, the map $$\hat{g}:\mathbb{R}^3\to \mathbb{R}$$ given by

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} \stackrel{\hat{g}}{\longmapsto} 3x+2y-4.5z+1
$$

is not; for instance,

$$
\hat{g}(\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}+\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix})=4 \quad\text{while}\quad \hat{g}(\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}) +\hat{g}(\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix})=5
$$

(to show that a map is not linear we need only produce one example of a linear combination that is not preserved).
2. The first of these two maps $$t_1,t_2:\mathbb{R}^3\to \mathbb{R}^2$$ is linear while the second is not.

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} \stackrel{t_1}{\longmapsto} \begin{pmatrix} 5x-2y \\ x+y \end{pmatrix} \quad\text{and}\quad \begin{pmatrix} x \\ y \\ z \end{pmatrix} \stackrel{t_2}{\longmapsto} \begin{pmatrix} 5x-2y \\ xy \end{pmatrix}
$$

Finding an example that the second fails to preserve structure is easy.

What distinguishes the homomorphisms is that the coordinate functions are linear combinations of the arguments. See also Problem 7.

Obviously, any isomorphism is a homomorphism— an isomorphism is a homomorphism that is also a correspondence. So, one way to think of the "homomorphism" idea is that it is a generalization of "isomorphism", motivated by the observation that many of the properties of isomorphisms have only to do with the map's structure preservation property and not to do with it being a correspondence. As examples, these two results from the prior section do not use one-to-one-ness or onto-ness in their proof, and therefore apply to any homomorphism.

**Lemma 1.6**  —

A homomorphism sends a zero vector to a zero vector.

**Lemma 1.7**  —

Each of these is a necessary and sufficient condition for $$f:V\to W$$ to be a homomorphism.

1. $$f(c_1\cdot\vec{v}_1+c_2\cdot\vec{v}_2)=c_1\cdot f(\vec{v}_1)+c_2\cdot f(\vec{v}_2)$$ for any $$c_1,c_2\in\mathbb{R}$$ and $$\vec{v}_1,\vec{v}_2\in V$$
2. $$f(c_1\cdot\vec{v}_1+\dots+c_n\cdot\vec{v}_n) =c_1\cdot f(\vec{v}_1)+\dots+c_n\cdot f(\vec{v}_n)$$ for any $$c_1,\dots,c_n\in\mathbb{R}$$ and $$\vec{v}_1,\ldots,\vec{v}_n\in V$$

Part 1 is often used to check that a function is linear.

**Example 1.8**  —

The map $$f:\mathbb{R}^2\to \mathbb{R}^4$$ given by

$$
\begin{pmatrix} x \\ y \end{pmatrix} \stackrel{f}{\longmapsto} \begin{pmatrix} x/2 \\ 0 \\ x+y \\ 3y \end{pmatrix}
$$

satisfies 1 of the prior result

$$
\begin{pmatrix} r_1(x_1/2)+r_2(x_2/2) \\ 0 \\ r_1(x_1+y_1)+r_2(x_2+y_2) \\ r_1(3y_1)+r_2(3y_2) \end{pmatrix} = r_1\begin{pmatrix} x_1/2 \\ 0 \\ x_1+y_1 \\ 3y_1 \end{pmatrix} + r_2\begin{pmatrix} x_2/2 \\ 0 \\ x_2+y_2 \\ 3y_2 \end{pmatrix}
$$

and so it is a homomorphism.

However, some of the results that we have seen for isomorphisms fail to hold for homomorphisms in general. Consider the theorem that an isomorphism between spaces gives a correspondence between their bases. Homomorphisms do not give any such correspondence; Example 1.2 shows that there is no such correspondence, and another example is the zero map between any two nontrivial spaces. Instead, for homomorphisms a weaker but still very useful result holds.

**Theorem 1.9**  —

A homomorphism is determined by its action on a basis. That is, if $$\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ is a basis of a vector space $$V$$ and $$\vec{w}_1,\dots,\vec{w}_n$$ are (perhaps not distinct) elements of a vector space $$W$$ then there exists a homomorphism from $$V$$ to $$W$$ sending $$\vec{\beta}_1$$ to $$\vec{w}_1$$, ..., and $$\vec{\beta}_n$$ to $$\vec{w}_n$$, and that homomorphism is unique.

**Proof**  —

We will define the map by associating $$\vec{\beta}_1$$ with $$\vec{w}_1$$, etc., and then extending linearly to all of the domain. That is, where $$\vec{v}=c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n$$, the map $$h:V\to W$$ is given by $$h(\vec{v})=c_1\vec{w}_1+\dots+c_n\vec{w}_n$$. This is well-defined because, with respect to the basis, the representation of each domain vector $$\vec{v}$$ is unique.

This map is a homomorphism since it preserves linear combinations; where $$\vec{v_1}=c_1\vec{\beta}_1+\cdots+c_n\vec{\beta}_n$$ and $$\vec{v_2}=d_1\vec{\beta}_1+\cdots+d_n\vec{\beta}_n$$, we have this.

$$
\begin{array}{rl} h(r_1\vec{v}_1+r_2\vec{v}_2) &=h((r_1c_1+r_2d_1)\vec{\beta}_1+\dots+(r_1c_n+r_2d_n)\vec{\beta}_n) \\ &=(r_1c_1+r_2d_1)\vec{w}_1+\dots+(r_1c_n+r_2d_n)\vec{w}_n \\ &=r_1h(\vec{v}_1)+r_2h(\vec{v}_2) \end{array}
$$

And, this map is unique since if $$\hat{h}:V\to W$$ is another homomorphism such that $$\hat{h}(\vec{\beta}_i)=\vec{w}_i$$ for each $$i$$ then $$h$$ and $$\hat{h}$$ agree on all of the vectors in the domain.

$$
\begin{array}{rl} \hat{h}(\vec{v}) &=\hat{h}(c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n) \\ &=c_1\hat{h}(\vec{\beta}_1)+\dots+c_n\hat{h}(\vec{\beta}_n) \\ &=c_1\vec{w}_1+\dots+c_n\vec{w}_n \\ &=h(\vec{v}) \end{array}
$$

Thus, $$h$$ and $$\hat{h}$$ are the same map.

**Example 1.10**  —

This result says that we can construct a homomorphism by fixing a basis for the domain and specifying where the map sends those basis vectors. For instance, if we specify a map $$h:\mathbb{R}^2\to \mathbb{R}^2$$ that acts on the standard basis $$\mathcal{E}_2$$ in this way

$$
h(\begin{pmatrix} 1 \\ 0 \end{pmatrix})=\begin{pmatrix} -1 \\ 1 \end{pmatrix} \quad\text{and}\quad h(\begin{pmatrix} 0 \\ 1 \end{pmatrix})=\begin{pmatrix} -4 \\ 4 \end{pmatrix}
$$

then the action of $$h$$ on any other member of the domain is also specified. For instance, the value of $$h$$ on this argument

$$
h(\begin{pmatrix} 3 \\ -2 \end{pmatrix})=h(3\cdot \begin{pmatrix} 1 \\ 0 \end{pmatrix}-2\cdot \begin{pmatrix} 0 \\ 1 \end{pmatrix}) =3\cdot h(\begin{pmatrix} 1 \\ 0 \end{pmatrix})-2\cdot h(\begin{pmatrix} 0 \\ 1 \end{pmatrix}) =\begin{pmatrix} 5 \\ -5 \end{pmatrix}
$$

is a direct consequence of the value of $$h$$ on the basis vectors.

Later in this chapter we shall develop a scheme, using matrices, that is convienent for computations like this one.

Just as the isomorphisms of a space with itself are useful and interesting, so too are the homomorphisms of a space with itself.

**Definition 1.11**  —

A linear map from a space into itself $$t:V\to V$$ is a *linear transformation*.

**Remark 1.12**  —

In this book we use "linear transformation" only in the case where the codomain equals the domain, but it is widely used in other texts as a general synonym for "homomorphism".

**Example 1.13**  —

The map on $$\mathbb{R}^2$$ that projects all vectors down to the $$x$$-axis

$$
\begin{pmatrix} x \\ y \end{pmatrix}\mapsto\begin{pmatrix} x \\ 0 \end{pmatrix}
$$

is a linear transformation.

**Example 1.14**  —

The derivative map $$d/dx:\mathcal{P}_n\to \mathcal{P}_n$$

$$
a_0+a_1x+\cdots+a_nx^n \stackrel{d/dx}{\longmapsto} a_1+2a_2x+3a_3x^2+\cdots+na_nx^{n-1}
$$

is a linear transformation, as this result from calculus notes: $$d(c_1f+c_2g)/dx=c_1\,(df/dx)+c_2\,(dg/dx)$$.

**Example 1.15**  — The matrix transpose map

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \;\mapsto\; \begin{pmatrix} a &c \\ b &d \end{pmatrix}
$$

is a linear transformation of $$\mathcal{M}_{2 \! \times \! 2}$$. Note that this transformation is one-to-one and onto, and so in fact it is an automorphism.

We finish this subsection about maps by recalling that we can linearly combine maps. For instance, for these maps from $$\mathbb{R}^2$$ to itself

$$
\begin{pmatrix} x \\ y \end{pmatrix} \stackrel{f}{\longmapsto} \begin{pmatrix} 2x \\ 3x-2y \end{pmatrix} \quad\text{and}\quad \begin{pmatrix} x \\ y \end{pmatrix} \stackrel{g}{\longmapsto} \begin{pmatrix} 0 \\ 5x \end{pmatrix}
$$

the linear combination $$5f-2g$$ is also a map from $$R^2$$ to itself.

$$
\begin{pmatrix} x \\ y \end{pmatrix} \stackrel{5f-2g}{\longmapsto} \begin{pmatrix} 10x \\ 5x-10y \end{pmatrix}
$$

**Lemma 1.16**  —

For vector spaces $$V$$ and $$W$$, the set of linear functions from $$V$$ to $$W$$ is itself a vector space, a subspace of the space of all functions from $$V$$ to $$W$$. It is denoted $$\mathop{\mathcal{L}}(V,W)$$.

**Proof**  —

This set is non-empty because it contains the zero homomorphism. So to show that it is a subspace we need only check that it is closed under linear combinations. Let $$f,g:V\to W$$ be linear. Then their sum is linear

$$
\begin{array}{rl} (f+g)(c_1\vec{v}_1+c_2\vec{v}_2) &=c_1f(\vec{v}_1)+c_2f(\vec{v}_2) +c_1g(\vec{v}_1)+c_2g(\vec{v}_2) \\ &=c_1\bigl(f+g\bigr)(\vec{v}_1)+c_2\bigl(f+g\bigr)(\vec{v}_2) \end{array}
$$

and any scalar multiple is also linear.

$$
\begin{array}{rl} (r\cdot f)(c_1\vec{v}_1+c_2\vec{v}_2) &=r(c_1f(\vec{v}_1)+c_2f(\vec{v}_2)) \\ &=c_1(r\cdot f)(\vec{v}_1)+c_2(r\cdot f)(\vec{v}_2) \end{array}
$$

Hence $$\mathop{\mathcal{L}}(V,W)$$ is a subspace.

We started this section by isolating the structure preservation property of isomorphisms. That is, we defined homomorphisms as a generalization of isomorphisms. Some of the properties that we studied for isomorphisms carried over unchanged, while others were adapted to this more general setting.

It would be a mistake, though, to view this new notion of homomorphism as derived from, or somehow secondary to, that of isomorphism. In the rest of this chapter we shall work mostly with homomorphisms, partly because any statement made about homomorphisms is automatically true about isomorphisms, but more because, while the isomorphism concept is perhaps more natural, experience shows that the homomorphism concept is actually more fruitful and more central to further progress.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Decide if each $$h:\mathbb{R}^3\to \mathbb{R}^2$$ is linear.

1. $$h(\begin{pmatrix} x \\ y \\ z \end{pmatrix})=\begin{pmatrix} x \\ x+y+z \end{pmatrix}$$
2. $$h(\begin{pmatrix} x \\ y \\ z \end{pmatrix})=\begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
3. $$h(\begin{pmatrix} x \\ y \\ z \end{pmatrix})=\begin{pmatrix} 1 \\ 1 \end{pmatrix}$$
4. $$h(\begin{pmatrix} x \\ y \\ z \end{pmatrix})=\begin{pmatrix} 2x+y \\ 3y-4z \end{pmatrix}$$

**Answer**  —

1. Yes. The verification is straightforward.

$$
\begin{array}{rl} h( c_1\cdot\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} +c_2\cdot\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} ) &=h( \begin{pmatrix} c_1x_1+c_2x_2 \\ c_1y_1+c_2y_2 \\ c_1z_1+c_2z_2 \end{pmatrix} ) \\ &=\begin{pmatrix} c_1x_1+c_2x_2 \\ c_1x_1+c_2x_2+c_1y_1+c_2y_2+c_1z_1+c_2z_2 \end{pmatrix} \\ &=c_1\cdot\begin{pmatrix} x_1 \\ x_1+y_1+z_1 \end{pmatrix} +c_2\cdot\begin{pmatrix} x_2 \\ c_2+y_2+z_2 \end{pmatrix} \\ &=c_1\cdot h(\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}) +c_2\cdot h(\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}) \end{array}
$$

2. Yes. The verification is easy.

$$
\begin{array}{rl} h(c_1\cdot\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} +c_2\cdot\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}) &=h( \begin{pmatrix} c_1x_1+c_2x_2 \\ c_1y_1+c_2y_2 \\ c_1z_1+c_2z_2 \end{pmatrix} ) \\ &=\begin{pmatrix} 0 \\ 0 \end{pmatrix} \\ &=c_1\cdot h(\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}) +c_2\cdot h(\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}) \end{array}
$$

3. No. An example of an addition that is not respected is this.

$$
h(\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}+\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}) =\begin{pmatrix} 1 \\ 1 \end{pmatrix} \neq h(\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix})+h(\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix})
$$

4. Yes. The verification is straightforward.

$$
\begin{array}{rl} h( c_1\cdot\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} +c_2\cdot\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} ) &=h( \begin{pmatrix} c_1x_1+c_2x_2 \\ c_1y_1+c_2y_2 \\ c_1z_1+c_2z_2 \end{pmatrix} ) \\ &=\begin{pmatrix} 2(c_1x_1+c_2x_2)+(c_1y_1+c_2y_2) \\ 3(c_1y_1+c_2y_2)-4(c_1z_1+c_2z_2) \end{pmatrix} \\ &=c_1\cdot\begin{pmatrix} 2x_1+y_1 \\ 3y_1-4z_1 \end{pmatrix} +c_2\cdot\begin{pmatrix} 2x_2+y_2 \\ 3y_2-4z_2 \end{pmatrix} \\ &=c_1\cdot h(\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}) +c_2\cdot h(\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}) \end{array}
$$

*This exercise is recommended for all readers.*

**Problem 2**  —

Decide if each map $$h:\mathcal{M}_{2 \! \times \! 2}\to \mathbb{R}$$ is linear.

1. $$h(\begin{pmatrix} a &b \\ c &d \end{pmatrix})=a+d$$
2. $$h(\begin{pmatrix} a &b \\ c &d \end{pmatrix})=ad-bc$$
3. $$h(\begin{pmatrix} a &b \\ c &d \end{pmatrix})=2a+3b+c-d$$
4. $$h(\begin{pmatrix} a &b \\ c &d \end{pmatrix})=a^2+b^2$$

**Answer**  —

For each, we must either check that linear combinations are preserved, or give an example of a linear combination that is not.

1. Yes. The check that it preserves combinations is routine.

$$
\begin{array}{rl} h(r_1\cdot\begin{pmatrix} a_1 &b_1 \\ c_1 &d_1 \end{pmatrix} +r_2\cdot\begin{pmatrix} a_2 &b_2 \\ c_2 &d_2 \end{pmatrix}) &=h(\begin{pmatrix} r_1a_1+r_2a_2 &r_1b_1+r_2b_2 \\ r_1c_1+r_2c_2 &r_1d_1+r_2d_2 \end{pmatrix}) \\ &=(r_1a_1+r_2a_2)+(r_1d_1+r_2d_2) \\ &=r_1(a_1+d_1)+r_2(a_2+d_2) \\ &=r_1\cdot h(\begin{pmatrix} a_1 &b_1 \\ c_1 &d_1 \end{pmatrix}) +r_2\cdot h(\begin{pmatrix} a_2 &b_2 \\ c_2 &d_2 \end{pmatrix}) \end{array}
$$

2. No. For instance, not preserved is multiplication by the scalar $$2$$.

$$
h(2\cdot\begin{pmatrix} 1 &0 \\ 0 &1 \end{pmatrix}) =h(\begin{pmatrix} 2 &0 \\ 0 &2 \end{pmatrix}) =4 \quad\text{while}\quad 2\cdot h(\begin{pmatrix} 1 &0 \\ 0 &1 \end{pmatrix}) =2\cdot 1=2
$$

3. Yes. This is the check that it preserves combinations of two members of the domain.

$$
\begin{array}{rl} h(r_1\cdot\begin{pmatrix} a_1 &b_1 \\ c_1 &d_1 \end{pmatrix} +r_2\cdot\begin{pmatrix} a_2 &b_2 \\ c_2 &d_2 \end{pmatrix}) &=h(\begin{pmatrix} r_1a_1+r_2a_2 &r_1b_1+r_2b_2 \\ r_1c_1+r_2c_2 &r_1d_1+r_2d_2 \end{pmatrix}) \\ &=2(r_1a_1+r_2a_2)+3(r_1b_1+r_2b_2) +(r_1c_1+r_2c_2)-(r_1d_1+r_2d_2) \\ &=r_1(2a_1+3b_1+c_1-d_1) +r_2(2a_2+3b_2+c_2-d_2) \\ &=r_1\cdot h(\begin{pmatrix} a_1 &b_1 \\ c_1 &d_1 \end{pmatrix} +r_2\cdot h(\begin{pmatrix} a_2 &b_2 \\ c_2 &d_2 \end{pmatrix}) \end{array}
$$

4. No. An example of a combination that is not preserved is this.

$$
h(\begin{pmatrix} 1 &0 \\ 0 &0 \end{pmatrix} +\begin{pmatrix} 1 &0 \\ 0 &0 \end{pmatrix}) =h(\begin{pmatrix} 2 &0 \\ 0 &0 \end{pmatrix}) =4 \quad\text{while}\quad h(\begin{pmatrix} 1 &0 \\ 0 &0 \end{pmatrix}) +h(\begin{pmatrix} 1 &0 \\ 0 &0 \end{pmatrix}) =1+1 =2
$$

*This exercise is recommended for all readers.*

**Problem 3**  —

Show that these two maps are homomorphisms.

1. $$d/dx:\mathcal{P}_3\to \mathcal{P}_2$$ given by $$a_0+a_1x+a_2x^2+a_3x^3$$ maps to $$a_1+2a_2x+3a_3x^2$$
2. $$\int:\mathcal{P}_2\to \mathcal{P}_3$$ given by $$b_0+b_1x+b_2x^2$$ maps to $$b_0x+(b_1/2)x^2+(b_2/3)x^3$$

Are these maps inverse to each other?

**Answer**  —

The check that each is a homomorphisms is routine. Here is the check for the differentiation map.

$$
\frac{d}{dx}(r\cdot (a_0+a_1x+a_2x^2+a_3x^3) +s\cdot (b_0+b_1x+b_2x^2+b_3x^3))
$$

$$
\begin{array}{rl} &=\frac{d}{dx}((ra_0+sb_0)+(ra_1+sb_1)x+(ra_2+sb_2)x^2 +(ra_3+sb_3)x^3) \\ &=(ra_1+sb_1)+2(ra_2+sb_2)x+3(ra_3+sb_3)x^2 \\ &=r\cdot (a_1+2a_2x+3a_3x^2)+s\cdot (b_1+2b_2x+3b_3x^2) \\ &=r\cdot \frac{d}{dx}(a_0+a_1x+a_2x^2+a_3x^3) +s\cdot \frac{d}{dx} (b_0+b_1x+b_2x^2+b_3x^3) \end{array}
$$

(An alternate proof is to simply note that this is a property of differentiation that is familar from calculus.)

These two maps are not inverses as this composition does not act as the identity map on this element of the domain.

$$
1\in\mathcal{P}_3\;\stackrel{d/dx}{\longmapsto}\; 0\in\mathcal{P}_2\;\stackrel{\int}{\longmapsto}\; 0\in\mathcal{P}_3
$$

**Problem 4**  —

Is (perpendicular) projection from $$\mathbb{R}^3$$ to the $$xz$$-plane a homomorphism? Projection to the $$yz$$-plane? To the $$x$$-axis? The $$y$$-axis? The $$z$$-axis? Projection to the origin?

**Answer**  —

Each of these projections is a homomorphism. Projection to the $$xz$$-plane and to the $$yz$$-plane are these maps.

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix}\mapsto\begin{pmatrix} x \\ 0 \\ z \end{pmatrix} \qquad \begin{pmatrix} x \\ y \\ z \end{pmatrix}\mapsto\begin{pmatrix} 0 \\ y \\ z \end{pmatrix}
$$

Projection to the $$x$$-axis, to the $$y$$-axis, and to the $$z$$-axis are these maps.

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix}\mapsto\begin{pmatrix} x \\ 0 \\ 0 \end{pmatrix} \qquad \begin{pmatrix} x \\ y \\ z \end{pmatrix}\mapsto\begin{pmatrix} 0 \\ y \\ 0 \end{pmatrix} \qquad \begin{pmatrix} x \\ y \\ z \end{pmatrix}\mapsto\begin{pmatrix} 0 \\ 0 \\ z \end{pmatrix}
$$

And projection to the origin is this map.

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix}\mapsto\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$

Verification that each is a homomorphism is straightforward. (The last one, of course, is the zero transformation on $$\mathbb{R}^3$$.)

**Problem 5**  —

Show that, while the maps from Example 1.3 preserve linear operations, they are not isomorphisms.

**Answer**  —

The first is not onto; for instance, there is no polynomial that is sent the constant polynomial $$p(x)=1$$. The second is not one-to-one; both of these members of the domain

$$
\begin{pmatrix} 1 &0 \\ 0 &0 \end{pmatrix} \quad\text{and}\quad \begin{pmatrix} 0 &0 \\ 0 &1 \end{pmatrix}
$$

are mapped to the same member of the codomain, $$1\in\mathbb{R}$$.

**Problem 6**  —

Is an identity map a linear transformation?

**Answer**  —

Yes; in any space $$\text{id}(c\cdot \vec{v}+d\cdot \vec{w}) = c\cdot \vec{v}+d\cdot \vec{w} = c\cdot\text{id}(\vec{v})+d\cdot\text{id}(\vec{w})$$.  
*This exercise is recommended for all readers.*

**Problem 7**  —

Stating that a function is "linear" is different than stating that its graph is a line.

1. The function $$f_1:\mathbb{R}\to \mathbb{R}$$ given by $$f_1(x)=2x-1$$ has a graph that is a line. Show that it is not a linear function.
2. The function $$f_2:\mathbb{R}^2\to \mathbb{R}$$ given by

$$
\begin{pmatrix} x \\ y \end{pmatrix} \mapsto x+2y
$$

does not have a graph that is a line. Show that it is a linear function.

**Answer**  —

1. This map does not preserve structure since $$f(1+1)=3$$, while $$f(1)+f(1)=2$$.
2. The check is routine.

$$
\begin{array}{rl} f(r_1\cdot\begin{pmatrix} x_1 \\ y_1 \end{pmatrix}+r_2\cdot\begin{pmatrix} x_2 \\ y_2 \end{pmatrix}) &=f(\begin{pmatrix} r_1x_1+r_2x_2 \\ r_1y_1+r_2y_2 \end{pmatrix}) \\ &=(r_1x_1+r_2x_2)+2(r_1y_1+r_2y_2) \\ &=r_1\cdot (x_1+2y_1)+r_2\cdot (x_2+2y_2) \\ &=r_1\cdot f(\begin{pmatrix} x_1 \\ y_1 \end{pmatrix})+r_2\cdot f(\begin{pmatrix} x_2 \\ y_2 \end{pmatrix}) \end{array}
$$

*This exercise is recommended for all readers.*

**Problem 8**  —

Part of the definition of a linear function is that it respects addition. Does a linear function respect subtraction?

**Answer**  —

Yes. Where $$h:V\to W$$ is linear, $$h(\vec{u}-\vec{v})=h(\vec{u}+(-1)\cdot\vec{v})=h(\vec{u})+(-1)\cdot h(\vec{v})=h(\vec{u})-h(\vec{v})$$.

**Problem 9**  —

Assume that $$h$$ is a linear transformation of $$V$$ and that $$\langle \vec{\beta}_1,\ldots,\vec{\beta}_n \rangle$$ is a basis of $$V$$. Prove each statement.

1. If $$h(\vec{\beta}_i)=\vec{0}$$ for each basis vector then $$h$$ is the zero map.
2. If $$h(\vec{\beta}_i)=\vec{\beta}_i$$ for each basis vector then $$h$$ is the identity map.
3. If there is a scalar $$r$$ such that $$h(\vec{\beta}_i)=r\cdot\vec{\beta}_i$$ for each basis vector then $$h(\vec{v})=r\cdot\vec{v}$$ for all vectors in $$V$$.

**Answer**  —

1. Let $$\vec{v}\in V$$ be represented with respect to the basis as $$\vec{v}=c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n$$. Then $$h(\vec{v})=h(c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n)=c_1h(\vec{\beta}_1)+\dots+c_nh(\vec{\beta}_n)=c_1\cdot\vec{0}+\dots+c_n\cdot\vec{0}=\vec{0}$$.
2. This argument is similar to the prior one. Let $$\vec{v}\in V$$ be represented with respect to the basis as $$\vec{v}=c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n$$. Then $$h(c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n)=c_1h(\vec{\beta}_1)+\dots+c_nh(\vec{\beta}_n)=c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n=\vec{v}$$.
3. As above, only $$c_1h(\vec{\beta}_1)+\dots+c_nh(\vec{\beta}_n)=c_1r\vec{\beta}_1+\dots+c_nr\vec{\beta}_n=r(c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n)=r\vec{v}$$.  
*This exercise is recommended for all readers.*

**Problem 10**  —

Consider the vector space $$\mathbb{R}^+$$ where vector addition and scalar multiplication are not the ones inherited from $$\mathbb{R}$$ but rather are these: $$a+b$$ is the product of $$a$$ and $$b$$, and $$r\cdot a$$ is the $$r$$-th power of $$a$$. (This was shown to be a vector space in an earlier exercise.) Verify that the natural logarithm map $$\ln:\mathbb{R}^+\to \mathbb{R}$$ is a homomorphism between these two spaces. Is it an isomorphism?

**Answer**  —

That it is a homomorphism follows from the familiar rules that the logarithm of a product is the sum of the logarithms $$\ln(ab)=\ln(a)+\ln(b)$$ and that the logarithm of a power is the multiple of the logarithm $$\ln(a^r)=r\ln(a)$$. This map is an isomorphism because it has an inverse, namely, the exponential map, so it is a correspondence, and therefore it is an isomorphism.  
*This exercise is recommended for all readers.*

**Problem 11**  —

Consider this transformation of $$\mathbb{R}^2$$.

$$
\begin{pmatrix} x \\ y \end{pmatrix} \mapsto \begin{pmatrix} x/2 \\ y/3 \end{pmatrix}
$$

Find the image under this map of this ellipse.

$$
\{\begin{pmatrix} x \\ y \end{pmatrix} \,\big|\, (x^2/4)+(y^2/9)=1\}
$$

**Answer**  —

Where $$\hat{x}=x/2$$ and $$\hat{y}=y/3$$, the image set is

$$
\{\begin{pmatrix} \hat{x} \\ \hat{y} \end{pmatrix} \,\big|\, \frac{\displaystyle (2\hat{x})^2}{\displaystyle 4} +\frac{\displaystyle (3\hat{y})^2}{\displaystyle 9}=1\} =\{\begin{pmatrix} \hat{x} \\ \hat{y} \end{pmatrix} \,\big|\, \hat{x}^2+\hat{y}^2=1\}
$$

the unit circle in the $$\hat{x}\hat{y}$$-plane.  
*This exercise is recommended for all readers.*

**Problem 12**  —

Imagine a rope wound around the earth's equator so that it fits snugly (suppose that the earth is a sphere). How much extra rope must be added to raise the circle to a constant six feet off the ground?

**Answer**  —

The circumference function $$r\mapsto 2\pi r$$ is linear. Thus we have $$2\pi\cdot (r_{\text{earth}}+6)- 2\pi\cdot (r_{\text{earth}})=12\pi$$. Observe that it takes the same amount of extra rope to raise the circle from tightly wound around a basketball to six feet above that basketball as it does to raise it from tightly wound around the earth to six feet above the earth.  
*This exercise is recommended for all readers.*

**Problem 13**  —

Verify that this map $$h:\mathbb{R}^3\to \mathbb{R}$$

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix}\;\mapsto\; \begin{pmatrix} x \\ y \\ z \end{pmatrix}\cdot\begin{pmatrix} 3 \\ -1 \\ -1 \end{pmatrix}=3x-y-z
$$

is linear. Generalize.

**Answer**  —

Verifying that it is linear is routine.

$$
\begin{array}{rl} h(c_1\cdot \begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} +c_2\cdot \begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}) &=h(\begin{pmatrix} c_1x_1+c_2x_2 \\ c_1y_1+c_2y_2 \\ c_1z_1+c_2z_2 \end{pmatrix}) \\ &=3(c_1x_1+c_2x_2)-(c_1y_1+c_2y_2)-(c_1z_1+c_2z_2) \\ &=c_1\cdot (3x_1-y_1-z_1)+c_2\cdot (3x_2-y_2-z_2) \\ &=c_1\cdot h(\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}) +c_2\cdot h(\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}) \end{array}
$$

The natural guess at a generalization is that for any fixed $$\vec{k}\in\mathbb{R}^3$$ the map $$\vec{v}\mapsto\vec{v}\cdot\vec{k}$$ is linear. This statement is true. It follows from properties of the dot product we have seen earlier: $$(\vec{v}+\vec{u})\cdot\vec{k}=\vec{v}\cdot\vec{k}+ \vec{u}\cdot\vec{k}$$ and $$(r\vec{v})\cdot\vec{k}=r(\vec{v}\cdot\vec{k})$$. (The natural guess at a generalization of this generalization, that the map from $$\mathbb{R}^n$$ to $$\mathbb{R}$$ whose action consists of taking the dot product of its argument with a fixed vector $$\vec{k}\in\mathbb{R}^n$$ is linear, is also true.)

**Problem 14**  —

Show that every homomorphism from $$\mathbb{R}^1$$ to $$\mathbb{R}^1$$ acts via multiplication by a scalar. Conclude that every nontrivial linear transformation of $$\mathbb{R}^1$$ is an isomorphism. Is that true for transformations of $$\mathbb{R}^2$$? $$\mathbb{R}^n$$?

**Answer**  —

Let $$h:\mathbb{R}^1\to \mathbb{R}^1$$ be linear. A linear map is determined by its action on a basis, so fix the basis $$\langle 1 \rangle$$ for $$\mathbb{R}^1$$. For any $$r\in\mathbb{R}^1$$ we have that $$h(r)=h(r\cdot 1)=r\cdot h(1)$$ and so $$h$$ acts on any argument $$r$$ by multiplying it by the constant $$h(1)$$. If $$h(1)$$ is not zero then the map is a correspondence— its inverse is division by $$h(1)$$— so any nontrivial transformation of $$\mathbb{R}^1$$ is an isomorphism.

This projection map is an example that shows that not every transformation of $$\mathbb{R}^n$$ acts via multiplication by a constant when $$n>1$$, including when $$n=2$$.

$$
\begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} \mapsto\begin{pmatrix} x_1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}
$$

**Problem 15**  —

1. Show that for any scalars $$a_{1,1},\dots, a_{m,n}$$ this map $$h:\mathbb{R}^n\to \mathbb{R}^m$$ is a homomorphism.

$$
\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} \mapsto \begin{pmatrix} a_{1,1}x_1+\dots+a_{1,n}x_n \\ \vdots \\ a_{m,1}x_1+\cdots+a_{m,n}x_n \end{pmatrix}
$$

2. Show that for each $$i$$, the $$i$$-th derivative operator $$d^i/dx^i$$ is a linear transformation of $$\mathcal{P}_n$$. Conclude that for any scalars $$c_k,\ldots, c_0$$ this map is a linear transformation of that space.

$$
f\mapsto \frac{d^k}{dx^k}f+c_{k-1}\frac{d^{k-1}}{dx^{k-1}}f +\dots+ c_1\frac{d}{dx}f+c_0f
$$

**Answer**  —

1. Where $$c$$ and $$d$$ are scalars, we have this.

$$
\begin{array}{rl} h(c\cdot \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} +d\cdot \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}) &=h(\begin{pmatrix} cx_1+dy_1 \\ \vdots \\ cx_n+dy_n \end{pmatrix}) \\ &=\begin{pmatrix} a_{1,1}(cx_1+dy_1)+\dots+a_{1,n}(cx_n+dy_n) \\ \vdots \\ a_{m,1}(cx_1+dy_1)+\dots+a_{m,n}(cx_n+dy_n) \end{pmatrix} \\ &=c\cdot\begin{pmatrix} a_{1,1}x_1+\dots+a_{1,n}x_n \\ \vdots \\ a_{m,1}x_1+\dots+a_{m,n}x_n \end{pmatrix} +d\cdot\begin{pmatrix} a_{1,1}y_1+\dots+a_{1,n}y_n \\ \vdots \\ a_{m,1}y_1+\dots+a_{m,n}y_n \end{pmatrix} \\ &=c\cdot h(\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}) +d\cdot h(\begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}) \end{array}
$$

2. Each power $$i$$ of the derivative operator is linear because of these rules familiar from calculus.

$$
\frac{d^i}{dx^i}(\,f(x)+g(x)\,)=\frac{d^i}{dx^i}f(x) +\frac{d^i}{dx^i}g(x) \quad\text{and}\quad \frac{d^i}{dx^i}\,r\cdot f(x)=r\cdot\frac{d^i}{dx^i}f(x)
$$

Thus the given map is a linear transformation of $$\mathcal{P}_n$$ because any linear combination of linear maps is also a linear map.

**Problem 16**  —

Lemma 1.16 shows that a sum of linear functions is linear and that a scalar multiple of a linear function is linear. Show also that a composition of linear functions is linear.

**Answer**  —

(This argument has already appeared, as part of the proof that isomorphism is an equivalence.) Let $$f:U\to V$$ and $$g:V\to W$$ be linear. For any $$\vec{u}_1,\vec{u}_2\in U$$ and scalars $$c_1,c_2$$ combinations are preserved.

$$
g\circ f(c_1\vec{u}_1+c_2\vec{u}_2) =g(\,f(c_1\vec{u}_1+c_2\vec{u}_2)\,) =g(\,c_1f(\vec{u}_1)+c_2f(\vec{u}_2)\,)
$$

$$
=c_1\cdot g(f(\vec{u}_1))+c_2\cdot g(f(\vec{u}_2)) =c_1\cdot g\circ f(\vec{u}_1) +c_2\cdot g\circ f(\vec{u}_2)
$$

*This exercise is recommended for all readers.*

**Problem 17**  —

Where $$f:V\to W$$ is linear, suppose that $$f(\vec{v}_1)=\vec{w}_1$$, ..., $$f(\vec{v}_n)=\vec{w}_n$$ for some vectors $$\vec{w}_1$$, ..., $$\vec{w}_n$$ from $$W$$.

1. If the set of $$\vec{w}\,$$'s is independent, must the set of $$\vec{v}\,$$'s also be independent?
2. If the set of $$\vec{v}\,$$'s is independent, must the set of $$\vec{w}\,$$'s also be independent?
3. If the set of $$\vec{w}\,$$'s spans $$W$$, must the set of $$\vec{v}\,$$'s span $$V$$?
4. If the set of $$\vec{v}\,$$'s spans $$V$$, must the set of $$\vec{w}\,$$'s span $$W$$?

**Answer**  —

1. Yes. The set of $$\vec{w}\,$$'s cannot be linearly independent if the set of $$\vec{v}\,$$'s is linearly dependent because any nontrivial relationship in the domain $$\vec{0}_V=c_1\vec{v}_1+\dots+c_n\vec{v}_n$$ would give a nontrivial relationship in the range $$f(\vec{0}_V)=\vec{0}_W=f(c_1\vec{v}_1+\dots+c_n\vec{v}_n) =c_1f(\vec{v}_1)+\dots+c_nf(\vec{v}_n) =c_1\vec{w}+\dots+c_n\vec{w}_n$$.
2. Not necessarily. For instance, the transformation of $$\mathbb{R}^2$$ given by

$$
\begin{pmatrix} x \\ y \end{pmatrix} \mapsto \begin{pmatrix} x+y \\ x+y \end{pmatrix}
$$

sends this linearly independent set in the domain to a linearly dependent image.

$$
\{\vec{v}_1,\vec{v}_2\}=\{\begin{pmatrix} 1 \\ 0 \end{pmatrix},\begin{pmatrix} 1 \\ 1 \end{pmatrix}\} \;\mapsto\; \{\begin{pmatrix} 1 \\ 1 \end{pmatrix},\begin{pmatrix} 2 \\ 2 \end{pmatrix}\}=\{\vec{w}_1,\vec{w}_2\}
$$

3. Not necessarily. An example is the projection map $$\pi:\mathbb{R}^3\to \mathbb{R}^2$$

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix}\mapsto\begin{pmatrix} x \\ y \end{pmatrix}
$$

and this set that does not span the domain but maps to a set that does span the codomain.

$$
\{\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix},\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}\} \stackrel{\pi}{\longmapsto}\{\begin{pmatrix} 1 \\ 0 \end{pmatrix},\begin{pmatrix} 0 \\ 1 \end{pmatrix}\}
$$

4. Not necessarily. For instance, the injection map $$\iota:\mathbb{R}^2\to \mathbb{R}^3$$ sends the standard basis $$\mathcal{E}_2$$ for the domain to a set that does not span the codomain. (*Remark.* However, the set of $$\vec{w}$$'s does span the range. A proof is easy.)

**Problem 18**  —

Generalize Example 1.15 by proving that the matrix transpose map is linear. What is the domain and codomain?

**Answer**  —

Recall that the entry in row $$i$$ and column $$j$$ of the transpose of $$M$$ is the entry $$m_{j,i}$$ from row $$j$$ and column $$i$$ of $$M$$. Now, the check is routine.

$$
\begin{array}{rl} {{[r\cdot\begin{pmatrix} &\vdots \\ \cdots &a_{i,j} &\cdots \\ &\vdots \end{pmatrix} +s\cdot\begin{pmatrix} &\vdots \\ \cdots &b_{i,j} &\cdots \\ &\vdots \end{pmatrix}]}^{\rm trans}} &={{\begin{pmatrix} &\vdots \\ \cdots &ra_{i,j}+sb_{i,j} &\cdots \\ &\vdots \end{pmatrix}}^{\rm trans}} \\ &=\begin{pmatrix} &\vdots \\ \cdots &ra_{j,i}+sb_{j,i} &\cdots \\ &\vdots \end{pmatrix} \\ &=r\cdot\begin{pmatrix} &\vdots \\ \cdots &a_{j,i} &\cdots \\ &\vdots \end{pmatrix} +s\cdot\begin{pmatrix} &\vdots \\ \cdots &b_{j,i} &\cdots \\ &\vdots \end{pmatrix} \\ &=r\cdot{{\begin{pmatrix} &\vdots \\ \cdots &a_{j,i} &\cdots \\ &\vdots \end{pmatrix} }^{\rm trans}} +s\cdot{{\begin{pmatrix} &\vdots \\ \cdots &b_{j,i} &\cdots \\ &\vdots \end{pmatrix} }^{\rm trans}} \end{array}
$$

The domain is $$\mathcal{M}_{m \! \times \! n}$$ while the codomain is $$\mathcal{M}_{n \! \times \! m}$$.

**Problem 19**  —

1. Where $$\vec{u},\vec{v}\in \mathbb{R}^n$$, the line segment connecting them is defined to be the set $$\ell=\{t\cdot\vec{u}+(1-t)\cdot\vec{v}\,\big|\, t\in [0..1]\}$$. Show that the image, under a homomorphism $$h$$, of the segment between $$\vec{u}$$ and $$\vec{v}$$ is the segment between $$h(\vec{u})$$ and $$h(\vec{v})$$.
2. A subset of $$\mathbb{R}^n$$ is **convex** if, for any two points in that set, the line segment joining them lies entirely in that set. (The inside of a sphere is convex while the skin of a sphere is not.) Prove that linear maps from $$\mathbb{R}^n$$ to $$\mathbb{R}^m$$ preserve the property of set convexity.

**Answer**  —

1. For any homomorphism $$h:\mathbb{R}^n\to \mathbb{R}^m$$ we have

$$
h(\ell) =\{h(t\cdot\vec{u}+(1-t)\cdot\vec{v})\,\big|\, t\in [0..1]\} =\{t\cdot h(\vec{u})+(1-t)\cdot h(\vec{v})\,\big|\, t\in [0..1]\}
$$

which is the line segment from $$h(\vec{u})$$ to $$h(\vec{v})$$.
2. We must show that if a subset of the domain is convex then its image, as a subset of the range, is also convex. Suppose that $$C\subseteq \mathbb{R}^n$$ is convex and consider its image $$h(C)$$. To show $$h(C)$$ is convex we must show that for any two of its members, $$\vec{d}_1$$ and $$\vec{d}_2$$, the line segment connecting them

$$
\ell=\{t\cdot\vec{d}_1+(1-t)\cdot\vec{d}_2\,\big|\, t\in [0..1]\}
$$

is a subset of $$h(C)$$. Fix any member $$\hat{t}\cdot\vec{d}_1+(1-\hat{t})\cdot\vec{d}_2$$ of that line segment. Because the endpoints of $$\ell$$ are in the image of $$C$$, there are members of $$C$$ that map to them, say $$h(\vec{c}_1)=\vec{d}_1$$ and $$h(\vec{c}_2)=\vec{d}_2$$. Now, where $$\hat{t}$$ is the scalar that is fixed in the first sentence of this paragraph, observe that $$h(\hat{t}\cdot\vec{c}_1+(1-\hat{t})\cdot\vec{c}_2) =\hat{t}\cdot h(\vec{c}_1)+(1-\hat{t})\cdot h(\vec{c}_2) =\hat{t}\cdot\vec{d}_1+(1-\hat{t})\cdot\vec{d}_2$$ Thus, any member of $$\ell$$ is a member of $$h(C)$$, and so $$h(C)$$ is convex.  
*This exercise is recommended for all readers.*

**Problem 20**  —

Let $$h:\mathbb{R}^n\to \mathbb{R}^m$$ be a homomorphism.

1. Show that the image under $$h$$ of a line in $$\mathbb{R}^n$$ is a (possibly degenerate) line in $$\mathbb{R}^n$$.
2. What happens to a $$k$$-dimensional linear surface?

**Answer**  —

1. For $$\vec{v}_0,\vec{v}_1\in\mathbb{R}^n$$, the line through $$\vec{v}_0$$ with direction $$\vec{v}_1$$ is the set $$\{\vec{v}_0+t\cdot \vec{v}_1\,\big|\, t\in\mathbb{R}\}$$. The image under $$h$$ of that line $$\{h(\vec{v}_0+t\cdot \vec{v}_1)\,\big|\, t\in\mathbb{R}\} =\{h(\vec{v}_0)+t\cdot h(\vec{v}_1)\,\big|\, t\in\mathbb{R}\}$$ is the line through $$h(\vec{v}_0)$$ with direction $$h(\vec{v}_1)$$. If $$h(\vec{v}_1)$$ is the zero vector then this line is degenerate.
2. A $$k$$-dimensional linear surface in $$\mathbb{R}^n$$ maps to a (possibly degenerate) $$k$$-dimensional linear surface in $$\mathbb{R}^m$$. The proof is just like that the one for the line.

**Problem 21**  —

Prove that the restriction of a homomorphism to a subspace of its domain is another homomorphism.

**Answer**  —

Suppose that $$h:V\to W$$ is a homomorphism and suppose that $$S$$ is a subspace of $$V$$. Consider the map $$\hat{h}:S\to W$$ defined by $$\hat{h}(\vec{s})=h(\vec{s})$$. (The only difference between $$\hat{h}$$ and $$h$$ is the difference in domain.) Then this new map is linear: $$\hat{h}(c_1\cdot\vec{s}_1+c_2\cdot\vec{s}_2)= h(c_1\vec{s}_1+c_2\vec{s}_2)=c_1h(\vec{s}_1)+c_2h(\vec{s}_2)= c_1\cdot\hat{h}(\vec{s}_1)+c_2\cdot\hat{h}(\vec{s}_2)$$.

**Problem 22**  —

Assume that $$h:V\to W$$ is linear.

1. Show that the **rangespace** of this map $$\{h(\vec{v})\,\big|\, \vec{v}\in V\}$$ is a subspace of the codomain $$W$$.
2. Show that the **nullspace** of this map $$\{\vec{v}\in V\,\big|\, h(\vec{v})=\vec{0}_W\}$$ is a subspace of the domain $$V$$.
3. Show that if $$U$$ is a subspace of the domain $$V$$ then its image $$\{h(\vec{u})\,\big|\, \vec{u}\in U\}$$ is a subspace of the codomain $$W$$. This generalizes the first item.
4. Generalize the second item.

**Answer**  —

This will appear as a lemma in the next subsection.

1. The range is nonempty because $$V$$ is nonempty. To finish we need to show that it is closed under combinations. A combination of range vectors has the form, where $$\vec{v}_1,\dots,\vec{v}_n\in V$$,

$$
c_1\cdot h(\vec{v}_1)+\dots+c_n\cdot h(\vec{v}_n) = h(c_1\vec{v}_1)+\dots+h(c_n\vec{v}_n) = h(c_1\cdot \vec{v}_1+\dots+c_n\cdot \vec{v}_n),
$$

which is itself in the range as $$c_1\cdot \vec{v}_1+\dots+c_n\cdot \vec{v}_n$$ is a member of domain $$V$$. Therefore the range is a subspace.
2. The nullspace is nonempty since it contains $$\vec{0}_V$$, as $$\vec{0}_V$$ maps to $$\vec{0}_W$$. It is closed under linear combinations because, where $$\vec{v}_1,\dots,\vec{v}_n\in V$$ are elements of the inverse image set $$\{\vec{v}\in V\,\big|\, h(\vec{v})=\vec{0}_W\}$$, for $$c_1,\ldots,c_n\in\mathbb{R}$$

$$
\vec{0}_W=c_1\cdot h(\vec{v}_1)+\dots+c_n\cdot h(\vec{v}_n) =h(c_1\cdot \vec{v}_1+\dots+c_n\cdot \vec{v}_n)
$$

and so $$c_1\cdot \vec{v}_1+\dots+c_n\cdot \vec{v}_n$$ is also in the inverse image of $$\vec{0}_W$$.
3. This image of $$U$$ nonempty because $$U$$ is nonempty. For closure under combinations, where $$\vec{u}_1,\ldots,\vec{u}_n\in U$$,

$$
c_1\cdot h(\vec{u}_1)+\dots+c_n\cdot h(\vec{u}_n) = h(c_1\cdot \vec{u}_1)+\dots+h(c_n\cdot \vec{u}_n) = h(c_1\cdot \vec{u}_1+\dots+c_n\cdot \vec{u}_n)
$$

which is itself in $$h(U)$$ as $$c_1\cdot \vec{u}_1+\dots+c_n\cdot \vec{u}_n$$ is in $$U$$. Thus this set is a subspace.
4. The natural generalization is that the inverse image of a subspace of is a subspace. Suppose that $$X$$ is a subspace of $$W$$. Note that $$\vec{0}_W\in X$$ so the set $$\{\vec{v}\in V \,\big|\, h(\vec{v})\in X\}$$ is not empty. To show that this set is closed under combinations, let $$\vec{v}_1,\dots,\vec{v}_n$$ be elements of $$V$$ such that $$h(\vec{v}_1)=\vec{x}_1$$, ..., $$h(\vec{v}_n)=\vec{x}_n$$ and note that

$$
h(c_1\cdot \vec{v}_1+\dots+c_n\cdot \vec{v}_n) =c_1\cdot h(\vec{v}_1)+\dots+c_n\cdot h(\vec{v}_n) =c_1\cdot \vec{x}_1+\dots+c_n\cdot \vec{x}_n
$$

so a linear combination of elements of $$h^{-1}(X)$$ is also in $$h^{-1}(X)$$.

**Problem 23**  —

Consider the set of isomorphisms from a vector space to itself. Is this a subspace of the space $$\mathop{\mathcal{L}}(V,V)$$ of homomorphisms from the space to itself?

**Answer**  —

No; the set of isomorphisms does not contain the zero map (unless the space is trivial).

**Problem 24**  —

Does Theorem 1.9 need that $$\langle \vec{\beta}_1,\ldots,\vec{\beta}_n \rangle$$ is a basis? That is, can we still get a well-defined and unique homomorphism if we drop either the condition that the set of $$\vec{\beta}$$'s be linearly independent, or the condition that it span the domain?

**Answer**  —

If $$\langle \vec{\beta}_1,\ldots,\vec{\beta}_n \rangle$$ doesn't span the space then the map needn't be unique. For instance, if we try to define a map from $$\mathbb{R}^2$$ to itself by specifying only that $$\vec{e}_1$$ is sent to itself, then there is more than one homomorphism possible; both the identity map and the projection map onto the first component fit this condition.

If we drop the condition that $$\langle \vec{\beta}_1,\ldots,\vec{\beta}_n \rangle$$ is linearly independent then we risk an inconsistent specification (i.e, there could be no such map). An example is if we consider $$\langle \vec{e}_2,\vec{e}_1,2\vec{e}_1 \rangle$$, and try to define a map from $$\mathbb{R}^2$$ to itself that sends $$\vec{e}_2$$ to itself, and sends both $$\vec{e}_1$$ and $$2\vec{e}_1$$ to $$\vec{e}_1$$. No homomorphism can satisfy these three conditions.

**Problem 25**  —

Let $$V$$ be a vector space and assume that the maps $$f_1,f_2:V\to \mathbb{R}^1$$ are linear.

1. Define a map $$F:V\to \mathbb{R}^2$$ whose component functions are the given linear ones.

$$
\vec{v}\mapsto\begin{pmatrix} f_1(\vec{v}) \\ f_2(\vec{v}) \end{pmatrix}
$$

Show that $$F$$ is linear.
2. Does the converse hold— is any linear map from $$V$$ to $$\mathbb{R}^2$$ made up of two linear component maps to $$\mathbb{R}^1$$?
3. Generalize.

**Answer**  —

1. Briefly, the check of linearity is this.

$$
F(r_1\cdot \vec{v}_1+r_2\cdot \vec{v}_2) =\begin{pmatrix} f_1(r_1\vec{v}_1+r_2\vec{v}_2) \\ f_2(r_1\vec{v}_1+r_2\vec{v}_2) \end{pmatrix} =r_1\begin{pmatrix} f_1(\vec{v}_1) \\ f_2(\vec{v}_1) \end{pmatrix} +r_2\begin{pmatrix} f_1(\vec{v}_2) \\ f_2(\vec{v}_2) \end{pmatrix} =r_1\cdot F(\vec{v}_1)+r_2\cdot F(\vec{v}_2)
$$

2. Yes. Let $$\pi_1:\mathbb{R}^2\to \mathbb{R}^1$$ and $$\pi_2:\mathbb{R}^2\to \mathbb{R}^1$$ be the projections

$$
\begin{pmatrix} x \\ y \end{pmatrix}\stackrel{\pi_1}{\longmapsto} x \quad\text{and}\quad \begin{pmatrix} x \\ y \end{pmatrix}\stackrel{\pi_2}{\longmapsto} y
$$

onto the two axes. Now, where $$f_1(\vec{v})=\pi_1(F(\vec{v}))$$ and $$f_2(\vec{v})=\pi_2(F(\vec{v}))$$ we have the desired component functions.

$$
F(\vec{v})= \begin{pmatrix} f_1(\vec{v}) \\ f_2(\vec{v}) \end{pmatrix}
$$

They are linear because they are the composition of linear functions, and the fact that the composition of linear functions is linear was shown as part of the proof that isomorphism is an equivalence relation (alternatively, the check that they are linear is straightforward).
3. In general, a map from a vector space $$V$$ to an $$\mathbb{R}^n$$ is linear if and only if each of the component functions is linear. The verification is as in the prior item.

---

*Source: Wikibooks, Linear Algebra/Definition of Homomorphism (https://en.wikibooks.org/wiki/Linear_Algebra/Definition_of_Homomorphism), by Wikibooks contributors, CC BY-SA 4.0.*
