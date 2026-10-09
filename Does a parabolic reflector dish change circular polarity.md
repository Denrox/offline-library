# Does a parabolic reflector dish change circular polarity?

*Tags: antenna-theory, circular-polarization, reflector · score 5*

## Question

I've been receiving satellite signals in the L-band (~1.7GHz), recently.

These signals are RHCP. So far, I've been using a DIY helical antenna in axial mode, and a patch antenna with cropped or clipped corners.

My favorite tool to calculate the latter, is btw. this: http://kempbros.github.io/antennas/Patch_Antenna_Generator/

Anyway, when a signal is RHCP, I need an RHCP antenna to receive it, that's quite logical, and I can visualise in my head, how the propagation works, etc.

But now I'd like to use a dish as a reflector, but as I imagine things, the reflector works like a mirror, and will change the polarity of the circular polarized signal. So to receive a RHCP signal with a parabolic dish antenna (receiving element pointed at the dish, similar to how the LNB is mounted on a Ku-band antenna for satellite TV), I'd need a LHCP antenna in the focal point of the dish.

At least that's how I understand it, but like I said, at this point I'm super confused.

## Accepted answer (score 9, by Brian K1LI)

A parabolic reflector reverses the sense of circular polarization. so your feed must have the opposite sense or "handedness" to the incoming signal to avoid significant polarization loss.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12083/does-a-parabolic-reflector-dish-change-circular-polarity, by polemon, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
