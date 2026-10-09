# Does a larger Biquad antenna give better results?

*Tags: antenna, antenna-theory · score 4*

## Question

Consider a biquad antenna used for receiving, not for sending. They are typically built with each side having a length of $\lambda / 4$.

If a biquad antenna was built with a side length of $\lambda / 2$ or even $\lambda$, would this give better results (for receiving)? If yes, how much better?

## Accepted answer (score 3, by jcoppens)

You need some theory to answer this - it's not entirely simple.

Consider that each quad loop really consists of 2 dipoles, with the ends connected together (at the corners of the quad). So, each quad loop really acts as two dipoles located parallel to each other. (The reflected loop, in a similar way, consists of two of these 'pseudo-dipoles').

So, if you then consider what would happen if you would *extend* the dipole to double its length: Instead of one dipole (which has low impedance at its center), you'd have two dipoles, which have a very high impedance at the center - almost impossible to feed (thousands of Ohms). But it would still be possible.

What's not so interesting is that a large part of the field irradiated by the dipoles would cancel each other (because they're too close), so you would probably 'feel' a slight improvement, but not nearly what you'd expect from such an effort.

Edit: Modified the text slightly to - hopefully - make it less confusing thanks for the remark, Phil). Making use of the edit, do note that if you'd extend the sides to 3/4$\lambda$ you'd actually get 3 dipoles and low impedance. But again, the gain won't be what you'd expect, as, again, parts will cancel. Moreover, if you'd think about using the biquad as a feed for a parabola, you'd be covering a much larger part of the useful area.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1949/does-a-larger-biquad-antenna-give-better-results, by Martin, jcoppens. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
