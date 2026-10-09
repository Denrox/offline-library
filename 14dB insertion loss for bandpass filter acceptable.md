# 14dB insertion loss for bandpass filter acceptable?

*Tags: diy · score 5*

## Question

I'm busy with a direct conversion receiver for the 20m band, using a VXO and a 14.060 MHz crystal.

I designed a bandpass filter with the following components, using this design calculator.

Someone gave me a nanoVNA to check the shape of the filter and after calibrating I got the following result....  The shape looks fine, but the insertion loss is -14 dB and the SWR 1.4. **I wonder if this is typical and/or acceptable or if I can implement some improvements.**

Here is the Smith chart (I don't have any knowledge of how to read Smith charts)....

And lastly a photo of the filter I built....

Any comments and suggestions welcome.

## Answer (score 2, by glen_geek)

This filter design looks good, but you should be able to tweak it for less passband loss...  
A LTspice simulation of this double-tuned bandpass filter has been done with a guess for inductor Q of 156 on those T50-6 toroids. This requires adding a 0.9 ohm series resistor to each inductor.  
Imperfect components do two thing:

- Pass band loss gets worse
- Coupling capacitor (C5) needs a slightly larger value for critical coupling.

With perfect components in a critically-coupled filter, a 50-ohm generator and 50 ohm load will yield a -3dB power gain. That's the best you can do (half the generator power is dissipated in the 50 ohm source, and the other half of the power is dissipated in the 50 ohm load). Note that in this simulation, output *voltage* is plotted (not power), so a perfect filter would show a -6 dB gain.  
- With C5= 0.5 pf, this filter is under-coupled - a bit lossy
- With C5= 1.0 pf, coupling is near the critical point
- With C5= 2.0 pf, it is over-coupled resulting in a wider pass-band.

In this voltage plot, those lossy inductors yield a passband voltage gain near -10.4 dB instead of perfect -6 dB.

Dealing with 1 pf capacitors is a bit tricky, and trimming them is difficult. If you replace C5 with a tiny trimmer capacitor, coupling to other components can change tuning. For example, if you were to add a shield, you'd have to retune the whole filter.  
You can possibly add a "gimmick" capacitor in parallel with C5 consisting of two insulated wires twisted tightly together so that there is capacitance between them - the pair perhaps two or three cm long. It is easy to cut the pair to reduce coupling.  
An alternative: Replace C5 with a 3-capacitor network. Assume you have a spare 30pf trimmer. This can be used to trim the coupling between the two resonators:

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20934/14db-insertion-loss-for-bandpass-filter-acceptable, by Hans Fong, glen_geek. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
