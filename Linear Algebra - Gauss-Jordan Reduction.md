# Gauss-Jordan Reduction

Gaussian elimination coupled with back-substitution solves linear systems, but it's not the only method possible. Here is an extension of Gauss' method that has some advantages.

**Example 1.1**  —

To solve

$$
\begin{array}{rcrcrcr} x &+ &y &- &2z &= &-2 \\ & &y &+ &3z &= &7 \\ x & & &- &z &= &-1 \end{array}
$$

we can start by going to echelon form as usual.

$$
\xrightarrow[]{-\rho_1+\rho_3} \left(\begin{array}{ccc|c} 1 &1 &-2 &-2 \\ 0 &1 &3 &7 \\ 0 &-1 &1 &1 \end{array}\right) \xrightarrow[]{\rho_2+\rho_3} \left(\begin{array}{ccc|c} 1 &1 &-2 &-2 \\ 0 &1 &3 &7 \\ 0 &0 &4 &8 \end{array}\right)
$$

We can keep going to a second stage by making the leading entries into ones

$$
\xrightarrow[]{(1/4)\rho_3} \left(\begin{array}{ccc|c} 1 &1 &-2 &-2 \\ 0 &1 &3 &7 \\ 0 &0 &1 &2 \end{array}\right)
$$

and then to a third stage that uses the leading entries to eliminate all of the other entries in each column by pivoting upwards.

$$
\xrightarrow[2\rho_3+\rho_1]{-3\rho_3+\rho_2} \left(\begin{array}{ccc|c} 1 &1 &0 &2 \\ 0 &1 &0 &1 \\ 0 &0 &1 &2 \end{array}\right) \xrightarrow[]{-\rho_2+\rho_1} \left(\begin{array}{ccc|c} 1 &0 &0 &1 \\ 0 &1 &0 &1 \\ 0 &0 &1 &2 \end{array}\right)
$$

The answer is $$x=1$$, $$y=1$$, and $$z=2$$.

Note that the pivot operations in the first stage proceed from column one to column three while the pivot operations in the third stage proceed from column three to column one.

**Example 1.2**  —

We often combine the operations of the middle stage into a single step, even though they are operations on different rows.

$$
\begin{array}{rcl} \left(\begin{array}{cc|c} 2 &1 &7 \\ 4 &-2 &6 \end{array}\right) &\xrightarrow[]{-2\rho_1+\rho_2} &\left(\begin{array}{cc|c} 2 &1 &7 \\ 0 &-4 &-8 \end{array}\right) \\ &\xrightarrow[(-1/4)\rho_2]{(1/2)\rho_1} &\left(\begin{array}{cc|c} 1 &1/2 &7/2 \\ 0 &1 &2 \end{array}\right) \\ &\xrightarrow[]{-(1/2)\rho_2+\rho_1} &\left(\begin{array}{cc|c} 1 &0 &5/2 \\ 0 &1 &2 \end{array}\right) \end{array}
$$

The answer is $$x=5/2$$ and $$y=2$$.

This extension of Gauss' method is **Gauss-Jordan reduction**. It goes past echelon form to a more refined, more specialized, matrix form.

**Definition 1.3**  —

A matrix is in **reduced echelon form** if, in addition to being in echelon form, each leading entry is a one and is the only nonzero entry in its column.

The disadvantage of using Gauss-Jordan reduction to solve a system is that the additional row operations mean additional arithmetic. The advantage is that the solution set can just be read off.

In any echelon form, plain or reduced, we can read off when a system has an empty solution set because there is a contradictory equation, we can read off when a system has a one-element solution set because there is no contradiction and every variable is the leading variable in some row, and we can read off when a system has an infinite solution set because there is no contradiction and at least one variable is free.

In reduced echelon form we can read off not just what kind of solution set the system has, but also its description. Whether or not the echelon form is reduced, we have no trouble describing the solution set when it is empty, of course. The two examples above show that when the system has a single solution then the solution can be read off from the right-hand column. In the case when the solution set is infinite, its parametrization can also be read off of the reduced echelon form. Consider, for example, this system that is shown brought to echelon form and then to reduced echelon form.

$$
\left(\begin{array}{cccc|c} 2 &6 &1 &2 &5 \\ 0 &3 &1 &4 &1 \\ 0 &3 &1 &2 &5 \end{array}\right) \xrightarrow[]{-\rho_2+\rho_3} \left(\begin{array}{cccc|c} 2 &6 &1 &2 &5 \\ 0 &3 &1 &4 &1 \\ 0 &0 &0 &-2 &4 \end{array}\right)
$$

$$
\xrightarrow[\begin{array}{c}\\[-19pt]\scriptstyle (1/3)\rho_2 \\[-5pt]\scriptstyle -(1/2)\rho_3\end{array}]{(1/2)\rho_1} \;\xrightarrow[-\rho_3+\rho_1]{(4/3)\rho_3+\rho_2} \;\xrightarrow[]{-3\rho_2+\rho_1} \left(\begin{array}{cccc|c} 1 &0 &-1/2 &0 &-9/2 \\ 0 &1 &1/3 &0 &3 \\ 0 &0 &0 &1 &-2 \end{array}\right)
$$

Starting with the middle matrix, the echelon form version, back substitution produces $$-2x_4=4$$ so that $$x_4=-2$$, then another back substitution gives $$3x_2+x_3+4(-2)=1$$ implying that $$x_2=3-(1/3)x_3$$, and then the final back substitution gives $$2x_1+6(3-(1/3)x_3)+x_3+2(-2)=5$$ implying that $$x_1=-(9/2)+(1/2)x_3$$. Thus the solution set is this.

$$
S=\{\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} =\begin{pmatrix} -9/2 \\ 3 \\ 0 \\ -2 \end{pmatrix} +\begin{pmatrix} 1/2 \\ -1/3 \\ 1 \\ 0 \end{pmatrix}x_3 \,\big|\, x_3\in\mathbb{R}\}
$$

Now, considering the final matrix, the reduced echelon form version, note that adjusting the parametrization by moving the $$x_3$$ terms to the other side does indeed give the description of this infinite solution set.

Part of the reason that this works is straightforward. While a set can have many parametrizations that describe it, e.g., both of these also describe the above set $$S$$ (take $$t$$ to be $$x_3/6$$ and $$s$$ to be $$x_3-1$$)

$$
\{\begin{pmatrix} -9/2 \\ 3 \\ 0 \\ -2 \end{pmatrix} +\begin{pmatrix} 3 \\ -2 \\ 6 \\ 0 \end{pmatrix}t \,\big|\, t\in\mathbb{R}\} \qquad \{\begin{pmatrix} -4 \\ 8/3 \\ 1 \\ -2 \end{pmatrix} +\begin{pmatrix} 1/2 \\ -1/3 \\ 1 \\ 0 \end{pmatrix}s \,\big|\, s\in\mathbb{R}\}
$$

nonetheless we have in this book stuck to a convention of parametrizing using the unmodified free variables (that is, $$x_3=x_3$$ instead of $$x_3=6t$$). We can easily see that a reduced echelon form version of a system is equivalent to a parametrization in terms of unmodified free variables. For instance,

$$
\begin{array}{rl} x_1 &=4-2x_3 \\ x_2 &=3-x_3 \end{array} \quad\Longleftrightarrow\quad \left(\begin{array}{ccc|c} 1 &0 &2 &4 \\ 0 &1 &1 &3 \\ 0 &0 &0 &0 \end{array}\right)
$$

(to move from left to right we also need to know how many equations are in the system). So, the convention of parametrizing with the free variables by solving each equation for its leading variable and then eliminating that leading variable from every other equation is exactly equivalent to the reduced echelon form conditions that each leading entry must be a one and must be the only nonzero entry in its column.

Not as straightforward is the other part of the reason that the reduced echelon form version allows us to read off the parametrization that we would have gotten had we stopped at echelon form and then done back substitution. The prior paragraph shows that reduced echelon form corresponds to some parametrization, but why the same parametrization? A solution set can be parametrized in many ways, and Gauss' method or the Gauss-Jordan method can be done in many ways, so a first guess might be that we could derive many different reduced echelon form versions of the same starting system and many different parametrizations. But we never do. Experience shows that starting with the same system and proceeding with row operations in many different ways always yields the same reduced echelon form and the same parametrization (using the unmodified free variables).

In the rest of this section we will show that the reduced echelon form version of a matrix is unique. It follows that the parametrization of a linear system in terms of its unmodified free variables is unique because two different ones would give two different reduced echelon forms.

We shall use this result, and the ones that lead up to it, in the rest of the book but perhaps a restatement in a way that makes it seem more immediately useful may be encouraging. Imagine that we solve a linear system, parametrize, and check in the back of the book for the answer. But the parametrization there appears different. Have we made a mistake, or could these be different-looking descriptions of the same set, as with the three descriptions above of $$S$$? The prior paragraph notes that we will show here that different-looking parametrizations (using the unmodified free variables) describe genuinely different sets.

Here is an informal argument that the reduced echelon form version of a matrix is unique. Consider again the example that started this section of a matrix that reduces to three different echelon form matrices. The first matrix of the three is the natural echelon form version. The second matrix is the same as the first except that a row has been halved. The third matrix, too, is just a cosmetic variant of the first. The definition of reduced echelon form outlaws this kind of fooling around. In reduced echelon form, halving a row is not possible because that would change the row's leading entry away from one, and neither is combining rows possible, because then a leading entry would no longer be alone in its column.

This informal justification is not a proof; we have argued that no two different reduced echelon form matrices are related by a single row operation step, but we have not ruled out the possibility that multiple steps might do. Before we go to that proof, we finish this subsection by rephrasing our work in a terminology that will be enlightening.

Many different matrices yield the same reduced echelon form matrix. The three echelon form matrices from the start of this section, and the matrix they were derived from, all give this reduced echelon form matrix.

$$
\begin{pmatrix} 1 &0 \\ 0 &1 \end{pmatrix}
$$

We think of these matrices as related to each other. The next result speaks to this relationship.

**Lemma 1.4**  —

Elementary row operations are reversible.

**Proof**  —

For any matrix $$A$$, the effect of swapping rows is reversed by swapping them back, multiplying a row by a nonzero $$k$$ is undone by multiplying by $$1/k$$, and adding a multiple of row $$i$$ to row $$j$$ (with $$i\neq j$$) is undone by subtracting the same multiple of row $$i$$ from row $$j$$.

$$
A \xrightarrow[]{\rho_i\leftrightarrow\rho_j} \;\xrightarrow[]{\rho_j\leftrightarrow\rho_i} A \qquad A \xrightarrow[]{k\rho_i} \;\xrightarrow[]{(1/k)\rho_i} A \qquad A \xrightarrow[]{k\rho_i+\rho_j} \;\xrightarrow[]{-k\rho_i+\rho_j} A
$$

(The $$i\neq j$$ conditions is needed. See Problem 7.)

This lemma suggests that "reduces to" is misleading— where $$A\longrightarrow B$$, we shouldn't think of $$B$$ as "after" $$A$$ or "simpler than" $$A$$. Instead we should think of them as interreducible or interrelated. Below is a picture of the idea. The matrices from the start of this section and their reduced echelon form version are shown in a cluster. They are all interreducible; these relationships are shown also.

We say that matrices that reduce to each other are "equivalent with respect to the relationship of row reducibility". The next result verifies this statement using the definition of an equivalence.

**Lemma 1.5**  —

Between matrices, "reduces to" is an equivalence relation.

**Proof**  —

We must check the conditions (i) reflexivity, that any matrix reduces to itself, (ii) symmetry, that if $$A$$ reduces to $$B$$ then $$B$$ reduces to $$A$$, and (iii) transitivity, that if $$A$$ reduces to $$B$$ and $$B$$ reduces to $$C$$ then $$A$$ reduces to $$C$$.

Reflexivity is easy; any matrix reduces to itself in zero row operations.

That the relationship is symmetric is Lemma 1.4— if $$A$$ reduces to $$B$$ by some row operations then also $$B$$ reduces to $$A$$ by reversing those operations.

For transitivity, suppose that $$A$$ reduces to $$B$$ and that $$B$$ reduces to $$C$$. Linking the reduction steps from $$A \rightarrow\cdots\rightarrow B$$ with those from $$B \rightarrow\cdots\rightarrow C$$ gives a reduction from $$A$$ to $$C$$.

**Definition 1.6**  —

Two matrices that are interreducible by the elementary row operations are **row equivalent**.

The diagram below shows the collection of all matrices as a box. Inside that box, each matrix lies in some class. Matrices are in the same class if and only if they are interreducible. The classes are disjoint— no matrix is in two distinct classes. The collection of matrices has been partitioned into **row equivalence classes**.

One of the classes in this partition is the cluster of matrices shown above, expanded to include all of the nonsingular $$2 \! \times \! 2$$ matrices.

The next subsection proves that the reduced echelon form of a matrix is unique; that every matrix reduces to one and only one reduced echelon form matrix. Rephrased in terms of the row-equivalence relationship, we shall prove that every matrix is row equivalent to one and only one reduced echelon form matrix. In terms of the partition what we shall prove is: every equivalence class contains one and only one reduced echelon form matrix. So each reduced echelon form matrix serves as a representative of its class.

After that proof we shall, as mentioned in the introduction to this section, have a way to decide if one matrix can be derived from another by row reduction. We just apply the Gauss-Jordan procedure to both and see whether or not they come to the same reduced echelon form.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Use Gauss-Jordan reduction to solve each system.

1. $$\begin{array}{rcrcr} x &+ &y &= &2 \\ x &- &y &= &0 \end{array}$$
2. $$\begin{array}{rcrcrcr} x & & &- &z &= &4 \\ 2x &+ &2y & & &= &1 \end{array}$$
3. $$\begin{array}{rcrcr} 3x &- &2y &= &1 \\ 6x &+ &y &= &1/2 \end{array}$$
4. $$\begin{array}{rcrcrcr} 2x &- &y & & &= &-1 \\ x &+ &3y &- &z &= &5 \\ & &y &+ &2z&= &5 \end{array}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Find the reduced echelon form of each matrix.

1. $$\begin{pmatrix} 2 &1 \\ 1 &3 \end{pmatrix}$$
2. $$\begin{pmatrix} 1 &3 &1 \\ 2 &0 &4 \\ -1 &-3 &-3 \end{pmatrix}$$
3. $$\begin{pmatrix} 1 &0 &3 &1 &2 \\ 1 &4 &2 &1 &5 \\ 3 &4 &8 &1 &2 \end{pmatrix}$$
4. $$\begin{pmatrix} 0 &1 &3 &2 \\ 0 &0 &5 &6 \\ 1 &5 &1 &5 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

Find each solution set by using Gauss-Jordan reduction, then reading off the parametrization.

1. $$\begin{array}{rcrcrcr} 2x &+ &y &- &z &= &1 \\ 4x &- &y & & &= &3 \end{array}$$
2. $$\begin{array}{rcrcrcrcr} x & & &- &z & & &= &1 \\ & &y &+ &2z &- &w &= &3 \\ x &+ &2y &+ &3z &- &w &= &7 \end{array}$$
3. $$\begin{array}{rcrcrcrcr} x &- &y &+ &z & & &= &0 \\ & &y & & &+ &w &= &0 \\ 3x &- &2y &+ &3z &+ &w &= &0 \\ & &-y & & &- &w &= &0 \end{array}$$
4. $$\begin{array}{rcrcrcrcrcr} a &+ &2b &+ &3c &+ &d &- &e &= &1 \\ 3a &- &b &+ &c &+ &d &+ &e &= &3 \end{array}$$

**Problem 4**  —

Give two distinct echelon form versions of this matrix.

$$
\begin{pmatrix} 2 &1 &1 &3 \\ 6 &4 &1 &2 \\ 1 &5 &1 &5 \end{pmatrix}
$$

*This exercise is recommended for all readers.*

**Problem 5**  —

List the reduced echelon forms possible for each size.

1. $$2 \! \times \! 2$$
2. $$2 \! \times \! 3$$
3. $$3 \! \times \! 2$$
4. $$3 \! \times \! 3$$  
*This exercise is recommended for all readers.*

**Problem 6**  —

What results from applying Gauss-Jordan reduction to a nonsingular matrix?

**Problem 7**  —

The proof of Lemma 1.4 contains a reference to the $$i\neq j$$ condition on the row pivoting operation.

1. The definition of row operations has an $$i\neq j$$ condition on the swap operation $$\rho_i\leftrightarrow\rho_j$$. Show that in $$A\xrightarrow[]{\rho_i\leftrightarrow\rho_j}\; \xrightarrow[]{\rho_i\leftrightarrow\rho_j}A$$ this condition is not needed.
2. Write down a $$2 \! \times \! 2$$ matrix with nonzero entries, and show that the $$-1\cdot\rho_1+\rho_1$$ operation is not reversed by $$1\cdot\rho_1+\rho_1$$.
3. Expand the proof of that lemma to make explicit exactly where the $$i\neq j$$ condition on pivoting is used.

Solutions  
### Footnotes

---

*Source: Wikibooks, Linear Algebra/Gauss-Jordan Reduction (https://en.wikibooks.org/wiki/Linear_Algebra/Gauss-Jordan_Reduction), by Wikibooks contributors, CC BY-SA 4.0.*
