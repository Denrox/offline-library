# Doppler Shift Compensation in Inter Satellite Communication

*Tags: receiver, satellites, frequency, oscillator, doppler · score 7*

## Question

I am currently doing a project in the area of optical inter-satellite communication (GEO-LEO).

I am using a optical carrier of 281 THz, and the Doppler shift corresponding to it is ±7 GHz. I introduced this Doppler shift in the transmitted signal $S$ as an offset like

$$ S \cdot e^{j 2 \pi f_\mathrm{doppler}} $$

At the receiver, I am using a Costas Loop as a demodulator. I have to do Doppler shift compensation to recover the signal. Guess, I have to add an offset compensator in the local oscillator.

Can anybody help me in doing this?

## Answer (score 2, by cmm)

I am jumping in late, and I hope that the OP received an out-of-band answer, or found their own answer.

I have a problem with the question, given the statement that the OP is using a Kostas Loop for the demodulator. By definition, the Kostas Loop is a type of phase-locked loop (PLL) in which the local oscillator (LO) frequency is adjusted until the phase error is small. At that point, the phase and frequency of the LO match the received (possibly virtual) carrier frequency. It does not seem to be meaningful to talk about adding an input to the LO to adjust the frequency, other than the error filter.

Because OPs ask good questions, the problem must be deeper, such as the signal not being strong enough (high enough signal to signal plus noise) to allow a broad enough response on the error filter to achieve lock. If this is the case, then a method of pre-compensating for the Doppler shift would be helpful. The loop bandwidth could be reduced, and lock achieved for a noisier signal.

This requires that we have a way of knowing what the proper doppler shift should be, and applying that to the LO. I think that could be hard, as it required knowledge of the positions of both the low Earth orbit and geostationary orbit satellites, both initially, and as they navigate or orbits change over time.

Because a loop has a broader tracking range when it is locked than it has an acquisition range, it may make sense to allow for a long initial lock time, knowing that over the course of an orbit the Doppler shift with take on the full range of positive and negative values. At some point, the loop will lock, and should remain locked.

As a second-order method to achieve faster re-lock if lock is lost, the error voltage could be used as a signal source for a secondary PLL that predicts the doppler shift. This would generate an estimation of the Doppler shift with a period of one relative orbit. The form of that estimate will depend on the orbital characteristics of the LEO satellite, including the orbital plane, apogee, and perigee.

The answer is to keep it simple. Wait a relatively time for a lock, and then preserve the lock.

You might need an extra hack to handle the times when the Earth eclipses the LEO. In an ad-hoc digital loop, this would take the form of freezing the loop error voltage for the expected time of an eclipse when lock is lost. I don't think the OP was asking about the eclipse case.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1936/doppler-shift-compensation-in-inter-satellite-communication, by Seetharama, cmm. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
