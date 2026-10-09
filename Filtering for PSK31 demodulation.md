# Filtering for PSK31 demodulation

*Tags: software-defined-radio, digital-modes, filter, psk31 · score 6*

## Question

What's the ideal filter for PSK31 demodulation? That is, something that minimizes ISI, while having a narrow bandwidth to reject adjacent channels, while being reasonably matched?

Most PSK modes use a root raised cosine pulse shape, thus the receiver can convolve the received signal with an identical filter which is then both perfectly matched and zero-ISI. However, PSK31 simply uses a raised-cosine envelope, which I guess means there's a second order discontinuity at each transition between 0's and 1's which increases the occupied bandwidth, and also the appropriate receive filter is not so obvious. G3PLX describes:

Note that the transmitter and receiver filters have to be "matched" to each other for the ISI performance to be right. Some systems like this use a pair of identical receive and transmit filters which are matched. If I did this and someone else came along wanting to improve the performance, they would have to get everyone else to change their transmit filters. I have therefore chosen to use the simple cosine shape for the transmitter and match that in the receiver. This leaves the way open for others to develope better receivers without new transmitters being incompatible with old. This is slightly different from the SP9VRC approach.

The few implementations I've been able to examine use a set of filter taps copied from some other implementation, or don't specifically say what the filtering is.

Is there any detailed information on these filters? Or equivalently, how would one go about designing such a filter?

## Accepted answer (score 4, by Marcus Müller)

So, to maximize SNR you'd use a matched filter (which is the conjugate complex of the time-reversed TX pulse shaping filter), and assuming the pulse shaper has been reasonably chosen, that'd also a ISI-minimizing filter.

Now, psk31.txt from the original DOS program says

The solution is to filter the output, or to shape the envelope amplitude of each bit which amounts to the same thing. In PSK31, a cosine shape is used. To see what this does to the waveform and the spectrum, consider transmitting a sequence of continuous polarity-reversals at 31 baud. With cosine shaping, the envelope ends up looking like full-wave rectified 31Hz AC.

So, the transmit filter is half a cosine. (Not RRC. I've just corrected the wikipedia page – it said RRC.)

The same document doesn't state what exactly the RX filter is – only that it is supposed to be "matched" (which doesn't seem to mean the "canonical" matched filter above). The author's reasoning goes like this:

Note that the transmitter and receiver filters have to be "matched" to each other for the ISI performance to be right. Some systems like this use a pair of identical receive and transmit filters which are matched. If I did this and someone else came along wanting to improve the performance, they would have to get everyone else to change their transmit filters. I have therefore chosen to use the simple cosine shape for the transmitter and match that in the receiver.

I cannot help but feel this is bogus reasoning. Mathematically, it's clear that maximum SNR without ISI can *only* be obtained by correlating with the conjugate reversed TX filter – and that being time-symmetric and real in the case of a cosine filter implies you get the same TX as RX filter. Stat – there's no design freedom anymore once you've chosen the TX filter, no matter how you chose that.

Of course, you can correlate multiple periods (let's say 4) of RX signal with all hypothetical permutations and get better SNR – but that's a lot more channel (de)coding than modulation.

So, best you can do is a cosine RX; everything else is higher-level error-correction. You should do that error correction – a trellis is your friend!

## Answer (score 2, by Phil Frost - W8II)

I was not able to find very much history on these filters, but I did track down two sets of coefficients from popular implementations, and for your pleasure, I'll present them here.

## Transmit Filtering

The pulse shape transmitted by a PSK31 transmitter is effectively a raised cosine, twice the symbol duration. That is, we can imagine a PSK31 transmitter as sending a series of impulses of either +1 or -1, then filtered by a FIR filter with coefficients that are a raised cosine.

Here are four such pulses:

The transmitted signal is then the sum of all these pulses. We can see there's no ISI in the transmitted signal since at the peak of one pulse (the ideal sampling point), the amplitude of the adjacent pulses is zero.

The frequency response of the transmit pulse shaping filter determines the bandwidth occupied by the signal. Here it is:

By modern standards, this isn't very good. Note the numerous, slowly decaying side-lobes, with the first of them only about 32dB down. As we will see, this doesn't necessarily detract from performance, provided everything within that frequency band is only white Gaussian noise. However, it does present a problem when trying to pack many signals close together, which unfortunately is frequently the case with PSK31.

## Matched Filter

In an AWGN channel the receive filter that maximizes the signal to noise ratio is the same filter as the transmit filter: a *matched filter*. So let's suppose the transmitted pulses are passed through a matched filter in the receiver. They would then become:

Notice now the amplitude of the adjacent pulses is not zero at the peak of each pulse. This is inter-symbol interference (ISI). Since the signal is the sum of each pulse, when a symbol is sampled to determine if it's a 0 or a 1 we're sampling not only the current symbol but also the ones next to it.

I found two filter implementations that attempt to address this by not using a matched filter in the receiver. Instead, they aim to make the pulse shape such that there is zero amplitude from adjacent pulses at each sample point, while remaining as close as possible to the matched filter in frequency response.

## G3PLX Filter from fldigi

The first I got from fldigi, but based on the attribution in the source it appears to originate from the original PSK31 implementation by G3PLX. Again, the four pulses after passing through this filter:

Notice the ISI is mostly eliminated: the amplitude of adjacent pulses is almost zero at the peak of the pulse being sampled.

Frequency response of G3PLX filter (orange), with the matched case (blue) for comparison:

The somewhat faster roll-off doesn't necessarily make it better. While it could mean an adjacent signal is better rejected, it also means some fraction of the transmitted signal energy is not captured..

It's also a significantly different shape at the top, where it matters most (since this is where most of the power is). Any difference in shape means a reduction in signal to noise ratio.

## PSKCore DLL

Now the second filter, which is from the PSKCore DLL. Again, pulse shapes and frequency response:  
*Blue: matched. Orange: PSKCore.*

## ISI: maybe there's another solution?

These two implementations sacrifice signal to noise ratio in order to use a filter with less ISI than a matched filter. We can quantify that loss by normalizing all the filters to have the same energy, with energy being the sum of the squares of their coefficients. If the coefficients are $x_1, x_2, \dots, x_n$, then:

$$ E = \sum_{i=1}^n x_i $$

By dividing each coefficient by $\sqrt E$ we get a normalized filter with $E=1$:

$$ {x_1 \over \sqrt E}, {x_2 \over \sqrt E}, \dots, {x_n \over \sqrt E} $$

For such a filter, if the samples represent voltage, then power in = power out. If the input pulse has E=1, then the peak of the filtered pulses output pulses are:

- matched filter: 1
- G3PLX: 0.9538
- PSKCore: 0.9711

Converting these to power in dB is for example $20 \log_{10}(0.9711) = -0.2547\:\mathrm{dB}$ so the change to SNR for each filter is:

- matched: 0 dB
- G3PLX: -0.4109 dB
- PSKCore: -0.2547 dB

Furthermore, The G3PLX and PSKCore filters still have non-zero ISI. The penalty calculation above accounts only for noise due to white Gaussian noise in the received signal; ISI remaining after filtering is additional noise that degrades decode accuracy. To give an idea of what this looks like, here is a bit stream decoded with the PSKCore filter with no noise and perfect timing:

Without ISI, there would be only two lines here, with each dot being exactly a 0 or a 1. However, depending on the value of the previous and next bit being a 0 or a 1, the decoded value is shifted from this ideal.

But I'll offer an observation: if we know the transmit filter (we do) and the receive filter (we can pick that), we know the pulse shape, and thus the ISI. So if the pulses have a non-zero amplitude at the sampling points of other pulses, we'd know what that amplitude is. If we know what the adjacent symbols are, then we can subtract their known contributions to the ISI and eliminate it entirely.

Trouble is of course we don't know the adjacent symbols, not only because noise introduces uncertainty, but those adjacent symbols in turn depend on the next adjacent symbols.

The Viterbi algorithm can be used to solve this problem in a computationally feasible way. It's more complex than a linear filter, but given the slow symbol rate of PSK31, the computational complexity is still trivial. The combination of a matched filter and a Viterbi detector is optimal in the case of an AWGN channel. I'm not aware of any existing decoders for PSK31 which use this technique, and I suspect it may be an improvement over current practice.

Having prototyped a simulation in as AWGN channel, Viterbi decoding and a matched filter show a performance gain over the PSKCore approach.

It remains to be seen if this amounts to an improvement in a real environment with timing errors, multipath, interfering stations and so on.

## Appendix: filter coefficients

Filter coefficients from fldigi:

```
// 4-bit receive filter for 31.25 baud BPSK
// Designed by G3PLX
//

double gmfir2c[64] = {
 0.000625000,
 0.000820912,
 0.001374651,
 0.002188141,
 0.003110600,
 0.003956273,
 0.004526787,
 0.004635947,
 0.004134515,
 0.002932456,
 0.001016352,
 -0.001539947,
 -0.004572751,
 -0.007834665,
 -0.011009254,
 -0.013733305,
 -0.015625000,
 -0.016315775,
 -0.015483216,
 -0.012882186,
 -0.008371423,
 -0.001933193,
 0.006315933,
 0.016124399,
 0.027115485,
 0.038807198,
 0.050640928,
 0.062016866,
 0.072333574,
 0.081028710,
 0.087617820,
 0.091728168,
 0.093125000,
 0.091728168,
 0.087617820,
 0.081028710,
 0.072333574,
 0.062016866,
 0.050640928,
 0.038807198,
 0.027115485,
 0.016124399,
 0.006315933,
 -0.001933193,
 -0.008371423,
 -0.012882186,
 -0.015483216,
 -0.016315775,
 -0.015625000,
 -0.013733305,
 -0.011009254,
 -0.007834665,
 -0.004572751,
 -0.001539947,
 0.001016352,
 0.002932456,
 0.004134515,
 0.004635947,
 0.004526787,
 0.003956273,
 0.003110600,
 0.002188141,
 0.001374651,
 0.000820912
};

```

And PSKCore DLL:

```
//  Filter type:   Multiband filter
//  Design method: Parks-McClellan method
//  Number of taps  =  65
//  Number of bands =  2
//  Band   Lower       Upper       Value      Weight
//         edge        edge
//
//  1       0.0        .03125         1.         1.
//  2        .0625     .5          .0000       286.
#define BITFIR_LENGTH 65
const double BitFirCoef[BITFIR_LENGTH*2] = { // 16 Hz bw LP filter for data recovery
 4.3453566e-005,
 -0.00049122414,
 -0.00078771292,
 -0.0013507826,
 -0.0021287814,
 -0.003133466,
 -0.004366817,
 -0.0058112187,
 -0.0074249976,
 -0.0091398882,
 -0.010860157,
 -0.012464086,
 -0.013807772,
 -0.014731191,
 -0.015067057,
 -0.014650894,
 -0.013333425,
 -0.01099166,
 -0.0075431246,
 -0.0029527849,
 0.0027546292,
 0.0094932775,
 0.017113308,
 0.025403511,
 0.034099681,
 0.042895839,
 0.051458575,
 0.059444853,
 0.066521003,
 0.072381617,
 0.076767694,
 0.079481619,
 0.080420311,
 0.079481619,
 0.076767694,
 0.072381617,
 0.066521003,
 0.059444853,
 0.051458575,
 0.042895839,
 0.034099681,
 0.025403511,
 0.017113308,
 0.0094932775,
 0.0027546292,
 -0.0029527849,
 -0.0075431246,
 -0.01099166,
 -0.013333425,
 -0.014650894,
 -0.015067057,
 -0.014731191,
 -0.013807772,
 -0.012464086,
 -0.010860157,
 -0.0091398882,
 -0.0074249976,
 -0.0058112187,
 -0.004366817,
 -0.003133466,
 -0.0021287814,
 -0.0013507826,
 -0.00078771292,
 -0.00049122414,
 4.3453566e-005,
//
 4.3453566e-005,
 -0.00049122414,
 -0.00078771292,
 -0.0013507826,
 -0.0021287814,
 -0.003133466,
 -0.004366817,
 -0.0058112187,
 -0.0074249976,
 -0.0091398882,
 -0.010860157,
 -0.012464086,
 -0.013807772,
 -0.014731191,
 -0.015067057,
 -0.014650894,
 -0.013333425,
 -0.01099166,
 -0.0075431246,
 -0.0029527849,
 0.0027546292,
 0.0094932775,
 0.017113308,
 0.025403511,
 0.034099681,
 0.042895839,
 0.051458575,
 0.059444853,
 0.066521003,
 0.072381617,
 0.076767694,
 0.079481619,
 0.080420311,
 0.079481619,
 0.076767694,
 0.072381617,
 0.066521003,
 0.059444853,
 0.051458575,
 0.042895839,
 0.034099681,
 0.025403511,
 0.017113308,
 0.0094932775,
 0.0027546292,
 -0.0029527849,
 -0.0075431246,
 -0.01099166,
 -0.013333425,
 -0.014650894,
 -0.015067057,
 -0.014731191,
 -0.013807772,
 -0.012464086,
 -0.010860157,
 -0.0091398882,
 -0.0074249976,
 -0.0058112187,
 -0.004366817,
 -0.003133466,
 -0.0021287814,
 -0.0013507826,
 -0.00078771292,
 -0.00049122414,
 4.3453566e-005
};

```

Or more accurately, the time-reversed complex conjugate filter. But since this filter (like most pulse shaping filters) is both real and symmetrical, it works out to the same thing.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7703/filtering-for-psk31-demodulation, by Phil Frost - W8II, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
