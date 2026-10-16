# Orthogonal Projection Onto a Line

We first consider orthogonal projection onto a line. To orthogonally project a vector $$\vec{v}$$ onto a line $$\ell$$, mark the point on the line at which someone standing on that point could see $$\vec{v}$$ by looking straight up or down (from that person's point of view).

The picture shows someone who has walked out on the line until the tip of $$\vec{v}$$ is straight overhead. That is, where the line is described as the span of some nonzero vector $$\ell=\{c\cdot\vec{s}\,\big|\, c\in\mathbb{R}\}$$, the person has walked out to find the coefficient $$c_{\vec{p}}\,$$ with the property that $$\vec{v}-c_{\vec{p}}\cdot\vec{s}\,$$ is orthogonal to $$c_{\vec{p}}\cdot\vec{s}$$.

We can solve for this coefficient by noting that because $$\vec{v}-c_{\vec{p}}\vec{s}\,$$ is orthogonal to a scalar multiple of $$\vec{s}\,$$ it must be orthogonal to $$\vec{s}\,$$ itself, and then the consequent fact that the dot product $$(\vec{v}-c_{\vec{p}}\vec{s})\cdot \vec{s}\,$$ is zero gives that $$c_{\vec{p}}=\vec{v}\cdot \vec{s}/\vec{s}\cdot \vec{s}$$.

**Definition 1.1**  —

The **orthogonal projection of $$\vec{v}$$ onto the line spanned by a nonzero $$\vec{s}\,$$** is this vector.

$$
\text{proj}_{[\vec{s}\,]}({\vec{v}})= \frac{ \vec{v}\cdot\vec{s} }{ \vec{s}\cdot\vec{s} }\vec{s}
$$

Problem 13 checks that the outcome of the calculation depends only on the line and not on which vector $$\vec{s}\,$$ happens to be used to describe that line.

**Remark 1.2**  —

The wording of that definition says "spanned by $$\vec{s}\,$$" instead the more formal "the span of the set $$\{\vec{s}\,\}$$". This casual first phrase is common.

**Example 1.3**  —

To orthogonally project the vector $$\binom{2}{3}$$ onto the line $$y=2x$$, we first pick a direction vector for the line. For instance,

$$
\vec{s}=\begin{pmatrix} 1 \\ 2 \end{pmatrix}
$$

will do. Then the calculation is routine.

- $$\frac{ \begin{pmatrix} 2 \\ 3 \end{pmatrix}\cdot\begin{pmatrix} 1 \\ 2 \end{pmatrix} }{ \begin{pmatrix} 1 \\ 2 \end{pmatrix}\cdot\begin{pmatrix} 1 \\ 2 \end{pmatrix} } \cdot\begin{pmatrix} 1 \\ 2 \end{pmatrix} ={\displaystyle \frac{8}{5}}\cdot\begin{pmatrix} 1 \\ 2 \end{pmatrix}=\begin{pmatrix} 8/5 \\ 16/5 \end{pmatrix}$$

**Example 1.4**  —

In $$\mathbb{R}^3$$, the orthogonal projection of a general vector

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix}
$$

onto the $$y$$-axis is

$$
\frac{ \begin{pmatrix} x \\ y \\ z \end{pmatrix}\cdot\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} }{ \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}\cdot\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} } \cdot\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}=\begin{pmatrix} 0 \\ y \\ 0 \end{pmatrix}
$$

which matches our intuitive expectation.

The picture above with the stick figure walking out on the line until $$\vec{v}$$'s tip is overhead is one way to think of the orthogonal projection of a vector onto a line. We finish this subsection with two other ways.

**Example 1.5**  —

A railroad car left on an east-west track without its brake is pushed by a wind blowing toward the northeast at fifteen miles per hour; what speed will the car reach?

For the wind we use a vector of length $$15$$ that points toward the northeast.

$$
\vec{v}=\begin{pmatrix} 15\sqrt{1/2} \\ 15\sqrt{1/2} \end{pmatrix}
$$

The car can only be affected by the part of the wind blowing in the east-west direction— the part of $$\vec{v}$$ in the direction of the $$x$$-axis is this (the picture has the same perspective as the railroad car picture above).

- $$\displaystyle \vec{p}=\begin{pmatrix} 15\sqrt{1/2} \\ 0 \end{pmatrix}$$

So the car will reach a velocity of $$15\sqrt{1/2}$$ miles per hour toward the east.

Thus, another way to think of the picture that precedes the definition is that it shows $$\vec{v}$$ as decomposed into two parts, the part with the line (here, the part with the tracks, $$\vec{p}$$), and the part that is orthogonal to the line (shown here lying on the north-south axis). These two are "not interacting" or "independent", in the sense that the east-west car is not at all affected by the north-south part of the wind (see Problem 5). So the orthogonal projection of $$\vec{v}$$ onto the line spanned by $$\vec{s}\,$$ can be thought of as the part of $$\vec{v}\,$$ that lies in the direction of $$\vec{s}$$.

Finally, another useful way to think of the orthogonal projection is to have the person stand not on the line, but on the vector that is to be projected to the line. This person has a rope over the line and pulls it tight, naturally making the rope orthogonal to the line.

That is, we can think of the projection $$\vec{p}\,$$ as being the vector in the line that is closest to $$\vec{v}$$ (see Problem 11).

**Example 1.6**  —

A submarine is tracking a ship moving along the line $$y=3x+2$$. Torpedo range is one-half mile. Can the sub stay where it is, at the origin on the chart below, or must it move to reach a place where the ship will pass within range?

The formula for projection onto a line does not immediately apply because the line doesn't pass through the origin, and so isn't the span of any $$\vec{s}$$. To adjust for this, we start by shifting the entire map down two units. Now the line is $$y=3x$$, which is a subspace, and we can project to get the point $$\vec{p}$$ of closest approach, the point on the line through the origin closest to

$$
\vec{v}=\begin{pmatrix} 0 \\ -2 \end{pmatrix}
$$

the sub's shifted position.

$$
\vec{p}=\frac{\begin{pmatrix} 0 \\ -2 \end{pmatrix}\cdot\begin{pmatrix} 1 \\ 3 \end{pmatrix}}{ \begin{pmatrix} 1 \\ 3 \end{pmatrix}\cdot\begin{pmatrix} 1 \\ 3 \end{pmatrix}} \cdot \begin{pmatrix} 1 \\ 3 \end{pmatrix}=\begin{pmatrix} -3/5 \\ -9/5 \end{pmatrix}
$$

The distance between $$\vec{v}$$ and $$\vec{p}$$ is approximately $$0.63$$ miles and so the sub must move to get in range.

This subsection has developed a natural projection map: orthogonal projection onto a line. As suggested by the examples, it is often called for in applications. The next subsection shows how the definition of orthogonal projection onto a line gives us a way to calculate especially convienent bases for vector spaces, again something that is common in applications. The final subsection completely generalizes projection, orthogonal or not, onto any subspace at all.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Project the first vector orthogonally onto the line spanned by the second vector.

1. $$\begin{pmatrix} 2 \\ 1 \end{pmatrix}$$, $$\begin{pmatrix} 3 \\ -2 \end{pmatrix}$$
2. $$\begin{pmatrix} 2 \\ 1 \end{pmatrix}$$, $$\begin{pmatrix} 3 \\ 0 \end{pmatrix}$$
3. $$\begin{pmatrix} 1 \\ 1 \\ 4 \end{pmatrix}$$, $$\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}$$
4. $$\begin{pmatrix} 1 \\ 1 \\ 4 \end{pmatrix}$$, $$\begin{pmatrix} 3 \\ 3 \\ 12 \end{pmatrix}$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Project the vector orthogonally onto the line.

1. $$\begin{pmatrix} 2 \\ -1 \\ 4 \end{pmatrix}, \{c\begin{pmatrix} -3 \\ 1 \\ -3 \end{pmatrix}\,\big|\, c\in\mathbb{R}\}$$
2. $$\begin{pmatrix} -1 \\ -1 \end{pmatrix}$$, the line $$y=3x$$

**Problem 3**  —

Although the development of Definition 1.1 is guided by the pictures, we are not restricted to spaces that we can draw. In $$\mathbb{R}^4$$ project this vector onto this line.

$$
\vec{v}=\begin{pmatrix} 1 \\ 2 \\ 1 \\ 3 \end{pmatrix} \qquad \ell=\{c\cdot\begin{pmatrix} -1 \\ 1 \\ -1 \\ 1 \end{pmatrix}\,\big|\, c\in\mathbb{R}\}
$$

*This exercise is recommended for all readers.*

**Problem 4**  —

Definition 1.1 uses two vectors $$\vec{s}$$ and $$\vec{v}$$. Consider the transformation of $$\mathbb{R}^2$$ resulting from fixing

$$
\vec{s}=\begin{pmatrix} 3 \\ 1 \end{pmatrix}
$$

and projecting $$\vec{v}$$ onto the line that is the span of $$\vec{s}$$. Apply it to these vectors.

1. $$\begin{pmatrix} 1 \\ 2 \end{pmatrix}$$
2. $$\begin{pmatrix} 0 \\ 4 \end{pmatrix}$$

Show that in general the projection tranformation is this.

$$
\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \mapsto \begin{pmatrix} (9 x_1+3 x_2)/10 \\ (3 x_1 + x_2)/10 \end{pmatrix}
$$

Express the action of this transformation with a matrix.

**Problem 5**  —

Example 1.5 suggests that projection breaks $$\vec{v}$$ into two parts, $$\text{proj}_{[\vec{s}\,]}({\vec{v}\,})$$ and $$\vec{v}-\text{proj}_{[\vec{s}\,]}({\vec{v}\,})$$, that are "not interacting". Recall that the two are orthogonal. Show that any two nonzero orthogonal vectors make up a linearly independent set.

**Problem 6**  —

1. What is the orthogonal projection of $$\vec{v}$$ onto a line if $$\vec{v}$$ is a member of that line?
2. Show that if $$\vec{v}$$ is not a member of the line then the set $$\{\vec{v},\vec{v}-\text{proj}_{[\vec{s}\,]}({\vec{v}\,})\}$$ is linearly independent.

**Problem 7**  —

Definition 1.1 requires that $$\vec{s}\,$$ be nonzero. Why? What is the right definition of the orthogonal projection of a vector onto the (degenerate) line spanned by the zero vector?

**Problem 8**  —

Are all vectors the projection of some other vector onto some line?  
*This exercise is recommended for all readers.*

**Problem 9**  —

Show that the projection of $$\vec{v}$$ onto the line spanned by $$\vec{s}$$ has length equal to the absolute value of the number $$\vec{v}\cdot\vec{s}$$ divided by the length of the vector $$\vec{s}$$.

**Problem 10**  —

Find the formula for the distance from a point to a line.

**Problem 11**  —

Find the scalar $$c$$ such that $$(cs_1,cs_2)$$ is a minimum distance from the point $$(v_1,v_2)$$ by using calculus (i.e., consider the distance function, set the first derivative equal to zero, and solve). Generalize to $$\mathbb{R}^n$$.  
*This exercise is recommended for all readers.*

**Problem 12**  —

Prove that the orthogonal projection of a vector onto a line is shorter than the vector.  
*This exercise is recommended for all readers.*

**Problem 13**  —

Show that the definition of orthogonal projection onto a line does not depend on the spanning vector: if $$\vec{s}$$ is a nonzero multiple of $$\vec{q}$$ then $$(\vec{v}\cdot\vec{s}/\vec{s}\cdot\vec{s}\,)\cdot\vec{s}$$ equals $$(\vec{v}\cdot\vec{q}/\vec{q}\cdot\vec{q}\,)\cdot\vec{q}$$.  
*This exercise is recommended for all readers.*

**Problem 14**  —

Consider the function mapping to plane to itself that takes a vector to its projection onto the line $$y=x$$. These two each show that the map is linear, the first one in a way that is bound to the coordinates (that is, it fixes a basis and then computes) and the second in a way that is more conceptual.

1. Produce a matrix that describes the function's action.
2. Show also that this map can be obtained by first rotating everything in the plane $$\pi/4$$ radians clockwise, then projecting onto the $$x$$-axis, and then rotating $$\pi/4$$ radians counterclockwise.

**Problem 15**  —

For $$\vec{a},\vec{b}\in\mathbb{R}^n$$ let $$\vec{v}_1$$ be the projection of $$\vec{a}$$ onto the line spanned by $$\vec{b}$$, let $$\vec{v}_2$$ be the projection of $$\vec{v}_1$$ onto the line spanned by $$\vec{a}$$, let $$\vec{v}_3$$ be the projection of $$\vec{v}_2$$ onto the line spanned by $$\vec{b}$$, etc., back and forth between the spans of $$\vec{a}$$ and $$\vec{b}$$. That is, $$\vec{v}_{i+1}$$ is the projection of $$\vec{v}_i$$ onto the span of $$\vec{a}$$ if $$i+1$$ is even, and onto the span of $$\vec{b}$$ if $$i+1$$ is odd. Must that sequence of vectors eventually settle down— must there be a sufficiently large $$i$$ such that $$\vec{v}_{i+2}$$ equals $$\vec{v}_{i}$$ and $$\vec{v}_{i+3}$$ equals $$\vec{v}_{i+1}$$? If so, what is the earliest such $$i$$?

Solutions

---

*Source: Wikibooks, Linear Algebra/Orthogonal Projection Onto a Line (https://en.wikibooks.org/wiki/Linear_Algebra/Orthogonal_Projection_Onto_a_Line), by Wikibooks contributors, CC BY-SA 4.0.*
