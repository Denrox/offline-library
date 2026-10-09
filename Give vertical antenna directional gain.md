# Give vertical antenna directional gain?

*Tags: antenna-theory, vertical-antenna, gain · score 4*

## Question

So here is a strange thought. If a vertical electrically speaking is a half dipole with the other half as a ground plane to balance out. Perhaps there are ways to make equivalent director and reflector make it into a vertical yagi? Is that a possibility?

I know that it might be difficult to do, but low take-off angle without height and with a directional gain is an advantage.

I heard that when you run radials into a general direction, you also get some gain into that direction, not sure how much that would effect.

## Accepted answer (score 4, by Cecil - W5DXP)

I took the EZNEC VERT1.EZ 40m model and added an identical passive element 27 feet away connected to the same miniNEC ground. Here are the results. 4+ dBi gain at a TOA of 24 deg. But this leads to another question. How does one implement a miniNEC ground in the real world?

To equal the above performance over high-accuracy ground, each element needs two radials elevated at 10 feet, one to the NW and one to the SW.

Note that the lowest SWR (1.6:1) occurs at 7.3 MHz but the highest gain occurs at 7.12 MHz where the SWR is 2.5:1.

## Answer (score 7, by tomnexus)

Sure, that can work.

Here's a monopole yagi I designed:  
Photo: Alaris Antennas MONO-A0005.

It's a half-yagi for remote control of a mine locomotive, improving the control range by firing one way down the tunnel. The driven element is a half-folded-dipole, a good match for 50 Ohms. Also, it's welded up from solid 20 mm steel so it survives low ceilings, cable snags, etc. It's for 915 MHz but the principle is the same at HF. A good ground screen will be required.

There is also a half-log-periodic antenna, sometimes called an LPMA. It's a fairly standard thing at HF, but takes up a lot of room for hams. Here's one from R&S for 1.5-30 MHz, 97 m long and needs a 90 m mast.

You'll find designs for directors or reflectors for monopoles out there. One neat trick is that you can switch direction with some relays to jump between being the driven element and being the reflector.

## Answer (score 3, by Brian K1LI)

Not a strange thought, at all, with several interesting solutions described over the years. The information below is **not** presented as a construction idea: elements are #14 wire and lengths are approximate. The antenna is simulated over "real" ground of "medium" conductivity (Sommerfeld model), with the lower set of elevated radials .05$\lambda$ above ground and .01$\lambda$ vertical separation between the radial sets to prevent shorts. More engineering would have to be done to result in a practical design.

Just as you would with a horizontal yagi, a lengthened vertical parasitic reflector (wire 6) could be added to a driven vertical (wire 1):

The horizontal spacing between the vertical elements is 0.15$\lambda$, the driven vertical and the radials (wires 2-4 and 7-10) are 0.24$\lambda$ long and the parasitic element (wire 6) is 9% longer than the driven element, producing some gain and useful directivity (elevation plane shown):

Alternatively, you could change the *electrical* length of the parasitic element by adding reactance to it. Instead of changing the *physical* length of the parasitic vertical, a 550nH inductor, similar to what one might use as a loading coil for a matching network, is added to the base (note the square at the base of element 6):

again with some gain and useful directivity (elevation plane shown here):

Sadly, modeling does not show useful directivity when replacing the inductive reactance with capacitance in an effort to make the loaded parasitic reflector into a director, so there is some limit to the flexibility of this approach. However, one could swap the driven and loaded connections to reverse the pattern.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14501/give-vertical-antenna-directional-gain, by Matthew Wang, Cecil - W5DXP, tomnexus, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
