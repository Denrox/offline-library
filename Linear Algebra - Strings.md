# Strings

*This subsection is optional, and requires material from the optional Direct Sum subsection.*

The prior subsection shows that as $$j$$ increases, the dimensions of the $$\mathcal{R}(t^j)$$'s fall while the dimensions of the $$\mathcal{N}(t^j)$$'s rise, in such a way that this rank and nullity split the dimension of $$V$$. Can we say more; do the two split a basis— is $$V=\mathcal{R}(t^j)\oplus\mathcal{N}(t^j)$$?

The answer is yes for the smallest power $$j=0$$ since $$V=\mathcal{R}(t^0)\oplus\mathcal{N}(t^0)=V\oplus\{\vec{0}\}$$. The answer is also yes at the other extreme.

**Lemma 2.1**  —

Where $$t:V\to V$$ is a linear transformation, the space is the direct sum $$V=\mathcal{R}_\infty(t)\oplus\mathcal{N}_\infty(t)$$. That is, both $$\dim(V)=\dim(\mathcal{R}_\infty(t))+\dim(\mathcal{N}_\infty(t))$$ and $$\mathcal{R}_\infty(t)\cap\mathcal{N}_\infty(t)=\{\vec{0}\,\}$$.

**Proof**  —

We will verify the second sentence, which is equivalent to the first. The first clause, that the dimension $$n$$ of the domain of $$t^n$$ equals the rank of $$t^n$$ plus the nullity of $$t^n$$, holds for any transformation and so we need only verify the second clause.

Assume that $$\vec{v}\in\mathcal{R}_\infty(t)\cap\mathcal{N}_\infty(t) =\mathcal{R}(t^n)\cap\mathcal{N}(t^n)$$, to prove that $$\vec{v}$$ is $$\vec{0}$$. Because $$\vec{v}$$ is in the nullspace, $$t^n(\vec{v})=\vec{0}$$. On the other hand, because $$\mathcal{R}(t^n)=\mathcal{R}(t^{n+1})$$, the map $$t:\mathcal{R}_\infty(t)\to \mathcal{R}_\infty(t)$$ is a dimension-preserving homomorphism and therefore is one-to-one. A composition of one-to-one maps is one-to-one, and so $$t^n:\mathcal{R}_\infty(t)\to \mathcal{R}_\infty(t)$$ is one-to-one. But now— because only $$\vec{0}$$ is sent by a one-to-one linear map to $$\vec{0}$$— the fact that $$t^n(\vec{v})=\vec{0}$$ implies that $$\vec{v}=\vec{0}$$.

**Note 2.2**  —

Technically we should distinguish the map $$t:V\to V$$ from the map $$t:\mathcal{R}_\infty(t)\to \mathcal{R}_\infty(t)$$ because the domains or codomains might differ. The second one is said to be the **restriction** of $$t$$ to $$\mathcal{R}(t^k)$$. We shall use later a point from that proof about the restriction map, namely that it is nonsingular.

In contrast to the $$j=0$$ and $$j=n$$ cases, for intermediate powers the space $$V$$ might not be the direct sum of $$\mathcal{R}(t^j)$$ and $$\mathcal{N}(t^j)$$. The next example shows that the two can have a nontrivial intersection.

**Example 2.3**  —

Consider the transformation of $$\mathbb{C}^2$$ defined by this action on the elements of the standard basis.

$$
\begin{pmatrix} 1 \\ 0 \end{pmatrix} \stackrel{n}{\longmapsto} \begin{pmatrix} 0 \\ 1 \end{pmatrix} \quad \begin{pmatrix} 0 \\ 1 \end{pmatrix} \stackrel{n}{\longmapsto} \begin{pmatrix} 0 \\ 0 \end{pmatrix} \qquad N={\rm Rep}_{\mathcal{E}_2,\mathcal{E}_2}(n)=\begin{pmatrix} 0 &0 \\ 1 &0 \end{pmatrix}
$$

The vector

$$
\vec{e}_2=\begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

is in both the rangespace and nullspace. Another way to depict this map's action is with a **string**.

$$
\begin{array}{ccccc} \vec{e}_1 &\mapsto &\vec{e}_2 &\mapsto &\vec{0} \end{array}
$$

**Example 2.4**  —

A map $$\hat{n}:\mathbb{C}^4\to \mathbb{C}^4$$ whose action on $$\mathcal{E}_4$$ is given by the string

$$
\begin{array}{ccccccccc} \vec{e}_1 &\mapsto &\vec{e}_2 &\mapsto &\vec{e}_3 &\mapsto &\vec{e}_4 &\mapsto &\vec{0} \end{array}
$$

has $$\mathcal{R}(\hat{n})\cap\mathcal{N}(\hat{n})$$ equal to the span $$[\{\vec{e}_4\}]$$, has $$\mathcal{R}(\hat{n}^2)\cap\mathcal{N}(\hat{n}^2)= [\{\vec{e}_3,\vec{e}_4\}]$$, and has $$\mathcal{R}(\hat{n}^3)\cap\mathcal{N}(\hat{n}^3)= [\{\vec{e}_4\}]$$. The matrix representation is all zeros except for some subdiagonal ones.

$$
\hat{N}={\rm Rep}_{\mathcal{E}_4,\mathcal{E}_4}(\hat{n}) =\begin{pmatrix} 0 &0 &0 &0 \\ 1 &0 &0 &0 \\ 0 &1 &0 &0 \\ 0 &0 &1 &0 \end{pmatrix}
$$

**Example 2.5**  —

Transformations can act via more than one string. A transformation $$t$$ acting on a basis $$B=\langle \vec{\beta}_1,\dots,\vec{\beta}_5 \rangle$$ by

$$
\begin{array}{ccccccc} \vec{\beta}_1 &\mapsto &\vec{\beta}_2 &\mapsto &\vec{\beta}_3 &\mapsto &\vec{0} \\ \vec{\beta}_4 &\mapsto &\vec{\beta}_5 &\mapsto &\vec{0} \end{array}
$$

is represented by a matrix that is all zeros except for blocks of subdiagonal ones

$$
{\rm Rep}_{B,B}(t)= \left(\begin{array}{ccc|cc} 0 &0 &0 &0 &0 \\ 1 &0 &0 &0 &0 \\ 0 &1 &0 &0 &0 \\ \hline 0 &0 &0 &0 &0 \\ 0 &0 &0 &1 &0 \end{array}\right)
$$

(the lines just visually organize the blocks).

In those three examples all vectors are eventually transformed to zero.

**Definition 2.6**  —

A **nilpotent** transformation is one with a power that is the zero map. A **nilpotent matrix** is one with a power that is the zero matrix. In either case, the least such power is the **index of nilpotency**.

**Example 2.7**  —

In Example 2.3 the index of nilpotency is two. In Example 2.4 it is four. In Example 2.5 it is three.

**Example 2.8**  —

The differentiation map $$d/dx:\mathcal{P}_2\to \mathcal{P}_2$$ is nilpotent of index three since the third derivative of any quadratic polynomial is zero. This map's action is described by the string $$x^2\mapsto 2x\mapsto 2\mapsto 0$$ and taking the basis $$B=\langle x^2,2x,2 \rangle$$ gives this representation.

$$
{\rm Rep}_{B,B}(d/dx)= \begin{pmatrix} 0 &0 &0 \\ 1 &0 &0 \\ 0 &1 &0 \end{pmatrix}
$$

Not all nilpotent matrices are all zeros except for blocks of subdiagonal ones.

**Example 2.9**  —

With the matrix $$\hat{N}$$ from Example 2.4, and this four-vector basis

$$
D=\langle \begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 2 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix} \rangle
$$

a change of basis operation produces this representation with respect to $$D,D$$.

$$
\begin{pmatrix} 1 &0 &1 &0 \\ 0 &2 &1 &0 \\ 1 &1 &1 &0 \\ 0 &0 &0 &1 \end{pmatrix} \begin{pmatrix} 0 &0 &0 &0 \\ 1 &0 &0 &0 \\ 0 &1 &0 &0 \\ 0 &0 &1 &0 \end{pmatrix} \begin{pmatrix} 1 &0 &1 &0 \\ 0 &2 &1 &0 \\ 1 &1 &1 &0 \\ 0 &0 &0 &1 \end{pmatrix}^{-1}\!\! = \begin{pmatrix} -1 &0 &1 &0 \\ -3 &-2 &5 &0 \\ -2 &-1 &3 &0 \\ 2 &1 &-2 &0 \end{pmatrix}
$$

The new matrix is nilpotent; it's fourth power is the zero matrix since

$$
(P\hat{N}P^{-1})^4 =P\hat{N}P^{-1}\cdot P\hat{N}P^{-1}\cdot P\hat{N}P^{-1}\cdot P\hat{N}P^{-1} =P\hat{N}^4P^{-1}
$$

and $$\hat{N}^4$$ is the zero matrix.

The goal of this subsection is Theorem 2.13, which shows that the prior example is prototypical in that every nilpotent matrix is similar to one that is all zeros except for blocks of subdiagonal ones.

**Definition 2.10**  —

Let $$t$$ be a nilpotent transformation on $$V$$. A **$$t$$-string generated by** $$\vec{v}\in V$$ is a sequence $$\langle \vec{v},t(\vec{v}),\ldots,t^{k-1}(\vec{v}) \rangle$$. This sequence has **length** $$k$$. A **$$t$$-string basis** is a basis that is a concatenation of $$t$$-strings.

**Example 2.11**  —

In Example 2.5, the $$t$$-strings $$\langle \vec{\beta}_1,\vec{\beta}_2,\vec{\beta}_3 \rangle$$ and $$\langle \vec{\beta}_4,\vec{\beta}_5 \rangle$$, of length three and two, can be concatenated to make a basis for the domain of $$t$$.

**Lemma 2.12**  —

If a space has a $$t$$-string basis then the longest string in it has length equal to the index of nilpotency of $$t$$.

**Proof**  —

Suppose not. Those strings cannot be longer; if the index is $$k$$ then $$t^k$$ sends any vector— including those starting the string— to $$\vec{0}$$. So suppose instead that there is a transformation $$t$$ of index $$k$$ on some space, such that the space has a $$t$$-string basis where all of the strings are shorter than length $$k$$. Because $$t$$ has index $$k$$, there is a vector $$\vec{v}$$ such that $$t^{k-1}(\vec{v})\neq\vec{0}$$. Represent $$\vec{v}$$ as a linear combination of basis elements and apply $$t^{k-1}$$. We are supposing that $$t^{k-1}$$ sends each basis element to $$\vec{0}$$ but that it does not send $$\vec{v}$$ to $$\vec{0}$$. That is impossible.

We shall show that every nilpotent map has an associated string basis. Then our goal theorem, that every nilpotent matrix is similar to one that is all zeros except for blocks of subdiagonal ones, is immediate, as in Example 2.5.

Looking for a counterexample, a nilpotent map without an associated string basis that is disjoint, will suggest the idea for the proof. Consider the map $$t:\mathbb{C}^5\to \mathbb{C}^5$$ with this action.

$$
{\rm Rep}_{\mathcal{E}_5,\mathcal{E}_5}(t)= \begin{pmatrix} 0 &0 &0 &0 &0 \\ 0 &0 &0 &0 &0 \\ 1 &1 &0 &0 &0 \\ 0 &0 &0 &0 &0 \\ 0 &0 &0 &1 &0 \end{pmatrix}
$$

Even after omitting the zero vector, these three strings aren't disjoint, but that doesn't end hope of finding a $$t$$-string basis. It only means that $$\mathcal{E}_5$$ will not do for the string basis.

To find a basis that will do, we first find the number and lengths of its strings. Since $$t$$'s index of nilpotency is two, Lemma 2.12 says that at least one string in the basis has length two. Thus the map must act on a string basis in one of these two ways.  
$$\begin{array}{ccccc} \vec{\beta}_1 &\mapsto &\vec{\beta}_2 &\mapsto &\vec{0} \\ \vec{\beta}_3 &\mapsto &\vec{\beta}_4 &\mapsto &\vec{0} \\ \vec{\beta}_5 &\mapsto &\vec{0} \end{array}$$ $$\begin{array}{ccccc} \vec{\beta}_1 &\mapsto &\vec{\beta}_2 &\mapsto &\vec{0} \\ \vec{\beta}_3 &\mapsto &\vec{0} \\ \vec{\beta}_4 &\mapsto &\vec{0} \\ \vec{\beta}_5 &\mapsto &\vec{0} \end{array}$$

Now, the key point. A transformation with the left-hand action has a nullspace of dimension three since that's how many basis vectors are sent to zero. A transformation with the right-hand action has a nullspace of dimension four. Using the matrix representation above, calculation of $$t$$'s nullspace

$$
\mathcal{N}(t)= \{\begin{pmatrix} x \\ -x \\ z \\ 0 \\ r \end{pmatrix}\,\big|\, x,z,r\in\mathbb{C} \}
$$

shows that it is three-dimensional, meaning that we want the left-hand action.

To produce a string basis, first pick $$\vec{\beta}_2$$ and $$\vec{\beta}_4$$ from $$\mathcal{R}(t)\cap\mathcal{N}(t)$$

$$
\vec{\beta}_2=\begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}\qquad \vec{\beta}_4=\begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}
$$

(other choices are possible, just be sure that $$\{\vec{\beta}_2,\vec{\beta}_4\}$$ is linearly independent). For $$\vec{\beta}_5$$ pick a vector from $$\mathcal{N}(t)$$ that is not in the span of $$\{ \vec{\beta}_2,\vec{\beta}_4 \}$$.

$$
\vec{\beta}_5=\begin{pmatrix} 1 \\ -1 \\ 0 \\ 0 \\ 0 \end{pmatrix}
$$

Finally, take $$\vec{\beta}_1$$ and $$\vec{\beta}_3$$ such that $$t(\vec{\beta}_1)=\vec{\beta}_2$$ and $$t(\vec{\beta}_3)=\vec{\beta}_4$$.

$$
\vec{\beta}_1=\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}\qquad \vec{\beta}_3=\begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}
$$

Now, with respect to $$B=\langle \vec{\beta}_1,\ldots,\vec{\beta}_5 \rangle$$, the matrix of $$t$$ is as desired.

$$
{\rm Rep}_{B,B}(t)= \left(\begin{array}{cc|cc|c} 0 &0 &0 &0 &0 \\ 1 &0 &0 &0 &0 \\ \hline 0 &0 &0 &0 &0 \\ 0 &0 &1 &0 &0 \\ \hline 0 &0 &0 &0 &0 \end{array}\right)
$$

**Theorem 2.13**  —

Any nilpotent transformation $$t$$ is associated with a $$t$$-string basis. While the basis is not unique, the number and the length of the strings is determined by $$t$$.

This illustrates the proof. Basis vectors are categorized into kind $$1$$, kind $$2$$, and kind $$3$$. They are also shown as squares or circles, according to whether they are in the nullspace or not.  
**Proof**  —

Fix a vector space $$V$$; we will argue by induction on the index of nilpotency of $$t:V\to V$$. If that index is $$1$$ then $$t$$ is the zero map and any basis is a string basis $$\vec{\beta}_1\mapsto\vec{0}$$, ..., $$\vec{\beta}_n\mapsto\vec{0}$$. For the inductive step, assume that the theorem holds for any transformation with an index of nilpotency between $$1$$ and $$k-1$$ and consider the index $$k$$ case.

First observe that the restriction to the rangespace $$t:\mathcal{R}(t)\to \mathcal{R}(t)$$ is also nilpotent, of index $$k-1$$. Apply the inductive hypothesis to get a string basis for $$\mathcal{R}(t)$$, where the number and length of the strings is determined by $$t$$.

$$
B=\langle \vec{\beta}_1,t(\vec{\beta}_1),\dots, t^{h_1}(\vec{\beta}_1) \rangle \!\mathbin{{}^\frown}\! \langle \vec{\beta}_2,\ldots,t^{h_2}(\vec{\beta}_2) \rangle \!\mathbin{{}^\frown}\!\cdots\!\mathbin{{}^\frown}\! \langle \vec{\beta}_i,\ldots,t^{h_i}(\vec{\beta}_i) \rangle
$$

(In the illustration these are the basis vectors of kind $$1$$, so there are $$i$$ strings shown with this kind of basis vector.)

Second, note that taking the final nonzero vector in each string gives a basis $$C=\langle t^{h_1}(\vec{\beta}_1),\dots,t^{h_i}(\vec{\beta}_i) \rangle$$ for $$\mathcal{R}(t)\cap\mathcal{N}(t)$$. (These are illustrated with $$1$$'s in squares.) For, a member of $$\mathcal{R}(t)$$ is mapped to zero if and only if it is a linear combination of those basis vectors that are mapped to zero. Extend $$C$$ to a basis for all of $$\mathcal{N}(t)$$.

$$
\hat{C}=C\!\mathbin{{}^\frown}\!\langle \vec{\xi}_1,\dots,\vec{\xi}_p \rangle
$$

(The $$\vec{\xi}$$'s are the vectors of kind $$2$$ so that $$\hat{C}$$ is the set of squares.) While many choices are possible for the $$\vec{\xi}$$'s, their number $$p$$ is determined by the map $$t$$ as it is the dimension of $$\mathcal{N}(t)$$ minus the dimension of $$\mathcal{R}(t)\cap\mathcal{N}(t)$$.

Finally, $$B\!\mathbin{{}^\frown}\!\hat{C}$$ is a basis for $$\mathcal{R}(t)+\mathcal{N}(t)$$ because any sum of something in the rangespace with something in the nullspace can be represented using elements of $$B$$ for the rangespace part and elements of $$\hat{C}$$ for the part from the nullspace. Note that

$$
\begin{array}{rl} \dim\big(\mathcal{R}(t)+\mathcal{N}(t)\big) &= \dim (\mathcal{R}(t))+\dim (\mathcal{N}(t)) -\dim(\mathcal{R}(t)\cap\mathcal{N}(t)) \\ &= \mathop{\text{rank}} (t)+\text{nullity}\, (t)-i \\ &= \dim (V)-i \end{array}
$$

and so $$B\!\mathbin{{}^\frown}\!\hat{C}$$ can be extended to a basis for all of $$V$$ by the addition of $$i$$ more vectors. Specifically, remember that each of $$\vec{\beta}_1,\dots,\vec{\beta}_i$$ is in $$\mathcal{R}(t)$$, and extend $$B\!\mathbin{{}^\frown}\!\hat{C}$$ with vectors $$\vec{v}_1,\dots,\vec{v}_i$$ such that $$t(\vec{v}_1)=\vec{\beta}_1,\dots,t(\vec{v}_i)=\vec{\beta}_i$$. (In the illustration, these are the $$3$$'s.) The check that linear independence is preserved by this extension is Problem 13.

**Corollary 2.14**  —

Every nilpotent matrix is similar to a matrix that is all zeros except for blocks of subdiagonal ones. That is, every nilpotent map is represented with respect to some basis by such a matrix.

This form is unique in the sense that if a nilpotent matrix is similar to two such matrices then those two simply have their blocks ordered differently. Thus this is a canonical form for the similarity classes of nilpotent matrices provided that we order the blocks, say, from longest to shortest.

**Example 2.15**  —

The matrix

$$
M=\begin{pmatrix} 1 &-1 \\ 1 &-1 \end{pmatrix}
$$

has an index of nilpotency of two, as this calculation shows.

$$
\begin{array}{c|cc} p & M^p & \mathcal{N}(M^p) \\ \hline 1 & M=\begin{pmatrix} 1 &-1 \\ 1 &-1 \end{pmatrix} & \{\begin{pmatrix} x \\ x \end{pmatrix}\,\big|\, x\in\mathbb{C}\} \\ 2 & M^2=\begin{pmatrix} 0 &0 \\ 0 &0 \end{pmatrix} & \mathbb{C}^2 \end{array}
$$

The calculation also describes how a map $$m$$ represented by $$M$$ must act on any string basis. With one map application the nullspace has dimension one and so one vector of the basis is sent to zero. On a second application, the nullspace has dimension two and so the other basis vector is sent to zero. Thus, the action of the map is $$\vec{\beta}_1\mapsto\vec{\beta}_2\mapsto\vec{0}$$ and the canonical form of the matrix is this.

$$
\begin{pmatrix} 0 &0 \\ 1 &0 \end{pmatrix}
$$

We can exhibit such a $$m$$-string basis and the change of basis matrices witnessing the matrix similarity. For the basis, take $$M$$ to represent $$m$$ with respect to the standard bases, pick a $$\vec{\beta}_2\in\mathcal{N}(m)$$ and also pick a $$\vec{\beta}_1$$ so that $$m(\vec{\beta}_1)=\vec{\beta}_2$$.

$$
\vec{\beta}_2=\begin{pmatrix} 1 \\ 1 \end{pmatrix} \qquad \vec{\beta}_1=\begin{pmatrix} 1 \\ 0 \end{pmatrix}
$$

(If we take $$M$$ to be a representative with respect to some nonstandard bases then this picking step is just more messy.) Recall the similarity diagram.  
The canonical form equals $${\rm Rep}_{B,B}(m)=PMP^{-1}$$, where

$$
P^{-1} ={\rm Rep}_{B,\mathcal{E}_2}(\text{id}) =\begin{pmatrix} 1 &1 \\ 0 &1 \end{pmatrix} \qquad P=(P^{-1})^{-1} =\begin{pmatrix} 1 &-1 \\ 0 &1 \end{pmatrix}
$$

and the verification of the matrix calculation is routine.

$$
\begin{pmatrix} 1 &-1 \\ 0 &1 \end{pmatrix} \begin{pmatrix} 1 &-1 \\ 1 &-1 \end{pmatrix} \begin{pmatrix} 1 &1 \\ 0 &1 \end{pmatrix}= \begin{pmatrix} 0 &0 \\ 1 &0 \end{pmatrix}
$$

**Example 2.16**  —

The matrix

$$
\begin{pmatrix} 0 &0 &0 &0 &0 \\ 1 &0 &0 &0 &0 \\ -1 &1 &1 &-1 &1 \\ 0 &1 &0 &0 &0 \\ 1 &0 &-1 &1 &-1 \end{pmatrix}
$$

is nilpotent. These calculations show the nullspaces growing.

$$
\begin{array}{c|cc} p & N^p & \mathcal{N}(N^p) \\ \hline 1 &\begin{pmatrix} 0 &0 &0 &0 &0 \\ 1 &0 &0 &0 &0 \\ -1 &1 &1 &-1 &1 \\ 0 &1 &0 &0 &0 \\ 1 &0 &-1 &1 &-1 \end{pmatrix} & \{\begin{pmatrix} 0 \\ 0 \\ u-v \\ u \\ v \end{pmatrix} \,\big|\, u,v\in\mathbb{C}\} \\ 2 &\begin{pmatrix} 0 &0 &0 &0 &0 \\ 0 &0 &0 &0 &0 \\ 1 &0 &0 &0 &0 \\ 1 &0 &0 &0 &0 \\ 0 &0 &0 &0 &0 \end{pmatrix} & \{\begin{pmatrix} 0 \\ y \\ z \\ u \\ v \end{pmatrix} \,\big|\, y,z,u,v\in\mathbb{C}\} \\ 3 &\textit{--zero matrix--} & \mathbb{C}^5 \end{array}
$$

That table shows that any string basis must satisfy: the nullspace after one map application has dimension two so two basis vectors are sent directly to zero, the nullspace after the second application has dimension four so two additional basis vectors are sent to zero by the second iteration, and the nullspace after three applications is of dimension five so the final basis vector is sent to zero in three hops.

$$
\begin{array}{ccccccc} \vec{\beta}_1 &\mapsto &\vec{\beta}_2 &\mapsto &\vec{\beta}_3 &\mapsto &\vec{0} \\ \vec{\beta}_4 &\mapsto &\vec{\beta}_5 &\mapsto &\vec{0} \end{array}
$$

To produce such a basis, first pick two independent vectors from $$\mathcal{N}(n)$$

$$
\vec{\beta}_3=\begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \\ 0 \end{pmatrix} \quad \vec{\beta}_5=\begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \\ 1 \end{pmatrix}
$$

then add $$\vec{\beta}_2,\vec{\beta}_4\in\mathcal{N}(n^2)$$ such that $$n(\vec{\beta}_2)=\vec{\beta}_3$$ and $$n(\vec{\beta}_4)=\vec{\beta}_5$$

$$
\vec{\beta}_2=\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} \quad \vec{\beta}_4=\begin{pmatrix} 0 \\ 1 \\ 0 \\ 1 \\ 0 \end{pmatrix}
$$

and finish by adding $$\vec{\beta}_1\in\mathcal{N}(n^3)=\mathbb{C}^5$$) such that $$n(\vec{\beta}_1)=\vec{\beta}_2$$.

$$
\vec{\beta}_1=\begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}
$$

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

What is the index of nilpotency of the **left-shift** operator, here acting on the space of triples of reals?

$$
(x,y,z)\mapsto(0,x,y)
$$

*This exercise is recommended for all readers.*

**Problem 2**  —

For each string basis state the index of nilpotency and give the dimension of the rangespace and nullspace of each iteration of the nilpotent map.

1. $$\begin{array}{ccccccc} \vec{\beta}_1 &\mapsto &\vec{\beta}_2 &\mapsto &\vec{0} \\ \vec{\beta}_3 &\mapsto &\vec{\beta}_4 &\mapsto &\vec{0} \end{array}$$
2. $$\begin{array}{ccccccc} \vec{\beta}_1 &\mapsto &\vec{\beta}_2 &\mapsto &\vec{\beta}_3 &\mapsto &\vec{0} \\ \vec{\beta}_4 &\mapsto &\vec{0} \\ \vec{\beta}_5 &\mapsto &\vec{0} \\ \vec{\beta}_6 &\mapsto &\vec{0} \end{array}$$
3. $$\begin{array}{ccccccccc} \vec{\beta}_1 &\mapsto &\vec{\beta}_2 &\mapsto &\vec{\beta}_3 &\mapsto &\vec{0} \end{array}$$

Also give the canonical form of the matrix.

**Problem 3**  —

Decide which of these matrices are nilpotent.

1. $$\begin{pmatrix} -2 &4 \\ -1 &2 \end{pmatrix}$$
2. $$\begin{pmatrix} 3 &1 \\ 1 &3 \end{pmatrix}$$
3. $$\begin{pmatrix} -3 &2 &1 \\ -3 &2 &1 \\ -3 &2 &1 \end{pmatrix}$$
4. $$\begin{pmatrix} 1 &1 &4 \\ 3 &0 &-1 \\ 5 &2 &7 \end{pmatrix}$$
5. $$\begin{pmatrix} 45 &-22 &-19 \\ 33 &-16 &-14 \\ 69 &-34 &-29 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 4**  —

Find the canonical form of this matrix.

$$
\begin{pmatrix} 0 &1 &1 &0 &1 \\ 0 &0 &1 &1 &1 \\ 0 &0 &0 &0 &0 \\ 0 &0 &0 &0 &0 \\ 0 &0 &0 &0 &0 \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 5**  —

Consider the matrix from Example 2.16.

1. Use the action of the map on the string basis to give the canonical form.
2. Find the change of basis matrices that bring the matrix to canonical form.
3. Use the answer in the prior item to check the answer in the first item.  
*This exercise is recommended for all readers.*

**Problem 6**  —

Each of these matrices is nilpotent.

1. $$\begin{pmatrix} 1/2 &-1/2 \\ 1/2 &-1/2 \end{pmatrix}$$
2. $$\begin{pmatrix} 0 &0 &0 \\ 0 &-1 &1 \\ 0 &-1 &1 \end{pmatrix}$$
3. $$\begin{pmatrix} -1 &1 &-1 \\ 1 &0 &1 \\ 1 &-1 &1 \end{pmatrix}$$

Put each in canonical form.

**Problem 7**  —

Describe the effect of left or right multiplication by a matrix that is in the canonical form for nilpotent matrices.

**Problem 8**  —

Is nilpotence invariant under similarity? That is, must a matrix similar to a nilpotent matrix also be nilpotent? If so, with the same index?  
*This exercise is recommended for all readers.*

**Problem 9**  —

Show that the only eigenvalue of a nilpotent matrix is zero.

**Problem 10**  —

Is there a nilpotent transformation of index three on a two-dimensional space?

**Problem 11**  —

In the proof of Theorem 2.13, why isn't the proof's base case that the index of nilpotency is zero?  
*This exercise is recommended for all readers.*

**Problem 12**  —

Let $$t:V\to V$$ be a linear transformation and suppose $$\vec{v}\in V$$ is such that $$t^k(\vec{v})=\vec{0}$$ but $$t^{k-1}(\vec{v})\neq\vec{0}$$. Consider the $$t$$-string $$\langle \vec{v},t(\vec{v}),\dots,t^{k-1}(\vec{v}) \rangle$$.

1. Prove that $$t$$ is a transformation on the span of the set of vectors in the string, that is, prove that $$t$$ restricted to the span has a range that is a subset of the span. We say that the span is a **$$t$$-invariant** subspace.
2. Prove that the restriction is nilpotent.
3. Prove that the $$t$$-string is linearly independent and so is a basis for its span.
4. Represent the restriction map with respect to the $$t$$-string basis.

**Problem 13**  —

Finish the proof of Theorem 2.13.

**Problem 14**  —

Show that the terms "nilpotent transformation" and "nilpotent matrix", as given in Definition 2.6, fit with each other: a map is nilpotent if and only if it is represented by a nilpotent matrix. (Is it that a transformation is nilpotent if an only if there is a basis such that the map's representation with respect to that basis is a nilpotent matrix, or that any representation is a nilpotent matrix?)

**Problem 15**  —

Let $$T$$ be nilpotent of index four. How big can the rangespace of $$T^3$$ be?

**Problem 16**  —

Recall that similar matrices have the same eigenvalues. Show that the converse does not hold.

**Problem 17**  —

Prove a nilpotent matrix is similar to one that is all zeros except for blocks of super-diagonal ones.  
*This exercise is recommended for all readers.*

**Problem 18**  —

Prove that if a transformation has the same rangespace as nullspace. then the dimension of its domain is even.

**Problem 19**  —

Prove that if two nilpotent matrices commute then their product and sum are also nilpotent.

**Problem 20**  —

Consider the transformation of $$\mathcal{M}_{n \! \times \! n}$$ given by $$t_S(T)=ST-TS$$ where $$S$$ is an $$n \! \times \! n$$ matrix. Prove that if $$S$$ is nilpotent then so is $$t_S$$.

**Problem 21**  —

Show that if $$N$$ is nilpotent then $$I-N$$ is invertible. Is that "only if" also?

Solutions

### References

---

*Source: Wikibooks, Linear Algebra/Strings (https://en.wikibooks.org/wiki/Linear_Algebra/Strings), by Wikibooks contributors, CC BY-SA 4.0.*
