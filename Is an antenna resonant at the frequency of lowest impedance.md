# Is an antenna resonant at the frequency of lowest impedance?

*Tags: antenna-theory, impedance · score 3*

## Question

I understand that an antenna is resonant at the frequency where the capacitive and inductive reactance cancel out to 0. Only the resistive impedance remains at resonance.

Does this mean that the impedance is lowest at the frequency where only the resistive impedance remains? Can we find the resonant frequency of an antenna by looking for the lowest point on it's impedance curve?

## Accepted answer (score 3, by Andrew)

Marcin, as you have alluded to, an antenna is resonant when there is no reactance present in the impedance seen at the feed point for the frequency you are using. There is no reactance because at resonance the antenna voltage and current are in phase, not because the inductive and capacitive reactances cancel out. When the antenna is not resonant, the voltage and current are not in phase which results in the impedance containing some reactance.

Assuming you are not changing the antenna or it's feed point and you are changing the frequency, the frequency at which the impedance has the lowest resistance (ignoring if there is any reactance present) does not however always match up with resonance.

The value of the resistive or real part of the impedance does not determine whether or not the antenna is resonant. At resonance there is no reactance, not least resistance.

## Answer (score 4, by Richard Fry)

A point to remember here is: A transmit antenna does not need to be **self**-resonant at the operating frequency to be a very efficient radiator of e-m energy.

A matching network at the antenna input terminals may be used to match the impedance of that antenna (including its non-zero reactive term) to the impedance of the transmission line connected there.

Such antenna *systems* are commonly used by medium-wave AM broadcast stations, and may radiate >95% of the r-f energy at the input of their matching network(s).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15659/is-an-antenna-resonant-at-the-frequency-of-lowest-impedance, by marcin42, Andrew, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
