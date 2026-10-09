# Can I reduce RFI/noise at the antenna?

*Tags: antenna, hf, rfi, snr · score 31*

## Question

Recently, the power was out in my neighborhood for an extended period of time. I fired up my HF rig using battery power and was amazed at the lack of noise across the HF bands.

When the power grid came back online, the noise returned. The difference was drastic. S2 vs. S9 drastic.

With that said, is there a good way to reduce RFI/noise at the antenna? Specifically a dipole antenna? Is there a better way to solve this problem?

The houses are packed so close together in my neighborhood, the likelihood of eliminating the noise at the source(s) is nil. For reference, the type of "noise" I'm hearing is more of a white noise rather than a noise pattern coming from an interfering appliance. (Though, I do hear RFI with a pattern to it from time to time on certain bands as well.)

## Accepted answer (score 18, by Phil Frost - W8II)

First, I'd be sure it's actually the antenna picking up the noise, and not something else. [If you don't have a balun on that dipole](Using%20a%20balun%20with%20a%20resonant%20dipole.md), probably your feedline is picking up all the noise in your house.

Any other wires attached to your receiver can also make good noise antennas, especially the power cord, which is attached to your home's wiring, and coupled to all the noisy stuff running on it. Get some ferrite beads designed for EMI control, and start snapping them on any wire attached to the receiver. Keep snapping them on until you stop getting improvement.

If you have cooperative neighbors, do the same to their noisy electronics. Ferrite beads work for keeping EMI out of your receiver, and also for preventing it from leaving the source in the first place.

Once that's done, the next thing is to get the antenna as far away from other noise sources as possible. Powerlines, neighbors, etc. Put it on the tallest tower allowed in your neighborhood. In urban areas, your options are limited, but do what you can.

The rest is just trying to null the noise based on its direction, or it's polarization, or something else. Every antenna has a particular polarization and radiation pattern. You don't know the same of your noise sources, but just by playing with the orientation of the antenna you might by chance find an arrangement that works well. Try not to be parallel to power lines, etc. A directional antenna helps, but is probably impracticably large at HF.

At this point, you are running out of options. Some of the noise is in the far field of the antenna, and there just isn't much you can do about this besides move.

Other noise is in the near field, which at HF, can be quite big. In this region your antenna isn't acting as an antenna, but rather one winding of a transformer, or one plate of a capacitor.

There is one additional game you can play here that might help. Remember that electromagnetic radiation is made of two fields: an electric field and a magnetic field. In the far field, these two are inseparably linked, related by the impedance of free space. However, in the near field, you can have a strong electric field and a weak magnetic field (capacitors), or vice-versa (transformers).

You can build different antennas which, at some distance in the near-field, have a different sensitivity to one type of field or the other. W8JI has a good article on small loop antennas, and describes this in some detail. In particular, there's this great graph:

A high impedance means the antenna is more sensitive to electric rather than magnetic fields. So, you can see that if your noise source is very close (less than 10 meters for this antenna) and is largely E-field noise, you'd want a loop.

However, keep in mind:

- the impedance of all antennas are *identical* and equal to the impedance of free space (377Ω) in the far-field. This only makes a difference for noise sources in the near-field, which couple to your receiver by mutual inductance or capacitance, *not* EM radiation.
- the impedance changes up and down in the near-field with distance, and if a particular antenna seems to have less noise, it's due to chance and your particular noise source's characteristics, not some magical "noise immunity" intrinsic to some antenna design.

That said, most people already have dipoles, so if they find them noisy, sometimes they have luck switching to a loop, which provides a complementary near-field impedance, and just might be better in a particular environment.

## Answer (score 2, by pu3hag)

Another approach would be nulling one signal (say: your neighbor's plasma TV) to allow other signals to come over. Devices known as "noise cancellers" or "phasers" do exactly this.

Try searching videos demonstrating MFJ-1026, Quantum Phaser and Timwave ANC-4 to have an idea how they work.

They have some constraints:

a) they can only null one signal at a time. You will either null the Plasma TV or the cell-phone charger jamming;

b) they have narrow bandwidth, you will have to re-tune every time you move 10-20KHz away;

c) they require a 'sense' antenna that capture the interfering signal. In practical terms, you would need to have a second antenna outside.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/606/can-i-reduce-rfi-noise-at-the-antenna, by The Driver, Phil Frost - W8II, pu3hag. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
