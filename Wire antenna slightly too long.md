# Wire antenna slightly too long

*Tags: antenna-construction, wire-antenna · score 9*

## Question

Say I have a wire antenna that is slightly (a few percent) too long for the desired frequency (of resonance or lowest SWR). What are the options, other than cutting the wire(s) and very likely ending up with an antenna wire that is now too short (by miss-measuring, or when re-strung, moved higher, environment changes, etc.)?

Can I fold the tips or the wires into a small flat circle or figure 8 (similar to a perpendicular capacitive hat)? Or loop the wire near the feed point? Or coil wire around a dowel somewhere in the middle? Etc.

Added: Is the answer different if the wire is insulated?

## Answer (score 8, by Kevin Reid AG6YO)

You should not make any coil in the middle of the antenna as that will greatly change its RF characteristics. Instead, bundle up the wire at the ends in some fashion:


One practical solution is to fold the wire back on itself and fasten the free end onto the main line; then you have a loop you can also use for supporting the antenna, though you might want to use a “rope thimble” or other large diameter support to keep it from being sharply kinked, depending on the size and material of the wire and whether you expect to adjust it repeatedly. Electrically, this is mostly like using thicker wire, so it doesn't change the antenna characteristics much.

There is some dispute about how equivalent this is to a shorter wire if the wire is insulated. To be sure, you could remove the insulation where the end is joined on, but of course that may introduce other problems such as excess wear on stranded wire of a portable antenna. Or you could adjust the length until the antenna is a decent match regardless of whether cutting it would produce different results.


If you want something more adjustable and have support solved, wind the excess wire length at the ends onto a spool; this will form an inductor, but since the far end of that inductor is open circuit it can't have significant current flowing and so has minimal effect on the antenna. [There are existing antennas that work this way](What%20happens%20to%20the%20Yo-Yo%20Tenna%20when%20you%20coil%20up%20its%20ends%20for%20use%20on%20higher%20frequencies.md).

## Answer (score 5, by Mike Waters)

Simply fold the excessive lengths at the ends 180° back along the dipole and tape them to the antenna. It's that simple.

**[See this post, where insulated wire was used](Tuning%20a%20wire%20antenna%20by%20folding.md)**.

The other methods you mention may work, but the above is an easy, time-tested and effective method of raising the resonant frequency of a dipole.

I suggest against coiling wire around a dowel somewhere in the middle.

## Answer (score 3, by Old Pelican)

My technique for wire antennas is to twist an eyelet about 10-20% in from the end of each leg, and attaching the support rope there. Letting the dipole ends dangle down allows a much more convenient way for trial and error fine tuning the end loops, since the attachment doesn't have to be re done each time. Also, moving the highest voltage point away from the attaching rope and trees reduces rain detuning and loss from induced antiphase currents.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11805/wire-antenna-slightly-too-long, by hotpaw2, Kevin Reid AG6YO, Mike Waters, Old Pelican. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
