# Erratic behavior on Baofeng UV-5R Plus

*Tags: rfi, baofeng, equipment-troubleshooting, uv-5r · score 3*

## Question

I bought a UV-5R Plus (8 watt radio in the same casing as a normal Baofeng), and I've noticed some strange behaviors.

Occasionally when I key up on my local repeater, the radio turns itself off and on again on its own.

In some conditions, the radio gives me painful shocks if I key up while touching one of two places: The negative battery terminal, and the little chunk of metal for attaching a strap. It feels like I'm touching a very hot surface, but the pieces of metal themselves aren't hot at all.

Now, for the biggest issue.

Sometimes I get random bursts of static coming through the radio for seemingly no reason. There are several strange things about this static that don't make sense:

- The static is present even if I detach the antenna
- The static is not affected by turning on a receive PL tone
- The static is not affected by changing the squelch filter. It sounds exactly the same whether squelch is all the way down or all the way up.
- The static usually happens in the same general areas in my house.
- The static also happens *outside* my house, even far away.
- It generally happens when I'm walking near houses, and it has happened so many times that I've memorized exactly where it happens. It's always in pretty much the same places.
- Sometimes when I'm outside and the radio is on the ground, it begins rapidly receiving bursts of static. There are about two per second and they last about a fraction of a second each.
- The static completely blocks out any received transmission - no signal can get through it
- I have experimentally walked into and out of one of these areas while transmitting. The person I was talking to told me there was no change in my transmission - clear the whole way through
- These "Static areas" vary in size, but they are usually between 3 and 8 feet (estimating).
- There is one in my bedroom near the wall, and it's about 2 feet. It has a *roughly* circular shape coming from the wall, and doesn't seem to be affected by radio height.
- There is one in my backyard that is fairly long. It is about 3 feet wide by roughly 10 feet long. It gets *considerably* worse the closer I get to the ground.
- I have occasionally found areas out in open fields, again roughly 3-8 feet and a somewhat circular shape.

Can anyone tell me what's going on?

EDIT: I thought I'd add, I have a 5W radio by a different company as well, and that radio is not affected by any of these issues. I also have a regular UV-5R, and it does not have any of these issues either.

Technical info:

- Radio: Baofeng UV-5R Plus
- Power: 8W
- Squelch: Doesn't matter
- Antenna: The long antenna that came with the radio
- Frequency: Doesn't seem to matter, maybe slightly worse in the 2m band because I'm using a 2m antenna.

## Answer (score 3, by rclocher3)

It seems to me that you have a bad radio, that is to say a radio with one or more faults in it. You shouldn't be getting the sensation of a shock or heat, and those are possible indications of a short. Direct shorts are sometimes easy to troubleshoot. The intermittent static issue could be an aspect of the same problem, or it could be an independent problem.

If it were my radio, and if it were still covered by the warranty, then I would return it and ask for a refund or a replacement. If it were my radio and it weren't covered by a warranty, then I would open it up and start troubleshooting by looking for shorts and intermittent connections. But I have electronics experience. Unfortunately this web site is not very conducive to talking someone through the troubleshooting of a device. You now have 20 reputation points, so you might try seeing if someone in the Ham Shack can help you troubleshoot, because back-and-forth discussions not strictly conforming to question or answer formats are fine there. But just taking a Baofeng apart is a bit risky; I took mine apart, and now there are a couple horizontal lines of pixels in the display that don't work any more.

I'm sorry that I can't give you a definitive account of what your problem is based on your description of the symptoms, but troubleshooting an electronic device is usually an iterative process that doesn't lend itself to nice neat answers before troubleshooting has even begun.

## Answer (score 2, by Jack0220)

I think you have a loose wire in there somewhere. It's probably the ground or center lead between antenna and amplifier. The bursts of static might be from the wire making contact or not, or contact with something else. Are the static circles repeatable or maybe it was a coincidence, maybe the way you are holding the radio, you can try holding it upside-down.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20013/erratic-behavior-on-baofeng-uv-5r-plus, by Proxy303, rclocher3, Jack0220. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
