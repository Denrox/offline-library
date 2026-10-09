# AM Radio Envelope Dectector

*Tags: am · score 4*

## Question

How do you choose the values of the capacitor and the resistor in an envelope detector circuit? In my case, the frequency range is from 20 Hz to 20,000 Hz. Also, am I correct in understanding that usually Schottky diodes are used in the circuit instead of other types of diodes because they have a lower turn-on voltage?

## Accepted answer (score 7, by Phil Frost - W8II)

The capacitor and resistor make a low-pass RC filter, with a frequency cutoff around $\frac{1}{2\pi RC}$ (in hertz). Do keep in mind $R$ is not just the value of the resistor, but rather the entire load on the circuit which includes the input impedance of the next stage.

The idea is to strip out the RF component, while passing the baseband component.

If the cutoff is too high, the rectified RF gets through, so you're not making an envelope detector anymore.

If the cutoff is too low, it means the envelope detector is slow to respond to changes in envelope amplitude. In an AM receiver this means high frequencies in the demodulated audio will be attenuated.

Since the baseband signal is usually something audible to humans, it's not above 20 kHz. And the RF signal is usually at least an order of magnitude higher than that. So there is a very wide range of values that will work.

You are correct, Schottky diodes are often selected for their lower turn-on voltage and fast switching speed.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16436/am-radio-envelope-dectector, by JackLalane1, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
