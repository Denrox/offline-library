# Properties of Determinants

As described above, we want a formula to determine whether an $$n \! \times \! n$$ matrix is nonsingular. We will not begin by stating such a formula. Instead, we will begin by considering the function that such a formula calculates. We will define the function by its properties, then prove that the function with these properties exists and is unique and also describe formulas that compute this function. (Because we will show that the function exists and is unique, from the start we will say "$$\det(T)$$" instead of "if there is a determinant function then $$\det(T)$$" and "the determinant" instead of "any determinant".)

**Definition 2.1**  —

A $$n \! \times \! n$$ **determinant** is a function $$\det:\mathcal{M}_{n \! \times \! n}\to \mathbb{R}$$ such that

1. $$\det (\vec{\rho}_1,\dots,k\cdot\vec{\rho}_i + \vec{\rho}_j,\dots,\vec{\rho}_n) =\det (\vec{\rho}_1,\dots,\vec{\rho}_j,\dots,\vec{\rho}_n)$$ for $$i\ne j$$
2. $$\det (\vec{\rho}_1,\ldots,\vec{\rho}_j, \dots,\vec{\rho}_i,\dots,\vec{\rho}_n) = -\det (\vec{\rho}_1,\dots,\vec{\rho}_i,\dots,\vec{\rho}_j, \dots,\vec{\rho}_n)$$ for $$i\ne j$$
3. $$\det (\vec{\rho}_1,\dots,k\vec{\rho}_i,\dots,\vec{\rho}_n) = k\cdot \det (\vec{\rho}_1,\dots,\vec{\rho}_i,\dots,\vec{\rho}_n)$$ for $$k\ne 0$$
4. $$\det(I)=1$$ where $$I$$ is an identity matrix

(the $$\vec{\rho}\,$$'s are the rows of the matrix). We often write $$\left|T\right|$$ for $$\det (T)$$.

**Remark 2.2**  —

Property (2) is redundant since

$$
T\;\xrightarrow[]{\rho_i+\rho_j} \;\xrightarrow[]{-\rho_j+\rho_i} \;\xrightarrow[]{\rho_i+\rho_j} \;\xrightarrow[]{-\rho_i} \;\hat{T}
$$

swaps rows $$i$$ and $$j$$. It is listed only for convenience.

The first result shows that a function satisfying these conditions gives a criteria for nonsingularity. (Its last sentence is that, in the context of the first three conditions, (4) is equivalent to the condition that the determinant of an echelon form matrix is the product down the diagonal.)

**Lemma 2.3**  —

A matrix with two identical rows has a determinant of zero. A matrix with a zero row has a determinant of zero. A matrix is nonsingular if and only if its determinant is nonzero. The determinant of an echelon form matrix is the product down its diagonal.

**Proof**  —

To verify the first sentence, swap the two equal rows. The sign of the determinant changes, but the matrix is unchanged and so its determinant is unchanged. Thus the determinant is zero.

For the second sentence, we multiply a zero row by −1 and apply property (3). Multiplying a zero row with a constant leaves the matrix unchanged, so property (3) implies that $$\det(T) = -\det(T)$$. The only way this can be is if $$\det(T) = 0$$.

For the third sentence, where $$T \rightarrow\cdots\rightarrow\hat{T}$$ is the Gauss-Jordan reduction, by the definition the determinant of $$T$$ is zero if and only if the determinant of $$\hat{T}$$ is zero (although they could differ in sign or magnitude). A nonsingular $$T$$ Gauss-Jordan reduces to an identity matrix and so has a nonzero determinant. A singular $$T$$ reduces to a $$\hat{T}$$ with a zero row; by the second sentence of this lemma its determinant is zero.

Finally, for the fourth sentence, if an echelon form matrix is singular then it has a zero on its diagonal, that is, the product down its diagonal is zero. The third sentence says that if a matrix is singular then its determinant is zero. So if the echelon form matrix is singular then its determinant equals the product down its diagonal.

If an echelon form matrix is nonsingular then none of its diagonal entries is zero so we can use property (3) of the definition to factor them out (again, the vertical bars $$\left|\cdots\right|$$ indicate the determinant operation).

$$
\begin{vmatrix} t_{1,1} &t_{1,2} & &t_{1,n} \\ 0 &t_{2,2} & &t_{2,n} \\ & &\ddots \\ 0 & & &t_{n,n} \end{vmatrix} = t_{1,1}\cdot t_{2,2}\cdots t_{n,n}\cdot \begin{vmatrix} 1 &t_{1,2}/t_{1,1} & &t_{1,n}/t_{1,1} \\ 0 &1 & &t_{2,n}/t_{2,2} \\ & &\ddots \\ 0 & & &1 \end{vmatrix}
$$

Next, the Jordan half of Gauss-Jordan elimination, using property (1) of the definition, leaves the identity matrix.

$$
= t_{1,1}\cdot t_{2,2}\cdots t_{n,n}\cdot \begin{vmatrix} 1 &0 & &0 \\ 0 &1 & &0 \\ & &\ddots \\ 0 & & &1 \end{vmatrix} = t_{1,1}\cdot t_{2,2}\cdots t_{n,n}\cdot 1
$$

Therefore, if an echelon form matrix is nonsingular then its determinant is the product down its diagonal.

That result gives us a way to compute the value of a determinant function on a matrix. Do Gaussian reduction, keeping track of any changes of sign caused by row swaps and any scalars that are factored out, and then finish by multiplying down the diagonal of the echelon form result. This procedure takes the same time as Gauss' method and so is sufficiently fast to be practical on the size matrices that we see in this book.

**Example 2.4**  —

Doing $$2 \! \times \! 2$$ determinants

$$
\begin{vmatrix} 2 &4 \\ -1 &3 \end{vmatrix} = \begin{vmatrix} 2 &4 \\ 0 &5 \end{vmatrix} =10
$$

with Gauss' method won't give a big savings because the $$2 \! \times \! 2$$ determinant formula is so easy. However, a $$3 \! \times \! 3$$ determinant is usually easier to calculate with Gauss' method than with the formula given earlier.

$$
\begin{vmatrix} 2 &2 &6 \\ 4 &4 &3 \\ 0 &-3 &5 \end{vmatrix} = \begin{vmatrix} 2 &2 &6 \\ 0 &0 &-9 \\ 0 &-3 &5 \end{vmatrix} = -\begin{vmatrix} 2 &2 &6 \\ 0 &-3 &5 \\ 0 &0 &-9 \end{vmatrix} =-54
$$

**Example 2.5**  —

Determinants of matrices any bigger than $$3 \! \times \! 3$$ are almost always most quickly done with this Gauss' method procedure.

$$
\begin{vmatrix} 1 &0 &1 &3 \\ 0 &1 &1 &4 \\ 0 &0 &0 &5 \\ 0 &1 &0 &1 \end{vmatrix} = \begin{vmatrix} 1 &0 &1 &3 \\ 0 &1 &1 &4 \\ 0 &0 &0 &5 \\ 0 &0 &-1 &-3 \end{vmatrix} = -\begin{vmatrix} 1 &0 &1 &3 \\ 0 &1 &1 &4 \\ 0 &0 &-1 &-3 \\ 0 &0 &0 &5 \end{vmatrix} =-(-5)=5
$$

The prior example illustrates an important point. Although we have not yet found a $$4 \! \times \! 4$$ determinant formula, if one exists then we know what value it gives to the matrix — if there is a function with properties (1)-(4) then on the above matrix the function must return $$5$$.

**Lemma 2.6**  —

For each $$n$$, if there is an $$n \! \times \! n$$ determinant function then it is unique.

**Proof**  —

For any $$n \! \times \! n$$ matrix we can perform Gauss' method on the matrix, keeping track of how the sign alternates on row swaps, and then multiply down the diagonal of the echelon form result. By the definition and the lemma, all $$n \! \times \! n$$ determinant functions must return this value on this matrix. Thus all $$n \! \times \! n$$ determinant functions are equal, that is, there is only one input argument/output value relationship satisfying the four conditions.

The "if there is an $$n \! \times \! n$$ determinant function" emphasizes that, although we can use Gauss' method to compute the only value that a determinant function could possibly return, we haven't yet shown that such a determinant function exists for all $$n$$. In the rest of the section we will produce determinant functions.

### Exercises

*For these, assume that an $$n \! \times \! n$$ determinant function exists for all $$n$$.*  
*This exercise is recommended for all readers.*

**Problem 1**  —

Use Gauss' method to find each determinant.

1. $$\begin{vmatrix} 3 &1 &2 \\ 3 &1 &0 \\ 0 &1 &4 \end{vmatrix}$$
2. $$\begin{vmatrix} 1 &0 &0 &1 \\ 2 &1 &1 &0 \\ -1 &0 &1 &0 \\ 1 &1 &1 &0 \end{vmatrix}$$

**Problem 2**  — Use Gauss' method to find each.

1. $$\begin{vmatrix} 2 &-1 \\ -1 &-1 \end{vmatrix}$$
2. $$\begin{vmatrix} 1 &1 &0 \\ 3 &0 &2 \\ 5 &2 &2 \end{vmatrix}$$

**Problem 3**  —

For which values of $$k$$ does this system have a unique solution?

$$
\begin{array}{rcrcrcrcr} x & & &+ &z &- &w &= &2 \\ & &y &- &2z & & &= &3 \\ x & & &+ &kz & & &= &4 \\ & & & &z &- &w &= &2 \end{array}
$$

*This exercise is recommended for all readers.*

**Problem 4**  —

Express each of these in terms of $$\left|H\right|$$.

1. $$\begin{vmatrix} h_{3,1} &h_{3,2} &h_{3,3} \\ h_{2,1} &h_{2,2} &h_{2,3} \\ h_{1,1} &h_{1,2} &h_{1,3} \end{vmatrix}$$
2. $$\begin{vmatrix} -h_{1,1} &-h_{1,2} &-h_{1,3} \\ -2h_{2,1} &-2h_{2,2} &-2h_{2,3} \\ -3h_{3,1} &-3h_{3,2} &-3h_{3,3} \end{vmatrix}$$
3. $$\begin{vmatrix} h_{1,1}+h_{3,1} &h_{1,2}+h_{3,2} &h_{1,3}+h_{3,3} \\ h_{2,1} &h_{2,2} &h_{2,3} \\ 5h_{3,1} &5h_{3,2} &5h_{3,3} \end{vmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 5**  —

Find the determinant of a diagonal matrix.

**Problem 6**  —

Describe the solution set of a homogeneous linear system if the determinant of the matrix of coefficients is nonzero.  
*This exercise is recommended for all readers.*

**Problem 7**  —

Show that this determinant is zero.

$$
\begin{vmatrix} y+z &x+z &x+y \\ x &y &z \\ 1 &1 &1 \end{vmatrix}
$$

**Problem 8**  —

1. Find the $$1 \! \times \! 1$$, $$2 \! \times \! 2$$, and $$3 \! \times \! 3$$ matrices with $$i,j$$ entry given by $$(-1)^{i+j}$$.
2. Find the determinant of the square matrix with $$i,j$$ entry $$(-1)^{i+j}$$.

**Problem 9**  —

1. Find the $$1 \! \times \! 1$$, $$2 \! \times \! 2$$, and $$3 \! \times \! 3$$ matrices with $$i,j$$ entry given by $$i+j$$.
2. Find the determinant of the square matrix with $$i,j$$ entry $$i+j$$.  
*This exercise is recommended for all readers.*

**Problem 10**  —

Show that determinant functions are not linear by giving a case where $$\left|A+B\right|\neq\left|A\right|+\left|B\right|$$.

**Problem 11**  —

The second condition in the definition, that row swaps change the sign of a determinant, is somewhat annoying. It means we have to keep track of the number of swaps, to compute how the sign alternates. Can we get rid of it? Can we replace it with the condition that row swaps leave the determinant unchanged? (If so then we would need new $$1 \! \times \! 1$$, $$2 \! \times \! 2$$, and $$3 \! \times \! 3$$ formulas, but that would be a minor matter.)

**Problem 12**  —

Prove that the determinant of any triangular matrix, upper or lower, is the product down its diagonal.

**Problem 13**  —

Refer to the definition of elementary matrices in the Mechanics of Matrix Multiplication subsection.

1. What is the determinant of each kind of elementary matrix?
2. Prove that if $$E$$ is any elementary matrix then $$\left|ES\right|=\left|E\right|\left|S\right|$$ for any appropriately sized $$S$$.
3. *(This question doesn't involve determinants.)* Prove that if $$T$$ is singular then a product $$TS$$ is also singular.
4. Show that $$\left|TS\right|=\left|T\right|\left|S\right|$$.
5. Show that if $$T$$ is nonsingular then $$\left|T^{-1}\right|=\left|T\right|^{-1}$$.

**Problem 14**  —

Prove that the determinant of a product is the product of the determinants $$\left|TS\right|=\left|T\right|\,\left|S\right|$$ in this way. Fix the $$n \! \times \! n$$ matrix $$S$$ and consider the function $$d:\mathcal{M}_{n \! \times \! n}\to \mathbb{R}$$ given by $$T\mapsto \left|TS\right|/\left|S\right|$$.

1. Check that $$d$$ satisfies property (1) in the definition of a determinant function.
2. Check property (2).
3. Check property (3).
4. Check property (4).
5. Conclude the determinant of a product is the product of the determinants.

**Problem 15**  —

A **submatrix** of a given matrix $$A$$ is one that can be obtained by deleting some of the rows and columns of $$A$$. Thus, the first matrix here is a submatrix of the second.

$$
\begin{pmatrix} 3 &1 \\ 2 &5 \end{pmatrix} \qquad \begin{pmatrix} 3 &4 &1 \\ 0 &9 &-2 \\ 2 &-1 &5 \end{pmatrix}
$$

Prove that for any square matrix, the rank of the matrix is $$r$$ if and only if $$r$$ is the largest integer such that there is an $$r \! \times \! r$$ submatrix with a nonzero determinant.  
*This exercise is recommended for all readers.*

**Problem 16**  —

Prove that a matrix with rational entries has a rational determinant.

**? Problem 17**  —

Find the element of likeness in (a) simplifying a fraction, (b) powdering the nose, (c) building new steps on the church, (d) keeping emeritus professors on campus, (e) putting $$B$$, $$C$$, $$D$$ in the determinant

$$
\begin{vmatrix} 1 &a &a^2 &a^3 \\ a^3 &1 &a &a^2 \\ B &a^3 &1 &a \\ C &D &a^3 &1 \end{vmatrix}.
$$

(Anning & Trigg 1953)

Solutions

### References

- Anning, Norman (proposer); Trigg, C. W. (solver) (1953), "Elementary problem 1016", *American Mathematical Monthly*, **60** (2), American Mathematical Society: 115 {{citation}}: Unknown parameter |month= ignored (help).

---

*Source: Wikibooks, Linear Algebra/Properties of Determinants (https://en.wikibooks.org/wiki/Linear_Algebra/Properties_of_Determinants), by Wikibooks contributors, CC BY-SA 4.0.*
