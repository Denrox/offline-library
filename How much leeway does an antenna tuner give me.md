# How much leeway does an antenna tuner give me?

*Tags: hf, dipole · score 3*

## Question

As far as I can tell, currently a 20m dipole has to be within a few inches to have a reasonable SWR without a tuner. How does this change with one? Does it depend on what tuner I have?

## Accepted answer (score 1, by Marcus Müller)

Generally, the accuracy you need is directly proportional to the wave length.

Thus, for 20m band (==20m wavelength), let's say 3% percent of that wavelength would be in the region of "less than half a meter error, and you're fine".

But: which accuracy you'll need depends on which mismatch you can tolerate. "A few inches" however sounds wrong – you're not using this antenna for a single fixed frequency, where there would be a theoretical "optimum" length, but for the whole band, so there's a range of frequencies you'll want to work with, and for all but a single one of these, your antenna will inherently be non-optimal, but it doesn't matter, because the slight mismatch (the slightly increased SWR) doesn't really hurt you all that much.

Yet another warning: SWR isn't really number you're aiming for. It **is** a useful measure for testing how well something is matched, but in the end, if I attach a 50Ω terminator to my receiver, I get a (damn near) perfect SWR. And receive exactly (damn near) nothing.

Your antenna has a resistive (non-radiating) component, too, and by matching to that, you improve your SNR, but you decrease your radiation efficiency. Luckily, that component should be small for metal conductors at these frequencies.

What you need, in the end, is an antenna system, and that incorporates doability, the mechanical aspects of temperature and wind tolerance, the feedline, eventually baluns and stuff, and you need that antenna system to work relatively well for all that you want to do. Good SWR is just one of the aspects of that; appropriate position to actually pick up EM energy, durability and cost of the build as well as boring aspects such as it being somewhat hard to actually cut down 10m of cable to a high degree of length accuracy and spanning it in a straight-as-possible line do play a larger role, in many installations.

Now, to your actual question:

How does this change with one (an antenna tuner)? Does it depend on what tuner I have?

Yes.

Let's look at RX only, TX is analogous, just the other way around:

So, what an antenna tuner is, is really a matching circuit between the impedance of your antenna at the frequency you want to operate at, and the receiver you're using (typically, 50Ω).

Since the impedance is (at least for a dipole) always depending on the frequency, you adjust the tuner to convert exactly the impedance of your antenna at the frequency you want to 50Ω. That makes energy at that frequency come through without losses from antenna to receiver. Other frequencies are mismatched, so they inherently experience reflection at the tuner, and don't end up in your receiver. That's a filtering effect you get for free!

Notice that for resonant antennas, this usually means that if you consider your antenna to be an inductivity, you adjust a capacitor until the antenna-tuner LC circuit is in resonance at exactly the frequency of interest.

So, the amount of frequency "variability" a tuner gives you actually depends on the amount of reactive/capacitive loading it can provide *compared to the antenna*; also note that typically, antennas work reasonably well for frequencies that are exact integer multiples (with the integers that work depending on the antenna type) of their fundamental frequency (but they do have a different directive pattern there).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9119/how-much-leeway-does-an-antenna-tuner-give-me, by Stephen, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
