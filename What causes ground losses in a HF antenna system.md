# What causes ground losses in a HF antenna system?

*Tags: grounding · score 9*

## Question

This applies to mobile and fixed installations. What are ground losses, and how can they be minimized? It seems to involve proximity to the ground, but what is the mechanism that causes loss? Does antenna installation height influence ground loss in any way?

## Accepted answer (score 7, by Phil Frost - W8II)

To add to what Dan is saying, for (horizontal) *dipole* antennas, ground height is important because although a dipole doesn't require ground to work, ground is still a (lossy) conductive plane, and you still get an image. That is, it appears that there's another dipole, fed in anti-phase, underground. Even if nothing in your transmitter or antenna is connected to the ground, your antenna will be capacitively coupled to the ground. There is no avoiding it.

If the dipole is close to the ground, then the currents in the ground can be quite strong, incurring significant resistive losses along the way. You could put radials (or any conductive mesh, really) in the ground to mitigate this.

But also: this image makes your dipole a kind of phased array. Depending on the spacing of the antenna and it's image, this might make a phased array that helpfully directs most of the RF energy at the horizon (low takeoff angle, desirable for HF DX exploiting skywave propagation), or unhelpfully straight up (useless, unless you are trying to exploit NVIS propagation on communicate with something in space).

*Radio Antenna Engineering* has a more detailed explanation, and this:

One interesting thing to note about this image: you can't get maximum gain in *any* direction until the dipole is $0.25\lambda$ high. Remember, the image is twice this distance away, and anti-phase. Below this height, in any direction you will get at least partial phase-cancellation. At $h=0.25\lambda$, you have two antennas, in anti-phase, $0.5\lambda$ apart, which makes the *add* instead of *cancel*, but only if you are directly over the antenna, which isn't useful for skywave propagation. Thus, the general recommendation to get a dipole something like $0.5\lambda$ high, which sends *most* of the energy at a reasonably low take-off angle, making the best of the transmit power available.

## Answer (score 7, by Dan KD2EE)

While ground effects are common concerns in almost every antenna and radio system, they are particularly important in the case of a monopole antenna. Monopole antennas, including quarter wave verticals along with many other electrically short verticals, are different from dipoles because the currents going into the elements do not balance. While a dipole has equal but opposite currents at all times, a monopole can't. One half of the signal goes into the antenna, and the other half has to come back through the shield of the coax, which is connected to ground.

When we're talking about antenna modeling, we describe the ground plane as an image plane - everything above it is mirrored below it. So in theory, the monopole should act as though there was another monopole directly below it, being fed 180 degrees out of phase. We do see the correct amount of current returning through the ground path for this model to work - we do have equal but opposite currents - but while your antenna is low-resistance wire and most of that current is being radiated, the ground typically has somewhat higher resistance. It's impossible to set a value here, because it is dependent on soil type, weather, how deep the water table is, and other factors, but it is greater than that of your antenna.

Because of this resistance in the ground, some of the power coming from your radio will be lost to normal resistive heating. Since, at a constant power and given $P=VI=I^2R$ the increased resistance in the ground results in decreased current into the ground (at constant power). Since the antenna and ground currents must be equal but opposite, that also decreases the current flowing into your antenna and therefore your actual radiated power.

You also can't just stick a multimeter into the ground to find this resistance - it's the resistance from your antenna feed point to the point where the coax shield is grounded, but it is frequency dependent because there is a capacitive component as well. An antenna analyzer can be used to detect the total resistance (including radiation resistance of the antenna) and this can be compared to a model with an ideal ground (perhaps obtained from EZNEC or another modelling program) to get the "extra" real-world losses, including ground loss. This also explains why height factors in: Your antenna system is effectively a series resistance (from ground loss and other factors), capacitance (between antenna and ground and other effects), and inductance (from loading coils and other effects). If the antenna is mounted further from ground, the capacitance decreases, and so the ground loss becomes a greater part of this total reactance, which is why it is better to have your antenna near to a ground and to have a ground that is as low resistance as possible. An extra way to help this is to install radials - wires underground at about a quarter wavelength which would act as a lower-resistance path for the return current to take.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/484/what-causes-ground-losses-in-a-hf-antenna-system, by Bill - K5WL, Phil Frost - W8II, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
