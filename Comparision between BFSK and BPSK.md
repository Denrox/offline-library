# Comparision between BFSK and BPSK

*Tags: modes · score 4*

## Question

Why is BPSK preferable over BFSK? On what parameters this comparison is based? What are the advantages of BPSK?

## Answer (score 3, by AndrejaKo)

In general, FSK modulations tend to be worse than comparable linear modulations by several criteria.

Unfortunately, I couldn't find a nice picture for this, so the one above from AtlantaRF will have to do, but in telecommunications literature, you have these bit error rate versus per bit signal to noise ratio graphs for various modulation schemes. One thing you always see in those graphs is that you need higher $E_{b}/N_{0}$ for same BER in FSK compared to PSK. In amateur radio, (clean) power is often relatively limited and getting more with less is respected, giving advantage to PSK.

One big advantage of FSK is that we don't need clean power for it! It can work with very non-linear power amplifiers, so a set power level is easier to reach with FSK than it is with PSK.

Next, we have the spectral efficiency as well. FSK is less spectrally efficient compared to PSK with same number of modulation levels.

For example, for non-coherent orthogonal FSK, the null-to-null bandwidth is $B=(M+1)R_{s}$, while for PSK (which is same as for non-coherent DPSK as used in say BPSK31) it's $2R_{s}$, so in binary case, we have $3R_{b}$ compared to $2R_{b}$ for BPSK. If number of modulation levels increases, FSK starts to lose very quickly, since in PSK case, bandwidth does not depend on number of modulation levels.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5279/comparision-between-bfsk-and-bpsk, by shweta, AndrejaKo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
