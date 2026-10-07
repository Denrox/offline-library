# Vectors in Space

"Higher-dimensional geometry" sounds exotic. It is exotic— interesting and eye-opening. But it isn't distant or unreachable.

We begin by defining one-dimensional space to be the set $$\mathbb{R}^1$$. To see that definition is reasonable, draw a one-dimensional space

and make the usual correspondence with $$\mathbb{R}$$: pick a point to label $$0$$ and another to label $$1$$.

Now, with a scale and a direction, finding the point corresponding to, say $$+2.17$$, is easy— start at $$0$$ and head in the direction of $$1$$ (i.e., the positive direction), but don't stop there, go $$2.17$$ times as far.

The basic idea here, combining magnitude with direction, is the key to extending to higher dimensions.

An object comprised of a magnitude and a direction is a **vector** (we will use the same word as in the previous section because we shall show below how to describe such an object with a column vector). We can draw a vector as having some length, and pointing somewhere.

There is a subtlety here— these vectors

are equal, even though they start in different places, because they have equal lengths and equal directions. Again: those vectors are not just alike, they are equal.

How can things that are in different places be equal? Think of a vector as representing a displacement ("vector" is Latin for "carrier" or "traveler"). These squares undergo the same displacement, despite that those displacements start in different places.

Sometimes, to emphasize this property vectors have of not being anchored, they are referred to as **free** vectors. Thus, these free vectors are equal as each is a displacement of one over and two up.

More generally, vectors in the plane are the same if and only if they have the same change in first components and the same change in second components: the vector extending from $$(a_1,a_2)$$ to $$(b_1,b_2)$$ equals the vector from $$(c_1,c_2)$$ to $$(d_1,d_2)$$ if and only if $$b_1-a_1=d_1-c_1$$ and $$b_2-a_2=d_2-c_2$$.

An expression like "the vector that, were it to start at $$(a_1,a_2)$$, would extend to $$(b_1,b_2)$$" is awkward. We instead describe such a vector as

$$
\begin{pmatrix} b_1-a_1 \\ b_2-a_2 \end{pmatrix}
$$

so that, for instance, the "one over and two up" arrows shown above picture this vector.

$$
\begin{pmatrix} 1 \\ 2 \end{pmatrix}
$$

We often draw the arrow as starting at the origin, and we then say it is in the **canonical position** (or **natural position**). When the vector

$$
\begin{pmatrix} b_1-a_1 \\ b_2-a_2 \end{pmatrix}
$$

is in its canonical position then it extends to the endpoint $$(b_1-a_1,b_2-a_2)$$.

We typically just refer to "the point  
$$\begin{pmatrix} 1 \\ 2 \end{pmatrix}$$"

rather than "the endpoint of the canonical position of" that vector.

Thus, we will call both of these sets $$\mathbb{R}^2$$.

$$
\{(x_1,x_2)\,\big|\, x_1,x_2\in\mathbb{R}\} \qquad \{\begin{pmatrix} x_1 \\ x_2 \end{pmatrix}\,\big|\, x_1,x_2\in\mathbb{R}\}
$$

In the prior section we defined vectors and vector operations with an algebraic motivation;

$$
r\cdot\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} rv_1 \\ rv_2 \end{pmatrix} \qquad \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} + \begin{pmatrix} w_1 \\ w_2 \end{pmatrix} = \begin{pmatrix} v_1+w_1 \\ v_2+w_2 \end{pmatrix}
$$

we can now interpret those operations geometrically. For instance, if $$\vec{v}$$ represents a displacement then $$3\vec{v}\,$$ represents a displacement in the same direction but three times as far, and $$-1\vec{v}\,$$ represents a displacement of the same distance as $$\vec{v}\,$$ but in the opposite direction.

And, where $$\vec{v}$$ and $$\vec{w}$$ represent displacements, $$\vec{v}+\vec{w}$$ represents those displacements combined.

The long arrow is the combined displacement in this sense: if, in one minute, a ship's motion gives it the displacement relative to the earth of $$\vec{v}$$ and a passenger's motion gives a displacement relative to the ship's deck of $$\vec{w}$$, then $$\vec{v}+\vec{w}$$ is the displacement of the passenger relative to the earth.

Another way to understand the vector sum is with the **parallelogram rule**. Draw the parallelogram formed by the vectors $$\vec{v}_1,\vec{v}_2$$ and then the sum $$\vec{v}_1+\vec{v}_2$$ extends along the diagonal to the far corner.

The above drawings show how vectors and vector operations behave in $$\mathbb{R}^2$$. We can extend to $$\mathbb{R}^3$$, or to even higher-dimensional spaces where we have no pictures, with the obvious generalization: the free vector that, if it starts at $$(a_1,\ldots,a_n)$$, ends at $$(b_1,\ldots,b_n)$$, is represented by this column

$$
\begin{pmatrix} b_1-a_1 \\ \vdots \\ b_n-a_n \end{pmatrix}
$$

(vectors are equal if they have the same representation), we aren't too careful to distinguish between a point and the vector whose canonical representation ends at that point,

$$
\mathbb{R}^n= \{\begin{pmatrix} v_1 \\ \vdots \\ v_n \end{pmatrix}\,\big|\, v_1,\ldots,v_n\in\mathbb{R}\}
$$

and addition and scalar multiplication are component-wise.

Having considered points, we now turn to the lines.

In $$\mathbb{R}^2$$, the line through $$(1,2)$$ and $$(3,1)$$ s comprised of (the endpoints of) the vectors in this set

$$
\{ \begin{pmatrix} 1 \\ 2 \end{pmatrix}+t\cdot\begin{pmatrix} 2 \\ -1 \end{pmatrix}\,\big|\, t\in\mathbb{R}\}
$$

That description expresses this picture.

The vector associated with the parameter $$t$$ has its whole body in the line— it is a **direction vector** for the line. Note that points on the line to the left of $$x=1$$ are described using negative values of $$t$$.

In $$\mathbb{R}^3$$, the line through $$(1,2,1)$$ and $$(2,3,2)$$ is the set of (endpoints of) vectors of this form

and lines in even higher-dimensional spaces work in the same way.

If a line uses one parameter, so that there is freedom to move back and forth in one dimension, then a plane must involve two. For example, the plane through the points $$(1,0,5)$$, $$(2,1,-3)$$, and $$(-2,4,0.5)$$ consists of (endpoints of) the vectors in

$$
\{ \begin{pmatrix} 1 \\ 0 \\ 5 \end{pmatrix} +t\cdot\begin{pmatrix} 1 \\ 1 \\ -8 \end{pmatrix} +s\cdot\begin{pmatrix} -3 \\ 4 \\ -4.5 \end{pmatrix} \,\big|\, t,s\in\mathbb{R} \}
$$

(the column vectors associated with the parameters

$$
\begin{pmatrix} 1 \\ 1 \\ -8 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ -3 \end{pmatrix} - \begin{pmatrix} 1 \\ 0 \\ 5 \end{pmatrix} \qquad \begin{pmatrix} -3 \\ 4 \\ -4.5 \end{pmatrix} = \begin{pmatrix} -2 \\ 4 \\ 0.5 \end{pmatrix} - \begin{pmatrix} 1 \\ 0 \\ 5 \end{pmatrix}
$$

are two vectors whose whole bodies lie in the plane). As with the line, note that some points in this plane are described with negative $$t$$'s or negative $$s$$'s or both.

A description of planes that is often encountered in algebra and calculus uses a single equation as the condition that describes the relationship among the first, second, and third coordinates of points in a plane.

The translation from such a description to the vector description that we favor in this book is to think of the condition as a one-equation linear system and parametrize $$x=(1/2)(4-y-z)$$.

Generalizing from lines and planes, we define a **$$k$$-dimensional linear surface** (or **$$k$$-flat**) in $$\mathbb{R}^n$$ to be $$\{\vec{p}+t_1\vec{v}_1+t_2\vec{v}_2+\cdots+t_k\vec{v}_k \,\big|\, t_1,\ldots ,t_k\in\mathbb{R}\}$$ where $$\vec{v}_1,\ldots,\vec{v}_k\in\mathbb{R}^n$$. For example, in $$\mathbb{R}^4$$,

$$
\{\begin{pmatrix} 2 \\ \pi \\ 3 \\ -0.5 \end{pmatrix} +t\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} \,\big|\, t\in\mathbb{R}\}
$$

is a line,

$$
\{ \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +t\begin{pmatrix} 1 \\ 1 \\ 0 \\ -1 \end{pmatrix} +s\begin{pmatrix} 2 \\ 0 \\ 1 \\ 0 \end{pmatrix} \,\big|\, t,s\in\mathbb{R}\}
$$

is a plane, and

$$
\{ \begin{pmatrix} 3 \\ 1 \\ -2 \\ 0.5 \end{pmatrix} +r\begin{pmatrix} 0 \\ 0 \\ 0 \\ -1 \end{pmatrix} +s\begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix} +t\begin{pmatrix} 2 \\ 0 \\ 1 \\ 0 \end{pmatrix} \,\big|\, r,s,t\in\mathbb{R}\}
$$

is a three-dimensional linear surface. Again, the intuition is that a line permits motion in one direction, a plane permits motion in combinations of two directions, etc.

A linear surface description can be misleading about the dimension— this

$$
L=\{ \begin{pmatrix} 1 \\ 0 \\ -1 \\ -2 \end{pmatrix} +t\begin{pmatrix} 1 \\ 1 \\ 0 \\ -1 \end{pmatrix} +s\begin{pmatrix} 2 \\ 2 \\ 0 \\ -2 \end{pmatrix} \,\big|\, t,s\in\mathbb{R}\}
$$

is a **degenerate** plane because it is actually a line.

$$
L=\{ \begin{pmatrix} 1 \\ 0 \\ -1 \\ -2 \end{pmatrix} +r\begin{pmatrix} 1 \\ 1 \\ 0 \\ -1 \end{pmatrix} \,\big|\, r\in\mathbb{R}\}
$$

We shall see in the Linear Independence section of Chapter Two what relationships among vectors causes the linear surface they generate to be degenerate.

We finish this subsection by restating our conclusions from the first section in geometric terms. First, the solution set of a linear system with $$n$$ unknowns is a linear surface in $$\mathbb{R}^n$$. Specifically, it is a $$k$$-dimensional linear surface, where $$k$$ is the number of free variables in an echelon form version of the system. Second, the solution set of a homogeneous linear system is a linear surface passing through the origin. Finally, we can view the general solution set of any linear system as being the solution set of its associated homogeneous system offset from the origin by a vector, namely by any particular solution.

### Exercises  
*This exercise is recommended for all readers.*

**Problem 1**  —

Find the canonical name for each vector.

1. the vector from $$(2,1)$$ to $$(4,2)$$ in $$\mathbb{R}^2$$
2. the vector from $$(3,3)$$ to $$(2,5)$$ in $$\mathbb{R}^2$$
3. the vector from $$(1,0,6)$$ to $$(5,0,3)$$ in $$\mathbb{R}^3$$
4. the vector from $$(6,8,8)$$ to $$(6,8,8)$$ in $$\mathbb{R}^3$$  
*This exercise is recommended for all readers.*

**Problem 2**  —

Decide if the two vectors are equal.

1. the vector from $$(5,3)$$ to $$(6,2)$$ and the vector from $$(1,-2)$$ to $$(1,1)$$
2. the vector from $$(2,1,1)$$ to $$(3,0,4)$$ and the vector from $$(5,1,4)$$ to $$(6,0,7)$$  
*This exercise is recommended for all readers.*

**Problem 3**  —

Does $$(1,0,2,1)$$ lie on the line through $$(-2,1,1,0)$$ and $$(5,10,-1,4)$$?  
*This exercise is recommended for all readers.*

**Problem 4**  —

1. Describe the plane through $$(1,1,5,-1)$$, $$(2,2,2,0)$$, and $$(3,1,0,4)$$.
2. Is the origin in that plane?

**Problem 5**  —

Describe the plane that contains the following point and line.

$$
\begin{pmatrix} 2 \\ 0 \\ 3 \end{pmatrix} \qquad \{\begin{pmatrix} -1 \\ 0 \\ -4 \end{pmatrix} +\begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix}t \,\big|\, t\in\mathbb{R}\}
$$

*This exercise is recommended for all readers.*

**Problem 6**  —

Find the intersection of these planes:

$$
\{\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}t+ \begin{pmatrix} 0 \\ 1 \\ 3 \end{pmatrix}s \,\big|\, t,s\in\mathbb{R}\}, \qquad \{\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} +\begin{pmatrix} 0 \\ 3 \\ 0 \end{pmatrix}k+ \begin{pmatrix} 2 \\ 0 \\ 4 \end{pmatrix}m \,\big|\, k,m\in\mathbb{R}\}.
$$

*This exercise is recommended for all readers.*

**Problem 7**  —

Find the intersection of each of the following pair, if possible.

1. $$\{\begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix}+t\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \,\big|\, t\in\mathbb{R}\},$$ $$\{\begin{pmatrix} 1 \\ 3 \\ -2 \end{pmatrix}+s\begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix} \,\big|\, s\in\mathbb{R}\}.$$
2. $$\{\begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}+t\begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} \,\big|\, t\in\mathbb{R}\},$$ $$\{s\begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix} +w\begin{pmatrix} 0 \\ 4 \\ 1 \end{pmatrix} \,\big|\, s,w\in\mathbb{R}\}.$$

**Problem 8**  —

When a plane does not pass through the origin, performing operations on vectors whose bodies lie in it is more complicated than when the plane passes through the origin. Consider the picture in this subsection of the plane

$$
\{\begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix} +\begin{pmatrix} -0.5 \\ 1 \\ 0 \end{pmatrix} y +\begin{pmatrix} -0.5 \\ 0 \\ 1 \end{pmatrix} z \,\big|\, y,z\in\mathbb{R}\}
$$

and the three vectors it shows, with endpoints $$(2,0,0)$$, $$(1.5,1,0)$$, and $$(1.5,0,1)$$.

1. Redraw the picture, including the vector in the plane that is twice as long as the one with endpoint $$(1.5,1,0)$$. The endpoint of your vector is not $$(3,2,0)$$; what is it?
2. Redraw the picture, including the parallelogram in the plane that shows the sum of the vectors ending at $$(1.5,0,1)$$ and $$(1.5,1,0)$$. The endpoint of the sum, on the diagonal, is not $$(3,1,1)$$; what is it?

**Problem 9**  —

Show that the line segments $$\overline{(a_1,a_2)(b_1,b_2)}$$ and $$\overline{(c_1,c_2)(d_1,d_2)}$$ have the same lengths and slopes *if* $$b_1-a_1=d_1-c_1$$ and $$b_2-a_2=d_2-c_2$$. Can we replace 'if' by 'if and only if'?

**Problem 10**  —

How should $$\mathbb{R}^0$$ be defined?  
*This exercise is recommended for all readers.*

**? Problem 11**  —

A person traveling eastward at a rate of $$3$$ miles per hour finds that the wind appears to blow directly from the north. On doubling his speed it appears to come from the north east. What was the wind's velocity? (Klamkin 1957)  
*This exercise is recommended for all readers.*

**Problem 12**  —

Euclid describes a plane as "a surface which lies evenly with the straight lines on itself". Commentators (e.g., Heron) have interpreted this to mean "(A plane surface is) such that, if a straight line pass through two points on it, the line coincides wholly with it at every spot, all ways". (Translations from Heath 1956, pp. 171-172.) Do planes, as described in this section, have that property? Does this description adequately define planes?

Solutions

### References

- Klamkin, M. S. (proposer) (1957), "Trickie T-27", *Mathematics Magazine*, **30** (3): 173 {{citation}}: Unknown parameter |month= ignored (help).
- Heath, T. (1956), *Euclid's Elements*, vol. 1, Dover.

---

*Source: Wikibooks, Linear Algebra/Vectors in Space (https://en.wikibooks.org/wiki/Linear_Algebra/Vectors_in_Space), by Wikibooks contributors, CC BY-SA 4.0.*
