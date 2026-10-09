# Why is analog TV vestigal side band and not SSB?

*Tags: ssb · score 4*

## Question

Analog TV signals have one sideband cut off to reduce their (very wide) bandwidth and save frequency space in the ether. The lower sideband is cut off, but not completely, the lower 1.25 MHz is kept resulting in a vestigial sideband signal. I've read several explanations on why this vestigial sideband is kept, but they don't fully make sense to me.

1.

Fully removing the lower sideband requires a filter with a very sharp edge because the signal contains significant low frequency information. Such a sharp filter is not practical, so as a compromise part of the lower sideband is kept. This makes total sense, but doesn't explain why you would want to keep a full 1.25 MHz of bandwidth. Surely the bandwidth filters at the time analog TV was developed could do better than that?

2.

"The video signal has significant low-frequency content (average brightness) and has rectangular synchronizing pulses. The engineering compromise is vestigial-sideband transmission." is what Wikipedia says. That makes no sense to me. All the information is present in only one sideband, so as long as one sideband is preserved without damage the original signal (including synchronization pulses, etc) can be recovered.

3.

It was desirable for TV sets to be able to use an envelope detector, which is cheaper than an SSB demodulator. That reasoning makes sense, but as far as I know envelope detectors only work for AM signals, not VSB. So I have no idea if this reasoning is just random internet nonsense or if there is some substance to this.

One reason I can imagine that makes it fit together is if TV sets use an envelope detector to extract the timing pulses and an SSB demodulator for the luminance signal, but I have not been able to find any corroboration of this idea.

So, what was the *actual* reason analog TV uses VSB with a full 1.25 MHz of lower sideband?

## Accepted answer (score 3, by JanKanis)

What I get from the paper JohnVE3WNA linked is slightly different from his answer:

Sidebands in a signal produce quadrature (i.e. phase and amplitude) distortions when demodulated with an envelope detector. In AM or DSB, the quadrature distortions from the lower and upper sidebands cancel out, but in SSB there is only one sideband so the quadrature errors remain, which would distort the TV image.

The RMA committee realized, correctly, that the sidebands at more than about 0.75 MHz from the visual carrier would normally be so small that most of the lower sidebands could safely be eliminated. It was a good tradeoff at that time. With VSB, the RMA committees were able to squeeze 4 MHz video bandwidth into the 6 MHz straitjacket.

So there is +/- 0.75 MHz of full sideband, and then 0.5 MHz in which the filter reduces the lower sideband amplitude to zero. The remaining higher frequencies for which there is only a single sideband are normally so small in amplitude that the errors they cause are negligible.

The receiver then needs filters to properly equalize the lower frequency components (which have more energy because they have double side bands) with the lower energy higher components. Affordable filters of that time would introduce frequency dependent delays, which means phase shifts and image ghosting. The paper then goes into what should be done about those, the part about the VSB signal was just introduction. This is where Nyquist slopes etc. come in. Those issues were never really solved, at least not at the time of publication. The author argues that the phase shift issue should be solved before there is any use to discussing analog HD transmissions. (Which of course never were introduced for NTSC, HD only came with digital modes.)

So in short, the 1.25 MHz vestigial sideband was a compromise between reducing bandwidth and still allowing the signal to be demodulated with a cheaper envelope detector with acceptable distortion. (Unfortunately this solution introduced its own types of problems and distortions, which were not all solved.)

So all three points in the question contain kernels of truth, but the actual reasoning is not something I could have derived from them.

Reference: The Vestigial Sideband and Other Tribulations, Archer S. Taylor, 1988, NCTA Technical Papers

## Answer (score 3)

**Hand-waving: It's all about money**

My understanding was that the process for filtering DSBSC to SSBSC was imperfect (or, rather, the costs for *perfection* were much higher) at the time, which resulted in a potential loss of information that had a big impact on the results.

As the Wikipedia article mentions, video has a fair amount of low-frequency components and important synchronization pulses. Constructing a perfect sideband that did not malign these parts of the signal wasn't actually feasible at the time. At least not for a *commercial* product intended to be in every living room at particular price-point.

So a slightly more complicated demodulation scheme that included part of the potentially missing information was used.

Thus we have lower bandwidth, we don't need high accuracy filters, and low-frequency components can be carried without further difficulty. The trade-offs are more complicated demodulation and slightly higher bandwidth than SSBSC.

**Technical Overview: It's all about Nyquist**

According to one paper I've skimmed on the subject, the problem with SSB with the information they were modulating is that they got a lot of quadature distortion because the carrier and modulation vectors are so far apart. It was found that if you could lower the amount of "swing" then you also lower this potential distortion, and ~0.75 MHz from the visual carrier was a sweet spot.

But that only defines the problem; it does not solve it. Now we have the problem of the "Nyquist slope", where our filter needs to form a knee without causing unwanted phase shifts. And, plainly put, **no** IF shaping filter of the day could reliably do this. Certainly not at the price-point we needed, and maybe not at all.

So, even the 0.75-1.0MHz sideband was a compromise, and was still susceptible to phase distortion.

The paper goes into more detail about the series of compromises that basically forced us into using a solution for a 1930s problem, but by then it was too late, and even NTSC standards had to accept the limitations.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20999/why-is-analog-tv-vestigal-side-band-and-not-ssb, by JanKanis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
