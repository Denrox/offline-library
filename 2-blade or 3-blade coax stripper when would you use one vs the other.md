# 2-blade or 3-blade coax stripper: when would you use one vs the other?

*Tags: coaxial-cable · score 4*

## Question

I've been looking for a RG8x/LMR240 coax strippers and found that they come in both 2-blade and 3-blade models. So far I haven't found a reason to use one over the other.

I did notice that the 3-blade version does not list rg8x specifically (only RG58/59/6), but the 2-blade model lists many cables with similar dimensions including those supported by the 3-blade version (RG-58/59/6/8X/Mini-8/LMR-240). So what is the best practice here?

**Questions:**

1. When would you use 2-blade vs 3-blade?
2. What are the benefits of one over the other?

## Accepted answer (score 2, by natevw - AF7TB)

I suspect this has everything to do with how you will be terminating the coax.

I use a 2-blade model for some SMA fittings which slide around just the dielectic and have a ferrule that the crimps onto the full length of outer shielding conductor material. With the way the part is designed there's no risk of the shield shorting to the pin.

But when soldering a something like an UHF connector or maybe just a different style of any plug, you might need the outer conductor braid trimmed back a little further from the exposed center pin? For example the connector at https://www.americanradiosupply.com/ars-g505-rg8x-pl-259-uhf-male-coaxial-connector-for-rg-8x-coax-cable/ has a "recommended cable stripping dims." with the outer shield trimmed back farther than the dielectric.

Basically if it's helpful to have a coax cable dressed out like the 3-blade version pictures show, you would use that, but if the prep should end up like the picture on the 2-blade version then use that :-D

Probably the difference comes when the center conductor needs to protrude farther into the assembly. My SMA connectors come with center pins which extend all the way back such that the shield aligns perfectly with the outside, whereas that with that UHF connector the center conductor and dielectric itself gets pushed farther in and so there'd be too much extra shield spilling out of the ferrule if it weren't trimmed back to compensate. (Hopefully someone with more coax preparation experience can weigh in more authoritatively!)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21536/2-blade-or-3-blade-coax-stripper-when-would-you-use-one-vs-the-other, by KJ7LNW, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
