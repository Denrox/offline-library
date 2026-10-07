# Definition of Determinant

For $$1 \! \times \! 1$$ matrices, determining nonsingularity is trivial.

$$\begin{pmatrix} a \end{pmatrix}$$ is nonsingular iff $$a \neq 0$$

The $$2 \! \times \! 2$$ formula came out in the course of developing the inverse.

$$\begin{pmatrix} a &b \\ c &d \end{pmatrix}$$ is nonsingular iff $$ad-bc \neq 0$$

The $$3 \! \times \! 3$$ formula can be produced similarly (see [Problem 9](Linear%20Algebra%20-%20Exploration.md)).

$$\begin{pmatrix} a &b &c \\ d &e &f \\ g &h &i \end{pmatrix}$$ is nonsingular iff $$aei+bfg+cdh-hfa-idb-gec \neq 0$$

With these cases in mind, we posit a family of formulas, $$a$$, $$ad-bc$$, etc. For each $$n$$ the formula gives rise to a **determinant** function $$\det\nolimits_{n \! \times \! n}:\mathcal{M}_{n \! \times \! n}\to \mathbb{R}$$ such that an $$n \! \times \! n$$ matrix $$T$$ is nonsingular if and only if $$\det\nolimits_{n \! \times \! n}(T)\neq 0$$. (We usually omit the subscript because if $$T$$ is $$n \! \times \! n$$ then "$$\det(T)$$" could only mean "$$\det\nolimits_{n \! \times \! n}(T)$$".)

---

*Source: Wikibooks, Linear Algebra/Definition of Determinant (https://en.wikibooks.org/wiki/Linear_Algebra/Definition_of_Determinant), by Wikibooks contributors, CC BY-SA 4.0.*
