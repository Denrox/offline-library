# What happens to a vertical Yagi when you mount it on a vertical metal pole?

*Tags: antenna-theory, antenna-construction, yagi · score 3*

## Question

How much difference does a metal pole make when it's sitting in the middle of all the lower elements of my beautiful new highly optimized to the max YO.EXE 10 m yagi ?

I get it that the closeness of the pole will mess up the impedance a bit.

But the elements are still there in the right place with the right length constructively adding to and destructively subtracting from the incoming signals (for example) and after a few tests it seems that a metal pole makes less difference that you might think.

Does it just affect the radiation pattern in the elevation plane ? Can anyone tell me if actually a metal pole which only goes up to the boom lowers the angle of radiation .. imagine that ! a rare case of owning an antenna cake and eating it at the same time :o

## Accepted answer (score 4, by Mike Waters)

Mounting a vertically-polarized Yagi on a vertical conductive mast usually screws up the pattern. You either have to use a non-conductive mast, or offset them from it with a horizontal boom.

40 years ago, Cushcraft sold an 11 element beam designed for 146 MHz. Not realizing this, I (and countless other hams) mounted it on top of a steel mast. That caused so many extra lobes that it made a better omnidirectional antenna than my ground plane! It still had a useful forward lobe, but those that mounted it as described above had a much cleaner pattern.

## Answer (score 5, by tomnexus)

You definitely don't want to mount a long metal pole through a Yagi. My rule of thumb is that it at best cuts off the Yagi at that point, perhaps worse.

You have three options to avoid this.

1.

Mount the Yagi at its back, perhaps supporting the front with a non-conductive rope. The mast can get quite close to the reflector, 1/8 wave is ok.

2.

Offset it from the mast with a bracket that's perpendicular to the plane of the Yagi. Exact length required is hard to say, but at least half a wavelength, maybe more. The Yagi is a slow-wave structure, its capture area at the front is large, perhaps 1 wavelength square for a 10 dBi antenna. Halfway along the boom the sensitive region is smaller.

3.

Use a non-conductive pole. I used many filament wound fiberglass poles for this purpose. Again, you probably want a half-wavelength clearance from the boom, but a third of a wavelength will work. The coax of course can't go in the tube, so it has to hang down from the very back, somewhat behind the director.

It is possible to put the coax in the pole if it's adequately loaded with ferrites. At 30 MHz I'd use a string of about 50 beads, 1.5" long, 1/2" dia, 1/4" hole, made of material 31, big enough for RG223 or RG58 to fit. You could also use three or four larger cores of 61 material, 1 m apart, wound with 6 turns of coax.

Finally, as you're only looking for a narrow band, you might be able to design some sort of quarter wave trap, several of them in series, on the coax or even on the metal pole. This would need to be carefully designed in simulation, and I've never tried it in this application.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12878/what-happens-to-a-vertical-yagi-when-you-mount-it-on-a-vertical-metal-pole, by Andrew, Mike Waters, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
