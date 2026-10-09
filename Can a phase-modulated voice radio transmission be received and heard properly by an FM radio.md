# Can a phase-modulated voice radio transmission be received and heard properly by an "FM" radio?

*Tags: modes, fm · score 4*

## Question

Not necessarily an amateur radio question (but perhaps a licensed amateur should know the answer?) - I note that the specifications for marine VHF radio operating in the 156-157 mhz band call for both (or allow both - or either?) frequency-modulation and phase modulation. So my question is - can typical civilian equipment (ie scanners, ham radio tranceivers, etc) discriminate or decode phase-modulated signals from marine VHF radios? Or are those transmissions only receivable by other marine radios?

(I note that "modulation" does not appear to be a valid or available tag, which is surprising given the forum)

## Answer (score 5, by Phil Frost - W8II)

Consider an unmodulated carrier. It has a phase that increases with time at some constant rate. The rate that phase increases is what we call the frequency.

What if the frequency isn't constant, but a function of time $\omega(t)$? If the frequency goes higher, phase increases faster. A lower frequency is a slower frequency increase. The phase at any given time is the accumulated phase change since the beginning of of time. In other words, phase is the integral of the instantaneous frequency:

$$ y(t) = \cos\left(\int_0^t \omega(\tau) d \tau \right) $$

We can extend this a bit to also allow a phase offset to be added at any time:

$$ y(t) = \cos\left(\theta(t) + \int_0^t \omega(\tau) d \tau \right) \tag 1 $$

This is a general expression we can use to represent any phase or frequency modulated signal with the functions $\theta(t)$ and $\omega(t)$ representing the phase and the angular frequency at any given time.

For frequency modulation, we don't add any phase offset, but the baseband signal $x(t)$ is added to the carrier frequency $\omega_c$. So:

$$ \theta(t) = 0 \\ \omega(t) = \omega_c + x(t) $$

Substituting these into equation 1, we get frequency modulation as:

$$ \begin{align} y(t) &= \cos\left(0 + \int_0^t \omega_c + x(\tau) d \tau \right) \\ &= \cos\left(\omega_c t + \int_0^t x(\tau) d \tau \right) \tag 2 \end{align}$$

For phase modulation, the phase offset is the baseband signal, and the frequency is just the carrier frequency. So:

$$ \theta(t) = x(t) \\ \omega(t) = \omega_c $$

So phase modulation is:

$$ \begin{align} y(t) &= \cos\left(x(t) + \int_0^t \omega_c d \tau \right) \\ &= \cos\left(\omega_c t + x(t) \right) \tag 3 \end{align} $$

The only difference then between frequency modulation (equation 2) and phase modulation (equation 3) is that the baseband signal $x(t)$ has been integrated in frequency modulation. Therefore:

- phase modulation is equivalent to frequency modulation with the baseband signal differentiated, and
- frequency modulation is equivalent to phase modulation with the baseband signal integrated.

Differentiation is a high-pass filter, and integration is a low-pass filter, so the two are really the same thing except for the frequency response. Especially considering radio standards already specify some kind of modification to the frequency response called pre-emphasis, one can convert a phase modulation radio into frequency modulation or vice-versa just by the modification of one term in the pre-emphasis function. As such, the difference between phase and frequency modulation is just in how we model the function of the device mathematically, while the two functionally are essentially the same.

## Answer (score 2)

FM and PM are almost identical; the answer is yes.

PM is limited in phase deviation, FM is not. The audio frequency response is different: PM received on a(n) FM receiver lacks lower audio frequencies due to the (apparent) differentiation of the frequency modulation.

In a formula: FM audio equals the actual deviation of the frequency; PM audio equals the actual deviation of the phase. Relation: Phase(PM) = d/dt{Phase(FM)}.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17839/can-a-phase-modulated-voice-radio-transmission-be-received-and-heard-properly-, by Peggy Schafer, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
