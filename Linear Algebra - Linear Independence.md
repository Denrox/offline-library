# Linear Independence

The prior section shows that a vector space can be understood as an unrestricted linear combination of some of its elements— that is, as a span. For example, the space of linear polynomials $$\{a+bx\,\big|\, a,b\in\mathbb{R}\}$$ is spanned by the set $$\{1,x\}$$. The prior section also showed that a space can have many sets that span it. The space of linear polynomials is also spanned by $$\{1,2x\}$$ and $$\{1,x,2x\}$$.

At the end of that section we described some spanning sets as "minimal", but we never precisely defined that word. We could take "minimal" to mean one of two things. We could mean that a spanning set is minimal if it contains the smallest number of members of any set with the same span. With this meaning $$\{1,x,2x\}$$ is not minimal because it has one member more than the other two. Or we could mean that a spanning set is minimal when it has no elements that can be removed without changing the span. Under this meaning $$\{1,x,2x\}$$ is not minimal because removing the $$2x$$ and getting $$\{1,x\}$$ leaves the span unchanged.

The first sense of minimality appears to be a global requirement, in that to check if a spanning set is minimal we seemingly must look at all the spanning sets of a subspace and find one with the least number of elements. The second sense of minimality is local in that we need to look only at the set under discussion and consider the span with and without various elements. For instance, using the second sense, we could compare the span of $$\{1,x,2x\}$$ with the span of $$\{1,x\}$$ and note that the $$2x$$ is a "repeat" in that its removal doesn't shrink the span.

In this section we will use the second sense of "minimal spanning set" because of this technical convenience. However, the most important result of this book is that the two senses coincide; we will prove that in the section after this one.

---

*Source: Wikibooks, Linear Algebra/Linear Independence (https://en.wikibooks.org/wiki/Linear_Algebra/Linear_Independence), by Wikibooks contributors, CC BY-SA 4.0.*
