# SDR: How are I and Q determined from the incoming signal in quadrature sampling on the receiver side?

*Tags: software-defined-radio, receiver, theory · score 6*

## Question

I'm new to digital radios and signal processing, so I apologize if this question is trivial but I haven't been able to find an answer here or by googling. Also, some terminology might be off, please feel free to refer me to correct sources or to correct my basic understanding.

Reading various sources (e.g. here), it seems to me that the I and Q components of a sample correspond to the complex representation of a portion of a sine wave described by $I \cdot \cos(2 \pi f t) + Q \cdot \sin(2 \pi f t)$ w.r.t. $t$, where $f$ denotes the frequency of interest. My question is, how does the receiver actually compute $I$ and $Q$ when a sample is needed?

Suppose that a sample is taken at a time $t$, I don't think that the receiver could just multiply the *instantaneous* strength $V$ (voltage?) of the incoming signal by $\cos(2\pi ft)$ and by $\sin(2 \pi f t)$ to recover $I$ and $Q$ (as the diagram in section "Receiver Side" of the linked article appears to suggests) since this would carry no more information than reporting $V$ itself.

Moreover, in principle, the incoming voltage from the antenna on the receiver side could be any continuous (and differentiable?) function $V(t)$... so how are $I$ and $Q$ recovered? Are they actually the values that minimize some error function between the incoming voltage and the function described by $I \cdot \sin(f) + Q \cdot \cos(f)$ over a length of time corresponding to some sampling interval $[t, t']$? E.g. something along the lines of: $$ I,Q = \arg\min_{I,Q \in \mathbb{R}}\int_{\tau=t}^{t'} \big( I \cdot \cos(2 \pi f \tau) + Q \cdot \sin(2 \pi f \tau) - V(\tau) \big)^2 \;\mbox{d}\tau \;\mbox{ ?} $$

Thank you!

## Accepted answer (score 3, by Phil Frost - W8II)

Suppose that a sample is taken at a time $t$, I don't think that the receiver could just multiply the *instantaneous* strength $V$ (voltage?) of the incoming signal by $\cos(2\pi ft)$ and by $\sin(2 \pi f t)$ to recover $I$ and $Q$ (as the diagram in section "Receiver Side" of the linked article appears to suggests) since this would carry no more information than reporting $V$ itself.

It can, and it does precisely this. But you are right that it carries no more information.

In practice it carries less, and that's the point. Say we want to make a WiFi radio operating in the 5 GHz band. This would require a sample rate of at least 10 GHz. That would be an expensive ADC, as would the computing power to process such a high sample rate.

But the bandwidth of a WiFi signal is only some 10s of MHz. The point of the mixer is to convert the signal at high frequency (somewhere in the 5 GHz band) down to a lower frequency which can be represented at a lower sample rate and thus more easily digitized and processed.

So, the output of the mixer is low-pass filtered before being digitized by the ADC.

Moreover, in principle, the incoming voltage from the antenna on the receiver side could be any continuous (and differentiable?) function $V(t)$... so how are $I$ and $Q$ recovered? Are they actually the values that minimize some error function [...]

No, it's nothing so complex. Remember the mixer is an analog component, so there's no need for any "sampling interval", and an arbitrary continuous function is no problem. The ideal mixer performs simply:

$$ I = V(t) \cdot \cos(2\pi f) \\ Q = V(t) \cdot \sin(2\pi f) $$

If I and Q are interpreted as the real and imaginary parts of a complex number respectively, it is simpler (by Euler's formula) to think of the mixer as performing:

$$ V(t) \cdot e^{i 2 \pi f} $$

This is useful because multiplying by $e^{i 2 \pi f}$ shifts all frequencies by $f$, which you can see for example in rule 103 of Wikipedia's list of Fourier transforms.

These *analog* signals are then low-pass filtered and digitized by the ADC.

## Answer (score 3, by Kevin Reid AG6YO)

the I and Q components of a sample correspond to the complex representation of a portion of a sine wave described by $I \cdot \cos(2 \pi f t) + Q \cdot \sin(2 \pi f t)$ w.r.t. $t$, where $f$ denotes the frequency of interest

This is correct (if we suppose the incoming signal is a sine wave, i.e. an unmodulated carrier).

I don't think that the receiver could just multiply the *instantaneous* strength $V$ (voltage?) of the incoming signal by $\cos(2\pi ft)$ and by $\sin(2 \pi f t)$ to recover $I$ and $Q$ … since this would carry no more information than reporting $V$ itself.

Actually, this is useful. The key facts are:

- This multiplication can done in the analog domain, using a *quadrature mixer,* to produce a new pair of “downconverted” signals *without sampling them yet.* This is how SDRs avoid needing gigahertz-rate analog-to-digital conversion.
- A signal of actually interesting content (modulation) is not just a pure sine wave, but has other frequency components.

These I and Q signals have had all their frequency components shifted down in frequency by $f$ — this is known as “baseband”. The signals are then low-pass filtered (which removes all frequencies outside of the range $f ± \text{filter frequency}$ in the original signal) and sampled by an ADC to produce the digital baseband signal.

Note that this means that an incoming signal at frequency $f$ has frequency *zero* in the baseband representation. If the signal is a sine wave with a small difference from $f$ (e.g. perhaps it is frequency-modulated around $f$) then the baseband form has a small difference from zero. If it has more frequency components, all of those are still present in the baseband signal, just translated.

You're correct to think that an IQ form of the original RF signal contains no more information than the original instantaneous voltage. The point of IQ is to allow us to throw out something we don't need — the extremely high carrier frequency $f$ — without discarding the *information we care about* in the signal (provided it is limited to a small band around $f$), so as to be able to receive, digitize, and demodulate it with simple general-purpose hardware.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17735/sdr-how-are-i-and-q-determined-from-the-incoming-signal-in-quadrature-sampling, by Steven, Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
