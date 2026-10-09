# Why does adding 50-ohm BNC Ethernet terminator(s) in parallel to my 4-element yagi improve my radio's reception? (70cm)

*Tags: antenna, receiver, antenna-system, path-loss, dummy-load · score 6*

## Question

I have this radio, with a rubber duck antenna, and a repeater twenty miles away to my north-northwest. If I set my radio on the top of a cabinet in my bathroom, I receive the repeater fine. I can't hit it from there, but I can hear it, which for now is good enough. I can't receive that repeater anywhere else in the house, though, on that antenna. My house is off-grade, so my floor is about three feet above the dirt below. Therefore, on the bathroom cabinet, it's around ten feet above ground.

I have also a 4-element yagi. Currently, I have it on a makeshift 3/4-inch PVC mast shoved into a 5-gallon Firehouse Subs pickle bucket with a hole in the lid sitting beside my recliner in the den. Keep laughing, but it works. So, this thing is pointed pretty much right at that repeater, a foot from my ceiling, so about the same altitude as the rubber duck in the bathroom, and nothing. I get bupkis. But wait...

I take the antenna off of the radio, and put on the radio a BNC tee. On one side of the tee, I put my antenna. On the other side, I put another tee, which itself has a BNC 50-ohm Ethernet terminator on each side (scavenged from work's trash, old Thinnet cabling being tossed). So, the antenna, and two BNC Ethernet terminators (dummy loads?) in parallel, and wouldn't you know it, I can now receive that repeater with almost zero static.

So I'm confused by this. ADDING load to the line IMPROVES reception?

The whole story is a lot more drawn out, and it's odd how I actually came to discover this phenomenon that seemingly improves reception (originally I had about eight of these tees all daisy-chained off of one another, just screwing around), but when I asked my father about it, he suggests that the antenna has such a high gain that it overpowers -- and desensitizes -- the receiver in my radio.

I trust my father, but does this sound feasible? Why would I then not just be able to aim my antenna slightly off target and pick up the repeater equally well (or better)?

## Accepted answer (score 2, by mrog)

A four element yagi shouldn't overload your receiver unless you're very close to the transmitter. If you were close enough for that to be an issue, your rubber duck antenna would work just fine.

When you added the tee to the cable, you created a quarter wave stub trap that would filter out certain frequencies. It would probably work even better if you shorted the ends instead of using resistors.

Those tee connectors aren't that big, so I'm betting your problem is from interference that's somewhere around the microwave part of the spectrum.

Maybe a different radio with better built-in filters would work better. But, if you have a solution that already works, you may want to stick with it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13065/why-does-adding-50-ohm-bnc-ethernet-terminator-s-in-parallel-to-my-4-element-y, by CJ KE4EDD, mrog. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
