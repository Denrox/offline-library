# Cross Yagi Antenna Design

*Tags: antenna, antenna-construction · score 4*

## Question

What will be the effect if I add the insulation between elements and metallic boom of the cross yagi antenna (where elements from outside of the boom, instead of through boom) and in this case boom correction is required? If this is not the best way, feel free to suggest another methods for connecting the elements and metallic Boom.

## Accepted answer (score 2, by Edwin van Mierlo)

"*But I want to get know what happen when the elements of the antenna are from outside and insulated from the metallic boom*"

The characteristics of your antenna will change:

- R component of Z at f will change
- X component of Z at f will change
- VSWR at f will change
- Antenna Resonance f(r) (where X~~0) will change
- directivity/gain-plots, -3dB angles, will change
- front/back ratio will change

How much all this is changing is cannot be determined unless a lot of very precise detail is documented, and complex simulations are ran.

Even then these would be simulations, as the real numbers are actually dependent on the mounting, height, and other environmental factors.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5028/cross-yagi-antenna-design, by 0x47-sci-tech, Edwin van Mierlo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
