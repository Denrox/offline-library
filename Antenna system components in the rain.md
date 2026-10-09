# Antenna system components in the rain

*Tags: antenna-system, weather · score 4*

## Question

An antenna system often consists of more than the feedline and radiating wires: such as fixed or tapped loading coils, LC traps, baluns, toroids, air variable capacitors, roller inductors, feed horns, reflector dishes, poles, standoffs, mounting hardware, etc.

What happens when this stuff gets wet? Which parts requires waterproofing and which do not? When does the entire antenna system need to go in an enclosed dome? And when will it all just work on the roof of a truck in a downpour?

## Answer (score 4, by Phil Frost - W8II)

A lot of things will work electrically when wet, as long as the water film is thin relative to the size of the thing. For example, a wet dipole, no problem. A tiny coil where water droplets can short adjacent turns, not so much.

Water getting in coax, either the feedline, or as part of a balun or trap, is a problem. The water will wick down the shield, causing corrosion and dielectric loss. The coax is ruined. Best practice is to terminate the coax with connectors, then waterproof the connections with mastic or rubber tape.

Water facilitates corrosion. Galvanic corrosion between dissimilar metals happens faster with water. Sticking to one kind of metal (don't connect aluminium and copper), or using corrosion resistant metals (stainless steel), or protective coatings (paint) are often easier than avoiding all water.

Water is only part of the problem: in many climates snow and ice must also be considered. A coil may not be a problem in rain, but may be sufficient for sticky snow to accumulate in it. A thin film of water may not be significant, but packing a coil with wet snow could be a problem. Furthermore, freeze-thaw cycles can cause mechanical stress and eventual failure, especially in ferrite which is slightly porous. Accumulated snow and ice can increase the weight of antenna systems beyond the structure's capacity.

At microwave frequencies, the dielectric loss of water is more significant, and the dimensions of a water droplet approach something significant relative to wavelength.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15122/antenna-system-components-in-the-rain, by hotpaw2, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
