# Is FM effectively spread spectrum?

*Tags: fm, theory · score 5*

## Question

My understanding is that FM achieves better audio quality (under the right circumstances) than AM by spreading the narrow audio signal's information into a wider RF signal. Does this mean FM is technically a form of spread spectrum?

## Answer (score 11, by Kevin Reid AG6YO)

This is the sort of question that often comes down to “what definition of the word is useful” — not necessary any objective truth. However, I would be inclined to say that no, wider FM should not be considered a form of “spread-spectrum”, even though it is a kind of “spreading” across the spectrum.

This is because modulation techniques that are considered spread-spectrum combine the increased bandwidth with some particular strategy for extracting the intended communication from that entire signal bandwidth (often by a pseudorandom sequence that the transmitter and receiver agree on). We can see this strategy as being a *substitute* for the simpler selection strategy of “use a narrow filter”. Thus, spread spectrum systems have resistance to interference of all kinds.

On the other hand, wide-band FM is not so general-purpose; it can result in *reduced* resistance to interference (assuming total power of the wanted signal and the interfering signal are kept constant), in at least one scenario: imagine an interfering single unmodulated carrier. If this falls within the bandwidth of the FM receiver, and is of equal or greater power, then the FM capture effect will greatly weaken reception of the wanted signal. Thus, all else being equal, increasing bandwidth increases the likelihood of interference. FM's “strategy” is “pick the strongest signal in this bandwidth”.

So, I would say that wide-band FM is not spread-spectrum because:

- Spread-spectrum increases signal bandwidth to improve signal-to-noise ratio against *arbitrary* interference (as long as it is uncorrelated with the chosen pseudorandom sequence).
- Wider FM increases signal bandwidth to decrease noise *if the noise is not concentrated in a narrow band that could overwhelm the FM carrier*.

Disclaimer: I'm not very well acquainted with the mathematical perspective on radio and signal-processing theory. There may be some considerations that I have missed.

## Answer (score 2, by Marcus Müller)

In a spread spectrum system, you use a method of transporting data in some bandwidth, and then apply some way of spreading it over a larger bandwidth, whilst maintaining the original method of data modulation. "Spread" implies that the signal was narrow before and is *made* wide.

Common examples¹ of this include

- frequency hopping spread spectrum (FHSS), where you take some narrowband modulation method, but change the carrier frequency rapidly, so to spread the signal over more space where there's potentially narrowband interferers,
- direct-sequence spread spectrum (DSSS), where you take your data-carrying symbols (or bits), and multiply each of them with a sequence, thereby making many symbols (or bits) out of one, thereby increasing the symbol rate (or the bitrate), which leads to increased bandwidth requirement.

Now, FM is not such a technique: it doesn't take another method of transporting information and *spread* it. It just actually modulates the information in frequency.

¹ There's few others that you find in practice. Lora uses what they call Chirp spread spectrum, but that's really just using the delay of a cyclically shifted reference waveform (a chirp) in combination with DSSS. There's time-hopping, which is rarely used, for it doesn't have the narrowband-interferer robustness of FHSS, but all the average-power downsides.  
If you need to make your low-datarate stream of data more robust and have bandwidth to spare, nowadays, you'd often rather go with something that can deal with a multipath channel, which you get through occupying much bandwidth, and has better gain than just repeating the same symbol – e.g., you'd do OFDM with N subcarriers and use a 1/N-rate code with heavy interleaving.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21400/is-fm-effectively-spread-spectrum, by Someone, Kevin Reid AG6YO, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
