# Which is better in my situation: Balanced dipole, or as much wire as possible in the air?

*Tags: antenna, wire-antenna, feed-line, antenna-system · score 6*

## Question

I'm finally getting to the point of hopefully putting up a HF antenna. The idea is to start with a simple, straight wire dipole using trees as support points. (No traps or coils.)

However, with the layout of my property and the location of the trees thereon, putting up a fully balanced antenna might be difficult.

I'm not aiming for an antenna that is resonant on any particular frequency to begin with, so will be using an ATU in any case. I'm also going to be operating on most of the HF bands, so the feedline will essentially be random length at least on *some* relevant frequencies.

I'm aiming more for local-ish contacts than DX; with what I'm planning to do right now I won't really be able to get the antenna up high enough to get the takeoff angle down far enough for DX anyway.

The general idea for station setup is to have the transceiver, then 50 ohm coax to the ATU (which in turn is just inside the window, and which has a built-in 4:1 balun), then attached to its binding posts balanced ladder line (through the window) which eventually splits into the two legs of the antenna to actually radiate the signal. There will also be a bleeder resistor somewhere along the length of feedline, to help reduce the buildup of static, and a physical/electrical disconnection point between the bleeder resistor and where the feedline enters the house (allowing for true electrical disconnection of the antenna when I'm not on the radio). I'm aware of the need to keep balanced ladder line away from other conductors that it could parasitically couple to (as e.g. [Hamsterdave illustrated just recently](Why%20aren%27t%20there%20baluns%20that%20do%20BOTH%20balanced%20unbalanced%20transformation%20and%20common%20mode%20current%20attenuation.md), though perhaps not quite as extreme).

With such a setup, **which approach is *likely* to lead to better operating results, as well as less problems with RFI and friends?**

- As much antenna wire in the air as possible, disregarding the relative feedpoint, *possibly* leading to an off-center-fed antenna?
- Keeping the antenna as balanced as possible, even if this means less wire in the air?

Bonus if answers also touch on how the choice is likely to impact antenna tuning (it'd be nice if I don't have to retune every 10 kHz).

The ambient HF noise level, as far as I have been able to determine by completely unscientific testing, is quite low, and I'd love to be able to make the most of that.

## Answer (score 5, by Phil Frost - W8II)

I think in practice you'll find it doesn't make much difference as long as there's a common mode choke or "current balun" at the feedpoint. In fact, if you get it off-center in just the right place you can get an impedance around 200 ohms on several bands. Even though you'll be using an ATU, there's a limit to how much mismatch they can tune out, and feedline losses go down with decreasing SWR.

When the feedline isn't in the middle of the dipole, the impedance between the common mode of the feedline and the two legs of the dipole are unequal, so you end up with common-mode currents on the feedline. This isn't much different from the situation with a coax feedline. Just use a choke.

The balun in the ATU does take care of interfacing with the ladder line, but it doesn't do anything about the feed arrangement: you still need a choke up there if you want to prevent common-mode current on the feedline, thus effectively making the feedline part of the antenna. At 100W or less you'll probably not get any RF burns, but it does mean your antenna is within a few feet of noisy electronics like computer monitors and switching power supplies in your shack. Not the best for receive performance.

A couple more points of note:

If the intention in disconnecting your antenna is to protect from lightning damage, you'll need more than a little gap in a switch to do it. See W8JI on grounding systems (The "Isolating or Disconnecting feed lines" section in particular) and [How can I protect equipment against a lightning strike?](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md)

Your antenna setup is not going to have any effect on RFI with your neighbors except to the extent that you radiate less energy (not usually desirable in an antenna), put it farther from the neighbors, or direct the radiation pattern away from them. Feeding the dipole in the center or not will make no difference.

Once you have a 1/2 wavelength of wire in the air, more isn't really a benefit.

or is it a balbal in this case? Or a unbal? Amateur terminology is so confusing.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6478/which-is-better-in-my-situation-balanced-dipole-or-as-much-wire-as-possible-in, by user, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
