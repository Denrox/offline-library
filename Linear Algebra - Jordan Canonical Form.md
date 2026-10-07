# Jordan Canonical Form

This subsection moves from the canonical form for nilpotent matrices to the one for all matrices.

We have shown that if a map is nilpotent then all of its eigenvalues are zero. We can now prove the converse.

**Lemma 2.1**  —

A linear transformation whose only eigenvalue is zero is nilpotent.

**Proof**  —

If a transformation $$t$$ on an $$n$$-dimensional space has only the single eigenvalue of zero then its characteristic polynomial is $$x^n$$. The Cayley-Hamilton Theorem says that a map satisfies its characteristic polynomial so $$t^n$$ is the zero map. Thus $$t$$ is nilpotent.

We have a canonical form for nilpotent matrices, that is, for each matrix whose single eigenvalue is zero: each such matrix is similar to one that is all zeroes except for blocks of subdiagonal ones. (To make this representation unique we can fix some arrangement of the blocks, say, from longest to shortest.) We next extend this to all single-eigenvalue matrices.

Observe that if $$t$$'s only eigenvalue is $$\lambda$$ then $$t-\lambda$$'s only eigenvalue is $$0$$ because $$t(\vec{v})=\lambda\vec{v}$$ if and only if $$(t-\lambda)\,(\vec{v})=0\cdot\vec{v}$$. The natural way to extend the results for nilpotent matrices is to represent $$t-\lambda$$ in the canonical form $$N$$, and try to use that to get a simple representation $$T$$ for $$t$$. The next result says that this try works.

**Lemma 2.2**  —

If the matrices $$T-\lambda I$$ and $$N$$ are similar then $$T$$ and $$N+\lambda I$$ are also similar, via the same change of basis matrices.

**Proof**  —

With $$N=P(T-\lambda I)P^{-1}=PTP^{-1}-P(\lambda I)P^{-1}$$ we have $$N=PTP^{-1}-PP^{-1}(\lambda I)$$ since the diagonal matrix $$\lambda I$$ commutes with anything, and so $$N=PTP^{-1}-\lambda I$$. Therefore $$N+\lambda I=PTP^{-1}$$, as required.

**Example 2.3**  —

The characteristic polynomial of

$$
T=\begin{pmatrix} 2 &-1 \\ 1 &4 \end{pmatrix}
$$

is $$(x-3)^2$$ and so $$T$$ has only the single eigenvalue $$3$$. Thus for

$$
T-3I=\begin{pmatrix} -1 &-1 \\ 1 &1 \end{pmatrix}
$$

the only eigenvalue is $$0$$, and $$T-3I$$ is nilpotent. The null spaces are routine to find; to ease this computation we take $$T$$ to represent the transformation $$t:\mathbb{C}^2\to \mathbb{C}^2$$ with respect to the standard basis (we shall maintain this convention for the rest of the chapter).

$$
\mathcal{N}(t-3)=\{\begin{pmatrix} -y \\ y \end{pmatrix}\,\big|\, y\in\mathbb{C}\} \qquad \mathcal{N}((t-3)^2)=\mathbb{C}^2
$$

The dimensions of these null spaces show that the action of an associated map $$t-3$$ on a string basis is $$\vec{\beta}_1\mapsto\vec{\beta}_2\mapsto\vec{0}$$. Thus, the canonical form for $$t-3$$ with one choice for a string basis is

$$
{\rm Rep}_{B,B}(t-3) =N =\begin{pmatrix} 0 &0 \\ 1 &0 \end{pmatrix} \qquad B=\langle \begin{pmatrix} 1 \\ 1 \end{pmatrix},\begin{pmatrix} -2 \\ 2 \end{pmatrix} \rangle
$$

and by Lemma 2.2, $$T$$ is similar to this matrix.

$$
{\rm Rep}_{t}(B,B)= N+3I= \begin{pmatrix} 3 &0 \\ 1 &3 \end{pmatrix}
$$

We can produce the similarity computation. Recall from the Nilpotence section how to find the change of basis matrices $$P$$ and $$P^{-1}$$ to express $$N$$ as $$P(T-3I)P^{-1}$$. The similarity diagram  
describes that to move from the lower left to the upper left we multiply by

$$
P^{-1}=\bigl({\rm Rep}_{\mathcal{E}_2,B}(\text{id})\bigr)^{-1} ={\rm Rep}_{B,\mathcal{E}_2}(\text{id}) =\begin{pmatrix} 1 &-2 \\ 1 &2 \end{pmatrix}
$$

and to move from the upper right to the lower right we multiply by this matrix.

$$
P=\begin{pmatrix} 1 &-2 \\ 1 &2 \end{pmatrix}^{-1} =\begin{pmatrix} 1/2 &1/2 \\ -1/4 &1/4 \end{pmatrix}
$$

So the similarity is expressed by

$$
\begin{pmatrix} 3 &0 \\ 1 &3 \end{pmatrix} = \begin{pmatrix} 1/2 &1/2 \\ -1/4 &1/4 \end{pmatrix} \begin{pmatrix} 2 &-1 \\ 1 &4 \end{pmatrix} \begin{pmatrix} 1 &-2 \\ 1 &2 \end{pmatrix}
$$

which is easily checked.

**Example 2.4**  —

This matrix has characteristic polynomial $$(x-4)^4$$

$$
T= \begin{pmatrix} 4 &1 &0 &-1 \\ 0 &3 &0 &1 \\ 0 &0 &4 &0 \\ 1 &0 &0 &5 \end{pmatrix}
$$

and so has the single eigenvalue $$4$$. The nullities of $$t-4$$ are: the null space of $$t-4$$ has dimension two, the null space of $$(t-4)^2$$ has dimension three, and the null space of $$(t-4)^3$$ has dimension four. Thus, $$t-4$$ has the action on a string basis of $$\vec{\beta}_1\mapsto\vec{\beta}_2\mapsto\vec{\beta}_3\mapsto\vec{0}$$ and $$\vec{\beta}_4\mapsto\vec{0}$$. This gives the canonical form $$N$$ for $$t-4$$, which in turn gives the form for $$t$$.

$$
N+4I= \begin{pmatrix} 4 &0 &0 &0 \\ 1 &4 &0 &0 \\ 0 &1 &4 &0 \\ 0 &0 &0 &4 \end{pmatrix}
$$

An array that is all zeroes, except for some number $$\lambda$$ down the diagonal and blocks of subdiagonal ones, is a **Jordan block**. We have shown that Jordan block matrices are canonical representatives of the similarity classes of single-eigenvalue matrices.

**Example 2.5**  —

The $$3 \! \times \! 3$$ matrices whose only eigenvalue is $$1/2$$ separate into three similarity classes. The three classes have these canonical representatives.

$$
\begin{pmatrix} 1/2 &0 &0 \\ 0 &1/2 &0 \\ 0 &0 &1/2 \end{pmatrix} \qquad \begin{pmatrix} 1/2 &0 &0 \\ 1 &1/2 &0 \\ 0 &0 &1/2 \end{pmatrix} \qquad \begin{pmatrix} 1/2 &0 &0 \\ 1 &1/2 &0 \\ 0 &1 &1/2 \end{pmatrix}
$$

In particular, this matrix

$$
\begin{pmatrix} 1/2 &0 &0 \\ 0 &1/2 &0 \\ 0 &1 &1/2 \end{pmatrix}
$$

belongs to the similarity class represented by the middle one, because we have adopted the convention of ordering the blocks of subdiagonal ones from the longest block to the shortest.

We will now finish the program of this chapter by extending this work to cover maps and matrices with multiple eigenvalues. The best possibility for general maps and matrices would be if we could break them into a part involving their first eigenvalue $$\lambda_1$$ (which we represent using its Jordan block), a part with $$\lambda_2$$, etc.

This ideal is in fact what happens. For any transformation $$t:V\to V$$, we shall break the space $$V$$ into the direct sum of a part on which $$t-\lambda_1$$ is nilpotent, plus a part on which $$t-\lambda_2$$ is nilpotent, etc. More precisely, we shall take three steps to get to this section's major theorem and the third step shows that $$V=\mathcal{N}_\infty(t-\lambda_1)\oplus\cdots\oplus \mathcal{N}_\infty(t-\lambda_\ell)$$ where $$\lambda_1,\ldots,\lambda_\ell$$ are $$t$$'s eigenvalues.

Suppose that $$t:V\to V$$ is a linear transformation. Note that the restriction of $$t$$ to a subspace $$M$$ need not be a linear transformation on $$M$$ because there may be an $$\vec{m}\in M$$ with $$t(\vec{m})\not\in M$$. To ensure that the restriction of a transformation to a "part" of a space is a transformation on the partwe need the next condition.

**Definition 2.6**  —

Let $$t:V\to V$$ be a transformation. A subspace $$M$$ is **$$t$$ invariant** if whenever $$\vec{m}\in M$$ then $$t(\vec{m})\in M$$ (shorter: $$t(M)\subseteq M$$).

Two examples are that the generalized null space $$\mathcal{N}_\infty(t)$$ and the generalized range space $$\mathcal{R}_\infty(t)$$ of any transformation $$t$$ are invariant. For the generalized null space, if $$\vec{v}\in\mathcal{N}_\infty(t)$$ then $$t^n(\vec{v})=\vec{0}$$ where $$n$$ is the dimension of the underlying space and so $$t(\vec{v})\in\mathcal{N}_\infty(t)$$ because $$t^n(\,t(\vec{v})\,)$$ is zero also. For the generalized range space, if $$\vec{v}\in\mathcal{R}_\infty(t)$$ then $$\vec{v}=t^n(\vec{w})$$ for some $$\vec{w}$$ and then $$t(\vec{v})=t^{n+1}(\vec{w})=t^n(\,t(\vec{w})\,)$$ shows that $$t(\vec{v})$$ is also a member of $$\mathcal{R}_\infty(t)$$.

Thus the spaces $$\mathcal{N}_\infty(t-\lambda_i)$$ and $$\mathcal{R}_\infty(t-\lambda_i)$$ are $$t-\lambda_i$$ invariant. Observe also that $$t-\lambda_i$$ is nilpotent on $$\mathcal{N}_\infty(t-\lambda_i)$$ because, simply, if $$\vec{v}$$ has the property that some power of $$t-\lambda_i$$ maps it to zero— that is, if it is in the generalized null space— then some power of $$t-\lambda_i$$ maps it to zero. The generalized null space $$\mathcal{N}_\infty(t-\lambda_i)$$ is a "part" of the space on which the action of $$t-\lambda_i$$ is easy to understand.

The next result is the first of our three steps. It establishes that $$t-\lambda_j$$ leaves $$t-\lambda_i$$'s part unchanged.

**Lemma 2.7**  —

A subspace is $$t$$ invariant if and only if it is $$t-\lambda$$ invariant for any scalar $$\lambda$$. In particular, where $$\lambda_i$$ is an eigenvalue of a linear transformation $$t$$, then for any other eigenvalue $$\lambda_j$$, the spaces $$\mathcal{N}_\infty(t-\lambda_i)$$ and $$\mathcal{R}_\infty(t-\lambda_i)$$ are $$t-\lambda_j$$ invariant.

**Proof**  —

For the first sentence we check the two implications of the "if and only if" separately. One of them is easy: if the subspace is $$t-\lambda$$ invariant for any $$\lambda$$ then taking $$\lambda=0$$ shows that it is $$t$$ invariant. For the other implication suppose that the subspace is $$t$$ invariant, so that if $$\vec{m}\in M$$ then $$t(\vec{m})\in M$$, and let $$\lambda$$ be any scalar. The subspace $$M$$ is closed under linear combinations and so if $$t(\vec{m})\in M$$ then $$t(\vec{m})-\lambda\vec{m}\in M$$. Thus if $$\vec{m}\in M$$ then $$(t-\lambda)\,(\vec{m})\in M$$, as required.

The second sentence follows straight from the first. Because the two spaces are $$t-\lambda_i$$ invariant, they are therefore $$t$$ invariant. From this, applying the first sentence again, we conclude that they are also $$t-\lambda_j$$ invariant.

The second step of the three that we will take to prove this section's major result makes use of an additional property of $$\mathcal{N}_\infty(t-\lambda_i)$$ and $$\mathcal{R}_\infty(t-\lambda_i)$$, that they are complementary. Recall that if a space is the direct sum of two others $$V=\mathcal{N}\oplus \mathcal{R}$$ then any vector $$\vec{v}$$ in the space breaks into two parts $$\vec{v}=\vec{n}+\vec{r}$$ where $$\vec{n}\in \mathcal{N}$$ and $$\vec{r}\in \mathcal{R}$$, and recall also that if $$B_{\mathcal{N}}$$ and $$B_{\mathcal{R}}$$ are bases for $$\mathcal{N}$$ and $$\mathcal{R}$$ then the concatenation $$B_{\mathcal{N}}\!\mathbin{{}^\frown}\!B_{\mathcal{R}}$$ is linearly independent (and so the two parts of $$\vec{v}$$ do not "overlap"). The next result says that for any subspaces $$\mathcal{N}$$ and $$\mathcal{R}$$ that are complementary as well as $$t$$ invariant, the action of $$t$$ on $$\vec{v}$$ breaks into the "non-overlapping" actions of $$t$$ on $$\vec{n}$$ and on $$\vec{r}$$.

**Lemma 2.8**  —

Let $$t:V\to V$$ be a transformation and let $$\mathcal{N}$$ and $$\mathcal{R}$$ be $$t$$ invariant complementary subspaces of $$V$$. Then $$t$$ can be represented by a matrix with blocks of square submatrices $$T_1$$ and $$T_2$$

$$
\left(\begin{array}{c|c} T_1 &Z_2 \\ \hline Z_1 &T_2 \end{array}\right) \begin{array}{ll} \} \dim(\mathcal{N})\text{-many rows} \\ \} \dim(\mathcal{R})\text{-many rows} \end{array}
$$

where $$Z_1$$ and $$Z_2$$ are blocks of zeroes.

**Proof**  —

Since the two subspaces are complementary, the concatenation of a basis for $$\mathcal{N}$$ and a basis for $$\mathcal{R}$$ makes a basis $$B=\langle \vec{\nu}_1,\dots,\vec{\nu}_p, \vec{\mu}_1,\ldots,\vec{\mu}_q \rangle$$ for $$V$$. We shall show that the matrix

$$
{\rm Rep}_{B,B}(t)= \left(\begin{array}{c|c|c} \vdots & &\vdots \\ {\rm Rep}_{B}(t(\vec{\nu}_1)) &\cdots &{\rm Rep}_{B}(t(\vec{\mu}_q)) \\ \vdots & &\vdots \\ \end{array}\right)
$$

has the desired form.

Any vector $$\vec{v}\in V$$ is in $$\mathcal{N}$$ if and only if its final $$q$$ components are zeroes when it is represented with respect to $$B$$. As $$\mathcal{N}$$ is $$t$$ invariant, each of the vectors $${\rm Rep}_{B}(t(\vec{\nu}_1))$$, ..., $${\rm Rep}_{B}(t(\vec{\nu}_p))$$ has that form. Hence the lower left of $${\rm Rep}_{B,B}(t)$$ is all zeroes.

The argument for the upper right is similar.

To see that $$t$$ has been decomposed into its action on the parts, observe that the restrictions of $$t$$ to the subspaces $$\mathcal{N}$$ and $$\mathcal{R}$$ are represented, with respect to the obvious bases, by the matrices $$T_1$$ and $$T_2$$. So, with subspaces that are invariant and complementary, we can split the problem of examining a linear transformation into two lower-dimensional subproblems. The next result illustrates this decomposition into blocks.

**Lemma 2.9**  —

If $$T$$ is a matrices with square submatrices $$T_1$$ and $$T_2$$

$$
T= \left(\begin{array}{c|c} T_1 &Z_2 \\ \hline Z_1 &T_2 \end{array}\right)
$$

where the $$Z$$'s are blocks of zeroes, then $$\left|T\right|=\left|T_1\right|\cdot\left|T_2\right|$$.

**Proof**  —

Suppose that $$T$$ is $$n \! \times \! n$$, that $$T_1$$ is $$p \! \times \! p$$, and that $$T_2$$ is $$q \! \times \! q$$. In the permutation formula for the determinant

$$
\left|T\right|= \sum_{\text{permutations }\phi} t_{1,\phi(1)}t_{2,\phi(2)}\cdots t_{n,\phi(n)}\operatorname{sgn}(\phi)
$$

each term comes from a rearrangement of the column numbers $$1,\dots,n$$ into a new order $$\phi(1),\dots,\phi(n)$$. The upper right block $$Z_2$$ is all zeroes, so if a $$\phi$$ has at least one of $$p+1,\dots,n$$ among its first $$p$$ column numbers $$\phi(1),\dots,\phi(p)$$ then the term arising from $$\phi$$ is zero, e.g., if $$\phi(1)=n$$ then $$t_{1,\phi(1)}t_{2,\phi(2)}\dots t_{n,\phi(n)} =0\cdot t_{2,\phi(2)}\dots t_{n,\phi(n)}=0$$.

So the above formula reduces to a sum over all permutations with two halves: any significant $$\phi$$ is the composition of a $$\phi_1$$ that rearranges only $$1,\dots,p$$ and a $$\phi_2$$ that rearranges only $$p+1,\dots,p+q$$. Now, the distributive law (and the fact that the signum of a composition is the product of the signums) gives that this

$$
\left|T_1\right|\cdot\left|T_2\right|= \bigg(\sum_{\begin{array}{c}\\[-19pt] \scriptstyle\text{perms }\phi_1 \\[-5pt] \scriptstyle\text{of } 1,\dots,p \end{array}} \!\!\! t_{1,\phi_1(1)}\cdots t_{p,\phi_1(p)}\operatorname{sgn}(\phi_1) \bigg)
$$

$$
\cdot \bigg(\sum_{\begin{array}{c}\\[-19pt] \scriptstyle\text{perms }\phi_2 \\[-5pt] \scriptstyle\text{of } p+1,\dots,p+q \end{array}} \!\!\! t_{p+1,\phi_2(p+1)}\cdots t_{p+q,\phi_2(p+q)}\operatorname{sgn}(\phi_2) \bigg)
$$

equals $$\left|T\right|= \sum_{\text{significant }\phi} t_{1,\phi(1)}t_{2,\phi(2)}\cdots t_{n,\phi(n)}\operatorname{sgn}(\phi)$$.

**Example 2.10**  —

$$
\begin{vmatrix} 2 &0 &0 &0 \\ 1 &2 &0 &0 \\ 0 &0 &3 &0 \\ 0 &0 &0 &3 \end{vmatrix} =\begin{vmatrix} 2 &0 \\ 1 &2 \end{vmatrix} \cdot \begin{vmatrix} 3 &0 \\ 0 &3 \end{vmatrix} =36
$$

From Lemma 2.9 we conclude that if two subspaces are complementary and $$t$$ invariant then $$t$$ is nonsingular if and only if its restrictions to both subspaces are nonsingular.

Now for the promised third, final, step to the main result.

**Lemma 2.11**  —

If a linear transformation $$t:V\to V$$ has the characteristic polynomial $$(x-\lambda_1)^{p_1}\dots(x-\lambda_\ell)^{p_\ell}$$ then (1) $$V=\mathcal{N}_\infty(t-\lambda_1)\oplus\cdots \oplus\mathcal{N}_\infty(t-\lambda_\ell)$$ and (2) $$\dim(\mathcal{N}_\infty(t-\lambda_i))=p_i$$.

**Proof**  —

Because $$\dim (V)$$ is the degree $$p_1+\cdots+p_\ell$$ of the characteristic polynomial, to establish statement (1) we need only show that statement (2) holds and that $$\mathcal{N}_\infty(t-\lambda_i)\cap\mathcal{N}_\infty(t-\lambda_j)$$ is trivial whenever $$i\neq j$$.

For the latter, by Lemma 2.7, both $$\mathcal{N}_\infty(t-\lambda_i)$$ and $$\mathcal{N}_\infty(t-\lambda_j)$$ are $$t$$ invariant. Notice that an intersection of $$t$$ invariant subspaces is $$t$$ invariant and so the restriction of $$t$$ to $$\mathcal{N}_\infty(t-\lambda_i)\cap\mathcal{N}_\infty(t-\lambda_j)$$ is a linear transformation. But both $$t-\lambda_i$$ and $$t-\lambda_j$$ are nilpotent on this subspace and so if $$t$$ has any eigenvalues on the intersection then its "only" eigenvalue is both $$\lambda_i$$ and $$\lambda_j$$. That cannot be, so this restriction has no eigenvalues: $$\mathcal{N}_\infty(t-\lambda_i)\cap\mathcal{N}_\infty(t-\lambda_j)$$ is trivial ([Lemma V.II.3.10](Linear%20Algebra%20-%20Eigenvalues%20and%20Eigenvectors.md) shows that the only transformation without any eigenvalues is on the trivial space).

To prove statement (2), fix the index $$i$$. Decompose $$V$$ as $$\mathcal{N}_\infty(t-\lambda_i)\oplus\mathcal{R}_\infty(t-\lambda_i)$$

and apply Lemma 2.8.

$$
T= \left(\begin{array}{c|c} T_1 &Z_2 \\ \hline Z_1 &T_2 \end{array}\right) \begin{array}{ll} \} \dim(\,\mathcal{N}_\infty(t-\lambda_i)\,)\text{-many rows} \\ \} \dim(\,\mathcal{R}_\infty(t-\lambda_i)\,)\text{-many rows} \end{array}
$$

By Lemma 2.9, $$\left|T-xI\right|=\left|T_1-xI\right|\cdot\left|T_2-xI\right|$$. By the uniqueness clause of the Fundamental Theorem of Arithmetic, the determinants of the blocks have the same factors as the characteristic polynomial $$\left|T_1-xI\right|=(x-\lambda_1)^{q_1}\dots(x-\lambda_\ell)^{q_\ell}$$ and $$\left|T_2-xI\right|=(x-\lambda_1)^{r_1}\dots(x-\lambda_\ell)^{r_\ell}$$, and the sum of the powers of these factors is the power of the factor in the characteristic polynomial: $$q_1+r_1=p_1$$, ..., $$q_\ell+r_\ell=p_\ell$$. Statement (2) will be proved if we will show that $$q_i=p_i$$ and that $$q_j=0$$ for all $$j\neq i$$, because then the degree of the polynomial $$\left|T_1-xI\right|$$— which equals the dimension of the generalized null space— is as required.

For that, first, as the restriction of $$t-\lambda_i$$ to $$\mathcal{N}_\infty(t-\lambda_i)$$ is nilpotent on that space, the only eigenvalue of $$t$$ on it is $$\lambda_i$$. Thus the characteristic equation of $$t$$ on $$\mathcal{N}_\infty(t-\lambda_i)$$ is $$\left|T_1-xI\right|=(x-\lambda_i)^{q_i}$$. And thus $$q_j=0$$ for all $$j\neq i$$.

Now consider the restriction of $$t$$ to $$\mathcal{R}_\infty(t-\lambda_i)$$. By [Note V.III.2.2](Linear%20Algebra%20-%20Strings.md), the map $$t-\lambda_i$$ is nonsingular on $$\mathcal{R}_\infty(t-\lambda_i)$$ and so $$\lambda_i$$ is not an eigenvalue of $$t$$ on that subspace. Therefore, $$x-\lambda_i$$ is not a factor of $$\left|T_2-xI\right|$$, and so $$q_i=p_i$$.

Our major result just translates those steps into matrix terms.

**Theorem 2.12**  —

Any square matrix is similar to one in **Jordan form**

$$
\begin{pmatrix} J_{\lambda_1} & &\textit{--zeroes--} \\ &J_{\lambda_2} \\ & &\ddots \\ & & &J_{\lambda_{\ell-1}} \\ & &\textit{--zeroes--} & &J_{\lambda_{\ell}} \end{pmatrix}
$$

where each $$J_{\lambda}$$ is the Jordan block associated with the eigenvalue $$\lambda$$ of the original matrix (that is, is all zeroes except for $$\lambda$$'s down the diagonal and some subdiagonal ones).

**Proof**  —

Given an $$n \! \times \! n$$ matrix $$T$$, consider the linear map $$t:\mathbb{C}^n\to \mathbb{C}^n$$ that it represents with respect to the standard bases. Use the prior lemma to write $$\mathbb{C}^n=\mathcal{N}_\infty(t-\lambda_1)\oplus\cdots \oplus\mathcal{N}_\infty(t-\lambda_\ell)$$ where $$\lambda_1,\ldots,\lambda_\ell$$ are the eigenvalues of $$t$$. Because each $$\mathcal{N}_\infty(t-\lambda_i)$$ is $$t$$ invariant, Lemma 2.8 and the prior lemma show that $$t$$ is represented by a matrix that is all zeroes except for square blocks along the diagonal. To make those blocks into Jordan blocks, pick each $$B_{\lambda_i}$$ to be a string basis for the action of $$t-\lambda_i$$ on $$\mathcal{N}_\infty(t-\lambda_i)$$.

Jordan form is a canonical form for similarity classes of square matrices, provided that we make it unique by arranging the Jordan blocks from least eigenvalue to greatest and then arranging the subdiagonal $$1$$ blocks inside each Jordan block from longest to shortest.

**Example 2.13**  —

This matrix has the characteristic polynomial $$(x-2)^2(x-6)$$.

$$
T= \begin{pmatrix} 2 &0 &1 \\ 0 &6 &2 \\ 0 &0 &2 \end{pmatrix}
$$

We will handle the eigenvalues $$2$$ and $$6$$ separately.

Computation of the powers, and the null spaces and nullities, of $$T-2I$$ is routine. (Recall from Example 2.3 the convention of taking $$T$$ to represent a transformation, here $$t:\mathbb{C}^3\to \mathbb{C}^3$$, with respect to the standard basis.)

$$
\begin{array}{r|ccc} \textit{power} p & (T-2I)^p & \mathcal{N}((t-2)^p) &\textit{nullity} \\ \hline 1 & \begin{pmatrix} 0 &0 &1 \\ 0 &4 &2 \\ 0 &0 &0 \end{pmatrix} & \{\begin{pmatrix} x \\ 0 \\ 0 \end{pmatrix}\,\big|\, x\in\mathbb{C}\} &1 \\ 2 & \begin{pmatrix} 0 &0 &0 \\ 0 &16 &8 \\ 0 &0 &0 \end{pmatrix} & \{\begin{pmatrix} x \\ -z/2 \\ z \end{pmatrix}\,\big|\, x,z\in\mathbb{C}\} &2 \\ 3 & \begin{pmatrix} 0 &0 &0 \\ 0 &64 &32 \\ 0 &0 &0 \end{pmatrix} &\textit{--same--} &\textit{---} \end{array}
$$

So the generalized null space $$\mathcal{N}_\infty(t-2)$$ has dimension two. We've noted that the restriction of $$t-2$$ is nilpotent on this subspace. From the way that the nullities grow we know that the action of $$t-2$$ on a string basis $$\vec{\beta}_1\mapsto\vec{\beta}_2\mapsto\vec{0}$$. Thus the restriction can be represented in the canonical form

$$
N_2= \begin{pmatrix} 0 &0 \\ 1 &0 \end{pmatrix} ={\rm Rep}_{B,B}(t-2) \qquad B_2=\langle \begin{pmatrix} 1 \\ 1 \\ -2 \end{pmatrix}, \begin{pmatrix} -2 \\ 0 \\ 0 \end{pmatrix} \rangle
$$

where many choices of basis are possible. Consequently, the action of the restriction of $$t$$ to $$\mathcal{N}_\infty(t-2)$$ is represented by this matrix.

$$
J_2=N_2+2I={\rm Rep}_{B_2,B_2}(t)= \begin{pmatrix} 2 &0 \\ 1 &2 \end{pmatrix}
$$

The second eigenvalue's computations are easier. Because the power of $$x-6$$ in the characteristic polynomial is one, the restriction of $$t-6$$ to $$\mathcal{N}_\infty(t-6)$$ must be nilpotent of index one. Its action on a string basis must be $$\vec{\beta}_3\mapsto\vec{0}$$ and since it is the zero map, its canonical form $$N_6$$ is the $$1 \! \times \! 1$$ zero matrix. Consequently, the canonical form $$J_6$$ for the action of $$t$$ on $$\mathcal{N}_\infty(t-6)$$ is the $$1 \! \times \! 1$$ matrix with the single entry $$6$$. For the basis we can use any nonzero vector from the generalized null space.

$$
B_6=\langle \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} \rangle
$$

Taken together, these two give that the Jordan form of $$T$$ is

$$
{\rm Rep}_{B,B}(t)= \begin{pmatrix} 2 &0 &0 \\ 1 &2 &0 \\ 0 &0 &6 \end{pmatrix}
$$

where $$B$$ is the concatenation of $$B_2$$ and $$B_6$$.

**Example 2.14**  —

Contrast the prior example with

$$
T= \begin{pmatrix} 2 &2 &1 \\ 0 &6 &2 \\ 0 &0 &2 \end{pmatrix}
$$

which has the same characteristic polynomial $$(x-2)^2(x-6)$$.

While the characteristic polynomial is the same,

$$
\begin{array}{r|ccc} \textit{power} p & (T-2I)^p & \mathcal{N}((t-2)^p) &\textit{nullity} \\ \hline 1 & \begin{pmatrix} 0 &2 &1 \\ 0 &4 &2 \\ 0 &0 &0 \end{pmatrix} & \{\begin{pmatrix} x \\ -z/2 \\ z \end{pmatrix}\,\big|\, x,z\in\mathbb{C}\} &2 \\ 2 & \begin{pmatrix} 0 &8 &4 \\ 0 &16 &8 \\ 0 &0 &0 \end{pmatrix} &\textit{--same--} &\textit{---} \end{array}
$$

here the action of $$t-2$$ is stable after only one application— the restriction of of $$t-2$$ to $$\mathcal{N}_\infty(t-2)$$ is nilpotent of index only one. (So the contrast with the prior example is that while the characteristic polynomial tells us to look at the action of the $$t-2$$ on its generalized null space, the characteristic polynomial does not describe completely its action and we must do some computations to find, in this example, that the minimal polynomial is $$(x-2)(x-6)$$.) The restriction of $$t-2$$ to the generalized null space acts on a string basis as $$\vec{\beta}_1\mapsto\vec{0}$$ and $$\vec{\beta}_2\mapsto\vec{0}$$, and we get this Jordan block associated with the eigenvalue $$2$$.

$$
J_2= \begin{pmatrix} 2 &0 \\ 0 &2 \end{pmatrix}
$$

For the other eigenvalue, the arguments for the second eigenvalue of the prior example apply again. The restriction of $$t-6$$ to $$\mathcal{N}_\infty(t-6)$$ is nilpotent of index one (it can't be of index less than one, and since $$x-6$$ is a factor of the characteristic polynomial to the power one it can't be of index more than one either). Thus $$t-6$$'s canonical form $$N_6$$ is the $$1 \! \times \! 1$$ zero matrix, and the associated Jordan block $$J_6$$ is the $$1 \! \times \! 1$$ matrix with entry $$6$$.

Therefore, $$T$$ is diagonalizable.

$$
{\rm Rep}_{B,B}(t)= \begin{pmatrix} 2 &0 &0 \\ 0 &2 &0 \\ 0 &0 &6 \end{pmatrix} \qquad B=B_2\!\mathbin{{}^\frown}\!B_6 =\langle \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ -2 \end{pmatrix}, \begin{pmatrix} 3 \\ 4 \\ 0 \end{pmatrix} \rangle
$$

(Checking that the third vector in $$B$$ is in the nullspace of $$t-6$$ is routine.)

**Example 2.15**  —

A bit of computing with

$$
T= \begin{pmatrix} -1 &4 &0 &0 &0 \\ 0 &3 &0 &0 &0 \\ 0 &-4 &-1 &0 &0 \\ 3 &-9 &-4 &2 &-1 \\ 1 &5 &4 &1 &4 \end{pmatrix}
$$

shows that its characteristic polynomial is $$(x-3)^3(x+1)^2$$. This table

$$
\begin{array}{r|ccc} \textit{power} p & (T-3I)^p & \mathcal{N}((t-3)^p) &\textit{nullity} \\ \hline 1 &\begin{pmatrix} -4 &4 &0 &0 &0 \\ 0 &0 &0 &0 &0 \\ 0 &-4 &-4 &0 &0 \\ 3 &-9 &-4 &-1 &-1 \\ 1 &5 &4 &1 &1 \end{pmatrix} & \{\begin{pmatrix} -(u+v)/2 \\ -(u+v)/2 \\ (u+v)/2 \\ u \\ v \end{pmatrix}\,\big|\, u,v\in\mathbb{C}\} &2 \\ 2 &\begin{pmatrix} 16 &-16&0 &0 &0 \\ 0 &0 &0 &0 &0 \\ 0 &16 &16 &0 &0 \\ -16 &32 &16 &0 &0 \\ 0 &-16&-16&0 &0 \end{pmatrix} & \{\begin{pmatrix} -z \\ -z \\ z \\ u \\ v \end{pmatrix}\,\big|\, z,u,v\in\mathbb{C}\} &3 \\ 3 &\begin{pmatrix} -64 &64 &0 &0 &0 \\ 0 &0 &0 &0 &0 \\ 0 &-64 &-64 &0 &0 \\ 64 &-128 &-64 &0 &0 \\ 0 &64 &64 &0 &0 \end{pmatrix} &\textit{--same--} &\textit{---} \end{array}
$$

shows that the restriction of $$t-3$$ to $$\mathcal{N}_\infty(t-3)$$ acts on a string basis via the two strings $$\vec{\beta}_1\mapsto\vec{\beta}_2\mapsto\vec{0}$$ and $$\vec{\beta}_3\mapsto\vec{0}$$.

A similar calculation for the other eigenvalue

$$
\begin{array}{r|ccc} \textit{power} p & (T+1I)^p & \mathcal{N}((t+1)^p) &\textit{nullity} \\ \hline 1 &\begin{pmatrix} 0 &4 &0 &0 &0 \\ 0 &4 &0 &0 &0 \\ 0 &-4 &0 &0 &0 \\ 3 &-9 &-4 &3 &-1 \\ 1 &5 &4 &1 &5 \end{pmatrix} & \{\begin{pmatrix} -(u+v) \\ 0 \\ -v \\ u \\ v \end{pmatrix}\,\big|\, u,v\in\mathbb{C}\} &2 \\ 2 &\begin{pmatrix} 0 &16 &0 &0 &0 \\ 0 &16 &0 &0 &0 \\ 0 &-16&0 &0 &0 \\ 8 &-40&-16&8 &-8 \\ 8 &24 &16 &8 &24 \end{pmatrix} &\textit{--same--} &\textit{---} \end{array}
$$

shows that the restriction of $$t+1$$ to its generalized null space acts on a string basis via the two separate strings $$\vec{\beta}_4\mapsto\vec{0}$$ and $$\vec{\beta}_5\mapsto\vec{0}$$.

Therefore $$T$$ is similar to this Jordan form matrix.

$$
\begin{pmatrix} -1 &0 &0 &0 &0 \\ 0 &-1 &0 &0 &0 \\ 0 &0 &3 &0 &0 \\ 0 &0 &1 &3 &0 \\ 0 &0 &0 &0 &3 \end{pmatrix}
$$

We close with the statement that the subjects considered earlier in this Chpater are indeed, in this sense, exhaustive.

**Corollary 2.16**  —

Every square matrix is similar to the sum of a diagonal matrix and a nilpotent matrix.

### Exercises

**Problem 1**  —

Do the check for Example 2.3.

**Problem 2**  —

Each matrix is in Jordan form. State its characteristic polynomial and its minimal polynomial.

1. $$\begin{pmatrix} 3 &0 \\ 1 &3 \end{pmatrix}$$
2. $$\begin{pmatrix} -1 &0 \\ 0 &-1 \end{pmatrix}$$
3. $$\begin{pmatrix} 2 &0 &0 \\ 1 &2 &0 \\ 0 &0 &-1/2 \end{pmatrix}$$
4. $$\begin{pmatrix} 3 &0 &0 \\ 1 &3 &0 \\ 0 &1 &3 \\ \end{pmatrix}$$
5. $$\begin{pmatrix} 3 &0 &0 &0 \\ 1 &3 &0 &0 \\ 0 &0 &3 &0 \\ 0 &0 &1 &3 \end{pmatrix}$$
6. $$\begin{pmatrix} 4 &0 &0 &0 \\ 1 &4 &0 &0 \\ 0 &0 &-4 &0 \\ 0 &0 &1 &-4 \end{pmatrix}$$
7. $$\begin{pmatrix} 5 &0 &0 \\ 0 &2 &0 \\ 0 &0 &3 \end{pmatrix}$$
8. $$\begin{pmatrix} 5 &0 &0 &0 \\ 0 &2 &0 &0 \\ 0 &0 &2 &0 \\ 0 &0 &0 &3 \end{pmatrix}$$
9. $$\begin{pmatrix} 5 &0 &0 &0 \\ 0 &2 &0 &0 \\ 0 &1 &2 &0 \\ 0 &0 &0 &3 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

Find the Jordan form from the given data.

1. The matrix $$T$$ is $$5 \! \times \! 5$$ with the single eigenvalue $$3$$. The nullities of the powers are: $$T-3I$$ has nullity two, $$(T-3I)^2$$ has nullity three, $$(T-3I)^3$$ has nullity four, and $$(T-3I)^4$$ has nullity five.
2. The matrix $$S$$ is $$5 \! \times \! 5$$ with two eigenvalues. For the eigenvalue $$2$$ the nullities are: $$S-2I$$ has nullity two, and $$(S-2I)^2$$ has nullity four. For the eigenvalue $$-1$$ the nullities are: $$S+1I$$ has nullity one.

**Problem 4**  —

Find the change of basis matrices for each example.

1. Example 2.13
2. Example 2.14
3. Example 2.15  
*This exercise is recommended for all readers.*

**Problem 5**  —

Find the Jordan form and a Jordan basis for each matrix.

1. $$\begin{pmatrix} -10 &4 \\ -25 &10 \end{pmatrix}$$
2. $$\begin{pmatrix} 5 &-4 \\ 9 &-7 \end{pmatrix}$$
3. $$\begin{pmatrix} 4 &0 &0 \\ 2 &1 &3 \\ 5 &0 &4 \end{pmatrix}$$
4. $$\begin{pmatrix} 5 &4 &3 \\ -1 &0 &-3 \\ 1 &-2 &1 \end{pmatrix}$$
5. $$\begin{pmatrix} 9 &7 &3 \\ -9 &-7 &-4 \\ 4 &4 &4 \end{pmatrix}$$
6. $$\begin{pmatrix} 2 &2 &-1 \\ -1 &-1 &1 \\ -1 &-2 &2 \end{pmatrix}$$
7. $$\begin{pmatrix} 7 &1 &2 &2 \\ 1 &4 &-1 &-1\\ -2 &1 &5 &-1\\ 1 &1 &2 &8 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 6**  —

Find all possible Jordan forms of a transformation with characteristic polynomial $$(x-1)^2(x+2)^2$$.

**Problem 7**  —

Find all possible Jordan forms of a transformation with characteristic polynomial $$(x-1)^3(x+2)$$.  
*This exercise is recommended for all readers.*

**Problem 8**  —

Find all possible Jordan forms of a transformation with characteristic polynomial $$(x-2)^3(x+1)$$ and minimal polynomial $$(x-2)^2(x+1)$$.

**Problem 9**  —

Find all possible Jordan forms of a transformation with characteristic polynomial $$(x-2)^4(x+1)$$ and minimal polynomial $$(x-2)^2(x+1)$$.  
*This exercise is recommended for all readers.*

**Problem 10**  — Diagonalize these.

1. $$\begin{pmatrix} 1 &1 \\ 0 &0 \end{pmatrix}$$
2. $$\begin{pmatrix} 0 &1 \\ 1 &0 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 11**  —

Find the Jordan matrix representing the differentiation operator on $$\mathcal{P}_3$$.  
*This exercise is recommended for all readers.*

**Problem 12**  —

Decide if these two are similar.

$$
\begin{pmatrix} 1 &-1 \\ 4 &-3 \\ \end{pmatrix} \qquad \begin{pmatrix} -1 &0 \\ 1 &-1 \\ \end{pmatrix}
$$

**Problem 13**  —

Find the Jordan form of this matrix.

$$
\begin{pmatrix} 0 &-1 \\ 1 &0 \end{pmatrix}
$$

Also give a Jordan basis.

**Problem 14**  —

How many similarity classes are there for $$3 \! \times \! 3$$ matrices whose only eigenvalues are $$-3$$ and $$4$$?  
*This exercise is recommended for all readers.*

**Problem 15**  —

Prove that a matrix is diagonalizable if and only if its minimal polynomial has only linear factors.

**Problem 16**  —

Give an example of a linear transformation on a vector space that has no non-trivial invariant subspaces.

**Problem 17**  —

Show that a subspace is $$t-\lambda_1$$ invariant if and only if it is $$t-\lambda_2$$ invariant.

**Problem 18**  —

Prove or disprove: two $$n \! \times \! n$$ matrices are similar if and only if they have the same characteristic and minimal polynomials.

**Problem 19**  —

The **trace** of a square matrix is the sum of its diagonal entries.

1. Find the formula for the characteristic polynomial of a $$2 \! \times \! 2$$ matrix.
2. Show that trace is invariant under similarity, and so we can sensibly speak of the "trace of a map". (*Hint:* see the prior item.)
3. Is trace invariant under matrix equivalence?
4. Show that the trace of a map is the sum of its eigenvalues (counting multiplicities).
5. Show that the trace of a nilpotent map is zero. Does the converse hold?

**Problem 20**  —

To use Definition 2.6 to check whether a subspace is $$t$$ invariant, we seemingly have to check all of the infinitely many vectors in a (nontrivial) subspace to see if they satisfy the condition. Prove that a subspace is $$t$$ invariant if and only if its subbasis has the property that for all of its elements, $$t(\vec{\beta})$$ is in the subspace.  
*This exercise is recommended for all readers.*

**Problem 21**  —

Is $$t$$ invariance preserved under intersection? Under union? Complementation? Sums of subspaces?

**Problem 22**  —

Give a way to order the Jordan blocks if some of the eigenvalues are complex numbers. That is, suggest a reasonable ordering for the complex numbers.

**Problem 23**  —

Let $$\mathcal{P}_j(\mathbb{R})$$ be the vector space over the reals of degree $$j$$ polynomials. Show that if $$j\le k$$ then $$\mathcal{P}_j(\mathbb{R})$$ is an invariant subspace of $$\mathcal{P}_k(\mathbb{R})$$ under the differentiation operator. In $$\mathcal{P}_7(\mathbb{R})$$, does any of $$\mathcal{P}_0(\mathbb{R})$$, ..., $$\mathcal{P}_6(\mathbb{R})$$ have an invariant complement?

**Problem 24**  —

In $$\mathcal{P}_n(\mathbb{R})$$, the vector space (over the reals) of degree $$n$$ polynomials,

$$
\mathcal{E}= \{p(x)\in\mathcal{P}_n(\mathbb{R})\,\big|\, p(-x)=p(x) \text{ for all }x\}
$$

and

$$
\mathcal{O}= \{p(x)\in\mathcal{P}_n(\mathbb{R})\,\big|\, p(-x)=-p(x) \text{ for all }x\}
$$

are the **even** and the **odd** polynomials; $$p(x)=x^2$$ is even while $$p(x)=x^3$$ is odd. Show that they are subspaces. Are they complementary? Are they invariant under the differentiation transformation?

**Problem 25**  —

Lemma 2.8 says that if $$M$$ and $$N$$ are invariant complements then $$t$$ has a representation in the given block form (with respect to the same ending as starting basis, of course). Does the implication reverse?

**Problem 26**  —

A matrix $$S$$ is the **square root** of another $$T$$ if $$S^2=T$$. Show that any nonsingular matrix has a square root.

Solutions

### Footnotes

---

*Source: Wikibooks, Linear Algebra/Jordan Canonical Form (https://en.wikibooks.org/wiki/Linear_Algebra/Jordan_Canonical_Form), by Wikibooks contributors, CC BY-SA 4.0.*
