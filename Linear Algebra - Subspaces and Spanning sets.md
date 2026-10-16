# Subspaces and Spanning sets

One of the examples that led us to introduce the idea of a vector space was the solution set of a homogeneous system. For instance, we've seen in [Example 1.4](Linear%20Algebra%20-%20Definition%20and%20Examples%20of%20Vector%20Spaces.md) such a space that is a planar subset of $$\mathbb{R}^3$$. There, the vector space $$\mathbb{R}^3$$ contains inside it another vector space, the plane.

**Definition 2.1**  —

For any vector space, a **subspace** is a subset that is itself a vector space, under the inherited operations.

**Example 2.2**  —

The plane from the prior subsection,

$$
P=\{\begin{pmatrix} x \\ y \\ z \end{pmatrix}\,\big|\, x+y+z=0\}
$$

is a subspace of $$\mathbb{R}^3$$. As specified in the definition, the operations are the ones that are inherited from the larger space, that is, vectors add in $$P$$ as they add in $$\mathbb{R}^3$$

$$
\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}+\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} =\begin{pmatrix} x_1+x_2 \\ y_1+y_2 \\ z_1+z_2 \end{pmatrix}
$$

and scalar multiplication is also the same as it is in $$\mathbb{R}^3$$. To show that $$P$$ is a subspace, we need only note that it is a subset and then verify that it is a space. Checking that $$P$$ satisfies the conditions in the definition of a vector space is routine. For instance, for closure under addition, just note that if the summands satisfy that $$x_1+y_1+z_1=0$$ and $$x_2+y_2+z_2=0$$ then the sum satisfies that $$(x_1+x_2)+(y_1+y_2)+(z_1+z_2)=(x_1+y_1+z_1)+(x_2+y_2+z_2)=0$$.

**Example 2.3**  —

The $$x$$-axis in $$\mathbb{R}^2$$ is a subspace where the addition and scalar multiplication operations are the inherited ones.

$$
\begin{pmatrix} x_1 \\ 0 \end{pmatrix} + \begin{pmatrix} x_2 \\ 0 \end{pmatrix} = \begin{pmatrix} x_1+x_2 \\ 0 \end{pmatrix} \qquad r\cdot\begin{pmatrix} x \\ 0 \end{pmatrix} =\begin{pmatrix} rx \\ 0 \end{pmatrix}
$$

As above, to verify that this is a subspace, we simply note that it is a subset and then check that it satisfies the conditions in definition of a vector space. For instance, the two closure conditions are satisfied: (1) adding two vectors with a second component of zero results in a vector with a second component of zero, and (2) multiplying a scalar times a vector with a second component of zero results in a vector with a second component of zero.

**Example 2.4**  —

Another subspace of $$\mathbb{R}^2$$ is

$$
\{\begin{pmatrix} 0 \\ 0 \end{pmatrix}\}
$$

its trivial subspace.

Any vector space has a trivial subspace $$\{\vec{0}\,\}$$. At the opposite extreme, any vector space has itself for a subspace. These two are the **improper** subspaces. Other subspaces are **proper**.

**Example 2.5**  —

The condition in the definition requiring that the addition and scalar multiplication operations must be the ones inherited from the larger space is important. Consider the subset $$\{1\}$$ of the vector space $$\mathbb{R}^1$$. Under the operations $$1+1=1$$ and $$r\cdot 1=1$$ that set is a vector space, specifically, a trivial space. But it is not a subspace of $$\mathbb{R}^1$$ because those aren't the inherited operations, since of course $$\mathbb{R}^1$$ has $$1+1=2$$.

**Example 2.6**  —

All kinds of vector spaces, not just $$\mathbb{R}^n$$'s, have subspaces. The vector space of cubic polynomials $$\{a+bx+cx^2+dx^3\,\big|\, a,b,c,d\in\mathbb{R}\}$$ has a subspace comprised of all linear polynomials $$\{m+nx\,\big|\, m,n\in\mathbb{R}\}$$.

**Example 2.7**  —

Another example of a subspace not taken from an $$\mathbb{R}^n$$ is one from the examples following the definition of a vector space. The space of all real-valued functions of one real variable $$f:\mathbb{R}\to \mathbb{R}$$ has a subspace of functions satisfying the restriction $$(d^2\,f/dx^2)+f=0$$.

**Example 2.8**  —

Being vector spaces themselves, subspaces must satisfy the closure conditions. The set $$\mathbb{R}^+$$ is not a subspace of the vector space $$\mathbb{R}^1$$ because with the inherited operations it is not closed under scalar multiplication: if $$\vec{v}=1$$ then $$-1\cdot\vec{v}\not\in\mathbb{R}^+$$.

The next result says that Example 2.8 is prototypical. The only way that a subset can fail to be a subspace (if it is nonempty and the inherited operations are used) is if it isn't closed.

**Lemma 2.9**  —

For a nonempty subset $$S$$ of a vector space, under the inherited operations, the following are equivalent statements.

1. $$S$$ is a subspace of that vector space
2. $$S$$ is closed under linear combinations of pairs of vectors: for any vectors $$\vec{s}_1,\vec{s}_2\in S$$ and scalars $$r_1,r_2$$ the vector $$r_1\vec{s}_1+r_2\vec{s}_2$$ is in $$S$$
3. $$S$$ is closed under linear combinations of any number of vectors: for any vectors $$\vec{s}_1,\ldots,\vec{s}_n\in S$$ and scalars $$r_1, \ldots,r_n$$ the vector $$r_1\vec{s}_1+\cdots+r_n\vec{s}_n$$ is in $$S$$.

Briefly, the way that a subset gets to be a subspace is by being closed under linear combinations.

**Proof**  —

"The following are equivalent" means that each pair of statements are equivalent.

$$
(1)\!\iff\!(2) \qquad (2)\!\iff\!(3) \qquad (3)\!\iff\!(1)
$$

We will show this equivalence by establishing that $$(1)\implies (3)\implies (2)\implies (1)$$. This strategy is suggested by noticing that $$(1)\implies (3)$$ and $$(3)\implies (2)$$ are easy and so we need only argue the single implication $$(2)\implies (1)$$.

For that argument, assume that $$S$$ is a nonempty subset of a vector space $$V$$ and that $$S$$ is closed under combinations of pairs of vectors. We will show that $$S$$ is a vector space by checking the conditions.

The first item in the vector space definition has five conditions. First, for closure under addition, if $$\vec{s}_1,\vec{s}_2\in S$$ then $$\vec{s}_1+\vec{s}_2\in S$$, as $$\vec{s}_1+\vec{s}_2=1\cdot\vec{s}_1+1\cdot\vec{s}_2$$. Second, for any $$\vec{s}_1,\vec{s}_2\in S$$, because addition is inherited from $$V$$, the sum $$\vec{s}_1+\vec{s}_2$$ in $$S$$ equals the sum $$\vec{s}_1+\vec{s}_2$$ in $$V$$, and that equals the sum $$\vec{s}_2+\vec{s}_1$$ in $$V$$ (because $$V$$ is a vector space, its addition is commutative), and that in turn equals the sum $$\vec{s}_2+\vec{s}_1$$ in $$S$$. The argument for the third condition is similar to that for the second. For the fourth, consider the zero vector of $$V$$ and note that closure of $$S$$ under linear combinations of pairs of vectors gives that (where $$\vec{s}$$ is any member of the nonempty set $$S$$) $$0\cdot\vec{s}+0\cdot\vec{s}=\vec{0}$$ is in $$S$$; showing that $$\vec{0}$$ acts under the inherited operations as the additive identity of $$S$$ is easy. The fifth condition is satisfied because for any $$\vec{s}\in S$$, closure under linear combinations shows that the vector $$0\cdot\vec{0}+(-1)\cdot\vec{s}$$ is in $$S$$; showing that it is the additive inverse of $$\vec{s}$$ under the inherited operations is routine.

The checks for item 2 are similar and are saved for Problem 13.

We usually show that a subset is a subspace with $$(2)\implies (1)$$.

**Remark 2.10**  —

At the start of this chapter we introduced vector spaces as collections in which linear combinations are "sensible". The above result speaks to this.

The vector space definition has ten conditions but eight of them— the conditions not about closure— simply ensure that referring to the operations as an "addition" and a "scalar multiplication" is sensible. The proof above checks that these eight are inherited from the surrounding vector space provided that the nonempty set $$S$$ satisfies Lemma 2.9's statement (2) (e.g., commutativity of addition in $$S$$ follows right from commutativity of addition in $$V$$). So, in this context, this meaning of "sensible" is automatically satisfied.

In assuring us that this first meaning of the word is met, the result draws our attention to the second meaning of "sensible". It has to do with the two remaining conditions, the closure conditions. Above, the two separate closure conditions inherent in statement (1) are combined in statement (2) into the single condition of closure under all linear combinations of two vectors, which is then extended in statement (3) to closure under combinations of any number of vectors. The latter two statements say that we can always make sense of an expression like $$r_1\vec{s}_1+r_2\vec{s}_2$$, without restrictions on the $$r$$'s— such expressions are "sensible" in that the vector described is defined and is in the set $$S$$.

This second meaning suggests that a good way to think of a vector space is as a collection of unrestricted linear combinations. The next two examples take some spaces and describe them in this way. That is, in these examples we parametrize, just as we did in Chapter One to describe the solution set of a homogeneous linear system.

**Example 2.11**  —

This subset of $$\mathbb{R}^3$$

$$
S=\{\begin{pmatrix} x \\ y \\ z \end{pmatrix}\,\big|\, x-2y+z=0\}
$$

is a subspace under the usual addition and scalar multiplication operations of column vectors (the check that it is nonempty and closed under linear combinations of two vectors is just like the one in Example 2.2). To parametrize, we can take $$x-2y+z=0$$ to be a one-equation linear system and expressing the leading variable in terms of the free variables $$x=2y-z$$.

$$
S =\{\begin{pmatrix} 2y-z \\ y \\ z \end{pmatrix}\,\big|\, y,z\in\mathbb{R}\} =\{y\begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}+z\begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}\,\big|\, y,z\in\mathbb{R}\}
$$

Now the subspace is described as the collection of unrestricted linear combinations of those two vectors. Of course, in either description, this is a plane through the origin.

**Example 2.12**  —

This is a subspace of the $$2 \! \times \! 2$$ matrices

$$
L=\{\begin{pmatrix} a &0 \\ b &c \end{pmatrix} \,\big|\, a+b+c=0\}
$$

(checking that it is nonempty and closed under linear combinations is easy). To parametrize, express the condition as $$a=-b-c$$.

$$
L =\{\begin{pmatrix} -b-c &0 \\ b &c \end{pmatrix} \,\big|\, b,c\in\mathbb{R}\} =\{b\begin{pmatrix} -1 &0 \\ 1 &0 \end{pmatrix} +c\begin{pmatrix} -1 &0 \\ 0 &1 \end{pmatrix} \,\big|\, b,c\in\mathbb{R}\}
$$

As above, we've described the subspace as a collection of unrestricted linear combinations (by coincidence, also of two elements).

Parametrization is an easy technique, but it is important. We shall use it often.

**Definition 2.13**  —

The **span**(or **linear closure**) of a nonempty subset $$S$$ of a vector space is the set of all linear combinations of vectors from $$S$$.

$$
[S] =\{ c_1\vec{s}_1+\cdots+c_n\vec{s}_n \,\big|\, c_1,\ldots, c_n\in\mathbb{R} \text{ and } \vec{s}_1,\ldots,\vec{s}_n\in S \}
$$

The span of the empty subset of a vector space is the trivial subspace.

No notation for the span is completely standard. The square brackets used here are common, but so are "$$\text{span}(S)$$" and "$$\text{sp}(S)$$".

**Remark 2.14**  —

In Chapter One, after we showed that the solution set of a homogeneous linear system can be written as $$\{c_1\vec{\beta}_1+\cdots+c_k\vec{\beta}_k\,\big|\, c_1,\ldots,c_k\in\mathbb{R}\}$$, we described that as the set "generated" by the $${\vec{\beta}}$$'s. We now have the technical term; we call that the "span" of the set $$\{\vec{\beta}_1,\ldots,\vec{\beta}_k\}$$.

Recall also the discussion of the "tricky point" in that proof. The span of the empty set is defined to be the set $$\{\vec{0}\}$$ because we follow the convention that a linear combination of no vectors sums to $$\vec{0}$$. Besides, defining the empty set's span to be the trivial subspace is a convenience in that it keeps results like the next one from having annoying exceptional cases.

**Lemma 2.15**  —

In a vector space, the span of any subset is a subspace.

**Proof**  —

Call the subset $$S$$. If $$S$$ is empty then by definition its span is the trivial subspace. If $$S$$ is not empty then by Lemma 2.9 we need only check that the span $$[S]$$ is closed under linear combinations. For a pair of vectors from that span, $$\vec{v}=c_1\vec{s}_1+\cdots+c_n\vec{s}_n$$ and $$\vec{w}=c_{n+1}\vec{s}_{n+1}+\cdots+c_m\vec{s}_m$$, a linear combination

$$
p\cdot(c_1\vec{s}_1+\cdots+c_n\vec{s}_n)+ r\cdot(c_{n+1}\vec{s}_{n+1}+\cdots+c_m\vec{s}_m)
$$

$$
= pc_1\vec{s}_1+\cdots+pc_n\vec{s}_n +rc_{n+1}\vec{s}_{n+1}+\cdots+rc_m\vec{s}_m
$$

($$p$$, $$r$$ scalars) is a linear combination of elements of $$S$$ and so is in $$[S]$$ (possibly some of the $$\vec{s}_i$$'s forming $$\vec{v}$$ equal some of the $$\vec{s}_j$$'s from $$\vec{w}$$, but it does not matter).

The converse of the lemma holds: any subspace is the span of some set, because a subspace is obviously the span of the set of its members. Thus a subset of a vector space is a subspace if and only if it is a span. This fits the intuition that a good way to think of a vector space is as a collection in which linear combinations are sensible.

Taken together, Lemma 2.9 and Lemma 2.15 show that the span of a subset $$S$$ of a vector space is the smallest subspace containing all the members of $$S$$.

**Example 2.16**  —

In any vector space $$V$$, for any vector $$\vec{v}$$, the set $$\{r\cdot\vec{v} \,\big|\, r\in\mathbb{R}\}$$ is a subspace of $$V$$. For instance, for any vector $$\vec{v}\in\mathbb{R}^3$$, the line through the origin containing that vector, $$\{k\vec{v}\,\big|\, k\in\mathbb{R} \}$$ is a subspace of $$\mathbb{R}^3$$. This is true even when $$\vec{v}$$ is the zero vector, in which case the subspace is the degenerate line, the trivial subspace.

**Example 2.17**  —

The span of this set is all of $$\mathbb{R}^2$$.

$$
\{\begin{pmatrix} 1 \\ 1 \end{pmatrix},\begin{pmatrix} 1 \\ -1 \end{pmatrix}\}
$$

To check this we must show that any member of $$\mathbb{R}^2$$ is a linear combination of these two vectors. So we ask: for which vectors (with real components $$x$$ and $$y$$) are there scalars $$c_1$$ and $$c_2$$ such that this holds?

$$
c_1\begin{pmatrix} 1 \\ 1 \end{pmatrix}+c_2\begin{pmatrix} 1 \\ -1 \end{pmatrix}=\begin{pmatrix} x \\ y \end{pmatrix}
$$

Gauss' method

$$
\begin{array}{rcl} \begin{array}{rcrcr} c_1 &+ &c_2 &= &x \\ c_1 &- &c_2 &= &y \end{array} &\xrightarrow[]{-\rho_1+\rho_2} &\begin{array}{rcrcr} c_1 &+ &c_2 &= &x \\ & &-2c_2 &= &-x+y \end{array} \end{array}
$$

with back substitution gives $$c_2=(x-y)/2$$ and $$c_1=(x+y)/2$$. These two equations show that for any $$x$$ and $$y$$ that we start with, there are appropriate coefficients $$c_1$$ and $$c_2$$ making the above vector equation true. For instance, for $$x=1$$ and $$y=2$$ the coefficients $$c_2=-1/2$$ and $$c_1=3/2$$ will do. That is, any vector in $$\mathbb{R}^2$$ can be written as a linear combination of the two given vectors.

Since spans are subspaces, and we know that a good way to understand a subspace is to parametrize its description, we can try to understand a set's span in that way.

**Example 2.18**  —

Consider, in $$\mathcal{P}_2$$, the span of the set $$\{3x-x^2, 2x\}$$. By the definition of span, it is the set of unrestricted linear combinations of the two $$\{c_1(3x-x^2)+c_2(2x)\,\big|\, c_1,c_2\in\mathbb{R}\}$$. Clearly polynomials in this span must have a constant term of zero. Is that necessary condition also sufficient?

We are asking: for which members $$a_2x^2+a_1x+a_0$$ of $$\mathcal{P}_2$$ are there $$c_1$$ and $$c_2$$ such that $$a_2x^2+a_1x+a_0=c_1(3x-x^2)+c_2(2x)$$? Since polynomials are equal if and only if their coefficients are equal, we are looking for conditions on $$a_2$$, $$a_1$$, and $$a_0$$ satisfying these.

$$
\begin{array}{rcrcr} -c_1 & & &= &a_2 \\ 3c_1 &+ &2c_2 &= &a_1 \\ & &0 &= &a_0 \end{array}
$$

Gauss' method gives that $$c_1=-a_2$$, $$c_2=(3/2)a_2+(1/2)a_1$$, and $$0=a_0$$. Thus the only condition on polynomials in the span is the condition that we knew of— as long as $$a_0=0$$, we can give appropriate coefficients $$c_1$$ and $$c_2$$ to describe the polynomial $$a_0+a_1x+a_2x^2$$ as in the span. For instance, for the polynomial $$0-4x+3x^2$$, the coefficients $$c_1=-3$$ and $$c_2=5/2$$ will do. So the span of the given set is $$\{a_1x+a_2x^2\,\big|\, a_1,a_2\in\mathbb{R}\}$$.

This shows, incidentally, that the set $$\{x,x^2\}$$ also spans this subspace. A space can have more than one spanning set. Two other sets spanning this subspace are $$\{x,x^2,-x+2x^2\}$$ and $$\{x,x+x^2,x+2x^2,\ldots\,\}$$. (Naturally, we usually prefer to work with spanning sets that have only a few members.)

**Example 2.19**  —

These are the subspaces of $$\mathbb{R}^3$$ that we now know of, the trivial subspace, the lines through the origin, the planes through the origin, and the whole space (of course, the picture shows only a few of the infinitely many subspaces). In the next section we will prove that $$\mathbb{R}^3$$ has no other type of subspaces, so in fact this picture shows them all.

The subsets are described as spans of sets, using a minimal number of members, and are shown connected to their supersets. Note that these subspaces fall naturally into levels— planes on one level, lines on another, etc.— according to how many vectors are in a minimal-sized spanning set.

So far in this chapter we have seen that to study the properties of linear combinations, the right setting is a collection that is closed under these combinations. In the first subsection we introduced such collections, vector spaces, and we saw a great variety of examples. In this subsection we saw still more spaces, ones that happen to be subspaces of others. In all of the variety we've seen a commonality. Example 2.19 above brings it out: vector spaces and subspaces are best understood as a span, and especially as a span of a small number of vectors. The next section studies spanning sets that are minimal.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Which of these subsets of the vector space of $$2 \! \times \! 2$$ matrices are subspaces under the inherited operations? For each one that is a subspace, parametrize its description. For each that is not, give a condition that fails.

1. $$\{\begin{pmatrix} a &0 \\ 0 &b \end{pmatrix} \,\big|\, a,b\in\mathbb{R}\}$$
2. $$\{\begin{pmatrix} a &0 \\ 0 &b \end{pmatrix} \,\big|\, a+b=0\}$$
3. $$\{\begin{pmatrix} a &0 \\ 0 &b \end{pmatrix} \,\big|\, a+b=5\}$$
4. $$\{\begin{pmatrix} a &c \\ 0 &b \end{pmatrix} \,\big|\, a+b=0, c\in\mathbb{R}\}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Is this a subspace of $$\mathcal{P}_2$$: $$\{a_0+a_1x+a_2x^2\,\big|\, a_0+2a_1+a_2=4\}$$? If it is then parametrize its description.  
*This exercise is recommended for all readers.*

**Problem 3**  —

Decide if the vector lies in the span of the set, inside of the space.

1. $$\begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}$$, $$\{\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \}$$, in $$\mathbb{R}^3$$
2. $$x-x^3$$, $$\{x^2,2x+x^2,x+x^3\}$$, in $$\mathcal{P}_3$$
3. $$\begin{pmatrix} 0 &1 \\ 4 &2 \end{pmatrix}$$, $$\{\begin{pmatrix} 1 &0 \\ 1 &1 \end{pmatrix}, \begin{pmatrix} 2 &0 \\ 2 &3 \end{pmatrix} \}$$, in $$\mathcal{M}_{2 \! \times \! 2}$$

**Problem 4**  —

Which of these are members of the span $$[\{\cos^2x,\sin^2x\} ]$$ in the vector space of real-valued functions of one real variable?

1. $$f(x)=1$$
2. $$f(x)=3+x^2$$
3. $$f(x)=\sin x$$
4. $$f(x)=\cos (2x)$$  
*This exercise is recommended for all readers.*

**Problem 5**  —

Which of these sets spans $$\mathbb{R}^3$$? That is, which of these sets has the property that any three-tall vector can be expressed as a suitable linear combination of the set's elements?

1. $$\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 3 \end{pmatrix} \}$$
2. $$\{ \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \}$$
3. $$\{ \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 3 \\ 0 \\ 0 \end{pmatrix} \}$$
4. $$\{ \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 3 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 2 \\ 1 \\ 5 \end{pmatrix} \}$$
5. $$\{ \begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 3 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 5 \\ 1 \\ 2 \end{pmatrix}, \begin{pmatrix} 6 \\ 0 \\ 2 \end{pmatrix} \}$$  
*This exercise is recommended for all readers.*

**Problem 6**  —

Parametrize each subspace's description. Then express each subspace as a span.

1. The subset $$\{\begin{pmatrix} a &b &c \end{pmatrix}\,\big|\, a-c=0\}$$ of the three-wide row vectors
2. This subset of $$\mathcal{M}_{2 \! \times \! 2}$$

$$
\{\begin{pmatrix} a &b \\ c &d \end{pmatrix} \,\big|\, a+d=0\}
$$

3. This subset of $$\mathcal{M}_{2 \! \times \! 2}$$

$$
\{\begin{pmatrix} a &b \\ c &d \end{pmatrix} \,\big|\, 2a-c-d=0 \text{ and } a+3b=0 \}
$$

4. The subset $$\{a+bx+cx^3\,\big|\, a-2b+c=0\}$$ of $$\mathcal{P}_3$$
5. The subset of $$\mathcal{P}_2$$ of quadratic polynomials $$p$$ such that $$p(7)=0$$  
*This exercise is recommended for all readers.*

**Problem 7**  —

Find a set to span the given subspace of the given space. (*Hint.* Parametrize each.)

1. the $$xz$$-plane in $$\mathbb{R}^3$$
2. $$\{\begin{pmatrix} x \\ y \\ z \end{pmatrix}\,\big|\, 3x+2y+z=0\}$$ in $$\mathbb{R}^3$$
3. $$\{\begin{pmatrix} x \\ y \\ z \\ w \end{pmatrix}\,\big|\, 2x+y+w=0 \text{ and } y+2z=0\}$$ in $$\mathbb{R}^4$$
4. $$\{a_0+a_1x+a_2x^2+a_3x^3\,\big|\, a_0+a_1=0 \text{ and } a_2-a_3=0\}$$ in $$\mathcal{P}_3$$
5. The set $$\mathcal{P}_4$$ in the space $$\mathcal{P}_4$$
6. $$\mathcal{M}_{2 \! \times \! 2}$$ in $$\mathcal{M}_{2 \! \times \! 2}$$

**Problem 8**  —

Is $$\mathbb{R}^2$$ a subspace of $$\mathbb{R}^3$$?  
*This exercise is recommended for all readers.*

**Problem 9**  —

Decide if each is a subspace of the vector space of real-valued functions of one real variable.

1. The **even** functions $$\{f:\mathbb{R}\to \mathbb{R} \,\big|\, f(-x)=f(x) \text{ for all } x\}$$. For example, two members of this set are $$f_1(x)=x^2$$ and $$f_2(x)=\cos (x)$$.
2. The **odd** functions $$\{f:\mathbb{R}\to \mathbb{R} \,\big|\, f(-x)=-f(x) \text{ for all } x\}$$. Two members are $$f_3(x)=x^3$$ and $$f_4(x)=\sin(x)$$.

**Problem 10**  —

Example 2.16 says that for any vector $$\vec{v}$$ that is an element of a vector space $$V$$, the set $$\{r\cdot\vec{v}\,\big|\, r\in\mathbb{R}\}$$ is a subspace of $$V$$. (This is of course, simply the span of the singleton set $$\{\vec{v}\}$$.) Must any such subspace be a proper subspace, or can it be improper?

**Problem 11**  —

An example following the definition of a vector space shows that the solution set of a homogeneous linear system is a vector space. In the terminology of this subsection, it is a subspace of $$\mathbb{R}^n$$ where the system has $$n$$ variables. What about a non-homogeneous linear system; do its solutions form a subspace (under the inherited operations)?

**Problem 12**  —

Example 2.19 shows that $$\mathbb{R}^3$$ has infinitely many subspaces. Does every nontrivial space have infinitely many subspaces?

**Problem 13**  —

Finish the proof of Lemma 2.9.

**Problem 14**  —

Show that each vector space has only one trivial subspace.  
*This exercise is recommended for all readers.*

**Problem 15**  —

Show that for any subset $$S$$ of a vector space, the span of the span equals the span $$[ [S] ]=[S]$$. (*Hint.* Members of $$[S]$$ are linear combinations of members of $$S$$. Members of $$[[S]]$$ are linear combinations of linear combinations of members of $$S$$.)

**Problem 16**  —

All of the subspaces that we've seen use zero in their description in some way. For example, the subspace in Example 2.3 consists of all the vectors from $$\mathbb{R}^2$$ with a second component of zero. In contrast, the collection of vectors from $$\mathbb{R}^2$$ with a second component of one does not form a subspace (it is not closed under scalar multiplication). Another example is Example 2.2, where the condition on the vectors is that the three components add to zero. If the condition were that the three components add to one then it would not be a subspace (again, it would fail to be closed). This exercise shows that a reliance on zero is not strictly necessary. Consider the set

$$
\{\begin{pmatrix} x \\ y \\ z \end{pmatrix}\,\big|\, x+y+z=1\}
$$

under these operations.

$$
\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}+\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} =\begin{pmatrix} x_1+x_2-1 \\ y_1+y_2 \\ z_1+z_2 \end{pmatrix} \qquad r\begin{pmatrix} x \\ y \\ z \end{pmatrix}=\begin{pmatrix} rx-r+1 \\ ry \\ rz \end{pmatrix}
$$

1. Show that it is not a subspace of $$\mathbb{R}^3$$. (*Hint.* See Example 2.5).
2. Show that it is a vector space. Note that by the prior item, Lemma 2.9 can not apply.
3. Show that any subspace of $$\mathbb{R}^3$$ must pass through the origin, and so any subspace of $$\mathbb{R}^3$$ must involve zero in its description. Does the converse hold? Does any subset of $$\mathbb{R}^3$$ that contains the origin become a subspace when given the inherited operations?

**Problem 17**  —

We can give a justification for the convention that the sum of zero-many vectors equals the zero vector. Consider this sum of three vectors $$\vec{v}_1+\vec{v}_2+\vec{v}_3$$.

1. What is the difference between this sum of three vectors and the sum of the first two of these three?
2. What is the difference between the prior sum and the sum of just the first one vector?
3. What should be the difference between the prior sum of one vector and the sum of no vectors?
4. So what should be the definition of the sum of no vectors?

**Problem 18**  —

Is a space determined by its subspaces? That is, if two vector spaces have the same subspaces, must the two be equal?

**Problem 19**  —

1. Give a set that is closed under scalar multiplication but not addition.
2. Give a set closed under addition but not scalar multiplication.
3. Give a set closed under neither.

**Problem 20**  —

Show that the span of a set of vectors does not depend on the order in which the vectors are listed in that set.

**Problem 21**  —

Which trivial subspace is the span of the empty set? Is it

$$
\{\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}\}\subseteq \mathbb{R}^3, \quad\text{or}\quad \{0+0x\}\subseteq \mathcal{P}_1,
$$

or some other subspace?

**Problem 22**  —

Show that if a vector is in the span of a set then adding that vector to the set won't make the span any bigger. Is that also "only if"?  
*This exercise is recommended for all readers.*

**Problem 23**  —

Subspaces are subsets and so we naturally consider how "is a subspace of" interacts with the usual set operations.

1. If $$A,B$$ are subspaces of a vector space, must $$A\cap B$$ be a subspace? Always? Sometimes? Never?
2. Must $$A\cup B$$ be a subspace?
3. If $$A$$ is a subspace, must its complement be a subspace?

(*Hint.* Try some test subspaces from Example 2.19.)  
*This exercise is recommended for all readers.*

**Problem 24**  —

Does the span of a set depend on the enclosing space? That is, if $$W$$ is a subspace of $$V$$ and $$S$$ is a subset of $$W$$ (and so also a subset of $$V$$), might the span of $$S$$ in $$W$$ differ from the span of $$S$$ in $$V$$?

**Problem 25**  —

Is the relation "is a subspace of" transitive? That is, if $$V$$ is a subspace of $$W$$ and $$W$$ is a subspace of $$X$$, must $$V$$ be a subspace of $$X$$?  
*This exercise is recommended for all readers.*

**Problem 26**  —

Because "span of" is an operation on sets we naturally consider how it interacts with the usual set operations.

1. If $$S\subseteq T$$ are subsets of a vector space, is $$[S]\subseteq[T]$$? Always? Sometimes? Never?
2. If $$S,T$$ are subsets of a vector space, is $$[S\cup T]=[S]\cup[T]$$?
3. If $$S,T$$ are subsets of a vector space, is $$[S\cap T]=[S]\cap[T]$$?
4. Is the span of the complement equal to the complement of the span?

**Problem 27**  —

Reprove Lemma 2.15 without doing the empty set separately.

**Problem 28**  —

Find a structure that is closed under linear combinations, and yet is not a vector space. (*Remark.* This is a bit of a trick question.)

Solutions

---

*Source: Wikibooks, Linear Algebra/Subspaces and Spanning sets (https://en.wikibooks.org/wiki/Linear_Algebra/Subspaces_and_Spanning_sets), by Wikibooks contributors, CC BY-SA 4.0.*
