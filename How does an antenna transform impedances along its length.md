# How does an antenna transform impedances along its length?

*Tags: antenna, impedance, theory, measurement · score 12*

## Question

If I insert some impedance (like a loading coil, or a trap) at the base of a monopole antenna, the effect on the feedpoint impedance is easy to predict: the impedance is in series with the antenna, so whatever the feedpoint impedance was, the added impedance (Z) is added to it. See ANT1:

But what happens as that impedance is moved away from the feedpoint, as in ANT2? The impedance is still in series with the antenna, but must be subject to some impedance transformation as seen by the feedpoint.

How can we characterize this impedance transformation? Can we put some math to it?

## Answer (score 3, by Glenn W9IQ)

The impedance along the length of the antenna is a function of the standing wave developed on the antenna. If we assume no ground losses and ignore the self capacitance at the tip of the antenna, then the following description can be applied to a monopole antenna <=1/4λ long.

The transmitter induces a voltage at the feed point of the antenna that causes current, as a function of the surge impedance of the antenna feed point, to flow. The current and voltage travel along the length of the antenna until reaching its tip. The tip of the antenna represents an impedance discontinuity near zero ohms that causes a reflected wave.

Following the notion of an open-ended transmission line, the current changes phase by 180 degrees as it is reflected while the voltage is reflected in phase. As the reflected waves meet the incident waves, the vector sum of each is produced along the length of the antenna giving rise the standing wave pattern. Once the reflected waves have reached the feed point, the conditions of varying impedance along the entire length of the antenna are now established as well as the input impedance at the feed point of the antenna.

Upon steady state conditions, the input impedance of the antenna establishes the RMS input current (I) at the feed point. The power applied to the antenna is calculated as I|Z|. It is also known that the pattern of the current on the vertical element of a monopole antenna with an electrical length <= 1/4λ can be modeled as sinusoidal with near zero current at the tip and reaching maximum current at the feed point. The impedance magnitude at any point along the antenna can therefore be approximated as:

|Z| = PFP/(IFPsin θ)

where θ is the electrical degrees from the tip, PFP is the transmitter power at the feed point, and IFP is the RMS current at the feed point. Due to real world effects excluded in the opening paragraph, this can only serve as a first approximation.

The insertion of any inductance or capacitance represents another impedance discontinuity along the length of the antenna. As such, it too will generate reflections and attendant phase shifts that alter the impedance of the feed point. The relative phase of the insertion point (for a given component) is the cause of the variation of input impedance as the position is changed. Careful modeling of all of the complex reflection coefficients and positions along the length of the antenna will allow the development of a nearly complete formula of the input impedance of the antenna.

## Answer (score 3, by AllYourBaseAreBelongToUs)

Think of the antenna as a whole as being many inductors in series along its length and along with that many capacitors branching off like a tree (capacitors in the air) going back to the "negative side", so parallel capacitors. The loading coil needs actual current to work with, the further up on the antenna that you mount it, the less current there is and the less effective the coil becomes. A loading coil placed at the tip would do nothing since there is no current left at this point.

To model this, I would use 2 series inductors for the antenna (the center point is where you insert your loading coil) and you have 2 parallel capacitors. Going from connector to tip of antenna it will be inductor capacitor inductor capacitor.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3606/how-does-an-antenna-transform-impedances-along-its-length, by Phil Frost - W8II, Glenn W9IQ, AllYourBaseAreBelongToUs. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
