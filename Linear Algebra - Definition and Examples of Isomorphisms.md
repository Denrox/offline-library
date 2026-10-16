# Definition and Examples of Isomorphisms

We start with two examples that suggest the right definition.

**Example 1.1**  —

Consider the example mentioned above, the space of two-wide row vectors and the space of two-tall column vectors. They are "the same" in that if we associate the vectors that have the same components, e.g.,

$$
\begin{pmatrix} 1 &2 \end{pmatrix} \quad\longleftrightarrow\quad \begin{pmatrix} 1 \\ 2 \end{pmatrix}
$$

then this correspondence preserves the operations, for instance this addition

$$
\begin{pmatrix} 1 &2 \end{pmatrix}+\begin{pmatrix} 3 &4 \end{pmatrix}=\begin{pmatrix} 4 &6 \end{pmatrix} \quad\longleftrightarrow\quad \begin{pmatrix} 1 \\ 2 \end{pmatrix}+\begin{pmatrix} 3 \\ 4 \end{pmatrix}=\begin{pmatrix} 4 \\ 6 \end{pmatrix}
$$

and this scalar multiplication.

$$
5\cdot\begin{pmatrix} 1 &2 \end{pmatrix}=\begin{pmatrix} 5 &10 \end{pmatrix} \quad\longleftrightarrow\quad 5\cdot\begin{pmatrix} 1 \\ 2 \end{pmatrix}=\begin{pmatrix} 5 \\ 10 \end{pmatrix}
$$

More generally stated, under the correspondence

$$
\begin{pmatrix} a_0 &a_1 \end{pmatrix} \quad\longleftrightarrow\quad \begin{pmatrix} a_0 \\ a_1 \end{pmatrix}
$$

both operations are preserved:

$$
\begin{pmatrix} a_0 &a_1 \end{pmatrix}+\begin{pmatrix} b_0 &b_1 \end{pmatrix}=\begin{pmatrix} a_0+b_0 &a_1+b_1 \end{pmatrix} \longleftrightarrow \begin{pmatrix} a_0 \\ a_1 \end{pmatrix}+\begin{pmatrix} b_0 \\ b_1 \end{pmatrix}=\begin{pmatrix} a_0+b_0 \\ a_1+b_1 \end{pmatrix}
$$

and

$$
r\cdot\begin{pmatrix} a_0 &a_1 \end{pmatrix}=\begin{pmatrix} ra_0 &ra_1 \end{pmatrix} \quad\longleftrightarrow\quad r\cdot\begin{pmatrix} a_0 \\ a_1 \end{pmatrix}=\begin{pmatrix} ra_0 \\ ra_1 \end{pmatrix}
$$

(all of the variables are real numbers).

**Example 1.2**  —

Another two spaces we can think of as "the same" are $$\mathcal{P}_2$$, the space of quadratic polynomials, and $$\mathbb{R}^3$$. A natural correspondence is this.

$$
a_0+a_1x+a_2x^2 \quad\longleftrightarrow\quad \begin{pmatrix} a_0 \\ a_1 \\ a_2 \end{pmatrix} \qquad\qquad (\text{e.g., }1+2x+3x^2\,\longleftrightarrow\,\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix})
$$

The structure is preserved: corresponding elements add in a corresponding way

$$
\begin{array}{r} a_0+a_1x+a_2x^2\\ +\,\,b_0+b_1x+b_2x^2 \\ \hline (a_0+b_0)+(a_1+b_1)x+(a_2+b_2)x^2 \end{array} \quad\longleftrightarrow\quad \begin{pmatrix} a_0 \\ a_1 \\ a_2 \end{pmatrix} +\begin{pmatrix} b_0 \\ b_1 \\ b_2 \end{pmatrix} =\begin{pmatrix} a_0+b_0 \\ a_1+b_1 \\ a_2+b_2 \end{pmatrix}
$$

and scalar multiplication corresponds also.

$$
r\cdot(a_0+a_1x+a_2x^2)= (ra_0)+(ra_1)x+(ra_2)x^2 \quad\longleftrightarrow\quad r\cdot\begin{pmatrix} a_0 \\ a_1 \\ a_2 \end{pmatrix} =\begin{pmatrix} ra_0 \\ ra_1 \\ ra_2 \end{pmatrix}
$$

**Definition 1.3**  —

An **isomorphism** between two vector spaces $$V$$ and $$W$$ is a map $$f:V\to W$$ that

1. is a correspondence: $$f$$ is one-to-one and onto;
2. **preserves structure:** if $$\vec{v}_1,\vec{v}_2\in V$$ then

$$
f(\vec{v}_1+\vec{v}_2)=f(\vec{v}_1)+f(\vec{v}_2)
$$

and if $$\vec{v}\in V$$ and $$r\in\mathbb{R}$$ then

$$
f(r\vec{v})=r\,f(\vec{v})
$$

(we write $$V\cong W$$, read "$$V$$ is isomorphic to $$W$$", when such a map exists).

("Morphism" means map, so "isomorphism" means a map expressing sameness.)

**Example 1.4**  —

The vector space $$G=\{c_1\cos\theta+c_2\sin\theta\,\big|\, c_1,c_2\in\mathbb{R}\}$$ of functions of $$\theta$$ is isomorphic to the vector space $$\mathbb{R}^2$$ under this map.

$$
c_1\cos\theta+c_2\sin\theta\stackrel{f}{\longmapsto}\begin{pmatrix} c_1 \\ c_2 \end{pmatrix}
$$

We will check this by going through the conditions in the definition.

We will first verify condition 1, that the map is a correspondence between the sets underlying the spaces.

To establish that $$f$$ is one-to-one, we must prove that $$f(\vec{a})=f(\vec{b})$$ only when $$\vec{a}=\vec{b}$$. If

$$
f(a_1\cos\theta+a_2\sin\theta)=f(b_1\cos\theta+b_2\sin\theta)
$$

then, by the definition of $$f$$,

$$
\begin{pmatrix} a_1 \\ a_2 \end{pmatrix}=\begin{pmatrix} b_1 \\ b_2 \end{pmatrix}
$$

from which we can conclude that $$a_1=b_1$$ and $$a_2=b_2$$ because column vectors are equal only when they have equal components. We've proved that $$f(\vec{a})=f(\vec{b})$$ implies that $$\vec{a}=\vec{b}$$, which shows that $$f$$ is one-to-one.

To check that $$f$$ is onto we must check that any member of the codomain $$\mathbb{R}^2$$ is the image of some member of the domain $$G$$. But that's clear—any

$$
\begin{pmatrix} x \\ y \end{pmatrix}\in \mathbb{R}^2
$$

is the image under $$f$$ of $$x\cos\theta+y\sin\theta\in G$$.

Next we will verify condition (2), that $$f$$ preserves structure.

This computation shows that $$f$$ preserves addition.

$$
f\bigl(\,(a_1\cos\theta+a_2\sin\theta) +(b_1\cos\theta+b_2\sin\theta)\,\bigr)
$$

$$
\begin{array}{rl} &=f\bigl(\,(a_1+b_1)\cos\theta+(a_2+b_2)\sin\theta\,\bigr) \\ &=\begin{pmatrix} a_1+b_1 \\ a_2+b_2 \end{pmatrix} \\ &=\begin{pmatrix} a_1 \\ a_2 \end{pmatrix}+\begin{pmatrix} b_1 \\ b_2 \end{pmatrix} \\ &=f(a_1\cos\theta+a_2\sin\theta)+f(b_1\cos\theta+b_2\sin\theta) \end{array}
$$

A similar computation shows that $$f$$ preserves scalar multiplication.

$$
\begin{array}{rl} f\bigl(\,r\cdot(a_1\cos\theta+a_2\sin\theta)\,\bigr) &=f(\,ra_1\cos\theta+ra_2\sin\theta\,) \\ &=\begin{pmatrix} ra_1 \\ ra_2 \end{pmatrix} \\ &=r\cdot\begin{pmatrix} a_1 \\ a_2 \end{pmatrix} \\ &=r\cdot\, f(a_1\cos\theta+a_2\sin\theta) \end{array}
$$

With that, conditions (1) and (2) are verified, so we know that $$f$$ is an isomorphism and we can say that the spaces are isomorphic $$G\cong\mathbb{R}^2$$.

**Example 1.5**  —

Let $$V$$ be the space $$\{c_1x+c_2y+c_3z\,\big|\, c_1,c_2,c_3\in\mathbb{R}\}$$ of linear combinations of three variables $$x$$, $$y$$, and $$z$$, under the natural addition and scalar multiplication operations. Then $$V$$ is isomorphic to $$\mathcal{P}_2$$, the space of quadratic polynomials.

To show this we will produce an isomorphism map. There is more than one possibility; for instance, here are four.

$$
\begin{array}{c} c_1x+c_2y+c_3z \end{array} \quad \begin{array}{rl} \stackrel{f_1}{\longmapsto} &c_1+c_2x+c_3x^2 \\ \stackrel{f_2}{\longmapsto} &c_2+c_3x+c_1x^2 \\ \stackrel{f_3}{\longmapsto} &-c_1-c_2x-c_3x^2 \\ \stackrel{f_4}{\longmapsto} &c_1+(c_1+c_2)x+(c_1+c_3)x^2 \end{array}
$$

The first map is the more natural correspondence in that it just carries the coefficients over. However, below we shall verify that the second one is an isomorphism, to underline that there are isomorphisms other than just the obvious one (showing that $$f_1$$ is an isomorphism is Problem 3).

To show that $$f_2$$ is one-to-one, we will prove that if $$f_2(c_1x+c_2y+c_3z)=f_2(d_1x+d_2y+d_3z)$$ then $$c_1x+c_2y+c_3z=d_1x+d_2y+d_3z$$. The assumption that $$f_2(c_1x+c_2y+c_3z)=f_2(d_1x+d_2y+d_3z)$$ gives, by the definition of $$f_2$$, that $$c_2+c_3x+c_1x^2=d_2+d_3x+d_1x^2$$. Equal polynomials have equal coefficients, so $$c_2=d_2$$, $$c_3=d_3$$, and $$c_1=d_1$$. Thus $$f_2(c_1x+c_2y+c_3z)=f_2(d_1x+d_2y+d_3z)$$ implies that $$c_1x+c_2y+c_3z=d_1x+d_2y+d_3z$$ and therefore $$f_2$$ is one-to-one.

The map $$f_2$$ is onto because any member $$a+bx+cx^2$$ of the codomain is the image of some member of the domain, namely it is the image of $$cx+ay+bz$$. For instance, $$2+3x-4x^2$$ is $$f_2(-4x+2y+3z)$$.

The computations for structure preservation are like those in the prior example. This map preserves addition

$$
f_2\bigl((c_1x+c_2y+c_3z) +(d_1x+d_2y+d_3z)\bigr)
$$

$$
\begin{array}{rl} &=f_2\bigl((c_1+d_1)x+(c_2+d_2)y+(c_3+d_3)z\bigr) \\ &=(c_2+d_2)+(c_3+d_3)x+(c_1+d_1)x^2 \\ &=(c_2+c_3x+c_1x^2)+(d_2+d_3x+d_1x^2) \\ &=f_2(c_1x+c_2y+c_3z)+f_2(d_1x+d_2y+d_3z) \end{array}
$$

and scalar multiplication.

$$
\begin{array}{rl} f_2\bigl(r\cdot(c_1x+c_2y+c_3z)\bigr) &=f_2(rc_1x+rc_2y+rc_3z) \\ &=rc_2+rc_3x+rc_1x^2 \\ &=r\cdot(c_2+c_3x+c_1x^2) \\ &=r\cdot\, f_2(c_1x+c_2y+c_3z) \end{array}
$$

Thus $$f_2$$ is an isomorphism and we write $$V\cong\mathcal{P}_2$$.

We are sometimes interested in an isomorphism of a space with itself, called an **automorphism**. An identity map is an automorphism. The next two examples show that there are others.

**Example 1.6**  —

A **dilation** map $$d_s:\mathbb{R}^2\to \mathbb{R}^2$$ that multiplies all vectors by a nonzero scalar $$s$$ is an automorphism of $$\mathbb{R}^2$$.

A **rotation** or **turning map** $$t_{\theta}:\mathbb{R}^2\to \mathbb{R}^2$$ that rotates all vectors through an angle $$\theta$$ is an automorphism.

A third type of automorphism of $$\mathbb{R}^2$$ is a map $$f_\ell:\mathbb{R}^2\to \mathbb{R}^2$$ that **flips** or **reflects** all vectors over a line $$\ell$$ through the origin.

See Problem 20.

**Example 1.7**  —

Consider the space $$\mathcal{P}_5$$ of polynomials of degree 5 or less and the map $$f$$ that sends a polynomial $$p(x)$$ to $$p(x-1)$$. For instance, under this map $$x^2\mapsto (x-1)^2=x^2-2x+1$$ and $$x^3+2x\mapsto (x-1)^3+2(x-1)=x^3-3x^2+5x-3$$. This map is an automorphism of this space; the check is Problem 12.

This isomorphism of $$\mathcal{P}_5$$ with itself does more than just tell us that the space is "the same" as itself. It gives us some insight into the space's structure. For instance, below is shown a family of parabolas, graphs of members of $$\mathcal{P}_5$$. Each has a vertex at $$y=-1$$, and the left-most one has zeroes at $$-2.25$$ and $$-1.75$$, the next one has zeroes at $$-1.25$$ and $$-0.75$$, etc.

Geometrically, the substitution of $$x-1$$ for $$x$$ in any function's argument shifts its graph to the right by one. Thus, $$f(p_0)=p_1$$ and $$f$$'s action is to shift all of the parabolas to the right by one. Notice that the picture before $$f$$ is applied is the same as the picture after $$f$$ is applied, because while each parabola moves to the right, another one comes in from the left to take its place. This also holds true for cubics, etc. So the automorphism $$f$$ gives us the insight that $$P_5$$ has a certain horizontal homogeneity; this space looks the same near $$x=1$$ as near $$x=0$$.  
As described in the preamble to this section, we will next produce some results supporting the contention that the definition of isomorphism above captures our intuition of vector spaces being the same.

Of course the definition itself is persuasive: a vector space consists of two components, a set and some structure, and the definition simply requires that the sets correspond and that the structures correspond also. Also persuasive are the examples above. In particular, Example 1.1, which gives an isomorphism between the space of two-wide row vectors and the space of two-tall column vectors, dramatizes our intuition that isomorphic spaces are the same in all relevant respects. Sometimes people say, where $$V\cong W$$, that "$$W$$ is just $$V$$ painted green"—any differences are merely cosmetic.

Further support for the definition, in case it is needed, is provided by the following results that, taken together, suggest that all the things of interest in a vector space correspond under an isomorphism. Since we studied vector spaces to study linear combinations, "of interest" means "pertaining to linear combinations". Not of interest is the way that the vectors are presented typographically (or their color!).

As an example, although the definition of isomorphism doesn't explicitly say that the zero vectors must correspond, it is a consequence of that definition.

**Lemma 1.8**  —

An isomorphism maps a zero vector to a zero vector.

**Proof**  —

Where $$f:V\to W$$ is an isomorphism, fix any $$\vec{v}\in V$$. Then $$f(\vec{0}_V)=f(0\cdot\vec{v})=0\cdot f(\vec{v})=\vec{0}_W$$.

The definition of isomorphism requires that sums of two vectors correspond and that so do scalar multiples. We can extend that to say that all linear combinations correspond.

**Lemma 1.9**  —

For any map $$f:V\to W$$ between vector spaces these statements are equivalent.

1. $$f$$ preserves structure

$$
f(\vec{v}_1+\vec{v}_2)=f(\vec{v}_1)+f(\vec{v}_2) \quad\text{and}\quad f(c\vec{v})=c\,f(\vec{v})
$$

2. $$f$$ preserves linear combinations of two vectors

$$
f(c_1\vec{v}_1+c_2\vec{v}_2)=c_1f(\vec{v}_1)+c_2f(\vec{v}_2)
$$

3. $$f$$ preserves linear combinations of any finite number of vectors

$$
f(c_1\vec{v}_1+\dots+c_n\vec{v}_n)= c_1f(\vec{v}_1)+\dots+c_nf(\vec{v}_n)
$$

**Proof**  —

Since the implications $$3\!\implies\!2$$ and $$2\!\implies\!1$$ are clear, we need only show that $$1\!\implies\!3$$. Assume statement 1. We will prove statement 3 by induction on the number of summands $$n$$.

The one-summand base case, that $$f(c\vec{v}_1)=c\,f(\vec{v}_1)$$, is covered by the assumption of statement 1.

For the inductive step assume that statement 3 holds whenever there are $$k$$ or fewer summands, that is, whenever $$n=1$$, or $$n=2$$, ..., or $$n=k$$. Consider the $$k+1$$-summand case. The first half of 1 gives

$$
f(c_1\vec{v}_1+\dots+c_k\vec{v}_k+c_{k+1}\vec{v}_{k+1}) =f(c_1\vec{v}_1+\dots+c_k\vec{v}_k)+f(c_{k+1}\vec{v}_{k+1})
$$

by breaking the sum along the final "$$+$$". Then the inductive hypothesis lets us break up the $$k$$-term sum.

$$
=f(c_1\vec{v}_1)+\dots+f(c_k\vec{v}_k)+f(c_{k+1}\vec{v}_{k+1})
$$

Finally, the second half of statement 1 gives

$$
=c_1\,f(\vec{v}_1)+\dots+c_k\,f(\vec{v}_k)+c_{k+1}\,f(\vec{v}_{k+1})
$$

when applied $$k+1$$ times.

In addition to adding to the intuition that the definition of isomorphism does indeed preserve the things of interest in a vector space, that lemma's second item is an especially handy way of checking that a map preserves structure.

We close with a summary. The material in this section augments the chapter on Vector Spaces. There, after giving the definition of a vector space, we informally looked at what different things can happen. Here, we defined the relation "$$\cong$$" between vector spaces and we have argued that it is the right way to split the collection of vector spaces into cases because it preserves the features of interest in a vector space—in particular, it preserves linear combinations. That is, we have now said precisely what we mean by "the same", and by "different", and so we have precisely classified the vector spaces.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Verify, using Example 1.4 as a model, that the two correspondences given before the definition are isomorphisms.

1. Example 1.1
2. Example 1.2  
*This exercise is recommended for all readers.*

**Problem 2**  —

For the map $$f:\mathcal{P}_1\to \mathbb{R}^2$$ given by

$$
a+bx\stackrel{f}{\longmapsto}\begin{pmatrix} a-b \\ b \end{pmatrix}
$$

Find the image of each of these elements of the domain.

1. $$3-2x$$
2. $$2+2x$$
3. $$x$$

Show that this map is an isomorphism.

**Problem 3**  —

Show that the natural map $$f_1$$ from Example 1.5 is an isomorphism.  
*This exercise is recommended for all readers.*

**Problem 4**  —

Decide whether each map is an isomorphism (if it is an isomorphism then prove it and if it isn't then state a condition that it fails to satisfy).

1. $$f:\mathcal{M}_{2 \! \times \! 2}\to \mathbb{R}$$ given by

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \mapsto ad-bc
$$

2. $$f:\mathcal{M}_{2 \! \times \! 2}\to \mathbb{R}^4$$ given by

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \mapsto \begin{pmatrix} a+b+c+d \\ a+b+c \\ a+b \\ a \end{pmatrix}
$$

3. $$f:\mathcal{M}_{2 \! \times \! 2}\to \mathcal{P}_3$$ given by

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \mapsto c+(d+c)x+(b+a)x^2+ax^3
$$

4. $$f:\mathcal{M}_{2 \! \times \! 2}\to \mathcal{P}_3$$ given by

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \mapsto c+(d+c)x+(b+a+1)x^2+ax^3
$$

**Problem 5**  —

Show that the map $$f:\mathbb{R}^1\to \mathbb{R}^1$$ given by $$f(x)=x^3$$ is one-to-one and onto.Is it an isomorphism?  
*This exercise is recommended for all readers.*

**Problem 6**  —

Refer to Example 1.1. Produce two more isomorphisms (of course, that they satisfy the conditions in the definition of isomorphism must be verified).

**Problem 7**  —

Refer to Example 1.2. Produce two more isomorphisms (and verify that they satisfy the conditions).  
*This exercise is recommended for all readers.*

**Problem 8**  —

Show that, although $$\mathbb{R}^2$$ is not itself a subspace of $$\mathbb{R}^3$$, it is isomorphic to the $$xy$$-plane subspace of $$\mathbb{R}^3$$.

**Problem 9**  —

Find two isomorphisms between $$\mathbb{R}^{16}$$ and $$\mathcal{M}_{4 \! \times \! 4}$$.  
*This exercise is recommended for all readers.*

**Problem 10**  —

For what $$k$$ is $$\mathcal{M}_{m \! \times \! n}$$ isomorphic to $$\mathbb{R}^{k}$$?

**Problem 11**  —

For what $$k$$ is $$\mathcal{P}_k$$ isomorphic to $$\mathbb{R}^n$$?

**Problem 12**  —

Prove that the map in Example 1.7, from $$\mathcal{P}_5$$ to $$\mathcal{P}_5$$ given by $$p(x)\mapsto p(x-1)$$, is a vector space isomorphism.

**Problem 13**  —

Why, in Lemma 1.8, must there be a $$\vec{v}\in V$$? That is, why must $$V$$ be nonempty?

**Problem 14**  —

Are any two trivial spaces isomorphic?

**Problem 15**  —

In the proof of Lemma 1.9, what about the zero-summands case (that is, if $$n$$ is zero)?

**Problem 16**  —

Show that any isomorphism $$f:\mathcal{P}_0\to \mathbb{R}^1$$ has the form $$a\mapsto ka$$ for some nonzero real number $$k$$.  
*This exercise is recommended for all readers.*

**Problem 17**  —

These prove that isomorphism is an equivalence relation.

1. Show that the identity map $$\text{id}:V\to V$$ is an isomorphism. Thus, any vector space is isomorphic to itself.
2. Show that if $$f:V\to W$$ is an isomorphism then so is its inverse $$f^{-1}:W\to V$$. Thus, if $$V$$ is isomorphic to $$W$$ then also $$W$$ is isomorphic to $$V$$.
3. Show that a composition of isomorphisms is an isomorphism: if $$f:V\to W$$ is an isomorphism and $$g:W\to U$$ is an isomorphism then so also is $$g\circ f:V\to U$$. Thus, if $$V$$ is isomorphic to $$W$$ and $$W$$ is isomorphic to $$U$$, then also $$V$$ is isomorphic to $$U$$.

**Problem 18**  —

Suppose that $$f:V\to W$$ preserves structure. Show that $$f$$ is one-to-one if and only if the unique member of $$V$$ mapped by $$f$$ to $$\vec{0}_W$$ is $$\vec{0}_V$$.

**Problem 19**  —

Suppose that $$f:V\to W$$ is an isomorphism. Prove that the set $$\{\vec{v}_1,\dots,\vec{v}_k\}\subseteq V$$ is linearly dependent if and only if the set of images $$\{f(\vec{v}_1),\dots,f(\vec{v}_k)\}\subseteq W$$ is linearly dependent.  
*This exercise is recommended for all readers.*

**Problem 20**  —

Show that each type of map from Example 1.6 is an automorphism.

1. Dilation $$d_s$$ by a nonzero scalar $$s$$.
2. Rotation $$t_\theta$$ through an angle $$\theta$$.
3. Reflection $$f_\ell$$ over a line through the origin.

*Hint.* For the second and third items, polar coordinates are useful.

**Problem 21**  —

Produce an automorphism of $$\mathcal{P}_2$$ other than the identity map, and other than a shift map $$p(x)\mapsto p(x-k)$$.

**Problem 22**  —

1. Show that a function $$f:\mathbb{R}^1\to \mathbb{R}^1$$ is an automorphism if and only if it has the form $$x\mapsto kx$$ for some $$k\neq 0$$.
2. Let $$f$$ be an automorphism of $$\mathbb{R}^1$$ such that $$f(3)=7$$. Find $$f(-2)$$.
3. Show that a function $$f:\mathbb{R}^2\to \mathbb{R}^2$$ is an automorphism if and only if it has the form

$$
\begin{pmatrix} x \\ y \end{pmatrix} \mapsto \begin{pmatrix} ax+by \\ cx+dy \end{pmatrix}
$$

for some $$a,b,c,d\in\mathbb{R}$$ with $$ad-bc\neq 0$$. *Hint.* Exercises in prior subsections have shown that

$$
\begin{pmatrix} b \\ d \end{pmatrix}\text{ is not a multiple of }\begin{pmatrix} a \\ c \end{pmatrix}
$$

if and only if $$ad-bc\neq 0$$.
4. Let $$f$$ be an automorphism of $$\mathbb{R}^2$$ with

$$
f(\begin{pmatrix} 1 \\ 3 \end{pmatrix})=\begin{pmatrix} 2 \\ -1 \end{pmatrix} \quad\text{and}\quad f(\begin{pmatrix} 1 \\ 4 \end{pmatrix})=\begin{pmatrix} 0 \\ 1 \end{pmatrix}.
$$

Find

$$
f(\begin{pmatrix} 0 \\ -1 \end{pmatrix}).
$$

**Problem 23**  —

Refer to Lemma 1.8 and Lemma 1.9. Find two more things preserved by isomorphism.

**Problem 24**  —

We show that isomorphisms can be tailored to fit in that, sometimes, given vectors in the domain and in the range we can produce an isomorphism associating those vectors.

1. Let $$B=\langle \vec{\beta}_1,\vec{\beta}_2,\vec{\beta}_3 \rangle$$ be a basis for $$\mathcal{P}_2$$ so that any $$\vec{p}\in\mathcal{P}_2$$ has a unique representation as $$\vec{p}=c_1\vec{\beta}_1+c_2\vec{\beta}_2+c_3\vec{\beta}_3$$, which we denote in this way.

$$
{\rm Rep}_{B}(\vec{p})=\begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix}
$$

Show that the $${\rm Rep}_{B}(\cdot)$$ operation is a function from $$\mathcal{P}_2$$ to $$\mathbb{R}^3$$ (this entails showing that with every domain vector $$\vec{v}\in\mathcal{P}_2$$ there is an associated image vector in $$\mathbb{R}^3$$, and further, that with every domain vector $$\vec{v}\in\mathcal{P}_2$$ there is at most one associated image vector).
2. Show that this $${\rm Rep}_{B}(\cdot)$$ function is one-to-one and onto.
3. Show that it preserves structure.
4. Produce an isomorphism from $$\mathcal{P}_2$$ to $$\mathbb{R}^3$$ that fits these specifications.

$$
x+x^2\mapsto\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \quad\text{and}\quad 1-x\mapsto\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
$$

**Problem 25**  —

Prove that a space is $$n$$-dimensional if and only if it is isomorphic to $$\mathbb{R}^n$$. *Hint.* Fix a basis $$B$$ for the space and consider the map sending a vector over to its representation with respect to $$B$$.

**Problem 26**  —

*(Requires the subsection on Combining Subspaces, which is optional.)* Let $$U$$ and $$W$$ be vector spaces. Define a new vector space, consisting of the set $$U\times W=\{(\vec{u},\vec{w}) \,\big|\, \vec{u}\in U\text{ and } \vec{w}\in W\}$$ along with these operations.

$$
(\vec{u}_1,\vec{w}_1)+(\vec{u}_2,\vec{w}_2)= (\vec{u}_1+\vec{u}_2,\vec{w}_1+\vec{w}_2) \quad\text{and}\quad r\cdot (\vec{u},\vec{w})=(r\vec{u},r\vec{w})
$$

This is a vector space, the **external direct sum** of $$U$$ and $$W$$.

1. Check that it is a vector space.
2. Find a basis for, and the dimension of, the external direct sum $$\mathcal{P}_2\times\mathbb{R}^2$$.
3. What is the relationship among $$\dim(U)$$, $$\dim(W)$$, and $$\dim(U\times W)$$?
4. Suppose that $$U$$ and $$W$$ are subspaces of a vector space $$V$$ such that $$V=U\oplus W$$ (in this case we say that $$V$$ is the **internal direct sum** of $$U$$ and $$W$$). Show that the map $$f:U\times W\to V$$ given by

$$
(\vec{u},\vec{w})\stackrel{f}{\longmapsto} \vec{u}+\vec{w}
$$

is an isomorphism. Thus if the internal direct sum is defined then the internal and external direct sums are isomorphic.

Solutions

### Footnotes

---

*Source: Wikibooks, Linear Algebra/Definition and Examples of Isomorphisms (https://en.wikibooks.org/wiki/Linear_Algebra/Definition_and_Examples_of_Isomorphisms), by Wikibooks contributors, CC BY-SA 4.0.*
