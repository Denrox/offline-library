# Gauss' Method

**Definition 1.1**  —

A **linear equation** in variables $$x_1,x_2,\ldots,x_n$$ has the form

$$
a_1x_1+a_2x_2+a_3x_3+\cdots+a_nx_n=d
$$

where the numbers $$a_1,\dots,a_n\in\R$$ are the equation's **coefficients** and $$d\in\R$$ is the **constant**. An $$n$$-tuple $$(s_1,s_2,\dots,s_n)\in\R^n$$ is a **solution** of, or **satisfies**, that equation if substituting the numbers $$s_1,\dots,s_n$$ for the variables gives a true statement: $$a_1s_1+a_2s_2+\ldots+a_ns_n=d$$.

A **system of linear equations**

$$
\begin{array}{rcrcrcrcr} a_{1,1}x_1 &+ &a_{1,2}x_2 &+ &\cdots &+ &a_{1,n}x_n &= &d_1 \\ a_{2,1}x_1 &+ &a_{2,2}x_2 &+ &\cdots &+ &a_{2,n}x_n &= &d_2 \\ & & & & & & &\vdots \\ a_{m,1}x_1 &+ &a_{m,2}x_2 &+ &\cdots &+ &a_{m,n}x_n &= &d_m \end{array}
$$

has the solution $$(s_1,s_2,\ldots,s_n)$$ if that $$n$$-tuple is a solution of all of the equations in the system.

**Example 1.2**  —

The ordered pair $$(-1,5)$$ is a solution of this system.

$$
\begin{array}{rcrcr} 4x_1 &+ &2x_2 &= &6 \\ -x_1 &+ &x_2 &= &6 \end{array}
$$

In contrast, $$(5,-1)$$ is not a solution.

Finding the set of all solutions is **solving** the system. No guesswork or good fortune is needed to solve a linear system. There is an algorithm that always works. The next example introduces that algorithm, called **Gauss' method**. It transforms the system, step by step, into one with a form that is easily solved.

**Example 1.3**  —

To solve this system

$$
\begin{array}{rcrcrcr} & & & &3x_3 &= &9 \\ x_1 &+ &5x_2 &- &2x_3 &= &2 \\ \frac{1}{3}x_1 &+ &2x_2 & & &= &3 \end{array}
$$

we repeatedly transform it until it is in a form that is easy to solve.

$$
\begin{array}{rcl} \quad &\xrightarrow[]{ \text{swap row 1 with row 3} } &\begin{array}{rcrcrcr} \frac{1}{3}x_1 &+ &2x_2 & & &= &3 \\ x_1 &+ &5x_2 &- &2x_3 &= &2 \\ & & & &3x_3 &= &9 \end{array} \\ &\xrightarrow[]{ \text{multiply row 1 by 3} } &\begin{array}{rcrcrcr} x_1 &+ &6x_2 & & &= &9 \\ x_1 &+ &5x_2 &- &2x_3 &= &2 \\ & & & &3x_3 &= &9 \end{array} \\ &\xrightarrow[]{ \text{add }-1\text{ times row 1 to row 2} } &\begin{array}{rcrcrcr} x_1 &+ &6x_2 & & &= &9 \\ & &-x_2 &- &2x_3 &= &-7 \\ & & & &3x_3 &= &9 \end{array} \end{array}
$$

The third step is the only nontrivial one. We've mentally multiplied both sides of the first row by $$-1$$, mentally added that to the old second row, and written the result in as the new second row.

Now we can find the value of each variable. The bottom equation shows that $$x_3=3$$. Substituting $$3$$ for $$x_3$$ in the middle equation shows that $$x_2=1$$. Substituting those two into the top equation gives that $$x_1=3$$ and so the system has a unique solution: the solution set is $$\{\,(3,1,3)\,\}$$.

Most of this subsection and the next one consists of examples of solving linear systems by Gauss' method. We will use it throughout this book. It is fast and easy. But, before we get to those examples, we will first show that this method is also safe in that it never loses solutions or picks up extraneous solutions.

**Theorem 1.4 (Gauss' method)**  —

If a linear system is changed to another by one of these operations

1. an equation is swapped with another
2. an equation has both sides multiplied by a nonzero constant
3. an equation is replaced by the sum of itself and a multiple of another

then the two systems have the same set of solutions.

Each of those three operations has a restriction. Multiplying a row by $$0$$ is not allowed because obviously that can change the solution set of the system. Similarly, adding a multiple of a row to itself is not allowed because adding $$-1$$ times the row to itself has the effect of multiplying the row by $$0$$. Finally, swapping a row with itself is disallowed to make some results in the fourth chapter easier to state and remember (and besides, self-swapping doesn't accomplish anything).

**Proof**  —

We will cover the equation swap operation here and save the other two cases for Problem 14.

Consider this swap of row $$i$$ with row $$j$$.

$$
\begin{array}{rcrcrcrcr} a_{1,1}x_1 &+ &a_{1,2}x_2 &+ &\cdots &&a_{1,n}x_n &= &d_1 \\ & & & & & & &\vdots \\ a_{i,1}x_1 &+ &a_{i,2}x_2 &+ &\cdots &&a_{i,n}x_n &= &d_i \\ & & & & & & &\vdots \\ a_{j,1}x_1 &+ &a_{j,2}x_2 &+ &\cdots &&a_{j,n}x_n &= &d_j \\ & & & & & & &\vdots \\ a_{m,1}x_1 &+ &a_{m,2}x_2 &+ &\cdots &&a_{m,n}x_n &= &d_m \end{array} \xrightarrow[]{} \begin{array}{rcrcrcrcr} a_{1,1}x_1 &+ &a_{1,2}x_2 &+ &\cdots &&a_{1,n}x_n &= &d_1 \\ & & & & & & &\vdots \\ a_{j,1}x_1 &+ &a_{j,2}x_2 &+ &\cdots &&a_{j,n}x_n &= &d_j \\ & & & & & & &\vdots \\ a_{i,1}x_1 &+ &a_{i,2}x_2 &+ &\cdots &&a_{i,n}x_n &= &d_i \\ & & & & & & &\vdots \\ a_{m,1}x_1 &+ &a_{m,2}x_2 &+ &\cdots &&a_{m,n}x_n &= &d_m \end{array}
$$

The $$n$$-tuple $$(s_1,\ldots,s_n)$$ satisfies the system before the swap if and only if substituting the values, the $$s$$'s, for the variables, the $$x$$'s, gives true statements: $$a_{1,1}s_1+a_{1,2}s_2+\cdots+a_{1,n}s_n=d_1$$ and ... $$a_{i,1}s_1+a_{i,2}s_2+\cdots+a_{i,n}s_n=d_i$$ and ... $$a_{j,1}s_1+a_{j,2}s_2+\cdots+a_{j,n}s_n=d_j$$ and ... $$a_{m,1}s_1+a_{m,2}s_2+\cdots+a_{m,n}s_n=d_m$$.

In a requirement consisting of statements and-ed together we can rearrange the order of the statements, so that this requirement is met if and only if $$a_{1,1}s_1+a_{1,2}s_2+\cdots+a_{1,n}s_n=d_1$$ and ... $$a_{j,1}s_1+a_{j,2}s_2+\cdots+a_{j,n}s_n=d_j$$ and ... $$a_{i,1}s_1+a_{i,2}s_2+\cdots+a_{i,n}s_n=d_i$$ and ... $$a_{m,1}s_1+a_{m,2}s_2+\cdots+a_{m,n}s_n=d_m$$. This is exactly the requirement that $$(s_1,\ldots,s_n)$$ solves the system after the row swap.

**Definition 1.5**  —

The three operations from Theorem 1.4 are the **elementary reduction operations**, or **row operations**, or **Gaussian operations**. They are **swapping**, **multiplying by a scalar** or **rescaling**, and **pivoting**.

When writing out the calculations, we will abbreviate "row $$i$$" by "$$\rho_i$$". For instance, we will denote a pivot operation by $$k\rho_i+\rho_j$$, with the row that is changed written second. We will also, to save writing, often list pivot steps together when they use the same $$\rho_i$$.

**Example 1.6**  —

A typical use of Gauss' method is to solve this system.

$$
\begin{array}{rcrcrcr} x &+ &y & & &= &0 \\ 2x &- &y &+ &3z &= &3 \\ x &- &2y &- &z &= &3 \end{array}
$$

The first transformation of the system involves using the first row to eliminate the $$x$$ in the second row and the $$x$$ in the third. To get rid of the second row's $$2x$$, we multiply the entire first row by $$-2$$, add that to the second row, and write the result in as the new second row. To get rid of the third row's $$x$$, we multiply the first row by $$-1$$, add that to the third row, and write the result in as the new third row.

$$
\begin{array}{rcl} &\xrightarrow[-\rho_1+\rho_3]{-2\rho_1+\rho_2} &\begin{array}{rcrcrcr} x &+ &y & & &= &0 \\ & &-3y&+ &3z &= &3 \\ & &-3y&- &z &= &3 \end{array} \end{array}
$$

(Note that the two $$\rho_1$$ steps $$-2\rho_1+\rho_2$$ and $$-\rho_1+\rho_3$$ are written as one operation.) In this second system, the last two equations involve only two unknowns. To finish we transform the second system into a third system, where the last equation involves only one unknown. This transformation uses the second row to eliminate $$y$$ from the third row.

$$
\begin{array}{rcl} &\xrightarrow[]{-\rho_2+\rho_3} &\begin{array}{rcrcrcr} x &+ &y & & &= &0 \\ & &-3y&+ &3z &= &3 \\ & & & &-4z&= &0 \end{array} \end{array}
$$

Now we are set up for the solution. The third row shows that $$z=0$$. Substitute that back into the second row to get $$y=-1$$, and then substitute back into the first row to get $$x=1$$.

**Example 1.7**  —

For the Physics problem from the start of this chapter, Gauss' method gives this.

$$
\begin{array}{rcl} \begin{array}{rcrcr} 40h &+ &15c &= &100 \\ -50h &+ &25c &= &50 \end{array} &\xrightarrow[]{5/4\rho_1 +\rho_2} &\begin{array}{rcrcr} 40h &+ &15c &= &100 \\ & &(175/4)c &= &175 \end{array} \end{array}
$$

So $$c=4$$, and back-substitution gives that $$h=1$$. (The Chemistry problem is solved later.)

**Example 1.8**  —

The reduction

$$
\begin{array}{rcl} \begin{array}{rcrcrcr} x &+ &y &+ &z &= &9 \\ 2x &+ &4y &- &3z &= &1 \\ 3x &+ &6y &- &5z &= &0 \end{array} &\xrightarrow[-3\rho_1 +\rho_3]{-2\rho_1 +\rho_2} &\begin{array}{rcrcrcr} x &+ &y &+ &z &= &9 \\ & &2y &- &5z &= &-17\\ & &3y &- &8z&= &-27 \end{array} \\ &\xrightarrow[]{-(3/2)\rho_2+\rho_3} &\begin{array}{rcrcrcr} x &+ &y &+ &z &= &9 \\ & &2y &- &5z &= &-17\\ & & & &-(1/2)z &= &-(3/2) \end{array} \end{array}
$$

shows that $$z=3$$, $$y=-1$$, and $$x=7$$.

As these examples illustrate, Gauss' method uses the elementary reduction operations to set up back-substitution.

**Definition 1.9**  —

In each row, the first variable with a nonzero coefficient is the row's **leading variable**. A system is in **echelon form** if each leading variable is to the right of the leading variable in the row above it (except for the leading variable in the first row).

**Example 1.10**  —

The only operation needed in the examples above is pivoting. Here is a linear system that requires the operation of swapping equations. After the first pivot

$$
\begin{array}{rcl} \begin{array}{rcrcrcrcr} x &- &y & & & & &= &0 \\ 2x &- &2y &+ &z &+ &2w &= &4 \\ & &y & & &+ &w &= &0 \\ & & & &2z &+ &w &= &5 \end{array} &\xrightarrow[]{-2\rho_1 +\rho_2} &\begin{array}{rcrcrcrcr} x &- &y & & & & &= &0 \\ & & & &z &+ &2w &= &4 \\ & &y & & &+ &w &= &0 \\ & & & &2z &+ &w &= &5 \end{array} \end{array}
$$

the second equation has no leading $$y$$. To get one, we look lower down in the system for a row that has a leading $$y$$ and swap it in.

$$
\begin{array}{rcl} &\xrightarrow[]{\rho_2 \leftrightarrow\rho_3} &\begin{array}{rcrcrcrcr} x &- &y & & & & &= &0 \\ & &y & & &+ &w &= &0 \\ & & & &z &+ &2w &= &4 \\ & & & &2z &+ &w &= &5 \end{array} \end{array}
$$

(Had there been more than one row below the second with a leading $$y$$ then we could have swapped in any one.) The rest of Gauss' method goes as before.

$$
\begin{array}{rcl} &\xrightarrow[]{-2\rho_3 +\rho_4} &\begin{array}{rcrcrcrcr} x &- &y & & & & &= &0 \\ & &y & & &+ &w &= &0 \\ & & & &z &+ &2w &= &4 \\ & & & & & &-3w&= &-3 \end{array} \end{array}
$$

Back-substitution gives $$w=1$$, $$z=2$$, $$y=-1$$, and $$x=-1$$.

Strictly speaking, the operation of rescaling rows is not needed to solve linear systems. We have included it because we will use it later in this chapter as part of a variation on Gauss' method, the Gauss-Jordan method.

All of the systems seen so far have the same number of equations as unknowns. All of them have a solution, and for all of them there is only one solution. We finish this subsection by seeing for contrast some other things that can happen.

**Example 1.11**  —

Linear systems need not have the same number of equations as unknowns. This system

$$
\begin{array}{rcrcr} x &+ &3y &= &1 \\ 2x &+ &y &= &-3 \\ 2x &+ &2y &= &-2 \end{array}
$$

has more equations than variables. Gauss' method helps us understand this system also, since this

$$
\begin{array}{rcl} &\xrightarrow[-2\rho_1 +\rho_3]{-2\rho_1 +\rho_2} &\begin{array}{rcrcr} x &+ &3y &= &1 \\ & &-5y &= &-5 \\ & &-4y &= &-4 \end{array} \end{array}
$$

shows that one of the equations is redundant. Echelon form

$$
\begin{array}{rcl} &\xrightarrow[]{-(4/5)\rho_2 +\rho_3} &\begin{array}{rcrcr} x &+ &3y &= &1 \\ & &-5y &= &-5 \\ & &0 &= &0 \end{array} \end{array}
$$

gives $$y=1$$ and $$x=-2$$. The "$$0=0$$" is derived from the redundancy.

That example's system has more equations than variables. Gauss' method is also useful on systems with more variables than equations. Many examples are in the next subsection.

Another way that linear systems can differ from the examples shown earlier is that some linear systems do not have a unique solution. This can happen in two ways.

The first is that it can fail to have any solution at all.

**Example 1.12**  —

Contrast the system in the last example with this one.

$$
\begin{array}{rcl} \begin{array}{rcrcr} x &+ &3y &= &1 \\ 2x &+ &y &= &-3 \\ 2x &+ &2y &= &0 \end{array} &\xrightarrow[-2\rho_1 +\rho_3]{-2\rho_1 +\rho_2} &\begin{array}{rcrcr} x &+ &3y &= &1 \\ & &-5y &= &-5 \\ & &-4y &= &-2 \end{array} \end{array}
$$

Here the system is inconsistent: no pair of numbers satisfies all of the equations simultaneously. Echelon form makes this inconsistency obvious.

$$
\begin{array}{rcl} &\xrightarrow[]{-(4/5)\rho_2 +\rho_3} &\begin{array}{rcrcr} x &+ &3y &= &1 \\ & &-5y &= &-5 \\ & &0 &= &2 \end{array} \end{array}
$$

The solution set is empty.

**Example 1.13**  —

The prior system has more equations than unknowns, but that is not what causes the inconsistency— Example 1.11 has more equations than unknowns and yet is consistent. Nor is having more equations than unknowns sufficient for inconsistency, as is illustrated by this inconsistent system with the same number of equations as unknowns.

$$
\begin{array}{rcl} \begin{array}{rcrcr} x &+ &2y &= &8 \\ 2x &+ &4y &= &8 \end{array} &\xrightarrow[]{-2\rho_1 + \rho_2} &\begin{array}{rcrcr} x &+ &2y &= &8 \\ & &0 &= &-8 \end{array} \end{array}
$$

The other way that a linear system can fail to have a unique solution is to have many solutions.

**Example 1.14**  —

In this system

$$
\begin{array}{rcrcr} x &+ &y &= &4 \\ 2x &+ &2y &= &8 \end{array}
$$

any pair of numbers satisfying the first equation automatically satisfies the second. The solution set $$\{ (x,y)\,\big|\, x+y=4 \}$$ is infinite; some of its members are $$(0,4)$$, $$(-1,5)$$, and $$(2.5,1.5)$$. The result of applying Gauss' method here contrasts with the prior example because we do not get a contradictory equation.

$$
\begin{array}{rcl} &\xrightarrow[]{-2\rho_1 + \rho_2} &\begin{array}{rcrcr} x &+ &y &= &4 \\ & &0 &= &0 \end{array} \end{array}
$$

Don't be fooled by the "$$0=0$$" equation in that example. It is not the signal that a system has many solutions.

**Example 1.15**  —

The absence of a "$$0=0$$" does not keep a system from having many different solutions. This system is in echelon form

$$
\begin{array}{rcrcrcr} x &+ &y &+ &z &= &0 \\ & &y &+ &z &= &0 \end{array}
$$

has no "$$0=0$$", and yet has infinitely many solutions. (For instance, each of these is a solution: $$(0,1,-1)$$, $$(0,1/2,-1/2)$$, $$(0,0,0)$$, and $$(0,-\pi,\pi)$$. There are infinitely many solutions because any triple whose first component is $$0$$ and whose second component is the negative of the third is a solution.)

Nor does the presence of a "$$0=0$$" mean that the system must have many solutions. Example 1.11 shows that. So does this system, which does not have many solutions— in fact it has none— despite that when it is brought to echelon form it has a "$$0=0$$" row.

$$
\begin{array}{rcl} \begin{array}{rcrcrcr} 2x & & &- &2z &= &6 \\ & &y &+ &z &= &1 \\ 2x &+ &y &- &z &= &7 \\ & &3y &+ &3z &= &0 \end{array} &\xrightarrow[]{-\rho_1 +\rho_3} &\begin{array}{rcrcrcr} 2x & & &- &2z &= &6 \\ & &y &+ &z &= &1 \\ & &y &+ &z &= &1 \\ & &3y &+ &3z &= &0 \end{array} \\ &\xrightarrow[-3\rho_2 +\rho_4]{-\rho_2 +\rho_3} &\begin{array}{rcrcrcr} 2x & & &- &2z &= &6 \\ & &y &+ &z &= &1 \\ & & & &0 &= &0 \\ & & & &0 &= &-3 \end{array} \end{array}
$$

We will finish this subsection with a summary of what we've seen so far about Gauss' method.

Gauss' method uses the three row operations to set a system up for back substitution. If any step shows a contradictory equation then we can stop with the conclusion that the system has no solutions. If we reach echelon form without a contradictory equation, and each variable is a leading variable in its row, then the system has a unique solution and we find it by back substitution. Finally, if we reach echelon form without a contradictory equation, and there is not a unique solution (at least one variable is not a leading variable) then the system has many solutions.

The next subsection deals with the third case— we will see how to describe the solution set of a system with many solutions.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Use Gauss' method to find the unique solution for each system.

1. $$\begin{array}{rcrcr} 2x &+ &3y &= &13 \\ x &- &y &= &-1 \end{array}$$  
  
2.

$$
\begin{array}{rcrcrcr} x & & &- &z &= &0 \\ 3x &+ &y & & &= &1 \\ -x &+ &y &+ &z &= &4 \end{array}
$$

*This exercise is recommended for all readers.*

**Problem 2**  —

Use Gauss' method to solve each system or conclude "many solutions" or "no solutions".

1. $$\begin{array}{rcrcr} 2x &+ &2y &= &5 \\ x &- &4y &= &0 \end{array}$$  
  
2. $$\begin{array}{rcrcr} -x &+ &y &= &1 \\ x &+ &y &= &2 \end{array}$$  
  
3. $$\begin{array}{rcrcrcr} x &- &3y &+ &z &= &1 \\ x &+ &y &+ &2z &= &14 \end{array}$$  
  
4. $$\begin{array}{rcrcr} -x &- &y &= &1 \\ -3x &- &3y &= &2 \end{array}$$  
  
5. $$\begin{array}{rcrcrcr} & &4y &+ &z &= &20 \\ 2x &- &2y &+ &z &= &0 \\ x & & &+ &z &= &5 \\ x &+ &y &- &z &= &10 \end{array}$$  
  
6. $$\begin{array}{rcrcrcrcr} 2x & & &+ &z &+ &w &= &5 \\ & &y & & &- &w &= &-1 \\ 3x & & &- &z &- &w &= &0 \\ 4x &+ &y &+ &2z &+ &w &= &9 \end{array}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

There are methods for solving linear systems other than Gauss' method. One often taught in high school is to solve one of the equations for a variable, then substitute the resulting expression into other equations. That step is repeated until there is an equation with only one variable. From that, the first number in the solution is derived, and then back-substitution can be done. This method takes longer than Gauss' method, since it involves more arithmetic operations, and is also more likely to lead to errors. To illustrate how it can lead to wrong conclusions, we will use the system

$$
\begin{array}{rcrcr} x &+ &3y &= &1 \\ 2x &+ &y &= &-3 \\ 2x &+ &2y &= &0 \end{array}
$$

from Example 1.12.

1. Solve the first equation for $$x$$ and substitute that expression into the second equation. Find the resulting $$y$$.
2. Again solve the first equation for $$x$$, but this time substitute that expression into the third equation. Find this $$y$$.

What extra step must a user of this method take to avoid erroneously concluding a system has a solution?  
*This exercise is recommended for all readers.*

**Problem 4**  —

For which values of $$k$$ are there no solutions, many solutions, or a unique solution to this system?

$$
\begin{array}{rcrcr} x &- &y &= &1 \\ 3x &- &3y &= &k \end{array}
$$

*This exercise is recommended for all readers.*

**Problem 5**  —

This system is not linear, in some sense,

$$
\begin{array}{rcrcrcr} 2\sin\alpha &- &\cos\beta &+ &3\tan\gamma &= &3 \\ 4\sin\alpha &+ &2\cos\beta &- &2\tan\gamma &= &10 \\ 6\sin\alpha &- &3\cos\beta &+ &\tan\gamma &= &9 \end{array}
$$

and yet we can nonetheless apply Gauss' method. Do so. Does the system have a solution?  
*This exercise is recommended for all readers.*

**Problem 6**  —

What conditions must the constants, the $$b$$'s, satisfy so that each of these systems has a solution? *Hint.* Apply Gauss' method and see what happens to the right side (Anton 1987).

1. $$\begin{array}{rcrcr} x &- &3y &= &b_1 \\ 3x &+ &y &= &b_2 \\ x &+ &7y &= &b_3 \\ 2x &+ &4y &= &b_4 \end{array}$$  
  
2. $$\begin{array}{rcrcrcr} x_1 &+ &2x_2 &+ &3x_3 &= &b_1 \\ 2x_1 &+ &5x_2 &+ &3x_3 &= &b_2 \\ x_1 & & &+ &8x_3 &= &b_3 \end{array}$$

**Problem 7**  —

True or false: a system with more unknowns than equations has at least one solution. (As always, to say "true" you must prove it, while to say "false" you must produce a counterexample.)

**Problem 8**  —

Must any Chemistry problem like the one that starts this subsection— a balance the reaction problem— have infinitely many solutions?  
*This exercise is recommended for all readers.*

**Problem 9**  —

Find the coefficients $$a$$, $$b$$, and $$c$$ so that the graph of $$f(x)=ax^2+bx+c$$ passes through the points $$(1,2)$$, $$(-1,6)$$, and $$(2,3)$$.

**Problem 10**  —

Gauss' method works by combining the equations in a system to make new equations.

1. Can the equation $$3x-2y=5$$ be derived, by a sequence of Gaussian reduction steps, from the equations in this system?

$$
\begin{array}{rcrcr} x &+ &y &= &1 \\ 4x &- &y &= &6 \end{array}
$$

2. Can the equation $$5x-3y=2$$ be derived, by a sequence of Gaussian reduction steps, from the equations in this system?

$$
\begin{array}{rcrcr} 2x &+ &2y &= &5 \\ 3x &+ &y &= &4 \end{array}
$$

3. Can the equation $$6x-9y+5z=-2$$ be derived, by a sequence of Gaussian reduction steps, from the equations in the system?

$$
\begin{array}{rcrcrcr} 2x &+ &y &- &z &= &4 \\ 6x &- &3y &+ &z &= &5 \end{array}
$$

**Problem 11**  —

Prove that, where $$a,b,\ldots,e$$ are real numbers and $$a\neq 0$$, if

$$
ax+by=c
$$

has the same solution set as

$$
ax+dy=e
$$

then they are the same equation. What if $$a=0$$?  
*This exercise is recommended for all readers.*

**Problem 12**  —

Show that if $$ad-bc\neq 0$$ then

$$
\begin{array}{rcrcr} ax &+ &by &= &j \\ cx &+ &dy &= &k \end{array}
$$

has a unique solution.  
*This exercise is recommended for all readers.*

**Problem 13**  —

In the system

$$
\begin{array}{rcrcr} ax &+ &by &= &c \\ dx &+ &ey &= &f \end{array}
$$

each of the equations describes a line in the $$xy$$-plane. By geometrical reasoning, show that there are three possibilities: there is a unique solution, there is no solution, and there are infinitely many solutions.

**Problem 14**  —

Finish the proof of Theorem 1.4.

**Problem 15**  —

Is there a two-unknowns linear system whose solution set is all of $$\mathbb{R}^2$$?  
*This exercise is recommended for all readers.*

**Problem 16**  —

Are any of the operations used in Gauss' method redundant? That is, can any of the operations be synthesized from the others?

**Problem 17**  —

Prove that each operation of Gauss' method is reversible. That is, show that if two systems are related by a row operation $$S_1\rightarrow S_2$$ then there is a row operation to go back $$S_2\rightarrow S_1$$.

**? Problem 18**  —

A box holding pennies, nickels and dimes contains thirteen coins with a total value of $$83$$ cents. How many coins of each type are in the box? (Anton 1987)

**? Problem 19**  —

Four positive integers are given. Select any three of the integers, find their arithmetic average, and add this result to the fourth integer. Thus the numbers 29, 23, 21, and 17 are obtained. One of the original integers is:

1. 19
2. 21
3. 23
4. 29
5. 17

(Salkind 1975, 1955 problem 38)  
*This exercise is recommended for all readers.*

**? Problem 20**  —

Laugh at this: $$\text{AHAHA}+\text{TEHE}=\text{TEHAW}$$. It resulted from substituting a code letter for each digit of a simple example in addition, and it is required to identify the letters and prove the solution unique (Ransom & Gupta 1935).

**? Problem 21**  —

The Wohascum County Board of Commissioners, which has 20 members, recently had to elect a President. There were three candidates ($$A$$, $$B$$, and $$C$$); on each ballot the three candidates were to be listed in order of preference, with no abstentions. It was found that 11 members, a majority, preferred $$A$$ over $$B$$ (thus the other 9 preferred $$B$$ over $$A$$). Similarly, it was found that 12 members preferred $$C$$ over $$A$$. Given these results, it was suggested that $$B$$ should withdraw, to enable a runoff election between $$A$$ and $$C$$. However, $$B$$ protested, and it was then found that 14 members preferred $$B$$ over $$C$$! The Board has not yet recovered from the resulting confusion. Given that every possible order of $$A$$, $$B$$, $$C$$ appeared on at least one ballot, how many members voted for $$B$$ as their first choice (Gilbert, Krusemeyer & Larson 1993, Problem number 2)?

**? Problem 22**  —

"This system of $$n$$ linear equations with $$n$$ unknowns," said the Great Mathematician, "has a curious property."

"Good heavens!" said the Poor Nut, "What is it?"

"Note," said the Great Mathematician, "that the constants are in arithmetic progression."

"It's all so clear when you explain it!" said the Poor Nut. "Do you mean like $$6x+9y=12$$ and $$15x+18y=21$$?"

"Quite so," said the Great Mathematician, pulling out his bassoon. "Indeed, even larger systems can be solved regardless of their progression. Can you find their solution?"

"Good heavens!" cried the Poor Nut, "I am baffled."

Are you? (Dudley, Lebow & Rothman 1963)

Solutions

### References

- Anton, Howard (1987), *Elementary Linear Algebra*, John Wiley & Sons.
- Dudley, Underwood (proposer); Lebow, Arnold (proposer); Rothman, David (solver) (1963), "Elemantary problem 1151", *American Mathematical Monthly*, **70** (1): 93.
- Gilbert, George T.; Krusemeyer, Mark; Larson, Loren C. (1993), *The Wohascum County Problem Book*, The Mathematical Association of America.
- Ransom, W. R. (proposer); Gupta, Hansraj (solver) (1935), "Elementary problem 105", *American Mathematical Monthly*, **42** (1): 47.
- Salkind, Charles T. (1975), *Contest Problem Book No 1: Annual High School Mathematics Examinations 1950-1960*.

---

*Source: Wikibooks, Linear Algebra/Gauss' Method (https://en.wikibooks.org/wiki/Linear_Algebra/Gauss%27_Method), by Wikibooks contributors, CC BY-SA 4.0.*
