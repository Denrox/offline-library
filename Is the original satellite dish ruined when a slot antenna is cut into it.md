# Is the original satellite dish "ruined" when a slot antenna is cut into it?

*Tags: antenna-theory · score 5*

## Question

A fun vertical antenna can be made by cutting a horizontal slot in a satellite dish, as documented in e.g. http://www.w6nbc.com/articles/2016-3QSTdishslot.pdf and discussed in [How does a slot antenna work?](How%20does%20a%20slot%20antenna%20work.md) and other questions here. But how would this modification affect the *original* (satellite receiver) antenna system?

Of course, trying to use both antennas simultaneously would run into practical concerns — aiming of the dish necessary for satellite reception vs. what would be ideal for a station's desired 2m pattern, whether the LBNF and/or satellite receiver would appreciate being party to a 25W ham signal, etc. But all the same, I'm curious if/how the slot affects the parabolic reflector itself.

I know that a reflector needn't be completely solid, and can work with a metal mesh or even a wider grid/skeleton of wires. So is a narrow slot — surprisingly effective at its own VHF frequency — also totally insignificant at the EHF frequencies? Or does a long continuous hole affect the aperture efficiency more than losing equal surface area via small disconnected holes would affect it?

## Accepted answer (score 6, by tomnexus)

I think the antenna will probably work OK as a satellite dish.

There are two effects to worry about:

1.

Loss of reflecting area:  
A slot is a lot worse than a hole or series of holes, because the hole is long and continuous. The loss of reflecting area is approximately the area of the hole itself, plus a fraction of a wavelength all around it - perhaps 1/4 wave. In this area, the radiation couples to the slot itself and is scattered in all directions, in front of and behind the dish. At Ku band, 25 mm wavelength, this makes the hole about 5% of the dish area, which is insignificant. Perhaps 10% when the feed radiation pattern is taken into account - it illuminates the centre much more strongly than the edge.

2.

Increase in antenna temperature:  
Noise from the warm ground will leak into the feed through the hole. The LNB is normally looking only into the cold sky, so the unmodified antenna temperature might be in the order of 50-100 Kelvin (guessing as I can't quickly find specifications, but we know it's well below 300 K as it easily detects your warm hand).  
The increase in system temperature will be in the order of 10% of 300 K or about 30 Kelvin. This is slighly more serious problem, it could reduce the SNR of a certain satellite by 1 or 2 dB. It's still likely to work.

Note that both of these apply only to the polarisation *where the electric field is perpendicular to the gap*, vertical in your photo. Horizontally polarised waves are reflected perfectly even in the region of the slot, if it's less than $\lambda/5$ or so. Because the satellite polarisation is dual linear and fairly arbitrary, not aligned with the slot, the effect of the slot will probably be split between the two polarisations.

Both effects could be reduced by including a Ku-band choke along the slot - a quarter-wave deep slot formed by a pair of parallel lips extending out of the back of the dish. These wouldn't make much difference to its VHF characteristics.

The MeerKAT antennas have ~ 5 mm gaps between their panels. Here's a backlit photo from the daily mail / AFP / Getty  
  
There's a small amount of noise leakage, not enough to justify covering the gaps.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20700/is-the-original-satellite-dish-ruined-when-a-slot-antenna-is-cut-into-it, by natevw - AF7TB, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
