# General = Particular + Homogeneous

### Description of Solution Sets

The prior subsection has many descriptions of solution sets. They all fit a pattern. They have a vector that is a particular solution of the system added to an unrestricted combination of some other vectors. The solution set from [Example 2.13](Linear%20Algebra%20-%20Describing%20the%20Solution%20Set.md) illustrates.

$$
\left\{ \underbrace{ \begin{pmatrix} 0 \\ 4 \\ 0 \\ 0 \\ 0 \end{pmatrix}}_{\begin{array}{c}\\[-19pt]\scriptstyle\text{particular} \\[-5pt]\scriptstyle\text{solution}\end{array}}+ \underbrace{w\begin{pmatrix} 1 \\ -1 \\ 3 \\ 1 \\ 0 \end{pmatrix}+ u\begin{pmatrix} 1/2 \\ -1 \\ 1/2 \\ 0 \\ 1 \end{pmatrix}}_{\begin{array}{c}\\[-19pt]\scriptstyle\text{unrestricted}\\[-5pt]\scriptstyle\text{combination}\end{array}} \,\big|\, w,u\in\mathbb{R}\right\}
$$

The combination is unrestricted in that $$w$$ and $$u$$ can be any real numbers— there is no condition like "such that $$2w-u=0$$" that would restrict which pairs $$w,u$$ can be used to form combinations.

That example shows an infinite solution set conforming to the pattern. We can think of the other two kinds of solution sets as also fitting the same pattern. A one-element solution set fits in that it has a particular solution, and the unrestricted combination part is a trivial sum (that is, instead of being a combination of two vectors, as above, or a combination of one vector, it is a combination of no vectors). A zero-element solution set fits the pattern since there is no particular solution, and so the set of sums of that form is empty.

We will show that the examples from the prior subsection are representative, in that the description pattern discussed above holds for every solution set.

**Theorem 3.1**  — For any linear system there are vectors $$\vec{\beta}_1$$, ..., $$\vec{\beta}_k$$ such that the solution set can be described as

$$
\left\{\vec{p}+c_1\vec{\beta}_1+\,\cdots\,+c_k\vec{\beta}_k \,\big|\, c_1,\,\ldots\,,c_k\in\mathbb{R}\right\}
$$

where $$\vec{p}$$ is any particular solution, and where the system has $$k$$ free variables.

This description has two parts, the particular solution $$\vec{p}$$ and also the unrestricted linear combination of the $$\vec{\beta}$$'s. We shall prove the theorem in two corresponding parts, with two lemmas.

### Homogeneous Systems

We will focus first on the unrestricted combination part. To do that, we consider systems that have the vector of zeroes as one of the particular solutions, so that $$\vec{p}+c_1\vec{\beta}_1+\dots+c_k\vec{\beta}_k$$ can be shortened to $$c_1\vec{\beta}_1+\dots+c_k\vec{\beta}_k$$.

**Definition 3.2**  —

A linear equation is **homogeneous** if it has a constant of zero, that is, if it can be put in the form $$a_1x_1+a_2x_2+\,\cdots\,+a_nx_n=0$$.

(These are "homogeneous" because all of the terms involve the same power of their variable— the first power— including a "$$0x_{0}$$" that we can imagine is on the right side.)

**Example 3.3**  —

With any linear system like

$$
\begin{array}{rcrcr} 3x &+ &4y &= 3 \\ 2x &- &y &= 1 \end{array}
$$

we associate a system of homogeneous equations by setting the right side to zeros.

$$
\begin{array}{rcrcr} 3x &+ &4y &= 0 \\ 2x &- &y &= 0 \end{array}
$$

Our interest in the homogeneous system associated with a linear system can be understood by comparing the reduction of the system

$$
\begin{array}{rcl} \begin{array}{rcrcr} 3x &+ &4y &= 3 \\ 2x &- &y &= 1 \end{array} &\xrightarrow[]{-(2/3)\rho_1+\rho_2} &\begin{array}{rcrcr} 3x &+ &4y &= 3 \\ & &-(11/3)y &= -1 \end{array} \end{array}
$$

with the reduction of the associated homogeneous system.

$$
\begin{array}{rcl} \begin{array}{rcrcr} 3x &+ &4y &= 0 \\ 2x &- &y &= 0 \end{array} &\xrightarrow[]{-(2/3)\rho_1+\rho_2} &\begin{array}{rcrcr} 3x &+ &4y &= 0 \\ & &-(11/3)y &= 0 \end{array} \end{array}
$$

Obviously the two reductions go in the same way. We can study how linear systems are reduced by instead studying how the associated homogeneous systems are reduced.

Studying the associated homogeneous system has a great advantage over studying the original system. Nonhomogeneous systems can be inconsistent. But a homogeneous system must be consistent since there is always at least one solution, the vector of zeros.

**Definition 3.4**  —

A column or row vector of all zeros is a **zero vector**, denoted $$\vec{0}$$.

There are many different zero vectors, e.g., the one-tall zero vector, the two-tall zero vector, etc. Nonetheless, people often refer to "the" zero vector, expecting that the size of the one being discussed will be clear from the context.

**Example 3.5**  —

Some homogeneous systems have the zero vector as their only solution.

$$
\begin{array}{rcrcrcr} 3x &+ &2y &+ &z &= &0 \\ 6x &+ &4y & & &= &0 \\ & &y &+ &z &= &0 \end{array} \;\xrightarrow[]{-2\rho_1 +\rho_2}\; \begin{array}{rcrcrcr} 3x &+ &2y &+ &z &= &0 \\ & & & &-2z&= &0 \\ & &y &+ &z &= &0 \end{array} \;\xrightarrow[]{\rho_2 \leftrightarrow\rho_3}\; \begin{array}{rcrcrcr} 3x &+ &2y &+ &z &= &0 \\ & &y &+ &z &= &0 \\ & & & &-2z&= &0 \end{array}
$$

**Example 3.6**  —

Some homogeneous systems have many solutions. One example is the Chemistry problem from the first page of this book.

$$
\begin{array}{rcl} \begin{array}{rcrcrcrcr} 7x & & &- &7z & & &= &0 \\ 8x &+ &y &- &5z &- &2w &= &0 \\ & &y &- &3z & & &= &0 \\ & &3y &- &6z &- &w &= &0 \end{array} &\xrightarrow[]{-(8/7)\rho_1+\rho_2} &\begin{array}{rcrcrcrcr} 7x & & &- &7z & & &= &0 \\ & &y &+ &3z &- &2w &= &0 \\ & &y &- &3z & & &= &0 \\ & &3y &- &6z &- &w &= &0 \end{array} \\ &\xrightarrow[-3\rho_2+\rho_4]{-\rho_2+\rho_3} &\begin{array}{rcrcrcrcr} 7x & & &- &7z & & &= &0 \\ & &y &+ &3z &- &2w &= &0 \\ & & & &-6z &+ &2w &= &0 \\ & & & &-15z&+ &5w &= &0 \end{array} \\ &\xrightarrow[]{-(5/2)\rho_3+\rho_4} &\begin{array}{rcrcrcrcr} 7x & & &- &7z & & &= &0 \\ & &y &+ &3z &- &2w &= &0 \\ & & & &-6z &+ &2w &= &0 \\ & & & & & &0 &= &0 \end{array} \end{array}
$$

The solution set:

$$
\{\begin{pmatrix} 1/3 \\ 1 \\ 1/3 \\ 1 \end{pmatrix}w \,\big|\, w\in\mathbb{R}\}
$$

has many vectors besides the zero vector (if we interpret $$w$$ as a number of molecules then solutions make sense only when $$w$$ is a nonnegative multiple of $$3$$).

We now have the terminology to prove the two parts of Theorem 3.1. The first lemma deals with unrestricted combinations.

**Lemma 3.7**  —

For any homogeneous linear system there exist vectors $$\vec{\beta}_1$$, ..., $$\vec{\beta}_k$$ such that the solution set of the system is

$$
\{c_1\vec{\beta}_1+\cdots+c_k\vec{\beta}_k \,\big|\, c_1,\ldots,c_k\in\mathbb{R}\}
$$

where $$k$$ is the number of free variables in an echelon form version of the system.

Before the proof, we will recall the back substitution calculations that were done in the prior subsection.

Imagine that we have brought a system to this echelon form.

$$
\begin{array}{rcrcrcrcr} x &+ &2y &- &z &+ &2w &= &0 \\ & &-3y &+ &z & & &= &0 \\ & & & & & &-w &= &0 \end{array}
$$

We next perform back-substitution to express each variable in terms of the free variable $$z$$. Working from the bottom up, we get first that $$w$$ is $$0\cdot z$$, next that $$y$$ is $$(1/3)\cdot z$$, and then substituting those two into the top equation $$x+2((1/3)z)-z+2(0)=0$$ gives $$x=(1/3)\cdot z$$. So, back substitution gives a parametrization of the solution set by starting at the bottom equation and using the free variables as the parameters to work row-by-row to the top. The proof below follows this pattern.

*Comment:* That is, this proof just does a verification of the bookkeeping in back substitution to show that we haven't overlooked any obscure cases where this procedure fails, say, by leading to a division by zero. So this argument, while quite detailed, doesn't give us any new insights. Nevertheless, we have written it out for two reasons. The first reason is that we need the result— the computational procedure that we employ must be verified to work as promised. The second reason is that the row-by-row nature of back substitution leads to a proof that uses the technique of mathematical induction. This is an important, and non-obvious, proof technique that we shall use a number of times in this book. Doing an induction argument here gives us a chance to see one in a setting where the proof material is easy to follow, and so the technique can be studied. Readers who are unfamiliar with induction arguments should be sure to master this one and the ones later in this chapter before going on to the second chapter.

**Proof**  —

First use Gauss' method to reduce the homogeneous system to echelon form. We will show that each leading variable can be expressed in terms of free variables. That will finish the argument because then we can use those free variables as the parameters. That is, the $$\vec{\beta}$$'s are the vectors of coefficients of the free variables (as in Example 3.6, where the solution is $$x=(1/3)w$$, $$y=w$$, $$z=(1/3)w$$, and $$w=w$$).

We will proceed by mathematical induction, which has two steps. The base step of the argument will be to focus on the bottom-most non-"$$0=0$$" equation and write its leading variable in terms of the free variables. The inductive step of the argument will be to argue that if we can express the leading variables from the bottom $$t$$ rows in terms of free variables, then we can express the leading variable of the next row up— the $$t+1$$-th row up from the bottom— in terms of free variables. With those two steps, the theorem will be proved because by the base step it is true for the bottom equation, and by the inductive step the fact that it is true for the bottom equation shows that it is true for the next one up, and then another application of the inductive step implies it is true for third equation up, etc.

For the base step, consider the bottom-most non-"$$0=0$$" equation (the case where all the equations are "$$0=0$$" is trivial). We call that the $$m$$-th row:

$$
a_{m,\ell_m}x_{\ell_m}+a_{m,\ell_m+1}x_{\ell_m+1}+\cdots+a_{m,n}x_n=0
$$

where $$a_{m,\ell_m}\neq 0$$. (The notation here has "$$\ell$$" stand for "leading", so $$a_{m,\ell_m}$$ means "the coefficient, from the row $$m$$ of the variable leading row $$m$$".) Either there are variables in this equation other than the leading one $$x_{\ell_m}$$ or else there are not. If there are other variables $$x_{\ell_{m}+1}$$, etc., then they must be free variables because this is the bottom non-"$$0=0$$" row. Move them to the right and divide by $$a_{m,\ell_m}$$

$$
x_{\ell_m} =(-a_{m,\ell_m+1}/a_{m,\ell_m})x_{\ell_m+1}+\cdots+(-a_{m,n}/a_{m,\ell_m})x_n
$$

to express this leading variable in terms of free variables. If there are no free variables in this equation then $$x_{\ell_m}=0$$ (see the "tricky point" noted following this proof).

For the inductive step, we assume that for the $$m$$-th equation, and for the $$(m-1)$$-th equation, ..., and for the $$(m-t)$$-th equation, we can express the leading variable in terms of free variables (where $$0\leq t<m$$). To prove that the same is true for the next equation up, the $$(m-(t+1))$$-th equation, we take each variable that leads in a lower-down equation $$x_{\ell_m},\ldots,x_{\ell_{m-t}}$$ and substitute its expression in terms of free variables. The result has the form

$$
a_{m-(t+1),\ell_{m-(t+1)}}x_{\ell_{m-(t+1)}}+ \text{sums of multiples of free variables}=0
$$

where $$a_{m-(t+1),\ell_{m-(t+1)}}\neq 0$$. We move the free variables to the right-hand side and divide by $$a_{m-(t+1),\ell_{m-(t+1)}}$$, to end with $$x_{\ell_{m-(t+1)}}$$ expressed in terms of free variables.

Because we have shown both the base step and the inductive step, by the principle of mathematical induction the proposition is true.

We say that the set $$\{c_1\vec{\beta}_1+\cdots+c_k\vec{\beta}_k \,\big|\, c_1,\ldots,c_k\in\mathbb{R}\}$$ is **generated by** or **spanned by** the set of vectors $$\{{\vec{\beta}_1},\ldots,{\vec{\beta}_k}\}$$. There is a tricky point to this definition. If a homogeneous system has a unique solution, the zero vector, then we say the solution set is generated by the empty set of vectors. This fits with the pattern of the other solution sets: in the proof above the solution set is derived by taking the $$c$$'s to be the free variables and if there is a unique solution then there are no free variables.

This proof incidentally shows, as discussed after [Example 2.4](Linear%20Algebra%20-%20Describing%20the%20Solution%20Set.md), that solution sets can always be parametrized using the free variables.

### Nonhomogeneous Systems

The next lemma finishes the proof of Theorem 3.1 by considering the particular solution part of the solution set's description.

**Lemma 3.8**  —

For a linear system, where $$\vec{p}$$ is any particular solution, the solution set equals this set.

$$
\{\vec{p}+\vec{h} \,\big|\, \vec{h}\text{ satisfies the associated homogeneous system}\}
$$

**Proof**  —

We will show mutual set inclusion, that any solution to the system is in the above set and that anything in the set is a solution to the system.

For set inclusion the first way, that if a vector solves the system then it is in the set described above, assume that $$\vec{s}$$ solves the system. Then $$\vec{s}-\vec{p}$$ solves the associated homogeneous system since for each equation index $$i$$,

$$
\begin{align} a_{i,1}(s_1-p_1)+\cdots+a_{i,n}(s_n-p_n) &=(a_{i,1}s_1+\cdots+a_{i,n}s_n) \\ &\quad -(a_{i,1}p_1+\cdots+a_{i,n}p_n) \\ &=d_i-d_i \\ &=0 \end{align}
$$

where $$p_j$$ and $$s_j$$ are the $$j$$-th components of $$\vec{p}$$ and $$\vec{s}$$. We can write $$\vec{s}-\vec{p}$$ as $$\vec{h}$$, where $$\vec{h}$$ solves the associated homogeneous system, to express $$\vec{s}$$ in the required $$\vec{p}+\vec{h}$$ form.

For set inclusion the other way, take a vector of the form $$\vec{p}+\vec{h}$$, where $$\vec{p}$$ solves the system and $$\vec{h}$$ solves the associated homogeneous system, and note that it solves the given system: for any equation index $$i$$,

$$
\begin{align} a_{i,1}(p_1+h_1)+\cdots+a_{i,n}(p_n+h_n) &=(a_{i,1}p_1+\cdots+a_{i,n}p_n) \\ &\quad+(a_{i,1}h_1+\cdots+a_{i,n}h_n) \\ &=d_i+0 \\ &=d_i \end{align}
$$

where $$h_j$$ is the $$j$$-th component of $$\vec{h}$$.

The two lemmas above together establish Theorem 3.1. We remember that theorem with the slogan "$$\text{General} = \text{Particular} + \text{Homogeneous}$$".

**Example 3.9**  —

This system illustrates Theorem 3.1.

$$
\begin{array}{rcrcrcr} x &+ &2y &- &z &= &1 \\ 2x &+ &4y & & &= &2 \\ & &y &- &3z &= &0 \end{array}
$$

Gauss' method

$$
\xrightarrow[]{-2\rho_1+\rho_2}\; \begin{array}{rcrcrcr} x &+ &2y &- &z &= &1 \\ & & & &2z &= &0 \\ & &y &- &3z &= &0 \end{array} \;\xrightarrow[]{\rho_2\leftrightarrow\rho_3}\; \begin{array}{rcrcrcr} x &+ &2y &- &z &= &1 \\ & &y &- &3z &= &0 \\ & & & &2z &= &0 \end{array}
$$

shows that the general solution is a singleton set.

$$
\left\{\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \right\}
$$

That single vector is, of course, a particular solution. The associated homogeneous system reduces via the same row operations

$$
\begin{array}{rcl} \begin{array}{rcrcrcr} x &+ &2y &- &z &= &0 \\ 2x &+ &4y & & &= &0 \\ & &y &- &3z &= &0 \end{array} &\xrightarrow[]{-2\rho_1+\rho_2} \;\xrightarrow[]{\rho_2\leftrightarrow\rho_3} &\begin{array}{rcrcrcr} x &+ &2y &- &z &= &0 \\ & &y &- &3z &= &0 \\ & & & &2z &= &0 \end{array} \end{array}
$$

to also give a singleton set.

$$
\left\{\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \right\}
$$

As the theorem states, and as discussed at the start of this subsection, in this single-solution case the general solution results from taking the particular solution and adding to it the unique solution of the associated homogeneous system.

**Example 3.10**  —

Also discussed there is that the case where the general solution set is empty fits the "$$\text{General}=\text{Particular}+\text{Homogeneous}$$" pattern. This system illustrates Gauss' method

$$
\begin{array}{rcl} \begin{array}{rcrcrcrcr} x & & &+ &z &+ &w &= &-1 \\ 2x &- &y & & &+ &w &= &3 \\ x &+ &y &+ &3z &+ &2w &= &1 \end{array} &\xrightarrow[-\rho_1+\rho_3]{-2\rho_1+\rho_2} &\begin{array}{rcrcrcrcr} x & & &+ &z &+ &w &= &-1 \\ & &-y&- &2z &- &w &= &5 \\ & &y &+ &2z &+ &w &= &2 \end{array} \end{array}
$$

shows that it has no solutions. The associated homogeneous system, of course, has a solution.

$$
\begin{array}{rcl} \begin{array}{rcrcrcrcr} x & & &+ &z &+ &w &= &0 \\ 2x &- &y & & &+ &w &= &0 \\ x &+ &y &+ &3z &+ &2w &= &0 \end{array} &\xrightarrow[-\rho_1+\rho_3]{-2\rho_1+\rho_2} \;\xrightarrow[]{\rho_2+\rho_3} &\begin{array}{rcrcrcrcr} x & & &+ &z &+ &w &= &0 \\ & &-y&- &2z &- &w &= &0 \\ & & & & & &0 &= &0 \end{array} \end{array}
$$

In fact, the solution set of the homogeneous system is infinite.

$$
\bigg\{\begin{pmatrix} -1 \\ -2 \\ 1 \\ 0 \end{pmatrix}z+\begin{pmatrix} -1 \\ -1 \\ 0 \\ 1 \end{pmatrix}w \,\big|\, z,w\in\mathbb{R}\bigg\}
$$

However, because no particular solution of the original system exists, the general solution set is empty— there are no vectors of the form $$\vec{p}+\vec{h}$$ because there are no $$\vec{p}\,$$'s.

**Corollary 3.11**  —

Solution sets of linear systems are either empty, have one element, or have infinitely many elements.

**Proof**  —

We've seen examples of all three happening so we need only prove that those are the only possibilities.

First, notice a homogeneous system with at least one non-$$\vec{0}$$ solution $$\vec{v}$$ has infinitely many solutions because the set of multiples $$s\vec{v}$$ is infinite— if $$s\neq 1$$ then $$s\vec{v}-\vec{v}=(s-1)\vec{v}$$ is easily seen to be non-$$\vec{0}$$, and so $$s\vec{v}\neq \vec{v}$$.

Now, apply Lemma 3.8 to conclude that a solution set

$$
\{\vec{p}+\vec{h}\,\big|\,\vec{h} \text{ solves the associated homogeneous system}\}
$$

is either empty (if there is no particular solution $$\vec{p}$$), or has one element (if there is a $$\vec{p}$$ and the homogeneous system has the unique solution $$\vec{0}$$), or is infinite (if there is a $$\vec{p}$$ and the homogeneous system has a non-$$\vec{0}$$ solution, and thus by the prior paragraph has infinitely many solutions).

This table summarizes the factors affecting the size of a general solution.

- *number of solutions of the*  
*associated homogeneous system*
- *one*   *infinitely many*
- *particular*  
*solution*  
*exists?*   *yes*   unique  
solution   infinitely many  
solutions
- *no*   no  
solutions   no  
solutions

The factor on the top of the table is the simpler one. When we perform Gauss' method on a linear system, ignoring the constants on the right side and so paying attention only to the coefficients on the left-hand side, we either end with every variable leading some row or else we find that some variable does not lead a row, that is, that some variable is free. (Of course, "ignoring the constants on the right" is formalized by considering the associated homogeneous system. We are simply putting aside for the moment the possibility of a contradictory equation.)

A nice insight into the factor on the top of this table at work comes from considering the case of a system having the same number of equations as variables. This system will have a solution, and the solution will be unique, if and only if it reduces to an echelon form system where every variable leads its row, which will happen if and only if the associated homogeneous system has a unique solution. Thus, the question of uniqueness of solution is especially interesting when the system has the same number of equations as variables.

**Definition 3.12**  —

A square matrix is **nonsingular** if it is the matrix of coefficients of a homogeneous system with a unique solution. It is **singular** otherwise, that is, if it is the matrix of coefficients of a homogeneous system with infinitely many solutions.

**Example 3.13**  —

The systems from Example 3.3, Example 3.5, and Example 3.9 each have an associated homogeneous system with a unique solution. Thus these matrices are nonsingular.

$$
\begin{pmatrix} 3 &4 \\ 2 &-1 \end{pmatrix} \qquad \begin{pmatrix} 3 &2 &1 \\ 6 &-4 &0 \\ 0 &1 &1 \end{pmatrix} \qquad \begin{pmatrix} 1 &2 &-1 \\ 2 &4 &0 \\ 0 &1 &-3 \end{pmatrix}
$$

The Chemistry problem from Example 3.6 is a homogeneous system with more than one solution so its matrix is singular.

$$
\begin{pmatrix} 7 &0 &-7 &0 \\ 8 &1 &-5 &-2 \\ 0 &1 &-3 &0 \\ 0 &3 &-6 &-1 \end{pmatrix}
$$

**Example 3.14**  —

The first of these matrices is nonsingular while the second is singular

$$
\begin{pmatrix} 1 &2 \\ 3 &4 \end{pmatrix} \qquad \begin{pmatrix} 1 &2 \\ 3 &6 \end{pmatrix}
$$

because the first of these homogeneous systems has a unique solution while the second has infinitely many solutions.

$$
\begin{array}{rcrcr} x &+ &2y &= &0 \\ 3x &+ &4y &= &0 \end{array} \qquad \begin{array}{rcrcr} x &+ &2y &= &0 \\ 3x &+ &6y &= &0 \end{array}
$$

We have made the distinction in the definition because a system (with the same number of equations as variables) behaves in one of two ways, depending on whether its matrix of coefficients is nonsingular or singular. A system where the matrix of coefficients is nonsingular has a unique solution for any constants on the right side: for instance, Gauss' method shows that this system

$$
\begin{array}{rcrcr} x &+ &2y &= &a \\ 3x &+ &4y &= &b \end{array}
$$

has the unique solution $$x=b-2a$$ and $$y=(3a-b)/2$$. On the other hand, a system where the matrix of coefficients is singular never has a unique solution— it has either no solutions or else has infinitely many, as with these.

$$
\begin{array}{rcrcr} x &+ &2y &= &1 \\ 3x &+ &6y &= &2 \end{array} \qquad \begin{array}{rcrcr} x &+ &2y &= &1 \\ 3x &+ &6y &= &3 \end{array}
$$

Thus, "singular" can be thought of as connoting "troublesome", or at least "not ideal".

The above table has two factors. We have already considered the factor along the top: we can tell which column a given linear system goes in solely by considering the system's left-hand side— the constants on the right-hand side play no role in this factor. The table's other factor, determining whether a particular solution exists, is tougher. Consider these two

$$
\begin{array}{rcrcr} 3x &+ &2y &= &5 \\ 3x &+ &2y &= &5 \end{array} \qquad \begin{array}{rcrcr} 3x &+ &2y &= &5 \\ 3x &+ &2y &= &4 \end{array}
$$

with the same left sides but different right sides. Obviously, the first has a solution while the second does not, so here the constants on the right side decide if the system has a solution. We could conjecture that the left side of a linear system determines the number of solutions while the right side determines if solutions exist, but that guess is not correct. Compare these two systems

$$
\begin{array}{rcrcr} 3x &+ &2y &= &5 \\ 4x &+ &2y &= &4 \end{array} \qquad \begin{array}{rcrcr} 3x &+ &2y &= &5 \\ 3x &+ &2y &= &4 \end{array}
$$

with the same right sides but different left sides. The first has a solution but the second does not. Thus the constants on the right side of a system don't decide alone whether a solution exists; rather, it depends on some interaction between the left and right sides.

For some intuition about that interaction, consider this system with one of the coefficients left as the parameter $$c$$.

$$
\begin{array}{rcrcrcr} x &+ &2y &+ &3z &= &1 \\ x &+ &y &+ &z &= &1 \\ cx &+ &3y &+ &4z &= &0 \end{array}
$$

If $$c=2$$ this system has no solution because the left-hand side has the third row as a sum of the first two, while the right-hand does not. If $$c\neq 2$$ this system has a unique solution (try it with $$c=1$$). For a system to have a solution, if one row of the matrix of coefficients on the left is a linear combination of other rows, then on the right the constant from that row must be the same combination of constants from the same rows.

More intuition about the interaction comes from studying linear combinations. That will be our focus in the second chapter, after we finish the study of Gauss' method itself in the rest of this chapter.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Solve each system. Express the solution set using vectors. Identify the particular solution and the solution set of the homogeneous system.

1. $$\begin{array}{rcrcr} 3x &+ &6y &= &18 \\ x &+ &2y &= &6 \end{array}$$
2. $$\begin{array}{rcrcr} x &+ &y &= &1 \\ x &- &y &= &-1 \end{array}$$
3. $$\begin{array}{rcrcrcr} x_1 & & &+ &x_3 &= &4 \\ x_1 &- &x_2 &+ &2x_3 &= &5 \\ 4x_1 &- &x_2 &+ &5x_3 &= &17 \end{array}$$
4. $$\begin{array}{rcrcrcr} 2a &+ &b &- &c &= &2 \\ 2a & & &+ &c &= &3 \\ a &- &b & & &= &0 \end{array}$$
5. $$\begin{array}{rcrcrcrcr} x &+ &2y &- &z & & &= &3 \\ 2x &+ &y & & &+ &w &= &4 \\ x &- &y &+ &z &+ &w &= &1 \end{array}$$
6. $$\begin{array}{rcrcrcrcr} x & & &+ &z &+ &w &= &4 \\ 2x &+ &y & & &- &w &= &2 \\ 3x &+ &y &+ &z & & &= &7 \end{array}$$

**Problem 2**  —

Solve each system, giving the solution set in vector notation. Identify the particular solution and the solution of the homogeneous system.

1. $$\begin{array}{rcrcrcr} 2x &+ &y &- &z &= &1 \\ 4x &- &y & & &= &3 \end{array}$$
2. $$\begin{array}{rcrcrcrcr} x & & &- &z & & &= &1 \\ & &y &+ &2z &- &w &= &3 \\ x &+ &2y &+ &3z &- &w &= &7 \end{array}$$
3. $$\begin{array}{rcrcrcrcr} x &- &y &+ &z & & &= &0 \\ & &y & & &+ &w &= &0 \\ 3x &- &2y &+ &3z &+ &w &= &0 \\ & &-y & & &- &w &= &0 \end{array}$$
4. $$\begin{array}{rcrcrcrcrcr} a &+ &2b &+ &3c &+ &d &- &e &= &1 \\ 3a &- &b &+ &c &+ &d &+ &e &= &3 \end{array}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

For the system

$$
\begin{array}{rcrcrcrcr} 2x &- &y & & &- &w &= &3 \\ & &y &+ &z &+ &2w &= &2 \\ x &- &2y &- &z & & &= &-1 \end{array}
$$

which of these can be used as the particular solution part of some general solution?

1. $$\begin{pmatrix} 0 \\ -3 \\ 5 \\ 0 \end{pmatrix}$$
2. $$\begin{pmatrix} 2 \\ 1 \\ 1 \\ 0 \end{pmatrix}$$
3. $$\begin{pmatrix} -1 \\ -4 \\ 8 \\ -1 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 4**  —

Lemma 3.8 says that any particular solution may be used for $$\vec{p}$$. Find, if possible, a general solution to this system

$$
\begin{array}{rcrcrcrcr} x &- &y & & &+ &w &= &4 \\ 2x &+ &3y &- &z & & &= &0 \\ & &y &+ &z &+ &w &= &4 \end{array}
$$

that uses the given vector as its particular solution.

1. $$\begin{pmatrix} 0 \\ 0 \\ 0 \\ 4 \end{pmatrix}$$
2. $$\begin{pmatrix} -5 \\ 1 \\ -7 \\ 10 \end{pmatrix}$$
3. $$\begin{pmatrix} 2 \\ -1 \\ 1 \\ 1 \end{pmatrix}$$

**Problem 5**  —

One of these is nonsingular while the other is singular. Which is which?

1. $$\begin{pmatrix} 1 &3 \\ 4 &-12 \end{pmatrix}$$
2. $$\begin{pmatrix} 1 &3 \\ 4 &12 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 6**  —

Singular or nonsingular?

1. $$\begin{pmatrix} 1 &2 \\ 1 &3 \end{pmatrix}$$
2. $$\begin{pmatrix} 1 &2 \\ -3 &-6 \end{pmatrix}$$
3. $$\begin{pmatrix} 1 &2 &1 \\ 1 &3 &1 \end{pmatrix}$$ (Careful!)
4. $$\begin{pmatrix} 1 &2 &1 \\ 1 &1 &3 \\ 3 &4 &7 \end{pmatrix}$$
5. $$\begin{pmatrix} 2 &2 &1 \\ 1 &0 &5 \\ -1 &1 &4 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 7**  —

Is the given vector in the set generated by the given set?

1. $$\begin{pmatrix} 2 \\ 3 \end{pmatrix},$$ $$\left\{\begin{pmatrix} 1 \\ 4 \end{pmatrix}, \begin{pmatrix} 1 \\ 5 \end{pmatrix}\right\}$$
2. $$\begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix},$$ $$\left\{\begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}\right\}$$
3. $$\begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix},$$ $$\left\{\begin{pmatrix} 1 \\ 0 \\ 4 \end{pmatrix}, \begin{pmatrix} 2 \\ 1 \\ 5 \end{pmatrix}, \begin{pmatrix} 3 \\ 3 \\ 0 \end{pmatrix}, \begin{pmatrix} 4 \\ 2 \\ 1 \end{pmatrix}\right\}$$
4. $$\begin{pmatrix} 1 \\ 0 \\ 1 \\ 1 \end{pmatrix},$$ $$\left\{\begin{pmatrix} 2 \\ 1 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 3 \\ 0 \\ 0 \\ 2 \end{pmatrix}\right\}$$

**Problem 8**  —

Prove that any linear system with a nonsingular matrix of coefficients has a solution, and that the solution is unique.

**Problem 9**  —

To tell the whole truth, there is another tricky point to the proof of Lemma 3.7. What happens if there are no non-"$$0=0$$" equations? (There aren't any more tricky points after this one.)  
*This exercise is recommended for all readers.*

**Problem 10**  —

Prove that if $$\vec{s}$$ and $$\vec{t}$$ satisfy a homogeneous system then so do these vectors.

1. $$\vec{s}+\vec{t}$$
2. $$3\vec{s}$$
3. $$k\vec{s}+m\vec{t}$$ for $$k,m\in\mathbb{R}$$

What's wrong with: "These three show that if a homogeneous system has one solution then it has many solutions— any multiple of a solution is another solution, and any sum of solutions is a solution also— so there are no homogeneous systems with exactly one solution."?

**Problem 11**  —

Prove that if a system with only rational coefficients and constants has a solution then it has at least one all-rational solution. Must it have infinitely many?  
Solutions

### Footnotes

---

*Source: Wikibooks, Linear Algebra/General = Particular + Homogeneous (https://en.wikibooks.org/wiki/Linear_Algebra/General_%3D_Particular_%2B_Homogeneous), by Wikibooks contributors, CC BY-SA 4.0.*
