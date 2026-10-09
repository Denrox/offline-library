# Is it practical to use a slug-tuned variable inductor in an antenna matcher (aka "antenna tuner")?

*Tags: diy, electronics, antenna-system · score 7*

## Question

I will soon need an antenna impedance match (aka "antenna tuner"), because I'll initially only have a single antenna for my HF rig (needs to cover 80m, 40m, 20m, 15m, and 10m). Obviously, in order to manage SWR, I'll need a matching network, quite likely with a wider capability than the pi network built into my Heathkit SB-102. Even if the SB-102 can manage without help, I'll also need to match my portable antenna to my portable QRP rigs.

One of the core components of any matching network -- L, T, SCS, or pi -- is a "variable" inductor. Home builders seemingly usually use a tapped coil for this, giving discrete increments of inductance and depending on a variable capacitance to finalize the match.

However, variable caps are getting harder to find; they're no longer manufactured in the old "interleaved plates, air spaced" form, and the tiny plastic dielectric ones that are still available can't take much voltage (and are difficult to adjust precisely).

It occurred to me that what's needed is to adjust the *ratio* of inductance to capacitance, not either one in particular; if one had an inductor with stepless adjustment over a wide range of value, one might be able to use common fixed capacitors, or possibly a switch-selected gang of parallel fixed capacitors.

Now, adjustable inductors have been around for decades; aligning an old superheterodyne receiver involves tweaking up to a couple dozen components, of which roughly half are slug-tuned variable inductors. I recall from studying for my license exam that a ferrite or iron slug will increase inductance when inserted into a coil, while a brass (or presumably copper or aluminum -- conductive but non-magnetic) slug decreases it.

What wasn't covered in the study materials is how widely one can adjust the inductance with slugs. Common variable capacitors out of old radio or TV tuners run from zero to several hundred picoFarad, and a tapped coil can likewise run near zero inductance when tapped down to two or three turns. What sort of range could I get with, say, a tuning slug that's iron on one end, brass on the other?

## Accepted answer (score 4, by Marcus Müller)

What wasn't covered in the study materials is how widely one can adjust the inductance with slugs. Common variable capacitors out of old radio or TV tuners run from zero to several hundred picoFarad, and a tapped coil can likewise run near zero inductance when tapped down to two or three turns. What sort of range could I get with, say, a tuning slug that's iron on one end, brass on the other?

The inductivity of a coil is very much dominated by the magnetic permeability of its core – use a core with a twice as high a permeability, get (pretty much) twice the inductivity. A ferrite core can have a permeability a couple thousand times higher than that of air. So, by inserting a core into an otherwise air-core coil, you could achieve that factor of variability.

Problem: Cores tend to saturate in strong fields. You'll have to dimension the core such that saturation does not occur at the powers you plan to use. That can be large, challenging and hence expensive!

## Answer (score 5, by Brian K1LI)

...variable caps are ... no longer manufactured in the old "interleaved plates, air spaced" form, and the tiny plastic dielectric ones that are still available can't take much voltage (and are difficult to adjust precisely).

Thankfully, Oren Elliott is a surprisingly affordable source of brand new air-variable capacitors. I have used them successfully in several projects.

## Answer (score 5, by Brian K1LI)

Fair-Rite makes ferrite rods which would be suitable for HF applications. It should be possible to create or repurpose a screw-operated mechanism to move the rod into and out of a cylindrical coil.

Preferably, the material will have steady permeability and low loss over the frequency range of interest. Loss is proportional to the ratio of the real and imaginary components of permeability, $\frac{\mu'}{\mu''}$.

The properties of Material 61 are probably best, because:

1. $\mu'$ doesn't begin to drop off until past 30MHz
2. $\mu''$ is relatively low and doesn't rise significantly until 20MHz

The relative permeability of a wound rod depends on the ratio of the rod's length to its diameter:

So you will have to make some preliminary calculations before deciding on turns count for rods using Material 61.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14505/is-it-practical-to-use-a-slug-tuned-variable-inductor-in-an-antenna-matcher-ak, by Zeiss Ikon, Marcus Müller, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
