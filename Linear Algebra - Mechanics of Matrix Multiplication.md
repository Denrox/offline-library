# Mechanics of Matrix Multiplication

In this subsection we consider matrix multiplication as a mechanical process, putting aside for the moment any implications about the underlying maps. As described earlier, the striking thing about matrix multiplication is the way rows and columns combine. The $$i,j$$ entry of the matrix product is the dot product of row $$i$$ of the left matrix with column $$j$$ of the right one. For instance, here a second row and a third column combine to make a $$2,3$$ entry.

$$
\begin{pmatrix} 1 & 1 \\ {\color{red} 0} & {\color{red} 1} \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 4 & 6 & {\color{red}8 } & 2\\ 5 & 7 & {\color{red}9 } & 3 \end{pmatrix} = \begin{pmatrix} 9 &13 &17 &5 \\ 5 &7 &{\color{red}9} &3 \\ 4 &6 &8 &2 \end{pmatrix}
$$

We can view this as the left matrix acting by multiplying its rows, one at a time, into the columns of the right matrix. Of course, another perspective is that the right matrix uses its columns to act on the left matrix's rows. Below, we will examine actions from the left and from the right for some simple matrices.

The first case, the action of a zero matrix, is very easy.

**Example 3.1**  —

Multiplying by an appropriately-sized zero matrix from the left or from the right

$$
\begin{pmatrix} 0 &0 \\ 0 &0 \end{pmatrix} \begin{pmatrix} 1 &3 &2 \\ -1 &1 &-1 \end{pmatrix} = \begin{pmatrix} 0 &0 &0 \\ 0 &0 &0 \end{pmatrix} \qquad \begin{pmatrix} 2 &3 \\ 1 &4 \end{pmatrix} \begin{pmatrix} 0 &0 \\ 0 &0 \end{pmatrix} = \begin{pmatrix} 0 &0 \\ 0 &0 \end{pmatrix}
$$

results in a zero matrix.

After zero matrices, the matrices whose actions are easiest to understand are the ones with a single nonzero entry.

**Definition 3.2**  —

A matrix with all zeroes except for a one in the $$i,j$$ entry is an $$i,j$$ **unit** matrix.

**Example 3.3**  —

This is the $$1,2\,$$ unit matrix with three rows and two columns, multiplying from the left.

$$
\begin{pmatrix} 0 &1 \\ 0 &0 \\ 0 &0 \end{pmatrix} \begin{pmatrix} 5 &6 \\ 7 &8 \end{pmatrix} = \begin{pmatrix} 7 &8 \\ 0 &0 \\ 0 &0 \end{pmatrix}
$$

Acting from the left, an $$i,j$$ unit matrix copies row $$j$$ of the multiplicand into row $$i$$ of the result. From the right an $$i,j$$ unit matrix copies column $$i$$ of the multiplicand into column $$j$$ of the result.

$$
\begin{pmatrix} 1 &2 &3 \\ 4 &5 &6 \\ 7 &8 &9 \end{pmatrix} \begin{pmatrix} 0 &1 \\ 0 &0 \\ 0 &0 \end{pmatrix} = \begin{pmatrix} 0 &1 \\ 0 &4 \\ 0 &7 \end{pmatrix}
$$

**Example 3.4**  —

Rescaling these matrices simply rescales the result. This is the action from the left of the matrix that is twice the one in the prior example.

$$
\begin{pmatrix} 0 &2 \\ 0 &0 \\ 0 &0 \end{pmatrix} \begin{pmatrix} 5 &6 \\ 7 &8 \end{pmatrix} = \begin{pmatrix} 14 &16 \\ 0 &0 \\ 0 &0 \end{pmatrix}
$$

And this is the action of the matrix that is minus three times the one from the prior example.

$$
\begin{pmatrix} 1 &2 &3 \\ 4 &5 &6 \\ 7 &8 &9 \end{pmatrix} \begin{pmatrix} 0 &-3 \\ 0 &0 \\ 0 &0 \end{pmatrix} = \begin{pmatrix} 0 &-3 \\ 0 &-12 \\ 0 &-21 \end{pmatrix}
$$

Next in complication are matrices with two nonzero entries. There are two cases. If a left-multiplier has entries in different rows then their actions don't interact.

**Example 3.5**  —

$$
\begin{array}{rl} \begin{pmatrix} 1 &0 &0 \\ 0 &0 &2 \\ 0 &0 &0 \end{pmatrix} \begin{pmatrix} 1 &2 &3 \\ 4 &5 &6 \\ 7 &8 &9 \end{pmatrix} &=( \begin{pmatrix} 1 &0 &0 \\ 0 &0 &0 \\ 0 &0 &0 \end{pmatrix} + \begin{pmatrix} 0 &0 &0 \\ 0 &0 &2 \\ 0 &0 &0 \end{pmatrix} ) \begin{pmatrix} 1 &2 &3 \\ 4 &5 &6 \\ 7 &8 &9 \end{pmatrix} \\ &=\begin{pmatrix} 1 &2 &3 \\ 0 &0 &0 \\ 0 &0 &0 \end{pmatrix} + \begin{pmatrix} 0 &0 &0 \\ 14 &16 &18 \\ 0 &0 &0 \end{pmatrix} \\ &=\begin{pmatrix} 1 &2 &3 \\ 14 &16 &18 \\ 0 &0 &0 \end{pmatrix} \end{array}
$$

But if the left-multiplier's nonzero entries are in the same row then that row of the result is a combination.

**Example 3.6**  —

$$
\begin{array}{rl} \begin{pmatrix} 1 &0 &2 \\ 0 &0 &0 \\ 0 &0 &0 \end{pmatrix} \begin{pmatrix} 1 &2 &3 \\ 4 &5 &6 \\ 7 &8 &9 \end{pmatrix} &=( \begin{pmatrix} 1 &0 &0 \\ 0 &0 &0 \\ 0 &0 &0 \end{pmatrix} + \begin{pmatrix} 0 &0 &2 \\ 0 &0 &0 \\ 0 &0 &0 \end{pmatrix} ) \begin{pmatrix} 1 &2 &3 \\ 4 &5 &6 \\ 7 &8 &9 \end{pmatrix} \\ &=\begin{pmatrix} 1 &2 &3 \\ 0 &0 &0 \\ 0 &0 &0 \end{pmatrix} + \begin{pmatrix} 14 &16 &18 \\ 0 &0 &0 \\ 0 &0 &0 \end{pmatrix} \\ &=\begin{pmatrix} 15 &18 &21 \\ 0 &0 &0 \\ 0 &0 &0 \end{pmatrix} \end{array}
$$

Right-multiplication acts in the same way, with columns.

These observations about matrices that are mostly zeroes extend to arbitrary matrices.

**Lemma 3.7**  —

In a product of two matrices $$G$$ and $$H$$, the columns of $$GH$$ are formed by taking $$G$$ times the columns of $$H$$

$$
G\cdot \left(\begin{array}{c|c|c} \vdots & &\vdots \\ \vec{h}_1 &\cdots &\vec{h}_n \\ \vdots & &\vdots \end{array}\right) =\left(\begin{array}{c|c|c} \vdots & &\vdots \\ G\cdot \vec{h}_1 &\cdots &G\cdot\vec{h}_n \\ \vdots & &\vdots \end{array}\right)
$$

and the rows of $$GH$$ are formed by taking the rows of $$G$$ times $$H$$

$$
\left(\begin{array}{c} \cdots\; \vec{g}_1 \;\cdots \\ \hline \vdots \\ \hline \cdots\; \vec{g}_r \;\cdots \end{array}\right)\cdot H =\left(\begin{array}{c} \cdots\; \vec{g}_1\cdot H \;\cdots\\ \hline \vdots\\ \hline \cdots\; \vec{g}_r\cdot H \;\cdots \end{array}\right)
$$

(ignoring the extra parentheses).

**Proof**  —

We will show the $$2 \! \times \! 2$$ case and leave the general case as an exercise.

$$
GH=\begin{pmatrix} g_{1,1} &g_{1,2} \\ g_{2,1} &g_{2,2} \end{pmatrix} \begin{pmatrix} h_{1,1} &h_{1,2} \\ h_{2,1} &h_{2,2} \end{pmatrix} = \begin{pmatrix} g_{1,1}h_{1,1}+g_{1,2}h_{2,1} &g_{1,1}h_{1,2}+g_{1,2}h_{2,2} \\ g_{2,1}h_{1,1}+g_{2,2}h_{2,1} &g_{2,1}h_{1,2}+g_{2,2}h_{2,2} \end{pmatrix}
$$

The right side of the first equation in the result

$$
\left(\begin{array}{c|c} G\begin{pmatrix} h_{1,1} \\ h_{2,1} \end{pmatrix} &G\begin{pmatrix} h_{1,2} \\ h_{2,2} \end{pmatrix} \end{array}\right) = \left(\begin{array}{c|c} \begin{pmatrix} g_{1,1}h_{1,1}+g_{1,2}h_{2,1} \\ g_{2,1}h_{1,1}+g_{2,2}h_{2,1} \end{pmatrix} &\begin{pmatrix} g_{1,1}h_{1,2}+g_{1,2}h_{2,2} \\ g_{2,1}h_{1,2}+g_{2,2}h_{2,2} \end{pmatrix} \end{array}\right)
$$

is indeed the same as the right side of GH, except for the extra parentheses (the ones marking the columns as column vectors). The other equation is similarly easy to recognize.

An application of those observations is that there is a matrix that just copies out the rows and columns.

**Definition 3.8**  —

The **main diagonal** (or **principal diagonal** or **diagonal**) of a square matrix goes from the upper left to the lower right.

**Definition 3.9**  —

An **identity matrix** is square and has with all entries zero except for ones in the main diagonal.

$$
I_{n \! \times \! n}= \begin{pmatrix} 1 &0 &\ldots &0 \\ 0 &1 &\ldots &0 \\ &\vdots \\ 0 &0 &\ldots &1 \end{pmatrix}
$$

**Example 3.10**  —

The $$3 \! \times \! 3$$ identity leaves its multiplicand unchanged both from the left

$$
\begin{pmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{pmatrix} \begin{pmatrix} 2 &3 &6 \\ 1 &3 &8 \\ -7 &1 &0 \end{pmatrix} = \begin{pmatrix} 2 &3 &6 \\ 1 &3 &8 \\ -7 &1 &0 \end{pmatrix}
$$

and from the right.

$$
\begin{pmatrix} 2 &3 &6 \\ 1 &3 &8 \\ -7 &1 &0 \end{pmatrix} \begin{pmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{pmatrix} = \begin{pmatrix} 2 &3 &6 \\ 1 &3 &8 \\ -7 &1 &0 \end{pmatrix}
$$

**Example 3.11**  —

So does the $$2 \! \times \! 2$$ identity matrix.

$$
\begin{pmatrix} 1 &-2 \\ 0 &-2 \\ 1 &-1 \\ 4 &3 \end{pmatrix} \begin{pmatrix} 1 &0 \\ 0 &1 \\ \end{pmatrix} = \begin{pmatrix} 1 &-2 \\ 0 &-2 \\ 1 &-1 \\ 4 &3 \end{pmatrix}
$$

In short, an identity matrix is the identity element of the set of $$n \! \times \! n$$ matrices with respect to the operation of matrix multiplication.

We next see two ways to generalize the identity matrix.

The first is that if the ones are relaxed to arbitrary reals, the resulting matrix will rescale whole rows or columns.

**Definition 3.12**  —

A **diagonal matrix** is square and has zeros off the main diagonal.

$$
\begin{pmatrix} a_{1,1} &0 &\ldots &0 \\ 0 &a_{2,2} &\ldots &0 \\ &\vdots \\ 0 &0 &\ldots &a_{n,n} \end{pmatrix}
$$

**Example 3.13**  —

From the left, the action of multiplication by a diagonal matrix is to rescales the rows.

$$
\begin{pmatrix} 2 &0 \\ 0 &-1 \end{pmatrix} \begin{pmatrix} 2 &1 &4 &-1 \\ -1 &3 &4 &4 \end{pmatrix} = \begin{pmatrix} 4 &2 &8 &-2 \\ 1 &-3 &-4 &-4 \end{pmatrix}
$$

From the right such a matrix rescales the columns.

$$
\begin{pmatrix} 1 &2 &1 \\ 2 &2 &2 \end{pmatrix} \begin{pmatrix} 3 &0 &0 \\ 0 &2 &0 \\ 0 &0 &-2 \end{pmatrix} = \begin{pmatrix} 3 &4 &-2 \\ 6 &4 &-4 \end{pmatrix}
$$

The second generalization of identity matrices is that we can put a single one in each row and column in ways other than putting them down the diagonal.

**Definition 3.14**  —

A **permutation matrix** is square and is all zeros except for a single one in each row and column.

**Example 3.15**  —

From the left these matrices permute rows.

$$
\begin{pmatrix} 0 &0 &1 \\ 1 &0 &0 \\ 0 &1 &0 \end{pmatrix} \begin{pmatrix} 1 &2 &3 \\ 4 &5 &6 \\ 7 &8 &9 \end{pmatrix} = \begin{pmatrix} 7 &8 &9 \\ 1 &2 &3 \\ 4 &5 &6 \end{pmatrix}
$$

From the right they permute columns.

$$
\begin{pmatrix} 1 &2 &3 \\ 4 &5 &6 \\ 7 &8 &9 \end{pmatrix} \begin{pmatrix} 0 &0 &1 \\ 1 &0 &0 \\ 0 &1 &0 \end{pmatrix} = \begin{pmatrix} 2 &3 &1 \\ 5 &6 &4 \\ 8 &9 &7 \end{pmatrix}
$$

We finish this subsection by applying these observations to get matrices that perform Gauss' method and Gauss-Jordan reduction.

**Example 3.16**  —

We have seen how to produce a matrix that will rescale rows. Multiplying by this diagonal matrix rescales the second row of the other by a factor of three.

$$
\begin{pmatrix} 1 &0 &0 \\ 0 &3 &0 \\ 0 &0 &1 \end{pmatrix} \begin{pmatrix} 0 &2 &1 &1 \\ 0 &1/3 &1 &-1 \\ 1 &0 &2 &0 \end{pmatrix} = \begin{pmatrix} 0 &2 &1 &1 \\ 0 &1 &3 &-3 \\ 1 &0 &2 &0 \end{pmatrix}
$$

We have seen how to produce a matrix that will swap rows. Multiplying by this permutation matrix swaps the first and third rows.

$$
\begin{pmatrix} 0 &0 &1 \\ 0 &1 &0 \\ 1 &0 &0 \end{pmatrix} \begin{pmatrix} 0 &2 &1 &1 \\ 0 &1 &3 &-3 \\ 1 &0 &2 &0 \end{pmatrix} = \begin{pmatrix} 1 &0 &2 &0 \\ 0 &1 &3 &-3 \\ 0 &2 &1 &1 \end{pmatrix}
$$

To see how to perform a pivot, we observe something about those two examples. The matrix that rescales the second row by a factor of three arises in this way from the identity.

$$
\begin{pmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{pmatrix} \xrightarrow[]{3\rho_2} \begin{pmatrix} 1 &0 &0 \\ 0 &3 &0 \\ 0 &0 &1 \end{pmatrix}
$$

Similarly, the matrix that swaps first and third rows arises in this way.

$$
\begin{pmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{pmatrix} \xrightarrow[]{\rho_1\leftrightarrow\rho_3} \begin{pmatrix} 0 &0 &1 \\ 0 &1 &0 \\ 1 &0 &0 \end{pmatrix}
$$

**Example 3.17**  —

The $$3 \! \times \! 3$$ matrix that arises as

$$
\begin{pmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{pmatrix} \xrightarrow[]{-2\rho_2+\rho_3} \begin{pmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &-2 &1 \end{pmatrix}
$$

will, when it acts from the left, perform the pivot operation $$-2\rho_2+\rho_3$$.

$$
\begin{pmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &-2 &1 \end{pmatrix} \begin{pmatrix} 1 &0 &2 &0 \\ 0 &1 &3 &-3 \\ 0 &2 &1 &1 \end{pmatrix} = \begin{pmatrix} 1 &0 &2 &0 \\ 0 &1 &3 &-3 \\ 0 &0 &-5 &7 \end{pmatrix}
$$

**Definition 3.18**  —

The **elementary reduction matrices** are obtained from identity matrices with one Gaussian operation. We denote them:

1. $$I\xrightarrow[]{k\rho_i}M_i(k)$$ for $$k\neq 0$$;
2. $$I\xrightarrow[]{\rho_i\leftrightarrow\rho_j}P_{i,j}$$ for $$i\neq j$$;
3. $$I\xrightarrow[]{k\rho_i+\rho_j}C_{i,j}(k)$$ for $$i\neq j$$.

**Lemma 3.19**  —

Gaussian reduction can be done through matrix multiplication.

1. If $$H\xrightarrow[]{k\rho_i}G$$ then $$M_i(k)H=G$$.
2. If $$H\xrightarrow[]{\rho_i\leftrightarrow\rho_j}G$$ then $$P_{i,j}H=G$$.
3. If $$H\xrightarrow[]{k\rho_i+\rho_j}G$$ then $$C_{i,j}(k)H=G$$.

**Proof**  —

Clear.

**Example 3.20**  —

This is the first system, from the first chapter, on which we performed Gauss' method.

$$
\begin{array}{rcrcrcr} & & & &3x_3 &= &9 \\ x_1 &+ &5x_2 &- &2x_3 &= &2 \\ (1/3)x_1 &+ &2x_2 & & &= &3 \end{array}
$$

It can be reduced with matrix multiplication. Swap the first and third rows,

$$
\begin{pmatrix} 0 &0 &1 \\ 0 &1 &0 \\ 1 &0 &0 \end{pmatrix} \left(\begin{array}{ccc|c} 0 &0 &3 &9 \\ 1 &5 &-2 &2 \\ 1/3 &2 &0 &3 \end{array}\right) = \left(\begin{array}{ccc|c} 1/3 &2 &0 &3 \\ 1 &5 &-2 &2 \\ 0 &0 &3 &9 \end{array}\right)
$$

triple the first row,

$$
\begin{pmatrix} 3 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{pmatrix} \left(\begin{array}{ccc|c} 1/3 &2 &0 &3 \\ 1 &5 &-2 &2 \\ 0 &0 &3 &9 \end{array}\right) = \left(\begin{array}{ccc|c} 1 &6 &0 &9 \\ 1 &5 &-2 &2 \\ 0 &0 &3 &9 \end{array}\right)
$$

and then add $$-1$$ times the first row to the second.

$$
\begin{pmatrix} 1 &0 &0 \\ -1 &1 &0 \\ 0 &0 &1 \end{pmatrix} \left(\begin{array}{ccc|c} 1 &6 &0 &9 \\ 1 &5 &-2 &2 \\ 0 &0 &3 &9 \end{array}\right) = \left(\begin{array}{ccc|c} 1 &6 &0 &9 \\ 0 &-1 &-2 &-7 \\ 0 &0 &3 &9 \end{array}\right)
$$

Now back substitution will give the solution.

**Example 3.21**  —

Gauss-Jordan reduction works the same way. For the matrix ending the prior example, first adjust the leading entries

$$
\begin{pmatrix} 1 &0 &0 \\ 0 &-1 &0 \\ 0 &0 &1/3 \end{pmatrix} \left(\begin{array}{ccc|c} 1 &6 &0 &9 \\ 0 &-1 &-2 &-7 \\ 0 &0 &3 &9 \end{array}\right) = \left(\begin{array}{ccc|c} 1 &6 &0 &9 \\ 0 &1 &2 &7 \\ 0 &0 &1 &3 \end{array}\right)
$$

and to finish, clear the third column and then the second column.

$$
\begin{pmatrix} 1 &-6 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{pmatrix} \begin{pmatrix} 1 &0 &0 \\ 0 &1 &-2 \\ 0 &0 &1 \end{pmatrix} \left(\begin{array}{ccc|c} 1 &6 &0 &9 \\ 0 &1 &2 &7 \\ 0 &0 &1 &3 \end{array}\right) = \left(\begin{array}{ccc|c} 1 &0 &0 &3 \\ 0 &1 &0 &1 \\ 0 &0 &1 &3 \end{array}\right)
$$

We have observed the following result, which we shall use in the next subsection.

**Corollary 3.22**  —

For any matrix $$H$$ there are elementary reduction matrices $$R_1$$, ..., $$R_r$$ such that $$R_r\cdot R_{r-1}\cdots R_1\cdot H$$ is in reduced echelon form.

Until now we have taken the point of view that our primary objects of study are vector spaces and the maps between them, and have adopted matrices only for computational convenience. This subsection show that this point of view isn't the whole story. Matrix theory is a fascinating and fruitful area.

In the rest of this book we shall continue to focus on maps as the primary objects, but we will be pragmatic— if the matrix point of view gives some clearer idea then we shall use it.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Predict the result of each multiplication by an elementary reduction matrix, and then check by multiplying it out.

1. $$\begin{pmatrix} 3 &0 \\ 0 &0 \end{pmatrix} \begin{pmatrix} 1 &2 \\ 3 &4 \end{pmatrix}$$
2. $$\begin{pmatrix} 4 &0 \\ 0 &2 \end{pmatrix} \begin{pmatrix} 1 &2 \\ 3 &4 \end{pmatrix}$$
3. $$\begin{pmatrix} 1 &0 \\ -2 &1 \end{pmatrix} \begin{pmatrix} 1 &2 \\ 3 &4 \end{pmatrix}$$
4. $$\begin{pmatrix} 1 &2 \\ 3 &4 \end{pmatrix} \begin{pmatrix} 1 &-1 \\ 0 &1 \end{pmatrix}$$
5. $$\begin{pmatrix} 1 &2 \\ 3 &4 \end{pmatrix} \begin{pmatrix} 0 &1 \\ 1 &0 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

The need to take linear combinations of rows and columns in tables of numbers arises often in practice. For instance, this is a map of part of Vermont and New York.

- In part because of Lake Champlain, there are no roads directly connecting some pairs of towns. For instance, there is no way to go from Winooski to Grand Isle without going through Colchester. (Of course, many other roads and towns have been left off to simplify the graph. From top to bottom of this map is about forty miles.)

1. The **incidence matrix** of a map is the square matrix whose $$i,j$$ entry is the number of roads from city $$i$$ to city $$j$$. Produce the incidence matrix of this map (take the cities in alphabetical order).
2. A matrix is **symmetric** if it equals its transpose. Show that an incidence matrix is symmetric. (These are all two-way streets. Vermont doesn't have many one-way streets.)
3. What is the significance of the square of the incidence matrix? The cube?  
*This exercise is recommended for all readers.*

**Problem 3**  —

This table gives the number of hours of each type done by each worker, and the associated pay rates. Use matrices to compute the wages due.

- *regular*   *overtime*
- Alan   40   12
- Betty   35   6
- Catherine   40   18
- Donald   28   0

- *wage*
- regular   $25.00
- overtime   $45.00

(*Remark.* This illustrates, as did the prior problem, that in practice we often want to compute linear combinations of rows and columns in a context where we really aren't interested in any associated linear maps.)

**Problem 4**  —

Find the product of this matrix with its transpose.

$$
\begin{pmatrix} \cos\theta &-\sin\theta \\ \sin\theta &\cos\theta \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 5**  —

Prove that the diagonal matrices form a subspace of $$\mathcal{M}_{n \! \times \! n}$$. What is its dimension?

**Problem 6**  —

Does the identity matrix represent the identity map if the bases are unequal?

**Problem 7**  —

Show that every multiple of the identity commutes with every square matrix. Are there other matrices that commute with all square matrices?

**Problem 8**  —

Prove or disprove: nonsingular matrices commute.  
*This exercise is recommended for all readers.*

**Problem 9**  —

Show that the product of a permutation matrix and its transpose is an identity matrix.

**Problem 10**  —

Show that if the first and second rows of $$G$$ are equal then so are the first and second rows of $$GH$$. Generalize.

**Problem 11**  —

Describe the product of two diagonal matrices.

**Problem 12**  —

Write

$$
\begin{pmatrix} 1 &0 \\ -3 &3 \end{pmatrix}
$$

as the product of two elementary reduction matrices.  
*This exercise is recommended for all readers.*

**Problem 13**  —

Show that if $$G$$ has a row of zeros then $$GH$$ (if defined) has a row of zeros. Does that work for columns?

**Problem 14**  —

Show that the set of unit matrices forms a basis for $$\mathcal{M}_{n \! \times \! m}$$.

**Problem 15**  —

Find the formula for the $$n$$-th power of this matrix.

$$
\begin{pmatrix} 1 &1 \\ 1 &0 \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 16**  —

The **trace** of a square matrix is the sum of the entries on its diagonal (its significance appears in Chapter Five). Show that $$\text{trace}\, (GH)=\text{trace}\, (HG)$$.  
*This exercise is recommended for all readers.*

**Problem 17**  —

A square matrix is **upper triangular** if its only nonzero entries lie above, or on, the diagonal. Show that the product of two upper triangular matrices is upper triangular. Does this hold for lower triangular also?

**Problem 18**  —

A square matrix is a **Markov matrix** if each entry is between zero and one and the sum along each row is one. Prove that a product of Markov matrices is Markov.  
*This exercise is recommended for all readers.*

**Problem 19**  —

Give an example of two matrices of the same rank with squares of differing rank.

**Problem 20**  —

Combine the two generalizations of the identity matrix, the one allowing entires to be other than ones, and the one allowing the single one in each row and column to be off the diagonal. What is the action of this type of matrix?

**Problem 21**  —

On a computer multiplications are more costly than additions, so people are interested in reducing the number of multiplications used to compute a matrix product.

1. How many real number multiplications are needed in formula we gave for the product of a $$m \! \times \! r$$ matrix and a $$r \! \times \! n$$ matrix?
2. Matrix multiplication is associative, so all associations yield the same result. The cost in number of multiplications, however, varies. Find the association requiring the fewest real number multiplications to compute the matrix product of a $$5 \! \times \! 10$$ matrix, a $$10 \! \times \! 20$$ matrix, a $$20 \! \times \! 5$$ matrix, and a $$5 \! \times \! 1$$ matrix.
3. *(Very hard.)* Find a way to multiply two $$2 \! \times \! 2$$ matrices using only seven multiplications instead of the eight suggested by the naive approach.

**? Problem 22**  —

If $$A$$ and $$B$$ are square matrices of the same size such that $$ABAB=0$$, does it follow that $$BABA=0$$? (*Putnam Exam 1990*)

**Problem 23**  —

Demonstrate these four assertions to get an alternate proof that column rank equals row rank. (Liebeck 1966)

1. $$\vec{y}\cdot\vec{y}=\vec{0}$$ iff $$\vec{y}=\vec{0}$$.
2. $$A\vec{x}=\vec{0}$$ iff $${{A}^{\rm trans}}A\vec{x}=\vec{0}$$.
3. $$\dim(\mathcal{R}(A))=\dim(\mathcal{R}({{A}^{\rm trans}}A))$$.
4. $$\text{col rank}(A)=\text{col rank}({{A}^{\rm trans}}) =\text{row rank}(A)$$.

**Problem 24**  —

Prove (where $$A$$ is an $$n \! \times \! n$$ matrix and so defines a transformation of any $$n$$-dimensional space $$V$$ with respect to $$B,B$$ where $$B$$ is a basis) that $$\dim(\mathcal{R}(A)\cap\mathcal{N}(A)) =\dim(\mathcal{R}(A))-\dim(\mathcal{R}(A^2))$$. Conclude

1. $$\mathcal{N}(A)\subset\mathcal{R}(A)$$ iff $$\dim(\mathcal{N}(A))=\dim(\mathcal{R}(A)) -\dim(\mathcal{R}(A^2))$$;
2. $$\mathcal{R}(A)\subseteq\mathcal{N}(A)$$ iff $$A^2=0$$;
3. $$\mathcal{R}(A)=\mathcal{N}(A)$$ iff $$A^2=0$$ and $$\dim(\mathcal{N}(A))=\dim(\mathcal{R}(A))$$ ;
4. $$\dim(\mathcal{R}(A)\cap\mathcal{N}(A))=0$$ iff $$\dim(\mathcal{R}(A))=\dim(\mathcal{R}(A^2))$$ ;
5. *(Requires the Direct Sum subsection, which is optional.)* $$V=\mathcal{R}(A)\oplus\mathcal{N}(A)$$ iff $$\dim(\mathcal{R}(A))=\dim(\mathcal{R}(A^2))$$.

(Ackerson 1955)

Solutions

### References

- Ackerson, R. H. (1955), "A Note on Vector Spaces", *American Mathematical Monthly*, **62** (10), American Mathematical Society: 721 {{citation}}: Unknown parameter |month= ignored (help).
- Liebeck, Hans. (1966), "A Proof of the Equality of Column Rank and Row Rank of a Matrix", *American Mathematical Monthly*, **73** (10), American Mathematical Society: 1114 {{citation}}: Unknown parameter |month= ignored (help).
- William Lowell Putnam Mathematical Competition, Problem A-5, 1990.

---

*Source: Wikibooks, Linear Algebra/Mechanics of Matrix Multiplication (https://en.wikibooks.org/wiki/Linear_Algebra/Mechanics_of_Matrix_Multiplication), by Wikibooks contributors, CC BY-SA 4.0.*
