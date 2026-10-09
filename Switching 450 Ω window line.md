# Switching 450 Ω window line

*Tags: electronics, feed-line · score 3*

## Question

I have a very old Harvey Wells Z-Match antenna tuner (transmatch) with two outputs on the back for 450 Ω window line. One output is for “medium frequency” and works for 75 and 40 meters. The other output is marked “high frequency” and works for 20 meters and up.

Currently switching the window line back and forth is a pain, since I have to break out a wrench and unscrew terminals. So I have three questions:

- How can I efficiently switch this back and forth?
- Am I correct in assuming that connecting two antennas at once is a bad idea?
- Would soldering PowerPole connectors to segments of window line create impedance problems, and are they up to the voltages and currents experienced in a piece of window line?

## Accepted answer (score 3, by Phil Frost - W8II)

Would soldering Power-Pole connectors to segments of window line create impedance problems?

On HF, no. The significance of an impedance mismatch is proportional to its size in relation to wavelength. For HF the wavelength is so much more huge compared to a connector that the impact is negligible.

are they up to the voltages and currents experienced in a piece of window line?

If you are using 450 ohm line, and transmitting with 100 watts, Ohm's law tells us:

$$ V = \sqrt{ P \cdot R } = \sqrt{ 100\:\mathrm{W} \cdot 450\:\Omega } = 212\:\mathrm V $$

That's an RMS voltage; the peak voltage is 1.4 times more, or about 300 volts. If you are operating the line with a high VSWR, the voltage could be higher.

With that in mind, read the datasheet for the particular connectors you are considering and see what their limits are.

Am i correct in assuming that connecting two antennas is a bad idea?

Usually, yes. However in some circumstances multi-band antennas are made by connecting multiple antennas to the same feedpoint, fan dipoles for example. Not recommending you try connecting two antennas, just an interesting fact.

How can I efficiently switch this back and forth?

You can just use a switch. Just be sure to check its voltage and current ratings (using Ohm's law) make sure it's rated appropriately. I'd build in a very healthy margin to account for high VSWR and other things which could make voltages and currents higher than in the ideal case. And you might want to take steps to avoid touching the switch when transmitting: RF burns are painful.

## Answer (score 2, by K7PEH)

I had a similar situation once with window line and I merely used a knife switch (double-pole) to handle the switching duties. Worked quite well. Nice thing about window (or, ladder) line is that it can be easily cut, switched, patched, and so on without too much disturbance.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6199/switching-450-o-window-line, by Arthur, Phil Frost - W8II, K7PEH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
