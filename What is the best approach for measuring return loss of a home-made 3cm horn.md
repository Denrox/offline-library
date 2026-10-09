# What is the best approach for measuring return loss of a home-made 3cm horn?

*Tags: impedance-matching, measurement, microwave · score 5*

## Question

Let's assume I have built a SMA-to-waveguide transition that flares out into a horn antenna. There's no flange between transition and horn, it's made of a single metal sheet. The antenna has tuning screws, and my goal is to find the screw position giving least reflected power.

Obviously, I don't have a suitable VNA with which I could measure the antenna S11 parameter. I do however have an uncalibrated power meter.

Which of the following methods gives best results?

1.

Receiver: Connect power meter to horn antenna, aim it at another RF source, find screw position that maximises power indication.

2.

Circulator: Connect TX to circ 1, circ 2 to horn antenna, circ 3 to power meter. Find screw position that minimises power indication.

3.

Directional coupler: connect TX through coupler to horn antenna, s.t. part of the reflected power is coupled towards the power meter. Tune screws, find minimum power.

The underlying more general question is: given that I don't need accurate absolute S11 or VSWR values, what shortcuts can I take to get the best out of my antenna?

## Accepted answer (score 2, by tomnexus)

The circulator is the most sensitive method, because all of the reflected power goes to the power meter.

Some thoughts:

- Are you sure that the circulator is working correctly at your frequency? Any issues with it will come out in the results.
- It is best to pad the source and the power meter, with 6 to 10 dB attenuators, to improve their own matching so that the reflections don't distort the picture.
- You could attempt to calibrate or just validate this method by comparing the power readings seen, with port 2 terminated, shorted and open circuit.

A transmitted power test is the least sensitive to antenna mismatch, but if all you are trying to do is optimise output power, not SWR, then it doesn't really matter if you're at 3:1 SWR or 1:1 SWR.

If you are using it as a receive antenna, with an LNA, then you could tune for noise performances instead. You would point it at a cold part of the sky and tune the antenna for minimum noise power. In a transceiver it might be best to optimise for noise performances and just accept the reasonably good transmit match that you would get.

Finally, you should worry about polarisation. You don't specify the horn type, but if it's big and square it could easily support both polarisations. Are the tuning screws in any way designed to induce circular polarisation? If they're not all in the E plane, they might be. This would be a new measurement challenge, beyond just matching.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12121/what-is-the-best-approach-for-measuring-return-loss-of-a-home-made-3cm-horn, by mpb HB9EGM, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
