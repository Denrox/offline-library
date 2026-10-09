# How does FM station have fixed frequency when FM modulation changes the frequency?

*Tags: rfi, fm · score 4*

## Question

I am not sure if this question fits better in physics.stackexchange or ham.stackexchange, feel free to correct me. I am new to studying RF and SDR in general, I was looking up how modulation works and FM by definition encodes information to carrier frequency by modifying the frequency of wave. Considering this, it doesnt make sense how you can tune into an fm frequency, say 101, 101 being the carrier frequency makes sense but once information/music is encoded to this shouldn't the frequency change to something else?

## Accepted answer (score 8, by Richard Fry)

"Tuning" an FM receiver sets the *center* frequency of the receiver, but its internal circuitry is designed to pass enough of the Bessel sidebands produced by frequency modulation of that waveform to be demodulated with low noise and distortion.

## Answer (score 5, by user10489)

There are two ways to look at this: center frequency and bandwidth.

In FM, the frequency varies as the amplitude of the audio varies. If the audio was a sinusoidal tone, the frequency would vary symmetrically around a center frequency, which is constant. More complex audio is generally still symmetrical. The FM receiver actually locks on to that center frequency using the symmetry, so even if your tuning is a bit off (but still within the radio's pass band), it will lock on to the signal. This is a fundamental defining feature of FM.

All transmissions containing information are assigned not just a frequency, but a bandwidth. (Without bandwidth, it can't contain any information.) The bandwidth of the FM transmission is tied with a fixed ratio (frequency modulation index) to the maximum amplitude range of the audio. If the audio has a dynamic range large enough to cause the FM to exceed its assigned bandwidth, it will be clipped before being modulated into FM. The maximum range of amplitude variation of the audio is sometimes called "envelope".

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16295/how-does-fm-station-have-fixed-frequency-when-fm-modulation-changes-the-freque, by mathemagician, Richard Fry, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
