# Why is the insertion loss of my coax cable higher than expected?

*Tags: coaxial-cable, measurement · score 4*

## Question

I am testing a long cable run (about 90m). This cable has been used outside and inside, for temporary setups.

I've set up my VNA with the correct values (velocity factor,...) and the distance to fault is correct when I just connect one side to the RF out connector (S11). I don't see any obvious impedance bumps when looking at the DTF measurement. DC resistance of the center conductor and shield is according to the manufacturer specifications for that length. There is no (measurable) DC loss between shield and center. Capacitance is defined at 56pF/m, I measured 5.82nF which seems to correct. So all seems allright.

However, the datasheet specifies 25.8dB loss per 100m at 1Ghz, but I am measuring 43dB loss (S21).

I am wondering if this could be caused by:

- possible moisture in the foam PE dielectric
- other reasons?

Anything I might be missing? Any other tests I could perform?

## Accepted answer (score 5, by Glenn W9IQ)

Based on your description, I would suspect moisture damage.

Moisture ingress in coax cables typically results in the corrosion of the copper braided wires in the shield. The oxide that forms increases the RF losses of the shield. A simple resistive test of the shield is not usually sufficient to detect this condition. If the center conductor is multi-stranded, a similar oxide problem can result.

Moisture ingress in coaxial cable left exposed to weather often occurs at the ends the cable but micro cracking in the outer jacket, animal damage, an abraded jacket, etc. are also common causes of ingress. Cable that is partially subterranean and not fully sealed can pull in moisture due to differential diurnal heating and cooling.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10464/why-is-the-insertion-loss-of-my-coax-cable-higher-than-expected, by Dieter Vansteenwegen, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
