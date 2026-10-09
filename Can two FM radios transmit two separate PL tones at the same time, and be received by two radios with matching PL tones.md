# Can two FM radios transmit two separate PL tones at the same time, and be received by two radios with matching PL tones?

*Tags: fm, tone-squelch · score 3*

## Question

Can two FM radios transmit two separate PL tones, and be received by two radios with matching PL tones? Or will the receivers hear a mix of the two, or nothing at all?

## Accepted answer (score 9, by Juancho)

Assuming that the two transmitters operate at the same carrier frequency, and that the receivers receive similar power from each transmitter, then the FM signals will suffer *destructive interference* and the demodulated signal will be heavily distorted. PL tone, which is part of the transmitted signal, will also be lost.

If one of the RF signals gets to the receiver with much more power than the other transmission, then there is FM *masking*, where the stronger signal prevails and the weaker signal is undetected.

You cannot expect to receive a nice mix of the two transmitted signals in FM.

P.S. this is why aviation VHF uses AM and not FM. In AM, all received signals add up in the demodulated audio, so you can hear all signals at once.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1797/can-two-fm-radios-transmit-two-separate-pl-tones-at-the-same-time-and-be-recei, by Evan Fosmark, Juancho. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
