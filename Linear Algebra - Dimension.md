# Dimension

In the prior subsection we defined the basis of a vector space, and we saw that a space can have many different bases. For example, following the definition of a basis, we saw three different bases for $$\mathbb{R}^2$$. So we cannot talk about "the" basis for a vector space. True, some vector spaces have bases that strike us as more natural than others, for instance, $$\mathbb{R}^2$$'s basis $$\mathcal{E}_2$$ or $$\mathbb{R}^3$$'s basis $$\mathcal{E}_3$$ or $$\mathcal{P}_2$$'s basis $$\langle 1,x,x^2 \rangle$$. But, for example in the space $$\{a_2x^2+a_1x+a_0\,\big|\, 2a_2-a_0=a_1\}$$, no particular basis leaps out at us as the most natural one. We cannot, in general, associate with a space any single basis that best describes that space.

We can, however, find something about the bases that is uniquely associated with the space. This subsection shows that any two bases for a space have the same number of elements. So, with each space we can associate a number, the number of vectors in any of its bases.

This brings us back to when we considered the two things that could be meant by the term "minimal spanning set". At that point we defined "minimal" as linearly independent, but we noted that another reasonable interpretation of the term is that a spanning set is "minimal" when it has the fewest number of elements of any set with the same span. At the end of this subsection, after we have shown that all bases have the same number of elements, then we will have shown that the two senses of "minimal" are equivalent.

Before we start, we first limit our attention to spaces where at least one basis has only finitely many members.

**Definition 2.1**  —

A vector space is **finite-dimensional** if it has a basis with only finitely many vectors.

(One reason for sticking to finite-dimensional spaces is so that the representation of a vector with respect to a basis is a finitely-tall vector, and so can be easily written.) From now on we study only finite-dimensional vector spaces. We shall take the term "vector space" to mean "finite-dimensional vector space". Other spaces are interesting and important, but they lie outside of our scope.

To prove the main theorem we shall use a technical result.

**Lemma 2.2 (Exchange Lemma)**  —

Assume that $$B=\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ is a basis for a vector space, and that for the vector $$\vec{v}$$ the relationship $$\vec{v}=c_1\vec{\beta}_1+c_2\vec{\beta}_2+\cdots +c_n\vec{\beta}_n$$ has $$c_i\neq 0$$. Then exchanging $$\vec{\beta}_i$$ for $$\vec{v}$$ yields another basis for the space.

**Proof**  —

Call the outcome of the exchange $$\hat{B}=\langle \vec{\beta}_1,\dots,\vec{\beta}_{i-1},\vec{v},\vec{\beta}_{i+1},\dots,\vec{\beta}_n \rangle$$.

We first show that $$\hat{B}$$ is linearly independent. Any relationship $$d_1\vec{\beta}_1+\dots+d_i\vec{v}+\dots+d_n\vec{\beta}_n=\vec{0}$$ among the members of $$\hat{B}$$, after substitution for $$\vec{v}$$,

$$
d_1\vec{\beta}_1+\dots +d_i\cdot(c_1\vec{\beta}_1+\dots+c_i\vec{\beta}_i+\dots+c_n\vec{\beta}_n) +\dots+d_n\vec{\beta}_n =\vec{0} \qquad\qquad(*)
$$

gives a linear relationship among the members of $$B$$. The basis $$B$$ is linearly independent, so the coefficient $$d_ic_i$$ of $$\vec{\beta}_i$$ is zero. Because $$c_i$$ is assumed to be nonzero, $$d_i=0$$. Using this in equation $$(*)$$ above gives that all of the other $$d$$'s are also zero. Therefore $$\hat{B}$$ is linearly independent.

We finish by showing that $$\hat{B}$$ has the same span as $$B$$. Half of this argument, that $$[{\hat{B}}]\subseteq[B]$$, is easy; any member $$d_1\vec{\beta}_1+\dots+d_i\vec{v}+\dots+d_n\vec{\beta}_n$$ of $$[{\hat{B}}]$$ can be written $$d_1\vec{\beta}_1+\dots+d_i\cdot(c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n)+\dots+d_n\vec{\beta}_n$$, which is a linear combination of linear combinations of members of $$B$$, and hence is in $$[B]$$. For the $$[B]\subseteq[{\hat{B}}]$$ half of the argument, recall that when $$\vec{v}=c_1\vec{\beta}_1+\dots+c_n\vec{\beta}_n$$ with $$c_i\neq 0$$, then the equation can be rearranged to $$\vec{\beta}_i=(-c_1/c_i)\vec{\beta}_1+\dots+(1/c_i)\vec{v}+\dots+(-c_n/c_i)\vec{\beta}_n$$. Now, consider any member $$d_1\vec{\beta}_1+\dots+d_i\vec{\beta}_i+\dots+d_n\vec{\beta}_n$$ of $$[B]$$, substitute for $$\vec{\beta}_i$$ its expression as a linear combination of the members of $$\hat{B}$$, and recognize (as in the first half of this argument) that the result is a linear combination of linear combinations, of members of $$\hat{B}$$, and hence is in $$[{\hat{B}}]$$.

**Theorem 2.3**  —

In any finite-dimensional vector space, all of the bases have the same number of elements.

**Proof**  —

Fix a vector space with at least one finite basis. Choose, from among all of this space's bases, one $$B=\langle \vec{\beta}_1,\dots,\vec{\beta}_n \rangle$$ of minimal size. We will show that any other basis $$D={\langle \vec{\delta}_1,\vec{\delta}_2,\ldots \rangle }$$ also has the same number of members, $$n$$. Because $$B$$ has minimal size, $$D$$ has no fewer than $$n$$ vectors. We will argue that it cannot have more than $$n$$ vectors.

The basis $$B$$ spans the space and $$\vec{\delta}_1$$ is in the space, so $$\vec{\delta}_1$$ is a nontrivial linear combination of elements of $$B$$. By the Exchange Lemma, $$\vec{\delta}_1$$ can be swapped for a vector from $$B$$, resulting in a basis $$B_1$$, where one element is $$\vec{\delta}$$ and all of the $$n-1$$ other elements are $$\vec{\beta}$$'s.

The prior paragraph forms the basis step for an induction argument. The inductive step starts with a basis $$B_k$$ (for $$1\leq k<n$$) containing $$k$$ members of $$D$$ and $$n-k$$ members of $$B$$. We know that $$D$$ has at least $$n$$ members so there is a $$\vec{\delta}_{k+1}$$. Represent it as a linear combination of elements of $$B_k$$. The key point: in that representation, at least one of the nonzero scalars must be associated with a $$\vec{\beta}_i$$ or else that representation would be a nontrivial linear relationship among elements of the linearly independent set $$D$$. Exchange $$\vec{\delta}_{k+1}$$ for $$\vec{\beta}_i$$ to get a new basis $$B_{k+1}$$ with one $$\vec{\delta}$$ more and one $$\vec{\beta}$$ fewer than the previous basis $$B_k$$.

Repeat the inductive step until no $$\vec{\beta}$$'s remain, so that $$B_n$$ contains $$\vec{\delta}_1,\dots,\vec{\delta}_n$$. Now, $$D$$ cannot have more than these $$n$$ vectors because any $$\vec{\delta}_{n+1}$$ that remains would be in the span of $$B_n$$ (since it is a basis) and hence would be a linear combination of the other $$\vec{\delta}$$'s, contradicting that $$D$$ is linearly independent.

**Definition 2.4**  —

The **dimension** of a vector space is the number of vectors in any of its bases.

**Example 2.5**  —

Any basis for $$\mathbb{R}^n$$ has $$n$$ vectors since the standard basis $$\mathcal{E}_n$$ has $$n$$ vectors. Thus, this definition generalizes the most familiar use of term, that $$\mathbb{R}^n$$ is $$n$$-dimensional.

**Example 2.6**  —

The space $$\mathcal{P}_n$$ of polynomials of degree at most $$n$$ has dimension $$n+1$$. We can show this by exhibiting any basis— $$\langle 1,x,\dots,x^n \rangle$$ comes to mind— and counting its members.

**Example 2.7**  —

A trivial space is zero-dimensional since its basis is empty.

Again, although we sometimes say "finite-dimensional" as a reminder, in the rest of this book all vector spaces are assumed to be finite-dimensional. An instance of this is that in the next result the word "space" should be taken to mean "finite-dimensional vector space".

**Corollary 2.8**  —

No linearly independent set can have a size greater than the dimension of the enclosing space.

**Proof**  —

Inspection of the above proof shows that it never uses that $$D$$ spans the space, only that $$D$$ is linearly independent.

**Example 2.9**  —

Recall the subspace diagram from the prior section showing the subspaces of $$\mathbb{R}^3$$. Each subspace shown is described with a minimal spanning set, for which we now have the term "basis". The whole space has a basis with three members, the plane subspaces have bases with two members, the line subspaces have bases with one member, and the trivial subspace has a basis with zero members. When we saw that diagram we could not show that these are the only subspaces that this space has. We can show it now. The prior corollary proves that the only subspaces of $$\mathbb{R}^3$$ are either three-, two-, one-, or zero-dimensional. Therefore, the diagram indicates all of the subspaces. There are no subspaces somehow, say, between lines and planes.

**Corollary 2.10**  —

Any linearly independent set can be expanded to make a basis.

**Proof**  —

If a linearly independent set is not already a basis then it must not span the space. Adding to it a vector that is not in the span preserves linear independence. Keep adding, until the resulting set does span the space, which the prior corollary shows will happen after only a finite number of steps.

**Corollary 2.11**  —

Any spanning set can be shrunk to a basis.

**Proof**  —

Call the spanning set $$S$$. If $$S$$ is empty then it is already a basis (the space must be a trivial space). If $$S=\{\vec{0}\}$$ then it can be shrunk to the empty basis, thereby making it linearly independent, without changing its span.

Otherwise, $$S$$ contains a vector $$\vec{s}_1$$ with $$\vec{s}_1\neq\vec{0}$$ and we can form a basis $$B_1=\langle \vec{s}_1 \rangle$$. If $$[B_1]=[S]$$ then we are done.

If not then there is a $$\vec{s}_2\in[S]$$ such that $$\vec{s}_2\not\in[B_1]$$. Let $$B_2=\langle \vec{s}_1,\vec{s_2} \rangle$$; if $$[B_2]=[S]$$ then we are done.

We can repeat this process until the spans are equal, which must happen in at most finitely many steps.

**Corollary 2.12**  —

In an $$n$$-dimensional space, a set of $$n$$ vectors is linearly independent if and only if it spans the space.

**Proof**  —

First we will show that a subset with $$n$$ vectors is linearly independent if and only if it is a basis. "If" is trivially true— bases are linearly independent. "Only if" holds because a linearly independent set can be expanded to a basis, but a basis has $$n$$ elements, so this expansion is actually the set that we began with.

To finish, we will show that any subset with $$n$$ vectors spans the space if and only if it is a basis. Again, "if" is trivial. "Only if" holds because any spanning set can be shrunk to a basis, but a basis has $$n$$ elements and so this shrunken set is just the one we started with.

The main result of this subsection, that all of the bases in a finite-dimensional vector space have the same number of elements, is the single most important result in this book because, as Example 2.9 shows, it describes what vector spaces and subspaces there can be. We will see more in the next chapter.

**Remark 2.13**  —

The case of infinite-dimensional vector spaces is somewhat controversial. The statement "any infinite-dimensional vector space has a basis" is known to be equivalent to a statement called the Axiom of Choice (see (Blass 1984).) Mathematicians differ philosophically on whether to accept or reject this statement as an axiom on which to base mathematics (although, the great majority seem to accept it). Consequently the question about infinite-dimensional vector spaces is still somewhat up in the air. (A discussion of the Axiom of Choice can be found in the Frequently Asked Questions list for the Usenet group sci.math. Another accessible reference is (Rucker 1982).

### Exercises

*Assume that all spaces are finite-dimensional unless otherwise stated.*  
*This exercise is recommended for all readers.*

**Problem 1**  —

Find a basis for, and the dimension of, $$\mathcal{P}_2$$.

**Problem 2**  —

Find a basis for, and the dimension of, the solution set of this system.

$$
\begin{array}{rcrcrcrcr} x_1 &- &4x_2 &+ &3x_3 &- &x_4 &= &0 \\ 2x_1 &- &8x_2 &+ &6x_3 &- &2x_4 &= &0 \end{array}
$$

*This exercise is recommended for all readers.*

**Problem 3**  —

Find a basis for, and the dimension of, $$\mathcal{M}_{2 \! \times \! 2}$$, the vector space of $$2 \! \times \! 2$$ matrices.

**Problem 4**  —

Find the dimension of the vector space of matrices

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix}
$$

subject to each condition.

1. $$a, b, c, d\in\mathbb{R}$$
2. $$a-b+2c=0$$ and $$d\in\mathbb{R}$$
3. $$a+b+c=0$$, $$a+b-c=0$$, and $$d\in\mathbb{R}$$  
*This exercise is recommended for all readers.*

**Problem 5**  —

Find the dimension of each.

1. The space of cubic polynomials $$p(x)$$ such that $$p(7)=0$$
2. The space of cubic polynomials $$p(x)$$ such that $$p(7)=0$$ and $$p(5)=0$$
3. The space of cubic polynomials $$p(x)$$ such that $$p(7)=0$$, $$p(5)=0$$, and $$p(3)=0$$
4. The space of cubic polynomials $$p(x)$$ such that $$p(7)=0$$, $$p(5)=0$$, $$p(3)=0$$, and $$p(1)=0$$

**Problem 6**  —

What is the dimension of the span of the set $$\{\cos^2\theta,\sin^2\theta,\cos2\theta,\sin2\theta\}$$? This span is a subspace of the space of all real-valued functions of one real variable.

**Problem 7**  —

Find the dimension of $$\mathbb{C}^{47}$$, the vector space of $$47$$-tuples of complex numbers.

**Problem 8**  —

What is the dimension of the vector space $$\mathcal{M}_{3 \! \times \! 5}$$ of $$3 \! \times \! 5$$ matrices?  
*This exercise is recommended for all readers.*

**Problem 9**  —

Show that this is a basis for $$\mathbb{R}^4$$.

$$
\langle \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} \rangle
$$

(The results of this subsection can be used to simplify this job.)

**Problem 10**  —

Refer to Example 2.9.

1. Sketch a similar subspace diagram for $$\mathcal{P}_2$$.
2. Sketch one for $$\mathcal{M}_{2 \! \times \! 2}$$.  
*This exercise is recommended for all readers.*

**Problem 11**  — Where $$S$$ is a set, the functions $$f:S\to\mathbb{R}$$ form a vector space under the natural operations: the sum $$f+g$$ is the function given by $$(f+g)\,(s)=f(s)+g(s)$$ and the scalar product is given by $$(r\cdot f) \, (s)=r\cdot f(s)$$. What is the dimension of the space resulting for each domain?

1. $$S=\{1\}$$
2. $$S=\{1,2\}$$
3. $$S=\{1,\ldots,n\}$$

**Problem 12**  —

(See Problem 11.) Prove that this is an infinite-dimensional space: the set of all functions $$f:\mathbb{R}\to\mathbb{R}$$ under the natural operations.

**Problem 13**  —

(See Problem 11.) What is the dimension of the vector space of functions $$f:S\to\mathbb{R}$$, under the natural operations, where the domain $$S$$ is the empty set?

**Problem 14**  —

Show that any set of four vectors in $$\mathbb{R}^2$$ is linearly dependent.

**Problem 15**  —

Show that the set $$\langle \vec{\alpha}_1,\vec{\alpha}_2,\vec{\alpha}_3 \rangle \subset\mathbb{R}^3$$ is a basis if and only if there is no plane through the origin containing all three vectors.

**Problem 16**  —

1. Prove that any subspace of a finite dimensional space has a basis.
2. Prove that any subspace of a finite dimensional space is finite dimensional.

**Problem 17**  —

Where is the finiteness of $$B$$ used in Theorem 2.3?  
*This exercise is recommended for all readers.*

**Problem 18**  —

Prove that if $$U$$ and $$W$$ are both three-dimensional subspaces of $$\mathbb{R}^5$$ then $$U\cap W$$ is non-trivial. Generalize.

**Problem 19**  —

Because a basis for a space is a subset of that space, we are naturally led to how the property "is a basis" interacts with set operations.

1. Consider first how bases might be related by "subset". Assume that $$U,W$$ are subspaces of some vector space and that $$U\subseteq W$$. Can there exist bases $$B_U$$ for $$U$$ and $$B_W$$ for $$W$$ such that $$B_U\subseteq B_W$$? Must such bases exist? For any basis $$B_U$$ for $$U$$, must there be a basis $$B_W$$ for $$W$$ such that $$B_U\subseteq B_W$$? For any basis $$B_W$$ for $$W$$, must there be a basis $$B_U$$ for $$U$$ such that $$B_U\subseteq B_W$$? For any bases $$B_U, B_W$$ for $$U$$ and $$W$$, must $$B_U$$ be a subset of $$B_W$$?
2. Is the intersection of bases a basis? For what space?
3. Is the union of bases a basis? For what space?
4. What about complement?

(*Hint.* Test any conjectures against some subspaces of $$\mathbb{R}^3$$.)  
*This exercise is recommended for all readers.*

**Problem 20**  —

Consider how "dimension" interacts with "subset". Assume $$U$$ and $$W$$ are both subspaces of some vector space, and that $$U\subseteq W$$.

1. Prove that $$\dim (U)\leq\dim (W)$$.
2. Prove that equality of dimension holds if and only if $$U=W$$.
3. Show that the prior item does not hold if they are infinite-dimensional.

?** Problem 21**  —

For any vector $$\vec{v}$$ in $$\mathbb{R}^n$$ and any permutation $$\sigma$$ of the numbers $$1$$, $$2$$, ..., $$n$$ (that is, $$\sigma$$ is a rearrangement of those numbers into a new order), define $$\sigma(\vec{v})$$ to be the vector whose components are $$v_{\sigma(1)}$$, $$v_{\sigma(2)}$$, ..., and $$v_{\sigma(n)}$$ (where $$\sigma(1)$$ is the first number in the rearrangement, etc.). Now fix $$\vec{v}$$ and let $$V$$ be the span of $$\{\sigma(\vec{v})\,\big|\, \sigma\text{ permutes }1, \ldots, n\}$$. What are the possibilities for the dimension of $$V$$? (Gilbert, Krusemeyer & Larson 1993, Problem 47)

Solutions

### References

- Blass, A. (1984), "Existence of Bases Implies the Axiom of Choice", in Baumgartner, J. E. (ed.), *Axiomatic Set Theory*, Providence RI: American Mathematical Society, pp. 31–33.
- Rucker, Rudy (1982), *Infinity and the Mind*, Birkhauser.
- Gilbert, George T.; Krusemeyer, Mark; Larson, Loren C. (1993), *The Wohascum County Problem Book*, The Mathematical Association of America.

---

*Source: Wikibooks, Linear Algebra/Dimension (https://en.wikibooks.org/wiki/Linear_Algebra/Dimension), by Wikibooks contributors, CC BY-SA 4.0.*
