# Exploration

*This subsection is optional. It briefly describes how an investigator might come to a good general definition, which is given in the next subsection.*

The three cases above don't show an evident pattern to use for the general $$n \! \times \! n$$ formula. We may spot that the $$1 \! \times \! 1$$ term $$a$$ has one letter, that the $$2 \! \times \! 2$$ terms $$ad$$ and $$bc$$ have two letters, and that the $$3 \! \times \! 3$$ terms $$aei$$, etc., have three letters. We may also observe that in those terms there is a letter from each row and column of the matrix, e.g., the letters in the $$cdh$$ term

$$
\begin{pmatrix} & &c \\ d \\ &h \end{pmatrix}
$$

come one from each row and one from each column. But these observations perhaps seem more puzzling than enlightening. For instance, we might wonder why some of the terms are added while others are subtracted.

A good problem solving strategy is to see what properties a solution must have and then search for something with those properties. So we shall start by asking what properties we require of the formulas.

At this point, our primary way to decide whether a matrix is singular is to do Gaussian reduction and then check whether the diagonal of resulting echelon form matrix has any zeroes (that is, to check whether the product down the diagonal is zero). So, we may expect that the proof that a formula determines singularity will involve applying Gauss' method to the matrix, to show that in the end the product down the diagonal is zero if and only if the determinant formula gives zero. This suggests our initial plan: we will look for a family of functions with the property of being unaffected by row operations and with the property that a determinant of an echelon form matrix is the product of its diagonal entries. Under this plan, a proof that the functions determine singularity would go, "Where $$T\rightarrow\cdots\rightarrow\hat{T}$$ is the Gaussian reduction, the determinant of $$T$$ equals the determinant of $$\hat{T}$$ (because the determinant is unchanged by row operations), which is the product down the diagonal, which is zero if and only if the matrix is singular". In the rest of this subsection we will test this plan on the $$2 \! \times \! 2$$ and $$3 \! \times \! 3$$ determinants that we know. We will end up modifying the "unaffected by row operations" part, but not by much.

The first step in checking the plan is to test whether the $$2 \! \times \! 2$$ and $$3 \! \times \! 3$$ formulas are unaffected by the row operation of pivoting: if

$$
T \xrightarrow[]{k\rho_i+\rho_j} \hat{T}
$$

then is $$\det(\hat{T})=\det(T)$$? This check of the $$2 \! \times \! 2$$ determinant after the $$k\rho_1+\rho_2$$ operation

$$
\det( \begin{pmatrix} a &b \\ ka+c &kb+d \\ \end{pmatrix} ) = a(kb+d)-(ka+c)b = ad-bc
$$

shows that it is indeed unchanged, and the other $$2 \! \times \! 2$$ pivot $$k\rho_2+\rho_1$$ gives the same result. The $$3 \! \times \! 3$$ pivot $$k\rho_3+\rho_2$$ leaves the determinant unchanged

$$
\begin{array}{rl} \det( \begin{pmatrix} a &b &c \\ kg+d &kh+e &ki+f \\ g &h &i \end{pmatrix} ) &=\begin{array}{l} a(kh+e)i+b(ki+f)g+c(kg+d)h \\ \ -h(ki+f)a-i(kg+d)b-g(kh+e)c \end{array} \\ &=aei + bfg + cdh - hfa - idb - gec \end{array}
$$

as do the other $$3 \! \times \! 3$$ pivot operations.

So there seems to be promise in the plan. Of course, perhaps the $$4 \! \times \! 4$$ determinant formula is affected by pivoting. We are exploring a possibility here and we do not yet have all the facts. Nonetheless, so far, so good.

The next step is to compare $$\det(\hat{T})$$ with $$\det(T)$$ for the operation

$$
T \xrightarrow[]{ {\rho}_i \leftrightarrow {\rho}_j } \hat{T}
$$

of swapping two rows. The $$2 \! \times \! 2$$ row swap $$\rho_1\leftrightarrow\rho_2$$

$$
\det( \begin{pmatrix} c &d \\ a &b \end{pmatrix} ) = cb - ad
$$

does not yield $$ad-bc$$. This $$\rho_1\leftrightarrow\rho_3$$ swap inside of a $$3 \! \times \! 3$$ matrix

$$
\det( \begin{pmatrix} g &h &i \\ d &e &f \\ a &b &c \end{pmatrix} ) = gec + hfa + idb - bfg - cdh - aei
$$

also does not give the same determinant as before the swap — again there is a sign change. Trying a different $$3 \! \times \! 3$$ swap $$\rho_1\leftrightarrow\rho_2$$

$$
\det( \begin{pmatrix} d &e &f \\ a &b &c \\ g &h &i \end{pmatrix} ) = dbi + ecg + fah - hcd - iae - gbf
$$

also gives a change of sign.

Thus, row swaps appear to change the sign of a determinant. This modifies our plan, but does not wreck it. We intend to decide nonsingularity by considering only whether the determinant is zero, not by considering its sign. Therefore, instead of expecting determinants to be entirely unaffected by row operations, will look for them to change sign on a swap.

To finish, we compare $$\det(\hat{T})$$ to $$\det(T)$$ for the operation

$$
T \xrightarrow[]{ k{\rho}_i } \hat{T}
$$

of multiplying a row by a scalar $$k\neq 0$$. One of the $$2 \! \times \! 2$$ cases is

$$
\det( \begin{pmatrix} a &b \\ kc &kd \end{pmatrix} ) = a(kd) - (kc)b =k\cdot (ad-bc)
$$

and the other case has the same result. Here is one $$3 \! \times \! 3$$ case

$$
\begin{array}{rl} \det( \begin{pmatrix} a &b &c \\ d &e &f \\ kg &kh &ki \end{pmatrix} ) &= \begin{array}{l} ae(ki) + bf(kg) + cd(kh) \\ \quad -(kh)fa - (ki)db - (kg)ec \end{array} \\ &= k\cdot(aei + bfg + cdh - hfa - idb - gec) \end{array}
$$

and the other two are similar. These lead us to suspect that multiplying a row by $$k$$ multiplies the determinant by $$k$$. This fits with our modified plan because we are asking only that the zeroness of the determinant be unchanged and we are not focusing on the determinant's sign or magnitude.

In summary, to develop the scheme for the formulas to compute determinants, we look for determinant functions that remain unchanged under the pivoting operation, that change sign on a row swap, and that rescale on the rescaling of a row. In the next two subsections we will find that for each $$n$$ such a function exists and is unique.

For the next subsection, note that, as above, scalars come out of each row without affecting other rows. For instance, in this equality

$$
\det( \begin{pmatrix} 3 &3 &9 \\ 2 &1 &1 \\ 5 &10 &-5 \end{pmatrix} ) =3 \cdot \det( \begin{pmatrix} 1 &1 &3 \\ 2 &1 &1 \\ 5 &10 &-5 \end{pmatrix} )
$$

the $$3$$ isn't factored out of all three rows, only out of the top row. The determinant acts on each row independently of the other rows. When we want to use this property of determinants, we shall write the determinant as a function of the rows: "$$\det (\vec{\rho}_1,\vec{\rho}_2,\dots\vec{\rho}_n)$$", instead of as "$$\det(T)$$" or "$$\det(t_{1,1},\dots,t_{n,n})$$". The definition of the determinant that starts the next subsection is written in this way.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Evaluate the determinant of each.

1. $$\begin{pmatrix} 3 &1 \\ -1 &1 \end{pmatrix}$$
2. $$\begin{pmatrix} 2 &0 &1 \\ 3 &1 &1 \\ -1 &0 &1 \end{pmatrix}$$
3. $$\begin{pmatrix} 4 &0 &1 \\ 0 &0 &1 \\ 1 &3 &-1 \end{pmatrix}$$

**Problem 2**  —

Evaluate the determinant of each.

1. $$\begin{pmatrix} 2 &0 \\ -1 &3 \end{pmatrix}$$
2. $$\begin{pmatrix} 2 &1 &1 \\ 0 &5 &-2 \\ 1 &-3 &4 \end{pmatrix}$$
3. $$\begin{pmatrix} 2 &3 &4 \\ 5 &6 &7 \\ 8 &9 &1 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

Verify that the determinant of an upper-triangular $$3 \! \times \! 3$$ matrix is the product down the diagonal.

$$
\det( \begin{pmatrix} a &b &c \\ 0 &e &f \\ 0 &0 &i \end{pmatrix} ) =aei
$$

Do lower-triangular matrices work the same way?  
*This exercise is recommended for all readers.*

**Problem 4**  —

Use the determinant to decide if each is singular or nonsingular.

1. $$\begin{pmatrix} 2 &1 \\ 3 &1 \end{pmatrix}$$
2. $$\begin{pmatrix} 0 &1 \\ 1 &-1 \end{pmatrix}$$
3. $$\begin{pmatrix} 4 &2 \\ 2 &1 \end{pmatrix}$$

**Problem 5**  —

Singular or nonsingular? Use the determinant to decide.

1. $$\begin{pmatrix} 2 &1 &1 \\ 3 &2 &2 \\ 0 &1 &4 \end{pmatrix}$$
2. $$\begin{pmatrix} 1 &0 &1 \\ 2 &1 &1 \\ 4 &1 &3 \end{pmatrix}$$
3. $$\begin{pmatrix} 2 &1 &0 \\ 3 &-2 &0 \\ 1 &0 &0 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 6**  —

Each pair of matrices differ by one row operation. Use this operation to compare $$\det(A)$$ with $$\det(B)$$.

1. $$A=\begin{pmatrix} 1 &2 \\ 2 &3 \end{pmatrix}$$ $$B=\begin{pmatrix} 1 &2 \\ 0 &-1 \end{pmatrix}$$
2. $$A=\begin{pmatrix} 3 &1 &0 \\ 0 &0 &1 \\ 0 &1 &2 \end{pmatrix}$$ $$B=\begin{pmatrix} 3 &1 &0 \\ 0 &1 &2 \\ 0 &0 &1 \end{pmatrix}$$
3. $$A=\begin{pmatrix} 1 &-1 &3 \\ 2 &2 &-6 \\ 1 &0 &4 \end{pmatrix}$$ $$B=\begin{pmatrix} 1 &-1 &3 \\ 1 &1 &-3 \\ 1 &0 &4 \end{pmatrix}$$

**Problem 7**  —

Show this.

$$
\det( \begin{pmatrix} 1 &1 &1 \\ a &b &c \\ a^2 &b^2 &c^2 \end{pmatrix} ) =(b-a)(c-a)(c-b)
$$

*This exercise is recommended for all readers.*

**Problem 8**  —

Which real numbers $$x$$ make this matrix singular?

$$
\begin{pmatrix} 12-x &4 \\ 8 &8-x \end{pmatrix}
$$

**Problem 9**  —

Do the Gaussian reduction to check the formula for $$3 \! \times \! 3$$ matrices stated in the preamble to this section.

$$\begin{pmatrix} a &b &c \\ d &e &f \\ g &h &i \end{pmatrix}$$ is nonsingular iff $$aei+bfg+cdh-hfa-idb-gec \neq 0$$

**Problem 10**  —

Show that the equation of a line in $$\mathbb{R}^2$$ thru $$(x_1,y_1)$$ and $$(x_2,y_2)$$ is expressed by this determinant.

$$
\det( \begin{pmatrix} x &y &1 \\ x_1 &y_1 &1 \\ x_2 &y_2 &1 \end{pmatrix})=0 \qquad x_1\neq x_2
$$

*This exercise is recommended for all readers.*

**Problem 11**  —

Many people know this mnemonic for the determinant of a $$3 \! \times \! 3$$ matrix: first repeat the first two columns and then sum the products on the forward diagonals and subtract the products on the backward diagonals. That is, first write

$$
\left(\begin{array}{ccc|cc} h_{1,1} &h_{1,2} &h_{1,3} &h_{1,1} &h_{1,2} \\ h_{2,1} &h_{2,2} &h_{2,3} &h_{2,1} &h_{2,2} \\ h_{3,1} &h_{3,2} &h_{3,3} &h_{3,1} &h_{3,2} \end{array}\right)
$$

and then calculate this.

$$
\begin{array}{l} h_{1,1}h_{2,2}h_{3,3}+h_{1,2}h_{2,3}h_{3,1}+h_{1,3}h_{2,1}h_{3,2} \\ \quad-h_{3,1}h_{2,2}h_{1,3}-h_{3,2}h_{2,3}h_{1,1} -h_{3,3}h_{2,1}h_{1,2} \end{array}
$$

1. Check that this agrees with the formula given in the preamble to this section.
2. Does it extend to other-sized determinants?

**Problem 12**  —

The **cross product** of the vectors

$$
\vec{x}=\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} \qquad \vec{y}=\begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix}
$$

is the vector computed as this determinant.

$$
\vec{x}\times\vec{y}= \det(\begin{pmatrix} \vec{e}_1 &\vec{e}_2 &\vec{e}_3 \\ x_1 &x_2 &x_3 \\ y_1 &y_2 &y_3 \end{pmatrix})
$$

Note that the first row is composed of vectors, the vectors from the standard basis for $$\mathbb{R}^3$$. Show that the cross product of two vectors is perpendicular to each vector.

**Problem 13**  —

Prove that each statement holds for $$2 \! \times \! 2$$ matrices.

1. The determinant of a product is the product of the determinants $$\det(ST)=\det(S)\cdot\det(T)$$.
2. If $$T$$ is invertible then the determinant of the inverse is the inverse of the determinant $$\det(T^{-1})=(\,\det(T)\,)^{-1}$$.

Matrices $$T$$ and $$T^\prime$$ are **similar** if there is a nonsingular matrix $$P$$ such that $$T^\prime=PTP^{-1}$$. (This definition is in Chapter Five.) Show that similar $$2 \! \times \! 2$$ matrices have the same determinant.  
*This exercise is recommended for all readers.*

**Problem 14**  —

Prove that the area of this region in the plane

is equal to the value of this determinant.

$$
\det( \begin{pmatrix} x_1 &x_2 \\ y_1 &y_2 \end{pmatrix})
$$

Compare with this.

$$
\det( \begin{pmatrix} x_2 &x_1 \\ y_2 &y_1 \end{pmatrix})
$$

**Problem 15**  —

Prove that for $$2 \! \times \! 2$$ matrices, the determinant of a matrix equals the determinant of its transpose. Does that also hold for $$3 \! \times \! 3$$ matrices?  
*This exercise is recommended for all readers.*

**Problem 16**  —

Is the determinant function linear — is $$\det(x\cdot T+y\cdot S)=x\cdot \det(T)+y\cdot \det(S)$$?

**Problem 17**  —

Show that if $$A$$ is $$3 \! \times \! 3$$ then $$\det(c\cdot A)=c^3\cdot \det(A)$$ for any scalar $$c$$.

**Problem 18**  —

Which real numbers $$\theta$$ make

$$
\begin{pmatrix} \cos\theta &-\sin\theta \\ \sin\theta &\cos\theta \end{pmatrix}
$$

singular? Explain geometrically.

**? Problem 19**  —

If a third order determinant has elements $$1$$, $$2$$, ..., $$9$$, what is the maximum value it may have? (Haggett & Saunders 1955)

Solutions

### References

- Haggett, Vern (proposer); Saunders, F. W. (solver) (1955), "Elementary problem 1135", *American Mathematical Monthly*, **62** (5), American Mathematical Society: 257 {{citation}}: Unknown parameter |month= ignored (help).

---

*Source: Wikibooks, Linear Algebra/Exploration (https://en.wikibooks.org/wiki/Linear_Algebra/Exploration), by Wikibooks contributors, CC BY-SA 4.0.*
