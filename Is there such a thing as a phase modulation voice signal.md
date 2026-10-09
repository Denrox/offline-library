# Is there such a thing as a phase modulation voice signal?

*Tags: modes, encoding · score 5*

## Question

Wikipedia indicates that in the digital domain ASK, FSK, and PSK are common. It seems that only AM and FM are used for analog forms of communication.

Why don't we use Phase Modulation techniques, and stick mostly to variants of AM and FM?

## Answer (score 3, by WPrecht)

PM is actually quite similar to FM in terms of modulation effects.

With phase modulation, the change of the phase angle is proportional to the message that is to be modulated onto the signal. With frequency modulation, on the other hand, the instantaneous change in frequency is proportional to the message that is to be modulated onto the signal. So with a little work, an FM modulator can be used to generate phase modulated signals and visa-verse.

However, that little extra work is more circuit complexity, so to base a transceiver on it requires more circuits and more cost. Plus, there is the potential for ambiguity on decoding between signals at +180deg and -180deg.

## Answer (score 2, by Phil Frost - W8II)

Phase-modulated voice is equivalent to FM, modulo differences in frequency response. An FM transmitter contains a pre-emphasis circuit to counteract this effect, making the two effectively equivalent on the air.

From the US extra class question pool:

E7E06 (A)  
*Why is de-emphasis commonly used in FM communications receivers?*  
**A.** For compatibility with transmitters using phase modulation  
B. To reduce impulse noise reception  
C. For higher efficiency  
D. To remove third-order distortion products  
An unmodulated carrier of angular frequency $\omega_c$ is simply:

$$ y(t) = \cos(\omega_c t) $$

$\omega_c t$ is the phase at time $t$. For phase modulation we simply add the baseband signal $m(t)$:

$$ y_\mathrm{PM}(t) = \cos\left(\omega_c t + m(t) \right) $$

Note that frequency is the instantaneous rate of change of phase. In other words, frequency is the derivative of phase. Likewise, phase is the integral of frequency. So to derive the expression for frequency modulation we just throw in an integral:

$$ y_\mathrm{FM}(t) = \cos\left( \omega_c t + \int _{0}^{t}m(\tau )d\tau \right) $$

This doesn't have too much effect on the signal because:

$$ \int \cos x\,dx=\sin ax+C \\ \int \sin x\,dx=-\cos ax+C $$

So, the difference between PM and FM is an integration of the baseband signal. This changes the phase of the baseband signal but that's not important for a voice transmission. The integration also effectively low-pass filters the baseband signal, since a sinusoid of equal amplitude but higher frequency has less area under each positive half-cycle, and thus the maximum of its integral is less. The pre-emphasis in the FM transmitter high-pass filters the baseband signal prior to the modulator, counteracting this effect, thus making PM and FM transmitted signals effectively equivalent.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1013/is-there-such-a-thing-as-a-phase-modulation-voice-signal, by Adam Davis, WPrecht, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
