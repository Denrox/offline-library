# Topic: Dimensional Analysis

"You can't add apples and oranges," the old saying goes. It reflects our experience that in applications the quantities have units and keeping track of those units is worthwhile. Everyone has done calculations such as this one that use the units as a check.

$$
60\,\frac{\text{sec}}{\text{min}} \cdot 60\,\frac{\text{min}}{\text{hr}} \cdot 24\,\frac{\text{hr}}{\text{day}} \cdot 365\,\frac{\text{day}}{\text{year}} = 31\,536\,000\,\frac{\text{sec}}{\text{year}}
$$

However, the idea of including the units can be taken beyond bookkeeping. It can be used to draw conclusions about what relationships are possible among the physical quantities.

To start, consider the physics equation: $$\text{distance}=16\cdot(\text{time})^2$$. If the distance is in feet and the time is in seconds then this is a true statement about falling bodies. However it is not correct in other unit systems; for instance, it is not correct in the meter-second system. We can fix that by making the $$16$$ a *dimensional constant*.

$$
\text{dist}=16\,\frac{\text{ft}}{\text{sec}^2}\cdot (\text{time})^2
$$

For instance, the above equation holds in the yard-second system.

$$
\text{distance in yards}=16\,\frac{(1/3)\,\text{yd}}{\text{sec}^2} \cdot (\text{time in sec})^2 =\frac{16}{3}\,\frac{\text{yd}}{\text{sec}^2} \cdot (\text{time in sec})^2
$$

So our first point is that by "including the units" we mean that we are restricting our attention to equations that use dimensional constants.

By using dimensional constants, we can be vague about units and say only that all quantities are measured in combinations of some units of length $$L$$, mass $$M$$, and time $$T$$. We shall refer to these three as **dimensions** (these are the only three dimensions that we shall need in this Topic). For instance, velocity could be measured in $$\text{feet}/\text{second}$$ or $$\text{fathoms}/\text{hour}$$, but in all events it involves some unit of length divided by some unit of time so the **dimensional formula** of velocity is $$L/T$$. Similarly, the dimensional formula of density is $$M/L^3$$. We shall prefer using negative exponents over the fraction bars and we shall include the dimensions with a zero exponent, that is, we shall write the dimensional formula of velocity as $$L^1M^0T^{-1}$$ and that of density as $$L^{-3}M^1T^0$$.

In this context, "You can't add apples to oranges" becomes the advice to check that all of an equation's terms have the same dimensional formula. An example is this version of the falling body equation: $$d-gt^2=0$$. The dimensional formula of the $$d$$ term is $$L^1M^0T^0$$. For the other term, the dimensional formula of $$g$$ is $$L^1M^0T^{-2}$$ ($$g$$ is the dimensional constant given above as $$16\,\text{ft}/\text{sec}^2$$) and the dimensional formula of $$t$$ is $$L^0M^0T^1$$, so that of the entire $$gt^2$$ term is $$L^1M^0T^{-2}(L^0M^0T^1)^2=L^1M^0T^0$$. Thus the two terms have the same dimensional formula. An equation with this property is **dimensionally homogeneous**.

Quantities with dimensional formula $$L^0M^0T^0$$ are **dimensionless**. For example, we measure an angle by taking the ratio of the subtended arc to the radius

which is the ratio of a length to a length $$L^1M^0T^0/L^1M^0T^0$$ and thus angles have the dimensional formula $$L^0M^0T^0$$.

The classic example of using the units for more than bookkeeping, using them to draw conclusions, considers the formula for the period of a pendulum.

$$
p=\text{--some expression involving the length of the string, etc.--}
$$

The period is in units of time $$L^0M^0T^1$$. So the quantities on the other side of the equation must have dimensional formulas that combine in such a way that their $$L$$'s and $$M$$'s cancel and only a single $$T$$ remains. The table on below has the quantities that an experienced investigator would consider possibly relevant. The only dimensional formulas involving $$L$$ are for the length of the string and the acceleration due to gravity. For the $$L$$'s of these two to cancel, when they appear in the equation they must be in ratio, e.g., as $$(\ell/g)^2$$, or as $$\cos(\ell/g)$$, or as $$(\ell/g)^{-1}$$. Therefore the period is a function of $$\ell/g$$.

This is a remarkable result: with a pencil and paper analysis, before we ever took out the pendulum and made measurements, we have determined something about the relationship among the quantities.

To do dimensional analysis systematically, we need to know two things (arguments for these are in (Bridgman 1931), Chapter II and IV). The first is that each equation relating physical quantities that we shall see involves a sum of terms, where each term has the form

$$
m_1^{p_1}m_2^{p_2}\cdots m_k^{p_k}
$$

for numbers $$m_1$$, ..., $$m_k$$ that measure the quantities.

For the second, observe that an easy way to construct a dimensionally homogeneous expression is by taking a product of dimensionless quantities or by adding such dimensionless terms. Buckingham's Theorem states that any complete relationship among quantities with dimensional formulas can be algebraically manipulated into a form where there is some function $$f$$ such that

$$
f(\Pi_1,\ldots,\Pi_n)=0
$$

for a complete set $$\{\Pi_1,\ldots,\Pi_n\}$$ of dimensionless products. (The first example below describes what makes a set of dimensionless products "complete".) We usually want to express one of the quantities, $$m_1$$ for instance, in terms of the others, and for that we will assume that the above equality can be rewritten

$$
m_1=m_2^{-p_2}\cdots m_k^{-p_k}\cdot \hat{f}(\Pi_2,\ldots,\Pi_n)
$$

where $$\Pi_1=m_1m_2^{p_2}\cdots m_k^{p_k}$$ is dimensionless and the products $$\Pi_2$$, ..., $$\Pi_n$$ don't involve $$m_1$$ (as with $$f$$, here $$\hat{f}$$ is just some function, this time of $$n-1$$ arguments). Thus, to do dimensional analysis we should find which dimensionless products are possible.

For example, consider again the formula for a pendulum's period.

- *quantity*   *dimensional*

*formula*

- period $$p$$   $$L^0M^0T^1$$
- length of string $$\ell$$   $$L^1M^0T^0$$
- mass of bob $$m$$   $$L^0M^1T^0$$
- acceleration due to gravity $$g$$   $$L^1M^0T^{-2}$$
- arc of swing $$\theta$$   $$L^0M^0T^0$$

By the first fact cited above, we expect the formula to have (possibly sums of terms of) the form $$p^{p_1}\ell^{p_2}m^{p_3}g^{p_4}\theta^{p_5}$$. To use the second fact, to find which combinations of the powers $$p_1$$, ..., $$p_5$$ yield dimensionless products, consider this equation.

$$
(L^0M^0T^1)^{p_1}(L^1M^0T^0)^{p_2}(L^0M^1T^0)^{p_3} (L^1M^0T^{-2})^{p_4}(L^0M^0T^0)^{p_5} =L^0M^0T^0
$$

It gives three conditions on the powers.

$$
\begin{array}{rcrcrcrcrcr} &\ &p_2 &\ & &+ &p_4 & & &= &0 \\ & & & &p_3 & & & & &= &0 \\ p_1& & & & &- &2p_4 & & &= &0 \end{array}
$$

Note that $$p_3$$ is $$0$$ and so the mass of the bob does not affect the period. Gaussian reduction and parametrization of that system gives this

$$
\{\begin{pmatrix} p_1 \\ p_2 \\ p_3 \\ p_4 \\ p_5 \end{pmatrix}= \begin{pmatrix} 1 \\ -1/2 \\ 0 \\ 1/2 \\ 0 \end{pmatrix}p_1+ \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}p_5 \,\big|\, p_1,p_5\in\mathbb{R}\}
$$

(we've taken $$p_1$$ as one of the parameters in order to express the period in terms of the other quantities).

Here is the linear algebra. The set of dimensionless products contains all terms $$p^{p_1}\ell^{p_2}m^{p_3}a^{p_4}\theta^{p_5}$$ subject to the conditions above. This set forms a vector space under the "$$+$$" operation of multiplying two such products and the "$$\cdot$$" operation of raising such a product to the power of the scalar (see Problem 5). The term "complete set of dimensionless products" in Buckingham's Theorem means a basis for this vector space.

We can get a basis by first taking $$p_1=1$$, $$p_5=0$$ and then $$p_1=0$$, $$p_5=1$$. The associated dimensionless products are $$\Pi_1=p\ell^{-1/2}g^{1/2}$$ and $$\Pi_2=\theta$$. Because the set $$\{\Pi_1,\Pi_2\}$$ is complete, Buckingham's Theorem says that

$$
p = \ell^{1/2}g^{-1/2}\cdot\hat{f}(\theta) = \sqrt{\ell/g}\cdot\hat{f}(\theta)
$$

where $$\hat{f}$$ is a function that we cannot determine from this analysis (a first year physics text will show by other means that for small angles it is approximately the constant function $$\hat{f}(\theta)=2\pi$$).

Thus, analysis of the relationships that are possible between the quantities with the given dimensional formulas has produced a fair amount of information: a pendulum's period does not depend on the mass of the bob, and it rises with the square root of the length of the string.

For the next example we try to determine the period of revolution of two bodies in space orbiting each other under mutual gravitational attraction. An experienced investigator could expect that these are the relevant quantities.

- *quantity*   *dimensional*

*formula*

- period $$p$$   $$L^0M^0T^1$$
- mean separation $$r$$   $$L^1M^0T^0$$
- first mass $$m_1$$   $$L^0M^1T^0$$
- second mass $$m_2$$   $$L^0M^1T^0$$
- grav. constant $$G$$   $$L^3M^{-1}T^{-2}$$

To get the complete set of dimensionless products we consider the equation

$$
(L^0M^0T^1)^{p_1}(L^1M^0T^0)^{p_2}(L^0M^1T^0)^{p_3}(L^0M^1T^0)^{p_4} (L^3M^{-1}T^{-2})^{p_5}=L^0M^0T^0
$$

which results in a system

$$
\begin{array}{rcrcrcrcrcr} & &p_2 & & & & &+ &3p_5 &= &0 \\ & & & &p_3 &+ &p_4 &- &p_5 &= &0 \\ p_1 & & & & & & &- &2p_5 &= &0 \end{array}
$$

with this solution.

$$
\{\begin{pmatrix} 1 \\ -3/2 \\ 1/2 \\ 0 \\ 1/2 \end{pmatrix}p_1 +\begin{pmatrix} 0 \\ 0 \\ -1 \\ 1 \\ 0 \end{pmatrix}p_4 \,\big|\, p_1,p_4\in\mathbb{R}\}
$$

As earlier, the linear algebra here is that the set of dimensionless products of these quantities forms a vector space, and we want to produce a basis for that space, a "complete" set of dimensionless products. One such set, gotten from setting $$p_1=1$$ and $$p_4=0$$, and also setting $$p_1=0$$ and $$p_4=1$$ is $$\{\Pi_1=pr^{-3/2}m_1^{1/2}G^{1/2},\,\Pi_2=m_1^{-1}m_2\}$$. With that, Buckingham's Theorem says that any complete relationship among these quantities is stateable this form.

$$
p = r^{3/2}m_1^{-1/2}G^{-1/2}\cdot\hat{f}(m_1^{-1}m_2) = \frac{r^{3/2}}{\sqrt{Gm_1}}\cdot\hat{f}(m_2/m_1)
$$

*Remark.* An important application of the prior formula is when $$m_1$$ is the mass of the sun and $$m_2$$ is the mass of a planet. Because $$m_1$$ is very much greater than $$m_2$$, the argument to $$\hat{f}$$ is approximately $$0$$, and we can wonder whether this part of the formula remains approximately constant as $$m_2$$ varies. One way to see that it does is this. The sun is so much larger than the planet that the mutual rotation is approximately about the sun's center. If we vary the planet's mass $$m_2$$ by a factor of $$x$$ (e.g., Venus's mass is $$x=0.815$$ times Earth's mass), then the force of attraction is multiplied by $$x$$, and $$x$$ times the force acting on $$x$$ times the mass gives, since $$F=ma$$, the same acceleration, about the same center (approximately). Hence, the orbit will be the same and so its period will be the same, and thus the right side of the above equation also remains unchanged (approximately). Therefore, $$\hat{f}(m_2/m_1)$$ is approximately constant as $$m_2$$ varies. This is Kepler's Third Law: the square of the period of a planet is proportional to the cube of the mean radius of its orbit about the sun.

The final example was one of the first explicit applications of dimensional analysis. Lord Raleigh considered the speed of a wave in deep water and suggested these as the relevant quantities.

- *quantity*   *dimensional*

*formula*

- velocity of the wave $$v$$   $$L^1M^0T^{-1}$$
- density of the water $$d$$   $$L^{-3}M^1T^0$$
- acceleration due to gravity $$g$$   $$L^1M^0T^{-2}$$
- wavelength $$\lambda$$   $$L^1M^0T^0$$

The equation

$$
(L^1M^0T^{-1})^{p_1}(L^{-3}M^1T^0)^{p_2} (L^1M^0T^{-2})^{p_3}(L^1M^0T^0)^{p_4}=L^0M^0T^0
$$

gives this system

$$
\begin{array}{rcrcrcrcr} p_1 &- &3p_2 &+ &p_3 &+ &p_4 &= &0 \\ & &p_2 & & & & &= &0 \\ -p_1 & & &- &2p_3 & & &= &0 \end{array}
$$

with this solution space

$$
\{\begin{pmatrix} 1 \\ 0 \\ -1/2 \\ -1/2 \end{pmatrix}p_1 \,\big|\, p_1\in \mathbb{R}\}
$$

(as in the pendulum example, one of the quantities $$d$$ turns out not to be involved in the relationship). There is one dimensionless product, $$\Pi_1=vg^{-1/2}\lambda^{-1/2}$$, and so $$v$$ is $$\sqrt{\lambda g}$$ times a constant ($$\hat{f}$$ is constant since it is a function of no arguments).

As the three examples above show, dimensional analysis can bring us far toward expressing the relationship among the quantities. For further reading, the classic reference is (Bridgman 1931)—this brief book is delightful. Another source is (Giordano, Wells & Wilde 1987).. A description of dimensional analysis's place in modeling is in (Giordano, Jaye & Weir 1986)..

### Exercises

**Problem 1**  —

Consider a projectile, launched with initial velocity $$v_0$$, at an angle $$\theta$$. An investigation of this motion might start with the guess that these are the relevant quantities. (de Mestre 1990)

- *quantity*   *dimensional*

*formula*

- horizontal position $$x$$   $$L^1M^0T^0$$
- vertical position $$y$$   $$L^1M^0T^0$$
- initial speed $$v_0$$   $$L^1M^0T^{-1}$$
- angle of launch $$\theta$$   $$L^0M^0T^0$$
- acceleration due to gravity $$g$$   $$L^1M^0T^{-2}$$
- time $$t$$   $$L^0M^0T^1$$

1. Show that $$\{gt/v_0,gx/v_0^2,gy/v_0^2,\theta\}$$ is a complete set of dimensionless products. (*Hint.* This can be done by finding the appropriate free variables in the linear system that arises, but there is a shortcut that uses the properties of a basis.)
2. These two equations of motion for projectiles are familiar: $$x=v_0\cos(\theta) t$$ and $$y=v_0\sin(\theta) t- (g/2)t^2$$. Manipulate each to rewrite it as a relationship among the dimensionless products of the prior item.

**Problem 2**  — Einstein (Einstein 1911) conjectured that the infrared characteristic frequencies of a solid may be determined by the same forces between atoms as determine the solid's ordanary elastic behavior. The relevant quantities are

- *quantity*   *dimensional*

*formula*

- characteristic frequency $$\nu$$   $$L^0M^0T^{-1}$$
- compressibility $$k$$   $$L^1M^{-1}T^2$$
- number of atoms per cubic cm $$N$$   $$L^{-3}M^0T^0$$
- mass of an atom $$m$$   $$L^0M^1T^0$$

Show that there is one dimensionless product. Conclude that, in any complete relationship among quantities with these dimensional formulas, $$k$$ is a constant times $$\nu^{-2}N^{-1/3}m^{-1}$$. This conclusion played an important role in the early study of quantum phenomena.

**Problem 3**  —

The torque produced by an engine has dimensional formula $$L^2M^1T^{-2}$$. We may first guess that it depends on the engine's rotation rate (with dimensional formula $$L^0M^0T^{-1}$$), and the volume of air displaced (with dimensional formula $$L^3M^0T^0$$) (Giordano, Wells & Wilde 1987).

1. Try to find a complete set of dimensionless products. What goes wrong?
2. Adjust the guess by adding the density of the air (with dimensional formula $$L^{-3}M^1T^0$$). Now find a complete set of dimensionless products.

**Problem 4**  —

Dominoes falling make a wave. We may conjecture that the wave speed $$v$$ depends on the spacing $$d$$ between the dominoes, the height $$h$$ of each domino, and the acceleration due to gravity $$g$$. *(Tilley)*

1. Find the dimensional formula for each of the four quantities.
2. Show that $$\{\Pi_1=h/d,\Pi_2=dg/v^2\}$$ is a complete set of dimensionless products.
3. Show that if $$h/d$$ is fixed then the propagation speed is proportional to the square root of $$d$$.

**Problem 5**  —

Prove that the dimensionless products form a vector space under the $$\vec{+}$$ operation of multiplying two such products and the $$\vec{\cdot}$$ operation of raising such the product to the power of the scalar. (The vector arrows are a precaution against confusion.) That is, prove that, for any particular homogeneous system, this set of products of powers of $$m_1$$, ..., $$m_k$$

$$
\{m_1^{p_1}\dots m_k^{p_k} \,\big|\, p_1, \ldots, p_k \text{ satisfy the system}\}
$$

is a vector space under:

$$
m_1^{p_1}\dots m_k^{p_k}\vec{+}m_1^{q_1}\dots m_k^{q_k}=m_1^{p_1+q_1}\dots m_k^{p_k+q_k}
$$

and

$$
r\vec{\cdot} (m_1^{p_1}\dots m_k^{p_k})= m_1^{rp_1}\dots m_k^{rp_k}
$$

(assume that all variables represent real numbers).

**Problem 6**  —

The advice about apples and oranges is not right. Consider the familiar equations for a circle $$C=2\pi r$$ and $$A=\pi r^2$$.

1. Check that $$C$$ and $$A$$ have different dimensional formulas.
2. Produce an equation that is not dimensionally homogeneous (i.e., it adds apples and oranges) but is nonetheless true of any circle.
3. The prior item asks for an equation that is complete but not dimensionally homogeneous. Produce an equation that is dimensionally homogeneous but not complete.

(Just because the old saying isn't strictly right, doesn't keep it from being a useful strategy. Dimensional homogeneity is often used as a check on the plausibility of equations used in models. For an argument that any complete equation can easily be made dimensionally homogeneous, see (Bridgman 1931, Chapter I, especially page 15.)

Solutions

### References

- Bridgman, P. W. (1931), *Dimensional Analysis*, Yale University Press.
- de Mestre, Neville (1990), *The Mathematics of Projectiles in sport*, Cambridge University Press.
- Giordano, R.; Jaye, M.; Weir, M. (1986), "The Use of Dimensional Analysis in Mathematical Modeling", *UMAP Modules* (632), COMAP.
- Giordano, R.; Wells, M.; Wilde, C. (1987), "Dimensional Analysis", *UMAP Modules* (526), COMAP.
- Einstein, A. (1911), "Elementare Betrachtungen über die thermische Molekularbewegung in festen Körpern", *Annals of Physics*, **35**: 686.
- Tilley, Burt, *Private Communication*.

---

*Source: Wikibooks, Linear Algebra/Topic: Dimensional Analysis (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Dimensional_Analysis), by Wikibooks contributors, CC BY-SA 4.0.*
