# Definition and Examples of Linear Independence

### Spanning Sets and Linear Independence

We first characterize when a vector can be removed from a set without changing the span of that set.

**Lemma 1.1**  —

Where $$S$$ is a subset of a vector space $$V$$,

$$
[S]=[S\cup\{\vec{v}\}] \quad\text{if and only if}\quad \vec{v}\in[S]
$$

for any $$\vec{v}\in V$$.

**Proof**  —

The left to right implication is easy. If $$[S]=[S\cup\{\vec{v}\}]$$ then, since $$\vec{v}\in[S\cup\{\vec{v}\}]$$, the equality of the two sets gives that $$\vec{v}\in[S]$$.

For the right to left implication assume that $$\vec{v}\in [S]$$ to show that $$[S]=[S\cup\{\vec{v}\}]$$ by mutual inclusion. The inclusion $$[S]\subseteq[S\cup\{\vec{v}\}]$$ is obvious. For the other inclusion $$[S]\supseteq[S\cup\{\vec{v}\}]$$, write an element of $$[S\cup\{\vec{v}\}]$$ as $$d_0\vec{v}+d_1\vec{s}_1+\dots+d_m\vec{s}_m$$ and substitute $$\vec{v}$$'s expansion as a linear combination of members of the same set $$d_0(c_0\vec{t}_0+\dots+c_k\vec{t}_k)+d_1\vec{s}_1+\dots+d_m\vec{s}_m$$. This is a linear combination of linear combinations and so distributing $$d_0$$ results in a linear combination of vectors from $$S$$. Hence each member of $$[S\cup\{\vec{v}\}]$$ is also a member of $$[S]$$.

**Example 1.2**  —

In $$\mathbb{R}^3$$, where

$$
\vec{v}_1=\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}\quad \vec{v}_2=\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}\quad \vec{v}_3=\begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}
$$

the spans $$[\{\vec{v}_1,\vec{v}_2\}]$$ and $$[\{\vec{v}_1,\vec{v}_2,\vec{v}_3\}]$$ are equal since $$\vec{v}_3$$ is in the span $$[\{\vec{v}_1,\vec{v}_2\}]$$.

The lemma says that if we have a spanning set then we can remove a $$\vec{v}$$ to get a new set $$S$$ with the same span if and only if $$\vec{v}$$ is a linear combination of vectors from $$S$$. Thus, under the second sense described above, a spanning set is minimal if and only if it contains no vectors that are linear combinations of the others in that set. We have a term for this important property.

**Definition 1.3**  —

A subset of a vector space is **linearly independent** if none of its elements is a linear combination of the others. Otherwise it is **linearly dependent**.

Here is an important observation:

$$
\vec{s}_0=c_1\vec{s}_1+c_2\vec{s}_2+\cdots +c_n\vec{s}_n
$$

although this way of writing one vector as a combination of the others visually sets $$\vec{s}_0$$ off from the other vectors, algebraically there is nothing special in that equation about $$\vec{s}_0$$. For any $$\vec{s}_i$$ with a coefficient $$c_i$$ that is nonzero, we can rewrite the relationship to set off $$\vec{s}_i$$.

$$
\vec{s}_i=(1/c_i)\vec{s}_0+(-c_1/c_i)\vec{s}_1 +\dots+(-c_n/c_i)\vec{s}_n
$$

When we don't want to single out any vector by writing it alone on one side of the equation we will instead say that $$\vec{s}_0,\vec{s}_1,\dots,\vec{s}_n$$ are in a **linear relationship** and write the relationship with all of the vectors on the same side. The next result rephrases the linear independence definition in this style. It gives what is usually the easiest way to compute whether a finite set is dependent or independent.

**Lemma 1.4**  —

A subset $$S$$ of a vector space is linearly independent if and only if for any distinct $$\vec{s}_1,\dots,\vec{s}_n\in S$$ the only linear relationship among those vectors

$$
c_1\vec{s}_1+\dots+c_n\vec{s}_n=\vec{0} \qquad c_1,\dots,c_n\in\mathbb{R}
$$

is the trivial one: $$c_1=0,\dots,\,c_n=0$$.

**Proof**  —

This is a direct consequence of the observation above.

If the set $$S$$ is linearly independent then no vector $$\vec{s}_i$$ can be written as a linear combination of the other vectors from $$S$$ so there is no linear relationship where some of the $$\vec{s}\,$$'s have nonzero coefficients. If $$S$$ is not linearly independent then some $$\vec{s}_i$$ is a linear combination $$\vec{s}_i=c_1\vec{s}_1+\dots+c_{i-1}\vec{s}_{i-1} +c_{i+1}\vec{s}_{i+1}+\dots+c_n\vec{s}_n$$ of other vectors from $$S$$, and subtracting $$\vec{s}_i$$ from both sides of that equation gives a linear relationship involving a nonzero coefficient, namely the $$-1$$ in front of $$\vec{s}_i$$.

**Example 1.5**  —

In the vector space of two-wide row vectors, the two-element set $$\{ \begin{pmatrix} 40 &15 \end{pmatrix},\begin{pmatrix} -50 &25 \end{pmatrix}\}$$ is linearly independent. To check this, set

$$
c_1\cdot\begin{pmatrix} 40 &15 \end{pmatrix}+c_2\cdot\begin{pmatrix} -50 &25 \end{pmatrix}=\begin{pmatrix} 0 &0 \end{pmatrix}
$$

and solving the resulting system

$$
\begin{array}{rcrcr} 40c_1 &- &50c_2 &= &0 \\ 15c_1 &+ &25c_2 &= &0 \end{array} \;\xrightarrow[]{-(15/40)\rho_1+\rho_2}\; \begin{array}{rcrcr} 40c_1 &- &50c_2 &= &0 \\ & &(175/4)c_2 &= &0 \end{array}
$$

shows that both $$c_1$$ and $$c_2$$ are zero. So the only linear relationship between the two given row vectors is the trivial relationship.

In the same vector space, $$\{ \begin{pmatrix} 40 &15 \end{pmatrix},\begin{pmatrix} 20 &7.5 \end{pmatrix}\}$$ is linearly dependent since we can satisfy

$$
c_1\begin{pmatrix} 40 &15 \end{pmatrix}+c_2\cdot\begin{pmatrix} 20 &7.5 \end{pmatrix}=\begin{pmatrix} 0 &0 \end{pmatrix}
$$

with $$c_1=1$$ and $$c_2=-2$$.

**Remark 1.6**  —

Recall the Statics example that began this book. We first set the unknown-mass objects at $$40$$ cm and $$15$$ cm and got a balance, and then we set the objects at $$-50$$ cm and $$25$$ cm and got a balance. With those two pieces of information we could compute values of the unknown masses. Had we instead first set the unknown-mass objects at $$40$$ cm and $$15$$ cm, and then at $$20$$ cm and $$7.5$$ cm, we would not have been able to compute the values of the unknown masses (try it). Intuitively, the problem is that the $$\begin{pmatrix} 20 &7.5 \end{pmatrix}$$ information is a "repeat" of the $$\begin{pmatrix} 40 &15 \end{pmatrix}$$ information— that is, $$\begin{pmatrix} 20 &7.5 \end{pmatrix}$$ is in the span of the set $$\{\begin{pmatrix} 40 &15 \end{pmatrix}\}$$— and so we would be trying to solve a two-unknowns problem with what is essentially one piece of information.

**Example 1.7**  —

The set $$\{1+x,1-x\}$$ is linearly independent in $$\mathcal{P}_2$$, the space of quadratic polynomials with real coefficients, because

$$
0+0x+0x^2 = c_1(1+x)+c_2(1-x) = (c_1+c_2)+(c_1-c_2)x+0x^2
$$

gives

$$
\begin{array}{rcl} \begin{array}{rcrcr} c_1 &+ &c_2 &= &0 \\ c_1 &- &c_2 &= &0 \end{array} &\xrightarrow[]{-\rho_1+\rho_2} &\begin{array}{rcrcr} c_1 &+ &c_2 &= &0 \\ & &2c_2 &= &0 \end{array} \end{array}
$$

since polynomials are equal only if their coefficients are equal. Thus, the only linear relationship between these two members of $$\mathcal{P}_2$$ is the trivial one.

**Example 1.8**  —

In $$\mathbb{R}^3$$, where

$$
\vec{v}_1=\begin{pmatrix} 3 \\ 4 \\ 5 \end{pmatrix} \quad \vec{v}_2=\begin{pmatrix} 2 \\ 9 \\ 2 \end{pmatrix} \quad \vec{v}_3=\begin{pmatrix} 4 \\ 18 \\ 4 \end{pmatrix}
$$

the set $$S=\{\vec{v}_1,\vec{v}_2,\vec{v}_3\}$$ is linearly dependent because this is a relationship

$$
0\cdot\vec{v}_1 +2\cdot\vec{v}_2 -1\cdot\vec{v}_3 =\vec{0}
$$

where not all of the scalars are zero (the fact that some of the scalars are zero doesn't matter).

**Remark 1.9**  —

That example illustrates why, although Definition 1.3 is a clearer statement of what independence is, Lemma 1.4 is more useful for computations. Working straight from the definition, someone trying to compute whether $$S$$ is linearly independent would start by setting $$\vec{v}_1=c_2\vec{v}_2+c_3\vec{v}_3$$ and concluding that there are no such $$c_2$$ and $$c_3$$. But knowing that the first vector is not dependent on the other two is not enough. This person would have to go on to try $$\vec{v}_2=c_1\vec{v}_1+c_3\vec{v}_3$$ to find the dependence $$c_1=0$$, $$c_3=1/2$$. Lemma 1.4 gets the same conclusion with only one computation.

**Example 1.10**  —

The empty subset of a vector space is linearly independent. There is no nontrivial linear relationship among its members as it has no members.

**Example 1.11**  —

In any vector space, any subset containing the zero vector is linearly dependent. For example, in the space $$\mathcal{P}_2$$ of quadratic polynomials, consider the subset $$\{1+x,x+x^2,0\}$$.

One way to see that this subset is linearly dependent is to use Lemma 1.4: we have $$0\cdot\vec{v}_1+0\cdot\vec{v}_2+1\cdot\vec{0}=\vec{0}$$, and this is a nontrivial relationship as not all of the coefficients are zero. Another way to see that this subset is linearly dependent is to go straight to Definition 1.3: we can express the third member of the subset as a linear combination of the first two, namely, $$c_1\vec{v}_1+c_2\vec{v}_2=\vec{0}$$ is satisfied by taking $$c_1=0$$ and $$c_2=0$$ (in contrast to the lemma, the definition allows all of the coefficients to be zero).

(There is still another way to see that this subset is dependent that is subtler. The zero vector is equal to the trivial sum, that is, it is the sum of no vectors. So in a set containing the zero vector, there is an element that can be written as a combination of a collection of other vectors from the set, specifically, the zero vector can be written as a combination of the empty collection.)

The above examples, especially Example 1.5, underline the discussion that begins this section. The next result says that given a finite set, we can produce a linearly independent subset by discarding what Remark 1.6 calls "repeats".  
**Theorem 1.12**  —

In a vector space, any finite subset has a linearly independent subset with the same span.

**Proof**  —

If the set $$S=\{ \vec{s}_1,\dots,\vec{s}_n\}$$ is linearly independent then $$S$$ itself satisfies the statement, so assume that it is linearly dependent.

By the definition of dependence, there is a vector $$\vec{s}_i$$ that is a linear combination of the others. Call that vector $$\vec{v}_1$$. Discard it— define the set $$S_1=S-\{\vec{v}_1\}$$. By Lemma 1.1, the span does not shrink $$[S_1]=[S]$$.

Now, if $$S_1$$ is linearly independent then we are finished. Otherwise iterate the prior paragraph: take a vector $$\vec{v}_2$$ that is a linear combination of other members of $$S_1$$ and discard it to derive $$S_2=S_1-\{\vec{v}_2\}$$ such that $$[S_2]=[S_1]$$. Repeat this until a linearly independent set $$S_j$$ appears; one must appear eventually because $$S$$ is finite and the empty set is linearly independent. (Formally, this argument uses induction on $$n$$, the number of elements in the starting set. Problem 20 asks for the details.)

**Example 1.13**  —

This set spans $$\mathbb{R}^3$$.

$$
S=\{\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ -1 \\ 1 \end{pmatrix}, \begin{pmatrix} 3 \\ 3 \\ 0 \end{pmatrix} \}
$$

Looking for a linear relationship

$$
c_1\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} +c_2\begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix} +c_3\begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} +c_4\begin{pmatrix} 0 \\ -1 \\ 1 \end{pmatrix} +c_5\begin{pmatrix} 3 \\ 3 \\ 0 \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$

gives a three equations/five unknowns linear system whose solution set can be parametrized in this way.  

$$
\{\begin{pmatrix} c_1 \\ c_2 \\ c_3 \\ c_4 \\ c_5 \end{pmatrix}= c_3\begin{pmatrix} -1 \\ -1 \\ 1 \\ 0 \\ 0 \end{pmatrix} +c_5\begin{pmatrix} -3 \\ -3/2 \\ 0 \\ 0 \\ 1 \end{pmatrix} \,\big|\, c_3,c_5\in\mathbb{R} \}
$$

So $$S$$ is linearly dependent. Setting $$c_3=0$$ and $$c_5=1$$ shows that the fifth vector is a linear combination of the first two. Thus, Lemma 1.1 says that discarding the fifth vector

$$
S_1=\{\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ -1 \\ 1 \end{pmatrix} \}
$$

leaves the span unchanged $$[S_1]=[S]$$. Now, the third vector of $$S_1$$ is a linear combination of the first two and we get

$$
S_2=\{\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ -1 \\ 1 \end{pmatrix} \}
$$

with the same span as $$S_1$$, and therefore the same span as $$S$$, but with one difference. The set $$S_2$$ is linearly independent (this is easily checked), and so discarding any of its elements will shrink the span.

### Linear Independence and Subset Relations

Theorem 1.12 describes producing a linearly independent set by shrinking, that is, by taking subsets. We finish this subsection by considering how linear independence and dependence, which are properties of sets, interact with the subset relation between sets.

**Lemma 1.14**

Any subset of a linearly independent set is also linearly independent. Any superset of a linearly dependent set is also linearly dependent.

**Proof**  —

This is clear.

Restated, independence is preserved by subset and dependence is preserved by superset.

Those are two of the four possible cases of interaction that we can consider. The third case, whether linear dependence is preserved by the subset operation, is covered by Example 1.13, which gives a linearly dependent set $$S$$ with a subset $$S_1$$ that is linearly dependent and another subset $$S_2$$ that is linearly independent.

That leaves one case, whether linear independence is preserved by superset. The next example shows what can happen.

**Example 1.15**  —

In each of these three paragraphs the subset $$S$$ is linearly independent.

For the set

$$
S =\{\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}\}
$$

the span $$[S]$$ is the $$x$$ axis. Here are two supersets of $$S$$, one linearly dependent and the other linearly independent.

dependent: $$\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} -3 \\ 0 \\ 0 \end{pmatrix}\}$$ independent: $$\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}\}$$

Checking the dependence or independence of these sets is easy.

For

$$
S =\{\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} \}
$$

the span $$[S]$$ is the $$xy$$ plane. These are two supersets.

dependent: $$\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 3 \\ -2 \\ 0 \end{pmatrix} \}$$ independent: $$\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \}$$

If

$$
S =\{\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \}
$$

then $$[S]=\mathbb{R}^3$$. A linearly dependent superset is

dependent: $$\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} \}$$

but there are no linearly independent supersets of $$S$$. The reason is that for any vector that we would add to make a superset, the linear dependence equation  

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} =c_1\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} +c_2\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} +c_3\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
$$

has a solution $$c_1=x$$, $$c_2=y$$, and $$c_3=z$$.

So, in general, a linearly independent set may have a superset that is dependent. And, in general, a linearly independent set may have a superset that is independent. We can characterize when the superset is one and when it is the other.

**Lemma 1.16**  —

Where $$S$$ is a linearly independent subset of a vector space $$V$$,

$$
S\cup\{\vec{v}\}\text{ is linearly dependent} \quad\text{if and only if}\quad \vec{v}\in[S]
$$

for any $$\vec{v}\in V$$ with $$\vec{v}\not\in S$$.

**Proof**  —

One implication is clear: if $$\vec{v}\in[S]$$ then $$\vec{v}=c_1\vec{s}_1+c_2\vec{s}_2+\cdots +c_n\vec{s}_n$$ where each $$\vec{s}_i\in S$$ and $$c_i\in\mathbb{R}$$, and so $$\vec{0}=c_1\vec{s}_1+c_2\vec{s}_2+\cdots +c_n\vec{s}_n+(-1)\vec{v}$$ is a nontrivial linear relationship among elements of $$S\cup\{\vec{v}\}$$.

The other implication requires the assumption that $$S$$ is linearly independent. With $$S\cup\{\vec{v}\}$$ linearly dependent, there is a nontrivial linear relationship $$c_0\vec{v}+c_1\vec{s}_1+c_2\vec{s}_2+\cdots +c_n\vec{s}_n=\vec{0}$$ and independence of $$S$$ then implies that $$c_0\neq 0$$, or else that would be a nontrivial relationship among members of $$S$$. Now rewriting this equation as $$\vec{v}=-(c_1/c_0)\vec{s}_1-\dots-(c_n/c_0)\vec{s}_n$$ shows that $$\vec{v}\in[S]$$.

(Compare this result with Lemma 1.1. Both say, roughly, that $$\vec{v}$$ is a "repeat" if it is in the span of $$S$$. However, note the additional hypothesis here of linear independence.)

**Corollary 1.17**  —

A subset $$S=\{\vec{s}_1,\dots,\vec{s}_n\}$$ of a vector space is linearly dependent if and only if some $$\vec{s_i}$$ is a linear combination of the vectors $$\vec{s}_1$$, ..., $$\vec{s}_{i-1}$$ listed before it.

**Proof**  —

Consider $$S_0=\{\}$$, $$S_1=\{\vec{s_1}\}$$, $$S_2=\{\vec{s}_1,\vec{s}_2 \}$$, etc. Some index $$i\geq 1$$ is the first one with $$S_{i-1}\cup\{\vec{s}_i \}$$ linearly dependent, and there $$\vec{s}_i\in[ S_{i-1} ]$$.

Lemma 1.16 can be restated in terms of independence instead of dependence: if $$S$$ is linearly independent and $$\vec{v}\not\in S$$ then the set $$S\cup\{\vec{v}\}$$ is also linearly independent if and only if $$\vec{v}\not\in[S].$$ Applying Lemma 1.1, we conclude that if $$S$$ is linearly independent and $$\vec{v}\not\in S$$ then $$S\cup\{\vec{v}\}$$ is also linearly independent if and only if $$[S\cup\{\vec{v}\}]\neq[S]$$. Briefly, when passing from $$S$$ to a superset $$S_1$$, to preserve linear independence we must expand the span $$[S_1]\supset[S]$$.

Example 1.15 shows that some linearly independent sets are maximal— have as many elements as possible— in that they have no supersets that are linearly independent. By the prior paragraph, a linearly independent sets is maximal if and only if it spans the entire space, because then no vector exists that is not already in the span.

This table summarizes the interaction between the properties of independence and dependence and the relations of subset and superset.  
- $$S_1\subset S$$  $$S_1\supset S$$
- *$$S$$ independent*

- $$S_1$$ must be independent  $$S_1$$ may be either
- $$S_1$$ may be either  $$S_1$$ must be dependent

- *$$S$$ dependent*  
In developing this table we've uncovered an intimate relationship between linear independence and span. Complementing the fact that a spanning set is minimal if and only if it is linearly independent, a linearly independent set is maximal if and only if it spans the space.

In summary, we have introduced the definition of linear independence to formalize the idea of the minimality of a spanning set. We have developed some properties of this idea. The most important is Lemma 1.16, which tells us that a linearly independent set is maximal when it spans the space.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Decide whether each subset of $$\mathbb{R}^3$$ is linearly dependent or linearly independent.

1. $$\{\begin{pmatrix} 1 \\ -3 \\ 5 \end{pmatrix}, \begin{pmatrix} 2 \\ 2 \\ 4 \end{pmatrix}, \begin{pmatrix} 4 \\ -4 \\ 14 \end{pmatrix} \}$$
2. $$\{\begin{pmatrix} 1 \\ 7 \\ 7 \end{pmatrix}, \begin{pmatrix} 2 \\ 7 \\ 7 \end{pmatrix}, \begin{pmatrix} 3 \\ 7 \\ 7 \end{pmatrix} \}$$
3. $$\{\begin{pmatrix} 0 \\ 0 \\ -1 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ 4 \end{pmatrix} \}$$
4. $$\{\begin{pmatrix} 9 \\ 9 \\ 0 \end{pmatrix}, \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 3 \\ 5 \\ -4 \end{pmatrix}, \begin{pmatrix} 12 \\ 12 \\ -1 \end{pmatrix} \}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Which of these subsets of $$\mathcal{P}_3$$ are linearly dependent and which are independent?

1. $$\{3-x+9x^2,5-6x+3x^2,1+1x-5x^2\}$$
2. $$\{-x^2,1+4x^2\}$$
3. $$\{2+x+7x^2,3-x+2x^2,4-3x^2\}$$
4. $$\{8+3x+3x^2,x+2x^2,2+2x+2x^2,8-2x+5x^2\}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

Prove that each set $$\{f,g\}$$ is linearly independent in the vector space of all functions from $$\mathbb{R}^+$$ to $$\mathbb{R}$$.

1. $$f(x)=x$$ and $$g(x)=1/x$$
2. $$f(x)=\cos(x)$$ and $$g(x)=\sin(x)$$
3. $$f(x)=e^x$$ and $$g(x)=\ln(x)$$  
*This exercise is recommended for all readers.*

**Problem 4**  —

Which of these subsets of the space of real-valued functions of one real variable is linearly dependent and which is linearly independent? (Note that we have abbreviated some constant functions; e.g., in the first item, the "$$2$$" stands for the constant function $$f(x)=2$$.)

1. $$\{2,4\sin^2(x),\cos^2(x)\}$$
2. $$\{1,\sin(x),\sin(2x)\}$$
3. $$\{x,\cos(x)\}$$
4. $$\{(1+x)^2,x^2+2x,3\}$$
5. $$\{\cos(2x),\sin^2(x),\cos^2(x)\}$$
6. $$\{0,x,x^2\}$$

**Problem 5**  —

Does the equation $$\sin^2(x)/\cos^2(x)=\tan^2(x)$$ show that this set of functions $$\{\sin^2(x),\cos^2(x),\tan^2(x)\}$$ is a linearly dependent subset of the set of all real-valued functions with domain the interval $$(-\pi/2..\pi/2)$$ of real numbers between $$-\pi/2$$ and $$\pi/2$$?

**Problem 6**  —

Why does Lemma 1.4 say "distinct"?  
*This exercise is recommended for all readers.*

**Problem 7**  —

Show that the nonzero rows of an echelon form matrix form a linearly independent set.  
*This exercise is recommended for all readers.*

**Problem 8**  —

1. Show that if the set $$\{\vec{u},\vec{v},\vec{w}\}$$ is linearly independent set then so is the set $$\{\vec{u},\vec{u}+\vec{v},\vec{u}+\vec{v}+\vec{w}\}$$.
2. What is the relationship between the linear independence or dependence of the set $$\{\vec{u},\vec{v},\vec{w}\}$$ and the independence or dependence of $$\{\vec{u}-\vec{v},\vec{v}-\vec{w},\vec{w}-\vec{u}\}$$?

**Problem 9**  —

Example 1.10 shows that the empty set is linearly independent.

1. When is a one-element set linearly independent?
2. How about a set with two elements?

**Problem 10**  —

In any vector space $$V$$, the empty set is linearly independent. What about all of $$V$$?

**Problem 11**  —

Show that if $$\{\vec{x},\vec{y},\vec{z}\}$$ is linearly independent then so are all of its proper subsets: $$\{\vec{x},\vec{y}\}$$, $$\{\vec{x},\vec{z}\}$$, $$\{\vec{y},\vec{z}\}$$, $$\{\vec{x}\}$$,$$\{\vec{y}\}$$, $$\{\vec{z}\}$$, and $$\{\}$$. Is that "only if" also?

**Problem 12**  —

1. Show that this

$$
S=\{\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix},\begin{pmatrix} -1 \\ 2 \\ 0 \end{pmatrix}\}
$$

is a linearly independent subset of $$\mathbb{R}^3$$.
2. Show that

$$
\begin{pmatrix} 3 \\ 2 \\ 0 \end{pmatrix}
$$

is in the span of $$S$$ by finding $$c_1$$ and $$c_2$$ giving a linear relationship.

$$
c_1\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} +c_2\begin{pmatrix} -1 \\ 2 \\ 0 \end{pmatrix} =\begin{pmatrix} 3 \\ 2 \\ 0 \end{pmatrix}
$$

Show that the pair $$c_1,c_2$$ is unique.
3. Assume that $$S$$ is a subset of a vector space and that $$\vec{v}$$ is in $$[S]$$, so that $$\vec{v}$$ is a linear combination of vectors from $$S$$. Prove that if $$S$$ is linearly independent then a linear combination of vectors from $$S$$ adding to $$\vec{v}$$ is unique (that is, unique up to reordering and adding or taking away terms of the form $$0\cdot\vec{s}$$). Thus $$S$$ as a spanning set is minimal in this strong sense: each vector in $$[S]$$ is "hit" a minimum number of times— only once.
4. Prove that it can happen when $$S$$ is not linearly independent that distinct linear combinations sum to the same vector.

**Problem 13**  —

Prove that a polynomial gives rise to the zero function if and only if it is the zero polynomial. (*Comment.* This question is not a Linear Algebra matter, but we often use the result. A polynomial gives rise to a function in the obvious way: $$x\mapsto c_nx^n+\dots+c_1x+c_0$$.)

**Problem 14**  —

Return to Section 1.2 and redefine point, line, plane, and other linear surfaces to avoid degenerate cases.

**Problem 15**  —

1. Show that any set of four vectors in $$\mathbb{R}^2$$ is linearly dependent.
2. Is this true for any set of five? Any set of three?
3. What is the most number of elements that a linearly independent subset of $$\mathbb{R}^2$$ can have?  
*This exercise is recommended for all readers.*

**Problem 16**  —

Is there a set of four vectors in $$\mathbb{R}^3$$, any three of which form a linearly independent set?

**Problem 17**  —

Must every linearly dependent set have a subset that is dependent and a subset that is independent?

**Problem 18**  —

In $$\mathbb{R}^4$$, what is the biggest linearly independent set you can find? The smallest? The biggest linearly dependent set? The smallest? ("Biggest" and "smallest" mean that there are no supersets or subsets with the same property.)  
*This exercise is recommended for all readers.*

**Problem 19**  —

Linear independence and linear dependence are properties of sets. We can thus naturally ask how those properties act with respect to the familiar elementary set relations and operations. In this body of this subsection we have covered the subset and superset relations. We can also consider the operations of intersection, complementation, and union.

1. How does linear independence relate to intersection: can an intersection of linearly independent sets be independent? Must it be?
2. How does linear independence relate to complementation?
3. Show that the union of two linearly independent sets need not be linearly independent.
4. Characterize when the union of two linearly independent sets is linearly independent, in terms of the intersection of the span of each.  
*This exercise is recommended for all readers.*

**Problem 20**  —

For Theorem 1.12,

1. fill in the induction for the proof;
2. give an alternate proof that starts with the empty set and builds a sequence of linearly independent subsets of the given finite set until one appears with the same span as the given set.

**Problem 21**  —

With a little calculation we can get formulas to determine whether or not a set of vectors is linearly independent.

1. Show that this subset of $$\mathbb{R}^2$$

$$
\{\begin{pmatrix} a \\ c \end{pmatrix},\begin{pmatrix} b \\ d \end{pmatrix}\}
$$

is linearly independent if and only if $$ad-bc\neq 0$$.
2. Show that this subset of $$\mathbb{R}^3$$

$$
\{\begin{pmatrix} a \\ d \\ g \end{pmatrix}, \begin{pmatrix} b \\ e \\ h \end{pmatrix}, \begin{pmatrix} c \\ f \\ i \end{pmatrix} \}
$$

is linearly independent iff $$aei+bfg+cdh-hfa-idb-gec \neq 0$$.
3. When is this subset of $$\mathbb{R}^3$$

$$
\{\begin{pmatrix} a \\ d \\ g \end{pmatrix}, \begin{pmatrix} b \\ e \\ h \end{pmatrix} \}
$$

linearly independent?
4. This is an opinion question: for a set of four vectors from $$\mathbb{R}^4$$, must there be a formula involving the sixteen entries that determines independence of the set? (You needn't produce such a formula, just decide if one exists.)  
*This exercise is recommended for all readers.*

**Problem 22**  —

1. Prove that a set of two perpendicular nonzero vectors from $$\mathbb{R}^n$$ is linearly independent when $$n>1$$.
2. What if $$n=1$$? $$n=0$$?
3. Generalize to more than two vectors.

**Problem 23**  —

Consider the set of functions from the open interval $$(-1..1)$$ to $$\mathbb{R}$$.

1. Show that this set is a vector space under the usual operations.
2. Recall the formula for the sum of an infinite geometric series: $$1+x+x^2+\cdots=1/(1-x)$$ for all $$x\in(-1..1)$$. Why does this not express a dependence inside of the set $$\{g(x)=1/(1-x),f_0(x)=1,f_1(x)=x,f_2(x)=x^2,\ldots\}$$ (in the vector space that we are considering)? (*Hint.* Review the definition of linear combination.)
3. Show that the set in the prior item is linearly independent.

This shows that some vector spaces exist with linearly independent subsets that are infinite.

**Problem 24**  —

Show that, where $$S$$ is a subspace of $$V$$, if a subset $$T$$ of $$S$$ is linearly independent in $$S$$ then $$T$$ is also linearly independent in $$V$$. Is that "only if"?

Solutions

---

*Source: Wikibooks, Linear Algebra/Definition and Examples of Linear Independence (https://en.wikibooks.org/wiki/Linear_Algebra/Definition_and_Examples_of_Linear_Independence), by Wikibooks contributors, CC BY-SA 4.0.*
