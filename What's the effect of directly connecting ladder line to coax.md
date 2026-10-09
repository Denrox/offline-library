# What's the effect of directly connecting ladder line to coax?

*Tags: antenna · score 5*

## Question

I was watching a video where ladder line (450-ohm) was directly connected to coax (50-ohm) without a matching transformer.

**Mating your Coax to Ladder Line**

Wouldn't this mismatch make it impossible to achieve a 1:1 ratio back in the shack? What am I missing here? TNX Dax

## Accepted answer (score 3, by Andrew)

Connecting ladder line directly to coax normally is not a good idea, for the following reasons.

1.

There will be an impedance mismatch at the junction between the two, for receive this will result in reflections from the join back towards the antenna, for transmit there will be reflections back from the join to the transmitter. The mismatch will result in loss of performance of the system.

2.

Because of the impedance mismatch, for transmit the SWR will bad. If the antenna was matched when using just 50 ohm coax, adding the ladder line between the 50 ohm coax and the antenna will make the SWR jump to about 9:1 depending on the length of the ladder line.

3.

Coax is an unbalanced transmission line with an earth and center (live) conductor, whereas ladder line is balanced with two identical conductors. At the junction, for transmit, the RF current from the transmitter traveling on the inside of the coax, when it reaches the join, will split up between the outside of the coax and the ladder line conductor. This will cause RF current to flow on the outside of the coax and result in the coax becoming part of the radiating component of the system.

There are instances where different impedance transmission lines are connected together to work as an impedance transformer, but when this is done the lines have to be of the same type, connecting unbalanced to balanced doesn't work properly.

Having said all that, there may be special types of antenna where the ladder line is used as part of the antenna matching system, as mentioned by Nate.

Hope that helps !

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20759/what-s-the-effect-of-directly-connecting-ladder-line-to-coax, by Dax, Andrew. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
