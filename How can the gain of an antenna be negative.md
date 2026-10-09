# How can the gain of an antenna be negative?

*Tags: antenna · score 3*

## Question

Aaronia released this ultra-wide-range antenna, that can measure up to 35GHz. This was really impressive for only 3000 Euros, so I was considering purchasing it, when I figured I would look at the spec sheet to compare it with their previous model. And that's when I realized that, above ~23GHz, the antenna's gain is all negative!  
Does this mean that when I point the antenna toward the source of the signal, then the reading would actually decrease?

## Answer (score 4, by Digiproc)

The vertical axis is in dB, which indicates a ratio. The literature probably mentions that it's the ratio of the antenna's gain to that of an isotropic antenna, or a dipole for the frequency in question (i.e. which is 2.15dB more). So a negative dB means the gain is less than that of a dipole or isotropic antenna. As far as directionality goes, I'd say this is the gain at the boresight. Again, the literature should make this clear.

EDIT: corrected gain of dipole to 2.15dB

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13059/how-can-the-gain-of-an-antenna-be-negative, by Alex, Digiproc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
