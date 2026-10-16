# Definition and Examples of Vector Spaces

**Definition 1.1**  —

A **vector space** (over $$\R$$) consists of a set $$V$$ along with two operations "$$+$$" and "$$\cdot$$" subject to these conditions.

1. For any $$\vec v,\vec w\in V:\vec v+\vec w\in V$$ .
2. For any $$\vec v,\vec w\in V:\vec v+\vec w=\vec w+\vec v$$ .
3. For any $$\vec u,\vec v,\vec w\in V:(\vec v+\vec w)+\vec u=\vec v+(\vec w+\vec u)$$ .
4. There is a **zero vector** $$\vec0\in V$$ such that $$\vec v+\vec0=\vec v$$ for all $$\vec v\in V$$ .
5. Each $$\vec v\in V$$ has an **additive inverse** $$\vec w\in V$$ such that $$\vec w+\vec v=\vec0$$ .
6. If $$r$$ is a **scalar**, that is, a member of $$\R$$ and $$\vec v\in V$$ then the **scalar multiple** $$r\cdot\vec v$$ is in $$V$$ .
7. If $$r,s\in\R$$ and $$\vec v\in V$$ then $$(r+s)\cdot\vec v=r\cdot\vec v+s\cdot\vec v$$ .
8. If $$r\in\R$$ and $$\vec v,\vec w\in V$$ , then $$r\cdot(\vec v+\vec w)=r\cdot\vec v+r\cdot\vec w$$ .
9. If $$r,s\in\R$$ and $$\vec v\in V$$ , then $$(rs)\cdot\vec v=r\cdot(s\cdot\vec v)$$
10. For any $$\vec v\in V$$ , $$1\cdot\vec v=\vec v$$ .

**Remark 1.2**  —

Because it involves two kinds of addition and two kinds of multiplication, that definition may seem confused. For instance, in condition 7 "$$(r+s)\cdot\vec v=r\cdot\vec v+s\cdot\vec v$$", the first "$$+$$" is the real number addition operator while the "$$+$$" to the right of the equals sign represents vector addition in the structure $$V$$ . These expressions aren't ambiguous because, e.g., $$r$$ and $$s$$ are real numbers so "$$r+s$$" can only mean real number addition.

The best way to go through the examples below is to check all ten conditions in the definition. That check is written out at length in the first example. Use it as a model for the others. Especially important are the first condition "$$\vec v+\vec w$$ is in $$V$$" and the sixth condition "$$r\cdot\vec v$$ is in $$V$$". These are the **closure** conditions. They specify that the addition and scalar multiplication operations are always sensible — they are defined for every pair of vectors, and every scalar and vector, and the result of the operation is a member of the set (see Example 1.4).

**Example 1.3**  —

The set $$\R^2$$ is a vector space if the operations "$$+$$" and "$$\cdot$$" have their usual meaning.

$$
\binom{x_1}{x_2}+\binom{y_1}{y_2}=\binom{x_1+y_1}{x_2+y_2}\qquad r\cdot\binom{x_1}{x_2}=\binom{rx_1}{rx_2}
$$

We shall check all of the conditions.

There are five conditions in item 1. For 1, closure of addition, note that for any $$v_1,v_2,w_1,w_2\in\R$$ the result of the sum

$$
\binom{v_1}{v_2}+\binom{w_1}{w_2}=\binom{v_1+w_1}{v_2+w_2}
$$

is a column array with two real entries, and so is in $$\R^2$$ . For 2, that addition of vectors commutes, take all entries to be real numbers and compute

$$
\binom{v_1}{v_2}+\binom{w_1}{w_2}=\binom{v_1+w_1}{v_2+w_2}=\binom{w_1+v_1}{w_2+v_2}=\binom{w_1}{w_2}+\binom{v_1}{v_2}
$$

(the second equality follows from the fact that the components of the vectors are real numbers, and the addition of real numbers is commutative). Condition 3, associativity of vector addition, is similar.

$$
\begin{align} \Bigg(\binom{v_1}{v_2}+\binom{w_1}{w_2}\Bigg)+\binom{u_1}{u_2} &=\binom{(v_1+w_1)+u_1}{(v_2+w_2)+u_2}\\ &=\binom{v_1+(w_1+u_1)}{v_2+(w_2+u_2)}\\ &=\binom{v_1}{v_2}+\Bigg(\binom{w_1}{w_2}+\binom{u_1}{u_2}\Bigg) \end{align}
$$

For the fourth condition we must produce a zero element — the vector of zeroes is it.

$$
\binom{v_1}{v_2}+\binom00=\binom{v_1}{v_2}
$$

For 5, to produce an additive inverse, note that for any $$v_1,v_2\in\R$$ we have

$$
\binom{-v_1}{-v_2}+\binom{v_1}{v_2}=\binom00
$$

so the first vector is the desired additive inverse of the second.

The checks for the five conditions having to do with scalar multiplication are just as routine. For 6, closure under scalar multiplication, where $$r,v_1,v_2\in\R$$ ,

$$
r\cdot\binom{v_1}{v_2}=\binom{rv_1}{rv_2}
$$

is a column array with two real entries, and so is in $$\R^2$$ . Next, this checks 7.

$$
(r+s)\cdot\binom{v_1}{v_2}=\binom{(r+s)v_1}{(r+s)v_2}= \binom{rv_1+sv_1}{rv_2+sv_2}=r\cdot\binom{v_1}{v_2}+s\cdot\binom{v_1}{v_2}
$$

For 8, that scalar multiplication distributes from the left over vector addition, we have this.

$$
r\cdot\Bigg(\binom{v_1}{v_2}+\binom{w_1}{w_2}\Bigg)=\binom{r(v_1+w_1)}{r(v_2+w_2)} =\binom{rv_1+rw_1}{rv_2+rw_2}=r\cdot\binom{v_1}{v_2}+r\cdot\binom{w_1}{w_2}
$$

The ninth

$$
(rs)\cdot\binom{v_1}{v_2}=\binom{(rs)v_1}{(rs)v_2}=\binom{r(sv_1)}{r(sv_2)}=r\cdot\left(s\cdot\binom{v_1}{v_2}\right)
$$

and tenth conditions are also straightforward.

$$
1\cdot\binom{v_1}{v_2}=\binom{1v_1}{1v_2}=\binom{v_1}{v_2}
$$

In a similar way, each $$\mathbb{R}^n$$ is a vector space with the usual operations of vector addition and scalar multiplication. (In $$\mathbb{R}^1$$, we usually do not write the members as column vectors, i.e., we usually do not write "$$(\pi)$$". Instead we just write "$$\pi$$".)

**Example 1.4**  — This subset of $$\mathbb{R}^3$$ that is a plane through the origin

$$
P=\{ \begin{pmatrix} x \\ y \\ z \end{pmatrix} \,\big|\, x+y+z=0\}
$$

is a vector space if "+" and "$$\cdot$$" are interpreted in this way.

$$
\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} + \begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} = \begin{pmatrix} x_1+x_2 \\ y_1+y_2 \\ z_1+z_2 \end{pmatrix} \qquad r\cdot \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} rx \\ ry \\ rz \end{pmatrix}
$$

The addition and scalar multiplication operations here are just the ones of $$\mathbb{R}^3$$, reused on its subset $$P$$. We say that $$P$$ **inherits** these operations from $$\mathbb{R}^3$$. This example of an addition in $$P$$

$$
\begin{pmatrix} 1 \\ 1 \\ -2 \end{pmatrix}+\begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}=\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}
$$

illustrates that $$P$$ is closed under addition. We've added two vectors from $$P$$— that is, with the property that the sum of their three entries is zero— and the result is a vector also in $$P$$. Of course, this example of closure is not a proof of closure. To prove that $$P$$ is closed under addition, take two elements of $$P$$

$$
\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} \quad \begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}
$$

(membership in $$P$$ means that $$x_1+y_1+z_1=0$$ and $$x_2+y_2+z_2=0$$), and observe that their sum

$$
\begin{pmatrix} x_1+x_2 \\ y_1+y_2 \\ z_1+z_2 \end{pmatrix}
$$

is also in $$P$$ since its entries add $$(x_1+x_2)+(y_1+y_2)+(z_1+z_2)=(x_1+y_1+z_1)+(x_2+y_2+z_2)$$ to $$0$$. To show that $$P$$ is closed under scalar multiplication, start with a vector from $$P$$

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix}
$$

(so that $$x+y+z=0$$) and then for $$r\in\mathbb{R}$$ observe that the scalar multiple

$$
r\cdot\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} rx \\ ry \\ rz \end{pmatrix}
$$

satisfies that $$rx+ry+rz=r(x+y+z)=0$$. Thus the two closure conditions are satisfied. Verification of the other conditions in the definition of a vector space are just as straightforward.

**Example 1.5**  —

Example 1.3 shows that the set of all two-tall vectors with real entries is a vector space. Example 1.4 gives a subset of an $$\mathbb{R}^n$$ that is also a vector space. In contrast with those two, consider the set of two-tall columns with entries that are integers (under the obvious operations). This is a subset of a vector space, but it is not itself a vector space. The reason is that this set is not closed under scalar multiplication, that is, it does not satisfy condition 6. Here is a column with integer entries, and a scalar, such that the outcome of the operation

$$
0.5 \cdot \begin{pmatrix} 4 \\ 3 \end{pmatrix} = \begin{pmatrix} 2 \\ 1.5 \end{pmatrix}
$$

is not a member of the set, since its entries are not all integers.

**Example 1.6**  —

The singleton set

$$
\{ \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} \}
$$

is a vector space under the operations

$$
\begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} \qquad r\cdot \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}
$$

that it inherits from $$\mathbb{R}^4$$.

A vector space must have at least one element, its zero vector. Thus a one-element vector space is the smallest one possible.

**Definition 1.7**  —

A one-element vector space is a **trivial** space.

**Warning!**  —

The examples so far involve sets of column vectors with the usual operations. But vector spaces need not be collections of column vectors, or even of row vectors. Below are some other types of vector spaces. The term "vector space" does not mean "collection of columns of reals". It means something more like "collection in which any linear combination is sensible".

### Examples

**Example 1.8**  —

Consider $$\mathcal{P}_3=\{a_0+a_1x+a_2x^2+a_3x^3\,\big|\, a_0,\ldots,a_3\in\mathbb{R}\}$$, the set of polynomials of degree three or less (in this book, we'll take constant polynomials, including the zero polynomial, to be of degree zero). It is a vector space under the operations

$$
(a_0+a_1x+a_2x^2+a_3x^3)+(b_0+b_1x+b_2x^2+b_3x^3)
$$

$$
=(a_0+b_0)+(a_1+b_1)x+(a_2+b_2)x^2+(a_3+b_3)x^3
$$

and

$$
r\cdot(a_0+a_1x+a_2x^2+a_3x^3)=(ra_0)+(ra_1)x+(ra_2)x^2+(ra_3)x^3
$$

(the verification is easy). This vector space is worthy of attention because these are the polynomial operations familiar from high school algebra. For instance, $$3\cdot(1-2x+3x^2-4x^3)-2\cdot(2-3x+x^2-(1/2)x^3)=-1+7x^2-11x^3$$.

Although this space is not a subset of any $$\mathbb{R}^n$$, there is a sense in which we can think of $$\mathcal{P}_3$$ as "the same" as $$\mathbb{R}^4$$. If we identify these two spaces's elements in this way  

$$
a_0+a_1x+a_2x^2+a_3x^3 \quad\text{corresponds to}\quad \begin{pmatrix} a_0 \\ a_1 \\ a_2 \\ a_3 \end{pmatrix}
$$

then the operations also correspond. Here is an example of corresponding additions.

$$
\begin{array}{lr} &1-2x+0x^2+1x^3 \\ + &2+3x+7x^2-4x^3 \\ \hline &3+1x+7x^2-3x^3 \end{array} \quad\text{corresponds to}\quad \begin{pmatrix} 1 \\ -2 \\ 0 \\ 1 \end{pmatrix} + \begin{pmatrix} 2 \\ 3 \\ 7 \\ -4 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \\ 7 \\ -3 \end{pmatrix}
$$

Things we are thinking of as "the same" add to "the same" sum. Chapter Three makes precise this idea of vector space correspondence. For now we shall just leave it as an intuition.

**Example 1.9**  —

The set $$\mathcal{M}_{2 \! \times \! 2}$$ of $$2 \! \times \! 2$$ matrices with real number entries is a vector space under the natural entry-by-entry operations.  

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} + \begin{pmatrix} w &x \\ y &z \end{pmatrix} = \begin{pmatrix} a+w &b+x \\ c+y &d+z \end{pmatrix} \qquad r\cdot \begin{pmatrix} a &b \\ c &d \end{pmatrix} = \begin{pmatrix} ra &rb \\ rc &rd \end{pmatrix}
$$

As in the prior example, we can think of this space as "the same" as $$\mathbb{R}^4$$.

**Example 1.10**  —

The set $$\{f\,\big|\, f:\mathbb{N}\to\mathbb{R}\}$$ of all real-valued functions of one natural number variable is a vector space under the operations

$$
(f_1+f_2)\,(n)=f_1(n)+f_2(n) \qquad (r\cdot f)\,(n)=r\,f(n)
$$

so that if, for example, $$f_1(n)=n^2+2\sin(n)$$ and $$f_2(n)=-\sin(n)+0.5$$ then $$(f_1+2f_2)\,(n)=n^2+1$$.

We can view this space as a generalization of Example 1.3— instead of $$2$$-tall vectors, these functions are like infinitely-tall vectors.

$$
\begin{array}{c|c} n & f(n)=n^2+1 \\ \hline 0 & 1 \\ 1 & 2 \\ 2 & 5 \\ 3 & 10 \\ \vdots & \vdots \\ \end{array} \quad\text{corresponds to}\quad \begin{pmatrix} 1 \\ 2 \\ 5 \\ 10 \\ \vdots \end{pmatrix}
$$

Addition and scalar multiplication are component-wise, as in Example 1.3. (We can formalize "infinitely-tall" by saying that it means an infinite sequence, or that it means a function from $$\mathbb{N}$$ to $$\mathbb{R}$$.)

**Example 1.11**  —

The set of polynomials with real coefficients

$$
\{ a_0+a_1x+\cdots+a_nx^n\,\big|\, n\in\mathbb{N} \text{ and } a_0,\ldots,a_n\in\mathbb{R}\}
$$

makes a vector space when given the natural "$$+$$"

$$
(a_0+a_1x+\cdots+a_nx^n)+(b_0+b_1x+\cdots+b_nx^n)
$$

$$
=(a_0+b_0)+(a_1+b_1)x+\cdots +(a_n+b_n)x^n
$$

and "$$\cdot$$".

$$
r\cdot (a_0+a_1x+\ldots a_nx^n)=(ra_0)+(ra_1)x+\ldots (ra_n)x^n
$$

This space differs from the space $$\mathcal{P}_3$$ of Example 1.8. This space contains not just degree three polynomials, but degree thirty polynomials and degree three hundred polynomials, too. Each individual polynomial of course is of a finite degree, but the set has no single bound on the degree of all of its members.

This example, like the prior one, can be thought of in terms of infinite-tuples. For instance, we can think of $$1+3x+5x^2$$ as corresponding to $$(1,3,5,0,0,\ldots)$$. However, don't confuse this space with the one from Example 1.10. Each member of this set has a bounded degree, so under our correspondence there are no elements from this space matching $$(1,2,5,10,\,\ldots\,)$$. The vectors in this space correspond to infinite-tuples that end in zeroes.

**Example 1.12**  —

The set $$\{f\,\big|\, f:\mathbb{R}\to\mathbb{R}\}$$ of all real-valued functions of one real variable is a vector space under these.

$$
(f_1+f_2)\,(x)=f_1(x)+f_2(x) \qquad (r\cdot f)\,(x)=r\,f(x)
$$

The difference between this and Example 1.10 is the domain of the functions.

**Example 1.13**  —

The set $$F=\{ a\cos\theta+b\sin\theta \,\big|\, a,b\in\mathbb{R}\}$$ of real-valued functions of the real variable $$\theta$$ is a vector space under the operations

$$
(a_1\cos\theta+b_1\sin\theta)+(a_2\cos\theta+b_2\sin\theta) =(a_1+a_2)\cos\theta+(b_1+b_2)\sin\theta
$$

and

$$
r\cdot (a\cos\theta+b\sin\theta)=(ra)\cos\theta+(rb)\sin\theta
$$

inherited from the space in the prior example. (We can think of $$F$$ as "the same" as $$\mathbb{R}^2$$ in that $$a\cos\theta+b\sin\theta$$ corresponds to the vector with components $$a$$ and $$b$$.)

**Example 1.14**  —

The set

$$
\{f:\mathbb{R}\to\mathbb{R} \,\big|\, \dfrac{d^2f}{dx^2}+f=0\}
$$

is a vector space under the, by now natural, interpretation.

$$
(f+g)\,(x)=f(x)+g(x) \qquad (r\cdot f)\,(x)=r\,f(x)
$$

In particular, notice that closure is a consequence:

$$
\frac{d^2(f+g)}{dx^2}+(f+g) =(\frac{d^2f}{dx^2}+f)+(\frac{d^2g}{dx^2}+g)
$$

and

$$
\frac{d^2(rf)}{dx^2}+(rf) =r(\frac{d^2 f}{dx^2}+f)
$$

of basic Calculus. This turns out to equal the space from the prior example— functions satisfying this differential equation have the form $$a\cos\theta+b\sin\theta$$— but this description suggests an extension to solutions sets of other differential equations.

**Example 1.15**  —

The set of solutions of a homogeneous linear system in $$n$$ variables is a vector space under the operations inherited from $$\mathbb{R}^n$$. For closure under addition, if

$$
\vec{v}=\begin{pmatrix} v_1 \\ \vdots \\ v_n \end{pmatrix} \qquad \vec{w}=\begin{pmatrix} w_1 \\ \vdots \\ w_n \end{pmatrix}
$$

both satisfy the condition that their entries add to $$0$$ then $$\vec{v}+\vec{w}$$ also satisfies that condition: $$c_1(v_1+w_1)+\cdots+c_n(v_n+w_n) =(c_1v_1+\cdots+c_nv_n)+(c_1w_1+\cdots+c_nw_n) =0$$. The checks of the other conditions are just as routine.

As we've done in those equations, we often omit the multiplication symbol "$$\cdot$$". We can distinguish the multiplication in "$$c_1v_1$$" from that in "$$r\vec{v}\,$$" since if both multiplicands are real numbers then real-real multiplication must be meant, while if one is a vector then scalar-vector multiplication must be meant.

The prior example has brought us full circle since it is one of our motivating examples.

**Remark 1.16**  —

Now, with some feel for the kinds of structures that satisfy the definition of a vector space, we can reflect on that definition. For example, why specify in the definition the condition that $$1\cdot\vec{v}=\vec{v}$$ but not a condition that $$0\cdot\vec{v}=\vec{0}$$?

One answer is that this is just a definition— it gives the rules of the game from here on, and if you don't like it, put the book down and walk away.

Another answer is perhaps more satisfying. People in this area have worked hard to develop the right balance of power and generality. This definition has been shaped so that it contains the conditions needed to prove all of the interesting and important properties of spaces of linear combinations. As we proceed, we shall derive all of the properties natural to collections of linear combinations from the conditions given in the definition.

The next result is an example. We do not need to include these properties in the definition of vector space because they follow from the properties already listed there.

**Lemma 1.17**  —

In any vector space $$V$$, for any $$\vec{v}\in V$$ and $$r\in\mathbb{R}$$, we have

1. $$0\cdot\vec{v}=\vec{0}$$, and
2. $$(-1\cdot\vec{v})+\vec{v}=\vec{0}$$, and
3. $$r\cdot\vec{0}=\vec{0}$$.

**Proof**  —

For 1, note that $$\vec{v}=(1+0)\cdot\vec{v}=\vec{v}+(0\cdot\vec{v})$$. Add to both sides the additive inverse of $$\vec{v}$$, the vector $$\vec{w}$$ such that $$\vec{w}+\vec{v}=\vec{0}$$.

$$
\begin{array}{rl} \vec{w}+\vec{v} &=\vec{w}+\vec{v}+0\cdot\vec{v} \\ \vec{0} &=\vec{0}+0\cdot\vec{v} \\ \vec{0} &=0\cdot\vec{v} \end{array}
$$

The second item is easy: $$(-1\cdot\vec{v})+\vec{v}=(-1+1)\cdot\vec{v}=0\cdot\vec{v}=\vec{0}$$ shows that we can write "$$-\vec{v}\,$$" for the additive inverse of $$\vec{v}$$ without worrying about possible confusion with $$(-1)\cdot\vec{v}$$.

For 3, this $$r\cdot\vec{0}=r\cdot(0\cdot\vec{0})=(r\cdot 0)\cdot\vec{0}=\vec{0}$$ will do.

### Summary

We finish with a recap.

Our study in Chapter One of Gaussian reduction led us to consider collections of linear combinations. So in this chapter we have defined a vector space to be a structure in which we can form such combinations, expressions of the form $$c_1\cdot\vec{v}_1+\dots+c_n\cdot\vec{v}_n$$ (subject to simple conditions on the addition and scalar multiplication operations). In a phrase: vector spaces are the right context in which to study linearity.

Finally, a comment. From the fact that it forms a whole chapter, and especially because that chapter is the first one, a reader could come to think that the study of linear systems is our purpose. The truth is, we will not so much use vector spaces in the study of linear systems as we will instead have linear systems start us on the study of vector spaces. The wide variety of examples from this subsection shows that the study of vector spaces is interesting and important in its own right, aside from how it helps us understand linear systems. Linear systems won't go away. But from now on our primary objects of study will be vector spaces.

### Exercises

**Problem 1**  —

Name the zero vector for each of these vector spaces.

1. The space of degree three polynomials under the natural operations
2. The space of $$2 \! \times \! 4$$ matrices
3. The space $$\{f:[0,1]\to\mathbb{R}\,\big|\, f\text{ is continuous}\}$$
4. The space of real-valued functions of one natural number variable  
*This exercise is recommended for all readers.*

**Problem 2**  —

Find the additive inverse, in the vector space, of the vector.

1. In $$\mathcal{P}_3$$, the vector $$-3-2x+x^2$$.
2. In the space $$2 \! \times \! 2$$,

$$
\begin{pmatrix} 1 &-1 \\ 0 &3 \end{pmatrix}.
$$

3. In $$\{ae^x+be^{-x}\,\big|\, a,b\in\mathbb{R}\}$$, the space of functions of the real variable $$x$$ under the natural operations, the vector $$3e^x-2e^{-x}$$.  
*This exercise is recommended for all readers.*

**Problem 3**  —

Show that each of these is a vector space.

1. The set of linear polynomials $$\mathcal{P}_1=\{a_0+a_1x\,\big|\, a_0,a_1\in\mathbb{R}\}$$ under the usual polynomial addition and scalar multiplication operations.
2. The set of $$2 \! \times \! 2$$ matrices with real entries under the usual matrix operations.
3. The set of three-component row vectors with their usual operations.
4. The set

$$
L=\{\begin{pmatrix} x \\ y \\ z \\ w \end{pmatrix}\in\mathbb{R}^4\,\big|\, x+y-z+w=0\}
$$

under the operations inherited from $$\mathbb{R}^4$$.  
*This exercise is recommended for all readers.*

**Problem 4**  —

Show that each of these is not a vector space. (*Hint.* Start by listing two members of each set.)

1. Under the operations inherited from $$\mathbb{R}^3$$, this set

$$
\{\begin{pmatrix} x \\ y \\ z \end{pmatrix}\in\mathbb{R}^3\,\big|\, x+y+z=1\}
$$

2. Under the operations inherited from $$\mathbb{R}^3$$, this set

$$
\{\begin{pmatrix} x \\ y \\ z \end{pmatrix}\in\mathbb{R}^3\,\big|\, x^2+y^2+z^2=1\}
$$

3. Under the usual matrix operations,

$$
\{\begin{pmatrix} a &1 \\ b &c \end{pmatrix} \,\big|\, a,b,c\in\mathbb{R}\}
$$

4. Under the usual polynomial operations,

$$
\{a_0+a_1x+a_2x^2\,\big|\, a_0,a_1,a_2\in\mathbb{R}^+\}
$$

where $$\mathbb{R}^+$$ is the set of reals greater than zero
5. Under the inherited operations,

$$
\{\begin{pmatrix} x \\ y \end{pmatrix}\in\mathbb{R}^2\,\big|\, x+3y=4 \text{ and } 2x-y=3 \text{ and } 6x+4y=10\}
$$

**Problem 5**  —

Define addition and scalar multiplication operations to make the complex numbers a vector space over $$\mathbb{R}$$.  
*This exercise is recommended for all readers.*

**Problem 6**  —

Is the set of rational numbers a vector space over $$\mathbb{R}$$ under the usual addition and scalar multiplication operations?

**Problem 7**  —

Show that the set of linear combinations of the variables $$x,y,z$$ is a vector space under the natural addition and scalar multiplication operations.

**Problem 8**  —

Prove that this is not a vector space: the set of two-tall column vectors with real entries subject to these operations.

$$
\begin{pmatrix} x_1 \\ y_1 \end{pmatrix} +\begin{pmatrix} x_2 \\ y_2 \end{pmatrix} =\begin{pmatrix} x_1-x_2 \\ y_1-y_2 \end{pmatrix} \qquad r\cdot\begin{pmatrix} x \\ y \end{pmatrix} =\begin{pmatrix} rx \\ ry \end{pmatrix}
$$

**Problem 9**  —

Prove or disprove that $$\mathbb{R}^3$$ is a vector space under these operations.

1. $$\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} +\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \quad\text{and}\quad r\begin{pmatrix} x \\ y \\ z \end{pmatrix} =\begin{pmatrix} rx \\ ry \\ rz \end{pmatrix}$$
2. $$\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} +\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \quad\text{and}\quad r\begin{pmatrix} x \\ y \\ z \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 10**  —

For each, decide if it is a vector space; the intended operations are the natural ones.

1. The **diagonal** $$2 \! \times \! 2$$ matrices

$$
\{\begin{pmatrix} a &0 \\ 0 &b \end{pmatrix}\,\big|\, a,b\in\mathbb{R}\}
$$

2. This set of $$2 \! \times \! 2$$ matrices

$$
\{\begin{pmatrix} x &x+y \\ x+y &y \end{pmatrix}\,\big|\, x,y\in\mathbb{R}\}
$$

3. This set

$$
\{\begin{pmatrix} x \\ y \\ z \\ w \end{pmatrix}\in\mathbb{R}^4 \,\big|\, x+y+w=1\}
$$

4. The set of functions $$\{f:\mathbb{R}\to\mathbb{R}\,\big|\, df/dx+2f=0\}$$
5. The set of functions $$\{f:\mathbb{R}\to\mathbb{R}\,\big|\, df/dx+2f=1\}$$  
*This exercise is recommended for all readers.*

**Problem 11**  —

Prove or disprove that this is a vector space: the real-valued functions $$f$$ of one real variable such that $$f(7)=0$$.  
*This exercise is recommended for all readers.*

**Problem 12**  —

Show that the set $$\mathbb{R}^+$$ of positive reals is a vector space when "$$x+y$$" is interpreted to mean the product of $$x$$ and $$y$$ (so that $$2+3$$ is $$6$$), and "$$r\cdot x$$" is interpreted as the $$r$$-th power of $$x$$.

**Problem 13**  —

Is $$\{(x,y)\,\big|\, x,y\in\mathbb{R}\}$$ a vector space under these operations?

1. $$(x_1,y_1)+(x_2,y_2)=(x_1+x_2,y_1+y_2)$$ and $$r\cdot (x,y)=(rx,y)$$
2. $$(x_1,y_1)+(x_2,y_2)=(x_1+x_2,y_1+y_2)$$ and $$r\cdot (x,y)=(rx,0)$$

**Problem 14**  —

Prove or disprove that this is a vector space: the set of polynomials of degree greater than or equal to two, along with the zero polynomial.

**Problem 15**  —

At this point "the same" is only an intuition, but nonetheless for each vector space identify the $$k$$ for which the space is "the same" as $$\mathbb{R}^k$$.

1. The $$2 \! \times \! 3$$ matrices under the usual operations
2. The $$n \! \times \! m$$ matrices (under their usual operations)
3. This set of $$2 \! \times \! 2$$ matrices

$$
\{\begin{pmatrix} a &0 \\ b &c \end{pmatrix} \,\big|\, a,b,c\in\mathbb{R}\}
$$

4. This set of $$2 \! \times \! 2$$ matrices

$$
\{\begin{pmatrix} a &0 \\ b &c \end{pmatrix} \,\big|\, a+b+c=0\}
$$

*This exercise is recommended for all readers.*

**Problem 16**  —

Using $$\vec{+}$$ to represent vector addition and $$\,\vec{\cdot}\,$$ for scalar multiplication, restate the definition of vector space.  
*This exercise is recommended for all readers.*

**Problem 17**  —

Prove these.

1. Any vector is the additive inverse of the additive inverse of itself.
2. Vector addition left-cancels: if $$\vec{v},\vec{s},\vec{t}\in V$$ then $$\vec{v}+\vec{s}=\vec{v}+\vec{t}\,$$ implies that $$\vec{s}=\vec{t}$$.

**Problem 18**  —

The definition of vector spaces does not explicitly say that $$\vec{0}+\vec{v}=\vec{v}$$ (it instead says that $$\vec{v}+\vec{0}=\vec{v}$$). Show that it must nonetheless hold in any vector space.  
*This exercise is recommended for all readers.*

**Problem 19**  —

Prove or disprove that this is a vector space: the set of all matrices, under the usual operations.

**Problem 20**  —

In a vector space every element has an additive inverse. Can some elements have two or more?

**Problem 21**  —

1. Prove that every point, line, or plane thru the origin in $$\mathbb{R}^3$$ is a vector space under the inherited operations.
2. What if it doesn't contain the origin?  
*This exercise is recommended for all readers.*

**Problem 22**  —

Using the idea of a vector space we can easily reprove that the solution set of a homogeneous linear system has either one element or infinitely many elements. Assume that $$\vec{v}\in V$$ is not $$\vec{0}$$.

1. Prove that $$r\cdot\vec{v}=\vec{0}$$ if and only if $$r=0$$.
2. Prove that $$r_1\cdot\vec{v}=r_2\cdot\vec{v}$$ if and only if $$r_1=r_2$$.
3. Prove that any nontrivial vector space is infinite.
4. Use the fact that a nonempty solution set of a homogeneous linear system is a vector space to draw the conclusion.

**Problem 23**  —

Is this a vector space under the natural operations: the real-valued functions of one real variable that are differentiable?

**Problem 24**  —

A **vector space over the complex numbers** $$\mathbb{C}$$ has the same definition as a vector space over the reals except that scalars are drawn from $$\mathbb{C}$$ instead of from $$\mathbb{R}$$. Show that each of these is a vector space over the complex numbers. (Recall how complex numbers add and multiply: $$(a_0+a_1i)+(b_0+b_1i)=(a_0+b_0)+(a_1+b_1)i$$ and $$(a_0+a_1i)(b_0+b_1i)=(a_0b_0-a_1b_1)+(a_0b_1+a_1b_0)i$$.)

1. The set of degree two polynomials with complex coefficients
2. This set

$$
\{\begin{pmatrix} 0 &a \\ b &0 \end{pmatrix}\,\big|\, a,b\in\mathbb{C}\text{ and } a+b=0+0i \}
$$

**Problem 25**  —

Name a property shared by all of the $$\mathbb{R}^n$$'s but not listed as a requirement for a vector space.  
*This exercise is recommended for all readers.*

**Problem 26**  —

1. Prove that a sum of four vectors $$\vec{v}_1,\ldots,\vec{v}_4\in V$$ can be associated in any way without changing the result.

$$
\begin{array}{rl} ((\vec{v}_1+\vec{v}_2)+\vec{v}_3)+\vec{v}_4 &=(\vec{v}_1+(\vec{v}_2+\vec{v}_3))+\vec{v}_4 \\ &=(\vec{v}_1+\vec{v}_2)+(\vec{v}_3+\vec{v}_4) \\ &=\vec{v}_1+((\vec{v}_2+\vec{v}_3)+\vec{v}_4) \\ &=\vec{v}_1+(\vec{v}_2+(\vec{v}_3+\vec{v}_4)) \end{array}
$$

This allows us to simply write "$$\vec{v}_1+\vec{v}_2+\vec{v}_3+\vec{v}_4$$" without ambiguity.
2. Prove that any two ways of associating a sum of any number of vectors give the same sum. (*Hint.* Use induction on the number of vectors.)

**Problem 27**  —

For any vector space, a subset that is itself a vector space under the inherited operations (e.g., a plane through the origin inside of $$\mathbb{R}^3$$) is a **subspace**.

1. Show that $$\{a_0+a_1x+a_2x^2\,\big|\, a_0+a_1+a_2=0\}$$ is a subspace of the vector space of degree two polynomials.
2. Show that this is a subspace of the $$2 \! \times \! 2$$ matrices.

$$
\{\begin{pmatrix} a &b \\ c &0 \end{pmatrix} \,\big|\, a+b=0\}
$$

3. Show that a nonempty subset $$S$$ of a real vector space is a subspace if and only if it is closed under linear combinations of pairs of vectors: whenever $$c_1,c_2\in\mathbb{R}$$ and $$\vec{s}_1,\vec{s}_2\in S$$ then the combination $$c_1\vec{s}_1+c_2\vec{s}_2$$ is in $$S$$.

Solutions

---

*Source: Wikibooks, Linear Algebra/Definition and Examples of Vector Spaces (https://en.wikibooks.org/wiki/Linear_Algebra/Definition_and_Examples_of_Vector_Spaces), by Wikibooks contributors, CC BY-SA 4.0.*
