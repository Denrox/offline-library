# Unitary and Hermitian matrices

#### Unitary Matrices

Of considerable interest are linear maps that are "isometric", also known as "distance preserving maps". Such a map is also called an "isometry". Let $$u:\Complex^n \to \Complex^n$$ denote an arbitrary isometric linear map. Recall from the chapter on [orthonormal matrices](Linear%20Algebra%20-%20Topic%20Orthonormal%20Matrices.md) that any isometric map that maps $$\vec{0}$$ to $$\vec{0}$$ is linear.

The distance preserving nature of isometries also means that angles are preserved. If $$\vec{a},\vec{b} \in \Complex^n$$ are arbitrary vectors, then the dot product is preserved by isometric transformations: $$u(\vec{a}) \cdot u(\vec{b}) = \vec{a} \cdot \vec{b}$$.

The standard basis vectors for $$\Complex^n$$, $$\vec{e}_1, \vec{e}_2, \dots, \vec{e}_n$$, are all of unit length and are all mutually orthogonal: $$\vec{e}_i \cdot \vec{e}_j = \left\{\begin{array}{cc} 1 & (i = j) \\ 0 & (i \neq j)\end{array}\right.$$

If $$U = \text{Rep}(u) = \begin{pmatrix}\vec{u}_1 & \vec{u}_2 & \dots & \vec{u}_n \\ \end{pmatrix}$$ is the matrix that describes the isometric linear map $$u$$, then the columns $$\vec{u}_i = u(\vec{e}_i)$$ are also all of unit length and are all mutually orthogonal: $$\vec{u}_i \cdot \vec{u}_j = \left\{\begin{array}{cc} 1 & (i = j) \\ 0 & (i \neq j)\end{array}\right.$$

The "Hermitian Transpose" of a matrix is the transpose with the conjugation of complex numbers applied on top:

$$
\begin{pmatrix} a_{1,1} & a_{1,2} & \dots & a_{1,m} \\ a_{2,1} & a_{2,2} & \dots & a_{2,m} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n,1} & a_{n,2} & \dots & a_{n,m} \\ \end{pmatrix}^H = \begin{pmatrix} a_{1,1}^* & a_{2,1}^* & \dots & a_{n,1}^* \\ a_{1,2}^* & a_{2,2}^* & \dots & a_{n,2}^* \\ \vdots & \vdots & \ddots & \vdots \\ a_{1,m}^* & a_{2,m}^* & \dots & a_{n,m}^* \\ \end{pmatrix}
$$

The orthonormal properties of the columns of $$U$$ imply that the inverse of $$U$$ is simply its Hermitian transpose: $$U^{-1} = U^H$$. Any matrix whose inverse is its Hermitian transpose is referred to as being "unitary". The key property of a unitary matrix $$U$$ is that $$U$$ be square and that $$U^HU = UU^H = I$$ (note that $$I = \text{Rep}(\text{id})$$ is the identity matrix). Unitary matrices denote isometric linear maps.

#### Hermitian matrices

Given a square $$n \times n$$ matrix $$A$$, analogous to how $$A$$ is symmetric if $$A^T = A$$, $$A$$ is Hermitian if $$A^H = A$$, meaning that diagonally opposite entries of $$A$$ are complex conjugates of each other.

For example, $$A = \begin{pmatrix} 4 & 6i \\ 6i & 5 \end{pmatrix}$$ is symmetric but not Hermitian, but $$A = \begin{pmatrix} 4 & 6i \\ -6i & 5 \end{pmatrix}$$ is Hermitian but not symmetric.

#### Quadratic forms

Given a square $$n \times n$$ matrix $$A$$ with real valued entries, the function $$Q(\vec{x}) = \vec{x}^TA\vec{x}$$ is a quadratic function over the entries of $$\vec{x} \in \R^n$$, referred to as a "quadratic form". All terms in a quadratic form have degree 2. For instance, given the quadratic form $$Q(x_1, x_2) = 4x_1^2 - 7x_1x_2 + 5x_2^2$$, $$Q(x_1, x_2)$$ can be expressed as:

$$
Q\begin{pmatrix} x_1 \\ x_2 \\ \end{pmatrix} = \begin{pmatrix} x_1 & x_2 \\ \end{pmatrix} \begin{pmatrix} 4 & -7 \\ 0 & 5 \\ \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \end{pmatrix}
$$

or as

$$
Q\begin{pmatrix} x_1 \\ x_2 \\ \end{pmatrix} = \begin{pmatrix} x_1 & x_2 \\ \end{pmatrix} \begin{pmatrix} 4 & -3.5 \\ -3.5 & 5 \\ \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \end{pmatrix}
$$

The coefficient of the term $$x_ix_j$$ for $$i \neq j$$ is the sum of the $$(i,j)$$ and $$(j,i)$$ entries. It then becomes sensible to split the coefficient of $$x_ix_j$$ between the $$(i,j)$$ and $$(j,i)$$ entries, in essence requiring $$A$$ to be symmetric: $$A^T = A$$.

Generalizing to complex numbers, consider the quadratic form $$Q(\vec{x}) = \vec{x}^HA\vec{x}$$, where $$\vec{x} \in \Complex^n$$ is arbitrary. Requiring that $$A$$ be Hermitian is similar to the requirement that $$A$$ be symmetric in the case of real numbers. $$Q(\vec{x})$$ always returns a real number if $$A$$ is Hermitian:

**Theorem**  —

If $$A$$ is Hermitian, then the quadratic form $$Q(\vec{x}) = \vec{x}^HA\vec{x}$$ always returns a real number.

**Proof**  —

$$
\forall\vec{x}\in\Complex^n : \vec{x}^HA\vec{x} \in \R \iff \forall\vec{x}\in\Complex^n : \vec{x}^HA\vec{x} = (\vec{x}^HA\vec{x})^* \iff \forall\vec{x}\in\Complex^n : \vec{x}^HA\vec{x} = \vec{x}^HA^H\vec{x}
$$

Since $$A^H = A$$ due to $$A$$ being Hermitian, $$Q(\vec{x})$$ always returns a real number.

---

*Source: Wikibooks, Linear Algebra/Unitary and Hermitian matrices (https://en.wikibooks.org/wiki/Linear_Algebra/Unitary_and_Hermitian_matrices), by Wikibooks contributors, CC BY-SA 4.0.*
