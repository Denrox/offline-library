# Improving VHF airband reception

*Tags: software-defined-radio, vhf, rtl-sdr, airband · score 3*

## Question

I'm trying to receive VHF airband transmitted from a nearby airport via RTLSDR and having a hard time doing so. Obviously the stock antenna is useless in this situation. I tried building a quarter-wave ground plane antenna but that didn't improve reception much. Only overhead planes are heard well, controller is barely audible, and so is the ATIS frequency. Roof access is also a hard one, so I'm limited by what I can receive from my window.

What are the important factors when trying to improve VHF airband reception? What will get me the best reception without going crazy with expensive antennas/parts?

## Accepted answer (score 4, by Kevin Reid AG6YO)

Controllers and ATIS are transmitting from the ground, so they're always harder to receive because terrain, trees, and buildings are in the way. The best thing you can do to improve your reception is **move your antenna as high off the ground as you can**, to reduce the density of line-of-sight obstacles. If you can't put it on the roof, at least hang it from the ceiling for a minor improvement.

The best antenna for your purpose would be a **“high-gain” vertical antenna**. Such an antenna has a pattern which is more flattened — it has more gain in the horizontal plane at the cost of lesser gain at higher angles. Since your current system performance is unbalanced in the other direction, it should be an overall improvement.

After setting up the best antenna you can, you want to improve your receiver's *signal-to-noise ratio*.


First, make sure you have **set the hardware AGC *off*** (there should be a checkbox for this in whichever software you are using), because the RTL's AGC doesn't work well for these applications (it runs too high). Then find a good setting for the manual gain control (e.g. pick an ATIS station you can barely hear, and listen for the best audio).


Check for local broadband noise sources. Try turning off electrical equipment (including non-incandescent light bulbs!), and watch the spectrum to see if the noise floor (‘everywhere there isn't a signal’) reduces in intensity. Find out if there's a culprit you own and can replace or turn off when you want to listen. **Try a different computer** in case you have a particularly noisy computer.


If you find that there is no significant local noise — in particular, if the noise floor doesn't rise above the level you get with the gain turned all the way down or the antenna disconnected — then you are in the “lucky” position of having a good signal-to-noise ratio but weak signals. This means that you can benefit from **a better receiver** — in particular one with a higher ADC bit depth than the 8-bit RTL-SDR. This will appear as reducing the receiver's internal noise floor.


Alternatively to the previous option, or if you *do* have local noise but can move the *antenna* away from it, you can use a **low-noise amplifier (LNA)**. This is a device which is installed right at the antenna, and amplifies the signal at that point so that it is much stronger than the noise internal to the receiver (or leaking into the receiver from nearby equipment or out-of-band).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6158/improving-vhf-airband-reception, by Yuval Adam 4X5UV, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
