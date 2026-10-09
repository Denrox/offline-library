# What do radials really do for a vertical antenna?

*Tags: antenna, vertical-antenna, radial, physics · score 4*

## Question

I have read everything I can find about monopole (vertical antenna) radials, and also watched many YouTube videos that touch on the topic. I see conflicting information about what they do, where a particular article or video tends to fall into one of two camps:

1. Radials are used to increase the conductivity of the ground surrounding a vertical antenna, to aid in returning current efficiently to the transmitter.
2. Radials create a mirror-like reflection around the vertical antenna, which reflects radio waves that hit the ground off at an angle that simulates an "image antenna" beneath the surface, as though it were a vertical dipole instead of a monopole.

I can't find any resources that brings these 2 things together, so I'm left confused about how radials work from a physics standpoint.

How do radials work?

P.S. explanation #1 further confuses me because I'd expect that we don't want to "capture" the energy from the radiated signal and return it to the transmitter, since we want it to radiate! So if #1 turns out to be the true purpose of radials, I'd love to have that clarified as well.

Thank you!

EDIT: Anyone else who has this question, here's the best video I found that really gave me an "a hah" moment as to what's happening with the ground around a vertical antenna and why radials help (I recommend entire video, but I started it at the most relevant part):

https://youtu.be/XMxaYj7Xs5k?t=1169

## Answer (score 6, by hotpaw2)

Both #1 and #2 are the same.

Accelerating currents are what sum up to create an EM field. And the law of conservation of charge requires that the currents be balanced. If you have a quarter wave vertical over a vast and solid highly conductive ground plane, then whatever current you accelerate up the vertical from the feed point will be balanced by an equal amount of current on the ground plane accelerating towards the feed point from all directions (360 degrees, due to symmetry).

In the far field, the EM field generated from all those ground plane currents coming from all directions towards the feedpoint will just happen to sum up (integrate in calculus) to create exactly the same EM field as if there were a mirror image of the vertical below the ground plane, creating a virtual dipole. However, this mirror is an “as if”, the real currents will be on the ground plane, not some imaginary reflection that would (if it existed) just happen to produce the same EM result in the far field.

If you don’t use a vast number of radials over dirt, then the return currents end up coming to the feed point from, not on a conductive plane, but a through a vast resistive blob of dirt (the other half of the dipole fading out gradually to being some fraction of the entire planet) near to the antenna ground and/or transmitter ground. Resistive blobs convert some of the energy from any return currents into heat (warming up the planet by a near infinitesimal amount), thus leaving less energy to radiate as the EM field. Or if you are (un)lucky, some fraction of return current EM will radiate from the feedline. Thus radials over dirt or rock (or a solid metal ground under a mobile roof mount vertical, etc.) are desirable if you want to maximize efficiency of radiating an RF field perpendicular (or nearly so at a low launch angle) to the vertical.

## Answer (score 3, by user10489)

Radials do both, but reflect is the wrong word and the reasoning behind increasing conductivity misses the point.

A monopole vertical antenna is really still a dipole, except that the vertical portion of the antenna is only half of the dipole. The other half of the dipole must exist for the antenna to work correctly, but it can take many forms.

If the ground has a high conductivity, then the ground (as in dirt under the antenna) itself can act as the other half. (Water, especially salt water, would work better than dirt.) But even if the ground is high conductivity, it likely is not as high as metal wires, so placing ground radials around the base of the antenna will be more efficient, as there will be less loss resistance. Some efficiency is also lost if those radials are buried, but this may be small enough to not care. Also, the ground radials do not have to be horizontal -- in fact, they work better if they are at an angle below the vertical element. (This gives the antenna a more ideal radiation pattern.)

Typically, ground radials are attached to and part of the antenna. Antennas are typically fed with two wires (either parallel as in ladder line, or concentric, as in coax). One wire goes to the antenna vertical element, the other wire goes to the ground radials.

However, it is also possible to capacitively couple the ground to the antenna -- and this is how mag mount monopoles work, with the car body (or other large metal surface under the antenna) acting as part of the antenna.

Don't think of it as the antenna reflecting off the ground -- this is wrong. The ground is actually *part* of the antenna, and it radiates with the other half of the antenna. The shape of the ground also affects the shape of the radiation moving away from the antenna. So if your ground radials are not symmetrical, or the magmount antenna is not in the center of the car roof, it will skew the radiation pattern towards the directions where there is more metal.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18516/what-do-radials-really-do-for-a-vertical-antenna, by User5754448, hotpaw2, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
