# Wider wire = picks up more energy, yah?

*Tags: antenna-construction, antenna-theory, wire-antenna · score 8*

## Question

I have seen many discussions re: wire gauge, insulation, velocity factor and K-factor...unfortunately, statements from various sources are not always in agreement, but that is not the issue. The issue that I have never heard discussed seems like a simple matter but ??

**Here it is:** A wider wire, let's say *really* wide (**4/0**) is being hit with more energy than a thin wire, is it not? A square foot of anything is exposed to one half the sunlight/energy that a two square foot anything is, when both are in sunlight.

I have some solid copper #4 AWG (*and 6, 10, 12, and 14*) and I have some 2/0 and some 4/0 (~1/2") stranded insulated aluminum wire. The question concerns a 14 foot, eight-element quagi that I want to build and I'm thinking that the **4/0 for the 'quads'** and **#4 for the directors** should pick up way more energy than all wire being #12, for instance.

I don't see folks writing about that anywhere which makes me wonder just how nutz is this?  
This site is a vast repository of knowledge and I thank in advance all who want to answer/comment.

## Accepted answer (score 2, by Kevin Reid AG6YO)

A wider wire, let's say really wide (4/0) is being hit with more energy than a thin wire, is it not? A square foot of anything is exposed to one half the sunlight/energy that a two square foot anything is, when both are in sunlight.

Sunlight has **extremely small wavelengths**, several orders of magnitude less than (to use the distance you mentioned) a foot. This means that the interactions of any given portion of the light with a solar panel (or even an ordinary dark object getting heated) occur in very small areas of the material, so if you analyze it as if it were an antenna, it's more like an array of tiny antennas than a bigger-in-some-dimension single antenna.

In the case of a radio wave interacting with a dipole antenna, for example (not that far from the case of your quagi), **the entire antenna is built around half-wavelength dimensions.** The area of the incoming electromagnetic wavefront that this antenna is interacting with is *not* the length and thickness of the wire, it is more like a circle whose diameter is the antenna length. (Reality is much more complex than this; there are no simple geometric shapes, but this will do for now.) Thus, making the wire thicker does not gather significantly more energy.

The analogy to making your solar panel two square feet instead of one is making two identical antennas, not too close to each other and connecting them in parallel. This is not a perfect analogy, because solar cells (and heating) are treating the radiation as *non-coherent*, meaning the phase of the signal is discarded and only the amplitude is kept. For coherent reception, as used in radio communications, the math works out that any such array of antennas or any other means of gathering more energy makes the antenna *more directional.* That's why we measure both properties as a single value, the “gain” of the antenna.

You can in theory gather more energy from a radio signal without increasing directionality, by using multiple antennas and multiple *receivers* as well — by independently demodulating from each antenna you avoid the signals cancelling each other. Imagine building lots of crystal radios and combining all their weak audio outputs into one stronger one. When the goal is actually to gather electric power from the RF field (in which case all you need is the diode rectification, no filtering or audio transducer), this is called a **rectenna** and it can be built into an arbitrarily large array just like a solar panel.

## Answer (score 9, by DonkeyOaty)

In short, no.

In long, it's really complicated. The wider your wire, the wider the bandwidth, due to the increase in available paths. Wide multi-strand wire does better against skin effect (more conductive area).

But, the "more exposed area" doesn't work here. You are picking up the E-field with this kind of antenna, so it's the voltages out on the tips that is important, not the cross section of current carrying in terms of the "amount you pick up". Does that make sense?

## Answer (score 4, by Phil Frost - W8II)

As other answers have explained, radio waves, being of a much longer wavelength than visible light, don't "hit" the wire in that way.

However there is a way to measure the size of the target the radio waves are hitting: *effective aperture* ($A_{eff}$). It's just another way of specifying gain ($G$) and wavelength ($\lambda$):

$$ G {\lambda ^{2} \over 4\pi} = A_{eff} $$

So if you have an antenna for 10 meters with a gain of 2 (3 dBi), then the "target" for the radio energy is:

$$ 2 {(10\:\mathrm m)^2 \over 4\pi} = 16\:\mathrm m^2$$

Sixteen square meters. You can use whatever wire thickness you want, but as long as the gain of the antenna is 3 dB the effective aperture does not change.

In case you are wondering, wire thickness in dipoles has no significant effect on gain.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6784/wider-wire-picks-up-more-energy-yah, by Mein Tenah, Kevin Reid AG6YO, DonkeyOaty, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
