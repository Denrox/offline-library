# Turn 75 Ω TV "Rabbit Ears" with a balun into a 50 Ω dipole antenna

*Tags: antenna, uhf, dipole, balun · score 3*

## Question

I got myself a TV "Rabbit Ears" module originally for a TV. It came with a small length of coax, permanently attached to the antenna foot, and a Belling-Lee connector on the other end.

My idea was to use an RG-58 coax with an SMA plug with this antenna, because it is easy to make a handle for it, and it's easy to store.

Inside the mounting point for the two telescopic antennas, there is a ferrite core, with a couple loops around it, going off to the two telescopic antennas:

In the schematic, (a) is four turns, (c) and (d) are two turns, each. As I said it's a dual-ferrite core, so two holes in one block of ferrite *(ignore the center tap on the (a) side, I couldn't find a transformer symbol with one inductor on one side, and two disjunct inductors on the other, with a core)*.

I also made a couple of pictures:

They *are* rather shoddily soldered together, and while handling the center core wire broke off from the solder point:

As you can see in the pictures above, then it's one ferrite block with two holes in it. A wire running from core to shield of the coax goes through both holes, looping four times. Then, each from the core and the shield a wire loops through either hole, twice and then connects to either of the two telescopic antennas, which I have removed, so handling is a bit easier.

Since this is a TV UHF antenna, this has to be 75 Ω, but I'm wondering how I should now modify the balun, such that the impedance is 50 Ω.

My first approach was to remove the balun altogether, and directly solder a length of 50 Ω RG-58 to either of the antenna solder points and that'll be it. But I'm not entirely sure that would be a good approach, since I believe the balun is here for a reason...

Instead of coming up with just a number of turns, it would be nice, if someone could provide a formula how to calculate these, or a place where I can find further information.

**UPDATE:** I think I've found the device that was wired up in my antenna in blog post *Make a wideband antenna matching transformer*.

So, it's a 4:1 balun, with 75 Ω on the coax-side. This means the antenna has an impedance of 300 Ω. 300 Ω for a dipole? It sounds strange to me, but I don't know.

Assuming this *is* a 300 Ω antenna, I'd need a 6:1 transformer / balun to match it up with 50 Ω. The closest I can practically wire up is a 2 and 5 turns transformer, resulting in a 6.25:1 transformer. I'm not sure that would be even usable. The closest match without going into crazy figures is 49 and 20 turns, resulting in 6.0025:1, which I think would be close enough.

I don't think I have a way of finding out the exact impedance of my rabbit ears antenna, so I guess I just have to assume it's 300Ω going by the fact how the balun / transformer was wired up, etc.

## Accepted answer (score 3, by Glenn W9IQ)

The feedpoint impedance of the rabbit ears antenna will be 72 ohms or less. It is basically a dipole antenna with shortened legs and potentially orientated in a Vee configuration. So with 50 ohm coax, attempting to exactly match impedance is a frivolous exercise.

Any notion of the balun correcting SWR is ill conceived. In a receive configuration, the SWR is established by the relationship of the receiver input impedance and the Zo of the feedline. The antenna is the signal source. Any mismatch between the receiver and the feedline will cause the impedance of the transmission line at the antenna end to be transformed. If this transformed impedance is not a match for the feedpoint impedance of the antenna, the antenna will not transfer its maximum received power to the feedline causing it to re-radiate some of the power. Given the potentially wide variation of the antenna impedance, matching the two impedances through a matching device is not warranted. A more practical approach is realized by simply adjusting the antenna length and configuration for the best received signal.

A properly constructed balun will minimize common mode currents on the coax but with a compromise antenna such as rabbit ears, concern about common mode currents is not warranted.

My advice would be to simply connect the 50 ohm coax directly to the rabbit ears and make the best of it.

The balun as pictured appears to be a transmission line transformer, probably a 4:1 configuration. Such devices do not work on the basis of turns ratios like more typical transformers.

## Answer (score 4, by Phil Frost - W8II)

A little impedance mismatch on the receiver is not a big deal. 75 to 50 ohms is an SWR of 1.5:1. For most applications, anything under 1.6:1 is considered a "good match". For a receive-only application, [the match is even less critical](What%20is%20the%20relationship%20between%20SWR%20and%20receive%20performance.md).

Besides, the impedance of the antenna is going to vary with its surroundings and how the ears are oriented.

And, you've said you don't have an antenna analyzer to accurately measure the impedance.

Given all this, little is to be gained by improving the match, and between environmental variation and the lack of equipment to measure it, any attempt you would make at improving the match would lack sufficient precision to make the difference between 50 and 75 ohms relevant in comparison.

If I were in your situation, I'd just repair the solder joint and perhaps put a different connector on it. It will work fine.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9897/turn-75-o-tv-rabbit-ears-with-a-balun-into-a-50-o-dipole-antenna, by polemon, Glenn W9IQ, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
