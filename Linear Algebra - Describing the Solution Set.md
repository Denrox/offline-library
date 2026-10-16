# Describing the Solution Set

A linear system with a unique solution has a solution set with one element. A linear system with no solution has a solution set that is empty. In these cases the solution set is easy to describe. Solution sets are a challenge to describe only when they contain many elements.

**Example 2.1**  —

This system has many solutions because in echelon form

$$
\begin{array}{rcl} \begin{array}{rcrcrcr} 2x & & &+ &z &= &3 \\ x &- &y &- &z &= &1 \\ 3x &- &y & & &= &4 \end{array} &\xrightarrow[-\left(\frac32\right)\rho_1+\rho_3]{-\left(\frac12\right)\rho_1+\rho_2} &\begin{array}{rcrcrcr} 2x & & &+ &z &= &3 \\ & &-y &- &\left(\frac32\right)z &= &-\frac12 \\ & &-y &- &\left(\frac32\right)z &= &-\frac12 \end{array} \\[3em] &\xrightarrow[]{-\rho_2+\rho_3} &\begin{array}{rcrcrcr} 2x & & &+ &z &= &3 \\ & &-y &- &\left(\frac32\right)z &= &-\frac12 \\ & & & &0 &= &0 \end{array} \end{array}
$$

not all of the variables are leading variables. The Gauss' method theorem showed that a triple satisfies the first system if and only if it satisfies the third. Thus, the solution set $$\Big\{(x,y,z)\Big|2x+z=3\text{ and }x-y-z=1\text{ and }3x-y=4\Big\}$$ can also be described as $$\left\{(x,y,z)\Big|2x+z=3\text{ and }-y-\frac{3z}{2}=-\frac12\right\}$$ . However, this second description is not much of an improvement. It has two equations instead of three, but it still involves some hard-to-understand interaction among the variables.

To get a description that is free of any such interaction, we take the variable that does not lead any equation, $$z$$ , and use it to describe the variables that do lead, $$x$$ and $$y$$ . The second equation gives $$y=\frac12-\frac32z$$ and the first equation gives $$x=\frac32-\frac12z$$ . Thus, the solution set can be described as $$\left\{(x,y,z)=\left(\frac32-\frac12z,\frac12-\frac32z,z\right)\Big|z\in\R\right\}$$ . For instance, $$\left(\frac12,-\frac52,2\right)$$ is a solution because taking $$z=2$$ gives a first component of $$\frac12$$ and a second component of $$-\frac52$$ .

The advantage of this description over the ones above is that the only variable appearing, $$z$$ , is unrestricted — it can be any real number.

**Definition 2.2**  —

The non-leading variables in an echelon-form linear system are **free variables**.

In the echelon form system derived in the above example, $$x$$ and $$y$$ are leading variables and $$z$$ is free.

**Example 2.3**  —

A linear system can end with more than one variable free. This row reduction

$$
\begin{array}{rcl} \begin{array}{rcrcrcrcr} x &+ &y &+ &z &- &w &= &1 \\ & &y &- &z &+ &w &= &-1 \\ 3x & & &+ &6z &- &6w &= &6 \\ & &-y &+ &z &- &w &= &1 \end{array} &\xrightarrow[]{-3\rho_1 +\rho_3} &\begin{array}{rcrcrcrcr} x &+ &y &+ &z &- &w &= &1 \\ & &y &- &z &+ &w &= &-1 \\ & &-3y &+ &3z &- &3w &= &3 \\ & &-y &+ &z &- &w &= &1 \end{array} \\[3em] &\xrightarrow[\rho_2+\rho_4]{3\rho_2+\rho_3} &\begin{array}{rcrcrcrcr} x &+ &y &+ &z &- &w &= &1 \\ & &y &- &z &+ &w &= &-1 \\ & & & & & &0 &= &0 \\ & & & & & &0 &= &0 \end{array} \end{array}
$$

ends with $$x$$ and $$y$$ leading, and with both $$z$$ and $$w$$ free. To get the description that we prefer we will start at the bottom. We first express $$y$$ in terms of the free variables $$z$$ and $$w$$ with $$y=-1+z-w$$ . Next, moving up to the top equation, substituting for $$y$$ in the first equation $$x+(-1+z-w)+z-w=1$$ and solving for $$x$$ yields $$x=2-2z+2w$$ . Thus, the solution set is $$\Big\{(2-2z+2w,-1+z-w,z,w)\Big|z,w\in\R\Big\}$$ .

We prefer this description because the only variables that appear, $$z$$ and $$w$$ , are unrestricted. This makes the job of deciding which four-tuples are system solutions into an easy one. For instance, taking $$z=1$$ and $$w=2$$ gives the solution $$(4,-2,1,2)$$ . In contrast, $$(3,-2,1,2)$$ is not a solution, since the first component of any solution must be $$2$$ minus twice the third component plus twice the fourth.

**Example 2.4**  —

After this reduction

$$
\begin{array}{rcl} \begin{array}{rcrcrcrcr} 2x &- &2y & & & & &= &0 \\ & & & &z &+ &3w &= &2 \\ 3x &- &3y & & & & &= &0 \\ x &- &y &+ &2z &+ &6w &= &4 \end{array} &\xrightarrow[-(\frac12)\rho_1+\rho_4]{-(\frac32)\rho_1+\rho_3} &\begin{array}{rcrcrcrcr} 2x &- &2y & & & & &= &0 \\ & & & &z &+ &3w &= &2 \\ & & & & & &0 &= &0 \\ & & & &2z &+ &6w &= &4 \end{array} \\[3em] &\xrightarrow[]{-2\rho_2+\rho_4} &\begin{array}{rcrcrcrcr} 2x &- &2y & & & & &= &0 \\ & & & &z &+ &3w &= &2 \\ & & & & & &0 &= &0 \\ & & & & & &0 &= &0 \end{array} \end{array}
$$

$$x,z$$ lead, $$y,w$$ are free. The solution set is $$\Big\{(y,y,2-3w,w)\Big|y,w\in\R\Big\}$$ . For instance, $$(1,1,2,0)$$ satisfies the system — take $$y=1$$ and $$w=0$$ . The four-tuple $$(1,0,5,4)$$ is not a solution since its first coordinate does not equal its second.

We refer to a variable used to describe a family of solutions as a **parameter** and we say that the set above is **parametrized** with $$y$$ and $$w$$ . (The terms "parameter" and "free variable" do not mean the same thing. Above, $$y$$ and $$w$$ are free because in the echelon form system they do not lead any row. They are parameters because they are used in the solution set description. We could have instead parametrized with $$y$$ and $$z$$ by rewriting the second equation as $$w=\frac23-\frac13z$$ . In that case, the free variables are still $$y$$ and $$w$$ , but the parameters are $$y$$ and $$z$$ . Notice that we could not have parametrized with $$x$$ and $$y$$ , so there is sometimes a restriction on the choice of parameters. The terms "parameter" and "free" are related because, as we shall show later in this chapter, the solution set of a system can always be parametrized with the free variables. Consequently, we shall parametrize all of our descriptions in this way.)

**Example 2.5**  —

This is another system with infinitely many solutions.

$$
\begin{array}{rcl} \begin{array}{rcrcrcrcr} x &+ &2y & & & & &= &1 \\ 2x & & &+ &z & & &= &2 \\ 3x &+ &2y &+ &z &- &w &= &4 \end{array} &\xrightarrow[-3\rho_1 +\rho_3]{-2\rho_1+\rho_2} &\begin{array}{rcrcrcrcr} x &+ &2y & & & & &= &1 \\ & &-4y &+ &z & & &= &0 \\ & &-4y &+ &z &- &w &= &1 \end{array} \\[3em] &\xrightarrow[]{-\rho_2+\rho_3} &\begin{array}{rcrcrcrcr} x &+ &2y & & & & &= &1 \\ & &-4y &+ &z & & &= &0 \\ & & & & & &-w &= &1 \end{array} \end{array}
$$

The leading variables are $$x,y,w$$ . The variable $$z$$ is free. (Notice here that, although there are infinitely many solutions, the value of one of the variables is fixed — $$w=-1$$ .) Write $$w$$ in terms of $$z$$ with $$w=-1+0z$$ . Then $$y=\frac14z$$ . To express $$x$$ in terms of $$z$$ , substitute for $$y$$ into the first equation to get $$x=1-\frac12z$$. The solution set is $$\left\{\left(1-\frac12z,\frac14z,z,-1\right)\Bigg|z\in\R\right\}$$ .

We finish this subsection by developing the notation for linear systems and their solution sets that we shall use in the rest of this book.

**Definition 2.6**  —

An $$m\times n$$ **matrix** is a rectangular array of numbers with $$m$$ **rows** and $$n$$ **columns**. Each number in the matrix is an **entry**.

Matrices are usually named by upper case roman letters, e.g. $$A$$ . Each entry is denoted by the corresponding lower-case letter, e.g. $$a_{i,j}$$ is the number in row $$i$$ and column $$j$$ of the array. For instance,

$$
A=\begin{pmatrix}1&2.2&5\\3&4&-7\end{pmatrix}
$$

has two rows and three columns, and so is a $$2\times3$$ matrix. (Read that "two-by-three"; the number of rows is always stated first.) The entry in the second row and first column is $$a_{2,1}=3$$ . Note that the order of the subscripts matters: $$a_{1,2}\ne a_{2,1}$$ since $$a_{1,2}=2.2$$ . (The parentheses around the array are a typographic device so that when two matrices are side by side we can tell where one ends and the other starts.)

Matrices occur throughout this book. We shall use $$\mathcal{M}_{n\times m}$$ to denote the collection of $$n\times m$$ matrices.

**Example 2.7**  —

We can abbreviate this linear system

$$
\begin{array}{rcrcrcr} x &+ &2y & & &= &4 \\ & &y &- &z &= &0 \\ x & & &+ &2z&= &4 \end{array}
$$

with this matrix.

$$
\left(\begin{array}{ccc|c} 1 &2 &0 &4 \\ 0 &1 &-1 &0 \\ 1 &0 &2 &4 \end{array}\right)
$$

The vertical bar just reminds a reader of the difference between the coefficients on the systems's left hand side and the constants on the right. When a bar is used to divide a matrix into parts, we call it an **augmented** matrix. In this notation, Gauss' method goes this way.

$$
\left(\begin{array}{ccc|c} 1 &2 &0 &4 \\ 0 &1 &-1 &0 \\ 1 &0 &2 &4 \end{array}\right) \xrightarrow[]{-\rho_1 +\rho_3} \left(\begin{array}{ccc|c} 1 &2 &0 &4 \\ 0 &1 &-1 &0 \\ 0 &-2 &2 &0 \end{array}\right) \xrightarrow[]{2\rho_2 +\rho_3} \left(\begin{array}{ccc|c} 1 &2 &0 &4 \\ 0 &1 &-1 &0 \\ 0 &0 &0 &0 \end{array}\right)
$$

The second row stands for $$y-z=0$$ and the first row stands for $$x+2y=4$$ so the solution set is $$\Big\{(4-2z,z,z)\Big|z\in\R\Big\}$$ . One advantage of the new notation is that the clerical load of Gauss' method — the copying of variables, the writing of $$+$$'s and $$=$$'s, etc. — is lighter.

We will also use the array notation to clarify the descriptions of solution sets. A description like $$\{(2-2z+2w,-1+z-w,z,w)\big|z,w\in\R\}$$ from Example 2.3 is hard to read. We will rewrite it to group all the constants together, all the coefficients of $$z$$ together, and all the coefficients of $$w$$ together. We will write them vertically, in one-column wide matrices.

$$
\left\{\begin{pmatrix}2\\-1\\0\\0\end{pmatrix}+\begin{pmatrix}-2\\1\\1\\0\end{pmatrix}z+\begin{pmatrix}2\\-1\\0\\1\end{pmatrix}w\Bigg|z,w\in\R\right\}
$$

For instance, the top line says that $$x=2-2z+2w$$ . The next section gives a geometric interpretation that will help us picture the solution sets when they are written in this way.

**Definition 2.8**  —

A **vector** (or **column vector**) is a matrix with a single column. A matrix with a single row is a **row vector**. The entries of a vector are its **components**.

Vectors are an exception to the convention of representing matrices with capital roman letters. We use lower-case roman or greek letters overlined with an arrow: $$\vec a,\vec b$$ ... or $$\vec{\alpha},\vec{\beta}$$ ... (boldface is also common: $$\mathbf{a}$$ or $$\boldsymbol{\alpha}$$). For instance, this is a column vector with a third component of $$7$$ .

$$
\vec v=\begin{pmatrix}1\\3\\7\end{pmatrix}
$$

**Definition 2.9**  —

The linear equation $$a_1x_1+\cdots+a_nx_n=d$$ with unknowns $$x_1,\ldots\,,x_n$$ is **satisfied** by

$$
\vec s=\begin{pmatrix}s_1\\ \vdots\\s_n\end{pmatrix}
$$

if $$a_1s_1+\cdots+a_ns_n=d$$ . A vector satisfies a linear system if it satisfies each equation in the system.

The style of description of solution sets that we use involves adding the vectors, and also multiplying them by real numbers, such as the $$z$$ and $$w$$ . We need to define these operations.

**Definition 2.10**  —

The **vector sum** of $$\vec u$$ and $$\vec v$$ is this.

$$
\vec u+\vec v=\begin{pmatrix}u_1\\ \vdots\\u_n\end{pmatrix}+\begin{pmatrix}v_1\\ \vdots\\v_n\end{pmatrix}=\begin{pmatrix}u_1+v_1\\ \vdots\\u_n+v_n\end{pmatrix}
$$

In general, two matrices with the same number of rows and the same number of columns add in this way, entry-by-entry.

**Definition 2.11**  —

The **scalar multiplication** of the real number $$r$$ and the vector $$\vec v$$ is this.

$$
r\cdot\vec v=r\cdot\begin{pmatrix}v_1\\ \vdots\\v_n\end{pmatrix}=\begin{pmatrix}rv_1\\ \vdots\\rv_n\end{pmatrix}
$$

In general, any matrix is multiplied by a real number in this entry-by-entry way.

Scalar multiplication can be written in either order: $$r\cdot\vec v$$ or $$\vec v\cdot r$$ , or without the "$$\cdot$$" symbol: $$r\vec v$$ . (Do not refer to scalar multiplication as "scalar product" because that name is used for a different operation.)

**Example 2.12**  —

$$
\begin{pmatrix}2\\3\\1\end{pmatrix}+\begin{pmatrix}3\\-1\\4\end{pmatrix}=\begin{pmatrix}2+3\\3-1\\1+4\end{pmatrix}=\begin{pmatrix}5\\2\\5\end{pmatrix} \qquad 7\cdot\begin{pmatrix}1\\4\\-1\\-3\end{pmatrix}=\begin{pmatrix}7\\28\\-7\\-21\end{pmatrix}
$$

Notice that the definitions of vector addition and scalar multiplication agree where they overlap, for instance, $$\vec v+\vec v=2\vec v$$ .

With the notation defined, we can now solve systems in the way that we will use throughout this book.

**Example 2.13**  —

This system

$$
\begin{array}{rcrcrcrcrcr} 2x &+ &y & & &- &w & & &= &4 \\ & &y & & &+ &w &+ &u &= &4 \\ x & & &- &z &+ &2w & & &= &0 \end{array}
$$

reduces in this way.

$$
\begin{array}{rcl} \left(\begin{array}{ccccc|c} 2 &1 &0 &-1 &0 &4 \\ 0 &1 &0 &1 &1 &4 \\ 1 &0 &-1 &2 &0 &0 \end{array}\right) &\xrightarrow[]{-\left(\frac12\right)\rho_1+\rho_3} &\left(\begin{array}{ccccc|c} 2 &1 &0 &-1 &0 &4 \\ 0 &1 &0 &1 &1 &4 \\ 0 &-\frac12 &-1 &\frac52 &0 &-2 \end{array}\right) \\[3em] &\xrightarrow[]{\left(\frac12\right)\rho_2+\rho_3} &\left(\begin{array}{ccccc|c} 2 &1 &0 &-1 &0 &4 \\ 0 &1 &0 &1 &1 &4 \\ 0 &0 &-1 &3 &\frac12 &0 \end{array}\right) \end{array}
$$

The solution set is $$\left\{(w+\frac12u,4-w-u,3w+\frac12u,w,u)\Bigg|w,u\in\R\right\}$$ . We write that in vector form.

$$
\left\{\begin{pmatrix} x \\ y \\ z \\ w \\ u \end{pmatrix}= \begin{pmatrix} 0 \\ 4 \\ 0 \\ 0 \\ 0 \end{pmatrix}+ \begin{pmatrix} 1 \\ -1 \\ 3 \\ 1 \\ 0 \end{pmatrix}w+ \begin{pmatrix} \frac12 \\ -1 \\ \frac12 \\ 0 \\ 1 \end{pmatrix}u \Bigg|w,u\in\R\right\}
$$

Note again how well vector notation sets off the coefficients of each parameter. For instance, the third row of the vector form shows plainly that if $$u$$ is held fixed then $$z$$ increases three times as fast as $$w$$ .

That format also shows plainly that there are infinitely many solutions. For example, we can fix $$u$$ as $$0$$ , let $$w$$ range over the real numbers, and consider the first component $$x$$ . We get infinitely many first components and hence infinitely many solutions.

Another thing shown plainly is that setting both $$w,u$$ to 0 gives that this

$$
\begin{pmatrix}x\\y\\z\\w\\u\end{pmatrix}=\begin{pmatrix}0\\4\\0\\0\\0\end{pmatrix}
$$

is a particular solution of the linear system.

**Example 2.14**  —

In the same way, this system

$$
\begin{array}{rcrcrcr} x &- &y &+ &z &= &1 \\ 3x & & &+ &z &= &3 \\ 5x &- &2y &+ &3z &= &5 \end{array}
$$

reduces

$$
\left(\begin{array}{ccc|c} 1 &-1 &1 &1 \\ 3 &0 &1 &3 \\ 5 &-2 &3 &5 \end{array}\right) \xrightarrow[-5\rho_1+\rho_3]{-3\rho_1+\rho_2} \left(\begin{array}{ccc|c} 1 &-1 &1 &1 \\ 0 &3 &-2 &0 \\ 0 &3 &-2 &0 \end{array}\right) \xrightarrow[]{-\rho_2+\rho_3} \left(\begin{array}{ccc|c} 1 &-1 &1 &1 \\ 0 &3 &-2 &0 \\ 0 &0 &0 &0 \end{array}\right)
$$

to a one-parameter solution set.

$$
\left\{\begin{pmatrix}1\\0\\0\end{pmatrix}+\begin{pmatrix}-\frac13\\ \frac23\\1\end{pmatrix}z\Bigg|z\in\R\right\}
$$

Before the exercises, we pause to point out some things that we have yet to do.

The first two subsections have been on the mechanics of Gauss' method. Except for one result, [Theorem 1.4](Linear%20Algebra%20-%20Gauss%27%20Method.md)— without which developing the method doesn't make sense since it says that the method gives the right answers— we have not stopped to consider any of the interesting questions that arise.

For example, can we always describe solution sets as above, with a particular solution vector added to an unrestricted linear combination of some other vectors? The solution sets we described with unrestricted parameters were easily seen to have infinitely many solutions so an answer to this question could tell us something about the size of solution sets. An answer to that question could also help us picture the solution sets, in $$\mathbb{R}^2$$, or in $$\mathbb{R}^3$$, etc.

Many questions arise from the observation that Gauss' method can be done in more than one way (for instance, when swapping rows, we may have a choice of which row to swap with). [Theorem 1.4](Linear%20Algebra%20-%20Gauss%27%20Method.md) says that we must get the same solution set no matter how we proceed, but if we do Gauss' method in two different ways must we get the same number of free variables both times, so that any two solution set descriptions have the same number of parameters? Must those be the same variables (e.g., is it impossible to solve a problem one way and get $$y$$ and $$w$$ free or solve it another way and get $$y$$ and $$z$$ free)?

In the rest of this chapter we answer these questions. The answer to each is "yes". The first question is answered in the last subsection of this section. In the second section we give a geometric description of solution sets. In the final section of this chapter we tackle the last set of questions. Consequently, by the end of the first chapter we will not only have a solid grounding in the practice of Gauss' method, we will also have a solid grounding in the theory. We will be sure of what can and cannot happen in a reduction.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Find the indicated entry of the matrix, if it is defined.

$$
A=\begin{pmatrix} 1 &3 &1 \\ 2 &-1 &4 \end{pmatrix}
$$

1. $$a_{2,1}$$
2. $$a_{1,2}$$
3. $$a_{2,2}$$
4. $$a_{3,1}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Give the size of each matrix.

1. $$\begin{pmatrix} 1 &0 &4 \\ 2 &1 &5 \end{pmatrix}$$
2. $$\begin{pmatrix} 1 &1 \\ -1 &1 \\ 3 &-1 \end{pmatrix}$$
3. $$\begin{pmatrix} 5 &10 \\ 10 &5 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

Do the indicated vector operation, if it is defined.

1. $$\begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix} +\begin{pmatrix} 3 \\ 0 \\ 4 \end{pmatrix}$$
2. $$5\begin{pmatrix} 4 \\ -1 \end{pmatrix}$$
3. $$\begin{pmatrix} 1 \\ 5 \\ 1 \end{pmatrix} -\begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix}$$
4. $$7\begin{pmatrix} 2 \\ 1 \end{pmatrix} +9\begin{pmatrix} 3 \\ 5 \end{pmatrix}$$
5. $$\begin{pmatrix} 1 \\ 2 \end{pmatrix} +\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$$
6. $$6\begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix} -4\begin{pmatrix} 2 \\ 0 \\ 3 \end{pmatrix} +2\begin{pmatrix} 1 \\ 1 \\ 5 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 4**  —

Solve each system using matrix notation. Express the solution using vectors.

1. $$\begin{array}{rcrcr} 3x &+ &6y &= &18 \\ x &+ &2y &= &6 \end{array}$$
2. $$\begin{array}{rcrcr} x &+ &y &= &1 \\ x &- &y &= &-1 \end{array}$$
3. $$\begin{array}{rcrcrcr} x_1 & & &+ &x_3 &= &4 \\ x_1 &- &x_2 &+ &2x_3 &= &5 \\ 4x_1 &- &x_2 &+ &5x_3 &= &17 \end{array}$$
4. $$\begin{array}{rcrcrcr} 2a &+ &b &- &c &= &2 \\ 2a & & &+ &c &= &3 \\ a &- &b & & &= &0 \end{array}$$
5. $$\begin{array}{rcrcrcrcr} x &+ &2y &- &z & & &= &3 \\ 2x &+ &y & & &+ &w &= &4 \\ x &- &y &+ &z &+ &w &= &1 \end{array}$$
6. $$\begin{array}{rcrcrcrcr} x & & &+ &z &+ &w &= &4 \\ 2x &+ &y & & &- &w &= &2 \\ 3x &+ &y &+ &z & & &= &7 \end{array}$$  
*This exercise is recommended for all readers.*

**Problem 5**  —

Solve each system using matrix notation. Give each solution set in vector notation.

1. $$\begin{array}{rcrcrcr} 2x &+ &y &- &z &= &1 \\ 4x &- &y & & &= &3 \end{array}$$
2. $$\begin{array}{rcrcrcrcr} x & & &- &z & & &= &1 \\ & &y &+ &2z &- &w &= &3 \\ x &+ &2y &+ &3z &- &w &= &7 \end{array}$$
3. $$\begin{array}{rcrcrcrcr} x &- &y &+ &z & & &= &0 \\ & &y & & &+ &w &= &0 \\ 3x &- &2y &+ &3z &+ &w &= &0 \\ & &-y & & &- &w &= &0 \end{array}$$
4. $$\begin{array}{rcrcrcrcrcr} a &+ &2b &+ &3c &+ &d &- &e &= &1 \\ 3a &- &b &+ &c &+ &d &+ &e &= &3 \end{array}$$  
*This exercise is recommended for all readers.*

**Problem 6**  —

The vector is in the set. What value of the parameters produces that vector?

1. $$\begin{pmatrix} 5 \\ -5 \end{pmatrix}$$, $$\{\begin{pmatrix} 1 \\ -1 \end{pmatrix}k\,\big|\, k\in\mathbb{R}\}$$
2. $$\begin{pmatrix} -1 \\ 2 \\ 1 \end{pmatrix}$$, $$\{\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}i +\begin{pmatrix} 3 \\ 0 \\ 1 \end{pmatrix}j\,\big|\, i,j\in\mathbb{R}\}$$
3. $$\begin{pmatrix} 0 \\ -4 \\ 2 \end{pmatrix}$$, $$\{\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}m +\begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}n\,\big|\, m,n\in\mathbb{R}\}$$

**Problem 7**  —

Decide if the vector is in the set.

1. $$\begin{pmatrix} 3 \\ -1 \end{pmatrix}$$, $$\{\begin{pmatrix} -6 \\ 2 \end{pmatrix}k\,\big|\, k\in\mathbb{R}\}$$
2. $$\begin{pmatrix} 5 \\ 4 \end{pmatrix}$$, $$\{\begin{pmatrix} 5 \\ -4 \end{pmatrix}j\,\big|\, j\in\mathbb{R}\}$$
3. $$\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$$, $$\{\begin{pmatrix} 0 \\ 3 \\ -7 \end{pmatrix}+\begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}r\,\big|\, r\in\mathbb{R}\}$$
4. $$\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$$, $$\{\begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}j +\begin{pmatrix} -3 \\ -1 \\ 1 \end{pmatrix}k\,\big|\, j,k\in\mathbb{R}\}$$

**Problem 8**  —

Parametrize the solution set of this one-equation system.

$$
x_1+x_2+\cdots+x_n=0
$$

*This exercise is recommended for all readers.*

**Problem 9**  —

1. Apply Gauss' method to the left-hand side to solve

$$
\begin{array}{rcrcrcrcr} x &+ &2y & & &- &w &= &a \\ 2x & & &+ &z & & &= &b \\ x &+ &y & & &+ &2w &= &c \end{array}
$$

for $$x$$, $$y$$, $$z$$, and $$w$$, in terms of the constants $$a$$, $$b$$, and $$c$$. Note that $$w$$ will be a free variable.
2. Use your answer from the prior part to solve this.

$$
\begin{array}{rcrcrcrcr} x &+ &2y & & &- &w &= &3 \\ 2x & & &+ &z & & &= &1 \\ x &+ &y & & &+ &2w &= &-2 \end{array}
$$

*This exercise is recommended for all readers.*

**Problem 10**  —

Why is the comma needed in the notation "$$a_{i,j}$$" for matrix entries?  
*This exercise is recommended for all readers.*

**Problem 11**  —

Give the $$4 \! \times \! 4$$ matrix whose $$i,j$$-th entry is

1. $$i+j$$;
2. $$-1$$ to the $$i+j$$ power.

**Problem 12**  —

For any matrix $$A$$, the **transpose** of $$A$$, written $${{A}^{\rm trans}}$$, is the matrix whose columns are the rows of $$A$$. Find the transpose of each of these.

1. $$\begin{pmatrix} 1 &2 &3 \\ 4 &5 &6 \end{pmatrix}$$
2. $$\begin{pmatrix} 2 &-3 \\ 1 &1 \end{pmatrix}$$
3. $$\begin{pmatrix} 5 &10 \\ 10 &5 \end{pmatrix}$$
4. $$\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 13**  —

1. Describe all functions $$f(x)=ax^2+bx+c$$ such that $$f(1)=2$$ and $$f(-1)=6$$.
2. Describe all functions $$f(x)=ax^2+bx+c$$ such that $$f(1)=2$$.

**Problem 14**  —

Show that any set of five points from the plane $$\mathbb{R}^2$$ lie on a common conic section, that is, they all satisfy some equation of the form $$ax^2+by^2+cxy+dx+ey+f=0$$ where some of $$a,\,\ldots\,,f$$ are nonzero.

**Problem 15**  —

Make up a four equations/four unknowns system having

1. a one-parameter solution set;
2. a two-parameter solution set;
3. a three-parameter solution set.

**? Problem 16**  —

1. Solve the system of equations.

$$
\begin{array}{rcrcr} ax &+ &y &= &a^2 \\ x &+ &ay &= &1 \end{array}
$$

For what values of $$a$$ does the system fail to have solutions, and for what values of $$a$$ are there infinitely many solutions?
2. Answer the above question for the system.

$$
\begin{array}{rcrcr} ax &+ &y &= &a^3 \\ x &+ &ay &= &1 \end{array}
$$

*(USSR Olympiad #174)*

**? Problem 17**  —

In air a gold-surfaced sphere weighs $$7588$$ grams. It is known that it may contain one or more of the metals aluminum, copper, silver, or lead. When weighed successively under standard conditions in water, benzene, alcohol, and glycerine its respective weights are $$6588$$, $$6688$$, $$6778$$, and $$6328$$ grams. How much, if any, of the forenamed metals does it contain if the specific gravities of the designated substances are taken to be as follows?

- Aluminum   2.7      Alcohol  0.81
- Copper   8.9      Benzene  0.90
- Gold   19.3      Glycerine   1.26
- Lead   11.3      Water  1.00
- Silver   10.8

(Duncan & Quelch 1952)

Solutions

### References

- *The USSR Mathematics Olympiad*, number 174.
- Duncan, Dewey (proposer); Quelch, W. H. (solver) (1952), *Mathematics Magazine*, **26** (1): 48 {{citation}}: Missing or empty |title= (help); Unknown parameter |month= ignored (help)

---

*Source: Wikibooks, Linear Algebra/Describing the Solution Set (https://en.wikibooks.org/wiki/Linear_Algebra/Describing_the_Solution_Set), by Wikibooks contributors, CC BY-SA 4.0.*
