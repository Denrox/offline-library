# Row Equivalence

We will close this section and this chapter by proving that every matrix is row equivalent to one and only one reduced echelon form matrix. The ideas that appear here will reappear, and be further developed, in the next chapter.

The underlying theme here is that one way to understand a mathematical situation is by being able to classify the cases that can happen. We have met this theme several times already. We have classified solution sets of linear systems into the no-elements, one-element, and infinitely-many elements cases. We have also classified linear systems with the same number of equations as unknowns into the nonsingular and singular cases. We adopted these classifications because they give us a way to understand the situations that we were investigating. Here, where we are investigating row equivalence, we know that the set of all matrices breaks into the row equivalence classes. When we finish the proof here, we will have a way to understand each of those classes— its matrices can be thought of as derived by row operations from the unique reduced echelon form matrix in that class.

To understand how row operations act to transform one matrix into another, we consider the effect that they have on the parts of a matrix. The crucial observation is that row operations combine the rows linearly.

**Definition 2.1**  —

A **linear combination** of $$x_1,\ldots,x_m$$ is an expression of the form $$c_1x_1+c_2x_2+\,\cdots\,+c_mx_m$$ where the $$c$$'s are scalars.

(We have already used the phrase "linear combination" in this book. The meaning is unchanged, but the next result's statement makes a more formal definition in order.)

**Lemma 2.2 (Linear Combination Lemma)**  —

A linear combination of linear combinations is a linear combination.

**Proof**  —

Given the linear combinations $$c_{1,1}x_1+\dots+c_{1,n}x_n$$ through $$c_{m,1}x_1+\dots+c_{m,n}x_n$$, consider a combination of those

$$
d_1(c_{1,1}x_1+\dots+c_{1,n}x_n)\,+\dots+\,d_m(c_{m,1}x_1+\dots+c_{m,n}x_n)
$$

where the $$d$$'s are scalars along with the $$c$$'s. Distributing those $$d$$'s and regrouping gives

$$
=(d_1c_{1,1}+\dots+d_mc_{m,1})x_1\,+\dots+\,(d_1c_{1,n}+\dots+d_mc_{m,n})x_n
$$

which is a linear combination of the $$x$$'s.

In this subsection we will use the convention that, where a matrix is named with an upper case roman letter, the matching lower-case greek letter names the rows.

$$
A= \begin{pmatrix} \cdots \alpha_1 \cdots \\ \cdots \alpha_2 \cdots \\ \vdots \\ \cdots \alpha_m \cdots \end{pmatrix} \qquad B= \begin{pmatrix} \cdots \beta_1 \cdots \\ \cdots \beta_2 \cdots \\ \vdots \\ \cdots \beta_m\cdots \end{pmatrix}
$$

**Corollary 2.3**  —

Where one matrix reduces to another, each row of the second is a linear combination of the rows of the first.

The proof below uses induction on the number of row operations used to reduce one matrix to the other. Before we proceed, here is an outline of the argument (readers unfamiliar with induction may want to compare this argument with the one used in the "$$\text{General}=\text{Particular}+\text{Homogeneous}$$" proof). First, for the base step of the argument, we will verify that the proposition is true when reduction can be done in zero row operations. Second, for the inductive step, we will argue that if being able to reduce the first matrix to the second in some number $$t\geq 0$$ of operations implies that each row of the second is a linear combination of the rows of the first, then being able to reduce the first to the second in $$t+1$$ operations implies the same thing. Together, this base step and induction step prove this result because by the base step the proposition is true in the zero operations case, and by the inductive step the fact that it is true in the zero operations case implies that it is true in the one operation case, and the inductive step applied again gives that it is therefore true in the two operations case, etc.

**Proof**  —

We proceed by induction on the minimum number of row operations that take a first matrix $$A$$ to a second one $$B$$.

In the base step, that zero reduction operations suffice, the two matrices are equal and each row of $$B$$ is obviously a combination of $$A$$'s rows: $$\vec{\beta}_i =0\cdot\vec{\alpha}_1+\dots+1\cdot\vec{\alpha}_i+\dots+0\cdot\vec{\alpha}_m$$.

For the inductive step, assume the inductive hypothesis: with $$t\geq 0$$, if a matrix can be derived from $$A$$ in $$t$$ or fewer operations then its rows are linear combinations of the $$A$$'s rows. Consider a $$B$$ that takes $$t+1$$ operations. Because there are more than zero operations, there must be a next-to-last matrix $$G$$ so that $$A\longrightarrow\cdots\longrightarrow G\longrightarrow B$$. This $$G$$ is only $$t$$ operations away from $$A$$ and so the inductive hypothesis applies to it, that is, each row of $$G$$ is a linear combination of the rows of $$A$$.

If the last operation, the one from $$G$$ to $$B$$, is a row swap then the rows of $$B$$ are just the rows of $$G$$ reordered and thus each row of $$B$$ is also a linear combination of the rows of $$A$$. The other two possibilities for this last operation, that it multiplies a row by a scalar and that it adds a multiple of one row to another, both result in the rows of $$B$$ being linear combinations of the rows of $$G$$. But therefore, by the Linear Combination Lemma, each row of $$B$$ is a linear combination of the rows of $$A$$.

With that, we have both the base step and the inductive step, and so the proposition follows.

**Example 2.4**  —

In the reduction

$$
\begin{pmatrix} 0 &2 \\ 1 &1 \end{pmatrix} \xrightarrow[]{\rho_1\leftrightarrow\rho_2} \begin{pmatrix} 1 &1 \\ 0 &2 \end{pmatrix} \xrightarrow[]{(1/2)\rho_2} \begin{pmatrix} 1 &1 \\ 0 &1 \end{pmatrix} \xrightarrow[]{-\rho_2+\rho_1} \begin{pmatrix} 1 &0 \\ 0 &1 \end{pmatrix}
$$

call the matrices $$A$$, $$D$$, $$G$$, and $$B$$. The methods of the proof show that there are three sets of linear relationships.

$$
\begin{align} \delta_1 &=0\cdot\alpha_1+1\cdot\alpha_2 \\ \delta_2 &=1\cdot\alpha_1+0\cdot\alpha_2 \end{align} \qquad \begin{align} \gamma_1 &=0\cdot\alpha_1+1\cdot\alpha_2 \\ \gamma_2 &=(1/2)\alpha_1+0\cdot\alpha_2 \end{align} \qquad \begin{align} \beta_1 &=(-1/2)\alpha_1+1\cdot\alpha_2 \\ \beta_2 &=(1/2)\alpha_1+0\cdot\alpha_2 \end{align}
$$

The prior result gives us the insight that Gauss' method works by taking linear combinations of the rows. But to what end; why do we go to echelon form as a particularly simple, or basic, version of a linear system? The answer, of course, is that echelon form is suitable for back substitution, because we have isolated the variables. For instance, in this matrix

$$
R=\begin{pmatrix} 2 &3 &7 &8 &0 &0 \\ 0 &0 &1 &5 &1 &1 \\ 0 &0 &0 &3 &3 &0 \\ 0 &0 &0 &0 &2 &1 \end{pmatrix}
$$

$$x_1$$ has been removed from $$x_5$$'s equation. That is, Gauss' method has made $$x_5$$'s row independent of $$x_1$$'s row.

Independence of a collection of row vectors, or of any kind of vectors, will be precisely defined and explored in the next chapter. But a first take on it is that we can show that, say, the third row above is not comprised of the other rows, that $$\rho_3\neq c_1\rho_1+c_2\rho_2+c_4\rho_4$$. For, suppose that there are scalars $$c_1$$, $$c_2$$, and $$c_4$$ such that this relationship holds.

$$
\begin{array}{rl} \begin{pmatrix} 0 &0 &0 &3 &3 &0 \end{pmatrix} &=c_1\begin{pmatrix} 2 &3 &7 &8 &0 &0 \end{pmatrix} \\ &\quad+c_2\begin{pmatrix} 0 &0 &1 &5 &1 &1 \end{pmatrix} \\ &\quad+c_4\begin{pmatrix} 0 &0 &0 &0 &2 &1 \end{pmatrix} \end{array}
$$

The first row's leading entry is in the first column and narrowing our consideration of the above relationship to consideration only of the entries from the first column $$0=2c_1+0c_2+0c_4$$ gives that $$c_1=0$$. The second row's leading entry is in the third column and the equation of entries in that column $$0=7c_1+1c_2+0c_4$$, along with the knowledge that $$c_1=0$$, gives that $$c_2=0$$. Now, to finish, the third row's leading entry is in the fourth column and the equation of entries in that column $$3=8c_1+5c_2+0c_4$$, along with $$c_1=0$$ and $$c_2=0$$, gives an impossibility.

The following result shows that this effect always holds. It shows that what Gauss' linear elimination method eliminates is linear relationships among the rows.

**Lemma 2.5**  —

In an echelon form matrix, no nonzero row is a linear combination of the other rows.

**Proof**  —

Let $$R$$ be in echelon form. Suppose, to obtain a contradiction, that some nonzero row is a linear combination of the others.

$$
\rho_i=c_1\rho_1+\ldots+c_{i-1}\rho_{i-1}+ c_{i+1}\rho_{i+1}+\ldots+c_m\rho_m
$$

We will first use induction to show that the coefficients $$c_1$$, ..., $$c_{i-1}$$ associated with rows above $$\rho_i$$ are all zero. The contradiction will come from consideration of $$\rho_i$$ and the rows below it.

The base step of the induction argument is to show that the first coefficient $$c_1$$ is zero. Let the first row's leading entry be in column number $$\ell_1$$ and consider the equation of entries in that column.

$$
\rho_{i,\ell_1}=c_1\rho_{1,\ell_1}+\ldots+c_{i-1}\rho_{i-1,\ell_1} +c_{i+1}\rho_{i+1,\ell_1}+\ldots+c_m\rho_{m,\ell_1}
$$

The matrix is in echelon form so the entries $$\rho_{2,\ell_1}$$, ..., $$\rho_{m,\ell_1}$$, including $$\rho_{i,\ell_1}$$, are all zero.

$$
0=c_1\rho_{1,\ell_1}+\dots+c_{i-1}\cdot 0 +c_{i+1}\cdot 0+\dots+c_m\cdot 0
$$

Because the entry $$\rho_{1,\ell_1}$$ is nonzero as it leads its row, the coefficient $$c_1$$ must be zero.

The inductive step is to show that for each row index $$k$$ between $$1$$ and $$i-2$$, if the coefficient $$c_1$$ and the coefficients $$c_2$$, ..., $$c_{k}$$ are all zero then $$c_{k+1}$$ is also zero. That argument, and the contradiction that finishes this proof, is saved for Problem 11.

We can now prove that each matrix is row equivalent to one and only one reduced echelon form matrix. We will find it convenient to break the first half of the argument off as a preliminary lemma. For one thing, it holds for any echelon form whatever, not just reduced echelon form.

**Lemma 2.6**  —

If two echelon form matrices are row equivalent then the leading entries in their first rows lie in the same column. The same is true of all the nonzero rows— the leading entries in their second rows lie in the same column, etc.

For the proof we rephrase the result in more technical terms. Define the **form** of an $$m \! \times \! n$$ matrix to be the sequence $$\langle \ell_1,\ell_2,\ldots\,,\ell_m \rangle$$ where $$\ell_i$$ is the column number of the leading entry in row $$i$$ and $$\ell_i=\infty$$ if there is no leading entry in that row. The lemma says that if two echelon form matrices are row equivalent then their forms are equal sequences.

**Proof**  —

Let $$B$$ and $$D$$ be echelon form matrices that are row equivalent. Because they are row equivalent they must be the same size, say $$m \! \times \! n$$. Let the column number of the leading entry in row $$i$$ of $$B$$ be $$\ell_i$$ and let the column number of the leading entry in row $$j$$ of $$D$$ be $$k_j$$. We will show that $$\ell_1=k_1$$, that $$\ell_2=k_2$$, etc., by induction.

This induction argument relies on the fact that the matrices are row equivalent, because the Linear Combination Lemma and its corollary therefore give that each row of $$B$$ is a linear combination of the rows of $$D$$ and vice versa:

$$
\beta_i=s_{i,1}\delta_1+s_{i,2}\delta_2+\dots+s_{i,m}\delta_m \quad\text{and}\quad \delta_j=t_{j,1}\beta_1+t_{j,2}\beta_2+\dots+t_{j,m}\beta_m
$$

where the $$s$$'s and $$t$$'s are scalars.

The base step of the induction is to verify the lemma for the first rows of the matrices, that is, to verify that $$\ell_1=k_1$$. If either row is a zero row then the entire matrix is a zero matrix since it is in echelon form, and therefore both matrices are zero matrices (by Corollary 2.3), and so both $$\ell_1$$ and $$k_1$$ are $$\infty$$. For the case where neither $$\beta_1$$ nor $$\delta_1$$ is a zero row, consider the $$i=1$$ instance of the linear relationship above.

$$
\begin{array}{rl} \beta_1 &=s_{1,1}\delta_1+s_{1,2}\delta_2+\dots+s_{1,m}\delta_m \\ \begin{pmatrix} 0 &\cdots &b_{1,\ell_1} &\cdots & \end{pmatrix} &=s_{1,1}\begin{pmatrix} 0 &\cdots &d_{1,k_1} &\cdots & \end{pmatrix} \\ &\quad+s_{1,2}\begin{pmatrix} 0 &\cdots &0 &\cdots & \end{pmatrix} \\ &\quad \vdots \\ &\quad+s_{1,m}\begin{pmatrix} 0 &\cdots &0 &\cdots & \end{pmatrix} \end{array}
$$

First, note that $$\ell_1<k_1$$ is impossible: in the columns of $$D$$ to the left of column $$k_1$$ the entries are all zeroes (as $$d_{1,k_1}$$ leads the first row) and so if $$\ell_1<k_1$$ then the equation of entries from column $$\ell_1$$ would be $$b_{1,\ell_1}=s_{1,1}\cdot 0+\dots+s_{1,m}\cdot 0$$, but $$b_{1,\ell_1}$$ isn't zero since it leads its row and so this is an impossibility. Next, a symmetric argument shows that $$k_1<\ell_1$$ also is impossible. Thus the $$\ell_1=k_1$$ base case holds.

The inductive step is to show that if $$\ell_1=k_1$$, and $$\ell_2=k_2$$, ..., and $$\ell_r=k_r$$, then also $$\ell_{r+1}=k_{r+1}$$ (for $$r$$ in the interval $$1\,..\,m-1$$). This argument is saved for Problem 12.

That lemma answers two of the questions that we have posed: (i) any two echelon form versions of a matrix have the same free variables, and consequently, and (ii) any two echelon form versions have the same number of free variables. There is no linear system and no combination of row operations such that, say, we could solve the system one way and get $$y$$ and $$z$$ free but solve it another way and get $$y$$ and $$w$$ free, or solve it one way and get two free variables while solving it another way yields three.

We finish now by specializing to the case of reduced echelon form matrices.

**Theorem 2.7**  —

Each matrix is row equivalent to a unique reduced echelon form matrix.

**Proof**  —

Clearly any matrix is row equivalent to at least one reduced echelon form matrix, via Gauss-Jordan reduction. For the other half, that any matrix is equivalent to at most one reduced echelon form matrix, we will show that if a matrix Gauss-Jordan reduces to each of two others then those two are equal.

Suppose that a matrix is row equivalent to two reduced echelon form matrices $$B$$ and $$D$$, which are therefore row equivalent to each other. The Linear Combination Lemma and its corollary allow us to write the rows of one, say $$B$$, as a linear combination of the rows of the other $$\beta_i=c_{i,1}\delta_1+\cdots+c_{i,m}\delta_m$$. The preliminary result, Lemma 2.6, says that in the two matrices, the same collection of rows are nonzero. Thus, if $$\beta_1$$ through $$\beta_r$$ are the nonzero rows of $$B$$ then the nonzero rows of $$D$$ are $$\delta_1$$ through $$\delta_r$$. Zero rows don't contribute to the sum so we can rewrite the relationship to include just the nonzero rows.

$$
\beta_i =c_{i,1}\delta_1+\dots+c_{i,r}\delta_r \qquad(*)
$$

The preliminary result also says that for each row $$j$$ between $$1$$ and $$r$$, the leading entries of the $$j$$-th row of $$B$$ and $$D$$ appear in the same column, denoted $$\ell_j$$. Rewriting the above relationship to focus on the entries in the $$\ell_j$$-th column

$$
\begin{array}{rl} \begin{pmatrix} &\cdots &b_{i,\ell_j} &\cdots & \end{pmatrix} &=c_{i,1}\begin{pmatrix} &\cdots &d_{1,\ell_j} &\cdots & \end{pmatrix} \\ &\quad+c_{i,2}\begin{pmatrix} &\cdots &d_{2,\ell_j} &\cdots & \end{pmatrix} \\ &\quad\vdots \\ &\quad+c_{i,r}\begin{pmatrix} &\cdots &d_{r,\ell_j} &\cdots & \end{pmatrix} \end{array}
$$

gives this set of equations for $$i=1$$ up to $$i=r$$.

$$
\begin{array}{rl} b_{1,\ell_j} &=c_{1,1}d_{1,\ell_j} +\cdots+c_{1,j}d_{j,\ell_j}+\cdots +c_{1,r}d_{r,\ell_j} \\ &\vdots \\ b_{j,\ell_j} &=c_{j,1}d_{1,\ell_j} +\cdots+c_{j,j}d_{j,\ell_j}+\cdots +c_{j,r}d_{r,\ell_j} \\ &\vdots \\ b_{r,\ell_j} &=c_{r,1}d_{1,\ell_j} +\cdots+c_{r,j}d_{j,\ell_j}+\cdots +c_{r,r}d_{r,\ell_j} \end{array}
$$

Since $$D$$ is in reduced echelon form, all of the $$d$$'s in column $$\ell_j$$ are zero except for $$d_{j,\ell_j}$$, which is $$1$$. Thus each equation above simplifies to $$b_{i,\ell_j}=c_{i,j}d_{j,\ell_j}=c_{i,j}\cdot 1$$. But $$B$$ is also in reduced echelon form and so all of the $$b$$'s in column $$\ell_j$$ are zero except for $$b_{j,\ell_j}$$, which is $$1$$. Therefore, each $$c_{i,j}$$ is zero, except that $$c_{1,1}=1$$, and $$c_{2,2}=1$$, ..., and $$c_{r,r}=1$$.

We have shown that the only nonzero coefficient in the linear combination labelled ($$*$$) is $$c_{j,j}$$, which is $$1$$. Therefore $$\beta_j=\delta_j$$. Because this holds for all nonzero rows, $$B=D$$.

We end with a recap. In Gauss' method we start with a matrix and then derive a sequence of other matrices. We defined two matrices to be related if one can be derived from the other. That relation is an equivalence relation, called row equivalence, and so partitions the set of all matrices into row equivalence classes.

(There are infinitely many matrices in the pictured class, but we've only got room to show two.) We have proved there is one and only one reduced echelon form matrix in each row equivalence class. So the reduced echelon form is a *canonical form* for row equivalence: the reduced echelon form matrices are representatives of the classes.

We can answer questions about the classes by translating them into questions about the representatives.

**Example 2.8**  —

We can decide if matrices are interreducible by seeing if Gauss-Jordan reduction produces the same reduced echelon form result. Thus, these are not row equivalent

$$
\begin{pmatrix} 1 &-3 \\ -2 &6 \end{pmatrix} \qquad \begin{pmatrix} 1 &-3 \\ -2 &5 \end{pmatrix}
$$

because their reduced echelon forms are not equal.

$$
\begin{pmatrix} 1 &-3 \\ 0 &0 \end{pmatrix} \qquad \begin{pmatrix} 1 &0 \\ 0 &1 \end{pmatrix}
$$

**Example 2.9**  —

Any nonsingular $$3 \! \times \! 3$$ matrix Gauss-Jordan reduces to this.

$$
\begin{pmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{pmatrix}
$$

**Example 2.10**  —

We can describe the classes by listing all possible reduced echelon form matrices. Any $$2 \! \times \! 2$$ matrix lies in one of these: the class of matrices row equivalent to this,

$$
\begin{pmatrix} 0 &0 \\ 0 &0 \end{pmatrix}
$$

the infinitely many classes of matrices row equivalent to one of this type

$$
\begin{pmatrix} 1 &a \\ 0 &0 \end{pmatrix}
$$

where $$a\in\mathbb{R}$$ (including $$a=0$$), the class of matrices row equivalent to this,

$$
\begin{pmatrix} 0 &1 \\ 0 &0 \end{pmatrix}
$$

and the class of matrices row equivalent to this

$$
\begin{pmatrix} 1 &0 \\ 0 &1 \end{pmatrix}
$$

(this is the class of nonsingular $$2 \! \times \! 2$$ matrices).

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Decide if the matrices are row equivalent.

1. $$\begin{pmatrix} 1 &2 \\ 4 &8 \end{pmatrix}, \begin{pmatrix} 0 &1 \\ 1 &2 \end{pmatrix}$$
2. $$\begin{pmatrix} 1 &0 &2 \\ 3 &-1 &1 \\ 5 &-1 &5 \end{pmatrix}, \begin{pmatrix} 1 &0 &2 \\ 0 &2 &10 \\ 2 &0 &4 \end{pmatrix}$$
3. $$\begin{pmatrix} 2 &1 &-1 \\ 1 &1 &0 \\ 4 &3 &-1 \end{pmatrix}, \begin{pmatrix} 1 &0 &2 \\ 0 &2 &10 \\ \end{pmatrix}$$
4. $$\begin{pmatrix} 1 &1 &1 \\ -1 &2 &2 \end{pmatrix}, \begin{pmatrix} 0 &3 &-1 \\ 2 &2 &5 \end{pmatrix}$$
5. $$\begin{pmatrix} 1 &1 &1 \\ 0 &0 &3 \end{pmatrix}, \begin{pmatrix} 0 &1 &2 \\ 1 &-1 &1 \end{pmatrix}$$

**Problem 2**  —

Describe the matrices in each of the classes represented in Example 2.10.

**Problem 3**  —

Describe all matrices in the row equivalence class of these.

1. $$\begin{pmatrix} 1 &0 \\ 0 &0 \end{pmatrix}$$
2. $$\begin{pmatrix} 1 &2 \\ 2 &4 \end{pmatrix}$$
3. $$\begin{pmatrix} 1 &1 \\ 1 &3 \end{pmatrix}$$

**Problem 4**  —

How many row equivalence classes are there?

**Problem 5**  —

Can row equivalence classes contain different-sized matrices?

**Problem 6**  —

How big are the row equivalence classes?

1. Show that the class of any zero matrix is finite.
2. Do any other classes contain only finitely many members?  
*This exercise is recommended for all readers.*

**Problem 7**  —

Give two reduced echelon form matrices that have their leading entries in the same columns, but that are not row equivalent.  
*This exercise is recommended for all readers.*

**Problem 8**  —

Show that any two $$n \! \times \! n$$ nonsingular matrices are row equivalent. Are any two singular matrices row equivalent?  
*This exercise is recommended for all readers.*

**Problem 9**  —

Describe all of the row equivalence classes containing these.

1. $$2 \! \times \! 2$$ matrices
2. $$2 \! \times \! 3$$ matrices
3. $$3 \! \times \! 2$$ matrices
4. $$3 \! \times \! 3$$ matrices

**Problem 10**  —

1. Show that a vector $$\vec{\beta}_0$$ is a linear combination of members of the set $$\{\vec{\beta}_1,\ldots,\vec{\beta}_n\}$$ if and only if there is a linear relationship $$\vec{0}=c_0\vec{\beta}_0+\cdots+c_n\vec{\beta}_n$$ where $$c_0$$ is not zero. (*Hint.* Watch out for the $$\vec{\beta}_0=\vec{0}$$ case.)
2. Use that to simplify the proof of Lemma 2.5.  
*This exercise is recommended for all readers.*

**Problem 11**  —

Finish the proof of Lemma 2.5.

1. First illustrate the inductive step by showing that $$c_2=0$$.
2. Do the full inductive step: where $$1\leq n<i-1$$, assume that $$c_k=0$$ for $$1<k< n$$ and deduce that $$c_{n+1}=0$$ also.
3. Find the contradiction.

**Problem 12**  —

Finish the induction argument in Lemma 2.6.

1. State the inductive hypothesis, Also state what must be shown to follow from that hypothesis.
2. Check that the inductive hypothesis implies that in the relationship $$\beta_{r+1}=s_{r+1,1}\delta_1+s_{r+2,2}\delta_2 +\dots+s_{r+1,m}\delta_m$$ the coefficients $$s_{r+1,1},\,\ldots\,,s_{r+1,r}$$ are each zero.
3. Finish the inductive step by arguing, as in the base case, that $$\ell_{r+1}<k_{r+1}$$ and $$k_{r+1}<\ell_{r+1}$$ are impossible.

**Problem 13**  —

Why, in the proof of Theorem 2.7, do we bother to restrict to the nonzero rows? Why not just stick to the relationship that we began with, $$\beta_i=c_{i,1}\delta_1+\dots+c_{i,m}\delta_m$$, with $$m$$ instead of $$r$$, and argue using it that the only nonzero coefficient is $$c_{i,i}$$, which is $$1$$?  
*This exercise is recommended for all readers.*

**Problem 14**  —

Three truck drivers went into a roadside cafe. One truck driver purchased four sandwiches, a cup of coffee, and ten doughnuts for $$\$8.45$$. Another driver purchased three sandwiches, a cup of coffee, and seven doughnuts for $$\$6.30$$. What did the third truck driver pay for a sandwich, a cup of coffee, and a doughnut? (Trono 1991)

**Problem 15**  —

The fact that Gaussian reduction disallows multiplication of a row by zero is needed for the proof of uniqueness of reduced echelon form, or else every matrix would be row equivalent to a matrix of all zeros. Where is it used?  
*This exercise is recommended for all readers.*

**Problem 16**  —

The Linear Combination Lemma says which equations can be gotten from Gaussian reduction from a given linear system.

1. Produce an equation not implied by this system.

$$
\begin{array}{rcrcr} 3x &- &y &= &8 \\ 2x &+ & y &= &3 \end{array}
$$

2. Can any equation be derived from an inconsistent system?

**Problem 17**  —

Extend the definition of row equivalence to linear systems. Under your definition, do equivalent systems have the same solution set? (Hoffman & Kunze 1971)  
*This exercise is recommended for all readers.*

**Problem 18**  —

In this matrix

$$
\begin{pmatrix} 1 &2 &3 \\ 3 &0 &3 \\ 1 &4 &5 \end{pmatrix}
$$

the first and second columns add to the third.

1. Show that remains true under any row operation.
2. Make a conjecture.
3. Prove that it holds.

Solutions

### Footnotes

### References

- Hoffman, Kenneth; Kunze, Ray (1971), *Linear Algebra* (Second ed.), Prentice Hall
- Trono, Tony (compilier) (1991), *University of Vermont Mathematics Department High School Prize Examinations 1958-1991*, mimeograhed printing

---

*Source: Wikibooks, Linear Algebra/Row Equivalence (https://en.wikibooks.org/wiki/Linear_Algebra/Row_Equivalence), by Wikibooks contributors, CC BY-SA 4.0.*
