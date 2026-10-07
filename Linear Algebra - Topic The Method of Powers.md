# Topic: The Method of Powers

In practice, calculating eigenvalues and eigenvectors is a difficult problem. Finding, and solving, the characteristic polynomial of the large matrices often encountered in applications is too slow and too hard. Other techniques, indirect ones that avoid the characteristic polynomial, are used. Here we shall see such a method that is suitable for large matrices that are "sparse" (the great majority of the entries are zero).

Suppose that the $$n \! \times \! n$$ matrix $$T$$ has the $$n$$ distinct eigenvalues $$\lambda_1$$, $$\lambda_2$$, ..., $$\lambda_n$$. Then $$\mathbb{R}^n$$ has a basis that is composed of the associated eigenvectors $$\langle \vec{\zeta}_1,\dots,\vec{\zeta}_n \rangle$$. For any $$\vec{v}\in\mathbb{R}^n$$, where $$\vec{v}=c_1\vec{\zeta}_1+\dots+c_n\vec{\zeta}_n$$, iterating $$T$$ on $$\vec{v}$$ gives these.

$$
\begin{array}{rl} T\vec{v} &=c_1\lambda_1\vec{\zeta}_1+c_2\lambda_2\vec{\zeta}_2+ \dots+c_n\lambda_n\vec{\zeta}_n \\ T^2\vec{v} &=c_1\lambda_1^2\vec{\zeta}_1+c_2\lambda_2^2\vec{\zeta}_2+ \dots+c_n\lambda_n^2\vec{\zeta}_n \\ T^3\vec{v} &=c_1\lambda_1^3\vec{\zeta}_1+c_2\lambda_2^3\vec{\zeta}_2+ \dots+c_n\lambda_n^3\vec{\zeta}_n \\ &\vdots \\ T^k\vec{v} &=c_1\lambda_1^k\vec{\zeta}_1+c_2\lambda_2^k\vec{\zeta}_2+ \dots+c_n\lambda_n^k\vec{\zeta}_n \end{array}
$$

If one of the eigenvalues, say, $$\lambda_1$$, has a larger absolute value than any of the other eigenvalues then its term will dominate the above expression. Put another way, dividing through by $$\lambda_1^k$$ gives this,

$$
\frac{T^k\vec{v}}{\lambda_1^k} =c_1\vec{\zeta}_1+c_2\frac{\lambda_2^k}{\lambda_1^k}\vec{\zeta}_2+ \dots+c_n\frac{\lambda_n^k}{\lambda_1^k}\vec{\zeta}_n
$$

and, because $$\lambda_1$$ is assumed to have the largest absolute value, as $$k$$ gets larger the fractions go to zero. Thus, the entire expression goes to $$c_1\vec{\zeta}_1$$.

That is (as long as $$c_1$$ is not zero), as $$k$$ increases, the vectors $$T^k\vec{v}$$ will tend toward the direction of the eigenvectors associated with the dominant eigenvalue, and, consequently, the ratios of the lengths $$|\,T^{k}\vec{v}\,|/|\,T^{k-1}\vec{v}\,|$$ will tend toward that dominant eigenvalue.

For example, (sample computer code for this follows the exercises), because the matrix

$$
T=\begin{pmatrix} 3 &0 \\ 8 &-1 \end{pmatrix}
$$

is triangular, its eigenvalues are just the entries on the diagonal, $$3$$ and $$-1$$. Arbitrarily taking $$\vec{v}$$ to have the components $$1$$ and $$1$$ gives

$$
\begin{array}{c|ccccc} \vec{v} &T\vec{v} &T^2\vec{v} &\cdots &T^9\vec{v} &T^{10}\vec{v} \\ \hline \begin{pmatrix} 1 \\ 1 \end{pmatrix} &\begin{pmatrix} 3 \\ 7 \end{pmatrix} &\begin{pmatrix} 9 \\ 17 \end{pmatrix} &\cdots &\begin{pmatrix} 19\,683 \\ 39\,367 \end{pmatrix} &\begin{pmatrix} 59\,049 \\ 118\,097 \end{pmatrix} \end{array}
$$

and the ratio between the lengths of the last two is $$2.999\,9$$.

Two implementation issues must be addressed. The first issue is that, instead of finding the powers of $$T$$ and applying them to $$\vec{v}$$, we will compute $$\vec{v}_1$$ as $$T\vec{v}$$ and then compute $$\vec{v}_2$$ as $$T\vec{v}_1$$, etc. (i.e., we never separately calculate $$T^2$$, $$T^3$$, etc.). These matrix-vector products can be done quickly even if $$T$$ is large, provided that it is sparse. The second issue is that, to avoid generating numbers that are so large that they overflow our computer's capability, we can normalize the $$\vec{v}_i$$'s at each step. For instance, we can divide each $$\vec{v}_i$$ by its length (other possibilities are to divide it by its largest component, or simply by its first component). We thus implement this method by generating

$$
\begin{array}{rl} \vec{w}_0 &=\vec{v}_0/|\vec{v}_0| \\ \vec{v}_1 &=T\vec{w}_0 \\ \vec{w}_1 &=\vec{v}_1/|\vec{v}_1| \\ \vec{v}_2 &=T\vec{w}_2 \\ &\vdots \\ \vec{w}_{k-1} &=\vec{v}_{k-1}/|\vec{v}_{k-1}| \\ \vec{v}_k &=T\vec{w}_k \end{array}
$$

until we are satisfied. Then the vector $$\vec{v}_k$$ is an approximation of an eigenvector, and the approximation of the dominant eigenvalue is the ratio $$|\vec{v}_{k}|/|\vec{w}_{k-1}|=|\vec{v}_k|$$.

One way we could be "satisfied" is to iterate until our approximation of the eigenvalue settles down. We could decide, for instance, to stop the iteration process not after some fixed number of steps, but instead when $$|\vec{v}_k|$$ differs from $$|\vec{v}_{k-1}|$$ by less than one percent, or when they agree up to the second significant digit.

The rate of convergence is determined by the rate at which the powers of $$|\lambda_2/\lambda_1|$$ go to zero, where $$\lambda_2$$ is the eigenvalue of second largest norm. If that ratio is much less than one then convergence is fast, but if it is only slightly less than one then convergence can be quite slow. Consequently, the method of powers is not the most commonly used way of finding eigenvalues (although it is the simplest one, which is why it is here as the illustration of the possibility of computing eigenvalues without solving the characteristic polynomial). Instead, there are a variety of methods that generally work by first replacing the given matrix $$T$$ with another that is similar to it and so has the same eigenvalues, but is in some reduced form such as *tridiagonal form*: the only nonzero entries are on the diagonal, or just above or below it. Then special techniques can be used to find the eigenvalues. Once the eigenvalues are known, the eigenvectors of $$T$$ can be easily computed. These other methods are outside of our scope. A good reference is (Goult et al. 1975).

### Exercises

**Problem 1**  —

Use ten iterations to estimate the largest eigenvalue of these matrices, starting from the vector with components $$1$$ and $$2$$. Compare the answer with the one obtained by solving the characteristic equation.

1. $$\begin{pmatrix} 1 &5 \\ 0 &4 \end{pmatrix}$$
2. $$\begin{pmatrix} 3 &2 \\ -1 &0 \end{pmatrix}$$

**Problem 2**  —

Redo the prior exercise by iterating until $$|\vec{v}_k|-|\vec{v}_{k-1}|$$ has absolute value less than $$0.01$$ At each step, normalize by dividing each vector by its length. How many iterations are required? Are the answers significantly different?

**Problem 3**  —

Use ten iterations to estimate the largest eigenvalue of these matrices, starting from the vector with components $$1$$, $$2$$, and $$3$$. Compare the answer with the one obtained by solving the characteristic equation.

1. $$\begin{pmatrix} 4 &0 &1 \\ -2 &1 &0 \\ -2 &0 &1 \end{pmatrix}$$
2. $$\begin{pmatrix} -1 &2 &2 \\ 2 &2 &2 \\ -3 &-6 &-6 \end{pmatrix}$$

**Problem 4**  —

Redo the prior exercise by iterating until $$|\vec{v}_k|-|\vec{v}_{k-1}|$$ has absolute value less than $$0.01$$. At each step, normalize by dividing each vector by its length. How many iterations does it take? Are the answers significantly different?

**Problem 5**  —

What happens if $$c_1=0$$? That is, what happens if the initial vector does not to have any component in the direction of the relevant eigenvector?

**Problem 6**  —

How can the method of powers be adopted to find the smallest eigenvalue?

Solutions

This is the code for the computer algebra system Octave that was used to do the calculation above. (It has been lightly edited to remove blank lines, etc.)

**Computer Code**  
  
>T=[3, 0;  
8, -1]  
T=  
3 0  
8 -1  
>v0=[1; 2]  
v0=  
1  
1  
>v1=T*v0  
v1=  
3  
7  
>v2=T*v1  
v2=  
9  
17  
>T9=T**9  
T9=  
19683 0  
39368 -1  
>T10=T**10  
T10=  
59049 0  
118096 1  
>v9=T9*v0  
v9=  
19683  
39367  
>v10=T10*v0  
v10=  
59049  
118096  
>norm(v10)/norm(v9)  
ans=2.9999  
  
Remark: we are ignoring the power of Octave here; there are built-in functions to automatically apply quite sophisticated methods to find eigenvalues and eigenvectors. Instead, we are using just the system as a calculator.

### References

- Goult, R.J.; Hoskins, R.F.; Milner, J.A.; Pratt, M.J. (1975), *Computational Methods in Linear Algebra*, Wiley.

---

*Source: Wikibooks, Linear Algebra/Topic: The Method of Powers (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_The_Method_of_Powers), by Wikibooks contributors, CC BY-SA 4.0.*
