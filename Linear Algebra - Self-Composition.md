# Self-Composition

*This subsection is optional, although it is necessary for later material in this section and in the next one.*

A linear transformations $$t:V\to V$$, because it has the same domain and codomain, can be iterated. That is, compositions of $$t$$ with itself such as $$t^2=t\circ t$$ and $$t^3=t\circ t\circ t$$ are defined.

Note that this power notation for the linear transformation functions dovetails with the notation that we've used earlier for their squared matrix representations because if $${\rm Rep}_{B,B}(t)=T$$ then $${\rm Rep}_{B,B}(t^j)=T^j$$.

**Example 1.1**  —

For the derivative map $$d/dx:\mathcal{P}_3\to \mathcal{P}_3$$ given by

$$
a+bx+cx^2+dx^3\stackrel{d/dx}{\longmapsto} b+2cx+3dx^2
$$

the second power is the second derivative

$$
a+bx+cx^2+dx^3\stackrel{d^2/dx^2}{\longmapsto} 2c+6dx
$$

the third power is the third derivative

$$
a+bx+cx^2+dx^3\stackrel{d^3/dx^3}{\longmapsto} 6d
$$

and any higher power is the zero map.

**Example 1.2**  —

This transformation of the space of $$2 \! \times \! 2$$ matrices

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \stackrel{t}{\longmapsto} \begin{pmatrix} b &a \\ d &0 \end{pmatrix}
$$

has this second power

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \stackrel{t^2}{\longmapsto} \begin{pmatrix} a &b \\ 0 &0 \end{pmatrix}
$$

and this third power.

$$
\begin{pmatrix} a &b \\ c &d \end{pmatrix} \stackrel{t^3}{\longmapsto} \begin{pmatrix} b &a \\ 0 &0 \end{pmatrix}
$$

After that, $$t^4=t^2$$ and $$t^5=t^3$$, etc.

These examples suggest that on iteration more and more zeros appear until there is a settling down. The next result makes this precise.

**Lemma 1.3**  —

For any transformation $$t:V\to V$$, the rangespaces of the powers form a descending chain

$$
V\supseteq \mathcal{R}(t)\supseteq\mathcal{R}(t^2)\supseteq\cdots
$$

and the nullspaces form an ascending chain.

$$
\{\vec{0}\,\}\subseteq\mathcal{N}(t)\subseteq\mathcal{N}(t^2)\subseteq\cdots
$$

Further, there is a $$k$$ such that for powers less than $$k$$ the subsets are proper (if $$j<k$$ then $$\mathcal{R}(t^j)\supset\mathcal{R}(t^{j+1})$$ and $$\mathcal{N}(t^j)\subset\mathcal{N}(t^{j+1})$$), while for powers greater than $$k$$ the sets are equal (if $$j\geq k$$ then $$\mathcal{R}(t^j)=\mathcal{R}(t^{j+1})$$ and $$\mathcal{N}(t^j)=\mathcal{N}(t^{j+1})$$).

**Proof**  —

We will do the rangespace half and leave the rest for Problem 6. Recall, however, that for any map the dimension of its rangespace plus the dimension of its nullspace equals the dimension of its domain. So if the rangespaces shrink then the nullspaces must grow.

That the rangespaces form chains is clear because if $$\vec{w}\in\mathcal{R}(t^{j+1})$$, so that $$\vec{w}=t^{j+1}(\vec{v})$$, then $$\vec{w}=t^{j}(\,t(\vec{v})\,)$$ and so $$\vec{w}\in\mathcal{R}(t^{j})$$. To verify the "further" property, first observe that if any pair of rangespaces in the chain are equal $$\mathcal{R}(t^{k})=\mathcal{R}(t^{k+1})$$ then all subsequent ones are also equal $$\mathcal{R}(t^{k+1})=\mathcal{R}(t^{k+2})$$, etc. This is because if $$t:\mathcal{R}(t^{k+1})\to \mathcal{R}(t^{k+2})$$ is the same map, with the same domain, as $$t:\mathcal{R}(t^{k})\to \mathcal{R}(t^{k+1})$$ and it therefore has the same range: $$\mathcal{R}(t^{k+1})=\mathcal{R}(t^{k+2})$$ (and induction shows that it holds for all higher powers). So if the chain of rangespaces ever stops being strictly decreasing then it is stable from that point onward.

But the chain must stop decreasing. Each rangespace is a subspace of the one before it. For it to be a proper subspace it must be of strictly lower dimension (see Problem 4). These spaces are finite-dimensional and so the chain can fall for only finitely-many steps, that is, the power $$k$$ is at most the dimension of $$V$$.

**Example 1.4**  —

The derivative map $$a+bx+cx^2+dx^3\stackrel{d/dx}{\longmapsto} b+2cx+3dx^2$$ of Example 1.1 has this chain of rangespaces

$$
\mathcal{P}_3\supset\mathcal{P}_2\supset\mathcal{P}_1 \supset\mathcal{P}_0\supset\{\vec{0}\,\}=\{\vec{0}\,\}=\cdots
$$

and this chain of nullspaces.

$$
\{\vec{0}\,\}\subset\mathcal{P}_0\subset\mathcal{P}_1\subset\mathcal{P}_2 \subset\mathcal{P}_3=\mathcal{P}_3=\cdots
$$

**Example 1.5**  —

The transformation $$\pi:\mathbb{C}^3\to \mathbb{C}^3$$ projecting onto the first two coordinates

$$
\begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix} \stackrel{\pi}{\longmapsto} \begin{pmatrix} c_1 \\ c_2 \\ 0 \end{pmatrix}
$$

has $$\mathbb{C}^3\supset\mathcal{R}(\pi)=\mathcal{R}(\pi^2)=\cdots$$ and $$\{\vec{0}\,\}\subset\mathcal{N}(\pi)=\mathcal{N}(\pi^2)=\cdots\,$$.

**Example 1.6**  —

Let $$t:\mathcal{P}_2\to \mathcal{P}_2$$ be the map $$c_0+c_1x+c_2x^2 \mapsto 2c_0+c_2x.$$ As the lemma describes, on iteration the rangespace shrinks

$$
\mathcal{R}(t^0)=\mathcal{P}_2 \quad \mathcal{R}(t)=\{a+bx\,\big|\, a,b\in\mathbb{C}\} \quad \mathcal{R}(t^2)=\{a\,\big|\, a\in\mathbb{C}\}
$$

and then stabilizes $$\mathcal{R}(t^2)=\mathcal{R}(t^3)=\cdots$$, while the nullspace grows

$$
\mathcal{N}(t^0)=\{0\} \quad \mathcal{N}(t)=\{cx\,\big|\, c\in\mathbb{C}\} \quad \mathcal{N}(t^2)=\{cx+d\,\big|\, c,d\in\mathbb{C}\}
$$

and then stabilizes $$\mathcal{N}(t^2)=\mathcal{N}(t^3)=\cdots$$.

This graph illustrates Lemma 1.3. The horizontal axis gives the power $$j$$ of a transformation. The vertical axis gives the dimension of the rangespace of $$t^j$$ as the distance above zero— and thus also shows the dimension of the nullspace as the distance below the gray horizontal line, because the two add to the dimension $$n$$ of the domain.

As sketched, on iteration the rank falls and with it the nullity grows until the two reach a steady state. This state must be reached by the $$n$$-th iterate. The steady state's distance above zero is the dimension of the generalized rangespace and its distance below $$n$$ is the dimension of the generalized nullspace.

**Definition 1.7**  —

Let $$t$$ be a transformation on an $$n$$-dimensional space. The **generalized rangespace** (or the **closure of the rangespace**) is $$\mathcal{R}_\infty(t)=\mathcal{R}(t^n)$$ The **generalized nullspace** (or the **closure of the nullspace**) is $$\mathcal{N}_\infty(t)=\mathcal{N}(t^n)$$.

### Exercises

**Problem 1**  —

Give the chains of rangespaces and nullspaces for the zero and identity transformations.

**Problem 2**  —

For each map, give the chain of rangespaces and the chain of nullspaces, and the generalized rangespace and the generalized nullspace.

1. $$t_0:\mathcal{P}_2\to \mathcal{P}_2$$, $$a+bx+cx^2\mapsto b+cx^2$$
2. $$t_1:\mathbb{R}^2\to \mathbb{R}^2$$,

$$
\begin{pmatrix} a \\ b \end{pmatrix}\mapsto\begin{pmatrix} 0 \\ a \end{pmatrix}
$$

3. $$t_2:\mathcal{P}_2\to \mathcal{P}_2$$, $$a+bx+cx^2\mapsto b+cx+ax^2$$
4. $$t_3:\mathbb{R}^3\to \mathbb{R}^3$$,

$$
\begin{pmatrix} a \\ b \\ c \end{pmatrix}\mapsto\begin{pmatrix} a \\ a \\ b \end{pmatrix}
$$

**Problem 3**  —

Prove that function composition is associative $$(t\circ t)\circ t=t\circ (t\circ t)$$ and so we can write $$t^3$$ without specifying a grouping.

**Problem 4**  —

Check that a subspace must be of dimension less than or equal to the dimension of its superspace. Check that if the subspace is proper (the subspace does not equal the superspace) then the dimension is strictly less. *(This is used in the proof of Lemma 1.3.)*

**Problem 5**  —

Prove that the generalized rangespace $$\mathcal{R}_\infty(t)$$ is the entire space, and the generalized nullspace $$\mathcal{N}_\infty(t)$$ is trivial, if the transformation $$t$$ is nonsingular. Is this "only if" also?

**Problem 6**  —

Verify the nullspace half of Lemma 1.3.

**Problem 7**  —

Give an example of a transformation on a three dimensional space whose range has dimension two. What is its nullspace? Iterate your example until the rangespace and nullspace stabilize.

**Problem 8**  —

Show that the rangespace and nullspace of a linear transformation need not be disjoint. Are they ever disjoint?

Solutions

---

*Source: Wikibooks, Linear Algebra/Self-Composition (https://en.wikibooks.org/wiki/Linear_Algebra/Self-Composition), by Wikibooks contributors, CC BY-SA 4.0.*
