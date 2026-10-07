# The Permutation Expansion

The prior subsection defines a function to be a determinant if it satisfies four conditions and shows that there is at most one $$n \! \times \! n$$ determinant function for each $$n$$. What is left is to show that for each $$n$$ such a function exists.

How could such a function not exist? After all, we have done computations that start with a square matrix, follow the conditions, and end with a number.

The difficulty is that, as far as we know, the computation might not give a well-defined result. To illustrate this possibility, suppose that we were to change the second condition in the definition of determinant to be that the value of a determinant does not change on a row swap. By [Remark 2.2](Linear%20Algebra%20-%20Properties%20of%20Determinants.md) we know that this conflicts with the first and third conditions. Here is an instance of the conflict: here are two Gauss' method reductions of the same matrix, the first without any row swap

$$
\begin{pmatrix} 1 &2 \\ 3 &4 \end{pmatrix} \xrightarrow[]{-3\rho_1+\rho_2} \begin{pmatrix} 1 &2 \\ 0 &-2 \end{pmatrix}
$$

and the second with a swap.

$$
\begin{pmatrix} 1 &2 \\ 3 &4 \end{pmatrix} \xrightarrow[]{\rho_1\leftrightarrow\rho_2} \begin{pmatrix} 3 &4 \\ 1 &2 \end{pmatrix} \xrightarrow[]{-(1/3)\rho_1+\rho_2} \begin{pmatrix} 3 &4 \\ 0 &2/3 \end{pmatrix}
$$

Following [Definition 2.1](Linear%20Algebra%20-%20Properties%20of%20Determinants.md) gives that both calculations yield the determinant $$-2$$ since in the second one we keep track of the fact that the row swap changes the sign of the result of multiplying down the diagonal. But if we follow the supposition and change the second condition then the two calculations yield different values, $$-2$$ and $$2$$. That is, under the supposition the outcome would not be well-defined — no function exists that satisfies the changed second condition along with the other three.

Of course, observing that [Definition 2.1](Linear%20Algebra%20-%20Properties%20of%20Determinants.md) does the right thing in this one instance is not enough; what we will do in the rest of this section is to show that there is never a conflict. The natural way to try this would be to define the determinant function with: "The value of the function is the result of doing Gauss' method, keeping track of row swaps, and finishing by multiplying down the diagonal". (Since Gauss' method allows for some variation, such as a choice of which row to use when swapping, we would have to fix an explicit algorithm.) Then we would be done if we verified that this way of computing the determinant satisfies the four properties. For instance, if $$T$$ and $$\hat{T}$$ are related by a row swap then we would need to show that this algorithm returns determinants that are negatives of each other. However, how to verify this is not evident. So the development below will not proceed in this way. Instead, in this subsection we will define a different way to compute the value of a determinant, a formula, and we will use this way to prove that the conditions are satisfied.

The formula that we shall use is based on an insight gotten from property (3) of the definition of determinants. This property shows that determinants are not linear.

**Example 3.1**  —

For this matrix $$\det(2A)\neq 2\cdot\det(A)$$.

$$
A=\begin{pmatrix} 2 &1 \\ -1 &3 \end{pmatrix}
$$

Instead, the scalar comes out of each of the two rows.

$$
\begin{vmatrix} 4 &2 \\ -2 &6 \end{vmatrix} =2\cdot\begin{vmatrix} 2 &1 \\ -2 &6 \end{vmatrix} =4\cdot\begin{vmatrix} 2 &1 \\ -1 &3 \end{vmatrix}
$$

Since scalars come out a row at a time, we might guess that determinants are linear a row at a time.

**Definition 3.2**  —

Let $$V$$ be a vector space. A map $$f:V^n\to \mathbb{R}$$ is **multilinear** if

1. $$f(\vec{\rho}_1,\dots,\vec{v}+\vec{w}, \ldots,\vec{\rho}_n) =f(\vec{\rho}_1,\dots,\vec{v},\dots,\vec{\rho}_n) +f(\vec{\rho}_1,\dots,\vec{w},\dots,\vec{\rho}_n)$$
2. $$f(\vec{\rho}_1,\dots,k\vec{v},\dots,\vec{\rho}_n) =k\cdot f(\vec{\rho}_1,\dots,\vec{v},\dots,\vec{\rho}_n)$$

for $$\vec{v}, \vec{w}\in V$$ and $$k\in\mathbb{R}$$.

**Lemma 3.3**  —

Determinants are multilinear.

**Proof**  —

The definition of determinants gives property (2) ([Lemma 2.3](Linear%20Algebra%20-%20Properties%20of%20Determinants.md) following that definition covers the $$k=0$$ case) so we need only check property (1).

$$
\det(\vec{\rho}_1,\dots,\vec{v}+\vec{w}, \dots,\vec{\rho}_n) =\det(\vec{\rho}_1,\dots,\vec{v},\dots,\vec{\rho}_n) +\det(\vec{\rho}_1,\dots,\vec{w},\dots,\vec{\rho}_n)
$$

If the set $$\{\vec{\rho}_1,\dots,\vec{\rho}_{i-1},\vec{\rho}_{i+1}, \dots,\vec{\rho}_n\}$$ is linearly dependent then all three matrices are singular and so all three determinants are zero and the equality is trivial. Therefore assume that the set is linearly independent. This set of $$n$$-wide row vectors has $$n-1$$ members, so we can make a basis by adding one more vector $$\langle \vec{\rho}_1,\dots,\vec{\rho}_{i-1},\vec{\beta}, \vec{\rho}_{i+1},\dots,\vec{\rho}_n \rangle$$. Express $$\vec{v}$$ and $$\vec{w}$$ with respect to this basis

$$
\begin{array}{rl} \vec{v} &=v_1\vec{\rho}_1+\dots+v_{i-1}\vec{\rho}_{i-1}+v_i\vec{\beta} +v_{i+1}\vec{\rho}_{i+1}+\dots+v_n\vec{\rho}_n \\ \vec{w} &= w_1\vec{\rho}_1+\dots+w_{i-1}\vec{\rho}_{i-1}+w_i\vec{\beta} +w_{i+1}\vec{\rho}_{i+1}+\dots+w_n\vec{\rho}_n \end{array}
$$

giving this.

$$
\vec{v}+\vec{w} = (v_1+w_1)\vec{\rho}_1+\dots+(v_i+w_i)\vec{\beta} +\dots+(v_n+w_n)\vec{\rho}_n
$$

By the definition of determinant, the value of $$\det(\vec{\rho}_1,\dots,\vec{v}+\vec{w},\dots,\vec{\rho}_n)$$ is unchanged by the pivot operation of adding $$-(v_1+w_1)\vec{\rho}_1$$ to $$\vec{v}+\vec{w}$$.

$$
\vec{v}+\vec{w}-(v_1+w_1)\vec{\rho}_1 = (v_2+w_2)\vec{\rho}_2+\cdots+(v_i+w_i)\vec{\beta} +\dots+(v_n+w_n)\vec{\rho}_n
$$

Then, to the result, we can add $$-(v_2+w_2)\vec{\rho}_2$$, etc. Thus

$$
\det (\vec{\rho}_1,\dots,\vec{v}+\vec{w},\dots,\vec{\rho}_n)
$$

$$
\begin{align} &=\det (\vec{\rho}_1,\dots,(v_i+w_i)\cdot\vec{\beta},\dots,\vec{\rho}_n) \\ &=(v_i+w_i)\cdot\det (\vec{\rho}_1,\dots,\vec{\beta},\dots,\vec{\rho}_n) \\ &=v_i\cdot \det (\vec{\rho}_1,\dots,\vec{\beta},\dots,\vec{\rho}_n) +w_i\cdot \det (\vec{\rho}_1,\dots,\vec{\beta},\dots,\vec{\rho}_n) \end{align}
$$

(using (2) for the second equality). To finish, bring $$v_i$$ and $$w_i$$ back inside in front of $$\vec{\beta}$$ and use pivoting again, this time to reconstruct the expressions of $$\vec{v}$$ and $$\vec{w}$$ in terms of the basis, e.g., start with the pivot operations of adding $$v_1\vec{\rho}_1$$ to $$v_i\vec{\beta}$$ and $$w_1\vec{\rho}_1$$ to $$w_i\vec{\rho}_1$$, etc.

Multilinearity allows us to expand a determinant into a sum of determinants, each of which involves a simple matrix.

**Example 3.4**  —

We can use multilinearity to split this determinant into two, first breaking up the first row

$$
\begin{vmatrix} 2 &1 \\ 4 &3 \end{vmatrix} = \begin{vmatrix} 2 &0 \\ 4 &3 \end{vmatrix} + \begin{vmatrix} 0 &1 \\ 4 &3 \end{vmatrix}
$$

and then separating each of those two, breaking along the second rows.

$$
=\begin{vmatrix} 2 &0 \\ 4 &0 \end{vmatrix} + \begin{vmatrix} 2 &0 \\ 0 &3 \end{vmatrix} + \begin{vmatrix} 0 &1 \\ 4 &0 \end{vmatrix} + \begin{vmatrix} 0 &1 \\ 0 &3 \end{vmatrix}
$$

We are left with four determinants, such that in each row of each matrix there is a single entry from the original matrix.

**Example 3.5**  —

In the same way, a $$3 \! \times \! 3$$ determinant separates into a sum of many simpler determinants. We start by splitting along the first row, producing three determinants (the zero in the $$1,3$$ position is underlined to set it off visually from the zeroes that appear in the splitting).

$$
\begin{vmatrix} 2 &1 &-1 \\ 4 &3 &\underline{0} \\ 2 &1 &5 \end{vmatrix} = \begin{vmatrix} 2 &0 &0 \\ 4 &3 &\underline{0} \\ 2 &1 &5 \end{vmatrix} + \begin{vmatrix} 0 &1 &0 \\ 4 &3 &\underline{0} \\ 2 &1 &5 \end{vmatrix} + \begin{vmatrix} 0 &0 &-1 \\ 4 &3 &\underline{0} \\ 2 &1 &5 \end{vmatrix}
$$

Each of these three will itself split in three along the second row. Each of the resulting nine splits in three along the third row, resulting in twenty seven determinants

$$
= \begin{vmatrix} 2 &0 &0 \\ 4 &0 &0 \\ 2 &0 &0 \end{vmatrix} + \begin{vmatrix} 2 &0 &0 \\ 4 &0 &0 \\ 0 &1 &0 \end{vmatrix} + \begin{vmatrix} 2 &0 &0 \\ 4 &0 &0 \\ 0 &0 &5 \end{vmatrix} + \begin{vmatrix} 2 &0 &0 \\ 0 &3 &0 \\ 2 &0 &0 \end{vmatrix} +\dots+ \begin{vmatrix} 0 &0 &-1 \\ 0 &0 &\underline{0} \\ 0 &0 &5 \end{vmatrix}
$$

such that each row contains a single entry from the starting matrix.

So an $$n \! \times \! n$$ determinant expands into a sum of $$n^n$$ determinants where each row of each summands contains a single entry from the starting matrix. However, many of these summand determinants are zero.

**Example 3.6**  —

In each of these three matrices from the above expansion, two of the rows have their entry from the starting matrix in the same column, e.g., in the first matrix, the $$2$$ and the $$4$$ both come from the first column.

$$
\begin{vmatrix} 2 &0 &0 \\ 4 &0 &0 \\ 0 &1 &0 \end{vmatrix} \qquad \begin{vmatrix} 0 &0 &-1 \\ 0 &3 &0 \\ 0 &0 &5 \end{vmatrix} \qquad \begin{vmatrix} 0 &1 &0 \\ 0 &0 &\underline{0} \\ 0 &0 &5 \end{vmatrix}
$$

Any such matrix is singular, because in each, one row is a multiple of the other (or is a zero row). Thus, any such determinant is zero, by Lemma 2.3.

Therefore, the above expansion of the $$3 \! \times \! 3$$ determinant into the sum of the twenty seven determinants simplifies to the sum of these six.

$$
\begin{array}{rl} \begin{vmatrix} 2 &1 &-1 \\ 4 &3 &\underline{0} \\ 2 &1 &5 \end{vmatrix} &=\begin{vmatrix} 2 &0 &0 \\ 0 &3 &0 \\ 0 &0 &5 \end{vmatrix} + \begin{vmatrix} 2 &0 &0 \\ 0 &0 &\underline{0} \\ 0 &1 &0 \end{vmatrix} \\ &\quad+\begin{vmatrix} 0 &1 &0 \\ 4 &0 &0 \\ 0 &0 &5 \end{vmatrix} + \begin{vmatrix} 0 &1 &0 \\ 0 &0 &\underline{0} \\ 2 &0 &0 \end{vmatrix} \\ &\quad+\begin{vmatrix} 0 &0 &-1 \\ 4 &0 &0 \\ 0 &1 &0 \end{vmatrix} + \begin{vmatrix} 0 &0 &-1 \\ 0 &3 &0 \\ 2 &0 &0 \end{vmatrix} \end{array}
$$

We can bring out the scalars.

$$
\begin{array}{rl} &=(2)(3)(5)\begin{vmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{vmatrix} +(2)(\underline{0})(1)\begin{vmatrix} 1 &0 &0 \\ 0 &0 &1 \\ 0 &1 &0 \end{vmatrix} \\ &\quad+(1)(4)(5)\begin{vmatrix} 0 &1 &0 \\ 1 &0 &0 \\ 0 &0 &1 \end{vmatrix} +(1)(\underline{0})(2)\begin{vmatrix} 0 &1 &0 \\ 0 &0 &1 \\ 1 &0 &0 \end{vmatrix} \\ &\quad+(-1)(4)(1)\begin{vmatrix} 0 &0 &1 \\ 1 &0 &0 \\ 0 &1 &0 \end{vmatrix} +(-1)(3)(2)\begin{vmatrix} 0 &0 &1 \\ 0 &1 &0 \\ 1 &0 &0 \end{vmatrix} \end{array}
$$

To finish, we evaluate those six determinants by row-swapping them to the identity matrix, keeping track of the resulting sign changes.

$$
\begin{array}{rl} &=30\cdot (+1)+0\cdot (-1) \\ &\quad+20\cdot (-1)+0\cdot (+1) \\ &\quad -4\cdot (+1)-6\cdot (-1)=12 \end{array}
$$

That example illustrates the key idea. We've applied multilinearity to a $$3 \! \times \! 3$$ determinant to get $$3^3$$ separate determinants, each with one distinguished entry per row. We can drop most of these new determinants because the matrices are singular, with one row a multiple of another. We are left with the one-entry-per-row determinants also having only one entry per column (one entry from the original determinant, that is). And, since we can factor scalars out, we can further reduce to only considering determinants of one-entry-per-row-and-column matrices where the entries are ones.

These are permutation matrices. Thus, the determinant can be computed in this three-step way *(Step 1)* for each permutation matrix, multiply together the entries from the original matrix where that permutation matrix has ones, *(Step 2)* multiply that by the determinant of the permutation matrix and *(Step 3)* do that for all permutation matrices and sum the results together.

To state this as a formula, we introduce a notation for permutation matrices. Let $$\iota_j$$ be the row vector that is all zeroes except for a one in its $$j$$-th entry, so that the four-wide $$\iota_2$$ is $$\begin{pmatrix} 0 &1 &0 &0 \end{pmatrix}$$. We can construct permutation matrices by permuting — that is, scrambling — the numbers $$1$$, $$2$$, ..., $$n$$, and using them as indices on the $$\iota$$'s. For instance, to get a $$4 \! \times \! 4$$ permutation matrix matrix, we can scramble the numbers from $$1$$ to $$4$$ into this sequence $$\langle 3,2,1,4 \rangle$$ and take the corresponding row vector $$\iota$$'s.

$$
\begin{pmatrix} \iota_{3} \\ \iota_{2} \\ \iota_{1} \\ \iota_{4} \end{pmatrix}= \begin{pmatrix} 0 &0 &1 &0 \\ 0 &1 &0 &0 \\ 1 &0 &0 &0 \\ 0 &0 &0 &1 \end{pmatrix}
$$

**Definition 3.7**  —

An **$$n$$-permutation** is a sequence consisting of an arrangement of the numbers $$1$$, $$2$$, ..., $$n$$.

**Example 3.8**  —

The $$2$$-permutations are $$\phi_1=\langle 1,2 \rangle$$ and $$\phi_2=\langle 2,1 \rangle$$. These are the associated permutation matrices.

$$
P_{\phi_1} =\begin{pmatrix} \iota_1 \\ \iota_2 \end{pmatrix} =\begin{pmatrix} 1 &0 \\ 0 &1 \end{pmatrix} \qquad P_{\phi_2} =\begin{pmatrix} \iota_2 \\ \iota_1 \end{pmatrix} =\begin{pmatrix} 0 &1 \\ 1 &0 \end{pmatrix}
$$

We sometimes write permutations as functions, e.g., $$\phi_2(1)=2$$, and $$\phi_2(2)=1$$. Then the rows of $$P_{\phi_2}$$ are $$\iota_{\phi_2(1)}=\iota_2$$ and $$\iota_{\phi_2(2)}=\iota_1$$.

The $$3$$-permutations are $$\phi_1=\langle 1,2,3 \rangle$$, $$\phi_2=\langle 1,3,2 \rangle$$, $$\phi_3=\langle 2,1,3 \rangle$$, $$\phi_4=\langle 2,3,1 \rangle$$, $$\phi_5=\langle 3,1,2 \rangle$$, and $$\phi_6=\langle 3,2,1 \rangle$$. Here are two of the associated permutation matrices.

$$
P_{\phi_2} =\begin{pmatrix} \iota_1 \\ \iota_3 \\ \iota_2 \end{pmatrix} =\begin{pmatrix} 1 &0 &0 \\ 0 &0 &1 \\ 0 &1 &0 \end{pmatrix} \qquad P_{\phi_5} =\begin{pmatrix} \iota_3 \\ \iota_1 \\ \iota_2 \end{pmatrix} =\begin{pmatrix} 0 &0 &1 \\ 1 &0 &0 \\ 0 &1 &0 \end{pmatrix}
$$

For instance, the rows of $$P_{\phi_5}$$ are $$\iota_{\phi_5(1)}=\iota_3$$, $$\iota_{\phi_5(2)}=\iota_1$$, and $$\iota_{\phi_5(3)}=\iota_2$$.

**Definition 3.9**  —

The **permutation expansion** for determinants is

$$
\begin{vmatrix} t_{1,1} &t_{1,2} &\ldots &t_{1,n} \\ t_{2,1} &t_{2,2} &\ldots &t_{2,n} \\ &\vdots \\ t_{n,1} &t_{n,2} &\ldots &t_{n,n} \end{vmatrix} = \begin{array}{l} t_{1,\phi_1(1)}t_{2,\phi_1(2)}\cdots t_{n,\phi_1(n)}\left|P_{\phi_1}\right| \\[.5ex] \quad+t_{1,\phi_2(1)}t_{2,\phi_2(2)}\cdots t_{n,\phi_2(n)}\left|P_{\phi_2}\right| \\[.5ex] \quad\vdots \\ \quad+t_{1,\phi_k(1)}t_{2,\phi_k(2)}\cdots t_{n,\phi_k(n)}\left|P_{\phi_k}\right| \end{array}
$$

where $$\phi_1,\ldots,\phi_k$$ are all of the $$n$$-permutations.

This formula is often written in **summation notation**

$$
\left|T\right|= \sum_{\text{permutations }\phi}\!\!\!\! t_{1,\phi(1)}t_{2,\phi(2)}\cdots t_{n,\phi(n)} \left|P_{\phi}\right|
$$

read aloud as "the sum, over all permutations $$\phi$$, of terms having the form $$t_{1,\phi(1)}t_{2,\phi(2)}\cdots t_{n,\phi(n)} \left|P_{\phi}\right|$$". This phrase is just a restating of the three-step process *(Step 1)* for each permutation matrix, compute $$t_{1,\phi(1)}t_{2,\phi(2)}\cdots t_{n,\phi(n)}$$ *(Step 2)* multiply that by $$\left|P_{\phi}\right|$$ and *(Step 3)* sum all such terms together.

**Example 3.10**  —

The familiar formula for the determinant of a $$2 \! \times \! 2$$ matrix can be derived in this way.

$$
\begin{array}{rl} \begin{vmatrix} t_{1,1} &t_{1,2} \\ t_{2,1} &t_{2,2} \end{vmatrix} &= t_{1,1}t_{2,2}\cdot\left|P_{\phi_1}\right| + t_{1,2}t_{2,1}\cdot\left|P_{\phi_2}\right| \\ &= t_{1,1}t_{2,2}\cdot\begin{vmatrix} 1 &0 \\ 0 &1 \end{vmatrix} + t_{1,2}t_{2,1}\cdot\begin{vmatrix} 0 &1 \\ 1 &0 \end{vmatrix} \\ &=t_{1,1}t_{2,2}-t_{1,2}t_{2,1} \end{array}
$$

(the second permutation matrix takes one row swap to pass to the identity). Similarly, the formula for the determinant of a $$3 \! \times \! 3$$ matrix is this.

$$
\begin{array}{rl} \begin{vmatrix} t_{1,1} &t_{1,2} &t_{1,3} \\ t_{2,1} &t_{2,2} &t_{2,3} \\ t_{3,1} &t_{3,2} &t_{3,3} \end{vmatrix} &= \begin{align} &t_{1,1}t_{2,2}t_{3,3}\left|P_{\phi_1}\right| +t_{1,1}t_{2,3}t_{3,2}\left|P_{\phi_2}\right| +t_{1,2}t_{2,1}t_{3,3}\left|P_{\phi_3}\right| \\ &\quad +t_{1,2}t_{2,3}t_{3,1}\left|P_{\phi_4}\right| +t_{1,3}t_{2,1}t_{3,2}\left|P_{\phi_5}\right| +t_{1,3}t_{2,2}t_{3,1}\left|P_{\phi_6}\right| \end{align} \\ &= \begin{align} &t_{1,1}t_{2,2}t_{3,3} -t_{1,1}t_{2,3}t_{3,2} -t_{1,2}t_{2,1}t_{3,3} \\ &\quad +t_{1,2}t_{2,3}t_{3,1} +t_{1,3}t_{2,1}t_{3,2} -t_{1,3}t_{2,2}t_{3,1} \end{align} \end{array}
$$

Computing a determinant by permutation expansion usually takes longer than Gauss' method. However, here we are not trying to do the computation efficiently, we are instead trying to give a determinant formula that we can prove to be well-defined. While the permutation expansion is impractical for computations, it is useful in proofs. In particular, we can use it for the result that we are after.

**Theorem 3.11**  —

For each $$n$$ there is a $$n \! \times \! n$$ determinant function.

The proof is deferred to the following subsection. Also there is the proof of the next result (they share some features).

**Theorem 3.12**  —

The determinant of a matrix equals the determinant of its transpose.

The consequence of this theorem is that, while we have so far stated results in terms of rows (e.g., determinants are multilinear in their rows, row swaps change the signum, etc.), all of the results also hold in terms of columns. The final result gives examples.

**Corollary 3.13**  —

A matrix with two equal columns is singular. Column swaps change the sign of a determinant. Determinants are multilinear in their columns.

**Proof**  —

For the first statement, transposing the matrix results in a matrix with the same determinant, and with two equal rows, and hence a determinant of zero. The other two are proved in the same way.

We finish with a summary (although the final subsection contains the unfinished business of proving the two theorems). Determinant functions exist, are unique, and we know how to compute them. As for what determinants are about, perhaps these lines (Kemp 1982) help make it memorable.  
  
* Determinant none,  
Solution: lots or none.  
Determinant some,  
Solution: just one. *

### Exercises

*These summarize the notation used in this book for the $$2$$- and $$3$$- permutations.*

$$
\begin{array}{c|cc} i &1 &2 \\ \hline \phi_1(i) &1 &2 \\ \phi_2(i) &2 &1 \end{array} \qquad \begin{array}{c|ccc} i &1 &2 &3 \\ \hline \phi_1(i) &1 &2 &3 \\ \phi_2(i) &1 &3 &2 \\ \phi_3(i) &2 &1 &3 \\ \phi_4(i) &2 &3 &1 \\ \phi_5(i) &3 &1 &2 \\ \phi_6(i) &3 &2 &1 \end{array}
$$

*This exercise is recommended for all readers.*

**Problem 1**  —

Compute the determinant by using the permutation expansion.

1. $$\begin{vmatrix} 1 &2 &3 \\ 4 &5 &6 \\ 7 &8 &9 \end{vmatrix}$$
2. $$\begin{vmatrix} 2 &2 &1 \\ 3 &-1 &0 \\ -2 &0 &5 \end{vmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Compute these both with Gauss' method and with the permutation expansion formula.

1. $$\begin{vmatrix} 2 &1 \\ 3 &1 \end{vmatrix}$$
2. $$\begin{vmatrix} 0 &1 &4 \\ 0 &2 &3 \\ 1 &5 &1 \end{vmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

Use the permutation expansion formula to derive the formula for $$3 \! \times \! 3$$ determinants.

**Problem 4**  —

List all of the $$4$$-permutations.

**Problem 5**  —

A permutation, regarded as a function from the set $$\{1,..,n\}$$ to itself, is one-to-one and onto. Therefore, each permutation has an inverse.

1. Find the inverse of each $$2$$-permutation.
2. Find the inverse of each $$3$$-permutation.

**Problem 6**  —

Prove that $$f$$ is multilinear if and only if for all $$\vec{v},\vec{w}\in V$$ and $$k_1,k_2\in\mathbb{R}$$, this holds.

$$
f(\vec{\rho}_1,\dots,k_1\vec{v}_1+k_2\vec{v}_2, \dots,\vec{\rho}_n) = k_1f(\vec{\rho}_1,\dots,\vec{v}_1,\dots,\vec{\rho}_n)+ k_2f(\vec{\rho}_1,\dots,\vec{v}_2,\dots,\vec{\rho}_n)
$$

**Problem 7**  —

Find the only nonzero term in the permutation expansion of this matrix.

$$
\begin{vmatrix} 0 &1 &0 &0 \\ 1 &0 &1 &0 \\ 0 &1 &0 &1 \\ 0 &0 &1 &0 \end{vmatrix}
$$

Compute that determinant by finding the signum of the associated permutation.

**Problem 8**  —

How would determinants change if we changed property (4) of the definition to read that $$\left|I\right|=2$$?

**Problem 9**  —

Verify the second and third statements in Corollary 3.13.  
*This exercise is recommended for all readers.*

**Problem 10**  —

Show that if an $$n \! \times \! n$$ matrix has a nonzero determinant then any column vector $$\vec{v}\in\mathbb{R}^n$$ can be expressed as a linear combination of the columns of the matrix.

**Problem 11**  —

True or false: a matrix whose entries are only zeros or ones has a determinant equal to zero, one, or negative one. (Strang 1980)

**Problem 12**  —

1. Show that there are $$120$$ terms in the permutation expansion formula of a $$5 \! \times \! 5$$ matrix.
2. How many are sure to be zero if the $$1,2$$ entry is zero?

**Problem 13**  —

How many $$n$$-permutations are there?

**Problem 14**  —

A matrix $$A$$ is **skew-symmetric** if $${{A}^{\rm trans}}=-A$$, as in this matrix.

$$
A=\begin{pmatrix} 0 &3 \\ -3 &0 \end{pmatrix}
$$

Show that $$n \! \times \! n$$ skew-symmetric matrices with nonzero determinants exist only for even $$n$$.  
*This exercise is recommended for all readers.*

**Problem 15**  —

What is the smallest number of zeros, and the placement of those zeros, needed to ensure that a $$4 \! \times \! 4$$ matrix has a determinant of zero?  
*This exercise is recommended for all readers.*

**Problem 16**  —

If we have $$n$$ data points $$(x_1,y_1),(x_2,y_2),\dots\,,(x_n,y_n)$$ and want to find a polynomial $$p(x)=a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+\dots+a_1x+a_0$$ passing through those points then we can plug in the points to get an $$n$$ equation/$$n$$ unknown linear system. The matrix of coefficients for that system is called the **Vandermonde matrix**. Prove that the determinant of the transpose of that matrix of coefficients

$$
\begin{vmatrix} 1 &1 &\ldots &1 \\ x_1 &x_2 &\ldots &x_n \\ {x_1}^2 &{x_2}^2 &\ldots &{x_n}^2 \\ &\vdots \\ {x_1}^{n-1} &{x_2}^{n-1} &\ldots &{x_n}^{n-1} \end{vmatrix}
$$

equals the product, over all indices $$i,j\in\{1,\dots,n\}$$ with $$i<j$$, of terms of the form $$x_j-x_i$$. (This shows that the determinant is zero, and the linear system has no solution, if and only if the $$x_i$$'s in the data are not distinct.)

**Problem 17**  —

A matrix can be divided into **blocks**, as here,

$$
\left(\begin{array}{cc|c} 1 &2 &0 \\ 3 &4 &0 \\ \hline 0 &0 &-2 \end{array}\right)
$$

which shows four blocks, the square $$2 \! \times \! 2$$ and $$1 \! \times \! 1$$ ones in the upper left and lower right, and the zero blocks in the upper right and lower left. Show that if a matrix can be partitioned as

$$
T= \left(\begin{array}{c|c} J &Z_2 \\ \hline Z_1 &K \end{array}\right)
$$

where $$J$$ and $$K$$ are square, and $$Z_1$$ and $$Z_2$$ are all zeroes, then $$\left|T\right|=\left|J\right|\cdot\left|K\right|$$.  
*This exercise is recommended for all readers.*

**Problem 18**  —

Prove that for any $$n \! \times \! n$$ matrix $$T$$ there are at most $$n$$ distinct reals $$r$$ such that the matrix $$T-rI$$ has determinant zero (we shall use this result in Chapter Five).

**? Problem 19**  —

The nine positive digits can be arranged into $$3 \! \times \! 3$$ arrays in $$9!$$ ways. Find the sum of the determinants of these arrays. (Trigg 1963)

**Problem 20**  —

Show that

$$
\begin{vmatrix} x-2 &x-3 &x-4 \\ x+1 &x-1 &x-3 \\ x-4 &x-7 &x-10 \end{vmatrix}=0.
$$

(Silverman & Trigg 1963)

**? Problem 21**  —

Let $$S$$ be the sum of the integer elements of a magic square of order three and let $$D$$ be the value of the square considered as a determinant. Show that $$D/S$$ is an integer. (Trigg & Walker 1949)

**? Problem 22**  —

Show that the determinant of the $$n^2$$ elements in the upper left corner of the Pascal triangle

$$
\begin{array}{cccccc} 1 &1 &1 &1 &. &. \\ 1 &2 &3 &. &. \\ 1 &3 &. &. & & \\ 1 &. &. & & & \\ . \\ . \end{array}
$$

has the value unity. (Rupp & Aude 1931)

Solutions

### References

- Kemp, Franklin (1982), "Linear Equations", *American Mathematical Monthly*, American Mathematical Society: 608 {{citation}}: Unknown parameter |month= ignored (help).
- Silverman, D. L. (proposer); Trigg, C. W. (solver) (1963), "Quickie 237", *Mathematics Magazine*, **36** (1), American Mathematical Society {{citation}}: Unknown parameter |month= ignored (help).
- Strang, Gilbert (1980), *Linear Algebra and its Applications* (2nd ed.), Hartcourt Brace Javanovich
- Trigg, C. W. (proposer) (1963), "Quickie 307", *Mathematics Magazine*, **36** (1), American Mathematical Society: 77 {{citation}}: Unknown parameter |month= ignored (help).
- Trigg, C. W. (proposer); Walker, R. J. (solver) (1949), "Elementary Problem 813", *American Mathematical Monthly*, **56** (1), American Mathematical Society {{citation}}: Unknown parameter |month= ignored (help).
- Rupp, C. A. (proposer); Aude, H. T. R. (solver) (1931), "Problem 3468", *American Mathematical Monthly*, **37** (6), American Mathematical Society: 355 {{citation}}: Unknown parameter |month= ignored (help).

---

*Source: Wikibooks, Linear Algebra/The Permutation Expansion (https://en.wikibooks.org/wiki/Linear_Algebra/The_Permutation_Expansion), by Wikibooks contributors, CC BY-SA 4.0.*
