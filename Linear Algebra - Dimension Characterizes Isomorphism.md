# Dimension Characterizes Isomorphism

In the prior subsection, after stating the definition of an isomorphism, we gave some results supporting the intuition that such a map describes spaces as "the same". Here we will formalize this intuition. While two spaces that are isomorphic are not equal, we think of them as almost equal— as equivalent. In this subsection we shall show that the relationship "is isomorphic to" is an equivalence relation.

**Theorem 2.1**  —

Isomorphism is an equivalence relation between vector spaces.

**Proof**  —

We must prove that this relation has the three properties of being symmetric, reflexive, and transitive. For each of the three we will use item 2 of [Lemma 1.9](Linear%20Algebra%20-%20Definition%20and%20Examples%20of%20Isomorphisms.md) and show that the map preserves structure by showing that it preserves linear combinations of two members of the domain.

To check reflexivity, that any space is isomorphic to itself, consider the identity map. It is clearly one-to-one and onto. The calculation showing that it preserves linear combinations is easy.

$$
\text{id}(c_1\cdot \vec{v}_1+c_2\cdot \vec{v}_2) =c_1\vec{v}_1+c_2\vec{v}_2 =c_1\cdot \text{id}(\vec{v}_1)+c_2\cdot \text{id}(\vec{v}_2)
$$

To check symmetry, that if $$V$$ is isomorphic to $$W$$ via some map $$f:V\to W$$ then there is an isomorphism going the other way, consider the inverse map $$f^{-1}:W\to V$$. As stated in the appendix, such an inverse function exists and it is also a correspondence. Thus we have reduced the symmetry issue to checking that, because $$f$$ preserves linear combinations, so also does $$f^{-1}$$. Assume that $$\vec{w}_1=f(\vec{v}_1)$$ and $$\vec{w}_2=f(\vec{v}_2)$$, i.e., that $$f^{-1}(\vec{w}_1)=\vec{v}_1$$ and $$f^{-1}(\vec{w}_2)=\vec{v}_2$$.

$$
\begin{array}{rl} f^{-1}(c_1\cdot\vec{w}_1+c_2\cdot\vec{w}_2) &=f^{-1}\bigl(\,c_1\cdot f(\vec{v}_1) +c_2\cdot f(\vec{v}_2)\,\bigr) \\ &=f^{-1}(\,f\bigl(c_1\vec{v}_1+c_2\vec{v}_2)\,\bigr) \\ &=c_1\vec{v}_1+c_2\vec{v}_2 \\ &=c_1\cdot f^{-1}(\vec{w}_1)+c_2\cdot f^{-1}(\vec{w}_2) \end{array}
$$

Finally, we must check transitivity, that if $$V$$ is isomorphic to $$W$$ via some map $$f$$ and if $$W$$ is isomorphic to $$U$$ via some map $$g$$ then also $$V$$ is isomorphic to $$U$$. Consider the composition $$g\circ f:V\to U$$. The appendix notes that the composition of two correspondences is a correspondence, so we need only check that the composition preserves linear combinations.

$$
\begin{array}{rl} g\circ f\,\bigl(c_1\cdot\vec{v}_1+c_2\cdot\vec{v}_2\bigr) &=g\bigl(\,f(c_1\cdot \vec{v}_1+c_2\cdot\vec{v}_2)\,\bigr) \\ &=g\bigl(\,c_1\cdot f(\vec{v}_1)+c_2\cdot f(\vec{v}_2)\,\bigr) \\ &=c_1\cdot g\bigl(f(\vec{v}_1))+c_2\cdot g(f(\vec{v}_2)\bigr) \\ &=c_1\cdot(g\circ f)\,(\vec{v}_1) +c_2\cdot(g\circ f)\,(\vec{v}_2) \end{array}
$$

Thus $$g\circ f:V\to U$$ is an isomorphism.

As a consequence of that result, we know that the universe of vector spaces is partitioned into classes: every space is in one and only one isomorphism class.

All finite dimensional

- vector spaces:

$$
V\cong W
$$

**Theorem 2.2**  —

Vector spaces are isomorphic if and only if they have the same dimension.

This follows from the next two lemmas.

**Lemma 2.3**  —

If spaces are isomorphic then they have the same dimension.

**Proof**  —

We shall show that an isomorphism of two spaces gives a correspondence between their bases. That is, where $$f:V\to W$$ is an isomorphism and a basis for the domain $$V$$ is $$B=\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$, then the image set $$D=\langle f(\vec{\beta}_1),\dots,f(\vec{\beta}_n) \rangle$$ is a basis for the codomain $$W$$. (The other half of the correspondence— that for any basis of $$W$$ the inverse image is a basis for $$V$$— follows on recalling that if $$f$$ is an isomorphism then $$f^{-1}$$ is also an isomorphism, and applying the prior sentence to $$f^{-1}$$.)

To see that $$D$$ spans $$W$$, fix any $$\vec{w}\in W$$, note that $$f$$ is onto and so there is a $$\vec{v}\in V$$ with $$\vec{w}=f(\vec{v})$$, and expand $$\vec{v}$$ as a combination of basis vectors.

$$
\vec{w}=f(\vec{v}) =f(v_1\vec{\beta}_1+\dots+v_n\vec{\beta}_n) =v_1\cdot f(\vec{\beta}_1)+\dots+v_n\cdot f(\vec{\beta}_n)
$$

For linear independence of $$D$$, if

$$
\vec{0}_W =c_1f(\vec{\beta}_1)+\dots+c_nf(\vec{\beta}_n) =f(c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n)
$$

then, since $$f$$ is one-to-one and so the only vector sent to $$\vec{0}_W$$ is $$\vec{0}_V$$, we have that $$\vec{0}_V=c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n$$, implying that all of the $$c$$'s are zero.

**Lemma 2.4**  —

If spaces have the same dimension then they are isomorphic.

**Proof**  —

To show that any two spaces of dimension $$n$$ are isomorphic, we can simply show that any one is isomorphic to $$\mathbb{R}^n$$. Then we will have shown that they are isomorphic to each other, by the transitivity of isomorphism (which was established in Theorem 2.1).

Let $$V$$ be $$n$$-dimensional. Fix a basis $$B=\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ for the domain $$V$$. Consider the representation of the members of that domain with respect to the basis as a function from $$V$$ to $$\mathbb{R}^n$$

$$
\vec{v}=v_1\vec{\beta}_1+\dots+v_n\vec{\beta}_n \,\stackrel{\text{Rep}_B}{\longmapsto}\,\begin{pmatrix} v_1 \\ \vdots \\ v_n \end{pmatrix}
$$

(it is well-defined since every $$\vec{v}$$ has one and only one such representation— see Remark 2.5 below).

This function is one-to-one because if

$$
\text{Rep}_B(u_1\vec{\beta}_1+\dots+u_n\vec{\beta}_n) =\text{Rep}_B(v_1\vec{\beta}_1+\dots+v_n\vec{\beta}_n)
$$

then

$$
\begin{pmatrix} u_1 \\ \vdots \\ u_n \end{pmatrix} = \begin{pmatrix} v_1 \\ \vdots \\ v_n \end{pmatrix}
$$

and so $$u_1=v_1$$, ..., $$u_n=v_n$$, and therefore the original arguments $$u_1\vec{\beta}_1+\dots+u_n\vec{\beta}_n$$ and $$v_1\vec{\beta}_1+\dots+v_n\vec{\beta}_n$$ are equal.

This function is onto; any $$n$$-tall vector

$$
\vec{w}=\begin{pmatrix} w_1 \\ \vdots \\ w_n \end{pmatrix}
$$

is the image of some $$\vec{v}\in V$$, namely $$\vec{w}={\rm Rep}_{B}(w_1\vec{\beta}_1+\dots+w_n\vec{\beta}_n)$$.

Finally, this function preserves structure.

$$
\begin{array}{rl} {\rm Rep}_{B}(r\cdot\vec{u}+s\cdot\vec{v}) &={\rm Rep}_{B}(\,(ru_1+sv_1)\vec{\beta}_1+\dots+(ru_n+sv_n)\vec{\beta}_n\,) \\ &=\begin{pmatrix} ru_1+sv_1 \\ \vdots \\ ru_n+sv_n \end{pmatrix} \\ &=r\cdot\begin{pmatrix} u_1 \\ \vdots \\ u_n \end{pmatrix}+s\cdot\begin{pmatrix} v_1 \\ \vdots \\ v_n \end{pmatrix} \\ &=r\cdot{\rm Rep}_{B}(\vec{u})+s\cdot{\rm Rep}_{B}(\vec{v}) \end{array}
$$

Thus the $$\text{Rep}_B$$ function is an isomorphism and thus any $$n$$-dimensional space is isomorphic to the $$n$$-dimensional space $$\mathbb{R}^n$$. Consequently, any two spaces with the same dimension are isomorphic.

**Remark 2.5**  —

The parenthetical comment in that proof about the role played by the "one and only one representation" result requires some explanation. We need to show that (for a fixed $$B$$) each vector in the domain is associated by $$\text{Rep}_B$$ with one and only one vector in the codomain.

A contrasting example, where an association doesn't have this property, is illuminating. Consider this subset of $$\mathcal{P}_2$$, which is not a basis.

$$
A=\{1+0x+0x^2, 0+1x+0x^2, 0+0x+1x^2, 1+1x+2x^2\}
$$

Call those four polynomials $$\vec{\alpha}_1$$, ..., $$\vec{\alpha}_4$$. If, mimicing above proof, we try to write the members of $$\mathcal{P}_2$$ as $$\vec{p}=c_1\vec{\alpha}_1+c_2\vec{\alpha}_2+ c_3\vec{\alpha}_3+c_4\vec{\alpha}_4$$, and associate $$\vec{p}$$ with the four-tall vector with components $$c_1$$, ..., $$c_4$$ then there is a problem. For, consider $$\vec{p}(x)=1+x+x^2$$. The set $$A$$ spans the space $$\mathcal{P}_2$$, so there is at least one four-tall vector associated with $$\vec{p}$$. But $$A$$ is not linearly independent and so vectors do not have unique decompositions. In this case, both

$$
\vec{p}(x)=1\vec{\alpha}_1+1\vec{\alpha}_2+1\vec{\alpha}_3+0\vec{\alpha}_4 \quad\text{and}\quad \vec{p}(x)=0\vec{\alpha}_1+0\vec{\alpha}_2- 1\vec{\alpha}_3+1\vec{\alpha}_4
$$

and so there is more than one four-tall vector associated with $$\vec{p}$$.

$$
\begin{pmatrix} 1 \\ 1 \\ 1 \\ 0 \end{pmatrix} \quad\text{and}\quad \begin{pmatrix} 0 \\ 0 \\ -1 \\ 1 \end{pmatrix}
$$

That is, with input $$\vec{p}$$ this association does not have a well-defined (i.e., single) output value.

Any map whose definition appears possibly ambiguous must be checked to see that it is well-defined. For $$\text{Rep}_B$$ in the above proof that check is Problem 11.

That ends the proof of Theorem 2.2. We say that the isomorphism classes are **characterized** by dimension because we can describe each class simply by giving the number that is the dimension of all of the spaces in that class.

This subsection's results give us a collection of representatives of the isomorphism classes.

**Corollary 2.6**  —

A finite-dimensional vector space is isomorphic to one and only one of the $$\mathbb{R}^n$$.

The proofs above pack many ideas into a small space. Through the rest of this chapter we'll consider these ideas again, and fill them out. For a taste of this, we will expand here on the proof of Lemma 2.4.

**Example 2.7**  —

The space $$\mathcal{M}_{2 \! \times \! 2}$$ of $$2 \! \times \! 2$$ matrices is isomorphic to $$\mathbb{R}^4$$. With this basis for the domain

$$
B=\langle \begin{pmatrix} 1 &0 \\ 0 &0 \end{pmatrix}, \begin{pmatrix} 0 &1 \\ 0 &0 \end{pmatrix}, \begin{pmatrix} 0 &0 \\ 1 &0 \end{pmatrix}, \begin{pmatrix} 0 &0 \\ 0 &1 \end{pmatrix} \rangle
$$

the isomorphism given in the lemma, the representation map $$f_1=\text{Rep}_B$$, simply carries the entries over.

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \stackrel{f_1}{\longmapsto} \begin{pmatrix} a \\ b \\ c \\ d \end{pmatrix}
$$

One way to think of the map $$f_1$$ is: fix the basis $$B$$ for the domain and the basis $$\mathcal{E}_4$$ for the codomain, and associate $$\vec{\beta}_1$$ with $$\vec{e}_1$$, and $$\vec{\beta}_2$$ with $$\vec{e}_2$$, etc. Then extend this association to all of the members of two spaces.

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} =a\vec{\beta}_1+b\vec{\beta}_2+c\vec{\beta}_3+d\vec{\beta}_4 \;\;\stackrel{f_1}{\longmapsto}\;\; a\vec{e}_1+b\vec{e}_2+c\vec{e}_3+d\vec{e}_4 =\begin{pmatrix} a \\ b \\ c \\ d \end{pmatrix}
$$

We say that the map has been **extended linearly** from the bases to the spaces.

We can do the same thing with different bases, for instance, taking this basis for the domain.

$$
A=\langle \begin{pmatrix} 2 &0 \\ 0 &0 \end{pmatrix}, \begin{pmatrix} 0 &2 \\ 0 &0 \end{pmatrix}, \begin{pmatrix} 0 &0 \\ 2 &0 \end{pmatrix}, \begin{pmatrix} 0 &0 \\ 0 &2 \end{pmatrix} \rangle
$$

Associating corresponding members of $$A$$ and $$\mathcal{E}_4$$ and extending linearly

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} =(a/2)\vec{\alpha}_1+(b/2)\vec{\alpha}_2 +(c/2)\vec{\alpha}_3+(d/2)\vec{\alpha}_4
$$

$$
\stackrel{f_2}{\longmapsto}\;\; (a/2)\vec{e}_1+(b/2)\vec{e}_2+(c/2)\vec{e}_3+(d/2)\vec{e}_4 =\begin{pmatrix} a/2 \\ b/2 \\ c/2 \\ d/2 \end{pmatrix}
$$

gives rise to an isomorphism that is different than $$f_1$$.

The prior map arose by changing the basis for the domain. We can also change the basis for the codomain. Starting with

$$
B \quad\text{and}\quad D=\langle \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} \rangle
$$

associating $$\vec{\beta}_1$$ with $$\vec{\delta}_1$$, etc., and then linearly extending that correspondence to all of the two spaces

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} =a\vec{\beta}_1+b\vec{\beta}_2+c\vec{\beta}_3+d\vec{\beta}_4 \;\;\stackrel{f_3}{\longmapsto}\;\; a\vec{\delta}_1+b\vec{\delta}_2+c\vec{\delta}_3+d\vec{\delta}_4 =\begin{pmatrix} a \\ b \\ d \\ c \end{pmatrix}
$$

gives still another isomorphism.

So there is a connection between the maps between spaces and bases for those spaces. Later sections will explore that connection.

We will close this section with a summary.

Recall that in the first chapter we defined two matrices as row equivalent if they can be derived from each other by elementary row operations (this was the meaning of same-ness that was of interest there). We showed that is an equivalence relation and so the collection of matrices is partitioned into classes, where all the matrices that are row equivalent fall together into a single class. Then, for insight into which matrices are in each class, we gave representatives for the classes, the reduced echelon form matrices.

In this section, except that the appropriate notion of same-ness here is vector space isomorphism, we have followed much the same outline. First we defined isomorphism, saw some examples, and established some properties. Then we showed that it is an equivalence relation, and now we have a set of class representatives, the real vector spaces $$\mathbb{R}^1$$, $$\mathbb{R}^2$$, etc.

All finite dimensional

vector spaces:

One representative

per class

As before, the list of representatives helps us to understand the partition. It is simply a classification of spaces by dimension.

In the second chapter, with the definition of vector spaces, we seemed to have opened up our studies to many examples of new structures besides the familiar $$\mathbb{R}^n$$'s. We now know that isn't the case. Any finite-dimensional vector space is actually "the same" as a real space. We are thus considering exactly the structures that we need to consider.

The rest of the chapter fills out the work in this section. In particular, in the next section we will consider maps that preserve structure, but are not necessarily correspondences.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Decide if the spaces are isomorphic.

1. $$\mathbb{R}^2$$, $$\mathbb{R}^4$$
2. $$\mathcal{P}_5$$, $$\mathbb{R}^5$$
3. $$\mathcal{M}_{2 \! \times \! 3}$$, $$\mathbb{R}^6$$
4. $$\mathcal{P}_5$$, $$\mathcal{M}_{2 \! \times \! 3}$$
5. $$\mathcal{M}_{2 \! \times \! k}$$, $$\mathbb{C}^k$$

**Answer**  —

Each pair of spaces is isomorphic if and only if the two have the same dimension. We can, when there is an isomorphism, state a map, but it isn't strictly necessary.

1. No, they have different dimensions.
2. No, they have different dimensions.
3. Yes, they have the same dimension. One isomorphism is this.

$$
\begin{pmatrix} a &b &c \\ d &e &f \end{pmatrix} \mapsto \begin{pmatrix} a \\ \vdots \\ f \end{pmatrix}
$$

4. Yes, they have the same dimension. This is an isomorphism.

$$
a+bx+\cdots+fx^5 \mapsto \begin{pmatrix} a &b &c \\ d &e &f \end{pmatrix}
$$

5. Yes, both have dimension $$2k$$.  
*This exercise is recommended for all readers.*

**Problem 2**  —

Consider the isomorphism $${\rm Rep}_{B}(\cdot):\mathcal{P}_1\to \mathbb{R}^2$$ where $$B=\langle 1,1+x \rangle$$. Find the image of each of these elements of the domain.

1. $$3-2x$$;
2. $$2+2x$$;
3. $$x$$

**Answer**  —

1. $${\rm Rep}_{B}(3-2x)=\begin{pmatrix} 5 \\ -2 \end{pmatrix}$$
2. $$\begin{pmatrix} 0 \\ 2 \end{pmatrix}$$
3. $$\begin{pmatrix} -1 \\ 1 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

Show that if $$m\neq n$$ then $$\mathbb{R}^m\not\cong\mathbb{R}^n$$.

**Answer**  —

They have different dimensions.  
*This exercise is recommended for all readers.*

**Problem 4**  —

Is $$\mathcal{M}_{m \! \times \! n}\cong\mathcal{M}_{n \! \times \! m}$$?

**Answer**  —

Yes, both are $$mn$$-dimensional.  
*This exercise is recommended for all readers.*

**Problem 5**  —

Are any two planes through the origin in $$\mathbb{R}^3$$ isomorphic?

**Answer**  —

Yes, any two (nondegenerate) planes are both two-dimensional vector spaces.

**Problem 6**  —

Find a set of equivalence class representatives other than the set of $$\mathbb{R}^n$$'s.

**Answer**  —

There are many answers, one is the set of $$\mathcal{P}_k$$ (taking $$\mathcal{P}_{-1}$$ to be the trivial vector space).

**Problem 7**  —

True or false: between any $$n$$-dimensional space and $$\mathbb{R}^n$$ there is exactly one isomorphism.

**Answer**  —

False (except when $$n=0$$). For instance, if $$f:V\to \mathbb{R}^n$$ is an isomorphism then multiplying by any nonzero scalar, gives another, different, isomorphism. (Between trivial spaces the isomorphisms are unique; the only map possible is $$\vec{0}_V\mapsto 0_W$$.)

**Problem 8**  —

Can a vector space be isomorphic to one of its (proper) subspaces?

**Answer**  —

No. A proper subspace has a strictly lower dimension than it's superspace; if $$U$$ is a proper subspace of $$V$$ then any linearly independent subset of $$U$$ must have fewer than $$\dim(V)$$ members or else that set would be a basis for $$V$$, and $$U$$ wouldn't be proper.  
*This exercise is recommended for all readers.*

**Problem 9**  —

This subsection shows that for any isomorphism, the inverse map is also an isomorphism. This subsection also shows that for a fixed basis $$B$$ of an $$n$$-dimensional vector space $$V$$, the map $$\text{Rep}_B:V\to \mathbb{R}^n$$ is an isomorphism. Find the inverse of this map.

**Answer**  —

Where $$B=\langle \vec{\beta}_1,\ldots,\vec{\beta}_n \rangle$$, the inverse is this.

$$
\begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix} \mapsto c_1\vec{\beta}_1+\cdots+c_n\vec{\beta}_n
$$

*This exercise is recommended for all readers.*

**Problem 10**  —

Prove these facts about matrices.

1. The row space of a matrix is isomorphic to the column space of its transpose.
2. The row space of a matrix is isomorphic to its column space.

**Answer**  —

All three spaces have dimension equal to the rank of the matrix.

**Problem 11**  —

Show that the function from Theorem 2.2 is well-defined.

**Answer**  —

We must show that if $$\vec{a}=\vec{b}$$ then $$f(\vec{a})=f(\vec{b})$$. So suppose that $$a_1\vec{\beta}_1+\dots+a_n\vec{\beta}_n =b_1\vec{\beta}_1+\dots+b_n\vec{\beta}_n$$. Each vector in a vector space (here, the domain space) has a unique representation as a linear combination of basis vectors, so we can conclude that $$a_1=b_1$$, ..., $$a_n=b_n$$. Thus,

$$
f(\vec{a}) =\begin{pmatrix} a_1 \\ \vdots \\ a_n \end{pmatrix}=\begin{pmatrix} b_1 \\ \vdots \\ b_n \end{pmatrix} =f(\vec{b})
$$

and so the function is well-defined.

**Problem 12**  —

Is the proof of Theorem 2.2 valid when $$n=0$$?

**Answer**  —

Yes, because a zero-dimensional space is a trivial space.

**Problem 13**  —

For each, decide if it is a set of isomorphism class representatives.

1. $$\{\mathbb{C}^k \,\big|\, k\in\mathbb{N}\}$$
2. $$\{\mathcal{P}_k\,\big|\, k\in \{-1,0,1,\ldots\}\}$$
3. $$\{\mathcal{M}_{m \! \times \! n}\,\big|\, m,n\in\mathbb{N}\}$$

**Answer**  —

1. No, this collection has no spaces of odd dimension.
2. Yes, because $$\mathcal{P}_{k}\cong\mathbb{R}^{k+1}$$.
3. No, for instance, $$\mathcal{M}_{2 \! \times \! 3}\cong\mathcal{M}_{3 \! \times \! 2}$$.

**Problem 14**  —

Let $$f$$ be a correspondence between vector spaces $$V$$ and $$W$$ (that is, a map that is one-to-one and onto). Show that the spaces $$V$$ and $$W$$ are isomorphic via $$f$$ if and only if there are bases $$B\subset V$$ and $$D\subset W$$ such that corresponding vectors have the same coordinates: $${\rm Rep}_{B}(\vec{v})={\rm Rep}_{D}(f(\vec{v}))$$.

**Answer**  —

One direction is easy: if the two are isomorphic via $$f$$ then for any basis $$B\subseteq V$$, the set $$D=f(B)$$ is also a basis (this is shown in Lemma 2.3). The check that corresponding vectors have the same coordinates: $$f(c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n) =c_1f(\vec{\beta}_1)+\dots+c_nf(\vec{\beta}_n) =c_1\vec{\delta}_1+\dots+c_n\vec{\delta}_n$$ is routine.

For the other half, assume that there are bases such that corresponding vectors have the same coordinates with respect to those bases. Because $$f$$ is a correspondence, to show that it is an isomorphism, we need only show that it preserves structure. Because $${\rm Rep}_{B}(\vec{v}\,)={\rm Rep}_{D}(f(\vec{v}\,))$$, the map $$f$$ preserves structure if and only if representations preserve addition: $${\rm Rep}_{B}(\vec{v}_1+\vec{v}_2)={\rm Rep}_{B}(\vec{v}_1)+{\rm Rep}_{B}(\vec{v}_2)$$ and scalar multiplication: $${\rm Rep}_{B}(r\cdot\vec{v}\,)=r\cdot{\rm Rep}_{B}(\vec{v}\,)$$ The addition calculation is this: $$(c_1+d_1)\vec{\beta}_1+\dots+(c_n+d_n)\vec{\beta}_n =c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n +d_1\vec{\beta}_1+\dots+d_n\vec{\beta}_n$$, and the scalar multiplication calculation is similar.

**Problem 15**  —

Consider the isomorphism $$\text{Rep}_B:\mathcal{P}_3\to \mathbb{R}^4$$.

1. Vectors in a real space are orthogonal if and only if their dot product is zero. Give a definition of orthogonality for polynomials.
2. The derivative of a member of $$\mathcal{P}_3$$ is in $$\mathcal{P}_3$$. Give a definition of the derivative of a vector in $$\mathbb{R}^4$$.

**Answer**  —

1. Pulling the definition back from $$\mathbb{R}^4$$ to $$\mathcal{P}_3$$ gives that $$a_0+a_1x+a_2x^2+a_3x^3$$ is orthogonal to $$b_0+b_1x+b_2x^2+b_3x^3$$ if and only if $$a_0b_0+a_1b_1+a_2b_2+a_3b_3=0$$.
2. A natural definition is this.

$$
D(\begin{pmatrix} a_0 \\ a_1 \\ a_2 \\ a_3 \end{pmatrix})= \begin{pmatrix} a_1 \\ 2a_2 \\ 3a_3 \\ 0 \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 16**  —

Does every correspondence between bases, when extended to the spaces, give an isomorphism?

**Answer**  —

Yes.

Assume that $$V$$ is a vector space with basis $$B=\langle \vec{\beta}_1,\ldots,\vec{\beta}_n \rangle$$ and that $$W$$ is another vector space such that the map $$f:B\to W$$ is a correspondence. Consider the extension $$\hat{f}:V\to W$$ of $$f$$.

$$
\hat{f}(c_1\vec{\beta}_1+\cdots+c_n\vec{\beta}_n)= c_1f(\vec{\beta}_1)+\cdots+c_nf(\vec{\beta}_n).
$$

The map $$\hat{f}$$ is an isomorphism.

First, $$\hat{f}$$ is well-defined because every member of $$V$$ has one and only one representation as a linear combination of elements of $$B$$.

Second, $$\hat{f}$$ is one-to-one because every member of $$W$$ has only one representation as a linear combination of elements of $$\langle f(\vec{\beta}_1),\dots,f(\vec{\beta}_n) \rangle$$. That map $$\hat{f}$$ is onto because every member of $$W$$ has at least one representation as a linear combination of members of $$\langle f(\vec{\beta}_1),\dots,f(\vec{\beta}_n) \rangle$$.

Finally, preservation of structure is routine to check. For instance, here is the preservation of addition calculation.

$$
\begin{array}{rl} \hat{f}(\,(c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n)+ (d_1\vec{\beta}_1+\dots+d_n\vec{\beta}_n)\,) &=\hat{f}(\,(c_1+d_1)\vec{\beta}_1+\dots+(c_n+d_n)\vec{\beta}_n\,) \\ &=(c_1+d_1)f(\vec{\beta}_1)+\dots+(c_n+d_n)f(\vec{\beta}_n) \\ &=c_1f(\vec{\beta}_1)+\dots+c_nf(\vec{\beta}_n) +d_1f(\vec{\beta}_1)+\dots+d_nf(\vec{\beta}_n) \\ &=\hat{f}(c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n)+ +\hat{f}(d_1\vec{\beta}_1+\dots+d_n\vec{\beta}_n). \end{array}
$$

Preservation of scalar multiplication is similar.

**Problem 17**  —

*(Requires the subsection on Combining Subspaces, which is optional.)* Suppose that $$V=V_1\oplus V_2$$ and that $$V$$ is isomorphic to the space $$U$$ under the map $$f$$. Show that $$U=f(V_1)\oplus f(U_2)$$.

**Answer**  —

Because $$V_1\cap V_2=\{\vec{0}_V\}$$ and $$f$$ is one-to-one we have that $$f(V_1)\cap f(V_2)=\{\vec{0}_U\}$$. To finish, count the dimensions: $$\dim(U)=\dim(V)=\dim(V_1)+\dim(V_2)=\dim(f(V_1))+\dim(f(V_2))$$, as required.

**Problem 18**  — Show that this is not a well-defined function from the rational numbers to the integers: with each fraction, associate the value of its numerator.

**Answer**  —

Rational numbers have many representations, e.g., $$1/2=3/6$$, and the numerators can vary among representations.

### Footnotes

---

*Source: Wikibooks, Linear Algebra/Dimension Characterizes Isomorphism (https://en.wikibooks.org/wiki/Linear_Algebra/Dimension_Characterizes_Isomorphism), by Wikibooks contributors, CC BY-SA 4.0.*
