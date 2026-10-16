# Matrix Multiplication

After representing addition and scalar multiplication of linear maps in the prior subsection, the natural next map operation to consider is composition.

**Lemma 2.1**  —

A composition of linear maps is linear.

**Proof**  —

*(This argument has appeared earlier, as part of the proof that isomorphism is an equivalence relation between spaces.)* Let $$h:V\to W$$ and $$g:W\to U$$ be linear. The calculation

$$
g\circ h\,\bigl(c_1\cdot\vec{v}_1+c_2\cdot\vec{v}_2\bigr) =g\bigl(\,h(c_1\cdot \vec{v}_1+c_2\cdot\vec{v}_2)\,\bigr) =g\bigl(\,c_1\cdot h(\vec{v}_1)+c_2\cdot h(\vec{v}_2)\,\bigr)
$$

$$
=c_1\cdot g\bigl(h(\vec{v}_1))+c_2\cdot g(h(\vec{v}_2)\bigr) =c_1\cdot (g\circ h)(\vec{v}_1) +c_2\cdot (g\circ h)(\vec{v}_2)
$$

shows that $$g\circ h:V\to U$$ preserves linear combinations.

To see how the representation of the composite arises out of the representations of the two compositors, consider an example.

**Example 2.2**  —

Let $$h:\mathbb{R}^4\to \mathbb{R}^2$$ and $$g:\mathbb{R}^2\to \mathbb{R}^3$$, fix bases $$B\subset\mathbb{R}^4$$, $$C\subset\mathbb{R}^2$$, $$D\subset\mathbb{R}^3$$, and let these be the representations.

$$
H={\rm Rep}_{B,C}(h) =\begin{pmatrix} 4 &6 &8 &2 \\ 5 &7 &9 &3 \end{pmatrix}_{B,C} \qquad G={\rm Rep}_{C,D}(g) =\begin{pmatrix} 1 &1 \\ 0 &1 \\ 1 &0 \end{pmatrix}_{C,D}
$$

To represent the composition $$g\circ h:\mathbb{R}^4\to \mathbb{R}^3$$ we fix a $$\vec{v}$$, represent $$h$$ of $$\vec{v}$$, and then represent $$g$$ of that. The representation of $$h(\vec{v})$$ is the product of $$h$$'s matrix and $$\vec{v}$$'s vector.

$$
{\rm Rep}_{C}(\,h(\vec{v})\,) = \begin{pmatrix} 4 &6 &8 &2 \\ 5 &7 &9 &3 \end{pmatrix}_{B,C} \begin{pmatrix} v_1 \\ v_2 \\ v_3 \\ v_4 \end{pmatrix}_B = \begin{pmatrix} 4v_1+6v_2+8v_3+2v_4 \\ 5v_1+7v_2+9v_3+3v_4 \end{pmatrix}_C
$$

The representation of $$g(\,h(\vec{v})\,)$$ is the product of $$g$$'s matrix and $$h(\vec{v})$$'s vector.

$$
\begin{array}{rl} {\rm Rep}_{D}(\,g(h(\vec{v}))\,)\! &=\!\begin{pmatrix} 1 &1 \\ 0 &1 \\ 1 &0 \end{pmatrix}_{C,D} \begin{pmatrix} 4v_1+6v_2+8v_3+2v_4 \\ 5v_1+7v_2+9v_3+3v_4 \end{pmatrix}_C \\ &=\!\begin{pmatrix} 1\cdot(4v_1+6v_2+8v_3+2v_4)+1\cdot(5v_1+7v_2+9v_3+3v_4) \\ 0\cdot(4v_1+6v_2+8v_3+2v_4)+1\cdot(5v_1+7v_2+9v_3+3v_4) \\ 1\cdot(4v_1+6v_2+8v_3+2v_4)+0\cdot(5v_1+7v_2+9v_3+3v_4) \end{pmatrix}_D \end{array}
$$

Distributing and regrouping on the $$v$$'s gives

$$
= \begin{pmatrix} (1\cdot4+1\cdot5)v_1+ (1\cdot6+1\cdot7)v_2+ (1\cdot8+1\cdot9)v_3+ (1\cdot2+1\cdot3)v_4 \\ (0\cdot4+1\cdot5)v_1+ (0\cdot6+1\cdot7)v_2+ (0\cdot8+1\cdot9)v_3+ (0\cdot2+1\cdot3)v_4 \\ (1\cdot4+0\cdot5)v_1+ (1\cdot6+0\cdot7)v_2+ (1\cdot8+0\cdot9)v_3+ (1\cdot2+0\cdot3)v_4 \end{pmatrix}_D
$$

which we recognizing as the result of this matrix-vector product.

$$
= \begin{pmatrix} 1\cdot4+1\cdot5 &1\cdot6+1\cdot7 &1\cdot8+1\cdot9 &1\cdot2+1\cdot3 \\ 0\cdot4+1\cdot5 &0\cdot6+1\cdot7 &0\cdot8+1\cdot9 &0\cdot2+1\cdot3 \\ 1\cdot4+0\cdot5 &1\cdot6+0\cdot7 &1\cdot8+0\cdot9 &1\cdot2+0\cdot3 \end{pmatrix}_{B,D} \begin{pmatrix} v_1 \\ v_2 \\ v_3 \\ v_4 \end{pmatrix}_D
$$

Thus, the matrix representing $$g\circ h$$ has the rows of $$G$$ combined with the columns of $$H$$.

**Definition 2.3**  —

The **matrix-multiplicative product** of the $$m \! \times \! r$$ matrix $$G$$ and the $$r \! \times \! n$$ matrix $$H$$ is the $$m \! \times \! n$$ matrix $$P$$, where

$$
p_{i,j} = g_{i,1}h_{1,j}+g_{i,2}h_{2,j}+\dots+g_{i,r}h_{r,j}
$$

that is, the $$i,j$$-th entry of the product is the dot product of the $$i$$-th row and the $$j$$-th column.

$$
GH= \begin{pmatrix} &\vdots \\ g_{i,1} &g_{i,2} &\ldots &g_{i,r} \\ &\vdots \end{pmatrix} \begin{pmatrix} &h_{1,j} \\ \ldots &h_{2,j} &\ldots \\ &\vdots \\ &h_{r,j} \end{pmatrix} = \begin{pmatrix} &\vdots \\ \ldots &p_{i,j} &\ldots \\ &\vdots \end{pmatrix}
$$

**Example 2.4**  —

The matrices from Example 2.2 combine in this way.

$$
\begin{pmatrix} 1\cdot4+1\cdot5 &1\cdot6+1\cdot7 &1\cdot8+1\cdot9 &1\cdot2+1\cdot3 \\ 0\cdot4+1\cdot5 &0\cdot6+1\cdot7 &0\cdot8+1\cdot9 &0\cdot2+1\cdot3 \\ 1\cdot4+0\cdot5 &1\cdot6+0\cdot7 &1\cdot8+0\cdot9 &1\cdot2+0\cdot3 \end{pmatrix} =\begin{pmatrix} 9 &13 &17 &5 \\ 5 &7 &9 &3 \\ 4 &6 &8 &2 \end{pmatrix}
$$

**Example 2.5**  —

$$
\begin{pmatrix} 2 &0 \\ 4 &6 \\ 8 &2 \end{pmatrix} \begin{pmatrix} 1 &3 \\ 5 &7 \end{pmatrix} = \begin{pmatrix} 2\cdot 1+0\cdot 5 &2\cdot 3+0\cdot 7 \\ 4\cdot 1+6\cdot 5 &4\cdot 3+6\cdot 7 \\ 8\cdot 1+2\cdot 5 &8\cdot 3+2\cdot 7 \end{pmatrix} = \begin{pmatrix} 2 &6 \\ 34 &54 \\ 18 &38 \end{pmatrix}
$$

**Theorem 2.6**  —

A composition of linear maps is represented by the matrix product of the representatives.

**Proof**  —

*(This argument parallels Example 2.2.)* Let $$h:V\to W$$ and $$g:W\to X$$ be represented by $$H$$ and $$G$$ with respect to bases $$B\subset V$$, $$C\subset W$$, and $$D\subset X$$, of sizes $$n$$, $$r$$, and $$m$$. For any $$\vec{v}\in V$$, the $$k$$-th component of $${\rm Rep}_{C}(\,h(\vec{v})\,)$$ is

$$
h_{k,1}v_1+\cdots+h_{k,n}v_n
$$

and so the $$i$$-th component of $${\rm Rep}_{D}(\,g\circ h\,(\vec{v})\,)$$ is this.

$$
g_{i,1}\cdot(h_{1,1}v_1+\dots+h_{1,n}v_n) +g_{i,2}\cdot(h_{2,1}v_1+\dots+h_{2,n}v_n)
$$

$$
+\dots +g_{i,r}\cdot(h_{r,1}v_1+\dots+h_{r,n}v_n)
$$

Distribute and regroup on the $$v$$'s.

$$
=(g_{i,1} h_{1,1}+g_{i,2} h_{2,1}+\dots+g_{i,r}h_{r,1})\cdot v_1
$$

$$
+\dots +(g_{i,1} h_{1,n}+g_{i,2} h_{2,n} +\dots+g_{i,r} h_{r,n})\cdot v_n
$$

Finish by recognizing that the coefficient of each $$v_j$$

$$
g_{i,1}h_{1,j}+g_{i,2}h_{2,j}+\dots+g_{i,r}h_{r,j}
$$

matches the definition of the $$i,j$$ entry of the product $$GH$$.

The theorem is an example of a result that supports a definition. We can picture what the definition and theorem together say with this **arrow diagram** ("wrt" abbreviates "with respect to").

Above the arrows, the maps show that the two ways of going from $$V$$ to $$X$$, straight over via the composition or else by way of $$W$$, have the same effect

$$
\vec{v}\stackrel{g\circ h}{\longmapsto}g(h(\vec{v})) \qquad \vec{v}\stackrel{h}{\longmapsto}h(\vec{v})\stackrel{g}{\longmapsto}g(h(\vec{v}))
$$

(this is just the definition of composition). Below the arrows, the matrices indicate that the product does the same thing— multiplying $$GH$$ into the column vector $${\rm Rep}_{B}(\vec{v})$$ has the same effect as multiplying the column first by $$H$$ and then multiplying the result by $$G$$.

$$
{\rm Rep}_{B,D}(g\circ h) =GH= {\rm Rep}_{C,D}(g)\,{\rm Rep}_{B,C}(h)
$$

The definition of the matrix-matrix product operation does not restrict us to view it as a representation of a linear map composition. We can get insight into this operation by studying it as a mechanical procedure. The striking thing is the way that rows and columns combine.

One aspect of that combination is that the sizes of the matrices involved is significant. Briefly, $$m \! \times \! r\text{ times }r \! \times \! n\text{ equals }m \! \times \! n$$.

**Example 2.7**  —

This product is not defined

$$
\begin{pmatrix} -1 &2 &0 \\ 0 &10 &1.1 \end{pmatrix} \begin{pmatrix} 0 &0 \\ 0 &2 \end{pmatrix}
$$

because the number of columns on the left does not equal the number of rows on the right.

In terms of the underlying maps, the fact that the sizes must match up reflects the fact that matrix multiplication is defined only when a corresponding function composition

$$
\text{dimension } n \text{ space} \;\stackrel{h}{\longrightarrow}\; \text{dimension } r \text{ space} \;\stackrel{g}{\longrightarrow}\; \text{dimension } m \text{ space}
$$

is possible.

**Remark 2.8**  —

The order in which these things are written can be confusing. In the "$$m \! \times \! r\text{ times }r \! \times \! n\text{ equals }m \! \times \! n$$" equation, the number written first $$m$$ is the dimension of $$g$$'s codomain and is thus the number that appears last in the map dimension description above. The explanation is that while $$f$$ is done first and then $$g$$ is applied, that composition is written $$g\circ f$$, from the notation "$$g(f(\vec{v}))$$". (Some people try to lessen confusion by reading "$$g\circ f$$" aloud as "$$g$$ following $$f$$".) That order then carries over to matrices: $$g\circ f$$ is represented by $$GF$$.

Another aspect of the way that rows and columns combine in the matrix product operation is that in the definition of the $$i,j$$ entry

$$
p_{i,j} = g_{i,{\color{red}1}}h_{{\color{red}1},j} +g_{i,{\color{red}2}}h_{{\color{red}2},j} +\dots+g_{i,{\color{red}r}}h_{{\color{red}r},j}
$$

the red subscripts on the $$g$$'s are column indicators while those on the $$h$$'s indicate rows. That is, summation takes place over the columns of $$G$$ but over the rows of $$H$$; left is treated differently than right, so $$GH$$ may be unequal to $$HG$$. Matrix multiplication is not commutative.

**Example 2.9**  —

Matrix multiplication hardly ever commutes. Test that by multiplying randomly chosen matrices both ways.

$$
\begin{pmatrix} 1 &2 \\ 3 &4 \end{pmatrix} \begin{pmatrix} 5 &6 \\ 7 &8 \end{pmatrix} = \begin{pmatrix} 19 &22 \\ 43 &50 \end{pmatrix} \qquad \begin{pmatrix} 5 &6 \\ 7 &8 \end{pmatrix} \begin{pmatrix} 1 &2 \\ 3 &4 \end{pmatrix} = \begin{pmatrix} 23 &34 \\ 31 &46 \end{pmatrix}
$$

**Example 2.10**  —

Commutativity can fail more dramatically:

$$
\begin{pmatrix} 5 &6 \\ 7 &8 \end{pmatrix} \begin{pmatrix} 1 &2 &0 \\ 3 &4 &0 \end{pmatrix} = \begin{pmatrix} 23 &34 &0 \\ 31 &46 &0 \end{pmatrix}
$$

while

$$
\begin{pmatrix} 1 &2 &0 \\ 3 &4 &0 \end{pmatrix} \begin{pmatrix} 5 &6 \\ 7 &8 \end{pmatrix}
$$

isn't even defined.

**Remark 2.11**  —

The fact that matrix multiplication is not commutative may be puzzling at first sight, perhaps just because most algebraic operations in elementary mathematics are commutative. But on further reflection, it isn't so surprising. After all, matrix multiplication represents function composition, which is not commutative— if $$f(x)=2x$$ and $$g(x)=x+1$$ then $$g\circ f(x)=2x+1$$ while $$f\circ g(x)=2(x+1)=2x+2$$. True, this $$g$$ is not linear and we might have hoped that linear functions commute, but this perspective shows that the failure of commutativity for matrix multiplication fits into a larger context.

Except for the lack of commutativity, matrix multiplication is algebraically well-behaved. Below are some nice properties and more are in Problem 10 and Problem 11.

**Theorem 2.12**  —

If $$F$$, $$G$$, and $$H$$ are matrices, and the matrix products are defined, then the product is associative $$(FG)H=F(GH)$$ and distributes over matrix addition $$F(G+H)=FG+FH$$ and $$(G+H)F=GF+HF$$.

**Proof**  —

Associativity holds because matrix multiplication represents function composition, which is associative: the maps $$(f\circ g)\circ h$$ and $$f\circ (g\circ h)$$ are equal as both send $$\vec{v}$$ to $$f(g(h(\vec{v})))$$.

Distributivity is similar. For instance, the first one goes $$f\circ (g+h)\,(\vec{v}) =f\bigl(\,(g+h)(\vec{v})\,\bigr) =f\bigl(\,g(\vec{v})+h(\vec{v})\,\bigr) =f(g(\vec{v}))+f(h(\vec{v})) =f\circ g(\vec{v})+f\circ h(\vec{v})$$ (the third equality uses the linearity of $$f$$).

**Remark 2.13**  —

We could alternatively prove that result by slogging through the indices. For example, associativity goes: the $$i,j$$-th entry of $$(FG)H$$ is

$$
\begin{array}{rl} &(f_{i,1}g_{1,1}+f_{i,2}g_{2,1}+\dots+f_{i,r}g_{r,1})h_{1,j} \\ &\quad +(f_{i,1}g_{1,2}+f_{i,2}g_{2,2}+\dots+f_{i,r}g_{r,2})h_{2,j} \\ &\quad\;\;\vdots \\ &\quad +(f_{i,1}g_{1,s}+f_{i,2}g_{2,s}+\dots+f_{i,r}g_{r,s})h_{s,j} \end{array}
$$

(where $$F$$, $$G$$, and $$H$$ are $$m \! \times \! r$$, $$r \! \times \! s$$, and $$s \! \times \! n$$ matrices), distribute

$$
\begin{array}{rl} &f_{i,1}g_{1,1}h_{1,j}+f_{i,2}g_{2,1}h_{1,j}+ \dots+f_{i,r}g_{r,1}h_{1,j} \\ &\quad+f_{i,1}g_{1,2}h_{2,j}+f_{i,2}g_{2,2}h_{2,j}+ \dots+f_{i,r}g_{r,2}h_{2,j} \\ &\quad\;\;\vdots \\ &\quad+f_{i,1}g_{1,s}h_{s,j}+f_{i,2}g_{2,s}h_{s,j}+\dots +f_{i,r}g_{r,s}h_{s,j} \end{array}
$$

and regroup around the $$f$$'s

$$
\begin{array}{rl} &f_{i,1}(g_{1,1}h_{1,j}+g_{1,2}h_{2,j}+\dots+g_{1,s}h_{s,j}) \\ &\quad +f_{i,2}(g_{2,1}h_{1,j}+g_{2,2}h_{2,j}+\dots+g_{2,s}h_{s,j}) \\ &\quad\;\;\vdots \\ &\quad +f_{i,r}(g_{r,1}h_{1,j}+g_{r,2}h_{2,j}+\dots+g_{r,s}h_{s,j}) \end{array}
$$

to get the $$i,j$$ entry of $$F(GH)$$.

Contrast these two ways of verifying associativity, the one in the proof and the one just above. The argument just above is hard to understand in the sense that, while the calculations are easy to check, the arithmetic seems unconnected to any idea (it also essentially repeats the proof of Theorem 2.6 and so is inefficient). The argument in the proof is shorter, clearer, and says why this property "really" holds. This illustrates the comments made in the preamble to the chapter on vector spaces— at least some of the time an argument from higher-level constructs is clearer.

We have now seen how the representation of the composition of two linear maps is derived from the representations of the two maps. We have called the combination the product of the two matrices. This operation is extremely important. Before we go on to study how to represent the inverse of a linear map, we will explore it some more in the next subsection.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Compute, or state "not defined".

1. $$\begin{pmatrix} 3 &1 \\ -4 &2 \end{pmatrix} \begin{pmatrix} 0 &5 \\ 0 &0.5 \end{pmatrix}$$
2. $$\begin{pmatrix} 1 &1 &-1 \\ 4 &0 &3 \end{pmatrix} \begin{pmatrix} 2 &-1 &-1 \\ 3 &1 &1 \\ 3 &1 &1 \end{pmatrix}$$
3. $$\begin{pmatrix} 2 &-7 \\ 7 &4 \end{pmatrix} \begin{pmatrix} 1 &0 &5 \\ -1 &1 &1 \\ 3 &8 &4 \end{pmatrix}$$
4. $$\begin{pmatrix} 5 &2 \\ 3 &1 \end{pmatrix} \begin{pmatrix} -1 &2 \\ 3 &-5 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Where

$$
A= \begin{pmatrix} 1 &-1 \\ 2 &0 \\ \end{pmatrix} \quad B= \begin{pmatrix} 5 &2 \\ 4 &4 \\ \end{pmatrix} \quad C= \begin{pmatrix} -2 &3 \\ -4 &1 \\ \end{pmatrix}
$$

compute or state "not defined".

1. $$AB$$
2. $$(AB)C$$
3. $$BC$$
4. $$A(BC)$$

**Problem 3**  —

Which products are defined?

1. $$3 \! \times \! 2$$ times $$2 \! \times \! 3$$
2. $$2 \! \times \! 3$$ times $$3 \! \times \! 2$$
3. $$2 \! \times \! 2$$ times $$3 \! \times \! 3$$
4. $$3 \! \times \! 3$$ times $$2 \! \times \! 2$$  
*This exercise is recommended for all readers.*

**Problem 4**  —

Give the size of the product or state "not defined".

1. a $$2 \! \times \! 3$$ matrix times a $$3 \! \times \! 1$$ matrix
2. a $$1 \! \times \! 12$$ matrix times a $$12 \! \times \! 1$$ matrix
3. a $$2 \! \times \! 3$$ matrix times a $$2 \! \times \! 1$$ matrix
4. a $$2 \! \times \! 2$$ matrix times a $$2 \! \times \! 2$$ matrix  
*This exercise is recommended for all readers.*

**Problem 5**  —

Find the system of equations resulting from starting with

$$
\begin{array}{rcrcrcr} h_{1,1}x_1 &+ &h_{1,2}x_2 &+ &h_{1,3}x_3 &= &d_1 \\ h_{2,1}x_1 &+ &h_{2,2}x_2 &+ &h_{2,3}x_3 &= &d_2 \end{array}
$$

and making this change of variable (i.e., substitution).

$$
\begin{array}{rcrcr} x_1 &= &g_{1,1}y_1 &+ &g_{1,2}y_2 \\ x_2 &= &g_{2,1}y_1 &+ &g_{2,2}y_2 \\ x_3 &= &g_{3,1}y_1 &+ &g_{3,2}y_2 \end{array}
$$

**Problem 6**  —

As Definition 2.3 points out, the matrix product operation generalizes the dot product. Is the dot product of a $$1 \! \times \! n$$ row vector and a $$n \! \times \! 1$$ column vector the same as their matrix-multiplicative product?  
*This exercise is recommended for all readers.*

**Problem 7**  —

Represent the derivative map on $$\mathcal{P}_n$$ with respect to $$B,B$$ where $$B$$ is the natural basis $$\langle 1,x,\ldots,x^n \rangle$$. Show that the product of this matrix with itself is defined; what the map does it represent?

**Problem 8**  —

Show that composition of linear transformations on $$\mathbb{R}^1$$ is commutative. Is this true for any one-dimensional space?

**Problem 9**  —

Why is matrix multiplication not defined as entry-wise multiplication? That would be easier, and commutative too.  
*This exercise is recommended for all readers.*

**Problem 10**  —

1. Prove that $$H^pH^q=H^{p+q}$$ and $$(H^p)^q=H^{pq}$$ for positive integers $$p,q$$.
2. Prove that $$(rH)^p=r^p\cdot H^p$$ for any positive integer $$p$$ and scalar $$r\in\mathbb{R}$$.  
*This exercise is recommended for all readers.*

**Problem 11**  —

1. How does matrix multiplication interact with scalar multiplication: is $$r(GH)=(rG)H$$? Is $$G(rH)=r(GH)$$?
2. How does matrix multiplication interact with linear combinations: is $$F(rG+sH)=r(FG)+s(FH)$$? Is $$(rF+sG)H=rFH+sGH$$?

**Problem 12**  —

We can ask how the matrix product operation interacts with the transpose operation.

1. Show that $${{(GH)}^{\rm trans}}={{H}^{\rm trans}}{{G}^{\rm trans}}$$.
2. A square matrix is **symmetric** if each $$i,j$$ entry equals the $$j,i$$ entry, that is, if the matrix equals its own transpose. Show that the matrices $$H{{H}^{\rm trans}}$$ and $${{H}^{\rm trans}}H$$ are symmetric.  
*This exercise is recommended for all readers.*

**Problem 13**  —

Rotation of vectors in $$\mathbb{R}^3$$ about an axis is a linear map. Show that linear maps do not commute by showing geometrically that rotations do not commute.

**Problem 14**  —

In the proof of Theorem 2.12 some maps are used. What are the domains and codomains?

**Problem 15**  —

How does matrix rank interact with matrix multiplication?

1. Can the product of rank $$n$$ matrices have rank less than $$n$$? Greater?
2. Show that the rank of the product of two matrices is less than or equal to the minimum of the rank of each factor.

**Problem 16**  —

Is "commutes with" an equivalence relation among $$n \! \times \! n$$ matrices?  
*This exercise is recommended for all readers.*

**Problem 17**  —

*(This will be used in the Matrix Inverses exercises.)* Here is another property of matrix multiplication that might be puzzling at first sight.

1. Prove that the composition of the projections $$\pi_x,\pi_y:\mathbb{R}^3\to \mathbb{R}^3$$ onto the $$x$$ and $$y$$ axes is the zero map despite that neither one is itself the zero map.
2. Prove that the composition of the derivatives $$d^2/dx^2,\,d^3/dx^3:\mathcal{P}_4\to \mathcal{P}_4$$ is the zero map despite that neither is the zero map.
3. Give a matrix equation representing the first fact.
4. Give a matrix equation representing the second.

When two things multiply to give zero despite that neither is zero, each is said to be a **zero divisor**.

**Problem 18**  —

Show that, for square matrices, $$(S+T)(S-T)$$ need not equal $$S^2-T^2$$.  
*This exercise is recommended for all readers.*

**Problem 19**  —

Represent the identity transformation $$\text{id}:V\to V$$ with respect to $$B,B$$ for any basis $$B$$. This is the **identity matrix** $$I$$. Show that this matrix plays the role in matrix multiplication that the number $$1$$ plays in real number multiplication: $$HI=IH=H$$ (for all matrices $$H$$ for which the product is defined).

**Problem 20**  —

In real number algebra, quadratic equations have at most two solutions. That is not so with matrix algebra. Show that the $$2 \! \times \! 2$$ matrix equation $$T^2=I$$ has more than two solutions, where $$I$$ is the identity matrix (this matrix has ones in its $$1,1$$ and $$2,2$$ entries and zeroes elsewhere; see Problem 19).

**Problem 21**  —

1. Prove that for any $$2 \! \times \! 2$$ matrix $$T$$ there are scalars $$c_0,\dots,c_4$$ that are not all $$0$$ such that the combination $$c_4T^4+c_3T^3+c_2T^2+c_1T+c_0I$$ is the zero matrix (where $$I$$ is the $$2 \! \times \! 2$$ identity matrix, with $$1$$'s in its $$1,1$$ and $$2,2$$ entries and zeroes elsewhere; see Problem 19).
2. Let $$p(x)$$ be a polynomial $$p(x)=c_nx^n+\dots+c_1x+c_0$$. If $$T$$ is a square matrix we define $$p(T)$$ to be the matrix $$c_nT^n+\dots+c_1T+I$$ (where $$I$$ is the appropriately-sized identity matrix). Prove that for any square matrix there is a polynomial such that $$p(T)$$ is the zero matrix.
3. The **minimal polynomial** $$m(x)$$ of a square matrix is the polynomial of least degree, and with leading coefficient $$1$$, such that $$m(T)$$ is the zero matrix. Find the minimal polynomial of this matrix.

$$
\begin{pmatrix} \sqrt{3}/2 &-1/2 \\ 1/2 &\sqrt{3}/2 \end{pmatrix}
$$

(This is the representation with respect to $$\mathcal{E}_2,\mathcal{E}_2$$, the standard basis, of a rotation through $$\pi/6$$ radians counterclockwise.)

**Problem 22**  —

The infinite-dimensional space $$\mathcal{P}$$ of all finite-degree polynomials gives a memorable example of the non-commutativity of linear maps. Let $$d/dx:\mathcal{P}\to \mathcal{P}$$ be the usual derivative and let $$s:\mathcal{P}\to \mathcal{P}$$ be the **shift** map.

$$
a_0+a_1x+\dots+a_nx^n \;\stackrel{s}{\longmapsto}\; 0+a_0x+a_1x^2+\dots+a_nx^{n+1}
$$

Show that the two maps don't commute $$d/dx\circ s\neq s\circ d/dx$$; in fact, not only is $$(d/dx\circ s)-(s\circ d/dx)$$ not the zero map, it is the identity map.

**Problem 23**  —

Recall the notation for the sum of the sequence of numbers $$a_1, a_2, \dots, a_n$$.

$$
\sum_{i=1}^{n}a_i=a_1+a_2+\dots+a_n
$$

In this notation, the $$i,j$$ entry of the product of $$G$$ and $$H$$ is this.

$$
p_{i,j}=\sum_{k=1}^{r} g_{i,k}h_{k,j}
$$

Using this notation,

1. reprove that matrix multiplication is associative;
2. reprove Theorem 2.6.

Solutions

---

*Source: Wikibooks, Linear Algebra/Matrix Multiplication (https://en.wikibooks.org/wiki/Linear_Algebra/Matrix_Multiplication), by Wikibooks contributors, CC BY-SA 4.0.*
