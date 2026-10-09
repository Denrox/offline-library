# Aluminum vs copper antenna element lengths

*Tags: antenna, antenna-theory, antenna-construction · score 10*

## Question

Does the particular metal used in antenna elements make any difference in element length or spacing, i.e. 1/2" aluminum tube vs 1/2" copper tube?

I know that length and diameter have an effect on resonance and impedance, but does the particular metal?

My question is specifically about element length vs type of metal element.

## Accepted answer (score 4, by user10489)

Changing the metal in an antenna is equivalent to changing the diameter of the elements, but most metals used for antennas are so close in conductivity that the equivalent diameter change is negligible for most antenna models.

## Answer (score 8, by Glenn W9IQ)

Besides mechanical differences, the primary difference between aluminum and copper in antenna construction is RF resistance. Copper will have slightly less RF resistance for the same surface area. Increasing the surface area slightly allows aluminum to exhibit the same RF resistance as copper.

RF resistance is unique due to the tendency of the RF current to crowd around the surface of the conductor. As the frequency is increased, the RF current crowds even more toward the surface, occupying an increasingly thinner layer of the metal. Because of this effect the surface area of the conductor becomes a dominant factor in determining the RF resistance and conductors can be hollow tubes since no appreciable current would flow in the core.

But specifically to your question, RF resistance has no appreciable effect on resonance or element spacing. It will potentially impact antenna efficiency and gain. This is critical in certain classes of antennas such as small loop antennas where the radiation resistance is quite low.

With typical antennas such as a yagi, the difference in efficiency and gain due to RF resistance differences between aluminum and copper will most likely be neglible. If you are concerned about your specific case, provide more details regarding the type of antenna and the intended frequency range of operation.

## Answer (score 4, by jan)

Leif SM5BSZ has made investigations on the matter by measuring Q of antenna elements in an enclosed box. Look at the fastening methods to the boom that change Q drastically, especially with iron involved.

The influence of resistivity to an actual antenna depends on grade of directivity optimization, the theoretical Q = bandwith / center frequency of the antenna.

For normal low Q antennas, like a dipole or ground plane antenna, the influence have negligble effect of performance.

See it from the source here:

Losses in yagi antenna elements at 413 MHz (sm5bsz.com)

Excerpt:

There are several mechanisms by which element losses may increase above the values computed by the modelling software.

- Reduced surface conductivity due to corrosion.
- Ohmic losses due to Eddy currents in the boom tube or other conducting materials near the element center.
- Magnetic losses in washers, screws and other magnetic materials near the element center.
- Dielectric losses in surface coatings used to prevent corrosion.
- Dielectric losses in plastic plugs at the element tips.

Losses in yagi antenna elements at 144 MHz (sm5bsz.com)

Excerpt:

At VHF frequencies element losses are much less important than they are at UHF frequencies because system noise temperatures are not much lower than the environmental temperature and therefore element losses only affect antenna gain, not the system noise temperature for the receiver even when the antenna points into cold sky.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9451/aluminum-vs-copper-antenna-element-lengths, by David Thorpe, user10489, Glenn W9IQ, jan. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
