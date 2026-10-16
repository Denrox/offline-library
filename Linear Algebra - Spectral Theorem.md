# Spectral Theorem

Given a Hermitian matrix $$A$$, $$A$$ is always diagonalizable. It is also the case that all eigenvalues of $$A$$ are real, and that all eigenvectors are mutually orthogonal. This is given by the "Spectral Theorem":

**The Spectral Theorem**  —

Given any $$n \times n$$ Hermitian matrix $$A$$, there exists an $$n \times n$$ unitary matrix $$U$$, and an $$n \times n$$ diagonal matrix of real values $$\Lambda$$ such that $$A = U\Lambda U^H$$

The columns of $$U = \begin{pmatrix} \vec{u}_1 & \vec{u}_2 & \dots & \vec{u}_n \end{pmatrix}$$ are the eigenvectors of $$U$$, and the diagonal entries of $$\Lambda = \begin{pmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n \end{pmatrix}$$ are the corresponding eigenvalues.

In essence $$A$$ can be decomposed into a "spectrum" of rank 1 projections: $$A = \sum_{i=1}^n \lambda_i(\vec{u}_i\vec{u}_i^H)$$

The spectral theorem can in fact be proven without the need for the characteristic polynomial of $$A$$, or any of the derivative theorems.

**Proof of the Spectral Theorem**  —

The proof will proceed by using induction on $$n$$.

**Base Case $$n = 1$$**  —

When $$A = \begin{pmatrix} a_{1,1} \end{pmatrix}$$, it must be the case that $$a_{1,1}$$ is real, or else $$A$$ is not Hermitian. The spectral decomposition is then simply $$A = \begin{pmatrix} 1 \end{pmatrix}\begin{pmatrix} a_{1,1} \end{pmatrix}\begin{pmatrix} 1 \end{pmatrix}^H$$

**Inductive Case $$n \geq 2$$**  —

Let $$\vec{e}_i$$ denote the $$i^\text{th}$$ standard basis vector of $$\Complex^n$$. Let $$\mathbf{0}_{k \times m}$$ denote a $$k \times m$$ matrix of 0s.

Let $$\vec{u}_1$$ be a unit length vector that maximizes $$\vec{u}_1^HA\vec{u}_1$$ (recall that $$\vec{u}_1^HA\vec{u}_1$$ is always real), and let $$\lambda_1 = \vec{u}_1^HA\vec{u}_1$$. Let $$U_1$$ be a unitary matrix where the first column is $$\vec{u}_1$$: $$U_1\vec{e}_1 = \vec{u}_1$$.

$$A = U_1A_1U_1^H$$ where $$A_1 = U_1^HAU_1$$. It will now be shown that $$A_1$$ has the form $$A_1 = \begin{pmatrix} \lambda_1 & \mathbf{0}_{1 \times (n-1)} \\ \mathbf{0}_{(n-1) \times 1} & A_\text{reduced} \end{pmatrix}$$

$$\vec{e}_1^HA_1\vec{e}_1 = \vec{u}_1^HA\vec{u}_1 = \lambda_1$$ so that the (1,1) entry of $$A_1$$ is $$\lambda_1$$. It will now be shown that the first row and column of $$A_1$$ is filled with 0s except for the first entry. For an arbitary $$i = 2, 3, \dots, n$$, consider the parameterized unit vector $$\vec{u}_t(t) = (\cos t) \vec{e}_1 + (\sin t) \vec{e}_i$$.

$$\vec{u}_t(t)^HA_1\vec{u}_t(t) = ((\cos t) \vec{e}_1 + (\sin t)\vec{e}_i)^HA_1((\cos t) \vec{e}_1 + (\sin t) \vec{e}_i)$$ $$= \lambda_1\cos^2 t + (a_{(i,1)} + a_{(1,i)})\cos t \sin t + a_{(i,i)}\sin^2 t$$ $$= \lambda_1\cos^2 t + 2\Re(a_{(i,1)})\cos t \sin t + a_{(i,i)}\sin^2 t$$ where $$a_{(i,j)}$$ denotes the $$(i,j)$$ entry of $$A_1$$ ($$\Re$$ and $$\Im$$ denote the real and imaginary components respectively).

$$\frac{d}{dt}(\vec{u}_t(t)^HA_1\vec{u}_t(t))\bigg|_{t=0} = 2\Re(a_{(i,1)})$$. Unit vector $$\vec{u} = \vec{u}_1$$ maximizes $$\vec{u}^HA\vec{u}$$ which implies that $$\vec{u} = \vec{u}_t(0) = \vec{e}_1$$ is the unit vector that maximizes $$\vec{u}^HA_1\vec{u}$$. Therefore $$\frac{d}{dt}(\vec{u}_t(t)^HA_1\vec{u}_t(t))\bigg|_{t=0} = 0$$ which gives $$\Re(a_{(i,1)}) = 0$$.

Now consider the parameterized unit vector $$\vec{u}_t(t) = (\cos t) \vec{e}_1 + i(\sin t) \vec{e}_i$$.

$$\vec{u}_t(t)^HA_1\vec{u}_t(t) = ((\cos t) \vec{e}_1 + i(\sin t)\vec{e}_i)^HA_1((\cos t) \vec{e}_1 + i(\sin t) \vec{e}_i)$$ $$= \lambda_1\cos^2 t + (-ia_{(i,1)} + ia_{(1,i)})\cos t \sin t + a_{(i,i)}\sin^2 t$$ $$= \lambda_1\cos^2 t + 2\Im(a_{(i,1)})\cos t \sin t + a_{(i,i)}\sin^2 t$$

$$\frac{d}{dt}(\vec{u}_t(t)^HA_1\vec{u}_t(t))\bigg|_{t=0} = 2\Im(a_{(i,1)})$$ so $$\frac{d}{dt}(\vec{u}_t(t)^HA_1\vec{u}_t(t))\bigg|_{t=0} = 0 \implies \Im(a_{(i,1)}) = 0$$. Therefore $$a_{(i,1)} = a_{(1,i)} = 0$$. It has been proven that the first row and column of $$A_1$$ is filled with 0s except for the first entry.

$$A_1$$ has the form $$A_1 = \begin{pmatrix} \lambda_1 & \mathbf{0}_{1 \times (n-1)} \\ \mathbf{0}_{(n-1) \times 1} & A_\text{reduced} \end{pmatrix}$$, and by an inductive argument, $$A_\text{reduced}$$ has the spectral decomposition $$U_r \Lambda_r U_r^H$$.

Therefore $$A = U\Lambda U^H$$ where $$U = U_1\begin{pmatrix} 1 & \mathbf{0}_{1 \times (n-1)} \\ \mathbf{0}_{(n-1) \times 1} & U_r\end{pmatrix}$$ and $$\Lambda = \begin{pmatrix} \lambda_1 & \mathbf{0}_{1 \times (n-1)} \\ \mathbf{0}_{(n-1) \times 1} & \Lambda_r\end{pmatrix}$$

---

*Source: Wikibooks, Linear Algebra/Spectral Theorem (https://en.wikibooks.org/wiki/Linear_Algebra/Spectral_Theorem), by Wikibooks contributors, CC BY-SA 4.0.*
