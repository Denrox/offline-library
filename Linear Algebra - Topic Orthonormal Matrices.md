# Topic: Orthonormal Matrices

In *The Elements*, Euclid considers two figures to be the same if they have the same size and shape. That is, the triangles below are not equal because they are not the same set of points. But they are **congruent**— essentially indistinguishable for Euclid's purposes— because we can imagine picking the plane up, sliding it over and rotating it a bit, although not warping or stretching it, and then putting it back down, to superimpose the first figure on the second. (Euclid never explicitly states this principle but he uses it often (Casey 1890).)

In modern terminology, "picking the plane up ..." means considering a map from the plane to itself. Euclid has limited consideration to only certain transformations of the plane, ones that may possibly slide or turn the plane but not bend or stretch it. Accordingly, we define a map $$f:\mathbb{R}^2\to \mathbb{R}^2$$ to be **distance-preserving** or a **rigid motion** or an **isometry**, if for all points $$P_1,P_2\in\mathbb{R}^2$$, the distance from $$f(P_1)$$ to $$f(P_2)$$ equals the distance from $$P_1$$ to $$P_2$$. We also define a plane **figure** to be a set of points in the plane and we say that two figures are **congruent** if there is a distance-preserving map from the plane to itself that carries one figure onto the other.

Many statements from Euclidean geometry follow easily from these definitions. Some are: (i) collinearity is invariant under any distance-preserving map (that is, if $$P_1$$, $$P_2$$, and $$P_3$$ are collinear then so are $$f(P_1)$$, $$f(P_2)$$, and $$f(P_3)$$), (ii) betweeness is invariant under any distance-preserving map (if $$P_2$$ is between $$P_1$$ and $$P_3$$ then so is $$f(P_2)$$ between $$f(P_1)$$ and $$f(P_3)$$), (iii) the property of being a triangle is invariant under any distance-preserving map (if a figure is a triangle then the image of that figure is also a triangle), (iv) and the property of being a circle is invariant under any distance-preserving map. In 1872, F. Klein suggested that Euclidean geometry can be characterized as the study of properties that are invariant under these maps. (This forms part of Klein's Erlanger Program, which proposes the organizing principle that each kind of geometry— Euclidean, projective, etc.— can be described as the study of the properties that are invariant under some group of transformations. The word "group" here means more than just "collection", but that lies outside of our scope.)

We can use linear algebra to characterize the distance-preserving maps of the plane.

First, there are distance-preserving transformations of the plane that are not linear. The obvious example is this *translation*.

$$
\begin{pmatrix} x \\ y \end{pmatrix} \quad\mapsto\quad \begin{pmatrix} x \\ y \end{pmatrix}+\begin{pmatrix} 1 \\ 0 \end{pmatrix}=\begin{pmatrix} x+1 \\ y \end{pmatrix}
$$

However, this example turns out to be the only example, in the sense that if $$f$$ is distance-preserving and sends $$\vec{0}$$ to $$\vec{v}_0$$ then the map $$\vec{v}\mapsto f(\vec{v})-\vec{v}_0$$ is linear. That will follow immediately from this statement: a map $$t$$ that is distance-preserving and sends $$\vec{0}$$ to itself is linear. To prove this equivalent statement, let  

$$
t(\vec{e}_1)=\begin{pmatrix} a \\ b \end{pmatrix} \qquad t(\vec{e}_2)=\begin{pmatrix} c \\ d \end{pmatrix}
$$

for some $$a,b,c,d\in\mathbb{R}$$. Then to show that $$t$$ is linear, we can show that it can be represented by a matrix, that is, that $$t$$ acts in this way for all $$x,y\in\mathbb{R}$$.  

$$
\vec{v}=\begin{pmatrix} x \\ y \end{pmatrix} \stackrel{t}{\longmapsto} \begin{pmatrix} ax+cy \\ bx+dy \end{pmatrix} \qquad\qquad(*)
$$

Recall that if we fix three non-collinear points then any point in the plane can be described by giving its distance from those three. So any point $$\vec{v}$$ in the domain is determined by its distance from the three fixed points $$\vec{0}$$, $$\vec{e}_1$$, and $$\vec{e}_2$$. Similarly, any point $$t(\vec{v})$$ in the codomain is determined by its distance from the three fixed points $$t(\vec{0})$$, $$t(\vec{e}_1)$$, and $$t(\vec{e}_2)$$ (these three are not collinear because, as mentioned above, collinearity is invariant and $$\vec{0}$$, $$\vec{e}_1$$, and $$\vec{e}_2$$ are not collinear). In fact, because $$t$$ is distance-preserving, we can say more: for the point $$\vec{v}$$ in the plane that is determined by being the distance $$d_0$$ from $$\vec{0}$$, the distance $$d_1$$ from $$\vec{e}_1$$, and the distance $$d_2$$ from $$\vec{e}_2$$, its image $$t(\vec{v})$$ must be the unique point in the codomain that is determined by being $$d_0$$ from $$t(\vec{0})$$, $$d_1$$ from $$t(\vec{e}_1)$$, and $$d_2$$ from $$t(\vec{e}_2)$$. Because of the uniqueness, checking that the action in ($$*$$) works in the $$d_0$$, $$d_1$$, and $$d_2$$ cases  

$$
\text{dist}\,(\begin{pmatrix} x \\ y \end{pmatrix},\vec{0}) =\text{dist}\,(t(\begin{pmatrix} x \\ y \end{pmatrix}),t(\vec{0})) =\text{dist}\,(\begin{pmatrix} ax+cy \\ bx+dy \end{pmatrix},\vec{0})
$$

($$t$$ is assumed to send $$\vec{0}$$ to itself)  

$$
\text{dist}\,(\begin{pmatrix} x \\ y \end{pmatrix},\vec{e}_1) =\text{dist}\,(t(\begin{pmatrix} x \\ y \end{pmatrix}),t(\vec{e}_1)) =\text{dist}\,(\begin{pmatrix} ax+cy \\ bx+dy \end{pmatrix},\begin{pmatrix} a \\ b \end{pmatrix})
$$

and  

$$
\text{dist}\,(\begin{pmatrix} x \\ y \end{pmatrix},\vec{e}_2) =\text{dist}\,(t(\begin{pmatrix} x \\ y \end{pmatrix}),t(\vec{e}_2)) =\text{dist}\,(\begin{pmatrix} ax+cy \\ bx+dy \end{pmatrix},\begin{pmatrix} c \\ d \end{pmatrix})
$$

suffices to show that ($$*$$) describes $$t$$. Those checks are routine.

Thus, any distance-preserving $$f:\mathbb{R}^2\to \mathbb{R}^2$$ can be written $$f(\vec{v})=t(\vec{v})+\vec{v}_0$$ for some constant vector $$\vec{v}_0$$ and linear map $$t$$ that is distance-preserving.

Not every linear map is distance-preserving, for example, $$\vec{v}\mapsto 2\vec{v}$$ does not preserve distances. But there is a neat characterization: a linear transformation $$t$$ of the plane is distance-preserving if and only if both $$|t(\vec{e}_1)|=|t(\vec{e}_2)|=1$$ and $$t(\vec{e}_1)$$ is orthogonal to $$t(\vec{e}_2)$$. The "only if" half of that statement is easy— because $$t$$ is distance-preserving it must preserve the lengths of vectors, and because $$t$$ is distance-preserving the Pythagorean theorem shows that it must preserve orthogonality. For the "if" half, it suffices to check that the map preserves lengths of vectors, because then for all $$\vec{p}$$ and $$\vec{q}$$ the distance between the two is preserved $$|t(\vec{p}-\vec{q}\,)|=|t(\vec{p})-t(\vec{q}\,)| =|\vec{p}-\vec{q}\,|$$. For that check, let  

$$
\vec{v}=\begin{pmatrix} x \\ y \end{pmatrix} \quad t(\vec{e}_1)=\begin{pmatrix} a \\ b \end{pmatrix} \quad t(\vec{e}_2)=\begin{pmatrix} c \\ d \end{pmatrix}
$$

and, with the "if" assumptions that $$a^2+b^2=c^2+d^2=1$$ and $$ac+bd=0$$ we have this.  

$$
\begin{array}{rl} |t(\vec{v}\,)|^2 &= (ax+cy)^2+(bx+dy)^2 \\ &= a^2x^2+2acxy+c^2y^2+b^2x^2+2bdxy+d^2y^2 \\ &= x^2(a^2+b^2)+y^2(c^2+d^2)+2xy(ac+bd) \\ &= x^2 + y^2 \\ &= |\vec{v}\,|^2 \end{array}
$$

One thing that is neat about this characterization is that we can easily recognize matrices that represent such a map with respect to the standard bases. Those matrices have that when the columns are written as vectors then they are of length one and are mutually orthogonal. Such a matrix is called an **orthonormal matrix** or **orthogonal matrix** (the first term is commonly used to mean not just that the columns are orthogonal, but also that they have length one).

We can use this insight to delimit the geometric actions possible in distance-preserving maps. Because $$|t(\vec{v}\,)|=|\vec{v}\,|$$, any $$\vec{v}$$ is mapped by $$t$$ to lie somewhere on the circle about the origin that has radius equal to the length of $$\vec{v}$$. In particular, $$\vec{e}_1$$ and $$\vec{e}_2$$ are mapped to the unit circle. What's more, once we fix the unit vector $$\vec{e}_1$$ as mapped to the vector with components $$a$$ and $$b$$ then there are only two places where $$\vec{e}_2$$ can be mapped if that image is to be perpendicular to the first vector: one where $$\vec{e}_2$$ maintains its position a quarter circle clockwise from

$$
\vec{e}_1
$$

$$
{\rm Rep}_{\mathcal{E}_2,\mathcal{E}_2}(t)= \begin{pmatrix} a &-b \\ b &a \end{pmatrix}
$$

and one where is is mapped a quarter circle counterclockwise.

$$
{\rm Rep}_{\mathcal{E}_2,\mathcal{E}_2}(t)= \begin{pmatrix} a &b \\ b &-a \end{pmatrix}
$$

We can geometrically describe these two cases. Let $$\theta$$ be the angle between the $$x$$-axis and the image of $$\vec{e}_1$$, measured counterclockwise. The first matrix above represents, with respect to the standard bases, a **rotation** of the plane by $$\theta$$ radians.

$$
\begin{pmatrix} x \\ y \end{pmatrix} \stackrel{t}{\longmapsto} \begin{pmatrix} x\cos\theta-y\sin\theta \\ x\sin\theta+y\cos\theta \end{pmatrix}
$$

The second matrix above represents a **reflection** of the plane through the line bisecting the angle between $$\vec{e}_1$$ and $$t(\vec{e}_1)$$.

$$
\begin{pmatrix} x \\ y \end{pmatrix}\stackrel{t}{\longmapsto} \begin{pmatrix} x\cos\theta+y\sin\theta \\ x\sin\theta-y\cos\theta \end{pmatrix}
$$

(This picture shows $$\vec{e}_1$$ reflected up into the first quadrant and $$\vec{e}_2$$ reflected down into the fourth quadrant.)

Note again: the angle between $$\vec{e}_1$$ and $$\vec{e}_2$$ runs counterclockwise, and in the first map above the angle from $$t(\vec{e}_1)$$ to $$t(\vec{e}_2)$$ is also counterclockwise, so the orientation of the angle is preserved. But in the second map the orientation is reversed. A distance-preserving map is **direct** if it preserves orientations and **opposite** if it reverses orientation.

So, we have characterized the Euclidean study of congruence: it considers, for plane figures, the properties that are invariant under combinations of (i) a rotation followed by a translation, or (ii) a reflection followed by a translation (a reflection followed by a non-trivial translation is a **glide reflection**).

Another idea, besides congruence of figures, encountered in elementary geometry is that figures are **similar** if they are congruent after a change of scale. These two triangles are similar since the second is the same shape as the first, but $$3/2$$-ths the size.

From the above work, we have that figures are similar if there is an orthonormal matrix $$T$$ such that the points $$\vec{q}$$ on one are derived from the points $$\vec{p}$$ by $$\vec{q}=(kT)\vec{v}+\vec{p}_0$$ for some nonzero real number $$k$$ and constant vector $$\vec{p}_0$$.

Although many of these ideas were first explored by Euclid, mathematics is timeless and they are very much in use today. One application of the maps studied above is in computer graphics. We can, for example, animate this top view of a cube by putting together film frames of it rotating; that's a rigid motion.

- Frame 1   Frame 2   Frame 3

We could also make the cube appear to be moving away from us by producing film frames of it shrinking, which gives us figures that are similar.

- Frame 1:   Frame 2:  Frame 3:

Computer graphics incorporates techniques from linear algebra in many other ways (see Problem 4).

So the analysis above of distance-preserving maps is useful as well as interesting. A beautiful book that explores some of this area is (Weyl 1952). More on groups, of transformations and otherwise, can be found in any book on Modern Algebra, for instance (Birkhoff & MacLane 1965). More on Klein and the Erlanger Program is in (Yaglom 1988).  
### Exercises

**Problem 1**  —

Decide if each of these is an orthonormal matrix.

1. $$\begin{pmatrix} 1/\sqrt{2} &-1/\sqrt{2} \\ -1/\sqrt{2} &-1/\sqrt{2} \end{pmatrix}$$
2. $$\begin{pmatrix} 1/\sqrt{3} &-1/\sqrt{3} \\ -1/\sqrt{3} &-1/\sqrt{3} \end{pmatrix}$$
3. $$\begin{pmatrix} 1/\sqrt{3} &-\sqrt{2}/\sqrt{3} \\ -\sqrt{2}/\sqrt{3} &-1/\sqrt{3} \end{pmatrix}$$

**Problem 2**  —

Write down the formula for each of these distance-preserving maps.

1. the map that rotates $$\pi/6$$ radians, and then translates by $$\vec{e}_2$$
2. the map that reflects about the line $$y=2x$$
3. the map that reflects about $$y=-2x$$ and translates over $$1$$ and up $$1$$

**Problem 3**  —

1. The proof that a map that is distance-preserving and sends the zero vector to itself incidentally shows that such a map is one-to-one and onto (the point in the domain determined by $$d_0$$, $$d_1$$, and $$d_2$$ corresponds to the point in the codomain determined by those three). Therefore any distance-preserving map has an inverse. Show that the inverse is also distance-preserving.
2. Prove that congruence is an equivalence relation between plane figures.

**Problem 4**  —

In practice the matrix for the distance-preserving linear transformation and the translation are often combined into one. Check that these two computations yield the same first two components.  

$$
\begin{pmatrix} a &c \\ b &d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} +\begin{pmatrix} e \\ f \end{pmatrix} \qquad \begin{pmatrix} a &c &e \\ b &d &f \\ 0 &0 &1 \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}
$$

(These are **homogeneous coordinates**; see the Topic on Projective Geometry).

**Problem 5**  —

1. Verify that the properties described in the second paragraph of this Topic as invariant under distance-preserving maps are indeed so.
2. Give two more properties that are of interest in Euclidean geometry from your experience in studying that subject that are also invariant under distance-preserving maps.
3. Give a property that is not of interest in Euclidean geometry and is not invariant under distance-preserving maps.

Solutions

### References

- Birkhoff, Garrett; MacLane, Saunders (1965), *Survey of Modern Algebra*, Macmillan.
- Casey, John (1890), *The Elements of Euclid, Books I to VI and XI* (9th ed.), Hodges, Figgis, and Co..
- Weyl, Hermann (1952), *Symmetry*, Princeton University Press.
- Yaglom, I. M. (1988), *Felix Klein and Sophus Lie: Evolution of the Idea of Symmetry in the Nineteenth Century*, Birkhäuser {{citation}}: Unknown parameter |translater= ignored (help).

---

*Source: Wikibooks, Linear Algebra/Topic: Orthonormal Matrices (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Orthonormal_Matrices), by Wikibooks contributors, CC BY-SA 4.0.*
