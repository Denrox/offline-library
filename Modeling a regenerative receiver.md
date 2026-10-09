# Modeling a regenerative receiver

*Tags: receiver, theory, dsp · score 4*

## Question

What is the signal processing model of a simple regenerative or super-regenerative receiver?

Is it just a linear 2-pole IIR filter with gain? How does a single regen control knob control both selectivity and gain? What causes the super-regenerative effect (a sub-harmonic oscillation?) to occur?

## Answer (score 2)

This is a basic question and needs an answer.

1. Regenerative receiver or audion. Single LC-filter with undamping: Q-multiplier. The frequency transfer of such a filter can be obtained from a simulation. See figure. As you can see: the AM demodulated audio response is affected when selectivity is too high. The example shows 1 MHz mediumwave. Audio bandwidth of 3 kHz requires sideband transfer of plus and minus 3 kHz. That is 6 kHz top bandwidth or a maximum Q-factor of 1000 kHz / 6 kHz = 167. Higher selectivity at the cost of audio bandwidth.

For shortwave the effective Q-factor can be much higher: 6 Mhz and 6 kHz BW allows Q_eff = 1000.

The single control knob adjusts the Q multiplication. In the simulation this is the negative resistance. In practice obtained from vacuum tube, bipolar transistor or field effect transistor.

1. Super-regenerative reception is an effect that the undamping is too strong and leads to oscillation AND that the DC operating point is affected in such a way that the oscillation stops. The oscillator starts again and the process is repeated. The sequence of start-stop is in the order of 20 to 50 kHz for most superregenerative receivers. The high sensitivity follows from the initial phase of the radiofrequency signal during startup of the oscillation: in phase with the oscillator "eigenfrequency" helps and out of phase is opposite.

Not in your question is a third option: synchrodyne reception. The oscillator is synchronised to the received carrier, simply by pushing. The audio response is now mainly the result of the post-detection audio bandwidth.

Have fun with these simple experiments! They lead to insight that is important for education.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17885/modeling-a-regenerative-receiver, by hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
