# Comparing Set Descriptions

*This subsection is optional. Later material will not require the work here.*

### Comparing Set Descriptions

A set can be described in many different ways. Here are two different descriptions of a single set:

$$
\{\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}z\,\big|\, z\in\mathbb{R}\} \quad\text{and}\quad \{\begin{pmatrix} 2 \\ 4 \\ 6 \end{pmatrix}w\,\big|\, w\in\mathbb{R}\}.
$$

For instance, this set contains

$$
\begin{pmatrix} 5 \\ 10 \\ 15 \end{pmatrix}
$$

(take $$z=5$$ and $$w=5/2$$) but does not contain

$$
\begin{pmatrix} 4 \\ 8 \\ 11 \end{pmatrix}
$$

(the first component gives $$z=4$$ but that clashes with the third component, similarly the first component gives $$w=2$$ but the third component gives something different). Here is a third description of the same set:

$$
\{\begin{pmatrix} 3 \\ 6 \\ 9 \end{pmatrix}+\begin{pmatrix} -1 \\ -2 \\ -3 \end{pmatrix}y\,\big|\, y\in\mathbb{R}\}.
$$

We need to decide when two descriptions are describing the same set. More pragmatically stated, how can a person tell when an answer to a homework question describes the same set as the one described in the back of the book?

### Set Equality

Sets are equal if and only if they have the same members. A common way to show that two sets, $$S_1$$ and $$S_2$$, are equal is to show mutual inclusion: any member of $$S_1$$ is also in $$S_2$$, and any member of $$S_2$$ is also in $$S_1$$.

**Example 4.1**  —

To show that

$$
S_1= \{\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}c+\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}d\,\big|\, c,d\in\mathbb{R}\}
$$

equals

$$
S_2= \{\begin{pmatrix} 4 \\ 1 \\ 0 \end{pmatrix}m+\begin{pmatrix} -1 \\ -3 \\ 0 \end{pmatrix}n\,\big|\, m,n\in\mathbb{R}\}
$$

we show first that $$S_1\subseteq S_2$$ and then that $$S_2\subseteq S_1$$.

For the first half we must check that any vector from $$S_1$$ is also in $$S_2$$. We first consider two examples to use them as models for the general argument. If we make up a member of $$S_1$$ by trying $$c=1$$ and $$d=1$$, then to show that it is in $$S_2$$ we need $$m$$ and $$n$$ such that

$$
\begin{pmatrix} 4 \\ 1 \\ 0 \end{pmatrix}m +\begin{pmatrix} -1 \\ -3 \\ 0 \end{pmatrix}n =\begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix}
$$

that is, this relation holds between $$m$$ and $$n$$.

$$
\begin{array}{rcrcr} 4m &- &n &= &2 \\ 1m &- &3n &= &0 \\ & &0 &= &0 \end{array}
$$

Similarly, if we try $$c=2$$ and $$d=-1$$, then to show that the resulting member of $$S_1$$ is in $$S_2$$ we need $$m$$ and $$n$$ such that

$$
\begin{pmatrix} 4 \\ 1 \\ 0 \end{pmatrix}m +\begin{pmatrix} -1 \\ -3 \\ 0 \end{pmatrix}n =\begin{pmatrix} 3 \\ -3 \\ 0 \end{pmatrix}
$$

that is, this holds.

$$
\begin{array}{rcrcr} 4m &- &n &= &3 \\ 1m &- &3n &= &-3 \\ & &0 &= &0 \end{array}
$$

In the general case, to show that any vector from $$S_1$$ is a member of $$S_2$$ we must show that for any $$c$$ and $$d$$ there are appropriate $$m$$ and $$n$$. We follow the pattern of the examples; fix

$$
\begin{pmatrix} c+d \\ -c+d \\ 0 \end{pmatrix}\in S_1
$$

and look for $$m$$ and $$n$$ such that

$$
\begin{pmatrix} 4 \\ 1 \\ 0 \end{pmatrix}m +\begin{pmatrix} -1 \\ -3 \\ 0 \end{pmatrix}n =\begin{pmatrix} c+d \\ -c+d \\ 0 \end{pmatrix}
$$

that is, this is true.

$$
\begin{array}{rcrcr} 4m &- &n &= &c+d \\ m &- &3n &= &-c+d \\ & &0 &= &0 \end{array}
$$

Applying Gauss' method

$$
\begin{array}{rcl} \begin{array}{rcrcr} 4m &- &n &= &c+d \\ m &- &3n &= &-c+d \end{array} &\xrightarrow[]{-(1/4)\rho_1+\rho_2} &\begin{array}{rcrcr} 4m &- &n &= &c+d \\ & &-(11/4)n &= &-(5/4)c+(3/4)d \end{array} \end{array}
$$

gives $$n=(5/11)c-(3/11)d$$ and $$m=(4/11)c+(2/11)d$$. This shows that for any choice of $$c$$ and $$d$$ there are appropriate $$m$$ and $$n$$. We conclude any member of $$S_1$$ is a member of $$S_2$$ because it can be rewritten in this way:

$$
\begin{pmatrix} c+d \\ -c+d \\ 0 \end{pmatrix} =\begin{pmatrix} 4 \\ 1 \\ 0 \end{pmatrix}((4/11)c+(2/11)d)+ \begin{pmatrix} -1 \\ -3 \\ 0 \end{pmatrix}((5/11)c-(3/11)d).
$$

For the other inclusion, $$S_2\subseteq S_1$$, we want to do the opposite. We want to show that for any choice of $$m$$ and $$n$$ there are appropriate $$c$$ and $$d$$. So fix $$m$$ and $$n$$ and solve for $$c$$ and $$d$$:

$$
\begin{array}{rcl} \begin{array}{rcrcr} c &+ &d &= &4m-n \\ -c &+ &d &= &m-3n \end{array} &\xrightarrow[]{\rho_1+\rho_2} &\begin{array}{rcrcr} c &+ &d &= &4m-n \\ & &2d &= &5m-4n \end{array} \end{array}
$$

shows that $$d=(5/2)m-2n$$ and $$c=(3/2)m+n$$. Thus any vector from $$S_2$$

$$
\begin{pmatrix} 4 \\ 1 \\ 0 \end{pmatrix}m+\begin{pmatrix} -1 \\ -3 \\ 0 \end{pmatrix}n
$$

is also of the right form for $$S_1$$

$$
\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}((3/2)m+n) +\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}((5/2)m-2n).
$$

**Example 4.2**  —

Of course, sometimes sets are not equal. The method of the prior example will help us see the relationship between the two sets. These

$$
P= \{\begin{pmatrix} x+y \\ 2x \\ y \end{pmatrix}\,\big|\, x,y\in\mathbb{R}\} \quad\text{and}\quad R= \{\begin{pmatrix} m+p \\ n \\ p \end{pmatrix}\,\big|\, m,n,p\in\mathbb{R}\}
$$

are not equal sets. While $$P$$ is a subset of $$R$$, it is a proper subset of $$R$$ because $$R$$ is not a subset of $$P$$.

To see that, observe first that given a vector from $$P$$ we can express it in the form for $$R$$— if we fix $$x$$ and $$y$$, we can solve for appropriate $$m$$, $$n$$, and $$p$$:

$$
\begin{array}{rcrcrcr} m & & &+ &p &= &x+y \\ & &n & & &= &2x \\ & & & &p &= &y \end{array}
$$

shows that that any

$$
\vec{v}= \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}x+ \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}y
$$

can be expressed as a member of $$R$$ with $$m=x$$, $$n=2x$$, and $$p=y$$:

$$
\vec{v}= \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}x+ \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}2x+ \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}y.
$$

Thus $$P\subseteq R$$.

But, for the other direction, the reduction resulting from fixing $$m$$, $$n$$, and $$p$$ and looking for $$x$$ and $$y$$

$$
\begin{array}{rcl} \begin{array}{rcrcr} x &+ &y &= &m+p \\ 2x & & &= &n \\ & &y &= &p \end{array} &\xrightarrow[]{-2\rho_1+\rho_2} &\begin{array}{rcrcr} x &+ &y &= &m+p \\ & &-2y&= &-2m+n-2p \\ & &y &= &p \end{array} \\ &\xrightarrow[]{(1/2)\rho_2+\rho_3} &\begin{array}{rcrcr} x &+ &y &= &m+p \\ & &-2y&= &-2m+n-2p \\ & &0 &= &m+(1/2)n \end{array} \end{array}
$$

shows that the only vectors

$$
\begin{pmatrix} m+p \\ n \\ p \end{pmatrix}\in R
$$

representable in the form

$$
\begin{pmatrix} x+y \\ 2x \\ y \end{pmatrix}
$$

are those where $$0=m+(1/2)n$$. For instance,

$$
\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
$$

is in $$R$$ but not in $$P$$.

### Exercises

**Problem 1**  —

Decide if the vector is a member of the set.

1. $$\begin{pmatrix} 2 \\ 3 \end{pmatrix}$$, $$\{\begin{pmatrix} 1 \\ 2 \end{pmatrix}k\,\big|\, k\in\mathbb{R}\}$$
2. $$\begin{pmatrix} -3 \\ 3 \end{pmatrix}$$, $$\{\begin{pmatrix} 1 \\ -1 \end{pmatrix}k\,\big|\, k\in\mathbb{R}\}$$
3. $$\begin{pmatrix} -3 \\ 3 \\ 4 \end{pmatrix}$$, $$\{\begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}k\,\big|\, k\in\mathbb{R}\}$$
4. $$\begin{pmatrix} -3 \\ 3 \\ 4 \end{pmatrix}$$, $$\{\begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}k+\begin{pmatrix} 0 \\ 0 \\ 2 \end{pmatrix}m \,\big|\, k,m\in\mathbb{R}\}$$
5. $$\begin{pmatrix} 1 \\ 4 \\ 14 \end{pmatrix}$$, $$\{\begin{pmatrix} 2 \\ 2 \\ 5 \end{pmatrix}k+\begin{pmatrix} -1 \\ 0 \\ 2 \end{pmatrix}m \,\big|\, k,m\in\mathbb{R}\}$$
6. $$\begin{pmatrix} 1 \\ 4 \\ 6 \end{pmatrix}$$, $$\{\begin{pmatrix} 2 \\ 2 \\ 5 \end{pmatrix}k+\begin{pmatrix} -1 \\ 0 \\ 2 \end{pmatrix}m \,\big|\, k,m\in\mathbb{R}\}$$

**Problem 2**  —

Produce two descriptions of this set that are different than this one.

$$
\{\begin{pmatrix} 2 \\ -5 \end{pmatrix}k\,\big|\, k\in\mathbb{R}\}
$$

*This exercise is recommended for all readers.*

**Problem 3**  —

Show that the three descriptions given at the start of this subsection all describe the same set.  
*This exercise is recommended for all readers.*

**Problem 4**  —

Show that these sets are equal

$$
\{\begin{pmatrix} 1 \\ 4 \\ 1 \\ 1 \end{pmatrix} +\begin{pmatrix} -1 \\ 0 \\ 1 \\ 0 \end{pmatrix}z\,\big|\, z\in\mathbb{R} \} \quad\text{and}\quad \{\begin{pmatrix} 0 \\ 4 \\ 2 \\ 1 \end{pmatrix} +\begin{pmatrix} -1 \\ 0 \\ 1 \\ 0 \end{pmatrix}k\,\big|\, k\in\mathbb{R} \},
$$

and that both describe the solution set of this system.

$$
\begin{array}{rcrcrcrcr} x &- &y &+ &z &+ &w &= &-1 \\ & &y & & &- &w &= &3 \\ x & & &+ &z &+ &2w &= &4 \end{array}
$$

*This exercise is recommended for all readers.*

**Problem 5**  —

Decide if the sets are equal.

1. $$\{\begin{pmatrix} 1 \\ 2 \end{pmatrix} +\begin{pmatrix} 0 \\ 3 \end{pmatrix}t \,\big|\, t\in\mathbb{R}\}$$ and $$\{\begin{pmatrix} 1 \\ 8 \end{pmatrix} +\begin{pmatrix} 0 \\ -1 \end{pmatrix}s \,\big|\, s\in\mathbb{R}\}$$
2. $$\{\begin{pmatrix} 1 \\ 3 \\ 1 \end{pmatrix}t +\begin{pmatrix} 2 \\ 1 \\ 5 \end{pmatrix}s \,\big|\, t,s\in\mathbb{R}\}$$ and $$\{\begin{pmatrix} 4 \\ 7 \\ 7 \end{pmatrix}m +\begin{pmatrix} -4 \\ -2 \\ -10 \end{pmatrix}n \,\big|\, m,n\in\mathbb{R}\}$$
3. $$\{\begin{pmatrix} 1 \\ 2 \end{pmatrix}t \,\big|\, t\in\mathbb{R}\}$$ and $$\{\begin{pmatrix} 2 \\ 4 \end{pmatrix}m +\begin{pmatrix} 4 \\ 8 \end{pmatrix}n \,\big|\, m,n\in\mathbb{R}\}$$
4. $$\{\begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}s +\begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}t \,\big|\, s,t\in\mathbb{R}\}$$ and $$\{\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}m +\begin{pmatrix} 0 \\ 1 \\ 3 \end{pmatrix}n \,\big|\, m,n\in\mathbb{R}\}$$
5. $$\{\begin{pmatrix} 1 \\ 3 \\ 1 \end{pmatrix}t +\begin{pmatrix} 2 \\ 4 \\ 6 \end{pmatrix}s \,\big|\, t,s\in\mathbb{R}\}$$ and $$\{\begin{pmatrix} 3 \\ 7 \\ 7 \end{pmatrix}t +\begin{pmatrix} 1 \\ 3 \\ 1 \end{pmatrix}s \,\big|\, t,s\in\mathbb{R}\}$$

Solutions

### Footnotes

---

*Source: Wikibooks, Linear Algebra/Comparing Set Descriptions (https://en.wikibooks.org/wiki/Linear_Algebra/Comparing_Set_Descriptions), by Wikibooks contributors, CC BY-SA 4.0.*
