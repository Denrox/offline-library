# Quantifiers

Compare these two statements about natural numbers: "there is an $$x$$ such that $$x$$ is divisible by $$x^2$$" is true, while "for all numbers $$x$$, that $$x$$ is divisible by $$x^2$$" is false. We call the "there is" and "for all" prefixes **quantifiers**.

#### For all

The "for all" prefix is the **universal quantifier**, symbolized $$\forall$$.

Venn diagrams aren't very helpful with quantifiers, but in a sense the box we draw to border the diagram shows the universal quantifier since it delineates the universe of possible members.

To prove that a statement holds in all cases, we must show that it holds in each case. Thus, to prove "every number divisible by $$p$$ has its square divisible by $$p^2$$", take a single number of the form $$pn$$ and square it $$(pn)^2=p^2n^2$$. This is a "typical element" or "generic element" proof.

This kind of argument requires that we are careful to not assume properties for that element other than those in the hypothesis— for instance, this type of wrong argument is a common mistake: "if $$n$$ is divisible by a prime, say $$2$$, so that $$n=2k$$ then $$n^2=(2k)^2=4k^2$$ and the square of the number is divisible by the square of the prime". That is an argument about the case $$p=2$$, but it isn't a proof for general $$p$$.

#### There exists

We will also use the **existential quantifier**, symbolized $$\exists$$ and read "there exists".

As noted above, Venn diagrams are not much help with quantifiers, but a picture of "there is a number such that $$P$$" would show both that there can be more than one and that not all numbers need satisfy $$P$$.

An existence proposition can be proved by producing something satisfying the property: once, to settle the question of primality of $$2^{2^5}+1$$, Euler produced its divisor $$641$$. But there are proofs showing that something exists without saying how to find it; Euclid's argument given in the next subsection shows there are infinitely many primes without naming them. In general, while demonstrating existence is better than nothing, giving an example is better, and an exhaustive list of all instances is great. Still, mathematicians take what they can get.

Finally, along with "Are there any?" we often ask "How many?" That is why the issue of uniqueness often arises in conjunction with questions of existence. Many times the two arguments are simpler if separated, so note that just as proving something exists does not show it is unique, neither does proving something is unique show that it exists. (Obviously "the natural number with more factors than any other" would be unique, but in fact no such number exists.)

---

*Source: Wikibooks, Linear Algebra/Quantifiers (https://en.wikibooks.org/wiki/Linear_Algebra/Quantifiers), by Wikibooks contributors, CC BY-SA 4.0.*
