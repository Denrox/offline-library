# 2m Biquad - Why not?

*Tags: antenna, echolink · score 4*

## Question

I'm thinking about putting together an Echolink link node on my local repeater frequency so I can participate in the weekly net when out of town. This seems straightforward as it's simply:

Being in an HOA, I have to try and keep my house from looking like an antenna farm / porcupine, so I thought "why not a panel antenna?" I figure I can build the elements out of 10AWG solid wire and place it on a vertical surface outside my house, paint it with leftover house paint, and it should be nicely unobtrusive.

Is there a reason not to build a biquad for such a purpose? Is there a better (less observable, easier to build, ...?) antenna for connecting from one known point to another?

I considered a simple dipole, but there's no good way to mount it and I have rain gutters on the side of the house that faces the repeater. A biquad, being relatively flat *and* vaguely directional, seems like an ideal solution to this particular task.

## Accepted answer (score 2, by Phil Frost - W8II)

Why not indeed. A biquad sounds like a fine solution, with the only caveat that on 2 meters (145 MHz) it will be significantly larger than the 2.4 GHz constructions typically seen. The size of the panel is on the order of one wavelength, so you're looking at something approximately 2 meters square. At that size you may want to construct the panel from a cage of wires, as a 4 square meter sheet of copper will be a little expensive.

The other difficulty is mounting the antenna high. Due to line-of-sight propagation on VHF, once the antenna is beyond the radio horizon, path losses increase sharply. This is because you must now rely on scattering off other objects to get your signal across.

So, given the option of mounting a panel antenna down low on the side of the house, and mounting a smaller antenna up high, I'd opt for the latter.

For example, HTs often come with compact antennas which are smaller than the 1/4 wavelength that would be required of a resonant monopole. Such an antenna, say mounted on your gutters for a ground plane, and painted to match your roof, may be sufficiently small that it will go unnoticed.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9192/2m-biquad-why-not, by William, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
