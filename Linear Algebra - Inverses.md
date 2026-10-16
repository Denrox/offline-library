# Inverses

We now consider how to represent the inverse of a linear map.

We start by recalling some facts about function inverses. Some functions have no inverse, or have an inverse on the left side or right side only.

**Example 4.1**  —

Where $$\pi:\mathbb{R}^3\to \mathbb{R}^2$$ is the projection map

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} \mapsto \begin{pmatrix} x \\ y \end{pmatrix}
$$

and $$\eta:\mathbb{R}^2\to \mathbb{R}^3$$ is the embedding

$$
\begin{pmatrix} x \\ y \end{pmatrix} \mapsto \begin{pmatrix} x \\ y \\ 0 \end{pmatrix}
$$

the composition $$\pi\circ \eta$$ is the identity map on $$\mathbb{R}^2$$.

$$
\begin{pmatrix} x \\ y \end{pmatrix} \stackrel{\eta}{\longmapsto} \begin{pmatrix} x \\ y \\ 0 \end{pmatrix} \stackrel{\pi}{\longmapsto} \begin{pmatrix} x \\ y \end{pmatrix}
$$

We say $$\pi$$ is a **left inverse map** of $$\eta$$ or, what is the same thing, that $$\eta$$ is a **right inverse map** of $$\pi$$. However, composition in the other order $$\eta\circ \pi$$ doesn't give the identity map— here is a vector that is not sent to itself under $$\eta\circ \pi$$.

$$
\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \stackrel{\pi}{\longmapsto} \begin{pmatrix} 0 \\ 0 \end{pmatrix} \stackrel{\eta}{\longmapsto} \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$

In fact, the projection $$\pi$$ has no left inverse at all. For, if $$f$$ were to be a left inverse of $$\pi$$ then we would have

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} \stackrel{\pi}{\longmapsto} \begin{pmatrix} x \\ y \end{pmatrix} \stackrel{f}{\longmapsto} \begin{pmatrix} x \\ y \\ z \end{pmatrix}
$$

for all of the infinitely many $$z$$'s. But no function $$f$$ can send a single argument to more than one value.

(An example of a function with no inverse on either side is the zero transformation on $$\mathbb{R}^2$$.) Some functions have a **two-sided inverse map**, another function that is the inverse of the first, both from the left and from the right. For instance, the map given by $$\vec{v}\mapsto 2\cdot \vec{v}$$ has the two-sided inverse $$\vec{v}\mapsto (1/2)\cdot\vec{v}$$. In this subsection we will focus on two-sided inverses. The appendix shows that a function has a two-sided inverse if and only if it is both one-to-one and onto. The appendix also shows that if a function $$f$$ has a two-sided inverse then it is unique, and so it is called "the" inverse, and is denoted $$f^{-1}$$. So our purpose in this subsection is, where a linear map $$h$$ has an inverse, to find the relationship between $${\rm Rep}_{B,D}(h)$$ and $${\rm Rep}_{D,B}(h^{-1})$$ (recall that we have shown, in [Theorem II.2.21](Linear%20Algebra%20-%20Rangespace%20and%20Nullspace.md) of Section II of this chapter, that if a linear map has an inverse then the inverse is a linear map also).

**Definition 4.2**  —

A matrix $$G$$ is a **left inverse matrix** of the matrix $$H$$ if $$GH$$ is the identity matrix. It is a **right inverse matrix** if $$HG$$ is the identity. A matrix $$H$$ with a two-sided inverse is an **invertible matrix**. That two-sided inverse is called **the inverse matrix** and is denoted $$H^{-1}$$.

Because of the correspondence between linear maps and matrices, statements about map inverses translate into statements about matrix inverses.

**Lemma 4.3**  —

If a matrix has both a left inverse and a right inverse then the two are equal.

**Theorem 4.4**  —

A matrix is invertible if and only if it is nonsingular.

**Proof**  —

*(For both results.)* Given a matrix $$H$$, fix spaces of appropriate dimension for the domain and codomain. Fix bases for these spaces. With respect to these bases, $$H$$ represents a map $$h$$. The statements are true about the map and therefore they are true about the matrix.

**Lemma 4.5**  —

A product of invertible matrices is invertible— if $$G$$ and $$H$$ are invertible and if $$GH$$ is defined then $$GH$$ is invertible and $$(GH)^{-1}=H^{-1}G^{-1}$$.

**Proof**  —

*(This is just like the prior proof except that it requires two maps.)* Fix appropriate spaces and bases and consider the represented maps $$h$$ and $$g$$. Note that $$h^{-1}g^{-1}$$ is a two-sided map inverse of $$gh$$ since $$(h^{-1}g^{-1})(gh) = h^{-1}(\text{id})h =h^{-1}h =\text{id}$$ and $$(gh)(h^{-1}g^{-1}) = g(\text{id})g^{-1} =gg^{-1} =\text{id}$$. This equality is reflected in the matrices representing the maps, as required.

Here is the arrow diagram giving the relationship between map inverses and matrix inverses. It is a special case of the diagram for function composition and matrix multiplication.

Beyond its place in our general program of seeing how to represent map operations, another reason for our interest in inverses comes from solving linear systems. A linear system is equivalent to a matrix equation, as here.

$$
\begin{array}{rcrcr} x_1 &+ &x_2 &= &3 \\ 2x_1 &- &x_2 &= &2 \end{array} \quad\Longleftrightarrow\quad \begin{pmatrix} 1 &1 \\ 2 &-1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \end{pmatrix} \qquad\qquad (*)
$$

By fixing spaces and bases (e.g., $$\mathbb{R}^2,\mathbb{R}^2$$ and $$\mathcal{E}_2,\mathcal{E}_2$$), we take the matrix $$H$$ to represent some map $$h$$. Then solving the system is the same as asking: what domain vector $$\vec{x}$$ is mapped by $$h$$ to the result $$\vec{d}\,$$? If we could invert $$h$$ then we could solve the system by multiplying $${\rm Rep}_{D,B}(h^{-1})\cdot{\rm Rep}_{D}(\vec{d})$$ to get $${\rm Rep}_{B}(\vec{x})$$.

**Example 4.6**  —

We can find a left inverse for the matrix just given

$$
\begin{pmatrix} m &n \\ p &q \end{pmatrix} \begin{pmatrix} 1 &1 \\ 2 &-1 \end{pmatrix} = \begin{pmatrix} 1 &0 \\ 0 &1 \end{pmatrix}
$$

by using Gauss' method to solve the resulting linear system.

$$
\begin{array}{rcrcrcrcr} m &+ &2n & & & & &= &1 \\ m &- &n & & & & &= &0 \\ & & & &p &+ &2q &= &0 \\ & & & &p &- &q &= &1 \end{array}
$$

Answer: $$m=1/3$$, $$n=1/3$$, $$p=2/3$$, and $$q=-1/3$$. This matrix is actually the two-sided inverse of $$H$$, as can easily be checked. With it we can solve the system ($$*$$) above by applying the inverse.

$$
\begin{pmatrix} x \\ y \end{pmatrix} =\begin{pmatrix} 1/3 &1/3 \\ 2/3 &-1/3 \end{pmatrix} \begin{pmatrix} 3 \\ 2 \end{pmatrix} =\begin{pmatrix} 5/3 \\ 4/3 \end{pmatrix}
$$

**Remark 4.7**  —

Why solve systems this way, when Gauss' method takes less arithmetic (this assertion can be made precise by counting the number of arithmetic operations, as computer algorithm designers do)? Beyond its conceptual appeal of fitting into our program of discovering how to represent the various map operations, solving linear systems by using the matrix inverse has at least two advantages.

First, once the work of finding an inverse has been done, solving a system with the same coefficients but different constants is easy and fast: if we change the entries on the right of the system ($$*$$) then we get a related problem

$$
\begin{pmatrix} 1 &1 \\ 2 &-1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \end{pmatrix}
$$

with a related solution method.

$$
\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 1/3 &1/3 \\ 2/3 &-1/3 \end{pmatrix} \begin{pmatrix} 5 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}
$$

In applications, solving many systems having the same matrix of coefficients is common.

Another advantage of inverses is that we can explore a system's sensitivity to changes in the constants. For example, tweaking the $$3$$ on the right of the system ($$*$$) to

$$
\begin{pmatrix} 1 &1 \\ 2 &-1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 3.01 \\ 2 \end{pmatrix}
$$

can be solved with the inverse.

$$
\begin{pmatrix} 1/3 &1/3 \\ 2/3 &-1/3 \end{pmatrix} \begin{pmatrix} 3.01 \\ 2 \end{pmatrix} = \begin{pmatrix} (1/3)(3.01)+(1/3)(2) \\ (2/3)(3.01)-(1/3)(2) \end{pmatrix}
$$

to show that $$x_1$$ changes by $$1/3$$ of the tweak while $$x_2$$ moves by $$2/3$$ of that tweak. This sort of analysis is used, for example, to decide how accurately data must be specified in a linear model to ensure that the solution has a desired accuracy.

We finish by describing the computational procedure usually used to find the inverse matrix.

**Lemma 4.8**  —

A matrix is invertible if and only if it can be written as the product of elementary reduction matrices. The inverse can be computed by applying to the identity matrix the same row steps, in the same order, as are used to Gauss-Jordan reduce the invertible matrix.

**Proof**  —

A matrix $$H$$ is invertible if and only if it is nonsingular and thus Gauss-Jordan reduces to the identity. By [Corollary 3.22](Linear%20Algebra%20-%20Mechanics%20of%20Matrix%20Multiplication.md) this reduction can be done with elementary matrices $$R_r\cdot R_{r-1}\dots R_1\cdot H=I$$. This equation gives the two halves of the result.

First, elementary matrices are invertible and their inverses are also elementary. Applying $$R_r^{-1}$$ to the left of both sides of that equation, then $$R_{r-1}^{-1}$$, etc., gives $$H$$ as the product of elementary matrices $$H=R_1^{-1}\cdots R_r^{-1}\cdot I$$ (the $$I$$ is here to cover the trivial $$r=0$$ case).

Second, matrix inverses are unique and so comparison of the above equation with $$H^{-1}H=I$$ shows that $$H^{-1}=R_r\cdot R_{r-1}\dots R_1\cdot I$$. Therefore, applying $$R_1$$ to the identity, followed by $$R_2$$, etc., yields the inverse of $$H$$.

**Example 4.9**  —

To find the inverse of

$$
\begin{pmatrix} 1 &1 \\ 2 &-1 \end{pmatrix}
$$

we do Gauss-Jordan reduction, meanwhile performing the same operations on the identity. For clerical convenience we write the matrix and the identity side-by-side, and do the reduction steps together.

$$
\begin{array}{rcl} \left(\begin{array}{cc|cc} 1 &1 &1 &0 \\ 2 &-1 &0 &1 \end{array}\right) &\xrightarrow[]{-2\rho_1+\rho_2} &\left(\begin{array}{cc|cc} 1 &1 &1 &0 \\ 0 &-3 &-2 &1 \end{array}\right) \\ &\xrightarrow[]{-1/3\rho_2} &\left(\begin{array}{cc|cc} 1 &1 &1 &0 \\ 0 &1 &2/3 &-1/3 \end{array}\right) \\ &\xrightarrow[]{-\rho_2+\rho_1} &\left(\begin{array}{cc|cc} 1 &0 &1/3 &1/3 \\ 0 &1 &2/3 &-1/3 \end{array}\right) \end{array}
$$

This calculation has found the inverse.

$$
\begin{pmatrix} 1 &1 \\ 2 &-1 \end{pmatrix}^{-1} = \begin{pmatrix} 1/3 &1/3 \\ 2/3 &-1/3 \end{pmatrix}
$$

**Example 4.10**  —

This one happens to start with a row swap.

$$
\begin{array}{rcl} \left(\begin{array}{ccc|ccc} 0 &3 &-1 &1 &0 &0 \\ 1 &0 &1 &0 &1 &0 \\ 1 &-1 &0 &0 &0 &1 \end{array}\right) &\xrightarrow[]{\rho_1\leftrightarrow\rho_2} & \left(\begin{array}{ccc|ccc} 1 &0 &1 &0 &1 &0 \\ 0 &3 &-1 &1 &0 &0 \\ 1 &-1 &0 &0 &0 &1 \end{array}\right) \\ &\xrightarrow[]{-\rho_1+\rho_3} & \left(\begin{array}{ccc|ccc} 1 &0 &1 &0 &1 &0 \\ 0 &3 &-1 &1 &0 &0 \\ 0 &-1 &-1 &0 &-1 &1 \end{array}\right) \\ &\vdots \\ &\xrightarrow[]{} & \left(\begin{array}{ccc|ccc} 1 &0 &0 &1/4 &1/4 &3/4 \\ 0 &1 &0 &1/4 &1/4 &-1/4 \\ 0 &0 &1 &-1/4 &3/4 &-3/4 \end{array}\right) \end{array}
$$

**Example 4.11**  —

A non-invertible matrix is detected by the fact that the left half won't reduce to the identity.

$$
\left(\begin{array}{cc|cc} 1 &1 &1 &0 \\ 2 &2 &0 &1 \end{array}\right) \xrightarrow[]{-2\rho_1+\rho_2} \left(\begin{array}{cc|cc} 1 &1 &1 &0 \\ 0 &0 &-2 &1 \end{array}\right)
$$

This procedure will find the inverse of a general $$n \! \times \! n$$ matrix. The $$2 \! \times \! 2$$ case is handy.

**Corollary 4.12**  —

The inverse for a $$2 \! \times \! 2$$ matrix exists and equals

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix}^{-1} = \frac{1}{ad-bc} \begin{pmatrix} d &-b \\ -c &a \end{pmatrix}
$$

if and only if $$ad-bc\neq 0$$.

**Proof**  —

This computation is Problem 10.

We have seen here, as in the Mechanics of Matrix Multiplication subsection, that we can exploit the correspondence between linear maps and matrices. So we can fruitfully study both maps and matrices, translating back and forth to whichever helps us the most.

Over the entire four subsections of this section we have developed an algebra system for matrices. We can compare it with the familiar algebra system for the real numbers. Here we are working not with numbers but with matrices. We have matrix addition and subtraction operations, and they work in much the same way as the real number operations, except that they only combine same-sized matrices. We also have a matrix multiplication operation and an operation inverse to multiplication. These are somewhat like the familiar real number operations (associativity, and distributivity over addition, for example), but there are differences (failure of commutativity, for example). And, we have scalar multiplication, which is in some ways another extension of real number multiplication. This matrix system provides an example that algebra systems other than the elementary one can be interesting and useful.

### Exercises

**Problem 1**  —

Supply the intermediate steps in Example 4.10.  
*This exercise is recommended for all readers.*

**Problem 2**  —

Use Corollary 4.12 to decide if each matrix has an inverse.

1. $$\begin{pmatrix} 2 &1 \\ -1 &1 \end{pmatrix}$$
2. $$\begin{pmatrix} 0 &4 \\ 1 &-3 \end{pmatrix}$$
3. $$\begin{pmatrix} 2 &-3 \\ -4 &6 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

For each invertible matrix in the prior problem, use Corollary 4.12 to find its inverse.  
*This exercise is recommended for all readers.*

**Problem 4**  —

Find the inverse, if it exists, by using the Gauss-Jordan method. Check the answers for the $$2 \! \times \! 2$$ matrices with Corollary 4.12.

1. $$\begin{pmatrix} 3 &1 \\ 0 &2 \end{pmatrix}$$
2. $$\begin{pmatrix} 2 &1/2 \\ 3 &1 \end{pmatrix}$$
3. $$\begin{pmatrix} 2 &-4 \\ -1 &2 \end{pmatrix}$$
4. $$\begin{pmatrix} 1 &1 &3 \\ 0 &2 &4 \\ -1 &1 &0 \end{pmatrix}$$
5. $$\begin{pmatrix} 0 &1 &5 \\ 0 &-2 &4 \\ 2 &3 &-2 \end{pmatrix}$$
6. $$\begin{pmatrix} 2 &2 &3 \\ 1 &-2 &-3 \\ 4 &-2 &-3 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 5**  —

What matrix has this one for its inverse?

$$
\begin{pmatrix} 1 &3 \\ 2 &5 \end{pmatrix}
$$

**Problem 6**  —

How does the inverse operation interact with scalar multiplication and addition of matrices?

1. What is the inverse of $$rH$$?
2. Is $$(H+G)^{-1}=H^{-1}+G^{-1}$$?  
*This exercise is recommended for all readers.*

**Problem 7**  —

Is $$(T^k)^{-1}=(T^{-1})^k$$?

**Problem 8**  —

Is $$H^{-1}$$ invertible?

**Problem 9**  —

For each real number $$\theta$$ let $$t_\theta:\mathbb{R}^2\to \mathbb{R}^2$$ be represented with respect to the standard bases by this matrix.

$$
\begin{pmatrix} \cos\theta &-\sin\theta \\ \sin\theta &\cos\theta \end{pmatrix}
$$

Show that $$t_{\theta_1+\theta_2}=t_{\theta_1}\cdot t_{\theta_2}$$. Show also that $${t_{\theta}}^{-1}=t_{-\theta}$$.

**Problem 10**  —

Do the calculations for the proof of Corollary 4.12.

**Problem 11**  —

Show that this matrix

$$
H=\begin{pmatrix} 1 &0 &1 \\ 0 &1 &0 \end{pmatrix}
$$

has infinitely many right inverses. Show also that it has no left inverse.

**Problem 12**  —

In Example 4.1, how many left inverses has $$\eta$$?

**Problem 13**  —

If a matrix has infinitely many right-inverses, can it have infinitely many left-inverses? Must it have?  
*This exercise is recommended for all readers.*

**Problem 14**  —

Assume that $$H$$ is invertible and that $$HG$$ is the zero matrix. Show that $$G$$ is a zero matrix.

**Problem 15**  —

Prove that if $$H$$ is invertible then the inverse commutes with a matrix $$GH^{-1}=H^{-1}G$$ if and only if $$H$$ itself commutes with that matrix $$GH=HG$$.  
*This exercise is recommended for all readers.*

**Problem 16**  —

Show that if $$T$$ is square and if $$T^4$$ is the zero matrix then $$(I-T)^{-1}=I+T+T^2+T^3$$. Generalize.  
*This exercise is recommended for all readers.*

**Problem 17**  —

Let $$D$$ be diagonal. Describe $$D^2$$, $$D^3$$, ... , etc. Describe $$D^{-1}$$, $$D^{-2}$$, ... , etc. Define $$D^0$$ appropriately.

**Problem 18**  —

Prove that any matrix row-equivalent to an invertible matrix is also invertible.

**Problem 19**  —

*The first question below appeared as Problem 15 in the Matrix Multiplication subsection.*

1. Show that the rank of the product of two matrices is less than or equal to the minimum of the rank of each.
2. Show that if $$T$$ and $$S$$ are square then $$TS=I$$ if and only if $$ST=I$$.

**Problem 20**  —

Show that the inverse of a permutation matrix is its transpose.

**Problem 21**  —

*The first two parts of this question appeared as Problem 12. of the Matrix Multiplication subsection*

1. Show that $${{(GH)}^{\rm trans}}={{H}^{\rm trans}}{{G}^{\rm trans}}$$.
2. A square matrix is **symmetric** if each $$i,j$$ entry equals the $$j,i$$ entry (that is, if the matrix equals its transpose). Show that the matrices $$H{{H}^{\rm trans}}$$ and $${{H}^{\rm trans}}H$$ are symmetric.
3. Show that the inverse of the transpose is the transpose of the inverse.
4. Show that the inverse of a symmetric matrix is symmetric.  
*This exercise is recommended for all readers.*

**Problem 22**  —

*The items starting this question appeared as Problem 17 of the Matrix Multiplication subsection.*

1. Prove that the composition of the projections $$\pi_x,\pi_y:\mathbb{R}^3\to \mathbb{R}^3$$ is the zero map despite that neither is the zero map.
2. Prove that the composition of the derivatives $$d^2/dx^2,\,d^3/dx^3:\mathcal{P}_4\to \mathcal{P}_4$$ is the zero map despite that neither map is the zero map.
3. Give matrix equations representing each of the prior two items.

When two things multiply to give zero despite that neither is zero, each is said to be a **zero divisor**. Prove that no zero divisor is invertible.

**Problem 23**  —

In real number algebra, there are exactly two numbers, $$1$$ and $$-1$$, that are their own multiplicative inverse. Does $$H^2=I$$ have exactly two solutions for $$2 \! \times \! 2$$ matrices?

**Problem 24**  —

Is the relation "is a two-sided inverse of" transitive? Reflexive? Symmetric?

**Problem 25**  —

Prove: if the sum of the elements in each row of a square matrix is $$k$$, then the sum of the elements in each row of the inverse matrix is $$1/k$$. (Wilansky 1951) harv error: no target: CITEREFWilansky1951 (help)

Solutions

### Footnotes

### References

- Wilansky, Albert, "The Row-Sum of the Inverse Matrix", *American Mathematical Monthly*, **58** (9), Mathematical Association of America: 614 {{citation}}: Unknown parameter |month= ignored (help).

---

*Source: Wikibooks, Linear Algebra/Inverses (https://en.wikibooks.org/wiki/Linear_Algebra/Inverses), by Wikibooks contributors, CC BY-SA 4.0.*
