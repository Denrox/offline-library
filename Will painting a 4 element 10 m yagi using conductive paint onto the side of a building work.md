# Will painting a 4 element 10 m yagi using conductive paint onto the side of a building work?

*Tags: antenna-construction · score 4*

## Question

Will painting a 4 element yagi using conductive paint onto the side of a building work?

## Accepted answer (score 3, by Marcus Müller)

ah, at 10m wavelengths, building aren't really RF transparent, but one can abstract a wall to something relatively homogenous with RF properties defined by the wall material.

(That's because the feature sizes are much smaller than the wavelength)

What's your building made of?

- If that contains steel reinforcements, or metal window panes, or cables running far, then these will effect the RF property of your paint-wall-combination far more than a bit of conductive paint.
- If, on the other hand, your building is made of wood, or a 17th century limestone wall without steel reinforcements, chances are good that it'll be something that works. But barely so: Conductive paint isn't very conductive, and your paint would be very thin, and your wall not perfectly flat (roughness below the thickness of paint!), so that this will be a very inefficient antenna. I don't think you'd do much better than a random piece of wire hung from the top of the wall down.

Aluminium foil might work way better; conductive paint is conductive, but not nearly as good as a continuous stripe of metal. Even better would be thin wires glued/nailed to that wall – you'd be surprised how good a piece of copper wire is as conductor compared to foil (and of course compared to conductive paint). Thin wires have the downside of leading to the yagi antenna being only pretty narrow in bandwidth – the combination of foil at the ends of the elements (to make them more "butterfly-y" and thus slightly wider matched) might help, but to be honest here: this is speculation and could only be realistically answered in simulation; due to the wall probably not being even nearly well-known enough geometrically and RF-wise for such a simulation to be meaningful:

You'd have to try with your specific wall.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15490/will-painting-a-4-element-10-m-yagi-using-conductive-paint-onto-the-side-of-a-, by Andrew, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
