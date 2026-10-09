# FM carrier wave frequency determination

*Tags: fm · score 3*

## Question

I know the difference between AM and FM, but how does a receiver determine the carrier wave frequency, as the frequency edited during the modulating process?

## Answer (score 2, by Phil Frost - W8II)

There are several ways.

One is *slope detection*. By placing the carrier on the transition band of a filter, the filter's output amplitude is proportional to the frequency:

- A higher frequency input moves closer to the passband, thus a higher amplitude output
- A lower frequency input moves closer to the stopband, thus a lower amplitude output

Thus, a slope detector is effectively an FM to AM converter. The demodulator is completed by following the output of the filter with an AM detector.

In digital implementations where the input samples are complex, the phase angle of each sample can be calculated. Then, the derivative of phase is frequency.

A *phase-locked loop* (PLL) is another implementation. The idea is to keep a variable-frequency oscillator synchronized in phase to the received signal. The phase of the signal and oscillator are compared, and this error signal adjusts the oscillator frequency to minimize the error.

This is just a small sampling: there are many other designs in use, especially in analog implementations which have a different set of rules for cost and complexity.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7874/fm-carrier-wave-frequency-determination, by root, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
