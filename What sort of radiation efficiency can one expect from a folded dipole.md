# What sort of radiation efficiency can one expect from a folded dipole?

*Tags: antenna, antenna-theory, efficiency, folded-dipole · score 9*

## Question

It is pretty well established that [folded dipoles have much greater acceptable-SWR bandwidth than ordinary dipoles](Why%20do%20folded%20dipoles%20have%20greater%20bandwidth%20than%20ordinary%20resonant%20dipoles.md).

Radiation efficiency is simply the quotient of radiated power to the antenna feedpoint input power.

Seeing that folded dipoles are able to achieve the greater bandwidth [without introducing a designed-as-lossy element](How%20does%20a%20folded%20dipole%20work.md) (a technique not unheard of with large-bandwidth antennas), **what is the effect on radiation efficiency of using a folded dipole as opposed to a regular dipole?** Are there any considerations affecting folded dipoles that would not affect a regular dipole antenna erected in the same physical location which would have a noticable impact on the radiation efficiency?

For the purpose of this question, assume otherwise identical conditions; identical height over ground, identical ground, identical possible parasitic elements, identical feedline, etc. Also, note that I am not asking about the radiation pattern of the folded dipole; I am *only* concerned with the antenna's radiation efficiency here, unless some other factor has a noticable impact on the radiation efficiency as compared to a regular dipole.

*A great answer* would look at this from both the perspective of a same-wire-length antenna (meaning approximately double the folded dipole's physical length) as well as a same-physical-space antenna (meaning effectively half the radiator length).

## Accepted answer (score 6, by Phil Frost - W8II)

For all practical purposes, the radiation efficiency of a folded dipole versus an ordinary dipole is the same. Consider, they are essentially the same antenna.

The only difference is that in the folded dipole, we've replaced the feedpoint with a short. Since the Thévenin equivalent resistance of a voltage source is 0Ω, this doesn't make a lick of difference to the currents in the antenna. The currents are the same, the fields are the same. Everything is the same, except that the voltage source now sees only half the current.

So then, what is there that could affect radiation efficiency? There is nothing. There might be some difference in ohmic losses, depending on if you allow the folded dipole to have twice as much copper or not, but this is a very small contributor to loss.

More significant for terrestrial antennas is ground losses in the Earth, but having established that the fields around a dipole and a folded dipole are the same, how could the losses be different? They aren't. The same reasoning applies to any other kind of loss.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1903/what-sort-of-radiation-efficiency-can-one-expect-from-a-folded-dipole, by user, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
