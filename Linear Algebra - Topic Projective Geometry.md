# Topic: Projective Geometry

There are geometries other than the familiar Euclidean one. One such geometry arose in art, where it was observed that what a viewer sees is not necessarily what is there. This is Leonardo da Vinci's *The Last Supper*.

What is there in the room, for instance where the ceiling meets the left and right walls, are lines that are parallel. However, what a viewer sees is lines that, if extended, would intersect. The intersection point is called the *vanishing point*. This aspect of perspective is also familiar as the image of a long stretch of railroad tracks that appear to converge at the horizon.

To depict the room, da Vinci has adopted a model of how we see, of how we project the three dimensional scene to a two dimensional image. This model is only a first approximation — it does not take into account that our retina is curved and our lens bends the light, that we have binocular vision, or that our brain's processing greatly affects what we see — but nonetheless it is interesting, both artistically and mathematically.

The projection is not orthogonal, it is a *central projection* from a single point, to the plane of the canvas.

(It is not an orthogonal projection since the line from the viewer to $$C$$ is not orthogonal to the image plane.) As the picture suggests, the operation of central projection preserves some geometric properties — lines project to lines. However, it fails to preserve some others — equal length segments can project to segments of unequal length; the length of $$AB$$ is greater than the length of $$BC$$ because the segment projected to $$AB$$ is closer to the viewer and closer things look bigger. The study of the effects of central projections is projective geometry. We will see how linear algebra can be used in this study.

There are three cases of central projection. The first is the projection done by a movie projector.

We can think that each source point is "pushed" from the domain plane outward to the image point in the codomain plane. This case of projection has a somewhat different character than the second case, that of the artist "pulling" the source back to the canvas.

In the first case $$S$$ is in the middle while in the second case $$I$$ is in the middle. One more configuration is possible, with $$P$$ in the middle. An example of this is when we use a pinhole to shine the image of a solar eclipse onto a piece of paper.

We shall take each of the three to be a central projection by $$P$$ of $$S$$ to $$I$$.

Consider again the effect of railroad tracks that appear to converge to a point. We model this with parallel lines in a domain plane $$S$$ and a projection via a $$P$$ to a codomain plane $$I$$ (The gray lines are parallel to $$S,I$$) .

All three projection cases appear here. The first picture below shows $$P$$ acting like a movie projector by pushing points from part of $$S$$ out to image points on the lower half of $$I$$ . The middle picture shows $$P$$ acting like the artist by pulling points from another part of $$S$$ back to image points in the middle of $$I$$ . In the third picture, $$P$$ acts like the pinhole, projecting points from $$S$$ to the upper part of $$I$$ . This picture is the trickiest — the points that are projected near to the vanishing point are the ones that are far out on the bottom left of $$S$$ . Points in $$S$$ that are near to the vertical gray line are sent high up on $$I$$ .

There are two awkward things about this situation. The first is that neither of the two points in the domain nearest to the vertical gray line (see below) has an image because a projection from those two is along the gray line that is parallel to the codomain plane (we sometimes say that these two are projected "to infinity"). The second awkward thing is that the vanishing point in $$I$$ isn't the image of any point from $$S$$ because a projection to this point would be along the gray line that is parallel to the domain plane (we sometimes say that the vanishing point is the image of a projection "from infinity").

For a better model, put the projector $$P$$ at the origin. Imagine that $$P$$ is covered by a glass hemispheric dome. As $$P$$ looks outward, anything in the line of vision is projected to the same spot on the dome. This includes things on the line between $$P$$ and the dome, as in the case of projection by the movie projector. It includes things on the line further from $$P$$ than the dome, as in the case of projection by the painter. It also includes things on the line that lie behind $$P$$ , as in the case of projection by a pinhole.

From this perspective $$P$$ , all of the spots on the line are seen as the same point. Accordingly, for any nonzero vector $$\vec v\in\R^3$$ , we define the associated **point $$v$$ in the projective plane** to be the set $$\bigl\{k\vec v:k\in\R,k\ne0\bigr\}$$ of nonzero vectors lying on the same line through the origin as $$\vec v$$ . To describe a projective point we can give any representative member of the line, so that the projective point shown above can be represented in any of these three ways.

$$
\begin{pmatrix}1\\2\\3\end{pmatrix}\qquad\begin{pmatrix}\frac13\\\frac23\\1\end{pmatrix}\qquad\begin{pmatrix}-2\\-4\\-6\end{pmatrix}
$$

Each of these is a **homogeneous coordinate vector** for $$v$$ .

This picture, and the above definition that arises from it, clarifies the description of central projection but there is something awkward about the dome model: what if the viewer looks down? If we draw $$P$$'s line of sight so that the part coming toward us, out of the page, goes down below the dome then we can trace the line of sight backward, up past $$P$$ and toward the part of the hemisphere that is behind the page. So in the dome model, looking down gives a projective point that is behind the viewer. Therefore, if the viewer in the picture above drops the line of sight toward the bottom of the dome then the projective point drops also and as the line of sight continues down past the equator, the projective point suddenly shifts from the front of the dome to the back of the dome. This discontinuity in the drawing means that we often have to treat equatorial points as a separate case. That is, while the railroad track discussion of central projection has three cases, the dome model has two.

We can do better than this. Consider a sphere centered at the origin. Any line through the origin intersects the sphere in two spots, which are said to be *antipodal*. Because we associate each line through the origin with a point in the projective plane, we can draw such a point as a pair of antipodal spots on the sphere. Below, the two antipodal spots are shown connected by a dashed line to emphasize that they are not two different points, the pair of spots together make one projective point.

While drawing a point as a pair of antipodal spots is not as natural as the one-spot-per-point dome mode, on the other hand the awkwardness of the dome model is gone, in that if as a line of view slides from north to south, no sudden changes happen on the picture. This model of central projection is uniform — the three cases are reduced to one.

So far we have described points in projective geometry. What about lines? What a viewer at the origin sees as a line is shown below as a great circle, the intersection of the model sphere with a plane through the origin.

(One of the projective points on this line is shown to bring out a subtlety. Because two antipodal spots together make up a single projective point, the great circle's behind-the-paper part is the same set of projective points as its in-front-of-the-paper part.) Just as we did with each projective point, we will also describe a projective line with a triple of reals. For instance, the members of this plane through the origin in $$\R^3$$

$$
\left\{\begin{pmatrix}x\\y\\z\end{pmatrix}:x+y-z=0\right\}
$$

project to a line that we can described with the triple $$(1\ 1\ -1)$$ (we use row vectors to typographically distinguish linesfrom points). In general, for any nonzero three-wide row vector $$\vec L$$ we define the associated **line in the projective plane**, to be the set $$L=\bigl\{k\vec L:k\in\R,k\ne0\bigr\}$$ of nonzero multiples of $$\vec L$$ .

The reason that this description of a line as a triple is convienent is that in the projective plane, a point $$v$$ and a line $$L$$ are **incident** — the point lies on the line, the line passes throught the point — if and only if a dot product of their representatives $$v_1L_1+v_2L_2+v_3L_3$$ is zero (Problem 4 shows that this is independent of the choice of representatives $$\vec v$$ and $$\vec L$$). For instance, the projective point described above by the column vector with components $$1,2,3$$ lies in the projective line described by $$(1\ 1\ -1)$$ , simply because any vector in $$\R^3$$ whose components are in ratio $$1:2:3$$ lies in the plane through the origin whose equation is of the form $$1k\cdot x+1k\cdot y-1k\cdot z=0$$ for any nonzero $$k$$ . That is, the incidence formula is inherited from the three-space lines and planes of which $$v$$ and $$L$$ are projections.

Thus, we can do analytic projective geometry. For instance, the projective line $$L=(1\ 1\ -1)$$ has the equation $$1v_1+1v_2-1v_3=0$$ , because points incident on the line are characterized by having the property that their representatives satisfy this equation. One difference from familiar Euclidean analytic geometry is that in projective geometry we talk about the equation of a point. For a fixed point like

$$
v=\begin{pmatrix}1\\2\\3\end{pmatrix}
$$

the property that characterizes lines through this point (that is, lines incident on this point) is that the components of any representatives satisfy $$1L_1+2L_2+3L_3=0$$ and so this is the equation of $$v$$ .

This symmetry of the statements about lines and points brings up the **Duality Principle** of projective geometry: in any true statement, interchanging "point" with "line" results in another true statement. For example, just as two distinct points determine one and only one line, in the projective plane, two distinct lines determine one and only one point. Here is a picture showing two lines that cross in antipodal spots and thus cross at one projective point.

$$
(*)
$$

Contrast this with Euclidean geometry, where two distinct lines may have a unique intersection or may be parallel. In this way, projective geometry is simpler, more uniform, than Euclidean geometry.

That simplicity is relevant because there is a relationship between the two spaces: the projective plane can be viewed as an extension of the Euclidean plane. Take the sphere model of the projective plane to be the unit sphere in $$\R^3$$ and take Euclidean space to be the plane $$z=1$$ . This gives us a way of viewing some points in projective space as corresponding to points in Euclidean space, because all of the points on the plane are projections of antipodal spots from the sphere.

$$
(**)
$$

Note though that projective points on the equator don't project up to the plane. Instead, these project "out to infinity". We can thus think of projective space as consisting of the Euclidean plane with some extra points adjoined — the Euclidean plane is embedded in the projective plane. These extra points, the equatorial points, are the **ideal points** or **points at infinity** and the equator is the **ideal line** or **line at infinity** (note that it is not a Euclidean line, it is a projective line).

The advantage of the extension to the projective plane is that some of the awkwardness of Euclidean geometry disappears. For instance, the projective lines shown above in $$(*)$$ cross at antipodal spots, a single projective point, on the sphere's equator. If we put those lines into $$(**)$$ then they correspond to Euclidean lines that are parallel. That is, in moving from the Euclidean plane to the projective plane, we move from having two cases, that lines either intersect or are parallel, to having only one case, that lines intersect (possibly at a point at infinity).

The projective case is nicer in many ways than the Euclidean case but has the problem that we don't have the same experience or intuitions with it. That's one advantage of doing analytic geometry, where the equations can lead us to the right conclusions. Analytic projective geometry uses linear algebra. For instance, for three points of the projective plane $$t,u,v$$ , setting up the equations for those points by fixing vectors representing each, shows that the three are collinear — incident in a single line — if and only if the resulting three-equation system has infinitely many row vector solutions representing that line. That, in turn, holds if and only if this determinant is zero.

$$
\begin{vmatrix}t_1&u_1&v_1\\t_2&u_2&v_2\\t_3&u_3&v_3\end{vmatrix}
$$

Thus, three points in the projective plane are collinear if and only if any three representative column vectors are linearly dependent. Similarly (and illustrating the Duality Principle), three lines in the projective plane are incident on a single point if and only if any three row vectors representing them are linearly dependent.

The following result is more evidence of the "niceness" of the geometry of the projective plane, compared to the Euclidean case. These two triangles are said to be **in perspective** from $$P$$ because their corresponding vertices are collinear.

Consider the pairs of corresponding sides: the sides $$T_1U_1,T_2U_2$$ , the sides $$T_1V_1,T_2V_2$$ , and the sides $$U_1V_1,U_2V_2$$ . Desargue's Theorem is that when the three pairs of corresponding sides are extended to lines, they intersect (shown here as the point $$TU$$ , the point $$TV$$ , and the point $$UV$$), and further, those three intersection points are collinear.

We will prove this theorem, using projective geometry. (These are drawn as Euclidean figures because it is the more familiar image. To consider them as projective figures, we can imagine that, although the line segments shown are parts of great circles and so are curved, the model has such a large radius compared to the size of the figures that the sides appear in this sketch to be straight.)

For this proof, we need a preliminary lemma (Coxeter 1974): if $$W,X,Y,Z$$ are four points in the projective plane (no three of which are collinear) then there are homogeneous coordinate vectors $$\vec w,\vec x,\vec y,\vec z$$ for the projective points, and a basis $$B$$ for $$\R^3$$ , satisfying this.

$$
\text{Rep}_B(\vec w)=\begin{pmatrix}1\\0\\0\end{pmatrix}\quad \text{Rep}_B(\vec x)=\begin{pmatrix}0\\1\\0\end{pmatrix}\quad \text{Rep}_B(\vec y)=\begin{pmatrix}0\\0\\1\end{pmatrix}\quad \text{Rep}_B(\vec z)=\begin{pmatrix}1\\1\\1\end{pmatrix}
$$

The proof is straightforward. Because $$W,X,Y$$ are not on the same projective line, any homogeneous coordinate vectors $$\vec{w}_0,\vec{x}_0,\vec{y}_0$$ do not line on the same plane through the origin in $$\R^3$$ and so form a spanning set for $$\R^3$$ . Thus any homogeneous coordinate vector for $$Z$$ can be written as a combination $$\vec{z}_0=a\vec{w}_0+b\vec{x}_0+c\vec{y}_0$$ . Then, we can take

$$
\begin{align}\vec w&=a\vec{w}_0\\\vec x&=b\vec{x}_0\\\vec y&=c\vec{y}_0\\\vec z&=\vec{z}_0\end{align}
$$

where the basis is $$B=\langle\vec w,\vec x,\vec y\rangle$$ .

Now, to prove of Desargue's Theorem, use the lemma to fix homogeneous coordinate vectors and a basis.

$$
\text{Rep}_B(\vec{t}_1)=\begin{pmatrix}1\\0\\0\end{pmatrix}\quad \text{Rep}_B(\vec{u}_1)=\begin{pmatrix}0\\1\\0\end{pmatrix}\quad \text{Rep}_B(\vec{v}_1)=\begin{pmatrix}0\\0\\1\end{pmatrix}\quad \text{Rep}_B(\vec{o})=\begin{pmatrix}1\\1\\1\end{pmatrix}
$$

Because the projective point $$T_2$$ is incident on the projective line $$OT_1$$ , any homogeneous coordinate vector for $$T_2$$ lies in the plane through the origin in $$\R^3$$ that is spanned by homogeneous coordinate vectors of $$O$$ and $$T_1$$ :

$$
\text{Rep}_B(\vec{t}_2)=a\begin{pmatrix}1\\1\\1\end{pmatrix}+b\begin{pmatrix}1\\0\\0\end{pmatrix}
$$

for some scalars $$a$$ and $$b$$ . That is, the homogenous coordinate vectors of members $$T_2$$ of the line $$OT_1$$ are of the form on the left below, and the forms for $$U_2,V_2$$ are similar.

$$
\text{Rep}_B(\vec{t}_2)=\begin{pmatrix}t_2\\1\\1\end{pmatrix}\qquad \text{Rep}_B(\vec{u}_2)=\begin{pmatrix}1\\u_2\\1\end{pmatrix}\qquad \text{Rep}_B(\vec{v}_2)=\begin{pmatrix}1\\1\\v_2\end{pmatrix}
$$

The projective line $$T_1U_1$$ is the image of a plane through the origin in $$\R^3$$ . A quick way to get its equation is to note that any vector in it is linearly dependent on the vectors for $$T_1$$ and $$U_1$$ and so this determinant is zero.

$$
\begin{vmatrix}1&0&x\\0&1&y\\0&0&z\end{vmatrix}=0\qquad\implies\qquad z=0
$$

The equation of the plane in $$\R^3$$ whose image is the projective line $$T_2U_2$$ is this.

$$
\begin{vmatrix}t_2&1&x\\1&u_2&y\\1&1&z\end{vmatrix}=0\qquad\implies\qquad(1-u_2)x+(1-t_2)y+(t_2u_2-1)z=0
$$

Finding the intersection of the two is routine.

$$
T_1U_1\cap T_2U_2=\begin{pmatrix}t_2-1\\1-u_2\\0\end{pmatrix}
$$

(This is, of course, the homogeneous coordinate vector of a projective point.) The other two intersections are similar.

$$
T_1V_1\cap T_2V_2=\begin{pmatrix}1-t_2\\0\\v_2-1\end{pmatrix}\qquad U_1V_1\cap U_2V_2=\begin{pmatrix}0\\u_2-1\\1-v_2\end{pmatrix}
$$

The proof is finished by noting that these projective points are on one projective line because the sum of the three homogeneous coordinate vectors is zero.

Every projective theorem has a translation to a Euclidean version, although the Euclidean result is often messier to state and prove. Desargue's theorem illustrates this. In the translation to Euclidean space, the case where $$O$$ lies on the ideal line must be treated separately for then the lines $$T_1T_2,U_1U_2,V_1V_2$$ are parallel.

The parenthetical remark following the statement of Desargue's Theorem suggests thinking of the Euclidean pictures as figures from projective geometry for a model of very large radius. That is, just as a small area of the earth appears flat to people living there, the projective plane is also "locally Euclidean".

Although its local properties are the familiar Euclidean ones, there is a global property of the projective plane that is quite different. The picture below shows a projective point. At that point is drawn an $$xy$$-axis. There is something interesting about the way this axis appears at the antipodal ends of the sphere. In the northern hemisphere, where the axis are drawn in black, a right hand put down with fingers on the $$x$$-axis will have the thumb point along the $$y$$-axis. But the antipodal axis has just the opposite: a right hand placed with its fingers on the $$x$$-axis will have the thumb point in the wrong way, instead, it is a left hand that works. Briefly, the projective plane is not orientable: in this geometry, left and right handedness are not fixed properties of figures.

The sequence of pictures below dramatizes this non-orientability. They sketch a trip around this space in the direction of the $$y$$ part of the $$xy$$-axis. (Warning: the trip shown is not halfway around, it is a full circuit. True, if we made this into a movie then we could watch the northern hemisphere spots in the drawing above gradually rotate about halfway around the sphere to the last picture below. And we could watch the southern hemisphere spots in the picture above slide through the south pole and up through the equator to the last picture. But: the spots at either end of the dashed line are the same projective point. We don't need to continue on much further; we are pretty much back to the projective point where we started by the last picture.)

$$\implies$$  $$\implies$$

At the end of the circuit, the $$x$$ part of the $$xy$$-axes sticks out in the other direction. Thus, in the projective plane we cannot describe a figure as right-{} or left-handed (another way to make this point is that we cannot describe a spiral as clockwise or counterclockwise).

This exhibition of the existence of a non-orientable space raises the question of whether our universe is orientable: is it possible for an astronaut to leave right-handed and return left-handed? An excellent nontechnical reference is (Gardner 1990). A classic science fiction story about orientation reversal is (Clarke 1982).

So projective geometry is mathematically interesting, in addition to the natural way in which it arises in art. It is more than just a technical device to shorten some proofs. For an overview, see (Courant & Robbins 1978). The approach we've taken here, the analytic approach, leads to quick theorems and — most importantly for us — illustrates the power of linear algebra (see Hanes (1990), Ryan (1986), and Eggar (1998)). But another approach, the synthetic approach of deriving the results from an axiom system, is both extraordinarily beautiful and is also the historical route of development. Two fine sources for this approach are (Coxeter 1974) or (Seidenberg 1962). An interesting and easy application is (Davies 1990).

### Exercises

**Problem 1**  —

What is the equation of this point?

$$
\begin{pmatrix}1\\0\\0\end{pmatrix}
$$

**Problem 2**  —

1. Find the line incident on these points in the projective plane.

$$
\begin{pmatrix}1\\2\\3\end{pmatrix},\begin{pmatrix}4\\5\\6\end{pmatrix}
$$

2. Find the point incident on both of these projective lines.

$$
(1\ 2\ 3),(4\ 5\ 6)
$$

**Problem 3**  —

Find the formula for the line incident on two projective points. Find the formula for the point incident on two projective lines.

**Problem 4**  —

Prove that the definition of incidence is independent of the choice of the representatives of $$p$$ and $$L$$ . That is, if $$p_1,p_2,p_3$$ and $$q_1,q_2,q_3$$ are two triples of homogeneous coordinates for $$p$$ , and $$L_1,L_2,L_3$$ and $$M_1,M_2,M_3$$ are two triples of homogeneous coordinates for $$L$$ , prove that $$p_1L_1+p_2L_2+p_3L_3=0$$ if and only if $$q_1M_1+q_2M_2+q_3M_3=0$$ .

**Problem 5**  —

Give a drawing to show that central projection does not preserve circles, that a circle may project to an ellipse. Can a (non-circular) ellipse project to a circle?

**Problem 6**  —

Give the formula for the correspondence between the non-equatorial part of the antipodal modal of the projective plane, and the plane $$z=1$$ .

**Problem 7**  —

(Pappus's Theorem) Assume that $$T_0,U_0,V_0$$ are collinear and that $$T_1,U_1,V_1$$ are collinear. Consider these three points:

1. the intersection $$V_2$$ of the lines $$T_0U_1,T_1U_0$$
2. the intersection $$U_2$$ of the lines $$T_0V_1,T_1V_0$$
3. the intersection $$T_2$$ of $$U_0V_1$$ and $$U_1V_0$$  
1. Draw a (Euclidean) picture.
2. Apply the lemma used in Desargue's Theorem to get simple homogeneous coordinate vectors for the $$T$$'s and $$V_0$$ .
3. Find the resulting homogeneous coordinate vectors for $$U$$'s (these must each involve a parameter as, e.g. $$U_0$$ could be anywhere on the $$T_0V_0$$ line).
4. Find the resulting homogeneous coordinate vectors for $$V_1$$ . (*Hint:* it involves two parameters.)
5. Find the resulting homogeneous coordinate vectors for $$V_2$$ . (It also involves two parameters.)
6. Show that the product of the three parameters is 1.
7. Verify that $$V_2$$ is on the $$T_2U_2$$ line..

Solutions

### See also

- Projective Geometry
- Category:Book:Projective Geometry

### References

- Clarke, Arthur C. (1982), *Great SF Stories 8: Technical Error*, DAW Books.
- Courant, Richard; Robbins, Herbert (1978), *What is Mathematics?*, Oxford University Press.
- Coxeter, H.S.M. (1974), *Projective Geometry* (Second ed.), Springer-Verlag.
- Davies, Thomas D. (1990), "New Evidence Places Peary at the Pole", *National Geographic Magazine*, **177** (1): 44 {{citation}}: Unknown parameter |month= ignored (help).
- Eggar, M.H. (1998), "Pinhole Cameras, Perspective, and Projective Geometry", *American Mathematical Monthly*, American Mathematical Society: 618–630 {{citation}}: Unknown parameter |month= ignored (help).
- Gardner, Martin (1990), *The New Ambidextrous Universe* (Third revised ed.), W. H. Freeman and Company.
- Hanes, Kit (1990), "Analytic Projective Geometry and its Applications", *UMAP Modules* (UMAP UNIT 710): 111.
- Ryan, Patrick J. (1986), *Euclidean and Non-Euclidean Geometry: an Analytic Approach*, Cambridge University Press.
- Seidenberg, A. (1962), *Lectures in Projective Geometry*, Van Nostrandg.

---

*Source: Wikibooks, Linear Algebra/Topic: Projective Geometry (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Projective_Geometry), by Wikibooks contributors, CC BY-SA 4.0.*
