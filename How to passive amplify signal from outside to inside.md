# How to passive amplify signal from outside to inside?

*Tags: antenna-construction, antenna-system · score 3*

## Question

I have a house in the mountains, with very thick walls (they are old-fashioned houses). Outside the balcony, I get the full 4g signal, while just inside, I get almost nothing. I would simply use 2 passive antennas, one hanging from the balcony railing, and one just inside the first room. I would like to use two antennas like this, using a coaxial cable. It might work ? In Italy the frequency of 4g, depending on the operator is: 800mhz and 2600mhz. Thank you

## Accepted answer (score 4, by Kevin Reid AG6YO)

Yes, in principle, this type of system can work. However, it will not give very much benefit unless you use the right sort of parts, because a lot of signal is lost to simply heading in the wrong direction, and by adding two more antennas you're adding two more places that happens.


The outdoor antenna should be a directional type (parabolic, Yagi, log-periodic, or such) which is pointed directly at your local cell tower, so that you have good antenna gain.


The indoor antenna you show needs a ground plane. You can either use a dipole antenna instead, or construct a ground plane. If you do not do either, it will function poorly and you will not get as much benefit from the system.

A ground plane (in this context) is simply a piece of sheet metal, at least 1/2 wavelength ( $c\, /\, 800\,\mathrm{MHz} = 0.38\,\mathrm{m}$ ) in diameter (it does not need to be a circle, but that is the smallest good shape), which the antenna is mounted to the center of (so the antenna is on one side and the coaxial cable is on the other side). The mounting would be done by using a SMA coupler that has a nut and flange so that you can bolt it down to the hole in the sheet metal, then attach the antenna and coax to the two sides. It does *not* need to be “grounded”, connected to the earth, but that won't hurt. You can also use a ring of metal rods (“radials”) instead of a single sheet, if that is easier to fabricate or more aesthetic for you.


The coaxial cable will also introduce some loss, which you will want to minimize:


When choosing cable, check its specifications for loss per length, at the *highest* frequency you care about (2600 MHz in this case). Cables with lower loss will often be thicker, and may come with larger connectors than SMA.

(For this application you might reasonably choose antennas and cable with N connectors rather than SMA; they are sturdy, high-performance, and weather resistant.)


Use the shortest length of cable that can reach where it needs to.


Do not bend the cable sharper than its specified minimum bend radius; this will cause it to reflect the signal.

Careful choice and usage of each of these components will increase the overall gain of your system.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22010/how-to-passive-amplify-signal-from-outside-to-inside, by stighy, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
