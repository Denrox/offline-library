# Signal in the center frequency of my SDR spectrum always

*Tags: software-defined-radio, audio-interface, hackrf · score 4*

## Question

I'm pretty new to SDR, but I understand a little bit about RF.

On all 3 of my SDR device (two RTL one HackRF) The center frequency is always full of interference from something unknown.....it doesn't appear to be static, because if I use a chirpchat demodulator, it's picking up data (even if the protocols wrong, I'm assuming there is still some sort of bit information)

Any idea what this interference is? How do I fix it? Thank you!

## Accepted answer (score 8, by Phil Frost - W8II)

That is DC offset, either in the analog to digital converters, or their driving circuitry.

The average voltage at the ADC's input is ideally exactly in the middle of the ADC's range, since this maximizes the maximum voltage swing up or down before clipping. The DC offset is the difference between the ADC's "middle" voltage and the average voltage present at the ADC's input. The analog circuitry in the SDR will contain biasing circuitry designed to minimize the DC offset.

But, the biasing circuitry and the ADC are subject to manufacturing and temperature variation among other things. It's theoretically possible to reduce the DC offset to an insignificant amount, but in practice this would require such precision that the expense would be unacceptable.

So, nearly every practical SDR with a quadrature mixer has this issue, and engineers work around it in other ways. Many modern modulations designed to be received by SDRs are designed to have no significant signal in the middle of their spectrum for this reason. For signals that don't require the total bandwidth of your device you can tune above or below the signal frequency so it doesn't overlap with the DC offset.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17746/signal-in-the-center-frequency-of-my-sdr-spectrum-always, by Dani, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
