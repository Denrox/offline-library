# Topic: Geometry of Eigenvalues

--Refer to Topic on Geometry of Linear Transformations---

The characterization of linear transformations in terms of the elementary operations is nice in some ways (for instance, we can easily see that lines are mapped to lines because each of the operations of projection, dilation, reflection, and skew maps lines to lines), but when a map is expressed as a composition of many small operations---no matter how simple---the description is less than ideal. We finish with another way, a somewhat more holistic way, of picturing the geometric effect of transformations of $$\mathbb{R}^2$$.

The pictures in that area give the action of the map on just one or two members of the domain. Although we know that a transformation is described completely by its action on a basis, and so to describe a transformation of $$\mathbb{R}^2$$ therefore, strictly speaking, requires only a description of where it sends the two vectors from any basis, those pictures seem not to convey much geometric intuition. Can we make clear a linear map's geometry by putting in more information, but not so much information that the picture gets confused?

A transformation of $$\mathbb{R}^2$$ sends lines through the origin to lines through the origin. Thus, two points on a line $$y=k_1x$$ will both be sent to the line, say, $$y=k_2x$$. Consider two such points. One is a multiple of the other, so we can write them with the second one as $$r$$ times the first, for some scalar $$r$$.

$$
\begin{pmatrix} x \\ k_1x \end{pmatrix}\quad\text{and}\quad\begin{pmatrix} (rx) \\ k_1(rx) \end{pmatrix}
$$

Compare their images.

$$
\begin{pmatrix} a &c \\ b &d \end{pmatrix} \begin{pmatrix} x \\ k_1x \end{pmatrix} = \begin{pmatrix} ax+ck_1x \\ bx+dk_1x \end{pmatrix} \qquad \begin{pmatrix} a &c \\ b &d \end{pmatrix} \begin{pmatrix} (rx) \\ k_1(rx) \end{pmatrix} = \begin{pmatrix} a(rx)+ck_1(rx) \\ b(rx)+dk_1(rx) \end{pmatrix}
$$

The second vector is $$r$$ times the first, and the image of the second is $$r$$ times the image of the first. Not only does the transformation preserve the fact that the vectors are colinear, it also preserves the relative scale of the vectors. That is, a transformation treats the points on a line through the origin uniformily. To describe the effect of the map on the entire line, we need only describe its effect on a single non-zero point in that line.

Since every point in the space is on some line through the origin, to understand the action of a linear transformation of $$\mathbb{R}^2$$, it is sufficient to pick one point from each line through the origin (say the point that is on the upper half of the unit circle) and show how the map's effect on that set of points.

Here is such a picture for a straightforward dilation.

Below, the same map is shown with the circle and its image superimposed.

Certainly the geometry here is more evident. For example, we can see that some lines through the origin are actually sent to themselves: the $$x$$-axis is sent to the $$x$$-axis, and the $$y$$-axis is sent to the $$y$$-axis.

This is the flip shown earlier, here with the circle and its image superimposed.

And this is the skew shown earlier.

Contrast the picture of this map's effect on the unit square with this one.

Here is a somewhat more complicated map (the second coordinate function is the same as the map in the prior picture, but the first coordinate function is different).

Observe that some vectors are being both dilated and rotated through some angle

$$
\begin{pmatrix} x \\ 2x \end{pmatrix}\mapsto\begin{pmatrix} x \\ k_1x \end{pmatrix}
$$

while others are just being dilated, not rotated at all.

$$
\begin{pmatrix} x \\ 3x \end{pmatrix}\mapsto\begin{pmatrix} x \\ 3x \end{pmatrix}
$$

### Exercises

**Problem 1**  — Show the effect each matrix has on the top half of the unit circle.

1. $$\begin{pmatrix} 1 &1 \\ 2 &2 \end{pmatrix}$$
2. $$\begin{pmatrix} 2 &3 \\ 1 &1 \end{pmatrix}$$
3. $$\begin{pmatrix} 2 &3 \\ 1 &-1 \end{pmatrix}$$

Which vectors stay on the same line through the origin?

Solutions

---

*Source: Wikibooks, Linear Algebra/Topic: Geometry of Eigenvalues (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Geometry_of_Eigenvalues), by Wikibooks contributors, CC BY-SA 4.0.*
