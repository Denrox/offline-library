# How the Coaxial Collinear Antenna Works?

*Tags: antenna, antenna-theory, coaxial-cable · score 3*

## Question

A length of coaxial cable radiates negligible amount of RF.  
Same length, if cut into pieces of length (λ/2 * VF), and these pieces joined again cross-connected (i.e. core of a piece to shield of adjacent piece & vice versa), then this length of coax becomes a very good radiator of RF. Why & how?

EDIT on Feb 05, 2017:  
Added sketch below to improve the question.

## Answer (score 5, by abcd567)

I am not sure, but I feel that the attached diagram explains how a Coaxial Collinear Antenna works. Suggestions/comments are welcomed.

***Click on image to see full size image***

## Answer (score 4, by Marcus Müller)

If you look at this, reduced to two segments:

```
==============x==============

```

you'll notice that the voltage on the outer conductor right of the crossover is exactly the opposite (assuming infinetly small crossover and perfect impedance matching) than on the left side.

So let's assume we simply feed the two outer conductors at that crossover point with exactly such a voltage:

```
______________-(~)+______________

```

Looking familiar? Yep, that is a classical dipole!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7076/how-the-coaxial-collinear-antenna-works, by abcd567, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
