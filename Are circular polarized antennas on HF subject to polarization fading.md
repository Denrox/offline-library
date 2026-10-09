# Are circular polarized antennas on HF subject to polarization fading?

*Tags: hf, polarization · score 3*

## Question

Consider the common scenario of two amateur radio operators communicating through an ionospheric channel. Typically, each station will have a linearly polarized antenna, like a dipole or a vertical. I understand that the ionosphere will randomize the wave's polarization over time, and so there will be some time-variant fading as the polarization changes.

LZ1AQ has some nice demonstrations of this, where the receiver is switched between horizontally and vertically polarized antennas. The difference between the two polarizations is sometimes as great as 20 dB, and the best choice of polarization varies over time. It would then follow that in the typical situation where the receiver has only one antenna to choose from, fades as deep as 20 dB would be experienced.

Now say the receiving antenna is circularly polarized while the transmitting antenna remains unchanged. Does this eliminate fading due to polarization mismatch?

## Answer (score 3, by Marcus Müller)

This question is *on point*. Let me make a quick excursion on how we physically model the rotating effect that the ionosphere has on linear polarizations.

You have [elegantly shown](Can%20left-hand%20and%20right-hand%20circular%20polarizations%20exist%20at%20the%20same%20time.md) in a previous answer that you can decompose any linearly polarized wave into two orthogonal circularly polarized ones of equal magnitude.

And that's exactly how we describe the *Faraday effect* in the ionosphere.

A ionosphere is a plasma, i.e. there's a lot of unboond charged particles floating around relatively freely, swinging around some drifting places, doing nothing inherently very specific. A charged particle moving about is essentially an electric current – and that causes a magnetic field. But, when these movements are random, all these magnetic fields just cancel and there's no net magnetic field.  
Now, the earth's ionosphere is a bit special, because there's the earth magnetic field applied to it. That forces ions to move in circles, in a plane perpendicular to the magnetic field lines. Imagine a copper ring in which a current flows around – it will align exactly that the induced electromagnet's north pole points in the south pole "direction" of the field lines.

Back to our circularly polarized "composite" wave: When that wave travels in parallel to the field lines, the direction of the E-field of the circularly wave rotates at the wave's frequency. That in turn exerts a force on charged particles.

Now comes the interesting part: There's rotational sense that goes well with the circling of the charged particles due to the earth magnetic field, and one that has to work against that. The LHCP wave component of the linear polarization "sees" a different medium than the RHCP one¹! There's one circular polarization which experiences a higher refractive index than the other, so they don't travel at the same speed.

Thus, the phase between RHCP and LHCP changes over distance; since the phase defines the angle of the linearly polarized sum wave, that wave experiences *Faraday Rotation*².

That would mean that the magnitude of what a circularly polarized receive antenna could pick up wouldn't ever change.

However, on HF, we don't see pure linear polarizations, but more elliptic ones, too. I must admit I'm not 100% sure how that physically happens - it has got to have something to do with a different attenuation for the two circular polarizations, because an elliptic polarization can be modeled as the sum of RHCP and LHCP with *different* magnitudes (and the angle of the main axis still defined as the phase between these two).

No matter *where* that comes from, it means that one circular polarization doesn't come through as well as the other. The more the ellipse looks like a circle, the less the opposing rotational sense circular polarization is present. So, concluding:

Are circular polarized antennas on HF subject to polarization fading?

Yes, but only as far as one can observe elliptic polarizations.

Now say the receiving antenna is circularly polarized while the transmitting antenna remains unchanged. Does this eliminate fading due to polarization mismatch?

Not completely, because of the above reason.

I don't know anything from experience to recommend, but consider this: If you build two compact linearly polarized receive antennas, and mount them perpendicularly, then you can combine them with a phase shifter and variable attenuators to find the optimum polarization.

¹ Please don't ask me which is which, I'll have to throw strange gang signs with my hands and put my head at unhealthy angles, cry a bit and then start over to remember my microwave engineering classes in such detail.

² By the way, we do the same in small scale using magnetic materials in waveguides to change polarizations. And because feeds can be made polarization-selective, and because we can switch magnetic fields on and off, that's a way to build a high-power microwave switch without moving parts.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16903/are-circular-polarized-antennas-on-hf-subject-to-polarization-fading, by Phil Frost - W8II, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
