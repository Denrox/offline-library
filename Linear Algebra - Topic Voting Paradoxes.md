# Topic: Voting Paradoxes

Imagine that a Political Science class studying the American presidential process holds a mock election. Members of the class are asked to rank, from most preferred to least preferred, the nominees from the Democratic Party, the Republican Party, and the Third Party, and this is the result ($$>$$ means "is preferred to").

- Preference order    Number with  
that preference
- Democrat > Republican > Third    5
- Democrat > Third > Republican    4
- Republican > Democrat > Third    2
- Republican > Third > Democrat    8
- Third > Democrat > Republican    8
- Third > Republican > Democrat    2
- Total    29

What is the preference of the group as a whole?

Overall, the group prefers the Democrat to the Republican by five votes; seventeen voters ranked the Democrat above the Republican versus twelve the other way. And, overall, the group prefers the Republican to the Third's nominee, fifteen to fourteen. But, strangely enough, the group also prefers the Third to the Democrat, eighteen to eleven.

‎

This is an example of a **voting paradox**, specifically, a **majority cycle**.

Voting paradoxes are studied in part because of their implications for practical politics. For instance, the instructor can manipulate the class into choosing the Democrat as the overall winner by first asking the class to choose between the Republican and the Third, and then asking the class to choose between the winner of that contest, the Republican, and the Democrat. By similar manipulations, any of the other two candidates can be made to come out as the winner. (In this Topic we will stick to three-candidate elections, but similar results apply to larger elections.)

Voting paradoxes are also studied simply because they are mathematically interesting. One interesting aspect is that the group's overall majority cycle occurs despite that each single voters's preference list is **rational**— in a straight-line order. That is, the majority cycle seems to arise in the aggregate, without being present in the elements of that aggregate, the preference lists. Recently, however, linear algebra has been used (Zwicker 1991) to argue that a tendency toward cyclic preference is actually present in each voter's list, and that it surfaces when there is more adding of the tendency than cancelling.

For this argument, abbreviating the choices as $$D$$, $$R$$, and $$T$$, we can describe how a voter with preference order $$D>R>T$$ contributes to the above cycle.

(The negative sign is here because the arrow describes $$T$$ as preferred to $$D$$, but this voter likes them the other way.) The descriptions for the other preference lists are in the *Voting preferences* table below.

Now, to conduct the election we linearly combine these descriptions; for instance, the Political Science mock election  
$$5\cdot\,$$ $$\,+4\cdot\,$$ $$\,+\cdots+2\cdot\,$$

yields the circular group preference shown earlier.

Of course, taking linear combinations is linear algebra. The above cycle notation is suggestive but inconvienent, so we temporarily switch to using column vectors by starting at the $$D$$ and taking the numbers from the cycle in counterclockwise order. Thus, the mock election and a single $$D>R>T$$ vote are represented in this way.

$$
\begin{pmatrix} 7 \\ 1 \\ 5 \end{pmatrix} \quad\text{and}\quad \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}
$$

We will decompose vote vectors into two parts, one cyclic and the other acyclic. For the first part, we say that a vector is **purely cyclic** if it is in this subspace of $$\mathbb{R}^3$$.

$$
C =\left\{\begin{pmatrix} k \\ k \\ k \end{pmatrix} \,\big|\, k \in\mathbb{R}\right\} =\left\{k\cdot\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \,\big|\, k \in\mathbb{R}\right\}
$$

For the second part, consider the subspace (see Problem 6) of vectors that are perpendicular to all of the vectors in $$C$$.

$$
C^\perp =\left\{\begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix} \,\big|\, \begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix}\cdot\begin{pmatrix} k \\ k \\ k \end{pmatrix} =0 \text{ for all } k\in\mathbb{R}\right\}
$$

$$
=\left\{\begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix} \,\big|\, c_1+c_2+c_3=0\right\} =\left\{c_2\begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix} +c_3\begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} \,\big|\, c_2,c_3\in\mathbb{R}\right\}
$$

(Read that aloud as "$$C$$ perp".) So we are led to this basis for $$\mathbb{R}^3$$.

$$
\left\langle \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} \right\rangle
$$

We can represent votes with respect to this basis, and thereby decompose them into a cyclic part and an acyclic part. *(Note for readers who have covered the optional section in this chapter: that is, the space is the direct sum of $$C$$ and $$C^\perp$$.)*

For example, consider the $$D>R>T$$ voter discussed above. The representation in terms of the basis is easily found,

$$
\begin{array}{rcl} \begin{array}{rcrcrcr} c_1 &- &c_2 &- &c_3 &= &-1 \\ c_1 &+ &c_2 & & &= &1 \\ c_1 & & &+ &c_3 &= &1 \end{array} &\xrightarrow[-\rho_1+\rho_3]{-\rho_1+\rho_2}\; \xrightarrow[]{(-1/2)\rho_2+\rho_3} &\begin{array}{rcrcrcr} c_1 &- &c_2 &- &c_3 &= &-1 \\ & &2c_2 &+ &c_3 &= &2 \\ & & & &(3/2)c_3 &= &1 \end{array} \end{array}
$$

so that $$c_1=1/3$$, $$c_2=2/3$$, and $$c_3=2/3$$. Then

$$
\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix} =\frac{1}{3}\cdot\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} +\frac{2}{3}\cdot\begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix} +\frac{2}{3}\cdot\begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} =\begin{pmatrix} 1/3 \\ 1/3 \\ 1/3 \end{pmatrix} +\begin{pmatrix} -4/3 \\ 2/3 \\ 2/3 \end{pmatrix}
$$

gives the desired decomposition into a cyclic part and an acyclic part.  
$$\,=\,$$ $$\,+\,$$

Thus, this $$D>R>T$$ voter's rational preference list can indeed be seen to have a cyclic part.

The $$T>R>D$$ voter is opposite to the one just considered in that the "$$>$$" symbols are reversed. This voter's decomposition

$$\,=\,$$ $$\,+\,$$

shows that these opposite preferences have decompositions that are opposite. We say that the first voter has positive **spin** since the cycle part is with the direction we have chosen for the arrows, while the second voter's spin is negative.

The fact that that these opposite voters cancel each other is reflected in the fact that their vote vectors add to zero. This suggests an alternate way to tally an election. We could first cancel as many opposite preference lists as possible, and then determine the outcome by adding the remaining lists.

The rows of the table below contain the three pairs of opposite preference lists. The columns group those pairs by spin. For instance, the first row contains the two voters just considered.

Voting preferences
- positive sign   negative spin
- Democrat > Republican > Third  
$$\,=\,$$ $$\,+\,$$

Third > Republican > Democrat  
$$\,=\,$$ $$\,+\,$$

- Republican > Third > Democrat  
$$\,=\,$$ $$\,+\,$$

Democrat > Third > Republican  
$$\,=\,$$ $$\,+\,$$

- Third > Democrat > Republican  
$$\,=\,$$ $$\,+\,$$

Republican > Democrat > Third  
$$\,=\,$$ $$\,+\,$$

If we conduct the election as just described then after the cancellation of as many opposite pairs of voters as possible, there will be left three sets of preference lists, one set from the first row, one set from the second row, and one set from the third row. We will finish by proving that a voting paradox can happen only if the spins of these three sets are in the same direction. That is, for a voting paradox to occur, the three remaining sets must all come from the left of the table or all come from the right (see Problem 3). This shows that there is some connection between the majority cycle and the decomposition that we are using---a voting paradox can happen only when the tendencies toward cyclic preference reinforce each other.

For the proof, assume that opposite preference orders have been cancelled, and we are left with one set of preference lists from each of the three rows. Consider the sum of these three (here, the numbers $$a$$, $$b$$, and $$c$$ could be positive, negative, or zero).  
  
$$\,+\,$$ $$\,+\,$$ $$\,=\,$$  
A voting paradox occurs when the three numbers on the right, $$a-b+c$$ and $$a+b-c$$ and $$-a+b+c$$, are all nonnegative or all nonpositive. On the left, at least two of the three numbers, $$a$$ and $$b$$ and $$c$$, are both nonnegative or both nonpositive. We can assume that they are $$a$$ and $$b$$. That makes four cases: the cycle is nonnegative and $$a$$ and $$b$$ are nonnegative, the cycle is nonpositive and $$a$$ and $$b$$ are nonpositive, etc. We will do only the first case, since the second is similar and the other two are also easy.

So assume that the cycle is nonnegative and that $$a$$ and $$b$$ are nonnegative. The conditions $$0\leq a-b+c$$ and $$0\leq -a+b+c$$ add to give that $$0\leq 2c$$, which implies that $$c$$ is also nonnegative, as desired. That ends the proof.

This result says only that having all three spin in the same direction is a necessary condition for a majority cycle. It is not sufficient; see Problem 4.

Voting theory and associated topics are the subject of current research. There are many intriguing results, most notably the one produced by K. Arrow (Arrow 1963), who won the Nobel Prize in part for this work, showing that no voting system is entirely fair (for a reasonable definition of "fair"). For more information, some good introductory articles are (Gardner 1970), (Gardner 1974), (Gardner 1980), and (Neimi & Riker 1976) harv error: no target: CITEREFNeimiRiker_1976 (help). A quite readable recent book is (Taylor 1995). The long list of cases from recent American political history given in (Poundstone 2008) show that manipulation of these paradoxes is routine in practice (and the author proposes a solution).

This Topic is largely drawn from (Zwicker 1991). *(Author's Note: I would like to thank Professor Zwicker for his kind and illuminating discussions.)*

### Exercises

**Problem 1**  —

Here is a reasonable way in which a voter could have a cyclic preference. Suppose that this voter ranks each candidate on each of three criteria.

1. Draw up a table with the rows labelled "Democrat", "Republican", and "Third", and the columns labelled "character", "experience", and "policies". Inside each column, rank some candidate as most preferred, rank another as in the middle, and rank the remaining oneas least preferred.
2. In this ranking, is the Democrat preferred to the Republican in (at least) two out of three criteria, or vice versa? Is the Republican preferred to the Third?
3. Does the table that was just constructed have a cyclic preference order? If not, make one that does.

So it is possible for a voter to have a cyclic preference among candidates. The paradox described above, however, is that even if each voter has a straight-line preference list, a cyclic preference can still arise for the entire group.

**Problem 2**  —

Compute the values in the table of decompositions.

**Problem 3**  —

Do the cancellations of opposite preference orders for the Political Science class's mock election. Are all the remaining preferences from the left three rows of the table or from the right?

**Problem 4**  —

The necessary condition that is proved above—a voting paradox can happen only if all three preference lists remaining after cancellation have the same spin—is not also sufficient.

1. Continuing the positive cycle case considered in the proof, use the two inequalities $$0\leq a-b+c$$ and $$0\leq -a+b+c$$ to show that $$|a-b|\leq c$$.
2. Also show that $$c\leq a+b$$, and hence that $$|a-b|\leq c\leq a+b$$.
3. Give an example of a vote where there is a majority cycle, and addition of one more voter with the same spin causes the cycle to go away.
4. Can the opposite happen; can addition of one voter with a "wrong" spin cause a cycle to appear?
5. Give a condition that is both necessary and sufficient to get a majority cycle.

**Problem 5**  — A one-voter election cannot have a majority cycle because of the requirement that we've imposed that the voter's list must be rational.

1. Show that a two-voter election may have a majority cycle. (We consider the group preference a majority cycle if all three group totals are nonnegative or if all three are nonpositive---that is, we allow some zero's in the group preference.)
2. Show that for any number of voters greater than one, there is an election involving that many voters that results in a majority cycle.

**Problem 6**  —

Let $$U$$ be a subspace of $$\mathbb{R}^3$$. Prove that the set $$U^\perp=\{\vec{v}\,\big|\,\vec{v}\cdot\vec{u}=0 \text{ for all } \vec{u}\in U\}$$ of vectors that are perpendicular to each vector in $$U$$ is also a subspace of $$\mathbb{R}^3$$.

Solutions

### References

- Arrow, J. (1963), *Social Choice and Individual Values*, Wiley.
- Gardner, Martin (April 1970), "Mathematical Games, Some mathematical curiosities embedded in the solar system", *Scientific American*: 108–112{{citation}}: CS1 maint: year (link).
- Gardner, Martin (October 1974), "Mathematical Games, On the paradoxical situations that arise from nontransitive relations", *Scientific American*{{citation}}: CS1 maint: year (link).
- Gardner, Martin (October 1980), "Mathematical Games, From counting votes to making votes count: the mathematics of elections", *Scientific American*{{citation}}: CS1 maint: year (link).
- Neimi, G.; Riker, W. (June 1976), "The Choice of Voting Systems", *Scientific American*: 21–27{{citation}}: CS1 maint: year (link).
- Poundstone, W. (2008), *Gaming the vote*, Hill and Wang, ISBN) 978-0-8090-4893-9.
- Taylor, Alan D. (1995), *Mathematics and Politics: Strategy, Voting, Power, and Proof*, Springer-Verlag.
- Zwicker, S. (1991), "The Voters' Paradox, Spin, and the Borda Count", *Mathematical Social Sciences*, **22**: 187–227

---

*Source: Wikibooks, Linear Algebra/Topic: Voting Paradoxes (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Voting_Paradoxes), by Wikibooks contributors, CC BY-SA 4.0.*
