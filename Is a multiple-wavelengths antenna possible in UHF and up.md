# Is a multiple-wavelengths antenna possible in UHF and up?

*Tags: antenna, uhf, antenna-theory · score 9*

## Question

I know that in the High Frequency regions of the ham bands, the antennas have to be sub-wavelength because most people just can't put up a 160 meter full-size antenna.

Let's say we're in the 23 centimeter or an even higher band. Can the antenna lengths there be, let's say, twice, four times, etc., as large?

## Accepted answer (score 4, by Phil Frost - W8II)

People can, and do, put up full size 160m antennas. Usually "full size" means a 1/2 wavelength dipole, or a 1/4 wave vertical. The vertical works because the 1/4 element is "mirrored" by the ground plane, creating an image antenna, which makes it very much like a 1/2 wave dipole.

1/2 wavelength seems like a magic number because it is the minimum length required to attain resonance. Antennas can be made smaller and resonated by introducing additional, non-radiating reactive components like inductors or capacitors. However, shortening the antenna in this way makes the antenna less efficient.

Making the antenna *longer* than 1/2 wavelength isn't frequently done because in most cases there isn't much point to it. As the antenna first becomes longer than 1/2 wavelength, it stops being resonant. If made longer to 1.5 wavelengths, it becomes resonant again. However, it isn't any more efficient than a 1/2 wavelength antenna. In fact, it's likely *less* efficient, because the current must now travel over more antenna, which has more resistance.

What making the antenna longer does do is alter the radiation pattern. For example, compare a 1/2 wave dipole (in free space):

to a 1.5 wave dipole:

These are from antenna-theory.com.

Is this really useful? Usually no. One possible exception might be for verticals, where making the antenna longer (to a point, usually 5/8 wavelength) lowers the takeoff angle a bit.

## Answer (score 2, by K7AAY)

Yes, you could create, instead of a 1/2 wave dipole, a full wave dipole. They get very directional after you pass full-wave in length as shown in graphs at http://www.antenna-theory.com/antennas/dipole.php.

However, most folks instead use a collinear dipole array of multiple dipoles stacked, or side-by-side, or both, for gain.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1139/is-a-multiple-wavelengths-antenna-possible-in-uhf-and-up, by Skyler 440, Phil Frost - W8II, K7AAY. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
