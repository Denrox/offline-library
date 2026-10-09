# Is the Boom Strictly Necessary in a Vertical Dipole?

*Tags: antenna-construction, diy, vhf, vertical-antenna · score 4*

## Question

I'm planning to build a vertical dipole for 4m and a club member pointed out that my design needs to allow for a boom that should be at least a 1/4 wave long. Why does a vertical dipole need a boom that offsets the radiating elements from the mount? I'm guessing it has something to do with the interaction between the feed (coax) and the elements? Can the boom length be shortened by using a balun (choke)?

Thanks in advance for your advice!

Image taken from here

## Answer (score 5, by hotpaw2)

If you don't route the feed line away from a center-fed dipole antenna at 90 degrees, it will be in an unbalanced RF field, and thus will couple to the unbalanced RF field, to some degree, even with a perfect (infinite impedance) balun.

Depending on the distance and angle of feed, an RF coupled feed line can act like an angled antenna director or reflector element and distort the antenna pattern, perhaps sending it off at some undesired angle. (or perhaps, if you are really lucky, or design for this pattern, adds gain to your desired direction).

A bazooka balun will reduce direct electrical coupling, but the high voltage RF field near the dipole tip will still couple to the feedline shield at some distance away from the balun. You can simulate this by putting an unconnected wire next the nearby feed line, using something like the NEC antenna modeling software. Or hold an RF meter up against this unconnected wire. At certain distances and lengths, a completely disconnected coax shield will pick up plenty of RF voltage if not closer to 90 degrees from dipole center.

## Answer (score 3, by webmarc)

You're right, the concern is coupling the feedline with the element.

But there's a neat trick: if your bottom element is a tube of large enough diameter to accommodate your coax, you can run the coax *thru* the bottom element... and now you don't need a boom.

Additionally, the bottom element will then act as a sleeve/bazooka balun.

You'll still need to insulate the antenna from the mast of course, but that can be accomplished with an appropriate PVC coupler.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17178/is-the-boom-strictly-necessary-in-a-vertical-dipole, by Buck8pe, hotpaw2, webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
