# What determines power handling capacity of an antenna?

*Tags: antenna, rf-power · score 10*

## Question

I just bought a cheap 1/4-wavelength, 2m. mag-mount antenna. The package says it can handle 50 watts. I can think of three things that could limit the capacity:


$I^2R$ losses in the connection to the feedpoint and in the antenna wire itself: increases with increasing current, produces gradual breakdown of materials;


dielectric heating at the feedpoint: increases with increasing voltage and frequency, produces gradual breakdown of materials;


dielectric breakdown at the feedpoint, happens suddenly when voltage is too large, produces immediate failure.

Are these right? Are there others?

## Accepted answer (score 6, by Phil Frost - W8II)

I think you pretty much summarized limiting factors in the general case. I'd add that there can be dielectric losses or breakdown at the ends, as well as the feedpoint. Common antenna designs (quarter-wave verticals, center-fed half-wave dipoles) are fed at a low-impedance node, and the ends are high-impedance nodes, so I'd expect dielectric breakdown (arcing) to be more likely at the ends than the feedpoint. At high power levels, the antenna ends can reach voltages high enough to cause arcing to nearby conductors (towers, trees, gutters) or corona discharge. Unlikely at your 50W example, however.

I'd also consider RF exposure. Consider that this is is a VHF antenna, and that exposure limits are lower with increasing frequency. Also consider that this antenna isn't installed in a fixed location, no one is going to test the RF exposure levels, and there's nothing preventing anyone from getting close to the antenna. In fact, given that most people will stick them to cars, it's not only possible, but *likely* that someone will be close. So, the manufacturer may specify a power limit due to regulatory or liability concerns.

## Answer (score 5, by WPrecht)

Cheap mag mounts, like many physically short antennas, have a coil in them to make up the correct electrical length. I am sure it's made with the finest materials available. But it's probably not. Even if it was, inexpensive means smaller gauge wire, cheaper connectors, etc. And so driving it at higher than it's rated capacity is going cause it to heat up and the dielectric is going to breakdown and melt until you get a short.

And of course, all the heat is power that isn't leaving the antenna, so your efficiency is poor too.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/724/what-determines-power-handling-capacity-of-an-antenna, by Pete NU9W, Phil Frost - W8II, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
