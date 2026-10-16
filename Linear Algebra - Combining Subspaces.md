# Combining Subspaces

*This subsection is optional. It is required only for the last sections of Chapter Three and Chapter Five and for occasional exercises, and can be passed over without loss of continuity.*

This chapter opened with the definition of a vector space, and the middle consisted of a first analysis of the idea. This subsection closes the chapter by finishing the analysis, in the sense that "analysis" means "method of determining the ... essential features of something by separating it into parts" (Halsey 1979).

A common way to understand things is to see how they can be built from component parts. For instance, we think of $$\mathbb{R}^3$$ as put together, in some way, from the $$x$$-axis, the $$y$$-axis, and $$z$$-axis. In this subsection we will make this precise;we will describe how to decompose a vector space into a combination of some of its subspaces. In developing this idea of subspace combination, we will keep the $$\mathbb{R}^3$$ example in mind as a benchmark model.

Subspaces are subsets and sets combine via union. But taking the combination operation for subspaces to be the simple union operation isn't what we want. For one thing, the union of the $$x$$-axis, the $$y$$-axis, and $$z$$-axis is not all of $$\mathbb{R}^3$$, so the benchmark model would be left out. Besides, union is all wrong for this reason: a union of subspaces need not be a subspace (it need not be closed; for instance, this $$\mathbb{R}^3$$ vector

$$
\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}
$$

is in none of the three axes and hence is not in the union). In addition to the members of the subspaces, we must at least also include all of the linear combinations.

**Definition 4.1**  —

Where $$W_1,\dots, W_k$$ are subspaces of a vector space, their **sum** is the span of their union $$W_1+W_2+\dots +W_k=[W_1\cup W_2\cup \dots W_k]$$.

(The notation, writing the "$$+$$" between sets in addition to using it between vectors, fits with the practice of using this symbol for any natural accumulation operation.)

**Example 4.2**  —

The $$\mathbb{R}^3$$ model fits with this operation. Any vector $$\vec{w}\in\mathbb{R}^3$$ can be written as a linear combination $$c_1\vec{v}_1+c_2\vec{v}_2+c_3\vec{v}_3$$ where $$\vec{v}_1$$ is a member of the $$x$$-axis, etc., in this way

$$
\begin{pmatrix} w_1 \\ w_2 \\ w_3 \end{pmatrix} =1\cdot\begin{pmatrix} w_1 \\ 0 \\ 0 \end{pmatrix} +1\cdot\begin{pmatrix} 0 \\ w_2 \\ 0 \end{pmatrix} +1\cdot\begin{pmatrix} 0 \\ 0 \\ w_3 \end{pmatrix}
$$

and so $$\mathbb{R}^3=x\text{-axis}+y\text{-axis}+z\text{-axis}$$.

**Example 4.3**  —

A sum of subspaces can be less than the entire space. Inside of $$\mathcal{P}_4$$, let $$L$$ be the subspace of linear polynomials $$\{a+bx\,\big|\, a,b\in\mathbb{R}\}$$ and let $$C$$ be the subspace of purely-cubic polynomials $$\{cx^3\,\big|\, c\in\mathbb{R}\}$$. Then $$L+C$$ is not all of $$\mathcal{P}_4$$. Instead, it is the subspace $$L+C=\{a+bx+cx^3\,\big|\, a,b,c\in\mathbb{R}\}$$.

**Example 4.4**  —

A space can be described as a combination of subspaces in more than one way. Besides the decomposition $$\mathbb{R}^3=x\text{-axis}+y\text{-axis}+z\text{-axis}$$, we can also write $$\mathbb{R}^3=xy\text{-plane}+yz\text{-plane}$$. To check this, note that any $$\vec{w}\in\mathbb{R}^3$$ can be written as a linear combination of a member of the $$xy$$-plane and a member of the $$yz$$-plane; here are two such combinations.  

$$
\begin{pmatrix} w_1 \\ w_2 \\ w_3 \end{pmatrix} =1\cdot\begin{pmatrix} w_1 \\ w_2 \\ 0 \end{pmatrix} +1\cdot\begin{pmatrix} 0 \\ 0 \\ w_3 \end{pmatrix} \qquad \begin{pmatrix} w_1 \\ w_2 \\ w_3 \end{pmatrix} =1\cdot\begin{pmatrix} w_1 \\ w_2/2 \\ 0 \end{pmatrix} +1\cdot\begin{pmatrix} 0 \\ w_2/2 \\ w_3 \end{pmatrix}
$$

The above definition gives one way in which a space can be thought of as a combination of some of its parts. However, the prior example shows that there is at least one interesting property of our benchmark model that is not captured by the definition of the sum of subspaces. In the familiar decomposition of $$\mathbb{R}^3$$, we often speak of a vector's "$$x$$part" or "$$y$$part" or "$$z$$part". That is, in this model, each vector has a unique decomposition into parts that come from the parts making up the whole space. But in the decomposition used in Example 4.4, we cannot refer to the "$$xy$$part" of a vector— these three sums

$$
\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} =\begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} +\begin{pmatrix} 0 \\ 0 \\ 3 \end{pmatrix} =\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} +\begin{pmatrix} 0 \\ 2 \\ 3 \end{pmatrix} =\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} +\begin{pmatrix} 0 \\ 1 \\ 3 \end{pmatrix}
$$

all describe the vector as comprised of something from the first plane plus something from the second plane, but the "$$xy$$part" is different in each.

That is, when we consider how $$\mathbb{R}^3$$ is put together from the three axes "in some way", we might mean "in such a way that every vector has at least one decomposition", and that leads to the definition above. But if we take it to mean "in such a way that every vector has one and only one decomposition" then we need another condition on combinations. To see what this condition is, recall that vectors are uniquely represented in terms of a basis. We can use this to break a space into a sum of subspaces such that any vector in the space breaks uniquely into a sum of members of those subspaces.

**Example 4.5**  —

The benchmark is $$\mathbb{R}^3$$ with its standard basis $$\mathcal{E}_3=\langle \vec{e}_1,\vec{e}_2,\vec{e}_3 \rangle$$. The subspace with the basis $$B_1=\langle \vec{e}_1 \rangle$$ is the $$x$$-axis. The subspace with the basis $$B_2=\langle \vec{e}_2 \rangle$$ is the $$y$$-axis. The subspace with the basis $$B_3=\langle \vec{e}_3 \rangle$$ is the $$z$$-axis. The fact that any member of $$\mathbb{R}^3$$ is expressible as a sum of vectors from these subspaces

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} =\begin{pmatrix} x \\ 0 \\ 0 \end{pmatrix} +\begin{pmatrix} 0 \\ y \\ 0 \end{pmatrix} +\begin{pmatrix} 0 \\ 0 \\ z \end{pmatrix}
$$

is a reflection of the fact that $$\mathcal{E}_3$$ spans the space— this equation

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} =c_1\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} +c_2\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} +c_3\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
$$

has a solution for any $$x,y,z\in\mathbb{R}$$. And, the fact that each such expression is unique reflects that fact that $$\mathcal{E}_3$$ is linearly independent— any equation like the one above has a unique solution.

**Example 4.6**  —

We don't have to take the basis vectors one at a time, the same idea works if we conglomerate them into larger sequences. Consider again the space $$\mathbb{R}^3$$ and the vectors from the standard basis $$\mathcal{E}_3$$. The subspace with the basis $$B_1=\langle \vec{e}_1,\vec{e}_3 \rangle$$ is the $$xz$$-plane. The subspace with the basis $$B_2=\langle \vec{e}_2 \rangle$$ is the $$y$$-axis. As in the prior example, the fact that any member of the space is a sum of members of the two subspaces in one and only one way

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} =\begin{pmatrix} x \\ 0 \\ z \end{pmatrix} +\begin{pmatrix} 0 \\ y \\ 0 \end{pmatrix}
$$

is a reflection of the fact that these vectors form a basis— this system

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} =(c_1\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} +c_3\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}) +c_2\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
$$

has one and only one solution for any $$x,y,z\in\mathbb{R}$$.

These examples illustrate a natural way to decompose a space into a sum of subspaces in such a way that each vector decomposes uniquely into a sum of vectors from the parts. The next result says that this way is the only way.

**Definition 4.7**  —

The **concatenation** of the sequences $$B_1=\langle \vec{\beta}_{1,1},\dots,\vec{\beta}_{1,n_1} \rangle$$, ..., $$B_k=\langle \vec{\beta}_{k,1},\dots,\vec{\beta}_{k,n_k} \rangle$$ is their adjoinment.

$$
B_1\!\mathbin{{}^\frown}\!B_2\!\mathbin{{}^\frown}\!\cdots\!\mathbin{{}^\frown}\!B_k= \langle \vec{\beta}_{1,1},\dots,\vec{\beta}_{1,n_1}, \vec{\beta}_{2,1},\dots,\vec{\beta}_{k,n_k} \rangle
$$

**Lemma 4.8**  —

Let $$V$$ be a vector space that is the sum of some of its subspaces $$V=W_1+\dots+W_k$$. Let $$B_1$$, ..., $$B_k$$ be any bases for these subspaces. Then the following are equivalent.

1. For every $$\vec{v}\in V$$, the expression $$\vec{v}=\vec{w}_1+\dots+\vec{w}_k$$ (with $$\vec{w}_i\in W_i$$) is unique.
2. The concatenation $$B_1\!\mathbin{{}^\frown}\!\cdots\!\mathbin{{}^\frown}\!B_k$$ is a basis for $$V$$.
3. The nonzero members of $$\{\vec{w}_1,\dots,\vec{w}_k\}$$ (with $$\vec{w}_i\in W_i$$) form a linearly independent set— among nonzero vectors from different $$W_i$$'s, every linear relationship is trivial.

**Proof**  —

We will show that $$\text{(1)}\implies\text{(2)}$$, that $$\text{(2)}\implies\text{(3)}$$, and finally that $$\text{(3)}\implies\text{(1)}$$. For these arguments, observe that we can pass from a combination of $$\vec{w}$$'s to a combination of $$\vec{\beta}$$'s

$$
(*)\qquad d_1\vec{w}_1+\dots+d_k\vec{w}_k=
$$

  
  

$$
\begin{array}{rl} &= d_1(c_{1,1}\vec{\beta}_{1,1}+\dots+c_{1,n_1}\vec{\beta}_{1,n_1}) +\dots +d_k(c_{k,1}\vec{\beta}_{k,1}+\dots+c_{k,n_k}\vec{\beta}_{k,n_k}) \\ &= d_1c_{1,1}\cdot\vec{\beta}_{1,1} +\dots +d_kc_{k,n_k}\cdot\vec{\beta}_{k,n_k} \end{array}
$$

and vice versa.

For $$\text{(1)}\implies\text{(2)}$$, assume that all decompositions are unique. We will show that $$B_1\!\mathbin{{}^\frown}\!\cdots\!\mathbin{{}^\frown}\!B_k$$ spans the space and is linearly independent. It spans the space because the assumption that $$V=W_1+\dots+W_k$$ means that every $$\vec{v}$$ can be expressed as $$\vec{v}=\vec{w}_1+\dots+\vec{w}_k$$, which translates by equation($$*$$) to an expression of $$\vec{v}$$ as a linear combination of the $$\vec{\beta}$$'s from the concatenation. For linear independence, consider this linear relationship.

$$
\vec{0}=c_{1,1}\vec{\beta}_{1,1}+\dots+c_{k,n_k}\vec{\beta}_{k,n_k}
$$

Regroup as in ($$*$$) (that is, take $$d_1$$, ..., $$d_k$$ to be $$1$$ and move from bottom to top) to get the decomposition $$\vec{0}=\vec{w}_1+\dots+\vec{w}_k$$. Because of the assumption that decompositions are unique, and because the zero vector obviously has the decomposition $$\vec{0}=\vec{0}+\dots+\vec{0}$$, we now have that each $$\vec{w}_i$$ is the zero vector. This means that $$c_{i,1}\vec{\beta}_{i,1}+\dots+c_{i,n_i}\vec{\beta}_{i,n_i}=\vec{0}$$. Thus, since each $$B_i$$ is a basis, we have the desired conclusion that all of the $$c$$'s are zero.

For $$\text{(2)}\implies\text{(3)}$$, assume that $$B_1\!\mathbin{{}^\frown}\!\cdots\!\mathbin{{}^\frown}\!B_k$$ is a basis for the space. Consider a linear relationship among nonzero vectors from different $$W_i$$'s,

$$
\vec{0}=\dots+d_i\vec{w}_i+\cdots
$$

in order to show that it is trivial. (The relationship is written in this way because we are considering a combination of nonzero vectors from only some of the $$W_i$$'s; for instance, there might not be a $$\vec{w}_1$$ in this combination.) As in ($$*$$), $$\vec{0} = \dots +d_i(c_{i,1}\vec{\beta}_{i,1}+\dots+c_{i,n_i}\vec{\beta}_{i,n_i}) +\cdots = \dots +d_ic_{i,1}\cdot\vec{\beta}_{i,1} +\dots+ d_ic_{i,n_i}\cdot\vec{\beta}_{i,n_i} +\cdots$$ and the linear independence of $$B_1\!\mathbin{{}^\frown}\!\cdots\!\mathbin{{}^\frown}\!B_k$$ gives that each coefficient $$d_ic_{i,j}$$ is zero. Now, $$\vec{w}_i$$ is a nonzero vector, so at least one of the $$c_{i,j}$$'s is not zero, and thus $$d_i$$ is zero. This holds for each $$d_i$$, and therefore the linear relationship is trivial.

Finally, for $$\text{(3)}\implies\text{(1)}$$, assume that, among nonzero vectors from different $$W_i$$'s, any linear relationship is trivial. Consider two decompositions of a vector $$\vec{v}=\vec{w}_1+\dots+\vec{w}_k$$ and $$\vec{v}=\vec{u}_1+\dots+\vec{u}_k$$ in order to show that the two are the same. We have

$$
\vec{0} =(\vec{w}_1+\dots+\vec{w}_k) -(\vec{u}_1+\dots+\vec{u}_k) =(\vec{w}_1-\vec{u}_1)+\dots+(\vec{w}_k-\vec{u}_k)
$$

which violates the assumption unless each $$\vec{w}_i-\vec{u}_i$$ is the zero vector. Hence, decompositions are unique.

**Definition 4.9**  —

A collection of subspaces $$\{W_1,\ldots, W_k\}$$ is **independent** if no nonzero vector from any $$W_i$$ is a linear combination of vectors from the other subspaces $$W_1,\dots, W_{i-1},W_{i+1},\dots, W_k$$.

**Definition 4.10**  —

A vector space $$V$$ is the **direct sum** (or **internal direct sum**) of its subspaces $$W_1,\dots, W_k$$ if $$V=W_1+W_2+\dots +W_k$$ and the collection $$\{W_1,\dots, W_k\}$$ is independent. We write $$V=W_1\oplus W_2\oplus \dots\oplus W_k$$.

**Example 4.11**  —

The benchmark model fits: $$\mathbb{R}^3=x\text{-axis}\oplus y\text{-axis}\oplus z\text{-axis}$$.

**Example 4.12**  —

The space of $$2 \! \times \! 2$$ matrices is this direct sum.

$$
\{\begin{pmatrix} a &0 \\ 0 &d \end{pmatrix} \,\big|\, a,d\in\mathbb{R} \} \,\oplus\, \{\begin{pmatrix} 0 &b \\ 0 &0 \end{pmatrix} \,\big|\, b\in\mathbb{R} \} \,\oplus\, \{\begin{pmatrix} 0 &0 \\ c &0 \end{pmatrix} \,\big|\, c\in\mathbb{R} \}
$$

It is the direct sum of subspaces in many other ways as well; direct sum decompositions are not unique.

**Corollary 4.13**  —

The dimension of a direct sum is the sum of the dimensions of its summands.

**Proof**  —

In Lemma 4.8, the number of basis vectors in the concatenation equals the sum of the number of vectors in the subbases that make up the concatenation.

The special case of two subspaces is worth mentioning separately.

**Definition 4.14**  —

When a vector space is the direct sum of two of its subspaces, then they are said to be **complements**.

**Lemma 4.15**  —

A vector space $$V$$ is the direct sum of two of its subspaces $$W_1$$ and $$W_2$$ if and only if it is the sum of the two $$V=W_1+W_2$$ and their intersection is trivial $$W_1\cap W_2=\{\vec{0}\,\}$$.

**Proof**  —

Suppose first that $$V=W_1\oplus W_2$$. By definition, $$V$$ is the sum of the two. To show that the two have a trivial intersection, let $$\vec{v}$$ be a vector from $$W_1\cap W_2$$ and consider the equation $$\vec{v}=\vec{v}$$. On the left side of that equation is a member of $$W_1$$, and on the right side is a linear combination of members (actually, of only one member) of $$W_2$$. But the independence of the spaces then implies that $$\vec{v}=\vec{0}$$, as desired.

For the other direction, suppose that $$V$$ is the sum of two spaces with a trivial intersection. To show that $$V$$ is a direct sum of the two, we need only show that the spaces are independent— no nonzero member of the first is expressible as a linear combination of members of the second, and vice versa. This is true because any relationship $$\vec{w}_1=c_1\vec{w}_{2,1}+\dots+d_k\vec{w}_{2,k}$$ (with $$\vec{w}_1\in W_1$$ and $$\vec{w}_{2,j}\in W_2$$ for all $$j$$) shows that the vector on the left is also in $$W_2$$, since the right side is a combination of members of $$W_2$$. The intersection of these two spaces is trivial, so $$\vec{w}_1=\vec{0}$$. The same argument works for any $$\vec{w}_2$$.

**Example 4.16**  —

In the space $$\mathbb{R}^2$$, the $$x$$-axis and the $$y$$-axis are complements, that is, $$\mathbb{R}^2=x\text{-axis}\oplus y\text{-axis}$$. A space can have more than one pair of complementary subspaces; another pair here are the subspaces consisting of the lines $$y=x$$ and $$y=2x$$.

**Example 4.17**  —

In the space $$F=\{a\cos\theta+b\sin\theta\,\big|\, a,b\in\mathbb{R}\}$$, the subspaces $$W_1=\{a\cos\theta\,\big|\, a\in\mathbb{R}\}$$ and $$W_2=\{b\sin\theta\,\big|\, b\in\mathbb{R}\}$$ are complements. In addition to the fact that a space like $$F$$ can have more than one pair of complementary subspaces, inside of the space a single subspace like $$W_1$$ can have more than one complement— another complement of $$W_1$$ is $$W_3=\{b\sin\theta+b\cos\theta \,\big|\, b\in\mathbb{R}\}$$.

**Example 4.18**  —

In $$\mathbb{R}^3$$, the $$xy$$-plane and the $$yz$$-planes are not complements, which is the point of the discussion following Example 4.4. One complement of the $$xy$$-plane is the $$z$$-axis. A complement of the $$yz$$-plane is the line through $$(1,1,1)$$.

**Example 4.19**  —

Following Lemma 4.15, here is a natural question:is the simple sum $$V=W_1+\dots+W_k$$ also a direct sum if and only if the intersection of the subspaces is trivial? The answer is that if there are more than two subspaces then having a trivial intersection is not enough to guarantee unique decomposition (i.e., is not enough to ensure that the spaces are independent). In $$\mathbb{R}^3$$, let $$W_1$$ be the $$x$$-axis, let $$W_2$$ be the $$y$$-axis, and let $$W_3$$ be this.  

$$
W_3=\{\begin{pmatrix} q \\ q \\ r \end{pmatrix} \,\big|\, q,r\in\mathbb{R}\}
$$

The check that $$\mathbb{R}^3=W_1+W_2+W_3$$ is easy. The intersection $$W_1\cap W_2\cap W_3$$ is trivial, but decompositions aren't unique.

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} +\begin{pmatrix} 0 \\ y-x \\ 0 \end{pmatrix} +\begin{pmatrix} x \\ x \\ z \end{pmatrix} =\begin{pmatrix} x-y \\ 0 \\ 0 \end{pmatrix} +\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} +\begin{pmatrix} y \\ y \\ z \end{pmatrix}
$$

(This example also shows that this requirement is also not enough: that all pairwise intersections of the subspaces be trivial. See Problem 11.)

**Example 4.20**

This subspace of $$\mathbb{R}^3$$, $$\{\begin{pmatrix}x \\ y \\ 0\end{pmatrix}\,\mid\, x,y\in\mathbb{R}\} = \{\begin{pmatrix}x \\ 0 \\ 0\end{pmatrix} \,\mid\, x\in\mathbb{R}\} \,\oplus\, \{\begin{pmatrix}0 \\ y \\ 0\end{pmatrix} \,\mid\, y\in\mathbb{R}\}$$.  
Shows that a direct sum doesn't have to be a maximal space.

**Example 4.21**

The direct sum $$\{a_0 + a_1x + a_2x^2 \,\mid\, a_0,a_1,a_2\in\mathbb{R}\} \,\oplus\, \{a_3x^3 + a_4x^4 \,\mid\, a_3,a_4\in\mathbb{R}\} = \mathcal{P}_4$$ i.e. the space of polynomials of degree at most 4.

And the direct sum $$\mathcal{P}_4 \,\oplus\, \{a_5x^5 + a_6x^6 + a_7x^7 \,\mid\, a_5,a_6,a_7\in\mathbb{R}\} = \mathcal{P}_7$$ i.e. the space of polynomials of degree at most 7.

This shows that direct sum of two vectors spaces can be directly summed again to form an even bigger vector space (at least in the case of fininte-dimensional vectors spaces of polynomials $$\mathcal{P}_n$$, this can be repeated indefinitely).  
**Example 4.22**

Summands of some direct sums can be written as direct sums themselves,

$$
\mathbb{R}^3 = x\text{-axis} \,\oplus\, yz\text{-plane} = x\text{-axis} \,\oplus\,(y\text{-axis}\,\oplus\,z\text{-axis})
$$

$$
\mathcal{P}_2 = \{a_2x^2\mid a_2\in\mathbb{R}\} \oplus \mathcal{P}_1 = \{a_2x^2\mid a_2\in\mathbb{R}\} \oplus (\, \{a_1x\mid a_1\in\mathbb{R}\} \oplus \mathcal{P}_0 \,)
$$

In this subsection we have seen two ways to regard a space as built up from component parts. Both are useful; in particular, in this book the direct sum definition is needed to do the Jordan Form construction in the fifth chapter.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Decide if $$\mathbb{R}^2$$ is the direct sum of each $$W_1$$ and $$W_2$$.

1. $$W_1=\{\begin{pmatrix} x \\ 0 \end{pmatrix}\,\big|\, x\in\mathbb{R}\}$$, $$W_2=\{\begin{pmatrix} x \\ x \end{pmatrix}\,\big|\, x\in\mathbb{R}\}$$
2. $$W_1=\{\begin{pmatrix} s \\ s \end{pmatrix}\,\big|\, s\in\mathbb{R}\}$$, $$W_2=\{\begin{pmatrix} s \\ 1.1s \end{pmatrix}\,\big|\, s\in\mathbb{R}\}$$
3. $$W_1=\mathbb{R}^2$$, $$W_2=\{\vec{0}\}$$
4. $$W_1=W_2=\{\begin{pmatrix} t \\ t \end{pmatrix}\,\big|\, t\in\mathbb{R}\}$$
5. $$W_1=\{\begin{pmatrix} 1 \\ 0 \end{pmatrix}+\begin{pmatrix} x \\ 0 \end{pmatrix} \,\big|\, x\in\mathbb{R}\}$$, $$W_2=\{\begin{pmatrix} -1 \\ 0 \end{pmatrix}+\begin{pmatrix} 0 \\ y \end{pmatrix}\,\big|\, y\in\mathbb{R}\}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Show that $$\mathbb{R}^3$$ is the direct sum of the $$xy$$-plane with each of these.

1. the $$z$$-axis
2. the line

$$
\{\begin{pmatrix} z \\ z \\ z \end{pmatrix} \,\big|\, z\in\mathbb{R} \}
$$

**Problem 3**  —

Is $$\mathcal{P}_2$$ the direct sum of $$\{a+bx^2\,\big|\, a,b\in\mathbb{R}\}$$ and $$\{cx\,\big|\, c\in\mathbb{R}\}$$?  
*This exercise is recommended for all readers.*

**Problem 4**  —

In $$\mathcal{P}_n$$, the **even** polynomials are the members of this set

$$
\mathcal{E}= \{p\in\mathcal{P}_n \,\big|\, p(-x)=p(x) \text{ for all } x\}
$$

and the **odd** polynomials are the members of this set.

$$
\mathcal{O}= \{p\in\mathcal{P}_n \,\big|\, p(-x)=-p(x) \text{ for all }x\}
$$

Show that these are complementary subspaces.

**Problem 5**  —

Which of these subspaces of $$\mathbb{R}^3$$

$$W_1$$: the $$x$$-axis, $$W_2$$:the $$y$$-axis, $$W_3$$:the $$z$$-axis,  
$$W_4$$:the plane $$x+y+z=0$$, $$W_5$$:the $$yz$$-plane

can be combined to

1. sum to $$\mathbb{R}^3$$?
2. direct sum to $$\mathbb{R}^3$$?  
*This exercise is recommended for all readers.*

**Problem 6**  —

Show that $$\mathcal{P}_n=\{a_0 \,\big|\, a_0\in\mathbb{R}\}\oplus\dots\oplus\{a_nx^n\,\big|\, a_n\in\mathbb{R}\}$$.

**Problem 7**  —

What is $$W_1+W_2$$ if $$W_1\subseteq W_2$$?

**Problem 8**  —

Does Example 4.5 generalize? That is, is this true or false:if a vector space $$V$$ has a basis $$\langle \vec{\beta}_1,\dots ,\vec{\beta}_n \rangle$$ then it is the direct sum of the spans of the one-dimensional subspaces $$V=[\{\vec{\beta}_1\}]\oplus\dots\oplus[\{\vec{\beta}_n\}]$$?

**Problem 9**  —

Can $$\mathbb{R}^4$$ be decomposed as a direct sum in two different ways? Can $$\mathbb{R}^1$$?

**Problem 10**  —

This exercise makes the notation of writing "$$+$$" between sets more natural. Prove that, where $$W_1,\dots, W_k$$ are subspaces of a vector space,

$$
W_1+\dots+W_k =\{\vec{w}_1+\vec{w}_2+\dots+\vec{w}_k \,\big|\, \vec{w}_1\in W_1,\dots,\vec{w}_k\in W_k\},
$$

and so the sum of subspaces is the subspace of all sums.

**Problem 11**  —

(Refer to Example 4.19. This exercise shows that the requirement that pariwise intersections be trivial is genuinely stronger than the requirement only that the intersection of all of the subspaces be trivial.) Give a vector space and three subspaces $$W_1$$, $$W_2$$, and $$W_3$$ such that the space is the sum of the subspaces, the intersection of all three subspaces $$W_1\cap W_2\cap W_3$$ is trivial, but the pairwise intersections $$W_1\cap W_2$$, $$W_1\cap W_3$$, and $$W_2\cap W_3$$ are nontrivial.  
*This exercise is recommended for all readers.*

**Problem 12**  —

Prove that if $$V=W_1\oplus\dots\oplus W_k$$ then $$W_i\cap W_j$$ is trivial whenever $$i\neq j$$. This shows that the first half of the proof of Lemma 4.15 extends to the case of more than two subspaces. (Example 4.19 shows that this implication does not reverse; the other half does not extend.)

**Problem 13**  —

Recall that no linearly independent set contains the zero vector. Can an independent set of subspaces contain the trivial subspace?  
*This exercise is recommended for all readers.*

**Problem 14**  —

Does every subspace have a complement?  
*This exercise is recommended for all readers.*

**Problem 15**  —

Let $$W_1, W_2$$ be subspaces of a vector space.

1. Assume that the set $$S_1$$ spans $$W_1$$, and that the set $$S_2$$ spans $$W_2$$. Can $$S_1\cup S_2$$ span $$W_1+W_2$$? Must it?
2. Assume that $$S_1$$ is a linearly independent subset of $$W_1$$ and that $$S_2$$ is a linearly independent subset of $$W_2$$. Can $$S_1\cup S_2$$ be a linearly independent subset of $$W_1+W_2$$? Must it?

**Problem 16**  —

When a vector space is decomposed as a direct sum, the dimensions of the subspaces add to the dimension of the space. The situation with a space that is given as the sum of its subspaces is not as simple. This exercise considers the two-subspace special case.

1. For these subspaces of $$\mathcal{M}_{2 \! \times \! 2}$$ find $$W_1\cap W_2$$, $$\dim(W_1\cap W_2)$$, $$W_1+W_2$$, and $$\dim(W_1+W_2)$$.

$$
W_1=\{\begin{pmatrix} 0 &0 \\ c &d \end{pmatrix} \,\big|\, c,d\in\mathbb{R} \} \qquad W_2=\{\begin{pmatrix} 0 &b \\ c &0 \end{pmatrix} \,\big|\, b,c\in\mathbb{R} \}
$$

2. Suppose that $$U$$ and $$W$$ are subspaces of a vector space. Suppose that the sequence $$\langle \vec{\beta}_1,\dots,\vec{\beta}_k \rangle$$ is a basis for $$U\cap W$$. Finally, suppose that the prior sequence has been expanded to give a sequence $$\langle \vec{\mu}_1,\dots,\vec{\mu}_j,\vec{\beta}_1,\dots,\vec{\beta}_k \rangle$$ that is a basis for $$U$$, and a sequence $$\langle \vec{\beta}_1,\dots,\vec{\beta}_k, \vec{\omega}_1,\dots,\vec{\omega}_p \rangle$$ that is a basis for $$W$$. Prove that this sequence

$$
\langle \vec{\mu}_1,\dots,\vec{\mu}_j, \vec{\beta}_1,\dots,\vec{\beta}_k, \vec{\omega}_1,\dots,\vec{\omega}_p \rangle
$$

is a basis for for the sum $$U+W$$.
3. Conclude that $$\dim (U+W)=\dim(U)+\dim(W)-\dim(U\cap W)$$.
4. Let $$W_1$$ and $$W_2$$ be eight-dimensional subspaces of a ten-dimensional space. List all values possible for $$\dim(W_1\cap W_2)$$.

**Problem 17**  —

Let $$V=W_1\oplus\dots\oplus W_k$$ and for each index $$i$$ suppose that $$S_i$$ is a linearly independent subset of $$W_i$$. Prove that the union of the $$S_i$$'s is linearly independent.

**Problem 18**  —

A matrix is **symmetric** if for each pair of indices $$i$$ and $$j$$, the $$i,j$$ entry equals the $$j,i$$ entry. A matrix is **antisymmetric** if each $$i,j$$ entry is the negative of the $$j,i$$ entry.

1. Give a symmetric $$2 \! \times \! 2$$ matrix and an antisymmetric $$2 \! \times \! 2$$ matrix. (*Remark.* For the second one, be careful about the entries on the diagional.)
2. What is the relationship between a square symmetric matrix and its transpose? Between a square antisymmetric matrix and its transpose?
3. Show that $$\mathcal{M}_{n \! \times \! n}$$ is the direct sum of the space of symmetric matrices and the space of antisymmetric matrices.

**Problem 19**  —

Let $$W_1,W_2,W_3$$ be subspaces of a vector space. Prove that $$(W_1\cap W_2)+(W_1\cap W_3)\subseteq W_1\cap (W_2+W_3)$$. Does the inclusion reverse?

**Problem 20**  —

The example of the $$x$$-axis and the $$y$$-axis in $$\mathbb{R}^2$$ shows that $$W_1\oplus W_2=V$$ does not imply that $$W_1\cup W_2=V$$. Can $$W_1\oplus W_2=V$$ and $$W_1\cup W_2=V$$ happen?  
*This exercise is recommended for all readers.*

**Problem 21**  —

Our model for complementary subspaces, the $$x$$-axis and the $$y$$-axis in $$\mathbb{R}^2$$, has one property not used here. Where $$U$$ is a subspace of $$\mathbb{R}^n$$ we define the **orthogonal complement** of $$U$$ to be

$$
U^\perp= \{\vec{v}\in\mathbb{R}^n \,\big|\, \vec{v}\cdot\vec{u}=0\text{ for all } \vec{u}\in U\}
$$

(read "$$U$$ perp").

1. Find the orthocomplement of the $$x$$-axis in $$\mathbb{R}^2$$.
2. Find the orthocomplement of the $$x$$-axis in $$\mathbb{R}^3$$.
3. Find the orthocomplement of the $$xy$$-plane in $$\mathbb{R}^3$$.
4. Show that the orthocomplement of a subspace is a subspace.
5. Show that if $$W$$ is the orthocomplement of $$U$$ then $$U$$ is the orthocomplement of $$W$$.
6. Prove that a subspace and its orthocomplement have a trivial intersection.
7. Conclude that for any $$n$$ and subspace $$U\subseteq \mathbb{R}^n$$ we have that $$\mathbb{R}^n=U\oplus U^\perp$$.
8. Show that $$\dim(U)+\dim(U^\perp)$$ equals the dimension of the enclosing space.  
*This exercise is recommended for all readers.*

**Problem 22**  —

Consider Corollary 4.13. Does it work both ways— that is, supposing that $$V=W_1+\dots+ W_k$$, is $$V=W_1\oplus\dots\oplus W_k$$ if and only if $$\dim(V)=\dim(W_1)+\dots+\dim(W_k)$$?

**Problem 23**  —

We know that if $$V=W_1\oplus W_2$$ then there is a basis for $$V$$ that splits into a basis for $$W_1$$ and a basis for $$W_2$$. Can we make the stronger statement that every basis for $$V$$ splits into a basis for $$W_1$$ and a basis for $$W_2$$?

**Problem 24**  —

We can ask about the algebra of the "$$+$$" operation.

1. Is it commutative; is $$W_1+W_2=W_2+W_1$$?
2. Is it associative; is $$(W_1+W_2)+W_3=W_1+(W_2+W_3)$$?
3. Let $$W$$ be a subspace of some vector space. Show that $$W+W=W$$.
4. Must there be an identity element, a subspace $$I$$ such that $$I+W=W+I=W$$ for all subspaces $$W$$?
5. Does left-cancelation hold:if $$W_1+W_2=W_1+W_3$$ then $$W_2=W_3$$? Right cancelation?

**Problem 25**  —

Consider the algebraic properties of the direct sum operation.

1. Does direct sum commute: does $$V=W_1\oplus W_2$$ imply that $$V=W_2\oplus W_1$$?
2. Prove that direct sum is associative:$$(W_1\oplus W_2)\oplus W_3=W_1\oplus(W_2\oplus W_3)$$.
3. Show that $$\mathbb{R}^3$$ is the direct sum of the three axes (the relevance here is that by the previous item, we needn't specify which two of the three axes are combined first).
4. Does the direct sum operation left-cancel:does $$W_1\oplus W_2=W_1\oplus W_3$$ imply $$W_2=W_3$$? Does it right-cancel?
5. There is an identity element with respect to this operation. Find it.
6. Do some, or all, subspaces have inverses with respect to this operation:is there a subspace $$W$$ of some vector space such that there is a subspace $$U$$ with the property that $$U\oplus W$$ equals the identity element from the prior item?

Solutions

### References

- Halsey, William D. (1979), *Macmillian Dictionary*, Macmillian.

---

*Source: Wikibooks, Linear Algebra/Combining Subspaces (https://en.wikibooks.org/wiki/Linear_Algebra/Combining_Subspaces), by Wikibooks contributors, CC BY-SA 4.0.*
