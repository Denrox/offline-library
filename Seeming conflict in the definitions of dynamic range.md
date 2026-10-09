# Seeming conflict in the definitions of dynamic range

*Tags: receiver, measurement, superheterodyne, dynamic-range · score 3*

## Question

As I understand it, dynamic range is the difference in dB between the strongest and weakest signal discernible by your receiver. So, the larger the dynamic range, the better, which seems intuitive.

However, calculating reciprocal mixing dynamic range (RMDR - dynamic range determined by the calculation of reciprocal mixing, distance in dB where the two lines cross the noise floor) shows that the closer the slope of the third-order intercept (IP3) line is to that of the ideal line for receiver amplifier compression, the smaller the dynamic range, and you want the IP3 line slope to be as close to the ideal as possible, which seems to minimize the dynamic range, which in turn seems to conflict with the original definition for dynamic range.

What am I missing, since there seems to be a conflict here?

## Accepted answer (score 2, by Glenn W9IQ)

While the two terms in question share the phrase "dynamic range", they are in fact, quite different metrics from one another. Therefore there is no reason to assume any type of conflict or contradiction.

The basic receiver dynamic range is a measure of a receiver's ability to handle a wide range of signal strengths - from the very weakest (typically at the receiver's MDS - Minimum Discernible Signal) to the strongest. Several factors come into play that determine the receiver's dynamic range such as phase noise, noise figure, 2nd and 3rd order intercepts, 1 dB compression point, etc.

The receiver RMDR - Reciprocal Mixing Dynamic Range became significant with the application of frequency synthesizers as the LO (local oscillator) in the superhetrodyne receiver. These synthesizers tend to have phase noise on the skirts of their envelope. Under the right conditions, a signal that is otherwise out of the passband of the IF chain can mix with this undesired LO phase noise to generate interference within the IF passband and thus interfere with desired signals in the passband. Lowering the LO skirt phase noise will improve the RMDR.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9530/seeming-conflict-in-the-definitions-of-dynamic-range, by Noji, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
