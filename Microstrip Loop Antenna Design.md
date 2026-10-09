# Microstrip Loop Antenna Design

*Tags: antenna, antenna-theory, antenna-construction · score 3*

## Question

I am trying to design a loop antenna for operation at 2.4 GHz, I would like for it to have above 2.5 dB gain at 2.4 GHz and have relatively good return loss (<-10 dB).

I have started my design as shown in the pictures. I am concerned with the radiation pattern cut at phi=90 degrees:

I feel as though this plane cut should be circular in shape. Is there any way I can adjust the antenna to produce the desired radiation pattern?

## Answer (score 3, by Glenn W9IQ)

By nature, the radiation pattern of a small loop antenna will not be uniform in the azimuth. It will typically have the classic bipolar lobe pattern with nulls in the quadrature positions as shown in your plots.

You should either consider classes of antennas that are omnidirectional in the azimuth (e.g. monopoles, vertical dipoles, horizontal slot, etc.) or phase two loops that are oriented 90 degrees from one another. In the latter case, the pattern will be pseudo omni in the azimuth and the solution will likely require two PCBs and an interconnecting transmission line.

You state that you require 2.5 dB gain. Note that this is an ambiguous statement since there is no normative reference. It should likely be stated as either dBi or dBd gain. In professional circles, dBi is used almost exclusively but it still should be explicitly stated.

Note that you also specified an RL without stating the ZO  of the transmission line, the output impedance of the transmitter, or the input impedance of the receiver. All of which are essential facts in order to engineer a solution that fully meets the requirement.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10174/microstrip-loop-antenna-design, by amantonas, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
