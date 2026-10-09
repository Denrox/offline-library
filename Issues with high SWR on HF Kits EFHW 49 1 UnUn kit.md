# Issues with high SWR on HF Kits EFHW 49:1 UnUn kit

*Tags: antenna, antenna-construction, wire-antenna, balun, efhw · score 3*

## Question

I recently tried assembling a EFHW kit, and some problems came up in testing. I believe this is the kit; I bought it through ARRL: HF Kits website. This is my first time making an UnUn and EFHW kit.

For this I have a nanoVNA running 10 segment sweeps on the UnUn with two gator clips on each end. Between the gator clips sit one 100 ohm resistor and two 1.2k ohm resistors which my Fluke tells me gives about 2420 ohms of resistance, which is close to the 2.4k ohms resistance I've seen used in YouTube vids to test this.

The results leave a lot to be desired. SWR is between 6 and 14 on a sweep with a nanoVNA when done between 7Mhz and 30Mhz. Obviously this is nowhere near what it should be if it's resonant on 40-10m bands.

I'm looking at the windings in particular. One of my two main windings crosses over the top of the other. Would that be a problem? I *think* I have 14 turns around the toroid here. I've got the little capacitor in there for the higher frequency bands, though it does look like some of the coating cracked in an effort by my to get everything to fit correctly. Otherwise continuity checks out with everything showing continuity to everything else. I also noticed that I had a weak solder joint on the PL-259 connector. That should be easy to fix, but I'd like to do any toroid rewinding before resoldering it.

What am I not seeing here?

Here's some photos of my work.

resistors:  general setup:  primary windings:  nanoVNA:

## Accepted answer (score 1, by Moron)

This appears to be a wiring error. There are two wires on the SO239 center conductor—likely one for the primary coil and one for the capacitor—and only one wire connected to ground, which seems to be the other side of the capacitor. There should be three wires on the ground terminal: one from the capacitor, one from the coil primary, and the third should be the secondary coil winding. It seems the primary and secondary coil was left open or misconnected. Below is the correct wiring.

Disregard post, I fell for it again, a 3-year-old post no one will read.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20716/issues-with-high-swr-on-hf-kits-efhw-49-1-unun-kit, by nerdenator, Moron. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
