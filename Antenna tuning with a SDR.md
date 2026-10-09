# Antenna tuning with a SDR

*Tags: antenna, software-defined-radio, antenna-tuner · score 3*

## Question

Was thinking about tuning my PCB trace / helical ISM bands antenna inside a device I am building by continuously emitting CW and looking at received dB level in GQRX or any other software; then swap inductors / capacitors until I find the sweet spot. Could this work ?

## Accepted answer (score 0, by jpa)

Tuning based on signal strength will work to an extent.

The problem is that the search space is two-dimensional, so it can take a lot of trial and error to find good values for the components:

- At each point, you have four choices: increase/decrease capacitance/inductance, and the size of the change.
- If you make a too large change at a time, you may overshoot the optimal point.
- If you make tiny changes, other effects such as surroundings and radio noise may obscure the results.

You can compare this with antenna matching using Smith chart. The perfect match is at the center and the lines you can follow are curved. For example, at one point it can seem that adding capacitance helps, but then you notice you need more inductance, and then it turns out you didn't need that much capacitance.

(Image credit: from page linked above)

For high power transmitters a further complication would be that the transmitter could be damaged if the reflected power is too high. Small transmitters usually aren't damaged even by 100% reflection.

## Answer (score 3, by Ryuji AB1WX)

Maybe, maybe not. You'll probably observe the level fluctuating for unrelated factors like your arms moving or other perturbations, and it'll be difficult to determine what's optimal unless the options you are comparing are drastically different.

For small power non-critical applications, it doesn't really matter whether SWR is 1 or 1.5 or 2 or even higher. At SWR of 2, you have a mismatch loss of 0.25dB. At 3, 1.25dB. At 4, 2dB. So, the receiver's signal level will be too coarse yet sensitive to environmental fluctuations to optimize for the SWR or the mismatch loss.

Of course, this is very different if you are transmitting some significant power because of the stress, dissipation, and voltage swings on the amplifier, which will be a problem.

So, the short answer is, most likely, no, pretty much on the practical ground.

Historically, before tandem bridges and other forms of directional couplers were introduced to amateur radio in the 1950s or 60s, it was common to tune the final amp plate matching network by monitoring the transmitted field strength, usually in addition to a light bulb or a meter. That was good enough for amateur work back then. But that was HF and tube amps. I wouldn't do that in UHF or higher unless you can set up a radio anechoic chamber or some other very stable setup.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23331/antenna-tuning-with-a-sdr, by kellogs, jpa, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
