# SSB demodulation

*Tags: receiver, frequency, oscillator, ssb · score 4*

## Question

I was building the superhet receiver for ham radio. But I seem to have got stuck at the demodulation stage.

As an example:

Suppose the person is transmitting SSB signal (20m band) at 14.250 MHz carrier frequency.

Let the speech signal occupy 1KHz bandwidth.

So the RF signal using Upper Side Band is 14.251 MHz.

I take intermediate frequency of 455 KHz.

So my Local oscillator is set to 14.251 + 0.455 = 14.706 MHz.

Now at the demodulator, the 455 KHz wave is needed to be demodulated. For this particular example, the oscillator frequency I need to inject in demodulator is 456 KHz (to recover 1 KHz speech).

Firstly, am I going wrong somewhere till now?

Secondly, in real situation, I would not be knowing this much information. The only thing I would be knowing is that my Mixer oscillator is set to 14.706 MHz. So the Rf freq must be 14.251 MHz. Now here is the problem:

This 14.251 MHz could be a 14.250 MHz carrier with 1 KHZ sideband or it can be a 14.249 MHz carrier with 2 KHz sideband or any other pair of values. So how do I demodulate?

In other words, how do I know what frequency to inject in the demodulator? Do I just keep tuning the oscillator attached to the demodulator until the combination is struck?

If yes, then wouldn't finding any random person over this wide range of band quite painful; First you set the Mixer oscillator to some value and then you keep tuning the demodulating oscillator over the entire 3 or 4 KHz bandwidth until you find someone?

## Accepted answer (score 4, by jcoppens)

To understand better, I'd suggest you follow this:

1) If you have an AM transmitter at 10.000 MHz (let's use simple numbers). If someone whistles in the microphone, at, say, 1kHz, two sidebands will appear, at 9.999MHz and 10.001 MHz (and a carrier at 10.000MHz).

2) If you convert the AM tx into USB, and transmit at 10.000 MHz, the whistler will appear at 10.001 MHz (only).

3) If you want to *hear* the whistle at 1kHz, you will have to insert a carrier at 10.000 MHz again. Any other frequency will change the tone of the whistle. (This is how direct conversion works).

4) So, if you IF is 0.5 MHz (again simple numbers), your tuning oscillator should be 9.500 MHz, resulting in the whistler being at 0.501 MHz. You would then need a carrier inserted at 0.500 MHz to get the whistle correct.

5) The voice passband should ideally be around 0.3 to 2.5 kHz, so you IF filter should pass from 0.5003 to 0.5025 MHz.

This is not overly complicated - in a superhet receiver, you will have a carrier oscillator at 0.500MHz, a tuning oscillator which varies in the range 0.5 MHz below the desired band, and the filter as described in 5).

And yes, tuning SSB is not easy - you have to be at less than 100 Hz (!) of the correct frequency to have an enjoyable voice reception. The problem isn't so much with a one-note whistler, but if (s)he whistles a melody, all notes will be off, making it sound very strange.

Note that 'demodulating' SSB is just mixing frequencies, just like mixing from 10.000 to 0.500 MHz - an SSB demodulator is just a mixer.

## Answer (score 2, by Bedfordian)

I would suggest looking at a couple of sites:

http://www.radio-electronics.com/info/rf-technology-design/superheterodyne-radio-receiver/basics-tutorial.php

http://users.tpg.com.au/users/ldbutler/Superhet.htm

- Looking at Figure 4 on this second site shows that the RF front end and the local oscillator have a ganged tuning capacitor. The difference in frequency between the two circuits is equal to the IF. Without that front-end selectivity, the mixer would be producing multiples of every signal arriving at the antenna, at equal levels.

At the IF stage, you can decide on the selectivity by adding band-pass circuits (e.g. 3kHz for SSB and 500Hz for CW).

For SSB demodulation, you also need to inject a carrier with another oscillator (the Beat Frequency Oscillator). There's another useful description and diagram on this page:

http://www.9h1mrl.org/ukrae/arc_cd/full/html/c5-1-2.htm

Going back to your example, your demodulator will always be set to the IF of 455kHz, and does not need to vary. The output of the demodulator is audio/speech/morse code/etc.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1953/ssb-demodulation, by Plutonium smuggler, jcoppens, Bedfordian. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
