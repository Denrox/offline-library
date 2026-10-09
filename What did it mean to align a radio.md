# What did it mean to "align" a radio?

*Tags: history, maintenance · score 9*

## Question

I've heard older hams talk about "aligning" their equipment. E.g. "I sent it to a guy for alignment" or "that rig probably needs to be completely aligned before you use it".

As a kid, sometimes I remember broadcast AM/FM receiver dial indicators would get "stuck" and you'd have to fuss with the knob, like crank it all the way one direction for a while, to get it to properly line up with the rough tuning labels again.

Is "alignment" basically that only on a more precise VFO indicator? Or does it involve more tuning elsewhere, say re-adjusting to factory biases via trimpots? Or is it not really a physical adjustment thing at all, more like checking capacitors or replacing tubes?

## Answer (score 4, by hobbs - KC2G)

It's more complicated than that. *One of the things* you do in an alignment is like what you describe, making sure that all of the fixed and adjustable frequencies inside the rig are correct and agree with what's on the dials. This might involve mechanical or electrical adjustment. But in addition to that you do things like

- Adjusting the tuned filters for different IF stages to make sure that they have the maximum response in the places where the signal ought to be
- Adjusting band pre-select filters to make sure that they admit as much of the desired band as possible, with a minimum of everything else
- Adjusting the gains and biases of various amplifiers so that they're operating in the ideal range, where they will pick up weak signals, but without saturating or distorting on strong signals
- Making sure that the receive and transmit sides of a transceiver are in good agreement, and the RIT offset is really 0 when that knob is at 0.

If you have some time, I recommend this Mr. Carlson's Lab video for a pretty detailed rundown of aligning a receiver; a few of his other restorations involve similar tuning-up.

## Answer (score 4, by Zeiss Ikon)

The process of alignment involves optimizing the settings of variable inductors and/or trimmer capacitors in the set to maximize sensitivity and selectivity. It usually involves feeding the set a series of precise signals and adjusting particular components, in sequence, in each case to maximize output volume or voltage at a particular test point.

This was mostly a procedure of the vacuum tube era, though solid state sets (even pocket transistor radios) could also be aligned. Once set, however, only extreme conditions or a goodly number of years of operation (resulting, in either case, in value drift of components like capacitors and resistors) would generally require realignment. One exception to this is that replacing a tube in a vacuum tube set might change some value (dependent on the replaced tube) enough that realignment would be of value.

There are at least a couple YouTube videos that show the process (with a little compression, not to see all, in that case, 23 adjustments required) -- in one of them, the operator has to use an alternative alignment frequency to work around a very strong local AM broadcast station close to the recommended one.

## Answer (score 2, by Mike Waters)

Alignment usually means to turn various built-in adjustable components to put the equipment back to factory specs. This is necessary because as some electronic components age, they change in value over time. That can and does cause reduced performance of the radio.

There are two basic types of alignment. This is kind of tongue-in-cheek, but bear with me. ;-)

1. Adjusting the adjustable adjustments
2. Adjusting the non-adjustable "adjustments".

The "adjustable adjustments" are built-in adjustable components, such as:

- Trim pots (variable resistors)
- Variable capacitors
- Variable inductors

These are found on IF cans (containing transformers).

"Non-adjustable" adjustments are necessary when a component has drifted out of specs, and the technician must add a component in series or parallel with it. For example, I had to trim the BFO crystals in my Collins S-Line back to spec by adding a capacitor in parallel or in series with the crystal.

The mechanical adjustment of the pointer *could* also be considered as alignment as well, I suppose; but that's not what is usually meant. A blind person would likely not be affected by that.

There's more that could be said, but basically, that is what it means to align a radio. I have done this many times over the years.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13271/what-did-it-mean-to-align-a-radio, by natevw - AF7TB, hobbs - KC2G, Zeiss Ikon, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
