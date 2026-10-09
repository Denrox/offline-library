# Does a loop antenna have less susceptibility to atmospheric noise than an open ended antenna?

*Tags: antenna-theory, dipole, noise, small-loop · score 5*

## Question

I always get the feeling that an antenna which has a loop for the driven element such as a folded dipole or quad will pick up less static or 'high impedance' noise than an antenna that has free ends such as a dipole or long wire. Noting that atmospheric noise probably doesn't have an impedance.

The reason I have this idea is as follows.

A short piece of thick wire 2 inches long which is used to short out the ends of a transmission line isn't going to pick up anything, right? It has a low DC resistance and at HF a low radiation resistance, and noise in the atmosphere is going to have a hard time inducing any current in it because it's a very low impedance short compared to the easily manipulated seemingly high impedance of the noise. So a loop antenna is like a tame version of the 2 inch short.

Whereas in contrast, the ends of a dipole (for example) are high impedance because the current is zero (R = E / I) and so you get the feeling that noise will be able to have an effect or 'pull' the voltage at the ends of the dipole more easily because the dipole ends are not a low impedance.

It this thinking correct?

## Accepted answer (score 6, by Phil Frost - W8II)

Your reasoning is not too far off.

Say you attach a signal generator to an antenna, and then probe the magnetic and electric fields at many places around this antenna in a test chamber. The ratio of the electric field strength to the magnetic field strength is called the *field impedance*.

For *any* antenna, several wavelengths away (in the far field), this ratio will be approximately 377 ohms (an ohm is a volt/ampere). This is a physical constant called the impedance of free space.

But closer to the antenna, the field impedance can vary by design. Let's compare a dipole that's small relative to wavelength, to a loop of similar size. Very close to the antenna, the field impedance for the dipole will be high, and low for the loop. And the intuitive explanation is as you expect: the loop is a short circuit, and the dipole an open circuit.

By reciprocity, the field strength measured when the antenna is transmitting is also proportional to its sensitivity when receiving. So very close to the antenna, the short dipole will be better at detecting electric fields, and the small loop will be better at detecting magnetic fields.

Paradoxically, at some intermediate distance which isn't very near the antenna, but is also not far enough away to be in the far field, the situation reverses. W8JI has this great graph:

If the vertical axis were logarithmic, these two antennas would each have a field impedance that's the mirror of the other. This is an example of duality.

You asked specifically if loops have reduced sensitivity to *atmospheric* noise, and the answer is *no*. Since such noise is in the far field of the antenna, a dipole and a loop will perform identically if all else (efficiency, polarization, feed arrangement, height above ground, etc) are equal.

However especially on HF, there can be quite a lot of noise in the near field of the antenna. Since the near field impedance of these antennas are quite different and complementary, it is often the case that a loop does not pick up the same noise sources that a dipole does.

You also mention a *folded dipole*, so I emphasize the above explanation works only for dipoles or loops which are *small* relative to wavelength. Folded dipoles are often a half-wavelength long, that is, the size of resonant ordinary dipoles. Other than the higher feedpoint impedance, they work just like ordinary dipoles. Just why this is merits a question of its own: [How does a folded dipole work?](How%20does%20a%20folded%20dipole%20work.md)

## Answer (score 2, by Cecil - W5DXP)

An ungrounded antenna element is subject to precipitation static (P-static) buildup that can result in arcing. At least one element of a dipole is usually without a DC ground reference while if one conductor of the transmission line to a loop antenna is grounded, P-static cannot build up to cause an arc. P-static can be caused by dust, snow, or rain and usually occurs under low humidity conditions, e.g. the Arizona desert around Phoenix. For more information about P-static, please do a web search.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13256/does-a-loop-antenna-have-less-susceptibility-to-atmospheric-noise-than-an-open, by Andrew, Phil Frost - W8II, Cecil - W5DXP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
