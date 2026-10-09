# DIY 40m Antenna tuning: RLC and SWR

*Tags: antenna, antenna-theory, antenna-construction · score 4*

## Question

I keep hearing the recommendation to make your SWR as low as possible and that would imply good tuning.

I'm a new HAM and made a centre-fed half wave fan, 40m, 20, 15m. It works, and pretty well.

I tuned it with a NanoVNA and the SWR is about 1:1 - 1:2 for all bands I use.

But I suspect there's more to tuning than just SWR.

- Is the perfect antenna going to be (50+0j) Ω?
- Is it the imaginary part that changes the SWR?
- How do you get a piece of copper wire to change its resistance to get to 50 Ω if its not?
- How does all this fit together?
- If I mess with it enough, am I ever going to get close to (50+0j) Ω?
- Should I even care, if it works pretty well as is?

Edit: Its an inverted V on top of my house. The V is about 120 degrees.I have a 1:1 balun at the feedpoint.

## Accepted answer (score 7, by Ryuji AB1WX)

Excellent that you're using a NanoVNA and measuring **complex impedance** instead of relying solely on SWR. That's the bare minimum standard for modern antenna discussions. **SWR (Standing Wave Ratio)** is vastly incomplete; it doesn't even reflect antenna performance. For five decades (c. 1960s, when SWR meters became widely available to amateurs to 2010s), SWR was the only metric most hams knew, but the answer was always clear: **SWR tells you almost nothing useful about an antenna's actual performance**. Complex impedance does not tell anything about the antenna's performance, either, but it is a better window to observe how the antenna is working, from which we can tell at least something about the performance.

#### The Myth of 50 Ohms

First, where did the number **50 ohms** come from? It's almost arbitrary. **SWR only tells you whether the source and load impedances match,** nothing more, and that source 50 was actually chosen by the transmission line technocrat committee without consulting the antenna union (because their answers would be all over the map). The antenna's feed point impedance is shaped by the relationship between the radiator's length and the excitation frequency's wavelength, not the resistance of the copper wire itself. If the latter were the case, the antenna would be glowing in the sky, radiating light (well, heat is more likely), not HF radiowave.

#### Feed Point Impedance: The Real Story

The **feed point impedance** depends on how easily the antenna takes current and how much voltage it projects back as a result of forming a **standing wave** on the antenna element(s). This relationship is phase-dependent, captured in the **imaginary part of the impedance**. If the phase of the exciting current and the feed point voltage align perfectly, the antenna is **so-called "resonant"** (though not a true resonator). For antennas shorter than a quarter-wavelength, the impedance is typically **low and capacitive**, requiring a **loading coil** to cancel the capacitance. Even then, the feed point impedance may still be far from 50 ohms, necessitating a **matching network** for a 1:1 SWR.

The imaginary part of the complex impedance is the reactance. That's what indicates whether the antenna is capacitive or inductive. It absolutely affects the SWR. If it didn't, no one would bother with loading inductors.

#### Matching Antenna Impedance to 50 Ohms

There are many ways to achieve a 50-ohm match, but not all improve performance. Some methods introduce **losses** (e.g., resistive grounding or radials), which dissipates RF power in exchange for a prettier SWR, while others (like L-networks, gamma matches, or T-matches) can be uglier but usually are smarter. Automatic antenna tuners (ATUs; usually features an L-network) use relays to switch in capacitors and inductors, typically with losses well under **0.5 dB**. Antenna tuners don't fix bad antennas, but they can salvage a good antenna with a poor match by creating an impedance that matches the antenna.

Some antennas (like folded dipoles or double dipoles) naturally have much higher impedances but perform well with proper transformers.

What's the technical reason that made 50 ohm the standard? Ease of transmitting RF power over unbalanced transmission lines (coaxial cables). The diameter ratio of the inner and outer conductors, optimized for maximum power rating and minimum loss, leads to the characteristic impedance between 50 and 75 ohms (depending on whether you fill the space with air or plastic). Antenna had nothing to do with this decision.

#### The Real Damage of Poor SWR

High SWR means **power is reflected back** to the transmitter, stressing the final amplifier stage. At SWR=1.5, 4% of power is wasted (harmless for QRP, noticeable at 100W). At SWR=3, 25% is wasted. It's terrible for efficiency and RF amplifier's component longevity at 100W.

Even a 25% loss of the power is not much impact to the communication quality (barely noticeable on the S-meter). A 4% is practically nothing.

#### What Makes an Antenna *Good*?

**SWR and impedance tell you *absolutely nothing* about radiation efficiency or pattern.** A "good" antenna must:

1. **Radiate effectively** (minimize losses).
2. **Direct power where you want it** (horizontally, not straight up or down).
3. **Avoid unnecessary losses** (e.g., resistive elements in the radiating, radial or feed system).

A **dummy load** might give a perfect SWR but radiates nothing. A classic proof that SWR is meaningless without context.

Questioning SWR is wise, but that doesn't make SWR unnecessary. It is a bare minimum level check box and not a performance rating. Complex impedance is not a performance rating, either, but it offers more direct information about the operating condition of the antenna. And tools like the NanoVNA make this accessible. But remember: **antenna design is about radiation, not just matching**. Use tuners judiciously, and always prioritize efficiency and radiation pattern over SWR.

## Answer (score 5, by Louis Seaman)

@lornop, there's a lot to @Ryuji AB1WX answer, and certainly all valid and worth understanding, but just in case some of it is a bit beyond your current understanding, I'll give you a different take; if you got your Fan Dipole to an SWR of 2:1 or less, THAT'S PRETTY GOOD. In a horizontal or inverted-V dipole antenna, four variables are in play to minimize your SWR and get as close as possible to 50+/-0jΩ and those are:

1. Wire length of each leg of the antenna.
2. The offset of each leg (is the feed-point in the middle or offset?)
3. The height of the antenna above ground.
4. The angle of separation between the antenna elements.

So in a Fan arrangement you are presumably using antenna wire elements that are approximately 1/4 (or 3/4 for a harmonic band) wavelength for each band you want to be on, and each pair of wires is equal in length (there is a reason to offset the feed-point to raise the "real" part of the impedance, but it doesn't work well as a fan arrangement). The actual length of the legs largely determines the imaginary part (+/-j Ohms) of the impedance .

Next is height above ground, and on some of your bands you may find very good real (close to 50 Ohm) impedance, and on lower bands, you may be in the 30-40 Ohm "real" impedance range, and this is due to ground proximity in reference to wavelength of the signal.

The last factor is the angle between the two radiating legs; as you can see from the chart above, you could have a horizontal dipole where the impedance approaches 100 Ohms, the way to compensate for that is to droop the two the antenna legs toward the ground, symmetrically, and bringing them closer together will lower the impedance. Could you narrow the angle between them on the horizontal plane? Yes, but you will have less of an omni-directional pattern, and your signal will favor one direction over the opposite direction, and if that works for you, then great. You just need to use some antenna modeling software to get a handle on how to arrange the elements. Here is free software with built-in antenna example to get you started: [https://www.eznec.com/]

You might experiment with arranging the element pairs at different angles to each other, keeping each set separated horizontally by 180 degrees, but distributing the pairs around like ribbons on a Maypole if you have the room and the ability to tie them off at various points.

The last point I'll make is in regard to an antenna tuner. While 2:1 SWR doesn't mean your antenna can't radiate most of the energy sent to it, it does mean that your radio transmitter may not be able to send all of its power to the antenna. An antenna tuner makes a conjugate impedance match between the radio, and the feedline (coax), since while they are both 50 Ohms, if your antenna is not a perfect 50 Ohms, the antenna is reflecting a portion of the energy you're trying to transmit, back to the radio, and an antenna tuner reflects the reflection back to the antenna at the correct phase (that's what a conjugate match is) and increases the power that the antenna must radiate, so even if 10% of the energy is reflected, the reflected reflection is increased roughly by 10%, forcing more power into the antenna. (Total radiated power remains the same, less coax losses) And if there are losses, it is largely due to the resistance and other characteristics of the coax cable, which are typically minimal. But this makes your transmitter operate efficiently because it is getting a 50 Ohm impedance into the antenna tuner, and the tuner is matching the signal energy on the coax that was reflected by the impedance mismatch at the antenna; this re-reflection creates a "larger" signal which has a greater total energy on the coax because a consistent percentage of power is constantly being reflected by the antenna due to the impedance mismatch. So 2:1 SWR and even greater is fine, but in practicality, only if you have a tuner. This power increase on the coax can be easily seen if you place a power meter between your antenna tuner and the coax that goes to the antenna; as you "tune" the antenna tuner for the lowest SWR as far as what your radio "sees" into the tuner, you will observe your forward power on the meter on the output of the tuner increase beyond what your radio is putting into the tuner.

## Answer (score 3, by hobbs - KC2G)

Is the perfect antenna going to be (50+0j) Ω?

That will be the perfectly *matched* antenna, with the minimum feedline loss. It's not necessarily the *perfect* antenna. A dummy load is 50+j0 too, and any time you see an antenna that has a "nice flat SWR" over a broad bandwidth, it's a fair bet that it has a bit of dummy-load in its ancestry.

Is it the imaginary part that changes the SWR?

It's both, but SWR changes a lot *faster* with reactance than resistance, and when you're tuning a wire antenna that's not far from resonance, the reactance changes a lot faster with length than the resistance does. Those two things put together mean that the point of zero reactance tends to be awfully close to the point of minimum SWR.

How do you get a piece of copper wire to change its resistance to get to 50 Ω if its not?  
If I mess with it enough, am I ever going to get close to (50+0j) Ω?  
Should I even care, if it works pretty well as is?

Last question first: nope! A practical approach for a dipole is simply to tune it so that the minimum SWR is in the middle of the band (or the middle of the segment you want to operate on), and then check the values at the edges. If they're good, you're done. With a dipole, you should pretty much always end up in a place where almost any transmitter will be happy and your feedline losses won't be excessive. Your minimum SWR will probably be 1.2 or 1.3, not 1.0. That's not even remotely an issue.

But say you're dealing with some other sort of antenna design that "natively" has a feedpoint impedance further from 50 ohms. A folded dipole or a full-wave loop might be several hundred ohms at resonance. An EFHW might be several thousand. Some kinds of Yagis might be 20-25 ohms. And you'll probably never build a 160m vertical tall enough to have more than a few ohms of resistance.

In those cases, some kind of transformation or matching comes into play. A "4:1 balun" or "49:1 unun" is a transformer that steps an impedance up or down to a more convenient value. A gamma match, delta match, or shunt feed is a kind of "one-turn transformer" built in to the antenna structure that we can tap at a point that gives a feedpoint impedance we want. And then there are LC matching networks, which can be placed at the antenna (to match the feedline), or at the shack (to match whatever comes off of the feedline to 50 ohms). A combination of parallel and series elements will change the magnitude of an impedance, besides adding or subtracting reactance. Different options have different tradeoffs in efficiency, convenience, cost, size, power handling, etc.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23816/diy-40m-antenna-tuning-rlc-and-swr, by lornop, Ryuji AB1WX, Louis Seaman, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
