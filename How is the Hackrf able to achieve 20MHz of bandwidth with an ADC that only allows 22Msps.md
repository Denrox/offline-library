# How is the Hackrf able to achieve 20MHz of bandwidth with an ADC that only allows 22Msps?

*Tags: software-defined-radio, hackrf · score 5*

## Question

The way I understand it, is that to avoid aliasing on an ADC, you have to be in the first Nyquist zone (so half the sampling speed). What doesn't make sense to me is how the Hackrf is able to bypass this, and achieve 20MHz of bandwidth, even though the 1st Nyquist zone would be only 11MHz.

I notice from the schematics that the MAX5864 ADC is two channels, with the baseband I signal going into one channel, and the baseband Q signal going into another. Do the two channels get added together, to form an overall bandwidth of 20MHz?

Also, while I'm at it, what exactly is the purpose of using in an sdr? Is it to make modulation/demodulation easier?

## Accepted answer (score 6, by hotpaw2)

Another way to look at it is that an IQ ADC is really taking 2 independent (not added together) samples per IQ sample. Thus the rate of information gathered is double from a just scalar sampling at 22 MHz. The 90 degree offset between the 2 IQ sample components allows capturing phase information that can help a complex FFT (et.al.) differentiate between what would have been aliasing between spectrum above and below the heterodyning LO frequency.

## Answer (score 7, by hobbs - KC2G)

The Nyquist limit is half the sampling rate because otherwise you can't distinguish a signal at a frequency $x$ from a signal at $f_s - x$ which starts 180° out of phase from the first one — they give exactly the same sequence of real samples. But [quadrature sampling gives *exactly* the phase information needed to resolve this ambiguity](Understanding%20how%20quadrature%20heterodyning%20captures%20information%20from%20negative%20frequencies.md). Knowing $\sin \omega t$ limits us to two of four quadrants, but knowing $\sin \omega t$ and $\cos \omega t$ at the same time limits us to one quadrant. With this distinction provided, it's possible to distinguish frequencies up to $f_s$ — or a little less, given that we still need to filter out frequencies above the sample rate, and filters have skirts.

## Answer (score 2, by user10489)

Are the two channels added together? Yes and no.

The whole point of collecting I and Q is so they can be treated as real and imaginary parts of a single complex sample.

This is one of the key methods of SDR.

This answer explains it well: https://electronics.stackexchange.com/questions/39796/can-somebody-explain-what-iq-quadrature-means-in-terms-of-sdr

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18077/how-is-the-hackrf-able-to-achieve-20mhz-of-bandwidth-with-an-adc-that-only-all, by camerakid, hotpaw2, hobbs - KC2G, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
