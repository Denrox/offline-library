# Reduced Echelon Form

After developing the mechanics of Gauss' method, we observed that it can be done in more than one way. One example is that we sometimes have to swap rows and there can be more than one row to choose from. Another example is that from this matrix

$$
\begin{pmatrix} 2 &2 \\ 4 &3 \end{pmatrix}
$$

Gauss' method could derive any of these echelon form matrices.

$$
\begin{pmatrix} 2 &2 \\ 0 &-1 \end{pmatrix} \qquad \begin{pmatrix} 1 &1 \\ 0 &-1 \end{pmatrix} \qquad \begin{pmatrix} 2 &0 \\ 0 &-1 \end{pmatrix}
$$

The first results from $$-2\rho_1+\rho_2$$. The second comes from following $$(1/2)\rho_1$$ with $$-4\rho_1+\rho_2$$. The third comes from $$-2\rho_1+\rho_2$$ followed by $$2\rho_2+\rho_1$$ (after the first pivot the matrix is already in echelon form so the second one is extra work but it is nonetheless a legal row operation).

The fact that the echelon form outcome of Gauss' method is not unique leaves us with some questions. Will any two echelon form versions of a system have the same number of free variables? Will they in fact have exactly the same variables free? In this section we will answer both questions "yes". We will do more than answer the questions. We will give a way to decide if one linear system can be derived from another by row operations. The answers to the two questions will follow from this larger result.

---

*Source: Wikibooks, Linear Algebra/Reduced Echelon Form (https://en.wikibooks.org/wiki/Linear_Algebra/Reduced_Echelon_Form), by Wikibooks contributors, CC BY-SA 4.0.*
