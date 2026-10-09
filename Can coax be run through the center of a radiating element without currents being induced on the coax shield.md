# Can coax be run through the center of a radiating element without currents being induced on the coax shield?

*Tags: antenna-theory, antenna-construction, dipole, vertical-antenna, feed-line · score 5*

## Question

I run a λ/2 vertical dipole for 20M that's fed to a 1.5:1 balun at its center with coax that is perpendicular to the dipole (parallel to the ground), for about 30 feet before it comes down to the shack. I wanted some opinions about what would happen if I ran the coax into the center of the lower λ/4 radiating element, if say that element were a copper pipe? I use a balun and get excellent VSWR across the entire band currently, but I wonder if running the coax through the lower element would induce current on the coax shield, and cause the shield to radiate outside the lower element, and of course, back to the radio. The other problem I was thinking about is changing the radiation pattern substantially. Here's a picture of the current setup, now picture the orange wires are copper tubes, and the lower element has the coax going through the tube to connect to the balun box.

## Accepted answer (score 1, by hotpaw2)

If a feedline isn't centered in a balanced antenna's near field, it can couple into the EM near field, pick up induced currents, and thus distort the pattern.

If you feed the feedline into a quarter wave length pipe segment of a half wave dipole, the end exit of that pipe will be a very high voltage node at resonance that can capacitively couple to the feed line shield at the pipe exit. Even a disconnected wire around that high voltage node can pick up induced currents, so a choke in that vicinity may not be very effective.

## Answer (score 5, by Phil Frost - W8II)

That is a great idea. In fact antennas of this design are quite common, and you probably have a much smaller antenna of similar construction on your Wi-Fi router:

Effectively, the lower dipole element, which is a tube, forms a "bazooka" or "sleeve" balun. See also W8JI's description of sleeve baluns. I'll let you follow the links for more detail, but briefly this construction creates another coaxial transmission line around the coax, with the coax shield being the "center" conductor, and the dipole element being the shield. By virtue of being a quarter wavelength long this transmission line is able to convert the short at one end (the feedpoint) into a high impedance at the other end.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18673/can-coax-be-run-through-the-center-of-a-radiating-element-without-currents-bei, by Louis Seaman, hotpaw2, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
