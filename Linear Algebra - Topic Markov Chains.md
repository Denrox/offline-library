# Topic: Markov Chains

Here is a simple game: a player bets on coin tosses, a dollar each time, and the game ends either when the player has no money left or is up to five dollars. If the player starts with three dollars, what is the chance that the game takes at least five flips? Twenty-five flips?

At any point, this player has either $0, or $1, ..., or $5. We say that the player is in the **state** $$s_0$$, $$s_1$$, ..., or $$s_5$$. A game consists of moving from state to state. For instance, a player now in state $$s_3$$ has on the next flip a $$0.5$$ chance of moving to state $$s_2$$ and a $$0.5$$ chance of moving to $$s_4$$. The boundary states are a bit different; once in state $$s_0$$ or stat $$s_5$$, the player never leaves.

Let $$p_{i}(n)$$ be the probability that the player is in state $$s_i$$ after $$n$$ flips. Then, for instance, we have that the probability of being in state $$s_0$$ after flip $$n+1$$ is $$p_{0}(n+1)=p_{0}(n)+0.5\cdot p_{1}(n)$$. This matrix equation summarizes.  

$$
\begin{pmatrix} 1 &0.5 &0 &0 &0 &0 \\ 0.5 &0 &0.5 &0 &0 &0 \\ 0 &0.5 &0 &0.5 &0 &0 \\ 0 &0 &0.5 &0 &0.5 &0 \\ 0 &0 &0 &0.5 &0 &0.5 \\ 0 &0 &0 &0 &0.5 &1 \end{pmatrix} \begin{pmatrix} p_{0}(n) \\ p_{1}(n) \\ p_{2}(n) \\ p_{3}(n) \\ p_{4}(n) \\ p_{5}(n) \end{pmatrix} =\begin{pmatrix} p_{0}(n+1) \\ p_{1}(n+1) \\ p_{2}(n+1) \\ p_{3}(n+1) \\ p_{4}(n+1) \\ p_{5}(n+1) \end{pmatrix}
$$

With the initial condition that the player starts with three dollars, calculation gives this.

- $$n=0$$   $$n=1$$   $$n=2$$   $$n=3$$   $$n=4$$   $$\cdots$$   $$n=24$$
- $$\begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}$$   $$\begin{pmatrix} 0 \\ 0 \\ 0.5 \\ 0 \\ 0.5 \\ 0 \end{pmatrix}$$   $$\begin{pmatrix} 0 \\ 0.25 \\ 0 \\ 0.5 \\ 0 \\ 0.25 \end{pmatrix}$$   $$\begin{pmatrix} 0.125 \\ 0 \\ 0.375 \\ 0 \\ 0.25 \\ 0.25 \end{pmatrix}$$   $$\begin{pmatrix} 0.125 \\ 0.1875 \\ 0 \\ 0.3125 \\ 0 \\ 0.375 \end{pmatrix}$$   $$\cdots$$   $$\begin{pmatrix} 0.39600 \\ 0.00276 \\ 0 \\ 0.00447 \\ 0 \\ 0.59676 \end{pmatrix}$$

As this computational exploration suggests, the game is not likely to go on for long, with the player quickly ending in either state $$s_0$$ or state $$s_5$$. For instance, after the fourth flip there is a probability of $$0.50$$ that the game is already over. (Because a player who enters either of the boundary states never leaves, they are said to be **absorbing**.)

This game is an example of a **Markov chain**, named for A.A. Markov, who worked in the first half of the 1900's. Each vector of $$p$$'s is a **probability vector** and the matrix is a **transition matrix**. The notable feature of a Markov chain model is that it is **historyless** in that with a fixed transition matrix, the next state depends only on the current state, not on any prior states. Thus a player, say, who arrives at $$s_2$$ by starting in state $$s_3$$, then going to state $$s_2$$, then to $$s_1$$, and then to $$s_2$$ has at this point exactly the same chance of moving next to state $$s_3$$ as does a player whose history was to start in $$s_3$$, then go to $$s_4$$, and to $$s_3$$, and then to $$s_2$$.

Here is a Markov chain from sociology. A study (Macdonald & Ridge 1988, p. 202) divided occupations in the United Kingdom into upper level (executives and professionals), middle level (supervisors and skilled manual workers), and lower level (unskilled). To determine the mobility across these levels in a generation, about two thousand men were asked, "At which level are you, and at which level was your father when you were fourteen years old?" This equation summarizes the results.

$$
\begin{pmatrix} 0.60 & 0.29 & 0.16 \\ 0.26 & 0.37 & 0.27 \\ 0.14 & 0.34 & 0.57 \end{pmatrix} \begin{pmatrix} p_{U}(n) \\ p_{M}(n) \\ p_{L}(n) \end{pmatrix} =\begin{pmatrix} p_{U}(n+1) \\ p_{M}(n+1) \\ p_{L}(n+1) \end{pmatrix}
$$

For instance, a child of a lower class worker has a $$.27$$ probability of growing up to be middle class. Notice that the Markov model assumption about history seems reasonable— we expect that while a parent's occupation has a direct influence on the occupation of the child, the grandparent's occupation has no such direct influence. With the initial distribution of the respondents's fathers given below, this table lists the distributions for the next five generations.

- $$n=0$$   $$n=1$$   $$n=2$$   $$n=3$$   $$n=4$$   $$n=5$$
- $$\begin{pmatrix} 0.12 \\ 0.32 \\ 0.56 \end{pmatrix}$$   $$\begin{pmatrix} 0.23 \\ 0.34 \\ 0.42 \end{pmatrix}$$   $$\begin{pmatrix} 0.29 \\ 0.34 \\ 0.37 \end{pmatrix}$$   $$\begin{pmatrix} 0.31 \\ 0.34 \\ 0.35 \end{pmatrix}$$   $$\begin{pmatrix} 0.32 \\ 0.33 \\ 0.34 \end{pmatrix}$$   $$\begin{pmatrix} 0.33 \\ 0.33 \\ 0.34 \end{pmatrix}$$

One more example, from a very important subject, indeed. The World Series of American baseball is played between the team winning the American League and the team winning the National League (we follow [Brunner] but see also [Woodside]). The series is won by the first team to win four games. That means that a series is in one of twenty-four states: 0-0 (no games won yet by either team), 1-0 (one game won for the American League team and no games for the National League team), etc. If we assume that there is a probability $$p$$ that the American League team wins each game then we have the following transition matrix.

$$
\begin{pmatrix} 0 &0 &0 &0 &\ldots \\ p &0 &0 &0 &\ldots \\ 1-p &0 &0 &0 &\ldots \\ 0 &p &0 &0 &\ldots \\ 0 &1-p &p &0 &\ldots \\ 0 &0 &1-p &0 &\ldots \\ \vdots &\vdots &\vdots &\vdots \end{pmatrix} \begin{pmatrix} p_{\text{0-0}}(n) \\ p_{\text{1-0}}(n) \\ p_{\text{0-1}}(n) \\ p_{\text{2-0}}(n) \\ p_{\text{1-1}}(n) \\ p_{\text{0-2}}(n) \\ \vdots \end{pmatrix} = \begin{pmatrix} p_{\text{0-0}}(n+1) \\ p_{\text{1-0}}(n+1) \\ p_{\text{0-1}}(n+1) \\ p_{\text{2-0}}(n+1) \\ p_{\text{1-1}}(n+1) \\ p_{\text{0-2}}(n+1) \\ \vdots \end{pmatrix}
$$

An especially interesting special case is $$p=0.50$$; this table lists the resulting components of the $$n=0$$ through $$n=7$$ vectors. (The code to generate this table in the computer algebra system Octave follows the exercises.)

- $$n=0$$   $$n=1$$   $$n=2$$   $$n=3$$   $$n=4$$   $$n=5$$   $$n=6$$   $$n=7$$
- 0-0   1   0   0   0   0   0   0   0
- 1-0   0   0.5   0   0   0   0   0   0
- 0-1   0   0.5   0   0   0   0   0   0
- 2-0   0   0   0.25   0   0   0   0   0
- 1-1   0   0   0.5   0   0   0   0   0
- 0-2   0   0   0.25   0   0   0   0   0
- 3-0   0   0   0   0.125   0   0   0   0
- 2-1   0   0   0   0.325   0   0   0   0
- 1-2   0   0   0   0.325   0   0   0   0
- 0-3   0   0   0   0.125   0   0   0   0
- 4-0   0   0   0   0   0.0625   0.0625   0.0625   0.0625
- 3-1   0   0   0   0   0.25   0   0   0
- 2-2   0   0   0   0   0.375   0   0   0
- 1-3   0   0   0   0   0.25   0   0   0
- 0-4   0   0   0   0   0.0625   0.0625   0.0625   0.0625
- 4-1   0   0   0   0   0   0.125   0.125   0.125
- 3-2   0   0   0   0   0   0.3125   0   0
- 2-3   0   0   0   0   0   0.3125   0   0
- 1-4   0   0   0   0   0   0.125   0.125   0.125
- 4-2   0   0   0   0   0   0   0.15625   0.15625
- 3-3   0   0   0   0   0   0   0.3125   0
- 2-4   0   0   0   0   0   0   0.15625   0.15625
- 4-3   0   0   0   0   0   0   0   0.15625
- 3-4   0   0   0   0   0   0   0   0.15625

Note that evenly-matched teams are likely to have a long series— there is a probability of $$0.625$$ that the series goes at least six games.

One reason for the inclusion of this Topic is that Markov chains are one of the most widely-used applications of matrix operations. Another reason is that it provides an example of the use of matrices where we do not consider the significance of the maps represented by the matrices. For more on Markov chains, there are many sources such as (Kemeny & Snell 1960) and (Iosifescu 1980).

### Exercises

*Use a computer for these problems. You can, for instance, adapt the Octave script given below.*

**Problem 1**  —

These questions refer to the coin-flipping game.

1. Check the computations in the table at the end of the first paragraph.
2. Consider the second row of the vector table. Note that this row has alternating $$0$$'s. Must $$p_{1}(j)$$ be $$0$$ when $$j$$ is odd? Prove that it must be, or produce a counterexample.
3. Perform a computational experiment to estimate the chance that the player ends at five dollars, starting with one dollar, two dollars, and four dollars.

**Problem 2**  —

We consider throws of a die, and say the system is in state $$s_i$$ if the largest number yet appearing on the die was $$i$$.

1. Give the transition matrix.
2. Start the system in state $$s_1$$, and run it for five throws. What is the vector at the end?

(Feller 1968, p. 424)

**Problem 3**  —

There has been much interest in whether industries in the United States are moving from the Northeast and North Central regions to the South and West, motivated by the warmer climate, by lower wages, and by less unionization. Here is the transition matrix for large firms in Electric and Electronic Equipment (Kelton 1983, p. 43)

- *NE*   *NC*   *S*   *W*   *Z*
- *NE*   0.787   0   0   0.111   0.102
- *NC*   0   0.966   0.034   0   0
- *S*   0   0.063   0.937   0   0
- *W*   0   0   0.074   0.612   0.314
- *Z*   0.021   0.009   0.005   0.010   0.954

For example, a firm in the Northeast region will be in the West region next year with probability $$0.111$$. (The *Z* entry is a "birth-death" state. For instance, with probability $$0.102$$ a large Electric and Electronic Equipment firm from the Northeast will move out of this system next year: go out of business, move abroad, or move to another category of firm. There is a $$0.021$$ probability that a firm in the *National Census of Manufacturers* will move into Electronics, or be created, or move in from abroad, into the Northeast. Finally, with probability $$0.954$$ a firm out of the categories will stay out, according to this research.)

1. Does the Markov model assumption of lack of history seem justified?
2. Assume that the initial distribution is even, except that the value at $$Z$$ is $$0.9$$. Compute the vectors for $$n=1$$ through $$n=4$$.
3. Suppose that the initial distribution is this.

- *NE*   *NC*   *S*   *W*   *Z*
- 0.0000   0.6522   0.3478   0.0000   0.0000

Calculate the distributions for $$n=1$$ through $$n=4$$.

4. Find the distribution for $$n=50$$ and $$n=51$$. Has the system settled down to an equilibrium?

**Problem 4**  —

This model has been suggested for some kinds of learning (Wickens 1982, p. 41). The learner starts in an undecided state $$s_U$$. Eventually the learner has to decide to do either response $$A$$ (that is, end in state $$s_A$$) or response $$B$$ (ending in $$s_B$$). However, the learner doesn't jump right from being undecided to being sure $$A$$ is the correct thing to do (or $$B$$). Instead, the learner spends some time in a "tentative-$$A$$" state, or a "tentative-$$B$$" state, trying the response out (denoted here $$t_A$$ and $$t_B$$). Imagine that once the learner has decided, it is final, so once $$s_A$$ or $$s_B$$ is entered it is never left. For the other state changes, imagine a transition is made with probability $$p$$ in either direction.

1. Construct the transition matrix.
2. Take $$p=0.25$$ and take the initial vector to be $$1$$ at $$s_U$$. Run this for five steps. What is the chance of ending up at $$s_A$$?
3. Do the same for $$p=0.20$$.
4. Graph $$p$$ versus the chance of ending at $$s_A$$. Is there a threshold value for $$p$$, above which the learner is almost sure not to take longer than five steps?

**Problem 5**  —

A certain town is in a certain country (this is a hypothetical problem). Each year ten percent of the town dwellers move to other parts of the country. Each year one percent of the people from elsewhere move to the town. Assume that there are two states $$s_T$$, living in town, and $$s_C$$, living elsewhere.

1. Construct the transistion matrix.
2. Starting with an initial distribution $$s_T=0.3$$ and $$s_C=0.7$$, get the results for the first ten years.
3. Do the same for $$s_T=0.2$$.
4. Are the two outcomes alike or different?

**Problem 6**  —

For the World Series application, use a computer to generate the seven vectors for $$p=0.55$$ and $$p=0.6$$.

1. What is the chance of the National League team winning it all, even though they have only a probability of $$0.45$$ or $$0.40$$ of winning any one game?
2. Graph the probability $$p$$ against the chance that the American League team wins it all. Is there a threshold value— a $$p$$ above which the better team is essentially ensured of winning?

(Some sample code is included below.)

**Problem 7**  —

A **Markov matrix** has each entry positive and each column sums to $$1$$.

1. Check that the three transistion matrices shown in this Topic meet these two conditions. Must any transition matrix do so?
2. Observe that if $$A\vec{v}_0=\vec{v}_1$$ and $$A\vec{v}_1=\vec{v}_2$$ then $$A^2$$ is a transition matrix from $$\vec{v}_0$$ to $$\vec{v}_2$$. Show that a power of a Markov matrix is also a Markov matrix.
3. Generalize the prior item by proving that the product of two appropriately-sized Markov matrices is a Markov matrix.

Solutions

** Computer Code **

This script *markov.m* for the computer algebra system Octave was used to generate the table of World Series outcomes. (The sharp character # marks the rest of a line as a comment.)

```
# Octave script file to compute chance of World Series outcomes.
function w = markov(p,v)
q = 1-p;
A=[0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 0-0
p,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 1-0
q,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 0-1_
0,p,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 2-0
0,q,p,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 1-1
0,0,q,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 0-2__
0,0,0,p,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 3-0
0,0,0,q,p,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 2-1
0,0,0,0,q,p, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 1-2_
0,0,0,0,0,q, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 0-3
0,0,0,0,0,0, p,0,0,0,1,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 4-0
0,0,0,0,0,0, q,p,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 3-1__
0,0,0,0,0,0, 0,q,p,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 2-2
0,0,0,0,0,0, 0,0,q,p,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0;  # 1-3
0,0,0,0,0,0, 0,0,0,q,0,0, 0,0,1,0,0,0, 0,0,0,0,0,0;  # 0-4_
0,0,0,0,0,0, 0,0,0,0,0,p, 0,0,0,1,0,0, 0,0,0,0,0,0;  # 4-1
0,0,0,0,0,0, 0,0,0,0,0,q, p,0,0,0,0,0, 0,0,0,0,0,0;  # 3-2
0,0,0,0,0,0, 0,0,0,0,0,0, q,p,0,0,0,0, 0,0,0,0,0,0;  # 2-3__
0,0,0,0,0,0, 0,0,0,0,0,0, 0,q,0,0,0,0, 1,0,0,0,0,0;  # 1-4
0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,p,0, 0,1,0,0,0,0;  # 4-2
0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,q,p, 0,0,0,0,0,0;  # 3-3_
0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,q, 0,0,0,1,0,0;  # 2-4
0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,p,0,1,0;  # 4-3
0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,q,0,0,1]; # 3-4
w = A * v;
endfunction

```

Then the Octave session was this.

```
> v0=[1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0]
> p=.5
> v1=markov(p,v0)
> v2=markov(p,v1)
...

```

Translating to another computer algebra system should be easy— all have commands similar to these.

### References

- Feller, William (1968), *An Introduction to Probability Theory and Its Applications*, vol. 1 (3rd ed.), Wiley.
- Iosifescu, Marius (1980), *Finite Markov Processes and Their Applications*, UMI Research Press.
- Kelton, Christina M.L. (1983), *Trends on the Relocation of U.S. Manufacturing*, Wiley.
- Kemeny, John G.; Snell, J. Laurie (1960), *Finite Markove Chains*, D.~Van Nostrand.
- Macdonald, Kenneth; Ridge, John (1988), "Social Mobility", *British Social Trends Since 1900*, Macmillian.
- Wickens, Thomas D. (1982), *Models for Behavior*, W.H. Freeman.

---

*Source: Wikibooks, Linear Algebra/Topic: Markov Chains (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Markov_Chains), by Wikibooks contributors, CC BY-SA 4.0.*
