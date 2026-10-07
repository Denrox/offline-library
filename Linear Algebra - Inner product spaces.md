# Inner product spaces

Recall that in your study of vectors, we looked at an operation known as the *dot product*, and that if we have two vectors in $$\mathbb{R}^n$$, we simply multiply the components together and sum them up. With the dot product, it becomes possible to introduce important new ideas like length and angle. The length of a vector $$\mathbf{a}$$, is just $$\|\mathbf{a}\|=\sqrt{\mathbf{a}\cdot\mathbf{a}}$$. The angle between two vectors, $$\mathbf{a}$$ and $$\mathbf{b}$$, is related to the dot product by

$$
\cos{\theta} = \frac{\mathbf{a}\cdot\mathbf{b}} {\|\mathbf{a}\|\cdot\|\mathbf{b}\|}
$$

It turns out that only a few properties of the dot product are necessary to define similar ideas in vector spaces other than $$\mathbb{R}^n$$, such as the spaces of $$m\times n$$ matrices, or polynomials. The more general operation that will take the place of the dot product in these other spaces is called the "inner product".

### The inner product

Say we have two vectors:

$$
\mathbf{a}=\begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix}, \mathbf{b}=\begin{pmatrix} 6 \\ 3 \\ 0 \end{pmatrix}
$$

If we want to take their dot product, we would work as follows

$$
\mathbf{a}\cdot\mathbf{b} = a_1b_1+a_2b_2+a_3b_3 = (2)(6)+(1)(3)+(4)(0) = 15
$$

Because in this case multiplication is commutative, we then have $$\mathbf{a}\cdot\mathbf{b}=\mathbf{b}\cdot\mathbf{a}$$.

But then, we observe

$$
\mathbf{v}\cdot(\alpha\mathbf{a}+\beta\mathbf{b}) = \alpha\mathbf{v}\cdot\mathbf{a} + \beta\mathbf{v}\cdot\mathbf{b}
$$

much like the regular algebraic equality $$v(aA+bB)=avA+bvB$$. For regular dot products this is true since, for $$\mathbb{R}^3$$, for example, one can expand both sides out to obtain

$$
\begin{matrix} (\alpha v_1a_1+\beta v_1b_1)+(\alpha v_2a_2+\beta v_2b_2)+(\alpha v_3a_3+\beta v_3b_3)=\\ (\alpha v_1a_1+\alpha v_2a_2+\alpha v_3a_3)+(\beta v_1b_1+\beta v_2b_2+\beta v_3b_3) \end{matrix}
$$

Finally, we can notice that $$\mathbf{v}\cdot\mathbf{v}$$ is always positive or greater than zero - checking this for $$\mathbb{R}^3$$ gives this as

$$
\mathbf{v}\cdot\mathbf{v}=v_1^2+v_2^2+v_3^2
$$

which can never be less than zero since a real number squared is positive. Note $$\mathbf{v}\cdot\mathbf{v}=0$$ if and only if $$\mathbf{v}=0$$.

In generalizing this sort of behaviour, we want to keep these three behaviours. We can then move on to a definition of a generalization of the dot product, which we call the *inner product*. An inner product of two vectors in some vector space $$V$$, written $$\langle \mathbf{x}, \mathbf{y}\rangle$$ is a function $$V\times V \to \mathbb{R}$$, which obeys the properties

- $$\langle \mathbf{x},\mathbf{y} \rangle = \langle \mathbf{y},\mathbf{x}\rangle$$
- $$\langle \mathbf{v},\alpha\mathbf{a}+\beta\mathbf{b}\rangle = \alpha\langle\mathbf{v},\mathbf{a}\rangle+\beta\langle\mathbf{v},\mathbf{b}\rangle$$
- $$\langle\mathbf{a},\mathbf{a}\rangle\geq0$$ with equality if and only if $$\mathbf{a}=0$$.

The vector space $$V$$ and some inner product together are known as an *inner product space*.  
### The dot product in $$\Complex^n$$

Given two vectors $$\mathbf{a} = a_1\vec{e}_1 + a_2\vec{e}_2 + \dots + a_n\vec{e}_n \in \Complex^n$$ and $$\mathbf{b} = b_1\vec{e}_1 + b_2\vec{e}_2 + \dots + b_n\vec{e}_n \in \Complex^n$$, the dot product generalized to complex numbers is:

$$
\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^n a_i^*b_i = a_1^*b_1 + a_2^*b_2 + \dots + a_n^*b_n
$$

where $$z^*$$ for an arbitrary complex number $$z = c + di$$ is the complex conjugate: $$z^* = c - di$$.

The dot product is "conjugate commutative": $$\mathbf{a} \cdot \mathbf{b} = (\mathbf{b} \cdot \mathbf{a})^*$$. One immediate consequence of the definition of the dot product is that the dot product of a vector with itself is always a non-negative real number: $$\mathbf{a} \cdot \mathbf{a} \geq 0$$.

$$\mathbf{a} \cdot \mathbf{a} = 0$$ if and only if $$\mathbf{a} = \vec{0}$$

#### The Cauchy-Schwarz Inequality for $$\Complex^n$$

**Cauchy-Schwarz Inequality**  —

Given two vectors $$\mathbf{a}, \mathbf{b} \in \Complex^n$$, it is the case that $$|\mathbf{a} \cdot \mathbf{b}| \leq |\mathbf{a}||\mathbf{b}|$$

In $$\R^n$$, the Cauchy-Schwarz inequality can be proven from the triangle inequality. Here, the Cauchy-Schwarz inequality will be proven algebraically.

To make the proof more intuitive, the algebraic proof for $$\mathbf{a}, \mathbf{b} \in \R^n$$ will be given first.

**Proof for $$\mathbf{a}, \mathbf{b} \in \R^n$$**  —

$$|\mathbf{a} \cdot \mathbf{b}| \leq |\mathbf{a}||\mathbf{b}|$$ follows from $$|\mathbf{a} \cdot \mathbf{b}|^2 \leq |\mathbf{a}|^2|\mathbf{b}|^2$$ which is equivalent to

$$
\left(\sum_{i=1}^n a_ib_i\right)^2 \leq \left(\sum_{i=1}^n a_i^2\right)\left(\sum_{j=1}^n b_j^2\right)
$$

expanding both sides gives:

$$
\sum_{i=1}^n \sum_{j=1}^n a_ib_ia_jb_j \leq \sum_{i=1}^n \sum_{j=1}^n a_i^2b_j^2
$$

$$
\iff \sum_{i=1}^n \sum_{j=1}^n (a_ib_j)(a_jb_i) \leq \sum_{i=1}^n \sum_{j=1}^n (a_ib_j)^2
$$

"Folding" the double sums along the diagonal, and cancelling out the diagonal terms which are equivalent on both sides, gives:

$$
\iff \sum_{i=2}^n \sum_{j=1}^{i-1} 2(a_ib_j)(a_jb_i) \leq \sum_{i=2}^n \sum_{j=1}^{i-1} ((a_ib_j)^2 + (a_jb_i)^2)
$$

$$
\iff 0 \leq \sum_{i=2}^n \sum_{j=1}^{i-1} (a_ib_j - a_jb_i)^2
$$

The above inequality is clearly true, therefore the Cauchy-Schwarz inequality holds for $$\mathbf{a}, \mathbf{b} \in \R^n$$.

**Proof for $$\mathbf{a}, \mathbf{b} \in \Complex^n$$**  —

Note that $$|\mathbf{a} \cdot \mathbf{b}| \leq |\mathbf{a}||\mathbf{b}|$$ follows from $$|\mathbf{a} \cdot \mathbf{b}|^2 \leq |\mathbf{a}|^2|\mathbf{b}|^2$$ which is equivalent to $$(\mathbf{a} \cdot \mathbf{b})^*(\mathbf{a} \cdot \mathbf{b}) \leq (\mathbf{a} \cdot \mathbf{a})(\mathbf{b} \cdot \mathbf{b})$$. Expanding both sides yields:

$$
\left(\sum_{i=1}^n a_i^*b_i\right)^*\left(\sum_{i=1}^n a_i^*b_i\right) \leq \left(\sum_{i=1}^n |a_i|^2\right)\left(\sum_{i=1}^n |b_i|^2\right)
$$

$$
\iff \sum_{i=1}^n\sum_{j=1}^n (a_i^*b_i)^*(a_j^*b_j) \leq \sum_{i=1}^n\sum_{j=1}^n |a_i|^2|b_j|^2
$$

$$
\iff \sum_{i=1}^n\sum_{j=1}^n (a_jb_i)^*(a_ib_j) \leq \sum_{i=1}^n\sum_{j=1}^n |a_ib_j|^2
$$

"Folding" the double sums along the diagonal, and cancelling out the diagonal terms which are equivalent on both sides, gives:

$$
\iff \sum_{i=2}^n\sum_{j=1}^{i-1} ((a_jb_i)^*(a_ib_j) + (a_ib_j)^*(a_jb_i)) \leq \sum_{i=2}^n\sum_{j=1}^{i-1} (|a_ib_j|^2 + |a_jb_i|^2)
$$

$$
\iff \sum_{i=2}^n\sum_{j=1}^{i-1} 2\Re((a_ib_j)^*(a_jb_i)) \leq \sum_{i=2}^n\sum_{j=1}^{i-1} (|a_ib_j|^2 + |a_jb_i|^2)
$$

Given complex numbers $$z$$ and $$w$$, it can be proven that $$2\Re(z^*w) \leq |z|^2 + |w|^2$$ (this is similar to $$2xy \leq x^2 + y^2$$ for real numbers). The above inequality holds, and therefore the Cauchy-Schwarz inequality holds for complex numbers.

---

*Source: Wikibooks, Linear Algebra/Inner product spaces (https://en.wikibooks.org/wiki/Linear_Algebra/Inner_product_spaces), by Wikibooks contributors, CC BY-SA 4.0.*
