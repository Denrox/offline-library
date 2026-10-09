# Low power long distance wireless data communication

*Tags: digital-modes, receiver, transmitter, europe · score 4*

## Question

I am looking for a communication solution with the following requirements:

- wireless
- unidirectional, point to point
- low power (li-ion battery powered, should operate at least one hour on the single charge)
- low baudrate data transfer (cca 40 - 80 bauds)
- long distance, in the terrain covered by the forest, behind the small hill. One km sholud be enough but more is better
- using free band within EU

What technologies should I check? Are there any existing modules for this? I would like to connect it to Arduino.

## Answer (score 2, by captcha)

RFM12B or RFM69CW sounds like what you want. Operates in the ISM band. There's sketches available for Arduino and with a decent yagi antenna you should be able to reach that far.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5554/low-power-long-distance-wireless-data-communication, by Martin Ždila, captcha. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
