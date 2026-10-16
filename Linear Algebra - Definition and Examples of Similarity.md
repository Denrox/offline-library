# Definition and Examples of Similarity

### Definition and Examples

We've defined $$H$$ and $$\hat{H}$$ to be matrix-equivalent if there are nonsingular matrices $$P$$ and $$Q$$ such that $$\hat{H}=PHQ$$. That definition is motivated by this diagram  
showing that $$H$$ and $$\hat{H}$$ both represent $$h$$ but with respect to different pairs of bases. We now specialize that setup to the case where the codomain equals the domain, and where the codomain's basis equals the domain's basis.  
To move from the lower left to the lower right we can either go straight over, or up, over, and then down. In matrix terms,

$$
{\rm Rep}_{D,D}(t) ={\rm Rep}_{B,D}(\text{id})\;{\rm Rep}_{B,B}(t)\;\bigl({\rm Rep}_{B,D}(\text{id})\bigr)^{-1}
$$

(recall that a representation of composition like this one reads right to left).

**Definition 1.1**  —

The matrices $$T$$ and $$S$$ are **similar** if there is a nonsingular $$P$$ such that $$T=PSP^{-1}$$.

Since nonsingular matrices are square, the similar matrices $$T$$ and $$S$$ must be square and of the same size.

**Example 1.2**  —

With these two,

$$
P= \begin{pmatrix} 2 &1 \\ 1 &1 \end{pmatrix} \qquad S= \begin{pmatrix} 2 &-3 \\ 1 &-1 \end{pmatrix}
$$

calculation gives that $$S$$ is similar to this matrix.

$$
T= \begin{pmatrix} 0 &-1 \\ 1 &1 \end{pmatrix}
$$

**Example 1.3**  —

The only matrix similar to the zero matrix is itself: $$PZP^{-1}=PZ=Z$$. The only matrix similar to the identity matrix is itself: $$PIP^{-1}=PP^{-1}=I$$.

Since matrix similarity is a special case of matrix equivalence, if two matrices are similar then they are equivalent. What about the converse: must matrix equivalent square matrices be similar? The answer is no. The prior example shows that the similarity classes are different from the matrix equivalence classes, because the matrix equivalence class of the identity consists of all nonsingular matrices of that size. Thus, for instance, these two are matrix equivalent but not similar.

$$
T= \begin{pmatrix} 1 &0 \\ 0 &1 \end{pmatrix} \qquad S= \begin{pmatrix} 1 &2 \\ 0 &3 \end{pmatrix}
$$

So some matrix equivalence classes split into two or more similarity classes— similarity gives a finer partition than does equivalence. This picture shows some matrix equivalence classes subdivided into similarity classes.

To understand the similarity relation we shall study the similarity classes. We approach this question in the same way that we've studied both the row equivalence and matrix equivalence relations, by finding a canonical form for representatives of the similarity classes, called Jordan form. With this canonical form, we can decide if two matrices are similar by checking whether they reduce to the same representative. We've also seen with both row equivalence and matrix equivalence that a canonical form gives us insight into the ways in which members of the same class are alike (e.g., two identically-sized matrices are matrix equivalent if and only if they have the same rank).

### Exercises

**Problem 1**  —

For

$$
S= \begin{pmatrix} 1 &3 \\ -2 &-6 \end{pmatrix} \quad T= \begin{pmatrix} 0 &0 \\ -11/2 &-5 \end{pmatrix} \quad P= \begin{pmatrix} 4 &2 \\ -3 &2 \end{pmatrix}
$$

check that $$T=PSP^{-1}$$.  
*This exercise is recommended for all readers.*

**Problem 2**  —

Example 1.3 shows that the only matrix similar to a zero matrix is itself and that the only matrix similar to the identity is itself.

1. Show that the $$1 \! \times \! 1$$ matrix $$(2)$$, also, is similar only to itself.
2. Is a matrix of the form $$cI$$ for some scalar $$c$$ similar only to itself?
3. Is a diagonal matrix similar only to itself?

**Problem 3**  —

Show that these matrices are not similar.

$$
\begin{pmatrix} 1 &0 &4 \\ 1 &1 &3 \\ 2 &1 &7 \end{pmatrix} \qquad \begin{pmatrix} 1 &0 &1 \\ 0 &1 &1 \\ 3 &1 &2 \end{pmatrix}
$$

**Problem 4**  —

Consider the transformation $$t:\mathcal{P}_2\to \mathcal{P}_2$$ described by $$x^2\mapsto x+1$$, $$x\mapsto x^2-1$$, and $$1\mapsto 3$$.

1. Find $$T={\rm Rep}_{B,B}(t)$$ where $$B=\langle x^2,x,1 \rangle$$.
2. Find $$S={\rm Rep}_{D,D}(t)$$ where $$D=\langle 1,1+x,1+x+x^2 \rangle$$.
3. Find the matrix $$P$$ such that $$T=PSP^{-1}$$.  
*This exercise is recommended for all readers.*

**Problem 5**  —

Exhibit an nontrivial similarity relationship in this way: let $$t:\mathbb{C}^2\to \mathbb{C}^2$$ act by

$$
\begin{pmatrix} 1 \\ 2 \end{pmatrix}\mapsto\begin{pmatrix} 3 \\ 0 \end{pmatrix} \qquad \begin{pmatrix} -1 \\ 1 \end{pmatrix}\mapsto\begin{pmatrix} -1 \\ 2 \end{pmatrix}
$$

and pick two bases, and represent $$t$$ with respect to then $$T={\rm Rep}_{B,B}(t)$$ and $$S={\rm Rep}_{D,D}(t)$$. Then compute the $$P$$ and $$P^{-1}$$ to change bases from $$B$$ to $$D$$ and back again.

**Problem 6**  —

Explain Example 1.3 in terms of maps.  
*This exercise is recommended for all readers.*

**Problem 7**  —

Are there two matrices $$A$$ and $$B$$ that are similar while $$A^2$$ and $$B^2$$ are not similar? (Halmos 1958)  
*This exercise is recommended for all readers.*

**Problem 8**  —

Prove that if two matrices are similar and one is invertible then so is the other.  
*This exercise is recommended for all readers.*

**Problem 9**  —

Show that similarity is an equivalence relation.

**Problem 10**  —

Consider a matrix representing, with respect to some $$B,B$$, reflection across the $$x$$-axis in $$\mathbb{R}^2$$. Consider also a matrix representing, with respect to some $$D,D$$, reflection across the $$y$$-axis. Must they be similar?

**Problem 11**  —

Prove that similarity preserves determinants and rank. Does the converse hold?

**Problem 12**  —

Is there a matrix equivalence class with only one matrix similarity class inside? One with infinitely many similarity classes?

**Problem 13**  —

Can two different diagonal matrices be in the same similarity class?  
*This exercise is recommended for all readers.*

**Problem 14**  —

Prove that if two matrices are similar then their $$k$$-th powers are similar when $$k>0$$. What if $$k\leq 0$$?  
*This exercise is recommended for all readers.*

**Problem 15**  —

Let $$p(x)$$ be the polynomial $$c_nx^n+\cdots+c_1x+c_0$$. Show that if $$T$$ is similar to $$S$$ then $$p(T)=c_nT^n+\cdots+c_1T+c_0I$$ is similar to $$p(S)=c_nS^n+\cdots+c_1S+c_0I$$.

**Problem 16**  —

List all of the matrix equivalence classes of $$1 \! \times \! 1$$ matrices. Also list the similarity classes, and describe which similarity classes are contained inside of each matrix equivalence class.

**Problem 17**  —

Does similarity preserve sums?

**Problem 18**  —

Show that if $$T-\lambda I$$ and $$N$$ are similar matrices then $$T$$ and $$N+\lambda I$$ are also similar.

Solutions

### References

- Halmos, Paul P. (1958), *Finite Dimensional Vector Spaces* (Second ed.), Van Nostrand.

---

*Source: Wikibooks, Linear Algebra/Definition and Examples of Similarity (https://en.wikibooks.org/wiki/Linear_Algebra/Definition_and_Examples_of_Similarity), by Wikibooks contributors, CC BY-SA 4.0.*
