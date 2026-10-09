# What would happen if the low noise amplifier (LNA) is saturated?

*Tags: lna · score 3*

## Question

Suppose that there is a 2 dBm interference signal and a -90 dBm signal of interest (SOI) at the input of LNA (Gain = 1, in linear region). Suppose that the P1dB of LNA is 1 dBm, so the LNA is saturated and can't amplify the input signal properly. My question is what the output of SOI would be like? Is it still -90 dBm? The interference and SOI are at the same frequency band.

## Answer (score 3, by S H)

As the amplifier gets closer to saturation, its gain reduces. This is because during the portion of time the transistor is saturated, it is not able to output any other signal. The signal of interest will therefore become weaker, or another way to think of it is the amplifier has less gain and proportionally higher noise figure.

The intermodulation products will also dramatically increase, faster than predicted by the third order intercept point (IP3) of the amplifier, because IP3 is characterized in the linear region and no longer applies as the amplifier is pushed into saturation.

## Answer (score 2, by Sam brown)

You would see higher order mixing products at the output of the LNA. The closest to the SOI would be third order products. 2*f2-f1 and f2-2*f1, where f1 and f2 are the frequencies of the two input signals.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20795/what-would-happen-if-the-low-noise-amplifier-lna-is-saturated, by tyrela, S H, Sam brown. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
