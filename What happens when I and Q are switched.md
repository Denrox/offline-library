# What happens when I and Q are switched?

*Tags: software-defined-radio, direct-conversion, am · score 6*

## Question

In [https://ham.stackexchange.com/a/1068/9](What%20are%20the%20I%20and%20Q%20in%20quadrature%20sampling.md) it's shown that one can use

$$ r = \sqrt{I^2+Q^2} $$

to decode AM signals from a direct conversion receiver. It appears that, in this particular case, I and Q are interchangeable, thus the SDR doesn't care which is which.

Is this true, and for straight AM they can be switched without issue?

Are there other modes, such as SSB and CW, where switching I and Q wouldn't matter?

If I'm operating an SDR, what clues can I look for that would indicate a swapped I and Q?

## Accepted answer (score 6, by Phil Frost - W8II)

Swapping I and Q reverses all the frequencies. For example, a signal 5 kHz above the mixer's LO will appear at -5 kHz, instead of 5kHz. CW and AM are symmetrical in the frequency domain, so it doesn't matter for the purposes of demodulation, though your software is likely to display the wrong frequency. SSB is not: reversing I and Q will make USB look like LSB, and LSB look like USB.

If you have a waterfall with lower frequencies on the left, then tuning to a higher frequency should shift everything to the left. If it goes to the right instead, you know I and Q are reversed.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1188/what-happens-when-i-and-q-are-switched, by Adam Davis, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
