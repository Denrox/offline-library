# Will measuring SWR through a feed line mislead me?

*Tags: impedance · score 5*

## Question

I know that except in the perfectly matched case, transmission lines transform impedances along their length; if I measure the impedance at the other end of my feed line, or even with a short jumper between my antenna analyzer and the antenna, I won't be reading the true impedance of the antenna (or other device at the end of the line).

**Will the impedance transformation ever make an actual mismatch “look good” (1:1 SWR)?**

## Accepted answer (score 4, by Phil Frost - W8II)

In an ideal world, if the characteristic impedance of your transmission line matches the system impedance (usually 50Ω), then adding or removing lengths of transmission line just moves the complex impedance around a constant-SWR circle. So you may get a different impedance (it may look capacitive instead of inductive, etc), but the SWR will always be the same, regardless of how much transmission line is between your meter and the antenna.

However, the real world is not ideal. Firstly, if the transmission line is lossy, that will make the SWR better. It does so because the transmission line absorbs some of the transmitted energy, and then absorbs again the reflected wave. No reflected wave means 1:1 SWR. Absorbing all the energy is one way to reduce the reflected wave.

Secondly, there are a great many amateur antenna designs which, intentionally or not, [use the feedline as part of the antenna](Using%20a%20balun%20with%20a%20resonant%20dipole.md). These antenna currents on the feedline are called *common-mode currents*. When they exist, the feedline is very much part of the antenna, and changing the feedline length can change the impedance of the antenna, just like changing the length of any of the other antenna elements would. For this reason and many others, good antenna designs do not have significant common-mode currents.

## Answer (score 3, by Kevin Reid AG6YO)

**No,** the SWR will remain high (in fact, constant) no matter how much line there is between the meter/analyzer and the antenna, assuming the line is matched to the meter.

An argument that this must be the case, skipping the math:

1.

Instead of considering the impedance of the antenna and how it is transformed along the feed line towards the transmitter or meter, work from the other direction. The transmitter has a standard 50 Ω (or whatever) impedance, and the feed line also has a *characteristic* impedance of 50 Ω, so we know the impedance observed at the other end of the line itself must be 50 Ω.

2.

Therefore, if the antenna feed point has an impedance other than 50 Ω, there is a mismatch at that junction. During transmission, this mismatch will, as mismatches do, reflect some of the signal, which will propagate all the way back down the feed line, and be observable at the transmitter end.

3.

Therefore, if we substitute the analyzer for the transmitter, it will detect the mismatch.

You won't see the same *complex impedance* as you would without the line in the way, but you'll see the same SWR.

There is a caveat here: the feed line has some loss, and that loss will tend to make the mismatch look less bad because it absorbs power in both directions, resulting in less reflection. But if you have a significant amount of such loss, then you have a worse problem than bad SWR.

If you did want to compensate for the effect of the transmission line, or generally to visualize this situation, the tool for that is a Smith chart. On a Smith chart, for this purpose:

- The center point corresponds to the characteristic impedance, and all other points to different impedances.
- Distances from the center correspond to SWR.
- Adding a length of transmission line corresponds to rotating by an angle about the center of the chart.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5098/will-measuring-swr-through-a-feed-line-mislead-me, by Kevin Reid AG6YO, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
