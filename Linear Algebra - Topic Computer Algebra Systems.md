# Topic: Computer Algebra Systems

The linear systems in this chapter are small enough that their solution by hand is easy. But large systems are easiest, and safest, to do on a computer. There are special purpose programs such as LINPACK for this job. Another popular tool is a general purpose computer algebra system, including both commercial packages such as Maple, Mathematica, or MATLAB, or free packages such as SciLab, Sage, or Octave.

For example, in the Topic on Networks, we need to solve this.

$$
\begin{array}{rcrcrcrcrcrcrcr} i_0 &- &i_1 &- &i_2 & & & & & & & & &= &0 \\ & &i_1 & & &- &i_3 & & &- &i_5 & & &= &0 \\ & & & &i_2 & & &- &i_4 &+ &i_5 & & &= &0 \\ & & & & & &i_3 &+ &i_4 & & &- &i_6 &= &0 \\ & &5i_1 & & &+ &10i_3 & & & & & & &= &10 \\ & & & &2i_2 & & &+ &4i_4 & & & & &= &10 \\ & &5i_1 &- &2i_2 & & & & &+ &50i_5 && &= &0 \end{array}
$$

It can be done by hand, but it would take a while and be error-prone. Using a computer is better.

We illustrate by solving that system under Maple (for another system, a user's manual would obviously detail the exact syntax needed). The array of coefficients can be entered in this way  
```
> A:=array( [[1,-1,-1,0,0,0,0],
[0,1,0,-1,0,-1,0],
[0,0,1,0,-1,1,0],
[0,0,0,1,1,0,-1],
[0,5,0,10,0,0,0],
[0,0,2,0,4,0,0],
[0,5,-2,0,0,50,0]] );

```  
(putting the rows on separate lines is not necessary, but is done for clarity). The vector of constants is entered similarly.

```
> u:=array( [0,0,0,0,10,10,0] );

```

Then the system is solved, like magic.

```
> linsolve(A,u);
7  2  5  2  5     7
[ -, -, -, -, -, 0, - ]
3  3  3  3  3     3

```

Mathematica can solve this with

```
RowReduce[({{1, -1, -1, 0, 0, 0, 0, 0}, {0, 1, 0, -1, 0, -1, 0,
 0}, {0, 0, 1, 0, -1, 1, 0, 0}, {0, 0, 0, 1, 1, 0, -1, 0}, {0, 5,
 0, 10, 0, 0, 0, 10}, {0, 0, 2, 0, 4, 0, 0, 10}, {0, 5, -2, 0, 0,
 50, 0, 0}})]

```

This returns the following output:

```
{{1, 0, 0, 0, 0, 0, 0, 7/3}, {0, 1, 0, 0, 0, 0, 0, 2/3}, {0, 0, 1, 0,
 0, 0, 0, 5/3}, {0, 0, 0, 1, 0, 0, 0, 2/3}, {0, 0, 0, 0, 1, 0, 0, 5/
 3}, {0, 0, 0, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 1, 7/3}}

```

Systems with infinitely many solutions are solved in the same

way— the computer simply returns a parametrization.

### Exercises

*Answers for this Topic use Maple as the computer algebra system. In particular, all of these were tested on Maple V running under MS-DOS NT version 4.0. (On all of them, the preliminary command to load the linear algebra package along with Maple's responses to the Enter key, have been omitted.) Other systems have similar commands.*

**Problem 1**  —

Use the computer to solve the two problems that opened this chapter.

1. This is the Statics problem.

$$
\begin{array}{rl} 40h+15c &= 100 \\ 25c &= 50+50h \end{array}
$$

2. This is the Chemistry problem.

$$
\begin{array}{rl} 7h &= 7j \\ 8h +1i &= 5j+2k \\ 1i &= 3j \\ 3i &= 6j+1k \end{array}
$$

**Problem 2**  —

Use the computer to solve these systems from the first subsection, or conclude "many solutions" or "no solutions".

1. $$\begin{array}{rcrcr} 2x &+ &2y &= &5 \\ x &- &4y &= &0 \end{array}$$
2. $$\begin{array}{rcrcr} -x &+ &y &= &1 \\ x &+ &y &= &2 \end{array}$$
3. $$\begin{array}{rcrcrcr} x &- &3y &+ &z &= &1 \\ x &+ &y &+ &2z &= &14 \end{array}$$
4. $$\begin{array}{rcrcr} -x &- &y &= &1 \\ -3x &- &3y &= &2 \end{array}$$
5. $$\begin{array}{rcrcrcr} & &4y &+ &z &= &20 \\ 2x &- &2y &+ &z &= &0 \\ x & & &+ &z &= &5 \\ x &+ &y &- &z &= &10 \end{array}$$
6. $$\begin{array}{rcrcrcrcr} 2x & & &+ &z &+ &w &= &5 \\ & &y & & &- &w &= &-1 \\ 3x & & &- &z &- &w &= &0 \\ 4x &+ &y &+ &2z &+ &w &= &9 \end{array}$$

**Problem 3**  —

Use the computer to solve these systems from the second subsection.

1. $$\begin{array}{rcrcr} 3x &+ &6y &= &18 \\ x &+ &2y &= &6 \end{array}$$
2. $$\begin{array}{rcrcr} x &+ &y &= &1 \\ x &- &y &= &-1 \end{array}$$
3. $$\begin{array}{rcrcrcr} x_1 & & &+ &x_3 &= &4 \\ x_1 &- &x_2 &+ &2x_3 &= &5 \\ 4x_1 &- &x_2 &+ &5x_3 &= &17 \end{array}$$
4. $$\begin{array}{rcrcrcr} 2a &+ &b &- &c &= &2 \\ 2a & & &+ &c &= &3 \\ a &- &b & & &= &0 \end{array}$$
5. $$\begin{array}{rcrcrcrcr} x &+ &2y &- &z & & &= &3 \\ 2x &+ &y & & &+ &w &= &4 \\ x &- &y &+ &z &+ &w &= &1 \end{array}$$
6. $$\begin{array}{rcrcrcrcr} x & & &+ &z &+ &w &= &4 \\ 2x &+ &y & & &- &w &= &2 \\ 3x &+ &y &+ &z & & &= &7 \end{array}$$

**Problem 4**  —

What does the computer give for the solution of the general $$2 \! \times \! 2$$ system?

$$
\begin{array}{rcrcr} ax &+ &cy &= &p \\ bx &+ &dy &= &q \end{array}
$$

Solutions

---

*Source: Wikibooks, Linear Algebra/Topic: Computer Algebra Systems (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Computer_Algebra_Systems), by Wikibooks contributors, CC BY-SA 4.0.*
