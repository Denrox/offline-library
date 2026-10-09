# What is the maximum number of turns in a ferrite core used as a common mode choke?

*Tags: ferrite, choke-balun · score 7*

## Question

Is there a way to estimate the maximum number of turns which can be used with a ferrite core used as a common mode choke?

It is known that the impedance of such a choke is proportional to the square of the number of turns and so there is a strong incentive to use multiple turns. But it is also known that there is a limit due to what looks like a sort of resonance phenomenon and, once that limit is exceeded, increasing the number of turns has either no influence or negative influence.

There is an excellent paper on the subject by Jim Brown (K9YC) ( http://audiosystemsgroup.com/RFI-Ham.pdf ). Unfortunately, his maximum frequency of interest is about 100 MHz and my application is VHF and UHF. [edit: this sentence is wrong]

The ferrite core manufacturers provide excellent information for impedance of a single turn at different frequencies. This can be used to estimate the impedance when using multiple turns, so long as the limit is not reached; that limit could be as low as 1 turn!

I am willing to buy bunches of cores and measure them, but it would seem to be more efficient if I could somehow estimate an ideal geometry and use that as a starting point. For example, if the limit is due to core volume, maybe lighter cores would be the preferred starting point. Or if it is somehow related to diameter or circumference, then perhaps a smaller, wider core would be better.

## Accepted answer (score 8, by Phil Frost - W8II)

The K9YC paper you mention gives data up to 1 GHz on page 49:

These data show for these core types the maximum number of turns is just one or two. Furthermore, it's quite difficult to achieve a choking impedance above 1 kΩ. That's not very much, and for many applications you'd want more.

To get a higher choking impedance will require a larger core, and so ferrite chokes can become quite expensive at higher frequencies. For this reason it's often worth considering [other techniques](Where%20are%20the%20baluns%20for%20VHF%20and%20higher%20How%20can%20one%20be%20made.md) to supplement or replace them.

## Answer (score 5, by Glenn W9IQ)

The primary issues with coax wound common mode chokes are;

1. The inductive reactance of the choke can cancel out the capacitive reactance associated with the feedline shield thereby worsening the CM situation
2. The resistive component of the choke is not sufficient such that the core undergoes an undesirable temperature rise
3. The interwinding capacitance forms a self resonant circuit which reduces the choking action

At VHF and UHF frequencies these pitfalls can be even more exasperating as windings become a significant fraction of a wavelength and the selection of suitable core materials diminishes.

You may wish to examine other methods of common mode suppression such as 1/4 wavelength sleeve baluns or transmission line baluns before attempting the coax on a ferrite choke approach. But if you care to pursue some lab work with ferrites you may find the VNA measurement method used by Steve G3TXQ to be helpful. His published work is for HF baluns but the measurement technique should be extensible to the higher bands.

What you are mostly likely to find, however, is that there is no number (minimum or maximum) of coaxial turns on a ferrite core that will make an adequate CM choke at frequencies above 100 MHz.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10126/what-is-the-maximum-number-of-turns-in-a-ferrite-core-used-as-a-common-mode-ch, by Chris K8NVH, Phil Frost - W8II, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
