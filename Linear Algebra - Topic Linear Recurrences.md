# Topic: Linear Recurrences

In 1202 Leonardo of Pisa, also known as Fibonacci, posed this problem.

A certain man put a pair of rabbits in a place surrounded on all sides by a wall. How many pairs of rabbits can be produced from that pair in a year if it is supposed that every month each pair begets a new pair which from the second month on becomes productive?

This moves past an elementary exponential growth model for population increase to include the fact that there is an initial period where newborns are not fertile. However, it retains other simplyfing assumptions, such as that there is no gestation period and no mortality.

The number of newborn pairs that will appear in the upcoming month is simply the number of pairs that were alive last month, since those will all be fertile, having been alive for two months. The number of pairs alive next month is the sum of the number alive current month and the number of newborns.

$$
f(n+1)=f(n)+f(n-1) \qquad \text{where }f(0)=1\text{, }f(1)=1
$$

The is an example of a *recurrence relation* (it is called that because the values of $$f$$ are calculated by looking at other, prior, values of $$f$$). From it, we can easily answer Fibonacci's twelve-month question.

$$
\begin{array}{r|ccccccccccccc} \textit{month} &0 &1 &2 &3 &4 &5 &6 &7 &8 &9 &10 &11 &12 \\ \hline \textit{pairs} &1 &1 &2 &3 &5 &8 &13 &21 &34 &55 &89 &144 &233 \end{array}
$$

The sequence of numbers defined by the above equation (of which the first few are listed) is the *Fibonacci sequence*. The material of this chapter can be used to give a formula with which we can can calculate $$f(n+1)$$ without having to first find $$f(n)$$, $$f(n-1)$$, etc.

For that, observe that the recurrence is a linear relationship and so we can give a suitable matrix formulation of it.

$$
\begin{pmatrix} 1 &1 \\ 1 &0 \end{pmatrix} \begin{pmatrix} f(n) \\ f(n-1) \end{pmatrix} = \begin{pmatrix} f(n+1) \\ f(n) \end{pmatrix} \qquad\text{where }\begin{pmatrix} f(1) \\ f(0) \end{pmatrix}=\begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

Then, where we write $$T$$ for the matrix and $$\vec{v}_{n}$$ for the vector with components $$f(n+1)$$ and $$f(n)$$, we have that $$\vec{v}_n=T^n\vec{v}_0$$. The advantage of this matrix formulation is that by diagonalizing $$T$$ we get a fast way to compute its powers: where $$T=PDP^{-1}$$ we have $$T^n=PD^nP^{-1}$$, and the $$n$$-th power of the diagonal matrix $$D$$ is the diagonal matrix whose entries that are the $$n$$-th powers of the entries of $$D$$.

The characteristic equation of $$T$$ is $$\lambda^2-\lambda-1$$. The quadratic formula gives its roots as $$(1+\sqrt{5})/2$$ and $$(1-\sqrt{5})/2$$. Diagonalizing gives this.

$$
\begin{pmatrix} 1 &1 \\ 1 &0 \end{pmatrix} =\begin{pmatrix} \frac{1+\sqrt{5}}{2} &\frac{1-\sqrt{5}}{2} \\ 1 &1 \end{pmatrix} \begin{pmatrix} \frac{1+\sqrt{5}}{2} &0 \\ 0 &\frac{1-\sqrt{5}}{2} \end{pmatrix} \begin{pmatrix} \frac{1}{\sqrt{5}} &-\frac{1-\sqrt{5}}{2\sqrt{5}} \\ \frac{-1}{\sqrt{5}} &\frac{1+\sqrt{5}}{2\sqrt{5}} \end{pmatrix}
$$

Introducing the vectors and taking the $$n$$-th power, we have

$$
\begin{array}{rl} \begin{pmatrix} f(n+1) \\ f(n) \end{pmatrix} &=\begin{pmatrix} 1 &1 \\ 1 &0 \end{pmatrix}^n \begin{pmatrix} f(1) \\ f(0) \end{pmatrix} \\ &=\begin{pmatrix} \frac{1+\sqrt{5}}{2} &\frac{1-\sqrt{5}}{2} \\ 1 &1 \end{pmatrix} \begin{pmatrix} \frac{1+\sqrt{5}}{2}^n &0 \\ 0 &\frac{1-\sqrt{5}}{2}^n \end{pmatrix} \begin{pmatrix} \frac{1}{\sqrt{5}} &-\frac{1-\sqrt{5}}{2\sqrt{5}} \\ \frac{-1}{\sqrt{5}} &\frac{1+\sqrt{5}}{2\sqrt{5}} \end{pmatrix} \begin{pmatrix} f(1) \\ f(0) \end{pmatrix} \end{array}
$$

We can compute $$f(n)$$ from the second component of that equation.

$$
f(n)=\frac{1}{\sqrt{5}}\left[\left(\frac{1+\sqrt{5}}{2}\right)^{n+1} -\left(\frac{1-\sqrt{5}}{2}\right)^{n+1}\right]
$$

Notice that $$f$$ is dominated by its first term because $$(1-\sqrt{5})/2$$ is less than one, so its powers go to zero.

In general, a *linear recurrence relation* has the form

$$
f(n+1)=a_nf(n)+a_{n-1}f(n-1)+\dots+a_{n-k}f(n-k)
$$

(it is also called a *difference equation*). This recurrence relation is *homogeneous* because there is no constant term; i.e, it can be put into the form $$0=-f(n+1)+a_nf(n)+a_{n-1}f(n-1)+\dots+a_{n-k}f(n-k)$$. This is said to be a relation of *order* $$k$$. The relation, along with the *initial conditions* $$f(0)$$, ..., $$f(k)$$ completely determine a sequence. For instance, the Fibonacci relation is of order $$2$$ and it, along with the two initial conditions $$f(0)=1$$ and $$f(1)=1$$, determines the Fibonacci sequence simply because we can compute any $$f(n)$$ by first computing $$f(2)$$, $$f(3)$$, etc. In this Topic, we shall see how linear algebra can be used to solve linear recurrence relations.

First, we define the vector space in which we are working. Let $$V$$ be the set of functions $$f$$ from the natural numbers $$\mathbb{N}=\{0,1,2,\ldots\}$$ to the real numbers. (Below we shall have functions with domain $$\{1,2,\ldots\}$$, that is, without $$0$$, but it is not an important distinction.)

Putting the initial conditions aside for a moment, for any recurrence, we can consider the subset $$S$$ of $$V$$ of solutions. For example, without initial conditions, in addition to the function $$f$$ given above, the Fibonacci relation is also solved by the function $$g$$ whose first few values are $$g(0)=1$$, $$g(1)=3$$, $$g(2)=4$$, and $$g(3)=7$$.

The subset $$S$$ is a subspace of $$V$$. It is nonempty because the zero function is a solution. It is closed under addition since if $$f_1$$ and $$f_2$$ are solutions, then

$$
a_{n+1}(f_1+f_2)(n+1)+\dots+a_{n-k}(f_1+f_2)(n-k)
$$

$$
\begin{align} &=(a_{n+1}f_1(n+1)+\dots+a_{n-k}f_1(n-k)) \\ &\quad+(a_{n+1}f_2(n+1)+\dots+a_{n-k}f_2(n-k)) \\ &=0. \end{align}
$$

And, it is closed under scalar multiplication since

$$
a_{n+1}(rf_1)(n+1)+\dots+a_{n-k}(rf_1)(n-k)
$$

$$
\begin{align} &=r(a_{n+1}f_1(n+1)+\dots+a_{n-k}f_1(n-k)) \\ &=r\cdot 0 \\ &=0. \end{align}
$$

We can give the dimension of $$S$$. Consider this map from the set of functions $$S$$ to the set of vectors $$\mathbb{R}^k$$.

$$
f \mapsto \begin{pmatrix} f(0) \\ f(1) \\ \vdots \\ f(k) \end{pmatrix}
$$

Problem 3 shows that this map is linear. Because, as noted above, any solution of the recurrence is uniquely determined by the $$k$$ initial conditions, this map is one-to-one and onto. Thus it is an isomorphism, and thus $$S$$ has dimension $$k$$, the order of the recurrence.

So (again, without any initial conditions), we can describe the set of solutions of any linear homogeneous recurrence relation of degree $$k$$ by taking linear combinations of only $$k$$ linearly independent functions. It remains to produce those functions.

For that, we express the recurrence $$f(n+1)=a_nf(n)+\dots+a_{n-k}f(n-k)$$ with a matrix equation.

$$
\begin{pmatrix} a_n &a_{n-1} &a_{n-2} &\ldots &a_{n-k+1} &a_{n-k} \\ 1 &0 &0 &\ldots &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \\ \vdots &\vdots & &\ddots & &\vdots \\ 0 &0 &0 &\ldots &1 &0 \end{pmatrix} \begin{pmatrix} f(n) \\ f(n-1) \\ \vdots \\ f(n-k) \end{pmatrix} = \begin{pmatrix} f(n+1) \\ f(n) \\ \vdots \\ f(n-k+1) \end{pmatrix}
$$

In trying to find the characteristic function of the matrix, we can see the pattern in the $$2 \! \times \! 2$$ case

$$
\begin{pmatrix} a_n-\lambda &a_{n-1} \\ 1 &-\lambda \end{pmatrix} =\lambda^2-a_n\lambda-a_{n-1}
$$

and $$3 \! \times \! 3$$ case.

$$
\begin{pmatrix} a_n-\lambda &a_{n-1} &a_{n-2} \\ 1 &-\lambda &0 \\ 0 &1 &-\lambda \end{pmatrix} =-\lambda^3+a_n\lambda^2+a_{n-1}\lambda+a_{n-2}
$$

Problem 4 shows that the characteristic equation is this.

$$
\begin{vmatrix} a_n-\lambda &a_{n-1} &a_{n-2} &\ldots &a_{n-k+1} &a_{n-k} \\ 1 &-\lambda &0 &\ldots &0 &0 \\ 0 &1 &-\lambda \\ 0 &0 &1 \\ \vdots &\vdots & &\ddots & &\vdots \\ 0 &0 &0 &\ldots &1 &-\lambda \end{vmatrix}
$$

$$
=\pm(-\lambda^k+a_n\lambda^{k-1}+a_{n-1}\lambda^{k-2} +\dots+a_{n-k+1}\lambda+a_{n-k})
$$

We call that the polynomial "associated" with the recurrence relation. (We will be finding the roots of this polynomial and so we can drop the $$\pm$$ as irrelevant.)

If $$-\lambda^k+a_n\lambda^{k-1}+a_{n-1}\lambda^{k-2} +\dots+a_{n-k+1}\lambda+a_{n-k}$$ has no repeated roots then the matrix is diagonalizable and we can, in theory, get a formula for $$f(n)$$ as in the Fibonacci case. But, because we know that the subspace of solutions has dimension $$k$$, we do not need to do the diagonalization calculation, provided that we can exhibit $$k$$ linearly independent functions satisfying the relation.

Where $$r_1$$, $$r_2$$, ..., $$r_k$$ are the distinct roots, consider the functions $$f_{r_1}(n)=r_1^n$$ through $$f_{r_k}(n)=r_k^n$$ of powers of those roots. Problem 2 shows that each is a solution of the recurrence and that the $$k$$ of them form a linearly independent set. So, given the homogeneous linear recurrence $$f(n+1)=a_nf(n)+\dots+a_{n-k}f(n-k)$$ (that is, $$0=-f(n+1)+a_nf(n)+\dots+a_{n-k}f(n-k)$$) we consider the associated equation $$0=-\lambda^k+a_n\lambda^{k-1}+\dots+a_{n-k+1}\lambda+a_{n-k}$$. We find its roots $$r_1$$, ..., $$r_k$$, and if those roots are distinct then any solution of the relation has the form $$f(n)=c_1r_1^n+c_2r_2^n+\dots+c_kr_k^n$$ for $$c_1, \dots, c_n\in\mathbb{R}$$. (The case of repeated roots is also easily done, but we won't cover it here— see any text on Discrete Mathematics.)

Now, given some initial conditions, so that we are interested in a particular solution, we can solve for $$c_1$$, ..., $$c_n$$. For instance, the polynomial associated with the Fibonacci relation is $$-\lambda^2+\lambda+1$$, whose roots are $$(1\pm\sqrt{5})/2$$ and so any solution of the Fibonacci equation has the form $$f(n)=c_1((1+\sqrt{5})/2)^n+c_2((1-\sqrt{5})/2)^n$$. Including the initial conditions for the cases $$n=0$$ and $$n=1$$ gives

$$
\begin{array}{rcrcr} c_1 &+ &c_2 &= &1 \\ (1+\sqrt{5}/2)c_1 &+ &(1-\sqrt{5}/2)c_2 &= &1 \end{array}
$$

which yields $$c_1=1/\sqrt{5}$$ and $$c_2=-1/\sqrt{5}$$, as was calculated above.

We close by considering the nonhomogeneous case, where the relation has the form $$f(n+1)=a_nf(n)+a_{n-1}f(n-1)+\dots+a_{n-k}f(n-k)+b$$ for some nonzero $$b$$. As in the first chapter of this book, only a small adjustment is needed to make the transition from the homogeneous case. This classic example illustrates.

In 1883, Edouard Lucas posed the following problem.

In the great temple at Benares, beneath the dome which marks the center of the world, rests a brass plate in which are fixed three diamond needles, each a cubit high and as thick as the body of a bee. On one of these needles, at the creation, God placed sixty four disks of pure gold, the largest disk resting on the brass plate, and the others getting smaller and smaller up to the top one. This is the Tower of Bramah. Day and night unceasingly the priests transfer the disks from one diamond needle to another according to the fixed and immutable laws of Bramah, which require that the priest on duty must not move more than one disk at a time and that he must place this disk on a needle so that there is no smaller disk below it. When the sixty-four disks shall have been thus transferred from the needle on which at the creation God placed them to one of the other needles, tower, temple, and Brahmins alike will crumble into dusk, and with a thunderclap the world will vanish.

(Translation of De Parvill (1884) from Ball (1962).)

How many disk moves will it take? Instead of tackling the sixty four disk problem right away, we will consider the problem for smaller numbers of disks, starting with three.

To begin, all three disks are on the same needle.

After moving the small disk to the far needle, the mid-sized disk to the middle needle, and then moving the small disk to the middle needle we have this.

Now we can move the big disk over. Then, to finish, we repeat the process of moving the smaller disks, this time so that they end up on the third needle, on top of the big disk.

So the thing to see is that to move the very largest disk, the bottom disk, at a minimum we must: first move the smaller disks to the middle needle, then move the big one, and then move all the smaller ones from the middle needle to the ending needle. Those three steps give us this recurrence.

$$
T(n+1)=T(n)+1+T(n)=2T(n)+1 \quad \text{where }T(1)=1
$$

We can easily get the first few values of $$T$$.

$$
\begin{array}{r|cccccccccc} n &1 &2 &3 &4 &5 &6 &7 &8 &9 &10 \\ \hline T(n) &1 &3 &7 &15 &31 &63 &127 &255 &511 &1023 \end{array}
$$

We recognize those as being simply one less than a power of two.

To derive this equation instead of just guessing at it, we write the original relation as $$-1=-T(n+1)+2T(n)$$, consider the homogeneous relation $$0=-T(n)+2T(n-1)$$, get its associated polynomial $$-\lambda+2$$, which obviously has the single, unique, root of $$r_1=2$$, and conclude that functions satisfying the homogeneous relation take the form $$T(n)=c_12^n$$.

That's the homogeneous solution. Now we need a particular solution.

Because the nonhomogeneous relation $$-1=-T(n+1)+2T(n)$$ is so simple, in a few minutes (or by remembering the table) we can spot the particular solution $$T(n)=-1$$ (there are other particular solutions, but this one is easily spotted). So we have that— without yet considering the initial condition— any solution of $$T(n+1)=2T(n)+1$$ is the sum of the homogeneous solution and this particular solution: $$T(n)=c_12^n-1$$.

The initial condition $$T(1)=1$$ now gives that $$c_1=1$$, and we've gotten the formula that generates the table: the $$n$$-disk Tower of Hanoi problem requires a minimum of $$2^n-1$$ moves.

Finding a particular solution in more complicated cases is, naturally, more complicated. A delightful and rewarding, but challenging, source on recurrence relations is (Graham, Knuth & Patashnik 1988)., For more on the Tower of Hanoi, (Ball 1962) or (Gardner 1957) are good starting points. So is (Hofstadter 1985). Some computer code for trying some recurrence relations follows the exercises.

### Exercises

**Problem 1**  —

Solve each homogeneous linear recurrence relations.

1. $$f(n+1)=5f(n)-6f(n-1)$$
2. $$f(n+1)=4f(n)$$
3. $$f(n+1)=6f(n)+7f(n-1)+6f(n-2)$$

**Problem 2**  —

Give a formula for the relations of the prior exercise, with these initial conditions.

1. $$f(0)=1$$, $$f(1)=1$$
2. $$f(0)=0$$, $$f(1)=1$$
3. $$f(0)=1$$, $$f(1)=1$$, $$f(2)=3$$.

**Problem 3**  —

Check that the isomorphism given between $$S$$ and $$\mathbb{R}^k$$ is a linear map. It is argued above that this map is one-to-one. What is its inverse?

**Problem 4**  —

Show that the characteristic equation of the matrix is as stated, that is, is the polynomial associated with the relation. (Hint: expanding down the final column, and using induction will work.)

**Problem 5**  —

Given a homogeneous linear recurrence relation $$f(n+1)=a_nf(n)+\dots+a_{n-k}f(n-k)$$, let $$r_1$$, ..., $$r_k$$ be the roots of the associated polynomial.

1. Prove that each function $$f_{r_i}(n)=r_k^n$$ satisfies the recurrence (without initial conditions).
2. Prove that no $$r_i$$ is $$0$$.
3. Prove that the set $$\{f_{r_1},\dots,f_{r_k}\}$$ is linearly independent.

**Problem 6**  —

(This refers to the value $$T(64)=18,446,744,073,709,551,615$$ given in the computer code below.) Transferring one disk per second, how many years would it take the priests at the Tower of Hanoi to finish the job?

**Computer Code**  
This code allows the generation of the first few values of a function defined by a recurrence and initial conditions. It is in the Scheme dialect of LISP (specifically, it was written for A. Jaffer's free scheme interpreter SCM, although it should run in any Scheme implementation).

First, the Tower of Hanoi code is a straightforward implementation of the recurrence.  
```
(define (tower-of-hanoi-moves n)
(if (= n 1)
1
(+ (* (tower-of-hanoi-moves (- n 1))
2)
1) )  )

```  
(Note for readers unused to recursive code: to compute $$T(64)$$, the computer is told to compute $$2*T(63)-1$$, which requires, of course, computing $$T(63)$$. The computer puts the "times $$2$$" and the "plus $$1$$" aside for a moment to do that. It computes $$T(63)$$ by using this same piece of code (that's what "recursive" means), and to do that is told to compute $$2*T(62)-1$$. This keeps up (the next step is to try to do $$T(62)$$ while the other arithmetic is held in waiting), until, after $$63$$ steps, the computer tries to compute $$T(1)$$. It then returns $$T(1)=1$$, which now means that the computation of $$T(2)$$ can proceed, etc., up until the original computation of $$T(64)$$ finishes.)

The next routine calculates a table of the first few values. (Some language notes: '() is the empty list, that is, the empty sequence, and cons pushes something onto the start of a list. Note that, in the last line, the procedure proc is called on argument n.)  
```
(define (first-few-outputs proc n)
(first-few-outputs-helper proc n '()) )
;
(define (first-few-outputs-aux proc n lst)
(if (< n 1)
lst
(first-few-outputs-aux proc (- n 1) (cons (proc n) lst)) ) )

```  
The session at the SCM prompt went like this.  
```
>(first-few-outputs tower-of-hanoi-moves 64)
Evaluation took 120 mSec
(1 3 7 15 31 63 127 255 511 1023 2047 4095 8191 16383 32767
65535 131071 262143 524287 1048575 2097151 4194303 8388607
16777215 33554431 67108863 134217727 268435455 536870911
1073741823 2147483647 4294967295 8589934591 17179869183
34359738367 68719476735 137438953471 274877906943 549755813887
1099511627775 2199023255551 4398046511103 8796093022207
17592186044415 35184372088831 70368744177663 140737488355327
281474976710655 562949953421311 1125899906842623
2251799813685247 4503599627370495 9007199254740991
18014398509481983 36028797018963967 72057594037927935
144115188075855871 288230376151711743 576460752303423487
1152921504606846975 2305843009213693951 4611686018427387903
9223372036854775807 18446744073709551615)

```  
This is a list of $$T(1)$$ through $$T(64)$$. (The $$120$$ mSec came on a 50 mHz '486 running in an XTerm of XWindow under Linux. The session was edited to put line breaks between numbers.)

Solutions

### References

- Ball, W.W. (1962), *Mathematical Recreations and Essays*, MacMillan (revised by H.S.M. Coxeter).
- De Parville (1884), *La Nature*, vol. I, Paris, pp. 285–286{{citation}}: CS1 maint: location missing publisher (link).
- Gardner, Martin (May. 1957), "Mathematical Games: About the remarkable similarity between the Icosian Game and the Tower of Hanoi", *Scientific American*: 150–154 {{citation}}: Check date values in: |year= (help)CS1 maint: year (link).
- Graham, Ronald L.; Knuth, Donald E.; Patashnik, Oren (1988), *Concrete Mathematics*, Addison-Wesley.
- Hofstadter, Douglas R. (1985), *Metamagical Themas:~Questing for the Essence of Mind and Pattern*, Basic Books.

---

*Source: Wikibooks, Linear Algebra/Topic: Linear Recurrences (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Linear_Recurrences), by Wikibooks contributors, CC BY-SA 4.0.*
