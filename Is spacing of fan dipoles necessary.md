# Is spacing of fan dipoles necessary?

*Tags: antenna-construction, parallel-dipole · score 4*

## Question

Is spacing of parallel dipoles necessary. Could they be banded together and then trimmed or is there some consideration, other than tuning, requiring separation.

I was considering a fan dipole. I have seen one where 300 ohm twin lead was used for two dipoles and I believe a 2nd piece for another 2 dipoles, all fed from a single line. I haven't seen one of those in use but assuming it worked (it's in the antenna bk) the spacing is about 1/2".

## Answer (score 3, by Mike Waters)

**Spacing is *absolutely* required between the antennas.**

You cannot bundle all the wires together. They must be spaced apart, or the interaction between them will be too great. You'll have a mostly useless "multiband" antenna.

Some of these search results indicate the need for spacing, as does [this question](3%20Band%20%2880-40-20%20Meter%29%20Fan%20Dipole%20Tuning%20Question.md).

## Answer (score 3, by pidloop)

In my experience no need for any spacing at all. I've made 80-10m fan dipoles with ribbon cable. Yes, the wires interact but after tuning I got nice clean resonances on all bands. Start with the shortest wavelength first and work down.

Just my $0.02.

## Answer (score 2, by rclocher3)

You don't say if you're talking about several dipoles connected together into a single antenna, which is an arrangement usually called a [fan dipole](3%20Band%20%2880-40-20%20Meter%29%20Fan%20Dipole%20Tuning%20Question.md), or several nearby dipole antennas that each have separate feed lines.

If you consider a piece of metal up in the air near a transmitting antenna, it is not difficult to imagine that the metal absorbs some of the RF from the antenna, which induces currents in the metal, which cause the piece of metal to re-radiate RF at the same frequency. The radiation pattern from the piece of metal interferes with the radiation pattern from the antenna, constructively in some directions (more gain) and destructively in others (less gain). So if the piece of metal is close enough to the antenna to absorb a meaningful amount of energy from the antenna, then one can see that the radiation pattern and impedance of the antenna are affected. That's how a yagi antenna works; a yagi is just a dipole (the "driven element") with a few metal rods ("passive elements") cleverly placed near it in a way that enhances gain in one direction. The same principles work in reverse for receiving, so if an antenna has more gain when transmitting in a certain direction, then it typically will have more gain receiving from that direction also. (There are exceptions.)

So a fan dipole is a bunch of dipoles cut for different frequencies that are strung near each other, and connected at the middle. (If you were to tightly band the dipoles together they would mostly act like a single dipole made with the longest wire, and not like a multi-band antenna. The wires in a fan dipole are typically held some distance apart by spacers.) Fan dipoles work, but if you were to build one by making several individual dipoles and then connecting them together, then you would find that the impedance and radiation pattern at one of the old resonant frequencies has changed quite a bit. They typically need careful adjustment of the lengths of all the wires, and the spacing between the wires, to have low SWR at the right frequencies. That's one of the main drawbacks of fan dipoles, that they need lots of careful tweaking to work well.

If you were talking about several dipoles with individual feed lines near each other, then similar considerations apply. The closer the antennas are together, the more they will interact with each other. (I've heard several closely-spaced antennas described as "a single antenna with multiple feed ports".) The more they interact, the more the radiation patterns and impedances will change, and the more they will need to be tweaked to work well together.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17933/is-spacing-of-fan-dipoles-necessary, by mike zias, Mike Waters, pidloop, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
