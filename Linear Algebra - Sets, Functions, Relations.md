# Sets, Functions, Relations

#### Sets

Mathematicians work with collections called **sets**. A set can be given as a listing between curly braces as in $$\{ 1,4,9,16 \}$$, or, if that's unwieldy, by using set-builder notation as in $$\{x\,\big|\, x^5-3x^3+2=0 \}$$ (read "the set of all $$x$$ such that \ldots"). We name sets with capital roman letters as with the primes $$P=\{2,3,5,7,11,\ldots\,\}$$, except for a few special sets such as the real numbers $$\mathbb{R}$$, and the complex numbers $$\mathbb{C}$$. To denote that something is an **element** (or **member**) of a set we use "$${}\in {}$$", so that $$7\in\{3,5,7\}$$ while $$8\not\in\{3,5,7\}$$.

What distinguishes a set from any other type of collection is the Principle of Extensionality, that two sets with the same elements are equal. Because of this principle, in a set repeats collapse $$\{7,7\}=\{7\}$$ and order doesn't matter $$\{2,\pi\}=\{\pi,2\}$$.

We use "$$\subset$$" for the subset relationship: $$\{2,\pi\}\subset\{2,\pi,7\}$$ and "$$\subseteq$$" for subset or equality (if $$A$$ is a subset of $$B$$ but $$A\neq B$$ then $$A$$ is a **proper subset** of $$B$$). These symbols may be flipped, for instance $$\{ 2,\pi,5\}\supset\{2,5\}$$.

Because of Extensionality, to prove that two sets are equal $$A=B$$, just show that they have the same members. Usually we show mutual inclusion, that both $$A\subseteq B$$ and $$A\supseteq B$$.

#### Set operations

Venn diagrams are handy here. For instance, $$x\in P$$ can be pictured

and "$$P\subseteq Q$$" looks like this.

Note that this is a repeat of the diagram for "if \ldots then ..." propositions. That's because "$$P\subseteq Q$$" means "if $$x\in P$$ then $$x\in Q$$".

In general, for every propositional logic operator there is an associated set operator. For instance, the **complement** of $$P$$ is $$P^{\text{comp}}=\{x\,\big|\, \text{not }(x\in P)\}$$

the **union** is $$P\cup Q=\{x\,\big|\,(x\in P) \text{ or }(x\in Q)\}$$

and the **intersection** is $$P\cap Q=\{x\,\big|\, (x\in P)\text{ and }(x\in Q)\}.$$

When two sets share no members their intersection is the **empty set** $$\{\}$$, symbolized $$\varnothing$$. Any set has the empty set for a subset, by the "vacuously true" property of the definition of implication.

#### Sequences

We shall also use collections where order does matter and where repeats do not collapse. These are **sequences**, denoted with angle brackets: $$\langle 2,3,7 \rangle \neq\langle 2,7,3 \rangle$$. A sequence of length $$2$$ is sometimes called an **ordered pair** and written with parentheses: $$(\pi,3)$$. We also sometimes say "ordered triple", "ordered $$4$$-tuple", etc. The set of ordered $$n$$-tuples of elements of a set $$A$$ is denoted $$A^n$$. Thus the set of pairs of reals is $$\mathbb{R}^2$$.

#### Functions

We first see functions in elementary Algebra, where they are presented as formulas (e.g., $$f(x)=16x^2-100$$), but progressing to more advanced Mathematics reveals more general functions— trigonometric ones, exponential and logarithmic ones, and even constructs like absolute value that involve piecing together parts— and we see that functions aren't formulas, instead the key idea is that a function associates with its input $$x$$ a single output $$f(x)$$.

Consequently, a **function** or **map** is defined to be a set of ordered pairs $$(x,f(x)\,)$$ such that $$x$$ suffices to determine $$f(x)$$, that is: if $$x_1=x_2$$ then $$f(x_1)=f(x_2)$$ (this requirement is referred to by saying a function is **well-defined**).\footnote{More on this is in the section on isomorphisms}

Each input $$x$$ is one of the function's **arguments** and each output $$f(x)$$ is a **value**. The set of all arguments is $$f$$'s **domain** and the set of output values is its **range**. Usually we don't need know what is and is not in the range and we instead work with a superset of the range, the **codomain**. The notation for a function $$f$$ with domain $$X$$ and codomain $$Y$$ is $$f:X\to Y$$.

We sometimes instead use the notation $$x\stackrel{f}{\longmapsto} 16x^2-100$$, read "$$x$$ maps under $$f$$ to $$16x^2-100$$", or "$$16x^2-100$$ is the "*image'* of $$x$$'.

Some maps, like $$x\mapsto \sin(1/x)$$, can be thought of as combinations of simple maps, here, $$g(y)=\sin(y)$$ applied to the image of $$f(x)=1/x$$. The **composition** of $$g:Y\to Z$$ with $$f:X\to Y$$, is the map sending $$x\in X$$ to $$g(\, f(x)\,)\in Z$$. It is denoted $$g\circ f:X\to Z$$. This definition only makes sense if the range of $$f$$ is a subset of the domain of $$g$$.

Observe that the **identity map** $$\text{id}:Y\to Y$$ defined by $$\text{id}(y)=y$$ has the property that for any $$f:X\to Y$$, the composition $$\text{id}\circ f$$ is equal to $$f$$. So an identity map plays the same role with respect to function composition that the number $$0$$ plays in real number addition, or that the number $$1$$ plays in multiplication.

In line with that analogy, define a **left inverse** of a map $$f:X\to Y$$ to be a function $$g:\text{range}(f)\to X$$ such that $$g\circ f$$ is the identity map on $$X$$. Of course, a **right inverse** of $$f$$ is a $$h:Y\to X$$ such that $$f\circ h$$ is the identity.

A map that is both a left and right inverse of $$f$$ is called simply an **inverse**. An inverse, if one exists, is unique because if both $$g_1$$ and $$g_2$$ are inverses of $$f$$ then $$g_1(x)=g_1\circ (f\circ g_2) (x) = (g_1\circ f) \circ g_2(x) =g_2(x)$$ (the middle equality comes from the associativity of function composition), so we often call it "the" inverse, written $$f^{-1}$$. For instance, the inverse of the function $$f:\mathbb{R}\to \mathbb{R}$$ given by $$f(x)=2x-3$$ is the function $$f^{-1}:\mathbb{R}\to \mathbb{R}$$ given by $$f^{-1}(x)=(x+3)/2$$.

The superscript "$$f^{-1}$$" notation for function inverse can be confusing— it doesn't mean $$1/f(x)$$. It is used because it fits into a larger scheme. Functions that have the same codomain as domain can be iterated, so that where $$f:X\to X$$, we can consider the composition of $$f$$ with itself: $$f\circ f$$, and $$f\circ f\circ f$$, etc.

Naturally enough, we write $$f\circ f$$ as $$f^2$$ and $$f\circ f\circ f$$ as $$f^3$$, etc. Note that the familiar exponent rules for real numbers obviously hold: $$f^i\circ f^j=f^{i+j}$$ and $$(f^i)^j=f^{i\cdot j}$$. The relationship with the prior paragraph is that, where $$f$$ is invertible, writing $$f^{-1}$$ for the inverse and $$f^{-2}$$ for the inverse of $$f^2$$, etc., gives that these familiar exponent rules continue to hold, once $$f^0$$ is defined to be the identity map.

If the codomain $$Y$$ equals the range of $$f$$ then we say that the function is **onto** (or **surjective**). A function has a right inverse if and only if it is onto (this is not hard to check). If no two arguments share an image, if $$x_1\neq x_2$$ implies that $$f(x_1)\neq f(x_2)$$, then the function is **one-to-one** (or **injective**). A function has a left inverse if and only if it is one-to-one (this is also not hard to check).

By the prior paragraph, a map has an inverse if and only if it is both onto and one-to-one; such a function is a **correspondence**. It associates one and only one element of the domain with each element of the range (for example, finite sets must have the same number of elements to be matched up in this way). Because a composition of one-to-one maps is one-to-one, and a composition of onto maps is onto, a composition of correspondences is a correspondence.

We sometimes want to shrink the domain of a function. For instance, we may take the function $$f:\mathbb{R}\to \mathbb{R}$$ given by $$f(x)=x^2$$ and, in order to have an inverse, limit input arguments to nonnegative reals $$\hat{f}:\mathbb{R}^+\to \mathbb{R}$$. Technically, $$\hat{f}$$ is a different function than $$f$$; we call it the **restriction** of $$f$$ to the smaller domain.

A final point on functions: neither $$x$$ nor $$f(x)$$ need be a number. As an example, we can think of $$f(x,y)=x+y$$ as a function that takes the ordered pair $$(x,y)$$ as its argument.

#### Relations

Some familiar operations are obviously functions: addition maps $$(5,3)$$ to $$8$$. But what of "$$<$$" or "$$=$$"? We here take the approach of rephrasing "$$3<5$$" to "$$(3,5)$$ is in the relation $$<$$". That is, define a **binary relation** on a set $$A$$ to be a set of ordered pairs of elements of $$A$$. For example, the $$<$$ relation is the set $$\{(a,b)\,\big|\, a<b\}$$; some elements of that set are $$(3,5)$$, $$(3,7)$$, and $$(1,100)$$.

Another binary relation on the natural numbers is equality; this relation is formally written as the set $$\{\ldots,(-1,-1),(0,0),(1,1),\ldots\}$$.

Still another example is "closer than $$10$$", the set $$\{(x,y)\,\big|\, |x-y|<10 \}$$. Some members of that relation are $$(1,10)$$, $$(10,1)$$, and $$(42,44)$$. Neither $$(11,1)$$ nor $$(1,11)$$ is a member.

Those examples illustrate the generality of the definition. All kinds of relationships (e.g., "both numbers even" or "first number is the second with the digits reversed") are covered under the definition.

#### Equivalence Relations

We shall need to say, formally, that two objects are alike in some way. While these alike things aren't identical, they are related (e.g., two integers that "give the same remainder when divided by $$2$$").

A binary relation $$\{(a,b),\ldots \}$$ is an **equivalence relation**when it satisfies

1. **reflexivity**: any object is related to itself;
2. **symmetry**: if $$a$$ is related to $$b$$ then $$b$$ is related to $$a$$;
3. **transitivity**: if $$a$$ is related to $$b$$ and $$b$$ is related to $$c$$ then $$a$$ is related to $$c$$.

(To see that these conditions formalize being the same, read them again, replacing "is related to" with "is like".)

Some examples (on the integers): "$$=$$" is an equivalence relation, "$$<$$" does not satisfy symmetry, "same sign" is a equivalence, while "nearer than $$10$$" fails transitivity.

#### Partitions

In "same sign" $$\{ (1,3),(-5,-7),(-1,-1),\ldots\}$$ there are two kinds of pairs, the first with both numbers positive and the second with both negative. So integers fall into exactly one of two classes, positive or negative.

A **partition** of a set $$S$$ is a collection of subsets $$\{S_1,S_2,\ldots\}$$ such that every element of $$S$$ is in one and only one $$S_i$$: $$S_1\cup S_2\cup \ldots{} = S$$, and if $$i$$ is not equal to $$j$$ then $$S_i\cap S_j=\varnothing$$. Picture $$S$$ being decomposed into distinct parts.

Thus, the first paragraph says "same sign" partitions the integers into the positives and the negatives.

Similarly, the equivalence relation "=" partitions the integers into one-element sets.

Another example is the fractions. Of course, $$2/3$$ and $$4/6$$ are equivalent fractions. That is, for the set $$S=\{n/d\,\big|\, n,d\in\mathbb{Z}\text{ and }d\neq 0\}$$, we define two elements $$n_1/d_1$$ and $$n_2/d_2$$ to be equivalent if $$n_1d_2=n_2d_1$$. We can check that this is an equivalence relation, that is, that it satisfies the above three conditions. With that, $$S$$ is divided up into parts.

Before we show that equivalence relations always give rise to partitions, we first illustrate the argument. Consider the relationship between two integers of "same parity", the set $$\{ (-1,3),(2,4),(0,0),\ldots\}$$ (i.e., "give the same remainder when divided by $$2$$"). We want to say that the natural numbers split into two pieces, the evens and the odds, and inside a piece each member has the same parity as each other. So for each $$x$$ we define the set of numbers associated with it: $$S_x=\{y\,\big|\, (x,y)\in\text{same parity}\}$$. Some examples are $$S_1=\{\ldots,-3,-1,1,3,\ldots\}$$, and $$S_4=\{\ldots,-2,0,2,4,\ldots\}$$, and $$S_{-1}=\{\ldots,-3,-1,1,3,\ldots\}$$. These are the parts, e.g., $$S_1$$ is the odds.  
**Theorem** An equivalence relation induces a partition on the underlying set.

**Proof**  —

Call the set $$S$$ and the relation $$R$$. In line with the illustration in the paragraph above, for each $$x\in S$$ define $$S_x=\{y\,\big|\, (x,y)\in R\}$$.

Observe that, as $$x$$ is a member if $$S_x$$, the union of all these sets is $$S$$. So we will be done if we show that distinct parts are disjoint: if $$S_x\neq S_y$$ then $$S_x\cap S_y=\varnothing$$. We will verify this through the contrapositive, that is, we wlll assume that $$S_x\cap S_y\neq\varnothing$$ in order to deduce that $$S_x=S_y$$.

Let $$p$$ be an element of the intersection. Then by definition of $$S_x$$ and $$S_y$$, the two $$(x,p)$$ and $$(y,p)$$ are members of $$R$$, and by symmetry of this relation $$(p,x)$$ and $$(p,y)$$ are also members of $$R$$. To show that $$S_x=S_y$$ we will show each is a subset of the other.

Assume that $$q\in S_x$$ so that $$(q,x)\in R$$. Use transitivity along with $$(x,p)\in R$$ to conclude that $$(q,p)$$ is also an element of $$R$$. But $$(p,y)\in R$$ so another use of transitivity gives that $$(q,y)\in R$$. Thus $$q\in S_y$$. Therefore $$q\in S_x$$ implies $$q\in S_y$$, and so $$S_x\subseteq S_y$$.

The same argument in the other direction gives the other inclusion, and so the two sets are equal, completing the contrapositive argument.

We call each part of a partition an **equivalence class** (or informally, "part").

We somtimes pick a single element of each equivalence class to be the **class representative**.

Usually when we pick representatives we have some natural scheme in mind. In that case we call them the **canonical** representatives.

An example is the simplest form of a fraction. We've defined $$3/5$$ and $$9/15$$ to be equivalent fractions. In everyday work we often use the "simplest form" or "reduced form" fraction as the class representatives.

---

*Source: Wikibooks, Linear Algebra/Sets, Functions, Relations (https://en.wikibooks.org/wiki/Linear_Algebra/Sets%2C_Functions%2C_Relations), by Wikibooks contributors, CC BY-SA 4.0.*
