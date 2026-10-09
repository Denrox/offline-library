# What is the easiest way to eliminate a beam antenna's backward radiation (rear lobe)?

*Tags: antenna, antenna-theory, yagi, radiation-pattern · score 3*

## Question

**I tried a metallic reflector which works well in terms of radiation, but considerably degrades the return loss and adds more complexity to the design.**

## Answer (score 3, by Glenn W9IQ)

No real world antenna exhibits "zero" power in any particular direction. Careful design can minimize the power in the unwanted direction but not eliminate it.

In a yagi antenna, the front to back ratio is the difference of the decibel gain of the forward, major lobe less the decibel gain of the lobe 180 degrees from the forward lobe. Thus a yagi antenna with a 20 dB front to back ratio would have 100 times less power transmitted or received in the rearward facing direction compared to the forward direction.

When designing a yagi antenna there is an unavoidable interaction between the gain of the forward lobe and the front to back ratio. If you optimize the front to back ratio, the rearward lobe is reduced but the main lobe becomes wider and has reduced gain. If you optimize the gain, you tend to reduce the front to back ratio.

For the average ham, optimizing the forward gain tends to be the desirable outcome. However, if you suffer from interference from directions other than your desired signal direction, optimizing the front to back ratio could improve your signal to noise ratio while receiving.

In reviewing the azimuth plot in the question, it appears that the design is significantly sub-optimized. The major lobe is not in the forward direction and the front to back ratio appears to be ~0.5 dB. You may find it advantageous to start with a well designed model and then experiment with single changes in order to observe the results of the change. As @MikeWaters pointed out, some modeling packages can optimize a design based on your stated preferences.

## Answer (score 2, by Phil Frost - W8II)

From the picture, it looks like you have a log-periodic antenna rather than a Yagi.

In either case, optimizing some parameter like front-to-back ratio involves optimizing the spacing and length of the elements. In the case of the log-periodic antenna this is more difficult given the broad-band nature.

Such optimization can be done by trial and error, either in modeling or empirically. Some antenna design software can automate the process.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9817/what-is-the-easiest-way-to-eliminate-a-beam-antenna-s-backward-radiation-rear-, by bibi, Glenn W9IQ, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
