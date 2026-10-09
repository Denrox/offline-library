# Is The Lowest Antenna Terminal Feedpoint SWR Always Optimal?

*Tags: vertical-antenna, radial, efficiency, radiation · score 3*

## Question

Intuition might lead one to believe that the antenna configuration with the lowest SWR(50) across its input terminals would provide the best radiation efficiency for the antenna ***system***. But is that always a correct assumption?

## Answer (score 2, by Richard Fry)

Below is a table showing that this is not always the result, for every antenna configuration. In this case, the configuration with the lowest system SWR(50) also has the lowest system radiation efficiency.

The system in this analysis using 0.5λ buried radials has higher SWR(50), with higher system gain and higher radiation efficiency than the system using 0.1λ radials. But even though that SWR(50) is higher, a well-designed matching network could be added to its feedpoint terminals to produce nearly a perfect match to a 50 j0 Ω transmission line connected there, with a matching loss that would reduce system gain and radiation efficiency by only several tenths of a decibel.

The gain and system radiation efficiency of that Z-matched system using 0.5λ buried radials (and other rows of that table) could be greater than from the system using 0.1λ radials — even though the 0.1λ system has lower SWR(50) before any matching networks are added.

## Answer (score 2, by Jens)

No, minimizing the SWR at load (antenna) interface is not sufficient for the minimization of the end-to-end loss at system level (Transducer Loss).

A Figure (screenshot) might be helpful for illustration. The case is for SWR=2.06 at load, implying a SWR=1.88 at the input of an example lossy transmission line (50Ω). The purple curve is the total system loss as function of normalized cable length, and with the thick black dot representing the nominal cable length of here 100 feet. If we increase the cable length to 135 feet, the SWR at load remains constant but the total system loss decreases from 1.39dB to about 1dB. If we shorten the cable from 100 to 90 feet, the total loss will increase to almost 1.5dB. This might appear very strange at first reading. However, as we change the cable length, we also change the input impedance of the transmission line at its interface with the source – and therefore the extent of match, or mismatch, w.r.t. the output impedance of the source at its operating point.

Now, if we deploy an impedance matching (next Figure) at load to enable SWR=1, then the input impedance of the line at the interface with the source equals the characteristic impedance of the line (50Ω). This impedance might still be mismatched with the given output impedance of the source (like in the considered example). Therefore, SWR=1 at load is not sufficient to reduce the total system loss of now 0.62dB further down to the matched line loss (0.54dB) as would be implied by solely the transmission line.

It makes a difference, if the impedance matching at the load aims at SWR=1, or at a complex conjugate matching which is considered in the third Figure. The total system loss is now further reduced to 0.56dB, but the SWR at load is SWR=1.28. So, we accept this SWR and tolerate reflections on the line for the benefit of increased delivered power. (This seems like the point S. Sessink makes in his posting.)

If we would deploy two matchings (assumed lossless in this discussion about principles) for both, SWR=1 at load and complex conjugate matching at source, the total system loss would eventually equal the matched line loss (0.54dB).

The applied tool allows to compare the case of no-matching with eight different matching approaches and the implied losses at system level. Such assessment does matter when answering how much of the maximum available power from a given source can be delivered to the load, commonly referred to as the system Transducer Loss. (Although not essential for the above discussion, the characteristic impedance becomes complex at relatively low RF frequencies and could be considered as such but would not compromise the above remarks.)

@ Phil:

I took your example and added a corresponding figure. – Indeed, when looking into the line, the source will see a transmission line input impedance that moves on a perfect circle as we change the cable length – on a perfect circle because the line is assumed now lossless. The power mismatch between source and line, or loss, is determined by the **radius** (ρ=|Γ|) of that circle (in a Smith-Chart). As the changing impedance stays on that circle, the source will always deliver the same power into the line, and eventually to the load at the other end, because the line is assumed lossless. Therefore, the system loss vs. cable length is in this case constant and a straight horizontal line (see figure).

@ Phil:

From your previous question with “the load impedance around a constant SWR circle (neglecting losses)” I thought a lossless line should be considered for the answer.

I go back to a lossy line, and the source has exactly 50 Ohm output impedance. To see waviness, we consider a line which is lossy and with characteristic impedance that is complex. The next figure shows the resulting waviness.

The waviness becomes more pronounced if additionally, complex conjugate matching is applied at the input of the line (see next Figure, because the significant reflection at the source enhances the waviness). For short cable lengths, the overall system loss of now (P2/Pmax)=(P2/P1) is lower than the matched line loss, which is a known phenomenon attributed to the nodes affected by the phase-shift between voltage and current waves due to the now complex line impedance.

The waviness becomes practically ignorable at higher RF frequencies. It disappears whenever the line characteristic impedance is, or is assumed to be, a real value.

As the big advantage, the used tool allows to incorporate the complex characteristic impedance of real-world transmission lines. This is very much in contrast to the popular ARRL equation that is included in the plots for comparison. Furthermore, the ARRL equation (like TLW) calculates only (P1/P2), and the ARRL equation allows this only for real-valued characteristic impedances; matching at the source side cannot be addressed; therefore, the approach is not a transducer loss assessment at system level. Good luck to those who wish to explore the waviness with the existing ARRL tool (or TLW).

For interesting comparison and perspective, the following diagram is published by the ARRL frequently and again in the QST Magazine, March 2021, p. 53. The Figure shows the “Additional Loss in dB Caused By Standing Waves” as function of “Line Loss in dB When Matched,” with SWR at Load as parameter.

For example, a source with 50 Ohms output impedance is considered. The source is connected to a 50 Ohms line that is terminated by 200 Ohms; this implies SWR=4 at load. Further, we consider a Matched Line Loss of 1 dB, which together with the Additional Loss Caused by SWR (0.8dB from the diagram) implies 1dB + 0.8dB = 1.8dB. From the Figure, readers are inclined to conclude this 1.8dB would be the total system loss. However, SWR not only affects the line-related loss but also the mismatch between source and the connected transmission line. (See screenshot below.) This impedance mismatch loss on its own is 1.1dB for the considered example and indeed exceeds the “Additional Loss in dB Caused by Standing Waves” (of 0.8dB).

The true system loss of 2.9dB (49% power loss) significantly exceeds a total of 1.8dB (34% power loss) which one might erroneously conclude from the diagram in QST. The QST diagram can represent a total system loss on the specific assumption of a lossless complex conjugate matching at the input of the transmission line and if the line has a real-valued characteristic impedance (which is not the case at lower RF frequencies). Regrettably, QST articles regularly fail to highlight these crucial conditions. So, the plot in QST can very much misinform because it is incomplete to assess the total end-to-end system loss (Transducer Loss) of a real-world transmatch.

Besides considering typical real-world transmatches, the applied tool considers the impact of mismatches on system loss, as well as the impact of intended impedance matching for zero-reflection or, alternatively, the impact of complex conjugate matching, or combinations thereof. Therefore, the tool allows to assess the merit of matching, or if the deployment of lossy match circuit/s might not be worth the effort or be even counterproductive in terms of overall system loss.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17998/is-the-lowest-antenna-terminal-feedpoint-swr-always-optimal, by Richard Fry, Jens. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
