# If receive performance doesn't depend on SWR, then how can I tune my manual HF antenna tuner by band noise?

*Tags: hf, antenna-system, impedance-matching, noise · score 6*

## Question

The popular question "[What is the relationship between SWR and receive performance?](What%20is%20the%20relationship%20between%20SWR%20and%20receive%20performance.md)" asks if a receiver with a well-matched antenna (low SWR) beats a receiver with a poorly-matched antenna, with everything else being equal. The consensus opinion of the answers, weighted according to the votes on the answers, is no; the two receivers should receive about the same.

The idea is that an impedance mismatch leads to power loss, and a weaker signal at the receiver. But losses shouldn't affect receiver performance as long as the signal-to-noise ratio (SNR) is the same, because the receiver's automatic gain control (AGC) feedback circuit can easily add a few more decibels of gain to compensate for any such losses. There is an important caveat to this rule that the received RF noise floor must be above the receiver's noise floor, because otherwise the signal-to-noise ratio will be affected.

This logic makes sense to me, and I can find no flaws in it. But if that is so, then why is it that when I use my manual T-network transmatch (antenna tuner) to tune my ZS6BKW antenna on various HF bands such as 40m and 20m, I can get a fairly good match without transmitting by turning the knobs to maximize the band noise in my headphones? (I say "band noise" because I tune the radio to an unused frequency and then adjust the transmatch for maximum static, but if there were a signal on the frequency then I would adjust the transmatch to make the signal the loudest.) If the consensus answers to the other question are correct, then I would think that turning the knobs would make no difference at all to the volume of sound in the headphones.

My HF rig is an Elecraft K2, which has an excellent receiver. The caveat to the rule shouldn't apply, because the RF noise floor should be well above the receiver's noise floor on 40m and 20m.

## Accepted answer (score 7, by hobbs - KC2G)

Receive power *does* vary with SWR; but for reception quality we're interested in signal-to-noise ratio. As long as you're getting enough receive power that the noise received from the antenna is greater than the receiver's own noise floor, getting more power from the antenna won't result in any noticeable improvement to your ability to copy. That's why we say things like "gain doesn't matter for receive antennas" or "SWR doesn't matter for receive". It's not an absolute truth, but it's a good starting point. For a typical HF noise floor, you need a lot of negative gain or a lot of mismatch loss before you'll notice any difference.

So why can you tune an antenna by peaking the noise? Because, again, receive power *does* vary, and because receiver AGC is (deliberately) imperfect, especially at low levels. So when you're just listening to noise, and turning the knobs on the tuner, the audio level *will* go up and down — not by as many dB as the RF level goes up and down, but by enough to notice. If you do the same thing while tuned to a good signal, you might or might not notice the effect, but in any case after making any necessary volume adjustments to equalize the signal level, the noise level should end up the same as it was before.

## Answer (score 3, by Phil Frost - W8II)

The noise you hear in your headphones is coming from the antenna. When you tune the antenna and minimize the SWR, the losses between the antenna and the receiver are minimized, thus more of the noise received by the antenna makes it to the receiver, and you hear more noise in your headphones.

(Assuming of course the receiver is set to a mode where power is proportional to noise, as in AM, SSB, or CW.)

It's also possible that the noise you hear in the headphones comes from thermal sources in the feedline or the receiver, or something other than the electromagnetic field around the antenna. In this case tuning the antenna would *not* significantly increase the noise volume in the headphones, and improving SWR would indeed increase receive performance. This is however very unlikely on HF, since the electromagnetic noise floor is so high compared to the internal noise of even a very inexpensive receiver.

## Answer (score 2)

Missing in this discussion is the fact that optimum power matching does not necessarily correspond with optimum noise matching.

Antenna tuner alignment on band noise is possible when the input impedance of the receiver is 50 Ohms real. Then maximum received noise corresponds to correct antenna tuner alignment.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17910/if-receive-performance-doesn-t-depend-on-swr-then-how-can-i-tune-my-manual-hf-, by rclocher3, hobbs - KC2G, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
