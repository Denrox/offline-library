# Relative computational requirement for various digital modes?

*Tags: digital-modes, dsp · score 4*

## Question

What might be the relative computational performance requirements for the various popular digital modes? (FT, JT, WS, PSK31, etc.)

I seem to recall FSK modulation/demodulation being done with 1 or so MHz 8-bit CPUs. By what factor or magnitude have the newer digital modes increased the processor requirements from this?

And what is taking up most of that computational requirement increase (CPU/FPU/GPU cycles) needed in the newer digital modes? (filtering? FFTs? cross-correlation? convolution decoding? AI/ML?, or ???)

Question is motivated because someone said their computer (GHz, multicore, with over 100X more performance than a Cray 1 supercomputer) couldn't handle receiving some popular HF digital mode, which surprised me. After all, lots of deep space comms were done well before Cray 1's were obsolete.

## Accepted answer (score 6, by Marcus Müller)

## Complexity of your question

It's hard to make general statements here, because computational complexity is a property of the *implementation* of a receiver, which usually is a choice given the properties of the transmission.

For example, assume you have 2-FSK. You can either demodulate that by having say, 2 bandpass filters applied to a passband signal, and a maximum-energy detector, or by averaging the phase error signal of a PLL, or by mixing to baseband and mutliplying each sample with the complex conjugate of the previous and making a sign decision.

All these have their advantages and disadvantages, and will perform differently errorwise and computationally, and the latter especially considering that different platforms can do different kind of calculations more or less easily.

But let's be honest here: the complexity of FSK demodulation (and in fact, most simple modulation schemes) will very likely be outshined by far four things:

1. digital Filtering to isolate the signal
2. synchronization in time, frequency (and phase)
3. Equalization
4. channel decoding

## Channelization / Filtering

Assume you know where your signal is in spectrum. It'd be only logical to filter out anything that's not part of the occupied bandwidth as a first step.

That usually would call for the well-known but impossible to realize brickwall filter. So, you live with what you can do and build a long filter.

Now, we're talking classical HAM modes: A steep FIR applied to a "couple hundred kilosamples per second" signal (if at all that much bandwidth) with a couple hundred taps is ... cute for modern hardware.

## Synchronization

Then, we have the synchronization part.

This is where things *really* get system-specific. Does your transmitter just send a white-ish preamble? Then, you might just want to correlate for that preamble (which is nothing but a filter of length equal to preamble length), but on a grid of frequency hypotheses: If you're not frequency-corrected yet, your correlation will not be good, and you'll need to simply "try out" a lot of different frequency offsets.

The complexity of that is typically in the order of $K\cdot L^2$, with $L$ being the preamble length, and $K$ being the number of different frequency offsets you need to try. You can reduce $L^2$ to $L\log L$ with FFT-based convolution, but that's it.  
$K$ is defined by how badly you want to detect the preamble: If $L$ gets longer, a frequency offset leads to more phase rotation, leading to higher decorrelation (until you do more than $\pi$ phase rotation over the whole length $L$). So, sadly, $K$ is a function that increases with $L$, and only decreases if you can accept a higher probability of not detecting the preamble.

Good thing is that after initial acquisition of the signal, complexity drops.

If, on the other hand, your transmit signal is "modern" and uses e.g. OFDM with one of the well-known OFDM synchronization aids (just because it's so standard, and because the paper is really good: Schmidl&Cox is something you want to look at), then the structure of your signal allows simultaneous timing and frequency estimation with a single correlation (within bounds). Nice, because that means your complexity drops a lot.

Phase sync is also very system-dependent: If you have short bursts, then, well, the preamble might be enough to estimate phase for the rest of the signal. If not, you'll have to go one of many routes, the most prevalent being

- in case of PSK, or sufficiently PSK-alike modulations, costas loops, or
- in most cases, transmit data-aided methods like inserting pilot symbols periodically, which require a full demodulation chain afterwards, or
- fully data-aided methods like constantly regenerating the signal that the transmitter would have generated considering the received bits, and comparing the phase of that and the reception through simple correlation, which of course requires that correlation (${}^2$) and a full demodulation, decision, channel decoding and re-modulation chain

## Equalization

Ugh. Equalizers need some form of channel estimation to work, in order to reverse the effects of the multipath propagation.

Again, there's more methods for this than there's modulations, but let's highlight a few.

- If you've got that preamble correlator from above, that might simply yield a reasonable estimate for the channel impulse response, if $L$ was large enough to allow for feasible SNR. That'd come more or less free at the cost of having to have a pretty complex sync to begin with.  
You can then go and try to find an "inverse" of the channel, either by building a zero-forcing (simply transform the channel impulse response to frequency domain, take the inverse, transform back) filter (which has terrible noise amplification) or by building a MMSE filter (similar, but respect noise variance in the process).  
So, you'd get the channel estimation cost plus a running cost of about the square of the length of the channel for equalization.
- If you're looking at a multicarrier system (like OFDM, as used in FreeDV, DVB-T, LTE, WiFi…) then your signal giant multipath channel typically gets decomposed into many flat narrow channels with but a single complex channel coefficient each. That often reduces the complexity of estimation to a linear function of the number of subcarriers, and the cost of equalization to a single complex multiplication per subcarrier.
- You can do a decision-feedback equalizer, if you've got sufficiently low receiver block sizes to allow you to cancel the influence of the first symbol on the later second and so on. You incur the complexity of an IIR, plus estimation and full decision chain.

## Channel Decoding

This is really where things go down.

You mentioned deep space comms: Yeah, good point. You know that there's "daytime" and "nighttime" decoders on Voyager comms? Comparable signal, two different decoders, one better in performance than the other, so that one works more or less at live speeds, whereas the other runs overnight on a more beefy machine on an offline recording.

Channel decoders can be built in different ways. You mention convolutional codes, and we'd often decode them with simple, and complexity-wise quite limited decoders like the Viterbi algorithm. Still uses a metric stuffton of memory and CPU for long depths, but can be made to decide early adaptively to signal quality.

But that's not all there is. You can use iterative decoders, involving e.g. the Turbo principle. Now, all your complexity bounds go out the window. Want to have lower error probability? Just run another iteration.

In more recent years, large block codes have become a favourite way of implementing very close-to-Shannon codes. Low-Density Parity Check (LDPC) matrices can (and will) be of multiple thousand columns in size, and the only way to realistically demodulate them is through iteratively improving the quality of the transmit data estimate by passing info through the check notes. That can, again, be done in very many ways, and LDPC codes are designed with specific hardware or software abilities in mind, having e.g. shifted-identity-matrix substructures or not. Like with most of the iterative decoders, you can abort decoding early, if acceptable error probability and SNR allow.

But, seriously, PCs are not *good* at juggling a lot of small-granularity distributed-memory operations. Both memory and CPU bandwidth get quickly exhausted. So, something that a cheap TV set-top box IC (not to mention smartphone chipsets) can do relatively nicely can be extremely harrowing to get to run sufficiently fast on CPU or GPU hardware.

## Conclusion

One would have to look at the individual standards, but I'm willing to say that usually, modern methods are lower in complexity to demodulate at a desired symbol error rate than legacy digital modes, especially if OFDM is involved.

As soon as we start to deal with bits, however, the full force of the desirable advances of the last 30 years of channel coding hits us in the face and you might end up with a code for which no commodity-CPU software decoder that is real-time capable exists. Of course, it's unlikely that someone specifying a ham mode will rely on custom hardware, unless they are a company that holds patents about that.

For least-SNR modes like WSPR/FT8 both the low-power signal detection (see "synchronization" above) and the channel decoding dominate.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14920/relative-computational-requirement-for-various-digital-modes, by hotpaw2, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
