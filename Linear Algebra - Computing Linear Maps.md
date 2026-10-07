# Computing Linear Maps

The prior section shows that a linear map is determined by its action on a basis. In fact, the equation

$$
h(\vec{v}) =h(c_1\cdot\vec{\beta}_1+\dots+c_n\cdot\vec{\beta}_n) =c_1\cdot h(\vec{\beta}_1)+\dots +c_n\cdot h(\vec{\beta}_n)
$$

shows that, if we know the value of the map on the vectors in a basis, then we can compute the value of the map on any vector $$\vec{v}$$ at all. We just need to find the $$c$$'s to express $$\vec{v}$$ with respect to the basis.

This section gives the scheme that computes, from the representation of a vector in the domain $${\rm Rep}_{B}(\vec{v})$$, the representation of that vector's image in the codomain $${\rm Rep}_{D}(h(\vec{v}))$$, using the representations of $$h(\vec{\beta}_1)$$, ..., $$h(\vec{\beta}_n)$$.

---

*Source: Wikibooks, Linear Algebra/Computing Linear Maps (https://en.wikibooks.org/wiki/Linear_Algebra/Computing_Linear_Maps), by Wikibooks contributors, CC BY-SA 4.0.*
