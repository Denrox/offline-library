# How would a time-difference-of-arrival receiver with two antennas know which side the signal is from?

*Tags: receiver, theory, direction-finding, phased-array · score 15*

## Question

An easy TDOA design by Byonics was published with the following schematic:

It appears that the antennas are switched at a rate of 640Hz, which allows a 640Hz tone to be heard in the radio when the antennas are not in phase. When the antennas are equidistant from the RF source, the tone goes away, so by turning the antenna and finding the null you can determine the direction of the source.

The author's description further explains:

Note that the transmitter being on that perpendicular line means that it could either be directly ahead, or directly behind. You would need to move some distance along the line of the antennas and take another bearing to determine which direction the transmitter actually was. In the next version, **when the audio from the receiver is fed back into the chip and analyzed, it will be able to tell if the signal is coming from the left or right** when the tone is present, and light the appropriate LED.

With the radio's audio going into the microcontroller, and the antennas out of phase with the source, what is the microcontroller looking for, or how would it tell, whether the signal is coming from the right or the left of the dipole array?

## Accepted answer (score 18, by Kevin Reid AG6YO)

When the tone is present, it is because the antennas are out of phase. One antenna's signal will be leading the other; which one is leading depends on which one is closer to the transmitter (provided that the antennas are less than 1/2 wavelength apart, so that the phase difference will always be less than 180°).

When we switch from the lagging signal to the leading signal (for example), the phase of the switched signal jumps ahead; equivalently, the *frequency* of the signal increases for an instant and then returns to normal. The same but inverted applies to switching from the leading signal to a lagging signal. The output of a FM receiver is determined by the frequency of the input, so we get a result like this:

The green waveform is the switch control and the blue waveform is the demodulated signal (the frequency deviation). After audio-frequency filtering on the output, we get a more ordinary tone, though with a delay introduced by the filter:

If the time delays of the arriving signal are the other way around, then the phase shifts are opposite, and the audio signal is negated — or, equivalently, phase shifted by 180°.

Therefore, to distinguish between left and right (that is, left signal leading vs. right signal leading) one need merely compare the phase of the audio signal to the phase of the switching signal; there are only two possible results (except when the audio tone is absent and the phase is therefore undefined).

Note that the exact phase difference found will depend on all delays in the system, including in the external receiver; but that would be simple to calibrate for.

I have built a simulation of this system using GNU Radio, and used it to produce the plots shown and confirm that the technique can produce a reliable left/right indication (at least for an unmodulated input). Here are the GNU Radio Companion file and generated Python program (GNU Radio 3.7+ required).

Note that while the RF sections of this simulation use complex (analytic) signals, there is nothing in those sections which would make a difference from the results obtained by using real signals at a nonzero IF as usual analog RF electronics do.

On the other hand, in the perpendicular direction, it is not possible to distinguish the front and back sides; there is a fundamental ambiguity due to the symmetry of the antenna array. No direction finding system can distinguish between directions in which its antennas are symmetrical; the asymmetry which allows the discrimination described here comes from the switching of the antennas rather than their shape.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1610/how-would-a-time-difference-of-arrival-receiver-with-two-antennas-know-which-s, by Adam Davis, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
