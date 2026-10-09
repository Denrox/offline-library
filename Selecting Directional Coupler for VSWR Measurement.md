# Selecting Directional Coupler for VSWR Measurement

*Tags: rf-power, directional-coupler · score 3*

## Question

Assume directional coupler is coupling with 16dB attenuation when signal is traveling from input to output. And directivity is let's say 20dB.

If I understand correctly, when the RF signal is traveling from input to output the coupled port signal will be 16dB less than the input signal. And if any signal is reflected back from the output port to input direction then this reflected signal will be coupled with 16+20 = 36dB attenuation. (learned from this video)

If I use a directional coupler to measure an antenna's performance then signal generator will be connected to output port and the antenna will be connected to input. So the reflected signal from the antenna will be coupled with 16dB less to coupling port. And the main signal we sent from output to input will be coupled with 36dB attenuation.

My question is: should I simply select a coupler with high directivity and low coupling attenuation? Because in my logic the directivity should be high enough so the main signal we sent traveling from output to input should not be coupled to couple port so much (we are not interested in it). And only the reflected signal should be coupled with as little attenuation as possible. Is this the correct approach?

## Accepted answer (score 3, by tomnexus)

Yes, you understand it correctly.

Directivity is the most important thing, as it limits how low a VSWR you can measure. In your example, 20 dB directivity, will show a constant ~20 dB return loss, or a VSWR of about 1.2, even with a perfect 50 Ohm load.

Coupling ratio is not as important. You can always adjust the input power to keep the detector in its sweet spot.

Watch out, when measuring reflected power, that your readings aren't dominated by external transmitters. Any signal out there will be received, coupled and detected like reflected power. It helps to use a larger test signal, and to have a frequency selective detector.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13227/selecting-directional-coupler-for-vswr-measurement, by nandflash1, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
