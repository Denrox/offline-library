# How were 1920s hams able to measure megahertz frequency?

*Tags: equipment-operation, measurement, history · score 8*

## Question

I was reading 200 Meters and Down but one thing that was unclear to me was that hams in the 1920s were operating on the 200 meter frequency, which is around 1.5 Mhz .... or 1500 kilocycles to use the old phrasing.

What's unclear to me is *how* they were able to measure frequencies that high. Up to around 20 kHz you could use audio frequencies, but how do you measure Hertz above 20 kilocycles -- especially just using vacuum tubes?

## Accepted answer (score 5, by natevw - AF7TB)

Discovered this via [a comment on another answer.]

According to their Wikipedia article:

**Lecher lines** were used as frequency measuring devices until frequency counters became available after World War 2.

The idea is to short a transmission line after some distance, forming what we now would call a resonant stub. The resonant reflections set up standing waves; the nodes of *those* waves could then be detected with an RF probe:

The voltage goes to zero at nodes located at multiples of half a wavelength from the end, with maxima called antinodes located midway between the nodes. Therefore, the wavelength λ can be determined by finding the location of two successive nodes (or antinodes) and measuring the distance between them, and multiplying by two.

But in practice, rather than having a fixed distance-to-short and moving an RF current probe, it sounds like usually there was a movable "shorting bar" under which was marked an appropriate scale:

In operation, the U end acts as a coupling link and is held near the transmitter's tank coil, and the shorting bar is slid out along the arms until the transmitter's plate current dips, indicating the first node has been reached. Then the distance from the end of the link to the shorting bar is a half-wavelength.

Apparently Lecher lines were even used to calculate the speed of light (working from known frequencies back…) before the turn of the century, "an important confirmation of James Clerk Maxwell's theory that light was an electromagnetic wave like radio waves"!

By September 1946, a "Frequency measurement at UHF" article in Radio News still listed this technique, as well as others which have already been mentioned in other answers/comments here:

[…] in general practice such great accuracy is not necessary, and frequency measurements at u.h.f. are generally performed by the following methods:

1. Wavemeters.
2. Lecher wires.
3. Heterodyne frequency meters.

IIUC, what the article describes as a wavemeter is essentially a resonant circuit with a conveniently-labelled variable capacitor.

(A PDF of the full issue is currently linked as the first citation on the Lecher lines article, which starts on page 50.)

## Answer (score 5, by Glenn W9IQ)

The US National Bureau of Standards (NBS) had a system for basic measurement of frequencies as early as 1911. They used very basic calculations to determine the resonance of an LC circuit. The math was greatly advanced in 1923 in an article in *Radio Broadcast* magazine entitled ""Reducing the Guesswork in Tuning". The method involved careful measurements of the physical dimensions of the capacitors and inductors that were applied to the equations. There is little doubt that the hams of that period closely followed and took advantage of this development.

During this same early 1920 period, the NBS was already experimenting with quartz oscillators as a frequency standard. They collaborated with other labs to continue their research. By 1929, Bell Labs had delivered four 100 kHz (kc at the time), temperature controlled crystal oscillators (TCXO). The uncertainty of these oscillators were estimated to be 10 ppm. These became the NBS primary frequency standards in this period.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10441/how-were-1920s-hams-able-to-measure-megahertz-frequency, by RoboKaren, natevw - AF7TB, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
