# Does iron ore in the ground affect my signal?

*Tags: propagation, earth · score 11*

## Question

Mineral content in the ground varies from one place to another. I've visited places where the ground & waters were an orange-red shade from the high iron content; not good for trees either.

This post on eHam.net, seems to indicate there may be propagation issues with high iron-ore content in the soil/environs

The iron content of the under lying iron deposits were not conducive for good communications. Many dead spots. The local iron deposits are on the high ground. I experienced hf and vhf deficiencies.

The same was echoed elsewhere (pdf) about RF propagation in the Adirondack Upland, and also in the context of WWII Market Garden, and the WWII Philippines campaigns.

Anyway, say in the future I want to operate from a location where the ground is rich in iron ore.

- Does iron ore in the ground affect my signal?
- Assuming a fixed location, what can I do to mitigate the effect?

## Answer (score 12, by Dan KD2EE)

If anything, living in an area with high metal deposits near to the ground will improve your conditions by improving the conductivity of your ground. That said, unless it's very near to the surface and high concentration, I doubt you'd notice any difference.

Note that when we model the ground as an ideal ground plane, anything underground has no impact on the signal at all - it is shielded. Of course our real ground isn't perfect, but metal deposits can only improve that, if they have any effect at all.

## Answer (score 3, by tomnexus)

Probably not much effect from iron in the ground.

HF communications are very sensitive to the ionosphere and other natural effects. Predictions are difficult, and only give a probability, never a guarantee. Real data are thin on the ground, and you know that the plural of anecdote is not data.

HF propagation happens mostly in the air, and by reflection off the ionosphere. The ground only gets involved at the antenna, and possibly if you are using ground wave propagation. Ground wave is more an MF thing, AM radio etc, above a few MHz it is only good for a few km.

The radiation pattern and efficiency of an antenna are affected by the ground constants, and the low-angle radiation, so important for long range HF, is particularly sensitive. No matter how far the signal will travel, the only ground that counts is the patch around each antenna. The size of the patch varies, but it's generally only some wavelengths in radius. In reasonable ground, all the RF conduction happens in the first few metres, so don't worry about what is being mined far below.

The two ground parameters, conductivity and permittivity, vary widely between locations, but in general, the "richer" the soil, the "better" the ground. So fertile farmland is much better than a desert. This effect is well studied.

The richness of the ground depends on its water content, the geological type of rock etc, and the minerals. Most ground is of course silicon dioxide, sand, which is an insulator. The size of the grains, and the other minerals, are what change its performance.

Iron oxide is not conductive, so along with the SiO2, AlO2 etc, would make up the inert part of the ground. Salts and water dominate that conductive parts of the ground.

To study this further, try to investigate the effect of various minerals on the ground permittivity and conductivity. This is where the hard data lies. Stories about good and bad reception, or even careful measurements of "how good the signals are", have too many confounding factors, and are not going to lead to useful conclusions.

## Answer (score 3, by John Rowlands)

Well, I operate daily from an old copper mine - where the main mineral is iron!

The comment about iron oxide are not correct. In places such as here, and where the OP mentions, the ground is highly acidic. Consequently, iron is in the FE2+ (ferric) state, not the FE3+ (ferrous/rust) state. This may or may not affect conductivity. You will have to consult a number of detailed academic papers on that, probably none of which are in the context of RF operations.

When one comes across 'red water' (pH above 4, and so iron in the precipitatable, Fe3+ state), then you know you are likely in an area with lots of different types of mineralisation. Picking out the role of each, and when geological layering and water in and through these is present, is a task that quickly leads to madness!

Are you better off with highly conductive ground under your antenna? Yes!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/425/does-iron-ore-in-the-ground-affect-my-signal, by VU2NHW, Dan KD2EE, tomnexus, John Rowlands. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
