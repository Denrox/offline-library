# Automation

This is a PASCAL routine to do $$k\rho_i+\rho_j$$ to an augmented matrix.

```
PROCEDURE Pivot(VAR LinSys : AugMat;
k : REAL;
i, j : INTEGER)
VAR
Col : INTEGER;
BEGIN
FOR Col:=1 TO NumVars+1 DO
LinSys[j,Col]:=k*LinSys[i,Col]+LinSys[j,Col];
END;

```

Of course this is only one part of a whole program, but it makes the point that Gaussian reduction is ideal for computer coding.

There are pitfalls, however. For example, some arise from the computer's use of finite-precision approximations of real numbers.

These systems provide a simple example.

(The second two lines are hard to tell apart.) Both have $$(1,1)$$ as their unique solution.

In the first system, some small change in the numbers will produce only a small change in the solution:  

$$
\begin{array}{rcrcr} x &+ &2y &= &3 \\ 3x &- &2y &= &1.008 \end{array}
$$

gives a solution of $$(1.002,0.999)$$. Geometrically, changing one of the lines by a small amount does not change the intersection point by very much.

That's not true for the second system. A small change in the coefficients  

$$
\begin{array}{rcrcr} x &+ &2y &= &3 \\ 1.000\,000\,01x &+ &2y &= &3.000\,000\,03 \end{array}
$$

leads to a completely different answer: $$(3,0)$$.

The solution of the second example varies wildly, depending on a $$9$$-th digit. That's bad news for a machine using $$8$$ digits to represent reals. In short, systems that are nearly singular may be hard to compute with.

Another thing that can go wrong is error propagation. In a system with a large number of equations (say, 100 or more), small rounding errors early in the procedure can snowball to overwhelm the solution at the end.

These issues, and many others like them, are outside the scope of this book, but remember that just because Gauss' method always works in theory and just because a program correctly implements that method and just because the answer appears on green-bar paper, doesn't mean that answer is right. In practice, always use a package where experts have worked hard to counter what can go wrong.

---

*Source: Wikibooks, Linear Algebra/Automation (https://en.wikibooks.org/wiki/Linear_Algebra/Automation), by Wikibooks contributors, CC BY-SA 4.0.*
