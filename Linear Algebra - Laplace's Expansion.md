# Laplace's Expansion

**Example 1.1**  —

In this permutation expansion

$$
\begin{array}{rl} \begin{vmatrix} t_{1,1} &t_{1,2} &t_{1,3} \\ t_{2,1} &t_{2,2} &t_{2,3} \\ t_{3,1} &t_{3,2} &t_{3,3} \end{vmatrix} &=\begin{align} &t_{1,1}t_{2,2}t_{3,3}\begin{vmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{vmatrix} +t_{1,1}t_{2,3}t_{3,2}\begin{vmatrix} 1 &0 &0 \\ 0 &0 &1 \\ 0 &1 &0 \end{vmatrix} \\ &\quad +t_{1,2}t_{2,1}t_{3,3}\begin{vmatrix} 0 &1 &0 \\ 1 &0 &0 \\ 0 &0 &1 \end{vmatrix} +t_{1,2}t_{2,3}t_{3,1}\begin{vmatrix} 0 &1 &0 \\ 0 &0 &1 \\ 1 &0 &0 \end{vmatrix} \\ &\quad +t_{1,3}t_{2,1}t_{3,2}\begin{vmatrix} 0 &0 &1 \\ 1 &0 &0 \\ 0 &1 &0 \end{vmatrix} +t_{1,3}t_{2,2}t_{3,1}\begin{vmatrix} 0 &0 &1 \\ 0 &1 &0 \\ 1 &0 &0 \end{vmatrix} \end{align} \end{array}
$$

we can, for instance, factor out the entries from the first row

$$
\begin{array}{rl} &=t_{1,1}\cdot \left[t_{2,2}t_{3,3}\begin{vmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{vmatrix} +t_{2,3}t_{3,2}\begin{vmatrix} 1 &0 &0 \\ 0 &0 &1 \\ 0 &1 &0 \end{vmatrix}\,\right] \\ &\quad +t_{1,2}\cdot \left[t_{2,1}t_{3,3}\begin{vmatrix} 0 &1 &0 \\ 1 &0 &0 \\ 0 &0 &1 \end{vmatrix} +t_{2,3}t_{3,1}\begin{vmatrix} 0 &1 &0 \\ 0 &0 &1 \\ 1 &0 &0 \end{vmatrix}\,\right] \\ &\quad +t_{1,3}\cdot \left[t_{2,1}t_{3,2}\begin{vmatrix} 0 &0 &1 \\ 1 &0 &0 \\ 0 &1 &0 \end{vmatrix} +t_{2,2}t_{3,1}\begin{vmatrix} 0 &0 &1 \\ 0 &1 &0 \\ 1 &0 &0 \end{vmatrix}\,\right] \end{array}
$$

and swap rows in the permutation matrices to get this.

$$
\begin{array}{rl} &=t_{1,1}\cdot \left[t_{2,2}t_{3,3}\begin{vmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{vmatrix} +t_{2,3}t_{3,2}\begin{vmatrix} 1 &0 &0 \\ 0 &0 &1 \\ 0 &1 &0 \end{vmatrix}\,\right] \\ &\quad -t_{1,2}\cdot \left[t_{2,1}t_{3,3}\begin{vmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{vmatrix} +t_{2,3}t_{3,1}\begin{vmatrix} 1 &0 &0 \\ 0 &0 &1 \\ 0 &1 &0 \end{vmatrix}\,\right] \\ &\quad +t_{1,3}\cdot \left[t_{2,1}t_{3,2}\begin{vmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{vmatrix} +t_{2,2}t_{3,1}\begin{vmatrix} 1 &0 &0 \\ 0 &0 &1 \\ 0 &1 &0 \end{vmatrix}\,\right] \end{array}
$$

The point of the swapping (one swap to each of the permutation matrices on the second line and two swaps to each on the third line) is that the three lines simplify to three terms.

$$
=t_{1,1}\cdot \begin{vmatrix} t_{2,2} &t_{2,3} \\ t_{3,2} &t_{3,3} \end{vmatrix} -t_{1,2}\cdot \begin{vmatrix} t_{2,1} &t_{2,3} \\ t_{3,1} &t_{3,3} \end{vmatrix} +t_{1,3}\cdot \begin{vmatrix} t_{2,1} &t_{2,2} \\ t_{3,1} &t_{3,2} \end{vmatrix}
$$

The formula given in Theorem 1.5, which generalizes this example, is a **recurrence** — the determinant is expressed as a combination of determinants. This formula isn't circular because, as here, the determinant is expressed in terms of determinants of matrices of smaller size.

**Definition 1.2**  —

For any $$n \! \times \! n$$ matrix $$T$$, the $$(n-1) \! \times \! (n-1)$$ matrix formed by deleting row $$i$$ and column $$j$$ of $$T$$ is the $$i,j$$ **minor** of $$T$$. The $$i,j$$ **cofactor** $$T_{i,j}$$ of $$T$$ is $$(-1)^{i+j}$$ times the determinant of the $$i,j$$ minor of $$T$$.

**Example 1.3**  —

The $$1,2$$ cofactor of the matrix from Example 1.1 is the negative of the second $$2 \! \times \! 2$$ determinant.

$$
T_{1,2}= -1\cdot\begin{vmatrix} t_{2,1} &t_{2,3} \\ t_{3,1} &t_{3,3} \end{vmatrix}
$$

**Example 1.4**  —

Where

$$
T= \begin{pmatrix} 1 &2 &3 \\ 4 &5 &6 \\ 7 &8 &9 \end{pmatrix}
$$

these are the $$1,2$$ and $$2,2$$ cofactors.

$$
T_{1,2}= (-1)^{1+2}\cdot\begin{vmatrix} 4 &6 \\ 7 &9 \end{vmatrix}=6 \qquad T_{2,2}= (-1)^{2+2}\cdot\begin{vmatrix} 1 &3 \\ 7 &9 \end{vmatrix}=-12
$$

**Theorem 1.5 (Laplace Expansion of Determinants)**  —

Where $$T$$ is an $$n \! \times \! n$$ matrix, the determinant can be found by expanding by cofactors on row $$i$$ or column $$j$$.

$$
\begin{array}{rl} \left|T\right| &=t_{i,1}\cdot T_{i,1}+t_{i,2}\cdot T_{i,2}+\cdots+t_{i,n}\cdot T_{i,n} \\ &=t_{1,j}\cdot T_{1,j}+t_{2,j}\cdot T_{2,j}+\cdots+t_{n,j}\cdot T_{n,j} \end{array}
$$

**Proof**  —

Problem 15.

**Example 1.6**  —

We can compute the determinant

$$
\left|T\right|= \begin{vmatrix} 1 &2 &3 \\ 4 &5 &6 \\ 7 &8 &9 \end{vmatrix}
$$

by expanding along the first row, as in Example 1.1.

$$
\left|T\right| =1\cdot(+1)\begin{vmatrix} 5 &6 \\ 8 &9 \end{vmatrix} +2\cdot(-1)\begin{vmatrix} 4 &6 \\ 7 &9 \end{vmatrix} +3\cdot(+1)\begin{vmatrix} 4 &5 \\ 7 &8 \end{vmatrix} =-3+12-9 =0
$$

Alternatively, we can expand down the second column.

$$
\left|T\right| =2\cdot(-1)\begin{vmatrix} 4 &6 \\ 7 &9 \end{vmatrix} +5\cdot(+1)\begin{vmatrix} 1 &3 \\ 7 &9 \end{vmatrix} +8\cdot(-1)\begin{vmatrix} 1 &3 \\ 4 &6 \end{vmatrix} =12-60+48 =0
$$

**Example 1.7**  —

A row or column with many zeroes suggests a Laplace expansion.

$$
\begin{vmatrix} 1 &5 &0 \\ 2 &1 &1 \\ 3 &-1 &0 \end{vmatrix} = 0\cdot(+1)\begin{vmatrix} 2 &1 \\ 3 &-1 \end{vmatrix}+ 1\cdot(-1)\begin{vmatrix} 1 &5 \\ 3 &-1 \end{vmatrix}+ 0\cdot(+1)\begin{vmatrix} 1 &5 \\ 2 &1 \end{vmatrix} =16
$$

We finish by applying this result to derive a new formula for the inverse of a matrix. With Theorem 1.5, the determinant of an $$n \! \times \! n$$ matrix $$T$$ can be calculated by taking linear combinations of entries from a row and their associated cofactors.

$$
t_{i,1}\cdot T_{i,1}+t_{i,2}\cdot T_{i,2}+\dots+t_{i,n}\cdot T_{i,n} =\left|T\right| \qquad (*)
$$

Recall that a matrix with two identical rows has a zero determinant. Thus, for any matrix $$T$$, weighing the cofactors by entries from the "wrong" row — row $$k$$ with $$k\neq i$$ — gives zero

$$
t_{i,1}\cdot T_{k,1}+t_{i,2}\cdot T_{k,2}+\dots+t_{i,n}\cdot T_{k,n}=0 \qquad (**)
$$

because it represents the expansion along the row $$k$$ of a matrix with row $$i$$ equal to row $$k$$. This equation summarizes ($$*$$) and ($$**$$).

$$
\left( \begin{array}{cccc} t_{1,1} &t_{1,2} &\ldots &t_{1,n}\\ t_{2,1} &t_{2,2} &\ldots &t_{2,n} \\ &\vdots\\ t_{n,1} &t_{n,2} &\ldots &t_{n,n} \end{array} \right) \begin{pmatrix} T_{1,1} &T_{2,1} &\ldots &T_{n,1} \\ T_{1,2} &T_{2,2} &\ldots &T_{n,2} \\ &\vdots & & \\ T_{1,n} &T_{2,n} &\ldots &T_{n,n} \end{pmatrix} =\begin{pmatrix} |T| &0 &\ldots &0 \\ 0 &|T| &\ldots &0 \\ &\vdots & & \\ 0 &0 &\ldots &|T| \end{pmatrix}
$$

Note that the order of the subscripts in the matrix of cofactors is opposite to the order of subscripts in the other matrix; e.g., along the first row of the matrix of cofactors the subscripts are $$1,1$$ then $$2,1$$, etc.

**Definition 1.8**  —

The matrix **adjoint** to the square matrix $$T$$ is

$$
\text{adj}\,(T)= \begin{pmatrix} T_{1,1} &T_{2,1} &\ldots &T_{n,1} \\ T_{1,2} &T_{2,2} &\ldots &T_{n,2} \\ &\vdots & & \\ T_{1,n} &T_{2,n} &\ldots &T_{n,n} \end{pmatrix}
$$

where $$T_{j,i}$$ is the $$j,i$$ cofactor.

**Theorem 1.9**  —

Where $$T$$ is a square matrix, $$T\cdot \text{adj}\,(T)=\text{adj}\,(T)\cdot T=\left|T\right|\cdot I$$.

**Proof**  —

Equations ($$*$$) and ($$**$$).

**Example 1.10**  —

If

$$
T=\begin{pmatrix} 1 &0 &4 \\ 2 &1 &-1 \\ 1 &0 &1 \end{pmatrix}
$$

then the adjoint $$\text{adj}\,(T)$$ is

$$
\begin{pmatrix} T_{1,1} &T_{2,1} &T_{3,1} \\ T_{1,2} &T_{2,2} &T_{3,2} \\ T_{1,3} &T_{2,3} &T_{3,3} \end{pmatrix} \!\!=\!\!\begin{pmatrix} \begin{vmatrix} 1 &-1 \\ 0 &1 \end{vmatrix} &-\begin{vmatrix} 0 &4 \\ 0 &1 \end{vmatrix} &\begin{vmatrix} 0 &4 \\ 1 &-1 \end{vmatrix} \\ -\begin{vmatrix} 2 &-1 \\ 1 &1 \end{vmatrix} &\begin{vmatrix} 1 &4 \\ 1 &1 \end{vmatrix} &-\begin{vmatrix} 1 &4 \\ 2 &-1 \end{vmatrix} \\ \begin{vmatrix} 2 &1 \\ 1 &0 \end{vmatrix} &-\begin{vmatrix} 1 &0 \\ 1 &0 \end{vmatrix} &\begin{vmatrix} 1 &0 \\ 2 &1 \end{vmatrix} \end{pmatrix} \!\!=\! \begin{pmatrix} 1 &0 &-4 \\ -3 &-3 &9 \\ -1 &0 &1 \end{pmatrix}
$$

and taking the product with $$T$$ gives the diagonal matrix $$\left|T\right|\cdot I$$.

$$
\begin{pmatrix} 1 &0 &4 \\ 2 &1 &-1 \\ 1 &0 &1 \end{pmatrix} \begin{pmatrix} 1 &0 &-4 \\ -3 &-3 &9 \\ -1 &0 &1 \end{pmatrix} =\begin{pmatrix} -3 &0 &0 \\ 0 &-3 &0 \\ 0 &0 &-3 \end{pmatrix}
$$

**Corollary 1.11**  —

If $$\left|T\right|\neq 0$$ then $$T^{-1}=(1/\left|T\right|)\cdot\text{adj}\,(T)$$.

**Example 1.12**  —

The inverse of the matrix from Example 1.10 is $$(1/-3)\cdot\text{adj}\,(T)$$.

$$
T^{-1} =\begin{pmatrix} 1/-3 &0/-3 &-4/-3 \\ -3/-3 &-3/-3 &9/-3 \\ -1/-3 &0/-3 &1/-3 \end{pmatrix} =\begin{pmatrix} -1/3 &0 &4/3 \\ 1 &1 &-3 \\ 1/3 &0 &-1/3 \end{pmatrix}
$$

The formulas from this section are often used for by-hand calculation and are sometimes useful with special types of matrices. However, they are not the best choice for computation with arbitrary matrices because they require more arithmetic than, for instance, the Gauss-Jordan method.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Find the cofactor.

$$
T=\begin{pmatrix} 1 &0 &2 \\ -1 &1 &3 \\ 0 &2 &-1 \end{pmatrix}
$$

1. $$T_{2,3}$$
2. $$T_{3,2}$$
3. $$T_{1,3}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Find the determinant by expanding

$$
\begin{vmatrix} 3 &0 &1 \\ 1 &2 &2 \\ -1 &3 &0 \end{vmatrix}
$$

1. on the first row
2. on the second row
3. on the third column.

**Problem 3**  —

Find the adjoint of the matrix in Example 1.6.  
*This exercise is recommended for all readers.*

**Problem 4**  —

Find the matrix adjoint to each.

1. $$\begin{pmatrix} 2 &1 &4 \\ -1 &0 &2 \\ 1 &0 &1 \end{pmatrix}$$
2. $$\begin{pmatrix} 3 &-1 \\ 2 &4 \end{pmatrix}$$
3. $$\begin{pmatrix} 1 &1 \\ 5 &0 \end{pmatrix}$$
4. $$\begin{pmatrix} 1 &4 &3 \\ -1 &0 &3 \\ 1 &8 &9 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 5**  —

Find the inverse of each matrix in the prior question with Theorem 1.9.

**Problem 6**  —

Find the matrix adjoint to this one.

$$
\begin{pmatrix} 2 &1 &0 &0 \\ 1 &2 &1 &0 \\ 0 &1 &2 &1 \\ 0 &0 &1 &2 \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 7**  —

Expand across the first row to derive the formula for the determinant of a $$2 \! \times \! 2$$ matrix.  
*This exercise is recommended for all readers.*

**Problem 8**  —

Expand across the first row to derive the formula for the determinant of a $$3 \! \times \! 3$$ matrix.  
*This exercise is recommended for all readers.*

**Problem 9**  —

1. Give a formula for the adjoint of a $$2 \! \times \! 2$$ matrix.
2. Use it to derive the formula for the inverse.  
*This exercise is recommended for all readers.*

**Problem 10**  —

Can we compute a determinant by expanding down the diagonal?

**Problem 11**  —

Give a formula for the adjoint of a diagonal matrix.  
*This exercise is recommended for all readers.*

**Problem 12**  —

Prove that the transpose of the adjoint is the adjoint of the transpose.

**Problem 13**  —

Prove or disprove: $$\text{adj}\,(\text{adj}\,(T))=T$$.

**Problem 14**  —

A square matrix is **upper triangular** if each $$i,j$$ entry is zero in the part above the diagonal, that is, when $$i>j$$.

1. Must the adjoint of an upper triangular matrix be upper triangular? Lower triangular?
2. Prove that the inverse of a upper triangular matrix is upper triangular, if an inverse exists.

**Problem 15**  —

*This question requires material from the optional Determinants Exist subsection.* Prove Theorem 1.5 by using the permutation expansion.

**Problem 16**  —

Prove that the determinant of a matrix equals the determinant of its transpose using Laplace's expansion and induction on the size of the matrix.

**? Problem 17**  —

Show that

$$
F_n= \begin{vmatrix} 1 &-1 &1 &-1 &1 &-1 &\ldots \\ 1 &1 &0 &1 &0 &1 &\ldots \\ 0 &1 &1 &0 &1 &0 &\ldots \\ 0 &0 &1 &1 &0 &1 &\ldots \\ . &. &. &. &. &. &\ldots \end{vmatrix}
$$

where $$F_n$$ is the $$n$$-th term of $$1,1,2,3,5,\dots,x,y,x+y,\ldots\,$$, the Fibonacci sequence, and the determinant is of order $$n-1$$. (Walter & Tytun 1949)

Solutions

### References

- Walter, Dan (proposer); Tytun, Alex (solver) (1949), "Elementary problem 834", *American Mathematical Monthly*, **56** (6), American Mathematical Society: 409.

---

*Source: Wikibooks, Linear Algebra/Laplace's Expansion (https://en.wikibooks.org/wiki/Linear_Algebra/Laplace%27s_Expansion), by Wikibooks contributors, CC BY-SA 4.0.*
