# Ferrite Rod Antenna Array?

*Tags: antenna-theory · score 4*

## Question

The ferrite rod is a reasonably effective receiving antenna for LW, MW, and lower HF spectrum. It is well known that a ferrite rod is much more effective than an air cored coil of the same dimensions. An array of ferrite rods would receive more power if tuned and phased properly. If all the rods were bundled together would they act as one large diameter rod? If the rods were spaced many diameters apart they would be independent. How far apart is reasonable? Would a spaced array be better than bundled rods due to a bigger capture area?

## Answer (score 4)

Ferrite rods are smaller than loop antennas, but since the $Q_u$ (unloaded *Q*) is lower (200 is already very good as maximum) a copper or aluminium loop with same effective diameter ($\mu_r$ of ferrox material is about 130) and $Q_u$ of 500 for the loop is better. Dimension is indeed a factor larger; diameter goes factor $\sqrt {130}$ = factor 11,4 up for same aperture of H-field.

And to go back to your question: it makes a difference wheter the antenna is tuned or not. When tuned loops are within the range where coupling comes in the region of $k*\sqrt {Q_l}$ = 1 then the antennas have unwanted mutual effects. ($Q_l$ is loaded *Q*.)

When more loopsticks antennas are coupled with single tuning capacitor then you created a larger ferroceptor antenna: higher effective height and better reception, better sensitivity and lower noise floor. Noise floor on medium wave 1 MHz is seldom lower than 3$\mu$V/m in RBW = 3 kHz ("radio bandwidth"). Finally, when you make separate wideband antennas (no resonance, wideband noise matching) loop and ferroceptor loopstick antennas can be placed closer together.

Spaced array: coherence of signal is high within a wavelength separation. Local interference can vary. Last week I did a test with RSP-duo and 2 antennas and found only decorrelation for separation beyond 0,7$\lambda$; probably only beam forming from an array. PA0FSB

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15656/ferrite-rod-antenna-array, by Autistic. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
