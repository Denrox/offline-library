# For air coax calculation, what is correct diameter metric vis-à-vis tube stock thickness?

*Tags: diy, impedance, coaxial-cable, transmission-line · score 5*

## Question

I am interested in creating a square outer-conductor with round inner-conductor air coax post for a hex beam antenna. I found the extremely useful information at:

[How do I design a round or square coaxial transmission line to have a specific impedance?](How%20do%20I%20design%20a%20round%20or%20square%20coaxial%20transmission%20line%20to%20have%20a%20specific%20impedance.md)

and

http://fermi.la.asu.edu/w9cf/articles/square/square.html

However, from a practical standpoint, in these explanations it is not clear to me what is the most appropriate measurement to use for the square outer conductor's single-side diameter. For example, if I use 2" x 2" x 0.125" square tube for construction of the air-coax, for the calculations should I use the outer 2" diameter, the inner 1.85" diameter, or the 1.925" average diameter?

## Accepted answer (score 4, by Glenn W9IQ)

Coaxial cable impedance is determined by the dialectric between the two conductors and the distance between the faces of the conductors. So normally it is the outer diameter of the inner conductor and the inner diameter of the outer conductor.

The facing surfaces being a controlling factor is due to the skin and proximity effects that tend to keep the current on the skin of the conductor and on the surfaces (skins) that are closest to each other.

The thickness of the tubes will probably not be a factor other than for mechanical and geometry factors. Normally though, you should have 4 to 5 skin depths for the lowest frequency in the application. This is in addition to the inner conductor having a sufficiently large enough diameter so as to minimize RF resistance at the highest frequency of application.

Kevin Schmidt's formula for the characteristic impedance of coax made with a square outer conductor and a round inner conductor is:

$$Z_o=138\log_{10}(1.08D/a) \tag 1$$

where $D$ is the inside dimension of one side of the square tube and $a$ is the outside diameter of the inner round conductor.

Note that the square tube dimension, $D$, is the inside of one side of the tube or equivalently, the outside dimension of one side of the tube minus the wall thickness times two.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10437/for-air-coax-calculation-what-is-correct-diameter-metric-vis-a-vis-tube-stock-, by photosynthesis, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
