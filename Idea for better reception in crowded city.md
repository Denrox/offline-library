# Idea for better reception in crowded city

*Tags: antenna, receiver · score 3*

## Question

I am living in crowed area of a city. It is impossible for me to set up an antenna outside the apartment. I receive signal inside the room.

I have a funcube dongle pro+ and some RTLSDR, the picture shows the antenna I am using:

Any suggestion on improving the reception by using other antenna of similar size or amplifier?

## Accepted answer (score 6, by Kevin Reid AG6YO)

You have a tough problem, because you are surrounded by many noise sources.

First, you should make sure that you have eliminated **your own apartment's noise**, because it is likely to interfere no matter what antenna you use.


Try shutting off all electronic equipment (including e.g. fluorescent or LED lights, and power adapters plugged into the wall) in your apartment, and use a laptop **on battery power with no other equipment connected** for receiving. If this cuts down the noise to a worthwhile degree, then you can start looking for individual problematic devices. In some cases, placing ferrite beads on cables connected to the noisy equipment can help (make sure they are appropriate for filtering the frequencies of the noise).


The computer the dongle is attached to can itself be a source of noise. Try using a different computer. Try connecting the dongle to a self-powered USB hub instead of directly from the computer, and move it away from the computer.

Now, if your primary noise sources are not nearby, here are some antenna-based approaches for getting more signal and less noise:

1.

Use a **directional antenna pointed at the transmitter**, thus attenuating all noise sources which don't happen to be in the same direction as the transmitter.

This requires you to know where to point the antenna — if you're trying to receive transmissions from moving vehicles, for example, it will not help. It will also not work as well indoors since the surrounding building will affect the effective pattern.

2.

Use an antenna which is significantly better at receiving the desired signal *frequency* than other frequencies — that is, have the antenna act as a **filter**. Your receiver hardware already contains a filter to suppress signals outside the band you tune to, but no filter is perfect, so you will always get some out-of-band leakage. Using an appropriately tuned antenna also improves the antenna's efficiency at collecting the desired signal.

Since you specify "30-400 MHz", which is a very wide band, this implies an antenna which is *adjustable*, tunable, in some way. A telescoping whip as seen on portable FM radios is a common example of such an antenna; a telescoping whip with an adjustable loading coil is even narrower; there are also loop antennas which are tuned by variable capacitors, and many other possible designs. (The antenna you have is a fixed-length whip with a fixed loading coil.)

If you have a tunable antenna and a SDR receiver, there is a simple way to determine when you have it adjusted correctly: watch the noise floor of the spectrum and adjust until it is at a *maximum* — ideally, there should be a visible hump with a peak at your desired frequency and dropping off elsewhere, but whether you can actually see the hump on-screen depends on the bandwidth of the antenna being smaller than the bandwidth of your spectrum plot. (Yes, it sounds funny to be tuning for maximum noise, but the antenna doesn't distinguish in-band signal from in-band noise, so we're also tuning for maximum signal.)

Unfortunately, using a tunable antenna is somewhat in conflict with the above option of using a directional antenna, because directional antennas have more complex shapes with multiple dimensions that must be adjusted for the desired frequency, else they will not have the expected radiation pattern.

3.

**Receive the noise and subtract it.**

This method is good when there is a single, known noise source, and works by using a secondary antenna which is set up to receive the noise source better than your primary antenna. The signal from this antenna is then subtracted from the main antenna's signal (or rather, added but opposite in phase), thus removing that specific noise source. This requires equipment to provide phase and amplitude adjustments to obtain good cancellation — the MFJ Enterprises MFJ-1026 is an example (I am not recommending this product).

This method is fundamentally the same thing as building a specialized directional antenna optimized for not receiving the noise source, but more modular and adjustable.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2211/idea-for-better-reception-in-crowded-city, by Harold Chan, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
