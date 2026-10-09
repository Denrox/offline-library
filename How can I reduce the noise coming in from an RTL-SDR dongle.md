# How can I reduce the noise coming in from an RTL-SDR dongle?

*Tags: rfi, rtl-sdr · score 9*

## Question

I've recently received an RTL-SDR dongle, and I'm picking up a lot of noise that is probably coming from my PC, especially a lot of "spikes" on the 2M band. I've already started using a USB extension cable instead of plugging the dongle into the PC. What else can I do to reduce the noise floor and get rid of the RFI on 2 meters?

## Accepted answer (score 8, by Kevin Reid AG6YO)

Here is an assortment of common ideas and recommendations for RTL-SDR devices:


**Mount the device directly on your antenna, or otherwise minimize the amount of feed line used.** (This does not directly remove noise but rather increases signal, but that's just as good if not better. It may also remove noise by moving the device further from your computer equipment.) Of course, if your antenna is outdoors you will need a weatherproof enclosure, and you must make sure the USB line meets USB specs despite its increased length (such as by using an *active extension cable* designed for the purpose).


Make sure you have the **RF gain set correctly**!


Too little gain will bury real signals in the noise floor; turn it up until you see the noise floor rising a bit so that [you're seeing the noise from the antenna](What%20is%20the%20relationship%20between%20SWR%20and%20receive%20performance.md).


Too much gain will overload and produce duplicated signals across the spectrum; turn it down until those extra spikes go away.

I have found that the built-in AGC may err in the direction of too much gain.


Build a **shielded enclosure around the device**; they come in plastic cases with no RF shielding at all.


**Add snap-on ferrite beads** near the ends of cables, if they didn't come with built-in ferrites.


An RTL-SDR-specific suggestion I have frequently heard is to modify a USB extension cable by removing the shield at the female-A end. (One could also modify the device's male-A plug but that might interfere with the mechanical connection.)

The argument given is that the ground and shield are tied together on the PCB, and by disconnecting the USB cable shield from the ground you prevent noise carried on the outside of the shield from entering the RF section's ground.

I have not yet tried this modification myself, and a few comments here suggest it is not worthwhile.

## Answer (score 3)

I've just mounted mine in an eddy stone box. I put a BNC on the end and swapped the USB plug for a socket and made a hole in the box to fit the cable from a USB extension. Works a treat, rugged, mobile and no noise. 73

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1174/how-can-i-reduce-the-noise-coming-in-from-an-rtl-sdr-dongle, by krzysz00 KF5SOQ, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
