# What should be the modulation when transmitting APRS signal?

*Tags: modes, aprs · score 7*

## Question

Is it SSB or NFM or other type of modulation?

## Accepted answer (score 9, by WPrecht)

APRS is a data transmission protocol and is independent of the underlying connection details. So there is no required modulation for the protocol.

That said, the common implementation of APRS is FM modulated 1200 baud AFSK in the 2m band. Several major vendors like Yaesu and Kenwood support the protocol with built in functionality for APRS.

There have also been implementations of the APRS protocol over AX.25 and PSK31 on HF frequencies as well.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1645/what-should-be-the-modulation-when-transmitting-aprs-signal, by Harold Chan, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
