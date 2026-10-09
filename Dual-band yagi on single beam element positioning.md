# Dual-band yagi on single beam: element positioning

*Tags: antenna-construction, yagi · score 3*

## Question

I'm planning to build the WA5JVB Cheap LEO Yagi, which is basically a 2M and a 70cm yagi on the same beam for handheld or tripod use. I'm thinking to do a 3-element 2M and a 5-element 70cm design, and I'd like to make the entire thing no more than 36" long. Each antenna is individually ~20", which obviously won't fit in 36". Can I place the director of the 2M antenna ahead of some of the elements of the 440? Ideally, this would be between D1 and D2 on the smaller yagi.

I'm not sure how much impact the variously sized pieces of metal would have on each other, my biggest concern is that the 2M director would act as a reflector in front of the 70cm driven element. If this isn't possible, I'll probably just build the 2 + 5 pictured to keep it portable.

## Accepted answer (score 2, by tomnexus)

You can't just mix the antennas together without doing a lot of work in simulation to make all the interaction work properly.

As you suspected, the longer 2m elements will upset the 70cm antenna.

However, as they are completely separate antennas on the same boom, if you tilt one so they are 90 degrees apart, they will not interact at all, and you can squeeze them onto a shorter boom. In other words, looking from the front, they form a cross. This won't be as easy to handle or store, so you might want to find a way to fold the elements of the 2m antenna. Make sure that no elements touch or get too close. Keep the baluns apart too, perhaps one forward and one backward.

Simulating antennas is fun, but it's a long journey, quite a lot of work for one yagi. The easy-to-use packages cost more than a car, and the free ones are harder to learn. My advice is to start with a published design from a reputable source and build it carefully.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3546/dual-band-yagi-on-single-beam-element-positioning, by David KF4MDV, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
