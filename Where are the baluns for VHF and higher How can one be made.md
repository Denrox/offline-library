# Where are the baluns for VHF and higher? How can one be made?

*Tags: vhf, uhf, balun, filter · score 18*

## Question

In [another question](Unexpected%20Resonance%20-%20Dual-Band%20Dipole.md), commenters recommended that I look into adding a 1:1 balun to a dual-band dipole to eliminate the feedline as a radiator. As I understand it, a 1:1 balun also functions as a choke, but is more efficient because... reasons?

When I try to find plans to build a balun, they all seem to specify a frequency range of 1.6-30MHz. Why is that and how can I make a balun that will work on VHF and UHF?

## Accepted answer (score 10, by Phil Frost - W8II)

Let's clarify some terminology: a balun is any device used to convert between a balanced system (ladder line, dipoles) and an unbalanced one (coax, vertical monopoles). There are a lot of ways to make a balun, and a common-mode choke is one of them. A choke can also be used in balanced to balanced, or unbalanced to unbalanced connections where suppression of common-mode currents is merited.

The choke approach (or "current balun" as you'll sometimes hear it described) is nice because it's small, easy to fabricate, broadband, and low-loss. "Small" is especially an advantage on HF where other balun designs would be huge.

Ferite-wound chokes can be done on VHF as well. Jim Brown, K9YC has some measured data on ferrites. Look for page 49. His data show that Fair-Rite mixes 31, 43, and 61 can all be made to work. He shows for a T240 core of any of those mixes, you can get about 600Ω on 2m with 2 turns, and 300Ω with one turn on 70cm.

However, the effective permeability of ferrites drops with increasing frequency, so it becomes difficult to get a sufficiently high choking impedance for the choke to function effectively as a balun. 300Ω isn't great but might be sufficient for some applications. You can always [measure and see](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md).

Alternatively, VHF wavelengths are small enough that other balun designs become practical.

One approach is to keep the system unbalanced all the way. If you have an unbalanced coax feedline, then put an unbalanced monopole antenna on it.  
By F1jmm - Own work • Self-photographed, CC BY-SA 3.0, Link

The three drooping wires are the "ground plane". Drooping them increases the feedpoint impedance from the 37Ω of a monopole on a flat ground plane to 50Ω for a better match. Since the ground plane presents a very low impedance to the ground currents, that's where most of the current will flow. The coax common-mode is a relatively high impedance.

Some antenna designs which aren't simple monopoles use a "skirt" which looks like radials on a monopole. As in the monopole, the skirt looks like a low impedance ground plane, and the feedline is "hidden" under it.

Other designs are the [folded balun](How%20does%20a%20folded%20balun%20work.md), and the folded dipole. These designs work by getting the coax to attach at a ground potential point, while creating such a point through some clever arrangement.

A [sleeve balun](How%20does%20the%20length%20of%20a%20metal%20sleeve%20around%20a%20%28shieled%29%20coax%20cable%20affect%20antenna%20performance.md) is another possibility. It uses a quarter-wave stub to insert a high impedance in the common-mode.

There some antenna designs out there that claim no balun is necessary. Sometimes it's true (the balun is intrinsic in the design) and sometimes it's not. Look for an antenna model that contains a feedline such as W8JI did with the J-pole. Or build the antenna and [measure the common-mode current yourself](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7225/where-are-the-baluns-for-vhf-and-higher-how-can-one-be-made, by William, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
