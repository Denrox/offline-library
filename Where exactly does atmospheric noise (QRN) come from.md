# Where exactly does atmospheric noise (QRN) come from?

*Tags: reception, qrn · score 7*

## Question

Where does the noise I can hear on my 28 MHz receiver come from? I'm not talking about the inherent noise produced by the internal circuitry of the radio, I mean the noise received by the antenna. It's always there, no matter where I am, even if I am in the middle of nowhere and there are no nearby noise sources. If it were noise from outer space, then it would be blocked by the ionosphere when there are skip conditions, but when there is skip the noise is still there. Is it dead people?

## Accepted answer (score 5, by jluu)

Atmospheric noise does not go as high as 28MHz, it becomes less dominant above 10MHz, see figure: https://en.wikipedia.org/wiki/Atmospheric_noise

At 28MHz it is the thermal noise of the earth, either directly picked by the antenna or coming from further and reflected. Thermal noise formula: https://en.wikipedia.org/wiki/Noise_temperature

At 28MHz most of the noise may be man made, mainly from switching power supplies, mainly from led lights.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18176/where-exactly-does-atmospheric-noise-qrn-come-from, by Andrew, jluu. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
