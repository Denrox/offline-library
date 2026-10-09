# Are chokes necessary for VHF and higher frequencies?

*Tags: antenna-theory, vhf, uhf, mobile · score 3*

## Question

I am trying to install a VHF/UHF antenna on my truck, and I have been studying everything I need to do that. I keep reading about chokes, in particular here: http://www.k0bg.com/choke.html

However, everything I find talking about it is in reference to 10m band and lower frequencies. Is choking necessary for the 2/70 bands?

## Accepted answer (score 1, by Rowan Hawkins)

The article you reference has to do with protecting the controller in a screwdriver antenna. Which you don't have at VHF or UHF.

The purpose of a screwdriver antenna is to lengthen or shorten the element to match the wavelength of your transmission band. VHF and UHF transmission bands are each wider than a single HF band but not wider than all of the HF bands grouped together. At VHF and UHF frequencies the ideal antenna length between the ends of the band is not that great.

A feedline choke can be installed on any antenna but unless you are planning on driving a wire brush you're not going to get much induced current in your feed line.

You don't mention what type of antenna you have or where on the truck you are mounting it. However as the linked article in the comment explains you will be fully unbalanced. Mobile installation is almost always fully unbalanced.

Trucks have some suboptimal mounting locations. They are not worse than motorcycles however. Accessories that you might have for your truck will change the below information. Which is for a regular Pickup. The main things that impact the information below would be a ladder rack or a metal cover.

Best: If you are planning on through hole mounting to the center of your roof deck, the ground plane will be physically established where the connector comes through the roof. If you are just planning on the one antenna you should try to get it close to the center front back left right. This would be an effort to maximize the amount of ground plane around the antenna, and to minimize the amount of directivity that the shape of your ground plane will provide your signal.

Good: If you are using a magmount, the ground plane is parasitic back to the radio chassis mount. A similar mounting point to the one above should be chosen. Route the cable in such a way that water won't drip in and it won't get smashed by the door as often.

Okay: Stake hole mounts I don't have a great deal of experience with. If you use the holes close to the cab these run into the same issues as a trunk mount car antenna. The metal structure of the cab drastically interferes with your radiation pattern and your match. If you have a full size pickup the rear stake holes will be more than a wavelength from the cab at 2m however you will still get Reflections from it.

## Answer (score 2, by Glenn W9IQ)

Choking baluns are not typically used on VHF and UHF antenna systems in a vehicle.

Part of the reason is that the ground plane formed by the roof or trunk of the vehicle is quite effective in isolating the feedline from common mode currents (the currents that a choking balun is trying to reduce or eliminate) at VHF and UHF frequencies.

If you did try to build one from coiled coax or a parallel transmission line wrapped around a torroid, you would find that the strays at those frequencies would significantly limit their effectiveness. With careful attention to details, you could probably tune one to be effective but this is beyond the resources of the typical ham.

So I recommend carrying on without one just like the rest of us do.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7451/are-chokes-necessary-for-vhf-and-higher-frequencies, by SandPiper, Rowan Hawkins, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
