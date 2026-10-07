# Singular Value Decomposition

#### Singular Value Decomposition

Given any $$m \times n$$ matrix $$A$$, the singular value decomposition (SVD) is $$A = U\Sigma V^H$$ where $$U$$ is an $$m \times m$$ unitary matrix, $$V$$ is an $$n \times n$$ unitary matrix, and $$\Sigma$$ is an $$m \times n$$ diagonal matrix where all off-diagonal entries are 0 and the diagonal entries are all non-negative real values. The diagonal entries of $$\Sigma$$ are referred to as "singular values".

As an example, consider the shear transformation $$A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ \end{pmatrix}$$. The singular value decomposition of $$A$$ is:

$$
\begin{pmatrix} 1 & 2 \\ 0 & 1 \\ \end{pmatrix} = \begin{pmatrix} 0.9239 & -0.3827 \\ 0.3827 & 0.9239 \\ \end{pmatrix} \begin{pmatrix} 2.4142 & 0 \\ 0 & 0.4142 \\ \end{pmatrix} \begin{pmatrix} 0.3827 & 0.9239 \\ -0.9239 & 0.3827 \\ \end{pmatrix}
$$

The set of all unit length vectors $$\vec{v}$$ such that $$|\vec{v}| = 1$$ form a sphere of radius 1 around the origin. When $$A$$ is applied to this sphere, it becomes an ellipsoid. The principal radii of this ellipsoid are the singular values, and their directions form the columns of $$U$$.  
#### Existence of the singular value decomposition

One fact that is not immediately obvious is that the singular value decomposition always exists:

**Theorem (existence of the singular value decomposition)**  —

Given **any** $$m \times n$$ matrix $$A$$, there exists $$m \times m$$ unitary matrix $$U$$, $$n \times n$$ unitary matrix $$V$$, and $$m \times n$$ diagonal matrix $$\Sigma$$ where all off-diagonal entries are 0 and the diagonal entries are all non-negative real values such that $$A = U\Sigma V^H$$.

In essence, any linear transformation is a rotation, followed by stretching or shrinking parallel to each axis (with some dimensions added or zeroed out of existence), followed by another rotation.

The following proof will demonstrate that the singular value decomposition always exists. An outline of the proof will be given first:

**Proof outline**

We need to prove that an arbitrary linear transform $$A$$ is a rotation: $$V^H$$, followed by scaling parallel to each axis: $$\Sigma$$, and lastly followed by another rotation: $$U$$, giving $$A = U\Sigma V^H$$.

If the columns of $$A$$ are already mutually orthogonal, then the first rotation is not necessary: $$V = I$$. The entries of $$\Sigma$$ are the lengths of the vectors formed by the columns of $$A$$, and $$U$$ is a rotation that rotates the elementary basis vectors of $$\Complex^m$$ to be parallel with the columns of $$A$$.

In most cases however, the columns of $$A$$ are not mutually orthogonal. In this case, the rotation $$V^H$$ is non-trivial. $$A = (AV)V^H$$, so $$V$$ must be chosen so that the columns of $$AV$$ are mutually orthogonal. Let $$V = \begin{pmatrix} \vec{v}_1 & \vec{v}_2 & \dots & \vec{v}_n \end{pmatrix}$$. We need to choose orthonormal vectors $$\vec{v}_1, \vec{v}_2, \dots, \vec{v}_n$$ so that $$A\vec{v}_1, A\vec{v}_2, \dots, A\vec{v}_n$$ are all mutually orthogonal. This can be done iteratively. Imagine that we have chosen $$\vec{v}_1$$ so that when given any vector $$\vec{v}$$ that is orthogonal to $$\vec{v}_1$$, that $$A\vec{v}_1$$ is orthogonal to $$A\vec{v}$$. The effort now switches to finding an orthonormal set of vectors $$\vec{v}_2, \vec{v}_3, \dots, \vec{v}_n$$ confined to the space of vectors that are perpendicular to $$\vec{v}_1$$ such that $$A\vec{v}_2, A\vec{v}_3, \dots, A\vec{v}_n$$ are mutually orthogonal.

Let $$V_1$$ be a unitary matrix with $$\vec{v}_1$$ as the first column. Factoring $$V_1$$ from the left side of $$V$$ to get $$V = V_1V_\text{new}$$ results in a new set of orthonormal vectors that are the columns of $$V_\text{new}$$. The goal of having the columns of $$AV$$ be mutually orthogonal is converted to having the columns of $$(AV_1)V_\text{new}$$ be mutually orthogonal with $$AV_1$$ effectively replacing $$A$$. $$\vec{v}_1$$ transforms to $$\vec{e}_1$$, and the space of vectors orthogonal to $$\vec{v}_1$$ transforms to the space spanned by the standard basis vectors $$\vec{e}_2, \vec{e}_3, \dots, \vec{e}_n$$. The first column of $$AV_1$$ is $$A\vec{v}_1$$ and so is orthogonal to all other columns.

If $$U_1$$ is a unitary matrix where the first column of $$U_1$$ is $$A\vec{v}_1$$ normalized to unit length, then factoring $$U_1$$ from the left side of $$AV_1$$ to get $$A_1 = U_1^HAV_1$$ results in a matrix in which the first column is parallel to the standard basis vector $$\vec{e}_1$$. The first column of $$AV_1$$ is orthogonal to all other columns, so the first column of $$A_1$$ is orthogonal to all other columns, so hence the first row of $$A_1$$ contains all 0s except for the first column.

$$\vec{v}_2, \vec{v}_3, \dots, \vec{v}_n$$ can now be determined recursively with the dimension reduced to $$n-1$$, and $$A$$ is replaced with $$A_1$$ with the first row and column removed. This forms the inductive component of the coming proof.

Lastly, how do we know that there exists $$\vec{v}_1$$ so that when given any vector $$\vec{v}$$ that is orthogonal to $$\vec{v}_1$$, that $$A\vec{v}_1$$ is orthogonal to $$A\vec{v}$$? The answer will be that the unit length $$\vec{v}$$ that maximizes $$|A\vec{v}|$$ is a valid $$\vec{v}_1$$.

We are now ready to give the proof in full detail:

**Proof of the existence of the singular value decomposition**  —

This proof will proceed using induction on both $$m$$ and $$n$$.

**Base Case $$m = 1$$**  —

$$A$$ has a single row, and therefore has the form $$A = \begin{pmatrix} \sigma_1\vec{v}_1^H \end{pmatrix}$$ where $$\vec{v}_1$$ is an arbitrary unit length vector, and $$\sigma_1$$ is an arbitrary non-negative real number. Note that $$\vec{v}_1$$ and $$\sigma_1$$ exist for any single row matrix $$A$$.

Let $$U = \begin{pmatrix} 1 \end{pmatrix}$$, $$\Sigma = \begin{pmatrix} \sigma_1 & 0 & \dots & 0 \\ \end{pmatrix}$$, and $$V = \begin{pmatrix} \vec{v}_1 & \vec{v}_2 & \dots & \vec{v}_n \end{pmatrix}$$ where $$\vec{v}_1, \vec{v}_2, \dots, \vec{v}_n$$ together form an mutually orthogonal set of unit length vectors. $$\vec{v}_2, \vec{v}_3, \dots, \vec{v}_n$$ can be determined via Gram-Schmidt orthogonalization. It is clear that: $$A = U\Sigma V^H$$.

**Base Case $$n = 1$$**  —

$$A$$ has a single column, and therefore has the form $$A = \begin{pmatrix} \sigma_1\vec{u}_1 \end{pmatrix}$$ where $$\vec{u}_1$$ is an arbitrary unit length vector, and $$\sigma_1$$ is an arbitrary non-negative real number. Note that $$\vec{u}_1$$ and $$\sigma_1$$ exist for any single column matrix $$A$$.

Let $$U = \begin{pmatrix} \vec{u}_1 & \vec{u}_2 & \dots & \vec{u}_m \end{pmatrix}$$, $$\Sigma = \begin{pmatrix} \sigma_1 \\ 0 \\ \vdots \\ 0 \\ \end{pmatrix}$$, and $$V = \begin{pmatrix} 1 \end{pmatrix}$$ where $$\vec{u}_1, \vec{u}_2, \dots, \vec{u}_m$$ together form an mutually orthogonal set of unit length vectors. $$\vec{u}_2, \vec{u}_3, \dots, \vec{u}_m$$ can be determined via Gram-Schmidt orthogonalization. It is clear that: $$A = U\Sigma V^H$$.

**Inductive Case $$m,n \geq 2$$**  —

Let $$\vec{e}_{k,i}$$ denote the $$i^\text{th}$$ standard basis vector of $$\Complex^k$$. Let $$\mathbf{0}_{k \times l}$$ denote a $$k \times l$$ matrix of 0s.

Maximize $$|A\vec{v}|$$ subject to the constraint $$|\vec{v}| = 1$$. Let $$\vec{v}_1$$ be a unit length vector that maximizes $$|A\vec{v}|$$, and let $$\sigma_1 = |A\vec{v}_1|$$. Let $$\vec{u}_1 = \frac{A\vec{v}_1}{\sigma_1}$$ (if $$\sigma_1 = 0$$, then $$\vec{u}_1$$ is an arbitrary unit length vector).

Using Gram-Schmidt orthogonalization, unitary matrices $$U_1$$ and $$V_1$$ can be determined such that the first columns of $$U_1$$ and $$V_1$$ respectively are $$\vec{u}_1$$ and $$\vec{v}_1$$: $$U_1\vec{e}_{m,1} = \vec{u}_1$$ and $$V_1\vec{e}_{n,1} = \vec{v}_1$$. $$A = U_1A_1V_1^H$$ where $$A_1 = U_1^HAV_1$$. It will now be proven that the first column and row of $$A_1$$ contain all 0s except for the (1,1) entry which contains $$\sigma_1$$: $$A_1 = \begin{pmatrix} \sigma_1 & \mathbf{0}_{1 \times (n-1)} \\ \mathbf{0}_{(m-1) \times 1} & A_\text{reduced} \end{pmatrix}$$.

$$A\vec{v}_1 = \sigma_1\vec{u}_1 \implies U_1A_1V_1^H\vec{v}_1 = \sigma_1\vec{u}_1 \implies A_1\vec{e}_{n,1} = \sigma_1\vec{e}_{m,1}$$. This means that the first column of $$A_1$$ is $$\sigma_1\vec{e}_{m,1} = \begin{pmatrix} \sigma_1 \\ \mathbf{0}_{(m-1) \times 1}\end{pmatrix}$$.

To show that the first row of $$A_1$$ is $$\sigma_1\vec{e}_{n,1}^H = \begin{pmatrix} \sigma_1 & \mathbf{0}_{1 \times (n-1)} \end{pmatrix}$$, we will show that the first column of $$A_1$$ is orthogonal to all of the other columns of $$A_1$$. This will require exploiting the fact that $$\vec{v} = \vec{e}_{n,1}$$ maximizes $$|A_1\vec{v}|$$ subject to the constraint $$|\vec{v}| = 1$$.

Let $$v(t)$$ be a parameterized unit length vector. Let $$v(0) = \vec{e}_{n,1}$$.

Taking the derivative of the constraint $$v^Hv = 1$$ gives $$\frac{dv^H}{dt}v + v^H\frac{dv}{dt} = 0$$

$$|A_1\vec{v}|$$ being maximized at $$\vec{e}_{n,1}$$ gives:

$$
\frac{d}{dt}(|A_1\vec{v}|^2)\bigg|_{t=0} = 0 \iff \frac{d}{dt}(\vec{v}^HA_1^HA_1\vec{v})\bigg|_{t=0} = 0 \iff \frac{d\vec{v}^H}{dt}\bigg|_{t=0}A_1^HA_1\vec{e}_{n,1} + \vec{e}_{n,1}^HA_1^HA_1\frac{d\vec{v}}{dt}\bigg|_{t=0} = 0
$$

$$
\iff \Re\left(\vec{e}_{n,1}^HA_1^HA_1\frac{d\vec{v}}{dt}\bigg|_{t=0}\right) = 0
$$

($$\Re$$ and $$\Im$$ denote the real and imaginary components of a complex number respectively.)

Let $$i = 2, 3, \dots, n$$ be arbitrary. Let $$\frac{d\vec{v}}{dt}\bigg|_{t=0} = \vec{e}_{n,i}$$. $$\vec{e}_{n,1}$$ and $$\vec{e}_{n,i}$$ are orthogonal.

This gives: $$\Re(\vec{e}_{n,1}^HA_1^HA_1\vec{e}_{n,i}) = 0$$.

Now let $$\frac{d\vec{v}}{dt}\bigg|_{t=0} = i\vec{e}_{n,i}$$ where the $$i$$ outside of the subscript is the imaginary constant. $$\vec{e}_{n,1}$$ and $$i\vec{e}_{n,i}$$ are orthogonal.

This gives: $$\Re(\vec{e}_{n,1}^HA_1^HA_1(i\vec{e}_{n,i})) = 0 \implies \Im(\vec{e}_{n,1}^HA_1^HA_1\vec{e}_{n,i}) = 0$$.

Hence: $$(A_1\vec{e}_{n,1})^H(A_1\vec{e}_{n,i}) = \vec{e}_{n,1}^HA_1^HA_1\vec{e}_{n,i} = 0$$.

Therefore, the first column of $$A_1$$ is orthogonal to all of the other columns of $$A_1$$, and $$A_1$$ has the form: $$A_1 = \begin{pmatrix} \sigma_1 & \mathbf{0}_{1 \times (n-1)} \\ \mathbf{0}_{(m-1) \times 1} & A_\text{reduced} \end{pmatrix}$$.

$$A_\text{reduced}$$ is an $$(m-1) \times (n-1)$$ matrix, and therefore by an inductive argument, $$A_\text{reduced} = U_r\Sigma_r V_r^H$$. Finally,

$$A = U\Sigma V^H$$ where $$U = U_1\begin{pmatrix} 1 & \mathbf{0}_{1 \times (m-1)} \\ \mathbf{0}_{(m-1) \times 1} & U_r \end{pmatrix}$$, $$\Sigma = \begin{pmatrix} \sigma_1 & \mathbf{0}_{1 \times (n-1)} \\ \mathbf{0}_{(m-1) \times 1} & \Sigma_r \end{pmatrix}$$, and $$V = V_1\begin{pmatrix} 1 & \mathbf{0}_{1 \times (n-1)} \\ \mathbf{0}_{(n-1) \times 1} & V_r \end{pmatrix}$$.

---

*Source: Wikibooks, Linear Algebra/Singular Value Decomposition (https://en.wikibooks.org/wiki/Linear_Algebra/Singular_Value_Decomposition), by Wikibooks contributors, CC BY-SA 4.0.*
