# Will a HF beam antenna on rooftop building interfere with other antennas there

*Tags: antenna, antenna-theory, rfi, antenna-system, yagi · score 5*

## Question

I am moving into an apartment on the top floor of a building and I intend to install a HF beam antenna for 20 to 10 meters, on the rooftop of the building.

I notice that there are already some antennas installed there on the rooftop. Possibly TV antennas and dish-like antennas for reception just. The question is, would my HF beam antenna interfere with these antennas if it is mounted close. Would it even be permitted normally?

I intend to use a 6-band HexBeam with 100% from 20M to 10M. The antenna would be mounted about 35 - 40 feet from the other antennas on the other side of the building.

Edited : Photo added for reference :

## Answer (score 3, by Jack0220)

Of course there can be interference but I would guesstimate the probability at about 30%, so that 70% chance that there will be no interference - basically have to try to find out. If there is interference you can move the antenna a little bit and that might even fix it or install a filter that might fix it, or use less power on certain frequencies. I would think that most of those other antennas are for different frequencies, that will be a big barrier against interference (because of filters and such).

## Answer (score 3, by user10489)

The likelihood of an antenna interfering with another antenna diminishes as their respective frequencies get further apart. Typically, if they are on different non-harmonic bands, it won't be an issue, and if they are harmonic, the higher frequency antenna might cause interference on the lower frequency antenna, not the reverse.

Dishes are probably above 400MHz, likely above 1GHz. (The usefulness of a dish diminishes if the diameter is <1 WL.) The lowest possible TV antenna might be 54MHz, but this depends on your country to some extent, and a lot of the lower bands have been phased out for TV use.

So it is unlikely your HF antenna will interfere with other commercial band antennas on the roof.

Having said that, if you put out enough power, it might be possible to give other electronics supporting those antennas front end overload. If this does turn out to be a problem, better grounding and shielding of those electronics might help, but you'd have to have cooperation to get that done. Being a beam might actually help, because unless a high power lobe of the beam is unfortunately aimed at something that can be overloaded, likely the side lobe power would be low enough to not cause problems.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19980/will-a-hf-beam-antenna-on-rooftop-building-interfere-with-other-antennas-there, by Engineer999, Jack0220, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
