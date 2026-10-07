# Propositions

The point at issue in an argument is the **proposition**. Mathematicians usually write the point in full before the proof and label it either **Theorem** for major points, **Corollary** for points that follow immediately from a prior one, or **Lemma** for results chiefly used to prove other results.

The statements expressing propositions can be complex, with many subparts. The truth or falsity of the entire proposition depends both on the truth value of the parts, and on the words used to assemble the statement from its parts.

#### Not

For example, where $$P$$ is a proposition, "it is not the case that $$P$$" is true provided that $$P$$ is false. Thus, "$$n$$ is not prime" is true only when $$n$$ is the product of smaller integers.

We can picture the "not" operation with a **Venn diagram**.

Where the box encloses all natural numbers, and inside the circle are the primes, the shaded area holds numbers satisfying "not $$P$$".

To prove that a "not $$P$$" statement holds, show that $$P$$ is false.

#### And

Consider the statement form "$$P$$ and $$Q$$". For the statement to be true both halves must hold: "$$7$$ is prime and so is $$3$$" is true, while "$$7$$ is prime and $$3$$ is not" is false.

Here is the Venn diagram for "$$P$$ and $$Q$$".

To prove "$$P$$ and $$Q$$", prove that each half holds.

#### Or

A "$$P$$ or $$Q$$" is true when either half holds: "$$7$$ is prime or $$4$$ is prime" is true, while "$$7$$ is not prime or $$4$$ is prime" is false. We take "or" inclusively so that if both halves are true "$$7$$ is prime or $$4$$ is not" then the statement as a whole is true. (In everyday speech, sometimes "or" is meant in an exclusive way— "Eat your vegetables or no dessert" does not intend both halves to hold— but we will not use "or" in that way.)

The Venn diagram for "or" includes all of both circles.

To prove "$$P$$ or $$Q$$", show that in all cases at least one half holds (perhaps sometimes one half and sometimes the other, but always at least one).

#### If-then

An "if $$P$$ then $$Q$$" statement (sometimes written "$$P$$ materially implies $$Q$$" or just "$$P$$ implies $$Q$$" or "$$P\implies Q$$") is true unless $$P$$ is true while $$Q$$ is false. Thus "if $$7$$ is prime then $$4$$ is not" is true while "if $$7$$ is prime then $$4$$ is also prime" is false. (Contrary to its use in casual speech, in mathematics "if $$P$$ then $$Q$$" does not connote that $$P$$ precedes $$Q$$ or causes $$Q$$.)

More subtly, in mathematics "if $$P$$ then $$Q$$" is true when $$P$$ is false: "if $$4$$ is prime then $$7$$ is prime" and "if $$4$$ is prime then $$7$$ is not" are both true statements, sometimes said to be **vacuously true**. We adopt this convention because we want statements like "if a number is a perfect square then it is not prime" to be true, for instance when the number is $$5$$ or when the number is $$6$$.

The diagram

shows that $$Q$$ holds whenever $$P$$ does (another phrasing is "$$P$$ is sufficient to give $$Q$$"). Notice again that if $$P$$ does not hold, $$Q$$ may or may not be in force.

There are two main ways to establish an implication. The first way is direct: assume that $$P$$ is true and, using that assumption, prove $$Q$$. For instance, to show "if a number is divisible by 5 then twice that number is divisible by 10", assume that the number is $$5n$$ and deduce that $$2(5n)=10n$$. The second way is indirect: prove the **contrapositive** statement: "if $$Q$$ is false then $$P$$ is false" (rephrased, "$$Q$$ can only be false when $$P$$ is also false"). As an example, to show "if a number is prime then it is not a perfect square", argue that if it were a square $$p=n^2$$ then it could be factored $$p=n\cdot n$$ where $$n<p$$ and so wouldn't be prime (of course $$p=0$$ or $$p=1$$ don't give $$n<p$$ but they are nonprime by definition).

Note two things about this statement form.

First, an "if $$P$$ then $$Q$$" result can sometimes be improved by weakening $$P$$ or strengthening $$Q$$. Thus, "if a number is divisible by $$p^2$$ then its square is also divisible by $$p^2$$" could be upgraded either by relaxing its hypothesis: "if a number is divisible by $$p$$ then its square is divisible by $$p^2$$", or by tightening its conclusion: "if a number is divisible by $$p^2$$ then its square is divisible by $$p^4$$".

Second, after showing "if $$P$$ then $$Q$$", a good next step is to look into whether there are cases where $$Q$$ holds but $$P$$ does not. The idea is to better understand the relationship between $$P$$ and $$Q$$, with an eye toward strengthening the proposition.

#### Equivalence

An if-then statement cannot be improved when not only does $$P$$ imply $$Q$$, but also $$Q$$ implies $$P$$. Some ways to say this are: "$$P$$ if and only if $$Q$$", "$$P$$ iff $$Q$$", "$$P$$ and $$Q$$ are logically equivalent", "$$P$$ is necessary and sufficient to give $$Q$$", "$$P\iff Q$$". For example, "a number is divisible by a prime if and only if that number squared is divisible by the prime squared".

The picture here shows that $$P$$ and $$Q$$ hold in exactly the same cases.

Although in simple arguments a chain like "$$P$$ if and only if $$R$$, which holds if and only if $$S$$ ..." may be practical, typically we show equivalence by showing the "if $$P$$ then $$Q$$" and "if $$Q$$ then $$P$$" halves separately.

---

*Source: Wikibooks, Linear Algebra/Propositions (https://en.wikibooks.org/wiki/Linear_Algebra/Propositions), by Wikibooks contributors, CC BY-SA 4.0.*
