# Loop Antenna - configuration?

*Tags: antenna, antenna-theory, magnetic-loop, small-loop · score 3*

## Question

Due to space limitations, I'm looking at loop antenna designs. I'm starting with receive only, but hope to eventually transmit.

I've seen magnetic loops (single turn with a coupled loop) and I'm wondering: how would a second turn impact performance?

"*Coupled loops are typically 1/5 to 1/3 of main loop in size*" I'm talking about a second loop, about 1/3 the size of the main loop. Not central, but arranged like the circles on a Smith chart. Would the increased coupling help performance?

**Note:** I'm aware just about any wire can act as a receive antenna. I could probably build this and receive quite happily on it. My concern is more for performance when I eventually trey to transmit.

## Accepted answer (score 4, by Glenn W9IQ)

Adding a smaller coupled loop will have a marginal result. The smaller, coupled loop seen on some small loop designs is there to provide impedance matching. If you wish to improve the gain of your loop antenna, consider adding a second turn to the main loop.

Adding an additional turn to a small loop antenna will improve its gain. But the increase in gain to due to increased radiation efficiency, not increased directivity. Recall that gain is directivity times radiation efficiency.

The radiation resistance of a small loop antenna is normally very low and is the largest factor in its inefficiency. The radiation resistance of a small loop goes up by the number of turns squared. So by going from one turn to two turns, you have multiplied the radiation resistance by four. That is very helpful in improving its efficiency.

But there is a downside as well. Each turn has a loss based on its RF resistance. But this loss goes up linearly with the number of turns. So doubling the number of turns doubles the resistive, dissipative loss.

Since in a typical small loop antenna the loss resistance is much greater than the radiation resistance then the radiation efficiency (power radiated vs power applied) improvement approaches the number of turns. So a second, properly spaced turn has the potential to double the radiation efficiency and thus the gain of a small loop. As the number of turns are increased, the succesive gain in radiation efficiency starts to decline so this approximation should not be extended for additional turns.

Keep in mind, however, that the maximum directivity of a small loop is ~1.5. So if the loop has an ideal radiation efficiency of 1 (zero losses), the maximum possible gain is 1.76 dBi regardless of the number of turns.

## Answer (score 3, by Mike Waters)

Larger multi-turn loops with the turns too close together can be degraded by the "proximity effect": the turn in the front (or in the case of a spiral, the outermost turn) may have a certain current value at a given point on that turn; but the turn adjacent to it *next to that point* may have a current that is quite different. This can cause (among other things) increased current in a given area. You can spread the turns out to reduce this effect, but the bottom line is that losses can be much higher than in single-turn loops.

Here's what Owen Duffy states:

Small Transmitting Loops (STL) are loops of less than about 0.1λ in diameter or about 0.3λ in circumference. Below these limits, the current around the loop is almost uniform and this permits a simplified analysis.

According to this, the total length of the conductor in a multiturn loop should be less than about 0.3λ depending on how close the turns are to each other.

IIRC, the two-turn loop in the 11/11 *QST* actually had significantly more loss than the single-turn one. Here are the files.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9013/loop-antenna-configuration, by Alan Campbell, Glenn W9IQ, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
