# Techniques of Proof

#### Induction

Many proofs are iterative, "Here's why the statement is true for for the case of the number $$1$$, it then follows for $$2$$, and from there to $$3$$, and so on ...". These are called proofs by **induction**. Such a proof has two steps. In the **base step** the proposition is established for some first number, often $$0$$ or $$1$$. Then in the **inductive step** we assume that the proposition holds for numbers up to some $$k$$ and deduce that it then holds for the next number $$k+1$$.

Here is an example.

We will prove that $$1+2+3+\dots+n=n(n+1)/2$$.

For the base step we must show that the formula holds when $$n=1$$. That's easy, the sum of the first $$1$$ number does indeed equal $$1(1+1)/2$$.

For the inductive step, assume that the formula holds for the numbers $$1,2,\ldots,k$$. That is, assume all of these instances of the formula.

$$
\begin{array}{rl} 1 &=1(1+1)/2 \\ \text{and}\quad 1+2 &=2(2+1)/2 \\ \text{and}\quad 1+2+3 &=3(3+1)/2 \\ &\vdots \\ \text{and}\quad 1+\dots+k &=k(k+1)/2 \end{array}
$$

From this assumption we will deduce that the formula therefore also holds in the $$k+1$$ next case. The deduction is straightforward algebra.

$$
1+2+\cdots+k+(k+1) = \frac{k(k+1)}{2}+(k+1) = \frac{(k+1)(k+2)}{2}
$$

We've shown in the base case that the above proposition holds for $$1$$. We've shown in the inductive step that if it holds for the case of $$1$$ then it also holds for $$2$$; therefore it does hold for $$2$$. We've also shown in the inductive step that if the statement holds for the cases of $$1$$ and $$2$$ then it also holds for the next case $$3$$, etc. Thus it holds for any natural number greater than or equal to $$1$$.

Here is another example.

We will prove that every integer greater than $$1$$ is a product of primes.

The base step is easy: $$2$$ is the product of a single prime.

For the inductive step assume that each of $$2, 3,\ldots ,k$$ is a product of primes, aiming to show $$k+1$$ is also a product of primes. There are two possibilities: (i) if $$k+1$$ is not divisible by a number smaller than itself then it is a prime and so is the product of primes, and (ii) if $$k+1$$ is divisible then its factors can be written as a product of primes (by the inductive hypothesis) and so $$k+1$$ can be rewritten as a product of primes. That ends the proof.

(*Remark.* The Prime Factorization Theorem of Number Theory says that not only does a factorization exist, but that it is unique. We've shown the easy half.)

There are two things to note about the "next number" in an induction argument.

For one thing, while induction works on the integers, it's no good on the reals. There is no "next" real.

The other thing is that we sometimes use induction to go down, say, from $$10$$ to $$9$$ to $$8$$, etc., down to $$0$$. So "next number" could mean "next lowest number". Of course, at the end we have not shown the fact for all natural numbers, only for those less than or equal to $$10$$.

#### Contradiction

Another technique of proof is to show something is true by showing it can't be false.

The classic example is Euclid's, that there are infinitely many primes.

Suppose there are only finitely many primes $$p_1,\dots,p_k$$. Consider $$p_1\cdot p_2\dots p_k +1$$. None of the primes on this supposedly exhaustive list divides that number evenly, each leaves a remainder of $$1$$. But every number is a product of primes so this can't be. Thus there cannot be only finitely many primes.

Every proof by contradiction has the same form: **assume** that **the false** proposition **istrue** and **derive** some **contradiction** to known facts. This kind of logic is known as Aristotelian Logic, or Term Logic

Another example is this proof that $$\sqrt{2}$$ is not a rational number.

Suppose that $$\sqrt{2}=m/n$$.

$$
2n^2=m^2
$$

Factor out the $$2$$'s: $$n=2^{k_n}\cdot \hat{n}$$ and $$m=2^{k_m}\cdot \hat{m}$$ and rewrite.

$$
2\cdot (2^{k_n}\cdot \hat{n})^2 = (2^{k_m}\cdot \hat{m})^2
$$

The Prime Factorization Theorem says that there must be the same number of factors of $$2$$ on both sides, but there are an odd number $$1+2k_n$$ on the left and an even number $$2k_m$$ on the right. That's a contradiction, so a rational with a square of $$2$$ cannot be.

Both of these examples aimed to prove something doesn't exist. A negative proposition often suggests a proof by contradiction.

---

*Source: Wikibooks, Linear Algebra/Techniques of Proof (https://en.wikibooks.org/wiki/Linear_Algebra/Techniques_of_Proof), by Wikibooks contributors, CC BY-SA 4.0.*
