# Vector Spaces and Linear Systems

We will now reconsider linear systems and Gauss' method, aided by the tools and terms of this chapter. We will make three points.

For the first point, recall the first chapter's Linear Combination Lemma and its corollary: if two matrices are related by row operations $$A\longrightarrow\cdots\longrightarrow B$$ then each row of $$B$$ is a linear combination of the rows of $$A$$. That is, Gauss' method works by taking linear combinations of rows. Therefore, the right setting in which to study row operations in general, and Gauss' method in particular, is the following vector space.

**Definition 3.1**  —

The **row space** of a matrix is the span of the set of its rows. The **row rank** is the dimension of the row space, the number of linearly independent rows.

**Example 3.2**  —

If

$$
A=\begin{pmatrix} 2 &3 \\ 4 &6 \end{pmatrix}
$$

then $$\mathop{{\text{Rowspace}}}(A)$$ is this subspace of the space of two-component row vectors.

$$
\{c_1\cdot\begin{pmatrix} 2 &3 \end{pmatrix}+c_2\cdot\begin{pmatrix} 4 &6 \end{pmatrix} \,\big|\, c_1,c_2\in\mathbb{R} \}
$$

The linear dependence of the second on the first is obvious and so we can simplify this description to $$\{c\cdot\begin{pmatrix} 2 &3 \end{pmatrix}\,\big|\, c\in\mathbb{R} \}$$.

**Lemma 3.3**  —

If the matrices $$A$$ and $$B$$ are related by a row operation

$$
A\xrightarrow[]{\rho_i\leftrightarrow\rho_j}B \quad\text{or}\quad A\xrightarrow[]{k\rho_i}B \quad\text{or}\quad A\xrightarrow[]{k\rho_i+\rho_j}B
$$

(for $$i\neq j$$ and $$k\neq 0$$) then their row spaces are equal. Hence, row-equivalent matrices have the same row space, and hence also, the same row rank.

**Proof**  —

By the Linear Combination Lemma's corollary, each row of $$B$$ is in the row space of $$A$$. Further, $$\mathop{{\text{Rowspace}}}(B)\subseteq\mathop{{\text{Rowspace}}}(A)$$ because a member of the set $$\mathop{{\text{Rowspace}}}(B)$$ is a linear combination of the rows of $$B$$, which means it is a combination of a combination of the rows of $$A$$, and hence, by the Linear Combination Lemma, is also a member of $$\mathop{{\text{Rowspace}}}(A)$$.

For the other containment, recall that row operations are reversible: $$A\longrightarrow B$$ if and only if $$B\longrightarrow A$$. With that, $$\mathop{{\text{Rowspace}}}(A)\subseteq\mathop{{\text{Rowspace}}}(B)$$ also follows from the prior paragraph, and so the two sets are equal.

Thus, row operations leave the row space unchanged. But of course, Gauss' method performs the row operations systematically, with a specific goal in mind, echelon form.

**Lemma 3.4**  —

The nonzero rows of an echelon form matrix make up a linearly independent set.

**Proof**  —

A result in the first chapter, [Lemma One.III.2.5](Linear%20Algebra%20-%20Row%20Equivalence.md), states that in an echelon form matrix, no nonzero row is a linear combination of the other rows. This is a restatement of that result into new terminology.

Thus, in the language of this chapter, Gaussian reduction works by eliminating linear dependencies among rows, leaving the span unchanged, until no nontrivial linear relationships remain (among the nonzero rows). That is, Gauss' method produces a basis for the row space.

**Example 3.5**  —

From any matrix, we can produce a basis for the row space by performing Gauss' method and taking the nonzero rows of the resulting echelon form matrix. For instance,

$$
\begin{array}{rcl} \begin{pmatrix} 1 &3 &1 \\ 1 &4 &1 \\ 2 &0 &5 \end{pmatrix} &\xrightarrow[-2\rho_1+\rho_3]{-\rho_1+\rho_2} \;\xrightarrow[]{6\rho_2+\rho_3} &\begin{pmatrix} 1 &3 &1 \\ 0 &1 &0 \\ 0 &0 &3 \end{pmatrix} \end{array}
$$

produces the basis $$\langle \begin{pmatrix} 1 &3 &1 \end{pmatrix}, \begin{pmatrix} 0 &1 &0 \end{pmatrix}, \begin{pmatrix} 0 &0 &3 \end{pmatrix} \rangle$$ for the row space. This is a basis for the row space of both the starting and ending matrices, since the two row spaces are equal.

Using this technique, we can also find bases for spans not directly involving row vectors.

**Definition 3.6**  —

The **column space** of a matrix is the span of the set of its columns. The **column rank** is the dimension of the column space, the number of linearly independent columns.

Our interest in column spaces stems from our study of linear systems. An example is that this system

$$
\begin{array}{rcrcrcr} c_1 &+ &3c_2 &+ &7c_3 &= &d_1 \\ 2c_1 &+ &3c_2 &+ &8c_3 &= &d_2 \\ & &c_2 &+ &2c_3 &= &d_3 \\ 4c_1 & & &+ &4c_3 &= &d_4 \end{array}
$$

has a solution if and only if the vector of $$d$$'s is a linear combination of the other column vectors,

$$
c_1\begin{pmatrix} 1 \\ 2 \\ 0 \\ 4 \end{pmatrix} +c_2\begin{pmatrix} 3 \\ 3 \\ 1 \\ 0 \end{pmatrix} +c_3\begin{pmatrix} 7 \\ 8 \\ 2 \\ 4 \end{pmatrix} =\begin{pmatrix} d_1 \\ d_2 \\ d_3 \\ d_4 \end{pmatrix}
$$

meaning that the vector of $$d$$'s is in the column space of the matrix of coefficients.

**Example 3.7**  —

Given this matrix,

$$
\begin{pmatrix} 1 &3 &7 \\ 2 &3 &8 \\ 0 &1 &2 \\ 4 &0 &4 \end{pmatrix}
$$

to get a basis for the column space, temporarily turn the columns into rows and reduce.

$$
\begin{array}{rcl} \begin{pmatrix} 1 &2 &0 &4 \\ 3 &3 &1 &0 \\ 7 &8 &2 &4 \end{pmatrix} &\xrightarrow[-7\rho_1+\rho_3]{-3\rho_1+\rho_2} \;\xrightarrow[]{-2\rho_2+\rho_3} &\begin{pmatrix} 1 &2 &0 &4 \\ 0 &-3 &1 &-12\\ 0 &0 &0 &0 \end{pmatrix} \end{array}
$$

Now turn the rows back to columns.

$$
\langle \begin{pmatrix} 1 \\ 2 \\ 0 \\ 4 \end{pmatrix}, \begin{pmatrix} 0 \\ -3 \\ 1 \\ -12 \end{pmatrix} \rangle
$$

The result is a basis for the column space of the given matrix.

**Definition 3.8**  —

The **transpose** of a matrix is the result of interchanging the rows and columns of that matrix. That is, column $$j$$ of the matrix $$A$$ is row $$j$$ of $${{A}^{\rm trans}}$$, and vice versa.

So the instructions for the prior example are "transpose, reduce, and transpose back".

We can even, at the price of tolerating the as-yet-vague idea of vector spaces being "the same", use Gauss' method to find bases for spans in other types of vector spaces.

**Example 3.9**  —

To get a basis for the span of $$\{x^2+x^4,2x^2+3x^4,-x^2-3x^4\}$$ in the space $$\mathcal{P}_4$$, think of these three polynomials as "the same" as the row vectors $$\begin{pmatrix} 0 &0 &1 &0 &1 \end{pmatrix}$$, $$\begin{pmatrix} 0 &0 &2 &0 &3 \end{pmatrix}$$, and $$\begin{pmatrix} 0 &0 &-1 &0 &-3 \end{pmatrix}$$, apply Gauss' method

$$
\begin{array}{rcl} \begin{pmatrix} 0 &0 &1 &0 &1 \\ 0 &0 &2 &0 &3 \\ 0 &0 &-1 &0 &-3 \end{pmatrix} &\xrightarrow[\rho_1+\rho_3]{-2\rho_1+\rho_2} \;\xrightarrow[]{2\rho_2+\rho_3} &\begin{pmatrix} 0 &0 &1 &0 &1 \\ 0 &0 &0 &0 &1 \\ 0 &0 &0 &0 &0 \end{pmatrix} \end{array}
$$

and translate back to get the basis $$\langle x^2+x^4,x^4 \rangle$$. (As mentioned earlier, we will make the phrase "the same" precise at the start of the next chapter.)

Thus, our first point in this subsection is that the tools of this chapter give us a more conceptual understanding of Gaussian reduction.

For the second point of this subsection, consider the effect on the column space of this row reduction.

$$
\begin{array}{rcl} \begin{pmatrix} 1 &2 \\ 2 &4 \end{pmatrix} &\xrightarrow[]{-2\rho_1+\rho_2} &\begin{pmatrix} 1 &2 \\ 0 &0 \end{pmatrix} \end{array}
$$

The column space of the left-hand matrix contains vectors with a second component that is nonzero. But the column space of the right-hand matrix is different because it contains only vectors whose second component is zero. It is this knowledge that row operations can change the column space that makes next result surprising.

**Lemma 3.10**  —

Row operations do not change the column rank.

**Proof**  —

Restated, if $$A$$ reduces to $$B$$ then the column rank of $$B$$ equals the column rank of $$A$$.

We will be done if we can show that row operations do not affect linear relationships among columns (e.g., if the fifth column is twice the second plus the fourth before a row operation then that relationship still holds afterwards), because the column rank is just the size of the largest set of unrelated columns. But this is exactly the first theorem of this book: in a relationship among columns,

$$
c_1\cdot\begin{pmatrix} a_{1,1} \\ a_{2,1} \\ \vdots \\ a_{m,1} \end{pmatrix} +\dots+ c_n\cdot \begin{pmatrix} a_{1,n} \\ a_{2,n} \\ \vdots \\ a_{m,n} \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix}
$$

row operations leave unchanged the set of solutions $$(c_1,\ldots,c_n)$$.

Another way, besides the prior result, to state that Gauss' method has something to say about the column space as well as about the row space is to consider again Gauss-Jordan reduction. Recall that it ends with the reduced echelon form of a matrix, as here.

$$
\begin{array}{rcl} \begin{pmatrix} 1 &3 &1 &6 \\ 2 &6 &3 &16 \\ 1 &3 &1 &6 \end{pmatrix} &\xrightarrow[]{}\;\cdots\;\xrightarrow[]{} &\begin{pmatrix} 1 &3 &0 &2 \\ 0 &0 &1 &4 \\ 0 &0 &0 &0 \end{pmatrix} \end{array}
$$

Consider the row space and the column space of this result. Our first point made above says that a basis for the row space is easy to get: simply collect together all of the rows with leading entries. However, because this is a reduced echelon form matrix, a basis for the column space is just as easy: take the columns containing the leading entries, that is, $$\langle \vec{e}_1,\vec{e}_2 \rangle$$. (Linear independence is obvious. The other columns are in the span of this set, since they all have a third component of zero.) Thus, for a reduced echelon form matrix, bases for the row and column spaces can be found in essentially the same way— by taking the parts of the matrix, the rows or columns, containing the leading entries.

**Theorem 3.11**  —

The row rank and column rank of a matrix are equal.

**Proof**  —

First bring the matrix to reduced echelon form. At that point, the row rank equals the number of leading entries since that equals the number of nonzero rows. Also at that point, the number of leading entries equals the column rank because the set of columns containing leading entries consists of some of the $$\vec{e}_i$$'s from a standard basis, and that set is linearly independent and spans the set of columns. Hence, in the reduced echelon form matrix, the row rank equals the column rank, because each equals the number of leading entries.

But Lemma 3.3 and Lemma 3.10 show that the row rank and column rank are not changed by using row operations to get to reduced echelon form. Thus the row rank and the column rank of the original matrix are also equal.

**Definition 3.12**  —

The **rank** of a matrix is its row rank or column rank.

So our second point in this subsection is that the column space and row space of a matrix have the same dimension. Our third and final point is that the concepts that we've seen arising naturally in the study of vector spaces are exactly the ones that we have studied with linear systems.

**Theorem 3.13**  —

For linear systems with $$n$$ unknowns and with matrix of coefficients $$A$$, the statements

1. the rank of $$A$$ is $$r$$
2. the space of solutions of the associated homogeneous system has dimension $$n-r$$

are equivalent.  
So if the system has at least one particular solution then for the set of solutions, the number of parameters equals $$n-r$$, the number of variables minus the rank of the matrix of coefficients.

**Proof**  —

The rank of $$A$$ is $$r$$ if and only if Gaussian reduction on $$A$$ ends with $$r$$ nonzero rows. That's true if and only if echelon form matrices row equivalent to $$A$$ have $$r$$-many leading variables. That in turn holds if and only if there are $$n-r$$ free variables.

**Remark 3.14**  — (Munkres 1964)

Sometimes that result is mistakenly remembered to say that the general solution of an $$n$$ unknown system of $$m$$ equations uses $$n-m$$ parameters. The number of equations is not the relevant figure, rather, what matters is the number of independent equations (the number of equations in a maximal independent set). Where there are $$r$$ independent equations, the general solution involves $$n-r$$ parameters.

**Corollary 3.15**  —

Where the matrix $$A$$ is $$n \! \times \! n$$, the statements

1. the rank of $$A$$ is $$n$$
2. $$A$$ is nonsingular
3. the rows of $$A$$ form a linearly independent set
4. the columns of $$A$$ form a linearly independent set
5. any linear system whose matrix of coefficients is $$A$$ has one and only one solution

are equivalent.

**Proof**  —

Clearly $$\text{(1)}\iff\text{(2)}\iff\text{(3)}\iff\text{(4)}$$. The last, $$\text{(4)}\iff\text{(5)}$$, holds because a set of $$n$$ column vectors that have $$n$$ components is linearly independent if and only if it is a basis for $$\mathbb{R}^n$$, but the system

$$
c_1\begin{pmatrix} a_{1,1} \\ a_{2,1} \\ \vdots \\ a_{m,1} \end{pmatrix} +\dots+ c_n\begin{pmatrix} a_{1,n} \\ a_{2,n} \\ \vdots \\ a_{m,n} \end{pmatrix} =\begin{pmatrix} d_1 \\ d_2 \\ \vdots \\ d_m \end{pmatrix}
$$

has a unique solution for all choices of $$d_1,\dots,d_n\in\mathbb{R}$$ if and only if the vectors of $$a$$'s form a basis.

### Exercises

**Problem 1**  —

Transpose each.

1. $$\begin{pmatrix} 2 &1 \\ 3 &1 \end{pmatrix}$$
2. $$\begin{pmatrix} 2 &1 \\ 1 &3 \end{pmatrix}$$
3. $$\begin{pmatrix} 1 &4 &3 \\ 6 &7 &8 \end{pmatrix}$$
4. $$\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
5. $$\begin{pmatrix} -1 &-2 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Decide if the vector is in the row space of the matrix.

1. $$\begin{pmatrix} 2 &1 \\ 3 &1 \end{pmatrix}$$, $$\begin{pmatrix} 1 &0 \end{pmatrix}$$
2. $$\begin{pmatrix} 0 &1 &3 \\ -1 &0 &1 \\ -1 &2 &7 \end{pmatrix}$$, $$\begin{pmatrix} 1 &1 &1 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

Decide if the vector is in the column space.

1. $$\begin{pmatrix} 1 &1 \\ 1 &1 \end{pmatrix}$$, $$\begin{pmatrix} 1 \\ 3 \end{pmatrix}$$
2. $$\begin{pmatrix} 1 &3 &1 \\ 2 &0 &4 \\ 1 &-3 &-3 \end{pmatrix}$$, $$\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 4**  —

Find a basis for the row space of this matrix.  

$$
\begin{pmatrix} 2 &0 &3 &4 \\ 0 &1 &1 &-1 \\ 3 &1 &0 &2 \\ 1 &0 &-4 &-1 \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 5**  —

Find the rank of each matrix.

1. $$\begin{pmatrix} 2 &1 &3 \\ 1 &-1 &2 \\ 1 &0 &3 \end{pmatrix}$$
2. $$\begin{pmatrix} 1 &-1 &2 \\ 3 &-3 &6 \\ -2 &2 &-4 \end{pmatrix}$$
3. $$\begin{pmatrix} 1 &3 &2 \\ 5 &1 &1 \\ 6 &4 &3 \end{pmatrix}$$
4. $$\begin{pmatrix} 0 &0 &0 \\ 0 &0 &0 \\ 0 &0 &0 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 6**  —

Find a basis for the span of each set.

1. $$\{\begin{pmatrix} 1 &3 \end{pmatrix}, \begin{pmatrix} -1 &3 \end{pmatrix}, \begin{pmatrix} 1 &4 \end{pmatrix}, \begin{pmatrix} 2 &1 \end{pmatrix} \}\subseteq\mathcal{M}_{1 \! \times \! 2}$$
2. $$\{\begin{pmatrix} 1 \\2 \\1 \end{pmatrix}, \begin{pmatrix} 3 \\ 1 \\ -1 \end{pmatrix}, \begin{pmatrix} 1 \\ -3 \\ -3 \end{pmatrix} \}\subseteq\mathbb{R}^3$$
3. $$\{1+x,1-x^2,3+2x-x^2\}\subseteq\mathcal{P}_3$$
4. $$\{ \begin{pmatrix} 1 &0 &1 \\ 3 &1 &-1 \end{pmatrix}, \begin{pmatrix} 1 &0 &3 \\ 2 &1 &4 \end{pmatrix}, \begin{pmatrix} -1 &0 &-5 \\ -1 &-1 &-9 \end{pmatrix} \} \subseteq\mathcal{M}_{2 \! \times \! 3}$$

**Problem 7**  —

Which matrices have rank zero? Rank one?  
*This exercise is recommended for all readers.*

**Problem 8**  —

Given $$a,b,c\in\mathbb{R}$$, what choice of $$d$$ will cause this matrix to have the rank of one?

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix}
$$

**Problem 9**  —

Find the column rank of this matrix.

$$
\begin{pmatrix} 1 &3 &-1 &5 &0 &4 \\ 2 &0 &1 &0 &4 &1 \end{pmatrix}
$$

**Problem 10**  —

Show that a linear system with at least one solution has at most one solution if and only if the matrix of coefficients has rank equal to the number of its columns.  
*This exercise is recommended for all readers.*

**Problem 11**  —

If a matrix is $$5 \! \times \! 9$$, which set must be dependent, its set of rows or its set of columns?

**Problem 12**  —

Give an example to show that, despite that they have the same dimension, the row space and column space of a matrix need not be equal. Are they ever equal?

**Problem 13**  —

Show that the set $$\{(1,-1,2,-3),(1,1,2,0),(3,-1,6,-6)\}$$ does not have the same span as $$\{(1,0,1,0),(0,2,0,3)\}$$. What, by the way, is the vector space?  
*This exercise is recommended for all readers.*

**Problem 14**  —

Show that this set of column vectors

$$
\left\{\begin{pmatrix} d_1 \\ d_2 \\ d_3 \end{pmatrix} \,\big|\, \text{there are }x, y, \text{ and } z \text{ such that } \begin{array}{rcrcrcr} 3x &+ &2y &+ &4z &= &d_1 \\ x & & &- &z &= &d_2 \\ 2x &+ &2y &+ &5z &= &d_3 \end{array} \right\}
$$

is a subspace of $$\mathbb{R}^3$$. Find a basis.

**Problem 15**  —

Show that the transpose operation is **linear**:

$$
{{(rA+sB)}^{\rm trans}} = r{{A}^{\rm trans}}+s{{B}^{\rm trans}}
$$

for $$r,s\in\mathbb{R}$$ and $$A,B\in\mathcal{M}_{m \! \times \! n}$$.  
*This exercise is recommended for all readers.*

**Problem 16**  —

In this subsection we have shown that Gaussian reduction finds a basis for the row space.

1. Show that this basis is not unique— different reductions may yield different bases.
2. Produce matrices with equal row spaces but unequal numbers of rows.
3. Prove that two matrices have equal row spaces if and only if after Gauss-Jordan reduction they have the same nonzero rows.

**Problem 17**  —

Why is there not a problem with Remark 3.14 in the case that $$r$$ is bigger than $$n$$?

**Problem 18**  —

Show that the row rank of an $$m \! \times \! n$$ matrix is at most $$m$$. Is there a better bound?  
*This exercise is recommended for all readers.*

**Problem 19**  —

Show that the rank of a matrix equals the rank of its transpose.

**Problem 20**  —

True or false: the column space of a matrix equals the row space of its transpose.  
*This exercise is recommended for all readers.*

**Problem 21**  —

We have seen that a row operation may change the column space. Must it?

**Problem 22**  —

Prove that a linear system has a solution if and only if that system's matrix of coefficients has the same rank as its augmented matrix.

**Problem 23**  —

An $$m \! \times \! n$$ matrix has **full row rank** if its row rank is $$m$$, and it has **full column rank** if its column rank is $$n$$.

1. Show that a matrix can have both full row rank and full column rank only if it is square.
2. Prove that the linear system with matrix of coefficients $$A$$ has a solution for any $$d_1$$, ..., $$d_m$$'s on the right side if and only if $$A$$ has full row rank.
3. Prove that a homogeneous system has a unique solution if and only if its matrix of coefficients $$A$$ has full column rank.
4. Prove that the statement "if a system with matrix of coefficients $$A$$ has any solution then it has a unique solution" holds if and only if $$A$$ has full column rank.

**Problem 24**  —

How would the conclusion of Lemma 3.3 change if Gauss' method is changed to allow multiplying a row by zero?  
*This exercise is recommended for all readers.*

**Problem 25**  —

What is the relationship between $$\mathop{\text{rank}}(A)$$ and $$\mathop{\text{rank}}(-A)$$? Between $$\mathop{\text{rank}}(A)$$ and $$\mathop{\text{rank}}(kA)$$? What, if any, is the relationship between $$\mathop{\text{rank}}(A)$$, $$\mathop{\text{rank}}(B)$$, and $$\mathop{\text{rank}}(A+B)$$?

Solutions

### References

- Munkres, James R. (1964), *Elementary Linear Algebra*, Addison-Wesley.

---

*Source: Wikibooks, Linear Algebra/Vector Spaces and Linear Systems (https://en.wikibooks.org/wiki/Linear_Algebra/Vector_Spaces_and_Linear_Systems), by Wikibooks contributors, CC BY-SA 4.0.*
