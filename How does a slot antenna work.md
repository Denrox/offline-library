# How does a slot antenna work?

*Tags: antenna, antenna-theory · score 9*

## Question

How does a so-called slot antenna work? How can one construct one? What might be the radiation pattern and efficiency compared to a wire antenna?

And, if a small slot antenna "works" at mobile phone cellular and radar frequencies, would a very large hole with proper (slot) dimensions in a large enough building (barn, aircraft hanger, office tower) work for some HF bands?

## Answer (score 5, by Phil Frost - W8II)

If we cut a hole in an infinite conducting plane, and feed it with a voltage source across the center, we get a slot antenna:

Because the slot is between the sides of the voltage source, the currents must travel around the slot. These currents traveling over a large distance are what make it an antenna and not a Faraday screen.

Babinet's principle, with some refinements from H.G. Booker, relate the slot antenna to a dipole. If, instead of a hole we have a conductor, and we make a very small cut in the center of this conductor so we can put a voltage source across it, we have a dipole. This dipole will be very similar to the slot, except:

- magnetic and electric fields are exchanged,
- as a consequence of the above, polarization is rotated, and
- the feedpoint impedance is different.

The impedance of the slot antenna ($Z_S$) is related to the equivalent dipole ($Z_D$) by:

$$ Z_S Z_D = { \eta^2 \over 4} $$

where $\eta$ is the impedance of free space, about 120πΩ. So if the impedance of a long, thin, half-wave dipole is about 72Ω, then a long, thin slot has an impedance of about:

$$ {(120\pi\:\Omega)^2 \over 4\cdot72\:\Omega } \approx 493\:\Omega $$

If the slot is made wider, this is equivalent to making a dipole thicker, and it has the same effect: increased bandwidth and decreased length at resonance.

In practice, we don't make slot antennas out of infinite conducting planes since infinite planes are so hard to find. A sheet that was many wavelengths big, such that there was negligible current far away from the slot, would be a good approximation. However there wouldn't be much point to it: the equivalent dipole would be smaller. Perhaps most of the slot antennas of this type are undesired, such as interruptions in the ground plane of a PCB, or undesired holes in something that should be acting as a shield.

For slots that are made to be intentional antennas, they are usually slots in a waveguide or a box. Of course this changes the radiation pattern and the impedance, and the feed is not a voltage source directly across the sides but provided by the currents in the waveguide, but the basic mechanism of how they work remains the same.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3531/how-does-a-slot-antenna-work, by hotpaw2, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
