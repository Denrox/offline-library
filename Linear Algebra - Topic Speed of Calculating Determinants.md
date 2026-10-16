# Topic: Speed of Calculating Determinants

The permutation expansion formula for computing determinants is useful for proving theorems, but the method of using row operations is a much better for finding the determinants of a large matrix. We can make this statement precise by considering, as computer algorithm designers do, the number of arithmetic operations that each method uses.

The speed of an algorithm is measured by finding how the time taken by the computer grows as the size of its input data set grows. For instance, how much longer will the algorithm take if we increase the size of the input data by a factor of ten, from a $$1000$$ row matrix to a $$10,000$$ row matrix or from $$10,000$$ to $$100,000$$? Does the time taken grow by a factor of ten, or by a factor of a hundred, or by a factor of a thousand? That is, is the time taken by the algorithm proportional to the size of the data set, or to the square of that size, or to the cube of that size, etc.?

Recall the permutation expansion formula for determinants.

$$
\begin{array}{rl} \begin{vmatrix} t_{1,1} &t_{1,2} &\ldots &t_{1,n} \\ t_{2,1} &t_{2,2} &\ldots &t_{2,n} \\ &\vdots \\ t_{n,1} &t_{n,2} &\ldots &t_{n,n} \end{vmatrix} &=\displaystyle\sum_{\text{permutations }\phi}\!\!\!\! t_{1,\phi(1)}t_{2,\phi(2)}\cdots t_{n,\phi(n)} \left|P_{\phi}\right| \\ &= \begin{align} &t_{1,\phi_1(1)}\cdot t_{2,\phi_1(2)}\cdots t_{n,\phi_1(n)}\left|P_{\phi_1}\right| \\ &\quad +t_{1,\phi_2(1)}\cdot t_{2,\phi_2(2)}\cdots t_{n,\phi_2(n)}\left|P_{\phi_2}\right| \\ &\quad\vdots \\ &\quad +t_{1,\phi_k(1)}\cdot t_{2,\phi_k(2)}\cdots t_{n,\phi_k(n)}\left|P_{\phi_k}\right| \end{align} \end{array}
$$

There are $$n!=n\cdot(n-1)\cdot(n-2)\cdots 2\cdot 1$$ different $$n$$-permutations. For numbers $$n$$ of any size at all, this is a large value; for instance, even if $$n$$ is only $$10$$ then the expansion has $$10!=3,628,800$$ terms, all of which are obtained by multiplying $$n$$ entries together. This is a very large number of multiplications (for instance, (Knuth 1988) suggests $$10!$$ steps as a rough boundary for the limit of practical calculation). The factorial function grows faster than the square function. It grows faster than the cube function, the fourth power function, or any polynomial function. (One way to see that the factorial function grows faster than the square is to note that multiplying the first two factors in $$n!$$ gives $$n\cdot(n-1)$$, which for large $$n$$ is approximately $$n^2$$, and then multiplying in more factors will make it even larger. The same argument works for the cube function, etc.) So a computer that is programmed to use the permutation expansion formula, and thus to perform a number of operations that is greater than or equal to the factorial of the number of rows, would take very long times as its input data set grows.

In contrast, the time taken by the row reduction method does not grow so fast. This fragment of row-reduction code is in the computer language FORTRAN. The matrix is stored in the $$N \! \times \! N$$ array *A*. For each *ROW* between $$1$$ and $$N$$ parts of the program not shown here have already found the pivot entry $$A(ROW,COL)$$. Now the program does a row pivot.

$$
-PIVINV\cdot \rho_{ROW} +\rho_i
$$

(This code fragment is for illustration only and is incomplete. Still, analysis of a finished version that includes all of the tests and subcases is messier but gives essentially the same conclusion.)  
  
PIVINV=1.0/A(ROW,COL)  
DO 10 I=ROW+1, N  
DO 20 J=I, N  
A(I,J)=A(I,J)-PIVINV*A(ROW,J)  
20 CONTINUE  
10 CONTINUE  
  
The outermost loop (not shown) runs through $$N-1$$ rows. For each row, the nested $$I$$ and $$J$$ loops shown perform arithmetic on the entries in *A* that are below and to the right of the pivot entry. Assume that the pivot is found in the expected place, that is, that $$COL=ROW$$. Then there are $$(N-ROW)^2$$ entries below and to the right of the pivot. On average, *ROW* will be $$N/2$$. Thus, we estimate that the arithmetic will be performed about $$(N/2)^2$$ times, that is, will run in a time proportional to the square of the number of equations. Taking into account the outer loop that is not shown, we get the estimate that the running time of the algorithm is proportional to the cube of the number of equations.

Finding the fastest algorithm to compute the determinant is a topic of current research. Algorithms are known that run in time between the second and third power.

Speed estimates like these help us to understand how quickly or slowly an algorithm will run. Algorithms that run in time proportional to the size of the data set are fast, algorithms that run in time proportional to the square of the size of the data set are less fast, but typically quite usable, and algorithms that run in time proportional to the cube of the size of the data set are still reasonable in speed for not-too-big input data. However, algorithms that run in time (greater than or equal to) the factorial of the size of the data set are not practical for input of any appreciable size.

There are other methods besides the two discussed here that are also used for computation of determinants. Those lie outside of our scope. Nonetheless, this contrast of the two methods for computing determinants makes the point that although in principle they give the same answer, in practice the idea is to select the one that is fast.

### Exercises

*Most of these problems presume access to a computer.*

**Problem 1**  —

Computer systems generate random numbers (of course, these are only pseudo-random, in that they are generated by an algorithm, but they pass a number of reasonable statistical tests for randomness).

1. Fill a $$5 \! \times \! 5$$ array with random numbers (say, in the range $$0..1)$$). See if it is singular. Repeat that experiment a few times. Are singular matrices frequent or rare (in this sense)?
2. Time your computer algebra system at finding the determinant of ten $$5 \! \times \! 5$$ arrays of random numbers. Find the average time per array. Repeat the prior item for $$15 \! \times \! 15$$ arrays, $$25 \! \times \! 25$$ arrays, and $$35 \! \times \! 35$$ arrays. (Notice that, when an array is singular, it can sometimes be found to be so quite quickly, for instance if the first row equals the second. In the light of your answer to the first part, do you expect that singular systems play a large role in your average?)
3. Graph the input size versus the average time.

**Problem 2**  —

Compute the determinant of each of these by hand using the two methods discussed above.

1. $$\begin{vmatrix} 2 &1 \\ 5 &-3 \end{vmatrix}$$
2. $$\begin{vmatrix} 3 &1 &1 \\ -1 &0 &5 \\ -1 &2 &-2 \end{vmatrix}$$
3. $$\begin{vmatrix} 2 &1 &0 &0 \\ 1 &3 &2 &0 \\ 0 &-1 &-2 &1 \\ 0 &0 &-2 &1 \end{vmatrix}$$

Count the number of multiplications and divisions used in each case, for each of the methods. (On a computer, multiplications and divisions take much longer than additions and subtractions, so algorithm designers worry about them more.)

**Problem 3**  —

What $$10 \! \times \! 10$$ array can you invent that takes your computer system the longest to reduce? The shortest?

**Problem 4**  —

Write the rest of the FORTRAN program to do a straightforward implementation of calculating determinants via Gauss' method. (Don't test for a zero pivot.) Compare the speed of your code to that used in your computer algebra system.

**Problem 5**  —

The FORTRAN language specification requires that arrays be stored "by column", that is, the entire first column is stored contiguously, then the second column, etc. Does the code fragment given take advantage of this, or can it be rewritten to make it faster, by taking advantage of the fact that computer fetches are faster from contiguous locations?

[Solutions

### References

- Knuth, Donald E. (1988), *The Art of Computer Programming*, Addison Wesley.

---

*Source: Wikibooks, Linear Algebra/Topic: Speed of Calculating Determinants (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Speed_of_Calculating_Determinants), by Wikibooks contributors, CC BY-SA 4.0.*
